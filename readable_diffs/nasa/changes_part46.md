# Change History for nasa.json (Part 46)

### Changes from 31606f9 to dd2190f (Part 35/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
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
+            "identifier": "C1331182628-LARC",
+            "issued": "2015-08-27",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry",
+                "atmospheric temperature",
+                "air quality",
+                "clouds"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2FORNS_L2.007",
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
+            "title": "TES/Aura L2 Formic Acid Nadir Special Observation V007"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MCD43C3.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang. 2021-02-22. MCD43C3.061. MODIS/Terra+Aqua BRDF/Albedo Albedo Daily L3 Global 0.05Deg CMG V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MCD43C3.061. https://doi.org/10.5067/MODIS/MCD43C3.061. The DOI landing page provides citations in APA and Chicago styles..",
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
-            "identifier": "C2532068039-LPCLOUD",
-            "description": "The Moderate Resolution Imaging Spectroradiometer (MODIS) MCD43C3 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) Albedo dataset is produced daily using 16 days of Terra and Aqua MODIS data in a 0.05 degree (5,600 meters at the equator) Climate Modeling Grid (CMG). Data are temporally weighted to the ninth day of the retrieval period which is reflected in the Julian date in the file name. This CMG product covers the entire globe for use in climate simulation models. \r\n\r\nMCD43C3 provides black-sky albedo (directional hemispherical reflectance) and white-sky albedo (bihemispherical reflectance) at local solar noon. Black-sky albedo and white-sky albedo values are available as a separate layer for MODIS spectral bands 1 through 7 as well as the visible, near infrared (NIR), and shortwave bands. Along with the 20 albedo layers are ancillary layers for quality, local solar noon, percent finer resolution inputs, snow cover, and uncertainty.\r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "MCD43C3.061",
             "creator": "Crystal Schaaf, Zhuosen Wang",
-            "title": "MODIS/Terra+Aqua BRDF/Albedo Albedo Daily L3 Global 0.05Deg CMG V061",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Moderate Resolution Imaging Spectroradiometer (MODIS) MCD43C3 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) Albedo dataset is produced daily using 16 days of Terra and Aqua MODIS data in a 0.05 degree (5,600 meters at the equator) Climate Modeling Grid (CMG). Data are temporally weighted to the ninth day of the retrieval period which is reflected in the Julian date in the file name. This CMG product covers the entire globe for use in climate simulation models. \r\n\r\nMCD43C3 provides black-sky albedo (directional hemispherical reflectance) and white-sky albedo (bihemispherical reflectance) at local solar noon. Black-sky albedo and white-sky albedo values are available as a separate layer for MODIS spectral bands 1 through 7 as well as the visible, near infrared (NIR), and shortwave bands. Along with the 20 albedo layers are ancillary layers for quality, local solar noon, percent finer resolution inputs, snow cover, and uncertainty.\r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43C3.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43C3.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43C3.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43C3.061",
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
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43C3.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43C3.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2532068039-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2532068039-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/MCD43C3.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/MCD43C3.061/contents.html",
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
-                    "downloadURL": "https://www.umb.edu/spectralmass/terra_aqua_modis/v006",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://www.umb.edu/spectralmass/terra_aqua_modis/v006",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MCD43C3",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MCD43C3",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MCD43C3",
-                    "description": "Further details regarding MODIS land product validation for the MCD43 data products are available from the MODIS Land Team Validation site.",
                     "@type": "dcat:Distribution",
+                    "description": "Further details regarding MODIS land product validation for the MCD43 data products are available from the MODIS Land Team Validation site.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MCD43C3",
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
+            "identifier": "C2532068039-LPCLOUD",
+            "issued": "2021-02-22",
+            "keyword": [
+                "ngda",
+                "surface radiative properties",
+                "land surface",
+                "earth science",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MCD43C3.061",
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
+            "series-name": "MCD43C3.061",
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
+            "title": "MODIS/Terra+Aqua BRDF/Albedo Albedo Daily L3 Global 0.05Deg CMG V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/MEASURES/WATERCYCLE/DATA314",
             "citation": "Princeton University (Eric Wood). 2017-03-01. WC_PM_ET_050. Version 1. SRB/GEWEX evapotranspiration (Penman-Monteith) L4 3 hour 0.5 degree x 0.5 degree V1. Greenbelt, MD USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/MEASURES/WATERCYCLE/DATA314. https://disc.gsfc.nasa.gov/datacollection/WC_PM_ET_050_1.html. Digital Science Data.",
-            "issued": "2014-09-25",
-            "temporal": "1984-01-01T00:00:00Z/2007-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2014-09-25",
-            "references": [
-                "https://doi.org/10.1016/j.rse.2010.11.006"
-            ],
-            "keyword": [
-                "atmospheric water vapor",
-                "atmosphere",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ERIC WOOD",
                 "hasEmail": "mailto:efwood@princeton.edu"
             },
+            "creator": "Princeton University (Eric Wood)",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1371013470-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "SRB/GEWEX evapotranspiration (Penman-Monteith) L4 3 hour 0.5 degree x 0.5 degree V1 is a global, 24-year (1984-2007), satellite-derived evapotranspiration over land data set. It is based on the Penman-Monteith model. Evapotranspiration provides the critical link between the water and energy cycles within the Earth system. Better representation of the spatial distribution and temporal development of surface evapotranspiration is needed not only to improve the description of water vapor exchanges for global water budget estimation but also to advance our understanding of the climate system.\n\nInput data sets include (1) vegetation index data, i.e., Leaf Area Index (LAI), derived from the Advanced Very High Resolution Radiometer (AVHRR) sensors onboard the NOAA-7, NOAA-9, NOAA-11, NOAA-14, and NOAA-16 satellites and the Moderate Resolution Imaging Spectroradiometer (MODIS) onboard the EOS-Terra and EOS-Aqua satellites; (2) meteorology data from the latest version of the Princeton University global forcing data sets and from the Variable Infiltration Capacity (VIC) land surface model output; and (3) radiative data from the NASA Global Energy and Water Exchanges (GEWEX) Surface Radiation Budget Project.",
-            "release-place": "Greenbelt, MD USA",
-            "series-name": "WC_PM_ET_050",
-            "creator": "Princeton University (Eric Wood)",
-            "graphic-preview-description": "SRB/GEWEX PM evapotranspiration",
-            "title": "SRB/GEWEX evapotranspiration (Penman-Monteith) L4 3 hour 0.5 degree x 0.5 degree V1 (WC_PM_ET_050) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/WC_PM_ET_050_1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FWATERCYCLE%2FDATA314",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FWATERCYCLE%2FDATA314",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/WC_PM_ET_050_1.png",
-                    "description": "SRB/GEWEX PM evapotranspiration",
                     "@type": "dcat:Distribution",
+                    "description": "SRB/GEWEX PM evapotranspiration",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/WC_PM_ET_050_1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/WC_PM_ET_050_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/WC_PM_ET_050_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/TerrestrialWaterCycle/WC_PM_ET_050.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/TerrestrialWaterCycle/WC_PM_ET_050.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=WC_PM_ET_050",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=WC_PM_ET_050",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/hyrax/TerrestrialWaterCycle/WC_PM_ET_050.1/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/hyrax/TerrestrialWaterCycle/WC_PM_ET_050.1/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/TerrestrialWaterCycle/WC_PM_ET_050.1/doc/README.WC_PM_ET_050_V1.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/TerrestrialWaterCycle/WC_PM_ET_050.1/doc/README.WC_PM_ET_050_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 }
             ],
+            "graphic-preview-description": "SRB/GEWEX PM evapotranspiration",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/WC_PM_ET_050_1.png",
+            "identifier": "C1371013470-GES_DISC",
+            "issued": "2014-09-25",
+            "keyword": [
+                "atmospheric water vapor",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/WATERCYCLE/DATA314",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2014-09-25",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1016/j.rse.2010.11.006"
+            ],
+            "release-place": "Greenbelt, MD USA",
+            "series-name": "WC_PM_ET_050",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1984-01-01T00:00:00Z/2007-12-31T23:59:59Z",
             "theme": [
                 "MEaSUREs",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SRB/GEWEX evapotranspiration (Penman-Monteith) L4 3 hour 0.5 degree x 0.5 degree V1 (WC_PM_ET_050) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/195",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hopkins, B. 2014. NPP Grassland: Olokemeji, Nigeria, 1956-1964, R1. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/195",
-            "issued": "2014-09-16",
-            "temporal": "1956-01-01T00:00:00Z/1964-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-17",
-            "keyword": [
-                "earth science",
-                "ecological dynamics",
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
-            "identifier": "C2751941950-ORNL_CLOUD",
             "description": "This data set contains two ASCII files (.txt format). One file contains monthly above-ground biomass data (total live biomass plus dead matter) for May 1956 to February 1958 for an annually burned, humid derived savanna in the Olokemeji Forest Reserve, Nigeria (7.42 N, 3.55 E) . This file also contains single measurements of above-ground biomass for years 1963 and 1964, single measurements of above-ground biomass at a nearby area for years 1960 and 1964, a single measurement of peak herbaceous leaf area index (LAI) for 1963, and a single measurement of peak tree/shrub LAI for 1964. Harvest procedures were used to measure biomass. LAI was determined by direct measurements. The second file contains climate data (precipitation amount and maximum/minimum temperature) from a weather station at the study site for the period 1956/01/01 through 1964/12/31.Annual above-ground net primary production (ANPP) estimates presented here are the sum of the increase in above-ground plant matter accumulation (total live biomass plus dead matter). ANPP of the herbaceous layer was estimated in 1957 to be around 680 g/m2/yr based on peak total clipped matter.",
-            "graphic-preview-description": "Browse Image",
-            "title": "NPP Grassland: Olokemeji, Nigeria, 1956-1964, R1",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/npp_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F195",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F195",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/npp/grassland/NPP_OLK/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/npp/grassland/NPP_OLK/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_OLK.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_OLK.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/195",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/195",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/grassland/NPP_OLK/comp/NPP_OLK.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/grassland/NPP_OLK/comp/NPP_OLK.pdf",
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
+            "identifier": "C2751941950-ORNL_CLOUD",
+            "issued": "2014-09-16",
+            "keyword": [
+                "earth science",
+                "ecological dynamics",
+                "biosphere",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/195",
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
             "spatial": "7.42 3.55",
+            "temporal": "1956-01-01T00:00:00Z/1964-12-31T23:59:59Z",
             "theme": [
                 "NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NPP Grassland: Olokemeji, Nigeria, 1956-1964, R1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AMSRU/AU_SI6_NRT_R04",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Meier, Walt, Josefino C Comiso, and Thorsten Markus.2019. NRT AMSR2 Unified L3 Daily 6.25 km Polar Gridded 89 GHz Brightness Temperatures [indicate subset used]. Dataset available online from the NASA Global Hydrology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/AMSRU/AU_SI6_NRT_R04",
-            "issued": "2020-06-30",
-            "temporal": "2020-06-29T08:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-06-30",
-            "keyword": [
-                "earth science",
-                "spectral/engineering",
-                "microwave",
-                "cryosphere",
-                "sea ice",
-                "oceans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:support-ghrc@earthdata.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
-            "identifier": "C1886605828-LANCEAMSR2",
             "description": "The Advanced Microwave Scanning Radiometer 2 (AMSR2) instrument on the Global Change Observation Mission - Water 1 (GCOM-W1) provides global passive microwave measurements of terrestrial, oceanic, and atmospheric parameters for the investigation of global water and energy cycles. Near real-time (NRT) products are generated within 3 hours of the last observations in the file, by the Land Atmosphere Near real-time Capability for EOS (LANCE) at the AMSR Science Investigator-led Processing System (AMSR SIPS), which is collocated with the Global Hydrology Resource Center (GHRC) DAAC.  The NRT AMSR2 Unified L3 Daily 6.25 km Polar Gridded 89 GHz Brightness Temperatures, Version 4 uses as input the resampled brightness temperature (Level-1R) data provided by the Japanese Aerospace Exploration Agency (JAXA).  The Version 4 dataset uses the AMSR-U2 product generation algorithm with slight modifications for NRT product generation, same algorithm used to generation the standard, science quality, data that is available at the NSIDC DAAC.  This Level-3 gridded product includes brightness temperatures at 89.0 GHz. Data are mapped to a polar stereographic grid at 6.25 km spatial resolution. This product is an intermediate product during processing of LANCE AMSR2 Level-3 sea ice products at 12.5 km and 25 km resolution. Data are stored in HDF-EOS5/netCDF-CF  format and are available via HTTP from the EOSDIS LANCE system at https://lance.nsstc.nasa.gov/amsr2-science/data/level3/seaice6.  If data latency is not a primary concern, please consider using science quality products. Science products are created using the best available ancillary, calibration and ephemeris information. Science quality products are an internally consistent, well-calibrated record of the Earth's geophysical properties to support science. These standard product, science quality, are available at the NSIDC DAAC: https://nsidc.org/",
-            "graphic-preview-description": "Sample browse image",
-            "title": "NRT AMSR2 Unified L3 Daily 6.25 km Polar Gridded 89 GHz Brightness Temperatures V4",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/browse_sample/lance/AMSR_U2_SI6.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAMSRU%2FAU_SI6_NRT_R04",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAMSRU%2FAU_SI6_NRT_R04",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://lance.nsstc.nasa.gov/amsr2-science/data/level3/seaice6/R04/hdfeos5/",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://lance.nsstc.nasa.gov/amsr2-science/data/level3/seaice6/R04/hdfeos5/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://lance.itsc.uah.edu/amsr2-science/data/level3/seaice6/R04/hdfeos5/",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://lance.itsc.uah.edu/amsr2-science/data/level3/seaice6/R04/hdfeos5/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LANCE"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://worldview.earthdata.nasa.gov/?l=AMSRU2_Sea_Ice_Brightness_Temp_6km_89V%2CAMSRU2_Sea_Ice_Brightness_Temp_6km_89H%2CCoastlines%2CMODIS_Terra_CorrectedReflectance_TrueColor",
-                    "description": "Interactively browse imagery in EOSDIS Worldview",
                     "@type": "dcat:Distribution",
+                    "description": "Interactively browse imagery in EOSDIS Worldview",
+                    "downloadURL": "https://worldview.earthdata.nasa.gov/?l=AMSRU2_Sea_Ice_Brightness_Temp_6km_89V%2CAMSRU2_Sea_Ice_Brightness_Temp_6km_89H%2CCoastlines%2CMODIS_Terra_CorrectedReflectance_TrueColor",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through WORLDVIEW"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/all-data-recipes#drp-formatcon",
-                    "description": "Data Format Conversion Recipes",
                     "@type": "dcat:Distribution",
+                    "description": "Data Format Conversion Recipes",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/all-data-recipes#drp-formatcon",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data recipes"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthdata.nasa.gov/earth-observation-data/near-real-time",
-                    "description": "The home page for the project or program which sponsored the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The home page for the project or program which sponsored the dataset",
+                    "downloadURL": "https://earthdata.nasa.gov/earth-observation-data/near-real-time",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/browse_sample/lance/AMSR_U2_SI6.jpg",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/browse_sample/lance/AMSR_U2_SI6.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/AU_SI6/versions/1",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://nsidc.org/data/AU_SI6/versions/1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
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
+            "graphic-preview-description": "Sample browse image",
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/browse_sample/lance/AMSR_U2_SI6.jpg",
+            "identifier": "C1886605828-LANCEAMSR2",
+            "issued": "2020-06-30",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "microwave",
+                "cryosphere",
+                "sea ice",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/AMSRU/AU_SI6_NRT_R04",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-06-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
             "spatial": "-180.0 -89.0 180.0 89.0",
+            "temporal": "2020-06-29T08:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "LANCE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NRT AMSR2 Unified L3 Daily 6.25 km Polar Gridded 89 GHz Brightness Temperatures V4"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NOAA20/CERES/ES4-FM6_L3.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2020-05-01. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/NOAA20/CERES/ES4-FM6_L3.001.",
-            "issued": "2020-03-13",
-            "temporal": "2018-05-01T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-03-13",
-            "keyword": [
-                "atmosphere",
-                "atmospheric radiation",
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
-            "identifier": "C2246001717-LARC_ASDC",
             "description": "CER_ES4_NOAA20-FM6_Edition1 is the Clouds and the Earth's Radiant Energy System (CERES) Earth Radiation Budget Experiment (ERBE)-like Monthly Geographical Averages NOAA-20 FM6 Edition1, data product. The CERES instrument TOA fluxes use algorithms identical to those used by ERBE, averaged regionally (2.5-degree, 5-degree, and 10-degree grid), zonally (2.5-degree, 5-degree, and 10-degree) and globally. The ERBE-like Monthly Geographical Averages (ES-4) product contains a month of space and time averaged CERES data for a single scanner instrument. For each observed 2.5-degree spatial region, the daily average, the hourly average over the month, and the overall monthly average of shortwave and long-wave fluxes at the Top-of-the-Atmosphere (TOA) from the CERES ES-9 product are spatially nested up from 2.5-degree regions to 5- and 10-degree regions, to 2.5-, 5-, and 10-degree zonal averages, and to global monthly averages. For each nested area, the albedo and net flux are given. For each region, the daily average flux is estimated from an algorithm that uses the available hourly data, scene identification data, and diurnal models. This algorithm is like the algorithm used for ERBE. CERES is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions are a follow-on to the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument (PFM) was launched on November 27, 1997 as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the EOS flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board EOS Aqua on May 4, 2002. The CERES instrument (FM5) was launched on board the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The last CERES instrument (FM6) was launched on board the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite on November 18, 2017.",
-            "title": "CERES ERBE-like Monthly Geographical Averages NOAA-20 FM6 Edition1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNOAA20%2FCERES%2FES4-FM6_L3.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNOAA20%2FCERES%2FES4-FM6_L3.001",
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
-                    "downloadURL": "https://doi.org/10.5067/NOAA20/CERES/ES4-FM6_L3.001",
-                    "description": "DOI data set landing page for CER_ES4_NOAA20-FM6_Edition1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CER_ES4_NOAA20-FM6_Edition1",
+                    "downloadURL": "https://doi.org/10.5067/NOAA20/CERES/ES4-FM6_L3.001",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/quality_summaries/CER_ES4_NOAA20_Edition1.pdf",
-                    "description": "Quality Summary: CERES ES4 NOAA-20 Edition 1",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Summary: CERES ES4 NOAA-20 Edition 1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/quality_summaries/CER_ES4_NOAA20_Edition1.pdf",
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
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/features/DelicateBalance/balance2.php",
-                    "description": "NASA Earth Observatory Article: A Delicate Balance: Signs of Change in the Tropics\u00a0-\u00a0New data sets were also used from NASA's Clouds and the Earth's Radiant Energy System (CERES) instruments that fly aboard the Tropical Rainfall Measuring Mission (TRMM) as well as the newer Terra satellite.",
+                {
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: A Delicate Balance: Signs of Change in the Tropics\u00a0-\u00a0New data sets were also used from NASA's Clouds and the Earth's Radiant Energy System (CERES) instruments that fly aboard the Tropical Rainfall Measuring Mission (TRMM) as well as the newer Terra satellite.",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2246001717-LARC_ASDC",
-                    "description": "Earthdata Search for CER_ES4_NOAA20-FM6_Edition1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CER_ES4_NOAA20-FM6_Edition1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2246001717-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/ES4/NOAA20-FM6_Edition1/",
-                    "description": "ASDC Direct Data Download for CER_ES4_NOAA20-FM6_Edition1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CER_ES4_NOAA20-FM6_Edition1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/ES4/NOAA20-FM6_Edition1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/ES4/NOAA20-FM6_Edition1/contents.html",
-                    "description": "OPeNDAP data access for CER_ES4_NOAA20-FM6_Edition1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CER_ES4_NOAA20-FM6_Edition1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/ES4/NOAA20-FM6_Edition1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2246001717-LARC_ASDC",
+            "issued": "2020-03-13",
+            "keyword": [
+                "atmosphere",
+                "atmospheric radiation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/NOAA20/CERES/ES4-FM6_L3.001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-03-13",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2018-05-01T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "CERES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CERES ERBE-like Monthly Geographical Averages NOAA-20 FM6 Edition1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-MSI-3-EDR-CRUISE3-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-msi-3-edr-cruise3-v1.0_8dtv-d52q",
+            "issued": "2018-06-26",
+            "keyword": [
+                "near earth asteroid rendezvous",
+                "eros"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-MSI-3-EDR-CRUISE3-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-msi-3-edr-cruise3-v1.0_8dtv-d52q",
-            "description": "NEAR EDR volume sets contain a single data set, from one instrument and one mission phase (defined in the phase table in /AAREADME.TXT).",
-            "title": "NEAR MSI IMAGES FOR CRUISE3",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEAR MSI IMAGES FOR CRUISE3"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0504-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-12-24T12:28:25.000 to 2014-12-24T20:40:35.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0504-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0504-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0504-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-12-24T12:28:25.000 to 2014-12-24T20:40:35.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0504 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0504 V1.0"
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
-                "sharing",
-                "appel",
-                "ask magazine",
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
-            "identifier": "NASA-860__47",
             "description": "Academy of Program/Project & Engineering Leadership's ASK Magazine archive.",
-            "title": "Academy of Program/Project & Engineering Leadership ASK Magazine Past Issues",
-            "programCode": [
-                "026:045"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -358363,299 +358342,302 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/P3M",
+            "identifier": "NASA-860__47",
+            "issued": "2018-06-25",
+            "keyword": [
+                "sharing",
+                "appel",
+                "ask magazine",
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
-            "landingPage": "https://doi.org/10.7265/N5057CVT",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Arctic and Southern Ocean Sea Ice Concentrations, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center. https://doi.org/10.7265/N5057CVT.",
-            "issued": "1953-01-01",
-            "temporal": "1953-01-01T00:00:00Z/1995-08-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1995-08-31",
-            "keyword": [
-                "cryosphere",
-                "earth science",
-                "sea ice"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Walsh",
                 "hasEmail": "mailto:walsh@wx.atmos.uiuc.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NSIDC"
-            },
-            "identifier": "C1386246223-NSIDCV0",
             "description": "This data set provides monthly sea ice concentration for the Arctic from 1901 to 1995 and for the Southern Oceans from 1973 to 1990 on a standard 1-degree grid (cylindrical projection) to provide a relatively uniform set of sea ice extent for all longitudes. The data are in ASCII format and are available via FTP.",
-            "title": "Arctic and Southern Ocean Sea Ice Concentrations, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN5057CVT",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN5057CVT",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/G00799_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/G00799_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5057CVT",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/N5057CVT",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5057CVT",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/N5057CVT",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386246223-NSIDCV0",
+            "issued": "1953-01-01",
+            "keyword": [
+                "cryosphere",
+                "earth science",
+                "sea ice"
+            ],
+            "landingPage": "https://doi.org/10.7265/N5057CVT",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1995-08-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "-180.0 40.0 180.0 90.0",
+            "temporal": "1953-01-01T00:00:00Z/1995-08-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Arctic and Southern Ocean Sea Ice Concentrations, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7265/N5B8562T",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Morphometric Characteristics of Ice and Snow in the Arctic Basin: Aircraft Landing Observations from the Former Soviet Union, 1928-1989, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center. https://doi.org/10.7265/N5B8562T.",
-            "issued": "1928-06-01",
-            "temporal": "1928-06-01T00:00:00Z/1989-05-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1989-05-31",
-            "keyword": [
-                "sea ice",
-                "snow/ice",
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
-                "name": "NSIDC"
-            },
-            "identifier": "C1386246252-NSIDCV0",
             "description": "This data set contains sea ice and snow measurements collected during aircraft landings associated with the Soviet Union's historical Sever airborne and North Pole drifting station programs. The data set contains measurements of 23 parameters, including ice thickness and snow depth on the runway and surrounding area; ridge, hummock, and sastrugi dimensions and areal coverage; and snow density.",
-            "title": "Morphometric Characteristics of Ice and Snow in the Arctic Basin: Aircraft Landing Observations from the Former Soviet Union, 1928-1989, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN5B8562T",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN5B8562T",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/G02140_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/G02140_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5B8562T",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/N5B8562T",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5B8562T",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/N5B8562T",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386246252-NSIDCV0",
+            "issued": "1928-06-01",
+            "keyword": [
+                "sea ice",
+                "snow/ice",
+                "earth science",
+                "cryosphere"
+            ],
+            "landingPage": "https://doi.org/10.7265/N5B8562T",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1989-05-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "-180.0 64.0 180.0 90.0",
+            "temporal": "1928-06-01T00:00:00Z/1989-05-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Morphometric Characteristics of Ice and Snow in the Arctic Basin: Aircraft Landing Observations from the Former Soviet Union, 1928-1989, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE1_AircraftRemoteSensing_DC8_Lidar_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2023-07-19. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE1_AircraftRemoteSensing_DC8_Lidar_Data_1.",
-            "issued": "2022-08-31",
-            "temporal": "1999-11-16T00:00:00Z/2000-03-15T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-08-31",
-            "keyword": [
-                "atmospheric chemistry",
-                "earth science",
-                "aerosols",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Johnathan Hair",
                 "hasEmail": "mailto:johnathan.w.hair@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2569836810-LARC_ASDC",
             "description": "SOLVE1_AircraftRemoteSensing_DC8_Lidar_Data is the remotely sensed lidar trace gas data for the DC-8 aircraft collected during the SAGE III Ozone Loss and Validation Experiment (SOLVE). Data were collected by Differential Absorption Lidar (DIAL) and the Airborne Raman Ozone, Temperature, and Aerosol Lidar (AROTAL). Data collection for this product is complete.\r\n\r\nThe SOLVE campaign was a NASA multi-program effort of the Upper Atmosphere Research Program (UARP), Atmospheric Effects of Aviation Project (AEAP), Atmospheric Chemistry Modeling and Analysis Program (ACMAP) and Earth Observing System (EOS) of NASA\u2019s Earth Science Enterprise (ESE). SOLVE\u2019s primary objective was for calibrating and validating the Stratospheric Aerosol and Gas Experiment (SAGE) III satellite measurements, while examining the processes that controlled ozone levels at a mid- to high-latitude range. The major goal of SAGE III was to quantitatively assess ozone loss at high latitudes. SOLVE was a two-phase experiment, the first phase, SOLVE, occurred during the fall of 1999 through the spring of 2000. The second phase, SOLVE II, occurred during the winter of 2003.\r\n\r\nSOLVE took place in the Arctic high-latitude region during the winter. The polar ozone depletion processes cause by human-produced chlorine and bromine are most active in mid-to-late winter and early spring in the high Arctic. In order to conduct this validation experiment, NASA deployed the NASA ER-2 aircraft and NASA DC-8 aircraft. The ER-2 measured a variety of atmospheric data, including ozone (O3), H2O, CO2, ClONO2, HCl, ClO/BrO, and Cl2O2. The DC-8 aircraft measured ozone, ClO/BrO, and aerosol, among other atmospheric data. SOLVE also utilized balloon platforms, ground-based instruments, and collaborations with the German Aerospace Center\u2019s (DLR) FALCON aircraft equipped with the OLEX Lidar to achieve the mission objectives. Overall, the campaign had 28 flights, with SOLVE featuring 17 total flights among the different aircrafts and SOLVE II featuring 11 flights.",
-            "title": "SOLVE I DC-8 Aircraft Remotely Sensed Lidar Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSOLVE1_AircraftRemoteSensing_DC8_Lidar_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSOLVE1_AircraftRemoteSensing_DC8_Lidar_Data_1",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/SOLVE/AircraftRemoteSensing_DC8_Lidar_Data_1/",
-                    "description": "ASDC Direct Data Download for SOLVE1_AircraftRemoteSensing_DC8_Lidar_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for SOLVE1_AircraftRemoteSensing_DC8_Lidar_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/SOLVE/AircraftRemoteSensing_DC8_Lidar_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2569836810-LARC_ASDC",
+            "issued": "2022-08-31",
+            "keyword": [
+                "atmospheric chemistry",
+                "earth science",
+                "aerosols",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE1_AircraftRemoteSensing_DC8_Lidar_Data_1",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>12.0 -180.0 12.0 180.0 90.0 180.0 90.0 -180.0 12.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1999-11-16T00:00:00Z/2000-03-15T23:59:59.999Z",
             "theme": [
                 "SOLVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SOLVE I DC-8 Aircraft Remotely Sensed Lidar Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/8e7s-kdza",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2015-10-14",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "pathogen",
-                "phenotypic",
-                "fungal"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NASA Open Data",
                 "hasEmail": "mailto:no-reply@data.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.nasa.gov"
-            },
-            "identifier": "https://data.nasa.gov/api/views/8e7s-kdza",
             "description": "https://c3.nasa.gov/genelab/accession/GLDS-20/\r\n\r\nThis study presents the first global transcriptional profiling and phenotypic characterization of the major human opportunistic fungal pathogen, Candida albicans, grown in spaceflight conditions. Microarray analysis revealed that C. albicans subjected to short-term spaceflight culture differentially regulated 454 genes compared to synchronous ground controls, which represented 8.4% of the analyzed ORFs. Spaceflight-cultured C. albicans induced genes involved in cell aggregation (similar to flocculation), which was validated by microscopic and flow cytometry analysis. We also observed enhanced random budding of spaceflight-cultured cells as opposed to more normal bipolar budding patterns for ground samples, in accordance with the gene expression data. Furthermore, genes involved in antifungal agent and stress resistance were differentially regulated in spaceflight, including induction of ABC transporters and members of the major facilitator family, downregulation of ergosterol-encoding genes, and upregulation of genes involved in oxidative stress resistance. Finally, downregulation of genes involved in the actin cytoskeleton was observed. Interestingly, the transcriptional regulator Cap1 and over 30% of the Cap1 regulon was differentially expressed in spaceflight-cultured C. albicans. A potential role for Cap1 in the spaceflight response of C. albicans is suggested, as this regulator is involved in random budding, cell aggregation, actin cytoskeleton, and oxidative stress resistance; all related to observed spaceflight-associated changes of C. albicans. While culture of C. albicans in microgravity potentiates a global change in gene expression that could induce a virulence-related phenotype, no increased virulence in a murine intraperitoneal (i.p.) infection model was observed. This study represents an important basis for the assessment of the risk that commensal flora could play during spaceflight missions. Furthermore, since the low fluid-shear environment of microgravity is relevant to physical forces encountered by pathogens during the infection process, insights gained from this study could identify novel infectious disease mechanisms, with downstream benefits for the general public. Cells were grown for 24 hours on the space shuttle or as ground-based controls, preserved in RNALater, and stored at -80C. Four samples of each flight- and ground-based controls were harvested for microarray analysis. GAP is Group Activation Pack and each GAP contains 8 FPAs. The numbers represent the # assigned to the particular GAP and the number assigned to the specific FPA (1-8) within the indicated GAP. The same hardware is used for the flight samples and the ground samples.",
-            "title": "S E- GEOD-50881 Study Samples --- Candida albicans response to spaceflight (NASA STS-115)",
-            "programCode": [
-                "026:035"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -358663,542 +358645,574 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.nasa.gov/api/views/8e7s-kdza/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.nasa.gov/api/views/8e7s-kdza/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.nasa.gov/api/views/8e7s-kdza/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.nasa.gov/api/views/8e7s-kdza/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.nasa.gov/api/views/8e7s-kdza/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.nasa.gov/api/views/8e7s-kdza/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.nasa.gov/api/views/8e7s-kdza/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.nasa.gov/api/views/8e7s-kdza/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.nasa.gov/api/views/8e7s-kdza/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.nasa.gov/api/views/8e7s-kdza",
+            "issued": "2015-10-14",
+            "keyword": [
+                "pathogen",
+                "phenotypic",
+                "fungal"
+            ],
+            "landingPage": "https://data.nasa.gov/d/8e7s-kdza",
+            "modified": "2023-01-31",
+            "programCode": [
+                "026:035"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.nasa.gov"
+            },
             "theme": [
                 "Applied Science"
-            ]
+            ],
+            "title": "S E- GEOD-50881 Study Samples --- Candida albicans response to spaceflight (NASA STS-115)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1%2FVG2-J-UVS-5-BRIGHTNESS-N%2FS-MAPS-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Voyager 1 and 2 measurements of the brightness of Jupiter at H Lyman alpha and in the H2 Lyman and Werner bands shortward of H Lyman alpha. Pointing has been corrected by the C-Smithing process, and these data were derived from the pre-encounter North-South Map sequences. In this sequence, the UVS field of view was located near the central meridian of the planet. The field of view stepped slowly from north to south, and then rapidly repositioned to the north. These scans were repeated until all Jovian longitudes had been sampled. Coverage in longitude was not continuous in time. Rather, some longitude ranges were covered on the preceding or following rotation of Jupiter.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-vg2-j-uvs-5-brightness-n-s-maps-v1.0_8e9u-g4ra",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "comet sl9/jupiter collision",
                 "jupiter",
                 "voyager"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1%2FVG2-J-UVS-5-BRIGHTNESS-N%2FS-MAPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-vg2-j-uvs-5-brightness-n-s-maps-v1.0_8e9u-g4ra",
-            "description": "This data set contains Voyager 1 and 2 measurements of the brightness of Jupiter at H Lyman alpha and in the H2 Lyman and Werner bands shortward of H Lyman alpha. Pointing has been corrected by the C-Smithing process, and these data were derived from the pre-encounter North-South Map sequences. In this sequence, the UVS field of view was located near the central meridian of the planet. The field of view stepped slowly from north to south, and then rapidly repositioned to the north. These scans were repeated until all Jovian longitudes had been sampled. Coverage in longitude was not continuous in time. Rather, some longitude ranges were covered on the preceding or following rotation of Jupiter.",
-            "title": "VOYAGER 1&2 JUPITER BRIGHTNESS NORTH/SOUTH MAP SET V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VOYAGER 1&2 JUPITER BRIGHTNESS NORTH/SOUTH MAP SET V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1000000280-LARC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 2 Aerosol parameters for the INTEX-B region;See ProductionDateTime for published Date.",
-            "issued": "2015-05-27",
-            "temporal": "2006-02-28T00:00:00Z/2006-04-03T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-05-27",
-            "keyword": [
-                "atmosphere",
-                "aerosols",
-                "air quality",
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
-            "identifier": "C1000000280-LARC",
             "description": "MISR Level 2 Aerosol Product containing aerosol optical depth and particle type, with associated atmospheric data for the INTEXB_2006 theme.",
-            "title": "MISR L2 Aerosol Product subset for the INTEX-B region V002",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1000000280-LARC.html",
-                    "description": "View this dataset on the CMR (Common Metadata Repository)",
                     "@type": "dcat:Distribution",
+                    "description": "View this dataset on the CMR (Common Metadata Repository)",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1000000280-LARC.html",
+                    "mediaType": "text/html",
                     "title": "CMR"
                 }
             ],
+            "identifier": "C1000000280-LARC",
+            "issued": "2015-05-27",
+            "keyword": [
+                "atmosphere",
+                "aerosols",
+                "air quality",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1000000280-LARC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-05-27",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LaRC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2006-02-28T00:00:00Z/2006-04-03T23:59:59Z",
             "theme": [
                 "INTEXB_2006",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR L2 Aerosol Product subset for the INTEX-B region V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0751-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-05-04T23:08:05.000 to 2015-05-05T07:21:42.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0751-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0751-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0751-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-05-04T23:08:05.000 to 2015-05-05T07:21:42.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0751 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0751 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aphx_mission_bundle&version=1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This version of the Phoenix bundle was created by the PDS Atmospheres node in 2014",
+            "identifier": "urn:nasa:pds:phx_mission_bundle_8eg3-34gq",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "mars",
                 "phoenix",
                 "phoenix mars mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aphx_mission_bundle&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:phx_mission_bundle_8eg3-34gq",
-            "description": "This version of the Phoenix bundle was created by the PDS Atmospheres node in 2014",
-            "title": "Phoenix Mission Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Phoenix Mission Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2306",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wright, K.A., and P. Passalacqua. 2024. Delta-X: Calibrated ANUGA Hydrodynamic Outputs for the Atchafalaya Basin, MRD, LA. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2306",
-            "issued": "2024-06-12",
-            "temporal": "2016-10-15T00:00:00Z/2021-08-27T11:30:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-13",
-            "keyword": [
-                "coastal processes",
-                "surface water",
-                "oceans",
-                "earth science",
-                "terrestrial hydrosphere"
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
-            "identifier": "C3091330782-ORNL_CLOUD",
             "description": "This dataset provides ANUGA hydrodynamic modeling results and input run-scripts for the Atchafalaya basin in the Mississippi River Delta in southern Louisiana, USA, during three windows of time corresponding to the Delta-X and Pre-Delta-X field campaigns in fall 2016, spring 2021, and fall 2021. ANUGA is a 2D depth-integrated hydrodynamic model which uses the Finite Volume Method (FVM) to numerically solve the shallow water momentum and continuity equations for fluid flow in broad-scale geophysical systems. Each iteration of the model was extensively calibrated using a database of in-situ and remotely-sensed observations, including about 54 water level gauges, numerous water surface profiles collected by AirSWOT or lidar, and water level change measurements derived from UAVSAR. The model was forced using observational data collected from NOAA and USGS, and the model mesh was specifically designed to capture channel-island connectivity using high-resolution Planet Labs imagery spanning over a decade. In total, over a month of simulation outputs are included in this dataset, covering different seasons and hydrological conditions in the Atchafalaya and Wax Lake Delta systems. These model outputs can be leveraged with other Delta-X datasets to provide contextual information about water levels or flow velocities at different times or locations within the Atchafalaya basin, and the model codes provided can be used to simulate additional time periods for further analysis in this region. Model outputs are presented in NetCDF (*.nc) format and run-scripts are in Python (*.py) or contained in compressed (*.zip) file format.",
-            "graphic-preview-description": "ANUGA flow directions and depth at one timestep during the 2021 Spring campaign.",
-            "title": "Delta-X: Calibrated ANUGA Hydrodynamic Outputs for the Atchafalaya Basin, MRD, LA",
-            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/DeltaX_ANUGA_AtchafalayaBasin_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2306",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2306",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/deltax/DeltaX_ANUGA_AtchafalayaBasin/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/deltax/DeltaX_ANUGA_AtchafalayaBasin/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_ANUGA_AtchafalayaBasin.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_ANUGA_AtchafalayaBasin.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2306",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2306",
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
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/DeltaX_ANUGA_AtchafalayaBasin/comp/DeltaX_ANUGA_AtchafalayaBasin.pdf",
-                    "description": "Delta-X: Calibrated ANUGA Hydrodynamic Outputs for the Atchafalaya Basin, MRD, LA: DeltaX_ANUGA_AtchafalayaBasin.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Delta-X: Calibrated ANUGA Hydrodynamic Outputs for the Atchafalaya Basin, MRD, LA: DeltaX_ANUGA_AtchafalayaBasin.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/DeltaX_ANUGA_AtchafalayaBasin/comp/DeltaX_ANUGA_AtchafalayaBasin.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_ANUGA_AtchafalayaBasin_Fig1.jpg",
-                    "description": "ANUGA flow directions and depth at one timestep during the 2021 Spring campaign.",
                     "@type": "dcat:Distribution",
+                    "description": "ANUGA flow directions and depth at one timestep during the 2021 Spring campaign.",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_ANUGA_AtchafalayaBasin_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://deltax.jpl.nasa.gov/",
-                    "description": "Delta-X Project Site",
                     "@type": "dcat:Distribution",
+                    "description": "Delta-X Project Site",
+                    "downloadURL": "https://deltax.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "graphic-preview-description": "ANUGA flow directions and depth at one timestep during the 2021 Spring campaign.",
+            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/DeltaX_ANUGA_AtchafalayaBasin_Fig1.jpg",
+            "identifier": "C3091330782-ORNL_CLOUD",
+            "issued": "2024-06-12",
+            "keyword": [
+                "coastal processes",
+                "surface water",
+                "oceans",
+                "earth science",
+                "terrestrial hydrosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2306",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-06-13",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-88.65 29.14 -88.3 29.54",
+            "temporal": "2016-10-15T00:00:00Z/2021-08-27T11:30:00Z",
             "theme": [
                 "Delta-X",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Delta-X: Calibrated ANUGA Hydrodynamic Outputs for the Atchafalaya Basin, MRD, LA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMAG-4-ESC1-RESAMPLED-V5.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This dataset contains RESAMPLED DATA (CODMAC LEVEL 4) of the COMET\nESCORT1 Phase from November 22, 2014 until March 10, 2015 of the\nROSETTA orbiter magnetometer RPCMAG. Data are averaged to 60s means.\nObservations are done in the vicinity of comet\n67P/CHURYUMOV-GERASIMENKO 1 (1969 R1).\nVersion V5.0 is the first version being released.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmag-4-esc1-resampled-v5.0_8ekw-ueef",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "checkout",
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMAG-4-ESC1-RESAMPLED-V5.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmag-4-esc1-resampled-v5.0_8ekw-ueef",
-            "description": "This dataset contains RESAMPLED DATA (CODMAC LEVEL 4) of the COMET\nESCORT1 Phase from November 22, 2014 until March 10, 2015 of the\nROSETTA orbiter magnetometer RPCMAG. Data are averaged to 60s means.\nObservations are done in the vicinity of comet\n67P/CHURYUMOV-GERASIMENKO 1 (1969 R1).\nVersion V5.0 is the first version being released.",
-            "title": "ROSETTA-ORBITER 67P RPCMAG 4 ESC1 RESAMPLED V5.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCMAG 4 ESC1 RESAMPLED V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-MB-4-SUMSPEC-SCI-V1.0",
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
+            "description": "This archive contains Mars Exploration Rover Moessbauer Summed Spectra Reduced Data Record (RDR) products and ancillary files. The products archived on this volume were generated by the Moessbauer instrument team from Moessbauer EDR (Experiment Data Record) products. Supporting documentation and label files conform to the Planetary Data System (PDS) Standards, Version 3.6, Jet Propulsion Laboratory (JPL) document number D-7669.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-mb-4-sumspec-sci-v1.0_8em2-iwzc",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-MB-4-SUMSPEC-SCI-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-mb-4-sumspec-sci-v1.0_8em2-iwzc",
-            "description": "This archive contains Mars Exploration Rover Moessbauer Summed Spectra Reduced Data Record (RDR) products and ancillary files. The products archived on this volume were generated by the Moessbauer instrument team from Moessbauer EDR (Experiment Data Record) products. Supporting documentation and label files conform to the Planetary Data System (PDS) Standards, Version 3.6, Jet Propulsion Laboratory (JPL) document number D-7669.",
-            "title": "MER 2 MOESSBAUER 4 SUMMED SPECTRA RDR SCIENCE V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MER 2 MOESSBAUER 4 SUMMED SPECTRA RDR SCIENCE V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SUBORBITAL/PISTON2019-ONR-NOAA/RVSALLYRIDE/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/SUBORBITAL/PISTON2019-ONR-NOAA/RVSALLYRIDE/DATA001 .",
-            "issued": "2019-08-31",
-            "temporal": "2019-08-31T00:00:00Z/2019-09-26T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-04",
-            "keyword": [
-                "altitude",
-                "earth science",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "ocean circulation",
-                "ocean heat budget",
-                "ocean pressure",
-                "atmospheric radiation",
-                "atmospheric pressure",
-                "oceans",
-                "atmosphere",
-                "ocean temperature",
-                "ocean waves",
-                "precipitation",
-                "salinity/density",
-                "atmospheric winds",
-                "clouds"
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
-            "identifier": "C2566393530-LARC_ASDC",
             "description": "PISTON-ONR-NOAA_RVSallyRide_2019 is the Propagation of Intra-Seasonal Tropical Oscillations (PISTON) 2019 Research Vessel (RV) Sally Ride data product. This product is the result of a joint effort that involved NASA as well as the Office of Naval Research (ONR), and National Oceanic and Atmospheric Administration (NOAA). Data was collected collection for this product using multiple instruments on the RV platform including: Conductivity, Temperature, Depth (CTD), Acoustic Doppler Current Profiler (ADCP), SEA-going POLarimetric Doppler Radar (SEA-POL), Chameleon Microstructure Profiler(CHAM), and SurfOtter Platform (SO). Data collection is complete.\r\n\r\nThe PISTON field campaign, sponsored by the Office of Naval Research (ONR) and the National Oceanic and Atmospheric Administration (NOAA), was designed to gain understanding and enhance the prediction capability of multi-scale tropical atmospheric convection and air-sea interaction in this region. PISTON targeted the Boreal Summer Intraseasonal Oscillation (BSISO), which defines the northward and eastward movement of convection associated with equatorial waves, the MJO, tropical cyclones, and the Maritime Continent monsoon during northern-hemispheric (boreal) summertime. PISTON completed three total shipboard cruises (this doi), deployed eight drifting ocean profiling floats and two full-depth ocean moorings, collaborated with a Japanese research vessel collecting similar data, and also made use of soundings from nearby islands. These activities took place in the Philippine Sea, which is in the tropical northwestern Pacific Ocean north of Palau, between August 2018 - September 2019, with each dataset spanning a slightly different amount of time. There were two US research vessels involved in PISTON: R/V Thomas G. Thompson in Aug-Sept and Sept-Oct 2018  and R/V Sally Ride in Sept 2019 (this doi). The first 2018 cruise coincided collaborative activities with R/V Mirai. The 2019 cruise coincided with the NASA CAMP2Ex airborne field experiment (Clouds, Aerosol and Monsoon Processes-Philippines Experiment, please see more info below).  The two specialized moorings were deployed north of Palau and collected data from August 2018 - Oct 2019 to document a time series of ocean characteristics beneath typhoons and other tropical weather disturbances. Toward the same goal, eight profiling ocean floats were also deployed ahead of typhoons in 2018. \r\n\r\nFor characterization of clouds and precipitation, the PISTON shipboard instrument payload included a scanning C-band dual-polarization Doppler radar (SEA-POL), a vertically-pointing Doppler W-band radar, and multiple vertically- and horizontally-scanning lidars. Rawinsondes were launched from the ships for atmospheric profiling. Additional radiosonde and precipitation radar data were collected from R/V Mirai via an international collaboration. Regular soundings were also archived from islands neighboring the Philippines and the Philippine Sea: Dongsha Island, Taiping Island, Yap, Palau, and Guam. Additional atmospheric sampling from the PISTON R/V Thompson 2018 and Sally Ride 2019 cruises included an electric field meter and disdrometer in 2018, and all-sky camera images in 2019. To document near-surface meteorological conditions, air-sea fluxes, and upper-ocean variability including ocean vertical profiles on these cruises, instruments were deployed on and towed from the ship. Additional profiles of ocean acoustics and oceanic chemistry were not archived but are available upon request by James N. Moum, Oregon State University, jim.moum@oregonstate.edu. A forecast team analyzed and predicted conditions of the weather and ocean throughout the PISTON experiment, which were not archived but are available upon request for future modeling and observational analysis studies (contacts: Sue Chen, US Naval Research Lab Monterey, sue.chen@nrlmry.navy.mil and Michael M. Bell, Colorado State University, mmbell@colostate.edu). \r\n\r\nThere are five total DOIs r",
-            "title": "PISTON 2019 Research Vessel (RV) Sally Ride Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSUBORBITAL%2FPISTON2019-ONR-NOAA%2FRVSALLYRIDE%2FDATA001+",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSUBORBITAL%2FPISTON2019-ONR-NOAA%2FRVSALLYRIDE%2FDATA001+",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2566393530-LARC_ASDC",
-                    "description": "Earthdata Search Client for PISTON-ONR-NOAA_RVSallyRide_2019_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search Client for PISTON-ONR-NOAA_RVSallyRide_2019_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2566393530-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/SUBORBITAL/PISTON2019-ONR-NOAA/RVSallyRide/Data001",
-                    "description": "DOI for PISTON-ONR-NOAA_RVSallyRide_2019_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for PISTON-ONR-NOAA_RVSallyRide_2019_1",
+                    "downloadURL": "https://doi.org/10.5067/SUBORBITAL/PISTON2019-ONR-NOAA/RVSallyRide/Data001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CAMP2Ex/PISTON-ONR-NOAA_RVSallyRide_2019_1/",
-                    "description": "ASDC Direct Data Download for PISTON-ONR-NOAA_RVSallyRide_2019_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for PISTON-ONR-NOAA_RVSallyRide_2019_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CAMP2Ex/PISTON-ONR-NOAA_RVSallyRide_2019_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CAMP2Ex/PISTON-ONR-NOAA_RVSallyRide_2019_1/contents.html",
-                    "description": "OPeNDAP data access for PISTON-ONR-NOAA_RVSallyRide_2019_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for PISTON-ONR-NOAA_RVSallyRide_2019_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CAMP2Ex/PISTON-ONR-NOAA_RVSallyRide_2019_1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2566393530-LARC_ASDC",
+            "issued": "2019-08-31",
+            "keyword": [
+                "altitude",
+                "earth science",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "ocean circulation",
+                "ocean heat budget",
+                "ocean pressure",
+                "atmospheric radiation",
+                "atmospheric pressure",
+                "oceans",
+                "atmosphere",
+                "ocean temperature",
+                "ocean waves",
+                "precipitation",
+                "salinity/density",
+                "atmospheric winds",
+                "clouds"
+            ],
+            "landingPage": "https://doi.org/10.5067/SUBORBITAL/PISTON2019-ONR-NOAA/RVSALLYRIDE/DATA001",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>14.98 125.628 14.98 130.0 21.41 130.0 21.41 125.628 14.98 125.628</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2019-08-31T00:00:00Z/2019-09-26T23:59:59.999Z",
             "theme": [
                 "CAMP2Ex",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "PISTON 2019 Research Vessel (RV) Sally Ride Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-ROSINA-2-ESC2-V1.0",
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
+            "description": "This data set contains science\ndata acquired by the COPS, DFMS and RTOF ROSINA sensors between\n2015-03-11 and 2015-06-30 during the Escort phase 2 of the Rosetta\nmission at the comet 67P/CG",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rosina-2-esc2-v1.0_8enq-4scq",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-ROSINA-2-ESC2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rosina-2-esc2-v1.0_8enq-4scq",
-            "description": "This data set contains science\ndata acquired by the COPS, DFMS and RTOF ROSINA sensors between\n2015-03-11 and 2015-06-30 during the Escort phase 2 of the Rosetta\nmission at the comet 67P/CG",
-            "title": "ROSETTA-ORBITER 67P ROSINA 2 ESC2 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P ROSINA 2 ESC2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/8epm-qtb2",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Proton irradiation is touted for its improved tumor targeting due to the physical advantages of ion beams for radiotherapy. Recent studies from our laboratory have shown that in addition to targeting advantages proton irradiation can inhibit angiogenic and immune factors and thereby modulate tumor progression. High-energy protons also constitute a principal component of the galactic cosmic rays to which astronauts are exposed. Increased understanding of the biological effects of proton exposure would thus contribute to both improved cancer therapy and carcinogenesis risk assessment for space travel. In addition age plays a major role in tumor incidence and is a critical consideration for estimating cancer risk. We investigated the effects of host age and proton exposure on tumor progression. Tumor lag time and growth dynamics were tracked following injection of murine Lewis lung carcinoma (LLC) cells into young (68 day) versus old (736 day) mice with or without coincident irradiation. Tumor progression was suppressed in old compared to young mice. Differences in progression were further modulated by proton irradiation (1GeV) with increased inhibition evident in old mice. Through global transcriptome analysis TGFB1 and TGFB2 were determined to be key players that contributed to the tumor dynamics observed. These findings point to older hosts providing decreased systemic tumor support which can be further inhibited by proton irradiation. Overall design: For genome-wide expression profiling of tumor tissue Mouse WG-6 BeadArray chips (Illumina San Diego CA) were used. Total RNA was amplified with the Ambion Illumina TotalPrep Amplification Kit (Ambion Austin TX) and labeled from all replicate biological samples for each condition. For tumor replicates thirty tumor samples from adolescent and thirty tumor samples from old mice for a total of 60 tumor samples were used. All replicate samples were run individually. For each age group ten tumor samples had received proton irradiation while twenty tumor samples were from unirradiated mice (as described above). Total RNA was isolated and purified using TRIzol (Invitrogen) and quantified using an Agilent Bioanalyzer. Samples were deemed suitable for amplification and hybridization if they had 28s/18s = 2:1 RIN >7. Total RNA of 500ng per sample was amplified using AmbionTotalPrep and 1.5ug of the product was loaded onto the chips. Following hybridization at 55C the chips were washed and then scanned using the Illumina iScan System. The data was checked with GenomeStudio (Illumina) for quality control. In GenomeStudio data was background subtracted and rank invariant normalization was applied. Data was imported into MultiExperiment Viewer MeV for statistical analysis. The statistically significant genes were determined using MeV by applying a one-way ANOVA analysis with standard Bonferroni correction with a FDR <0.05 that resulted in a list of significant genes. Average gene expression signals <10 were filtered out due to signal being",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-131",
+                    "mediaType": "text/html",
+                    "title": "Proton irradiation augments the reduction in tumor progression observed with advanced age"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-131_8epm-qtb2",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "data collection",
                 "normalization data transformation",
@@ -359210,45 +359224,45 @@
                 "sample collection",
                 "ionzing radiation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/8epm-qtb2",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-131_8epm-qtb2",
-            "description": "Proton irradiation is touted for its improved tumor targeting due to the physical advantages of ion beams for radiotherapy. Recent studies from our laboratory have shown that in addition to targeting advantages proton irradiation can inhibit angiogenic and immune factors and thereby modulate tumor progression. High-energy protons also constitute a principal component of the galactic cosmic rays to which astronauts are exposed. Increased understanding of the biological effects of proton exposure would thus contribute to both improved cancer therapy and carcinogenesis risk assessment for space travel. In addition age plays a major role in tumor incidence and is a critical consideration for estimating cancer risk. We investigated the effects of host age and proton exposure on tumor progression. Tumor lag time and growth dynamics were tracked following injection of murine Lewis lung carcinoma (LLC) cells into young (68 day) versus old (736 day) mice with or without coincident irradiation. Tumor progression was suppressed in old compared to young mice. Differences in progression were further modulated by proton irradiation (1GeV) with increased inhibition evident in old mice. Through global transcriptome analysis TGFB1 and TGFB2 were determined to be key players that contributed to the tumor dynamics observed. These findings point to older hosts providing decreased systemic tumor support which can be further inhibited by proton irradiation. Overall design: For genome-wide expression profiling of tumor tissue Mouse WG-6 BeadArray chips (Illumina San Diego CA) were used. Total RNA was amplified with the Ambion Illumina TotalPrep Amplification Kit (Ambion Austin TX) and labeled from all replicate biological samples for each condition. For tumor replicates thirty tumor samples from adolescent and thirty tumor samples from old mice for a total of 60 tumor samples were used. All replicate samples were run individually. For each age group ten tumor samples had received proton irradiation while twenty tumor samples were from unirradiated mice (as described above). Total RNA was isolated and purified using TRIzol (Invitrogen) and quantified using an Agilent Bioanalyzer. Samples were deemed suitable for amplification and hybridization if they had 28s/18s = 2:1 RIN >7. Total RNA of 500ng per sample was amplified using AmbionTotalPrep and 1.5ug of the product was loaded onto the chips. Following hybridization at 55C the chips were washed and then scanned using the Illumina iScan System. The data was checked with GenomeStudio (Illumina) for quality control. In GenomeStudio data was background subtracted and rank invariant normalization was applied. Data was imported into MultiExperiment Viewer MeV for statistical analysis. The statistically significant genes were determined using MeV by applying a one-way ANOVA analysis with standard Bonferroni correction with a FDR <0.05 that resulted in a list of significant genes. Average gene expression signals <10 were filtered out due to signal being",
-            "title": "Proton irradiation augments the reduction in tumor progression observed with advanced age",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-131",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Proton irradiation augments the reduction in tumor progression observed with advanced age"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Proton irradiation augments the reduction in tumor progression observed with advanced age"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/8eqb-6r9s",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "To realistically evaluate the effects of the environment in space it is necessary to understand the effects of external factors during sample transport from Earth to space. The present study focused on temperature profiling the altered gene expression that develops under low cultivation temperatures in C. elegans used as a space life science model. The 7903 genes were selected as differentially expressed genes and divided into five sets with similar expression patterns using k-means clustering. Results from Gene Ontology analysis are significantly indicated that the cell cycle related genes and the TGF?/insulin-like signal pathway related genes changed. The TGF?/insulin-like signal pathway is expected to be activated due to low temperatures as well as by other stressors. To determine the genes whose expression changed four thermal conditions (10 15 20 and 25  xa1C) DNA microarray analysis was performed. The data consisted of 12 samples consisting of three biological replicates at each temperature.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-40",
+                    "mediaType": "text/html",
+                    "title": "Gene expression profiling of C. elegans under various thermal conditions"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-40_8eqb-6r9s",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "hybridization",
                 "p-gse14475-1",
@@ -359264,85 +359278,73 @@
                 "bioassay_data_transformation",
                 "feature_extraction"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/8eqb-6r9s",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-40_8eqb-6r9s",
-            "description": "To realistically evaluate the effects of the environment in space it is necessary to understand the effects of external factors during sample transport from Earth to space. The present study focused on temperature profiling the altered gene expression that develops under low cultivation temperatures in C. elegans used as a space life science model. The 7903 genes were selected as differentially expressed genes and divided into five sets with similar expression patterns using k-means clustering. Results from Gene Ontology analysis are significantly indicated that the cell cycle related genes and the TGF?/insulin-like signal pathway related genes changed. The TGF?/insulin-like signal pathway is expected to be activated due to low temperatures as well as by other stressors. To determine the genes whose expression changed four thermal conditions (10 15 20 and 25  xa1C) DNA microarray analysis was performed. The data consisted of 12 samples consisting of three biological replicates at each temperature.",
-            "title": "Gene expression profiling of C. elegans under various thermal conditions",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-40",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Gene expression profiling of C. elegans under various thermal conditions"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Gene expression profiling of C. elegans under various thermal conditions"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-PRL-67PCHURYUMOV-M03-V1.0",
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
+            "description": "This data set contains calibrated images acquired by the OSIRIS Wide Angle\nCamera during the prelanding phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-05-07 to 2014-06-04.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-prl-67pchuryumov-m03-v1.0_8eus-tgek",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-PRL-67PCHURYUMOV-M03-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-prl-67pchuryumov-m03-v1.0_8eus-tgek",
-            "description": "This data set contains calibrated images acquired by the OSIRIS Wide Angle\nCamera during the prelanding phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-05-07 to 2014-06-04.",
-            "title": "ROSETTA-ORBITER COMET PRELANDING OSIWAC 3 RDR DATA MTP 003",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMET PRELANDING OSIWAC 3 RDR DATA MTP 003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-ESC3-67PCHURYUMOV-M18-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-06-30T23:25:00.000 to 2015-07-28T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-esc3-67pchuryumov-m18-v3.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
@@ -359352,36 +359354,48 @@
                 "vega",
                 "zeta cas"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-ESC3-67PCHURYUMOV-M18-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-esc3-67pchuryumov-m18-v3.0",
-            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-06-30T23:25:00.000 to 2015-07-28T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 2 ESC3-MTP018 EDR V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 2 ESC3-MTP018 EDR V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/8evn-ed2m",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Distinct transcriptome profiles in response to low-LET and high-LET and different radiation qualities of HZE particles. Total RNA obtained from HBEC3KT cells after 1 4 12 and 24 hours of radiation. Mock-irradiated samples at each time point and control samples before radiation (0 hour) were also collected.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-73",
+                    "mediaType": "text/html",
+                    "title": "Transcriptome Profiles in Normal Human Bronchial Epithelial Cells after Exposure to gamma-rays and different HZE particles"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-73_8evn-ed2m",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "p-gse44282-3",
                 "p-gse44282-2",
@@ -359397,115 +359411,70 @@
                 "normalization data transformation protocol",
                 "nucleic acid extraction protocol"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/8evn-ed2m",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-73_8evn-ed2m",
-            "description": "Distinct transcriptome profiles in response to low-LET and high-LET and different radiation qualities of HZE particles. Total RNA obtained from HBEC3KT cells after 1 4 12 and 24 hours of radiation. Mock-irradiated samples at each time point and control samples before radiation (0 hour) were also collected.",
-            "title": "Transcriptome Profiles in Normal Human Bronchial Epithelial Cells after Exposure to gamma-rays and different HZE particles",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-73",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Transcriptome Profiles in Normal Human Bronchial Epithelial Cells after Exposure to gamma-rays and different HZE particles"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Transcriptome Profiles in Normal Human Bronchial Epithelial Cells after Exposure to gamma-rays and different HZE particles"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-3-PRL-CALIB-V1.0",
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
+            "description": "This dataset contains CALIBRATED raw data from the\nRosetta RPC-LAP instrument, acquired during the prelanding phase (PRL) at\ncomet 67P/Churyomov-Gerasimenko 1.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-3-prl-calib-v1.0_8ewu-fxn9",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-3-PRL-CALIB-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-3-prl-calib-v1.0_8ewu-fxn9",
-            "description": "This dataset contains CALIBRATED raw data from the\nRosetta RPC-LAP instrument, acquired during the prelanding phase (PRL) at\ncomet 67P/Churyomov-Gerasimenko 1.",
-            "title": "ROSETTA-ORBITER 67P RPCLAP 3 PRL CALIB V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCLAP 3 PRL CALIB V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.nasa.gov/centers/kennedy/launchingrockets/archives/2012.html",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2012-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://www.nasa.gov/centers/kennedy/launchingrockets/archives/elv_archive-index.html"
-            ],
-            "keyword": [
-                "time",
-                "expedition",
-                "history",
-                "atlas",
-                "delta",
-                "vehicle",
-                "landing",
-                "support",
-                "schedule",
-                "earth's bridge to space",
-                "pegasus",
-                "mission",
-                "elana",
-                "launch"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Brian Dunbar",
                 "hasEmail": "mailto:brian.dunbar@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-922",
             "description": "A list of launch vehicles launched for NASA missions in 2012.",
-            "title": "NASA Expendable Launch Vehicle Launch Archive 2012",
-            "programCode": [
-                "026:046"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -359543,147 +359512,189 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-922",
+            "issued": "2012-01-01",
+            "keyword": [
+                "time",
+                "expedition",
+                "history",
+                "atlas",
+                "delta",
+                "vehicle",
+                "landing",
+                "support",
+                "schedule",
+                "earth's bridge to space",
+                "pegasus",
+                "mission",
+                "elana",
+                "launch"
+            ],
+            "landingPage": "http://www.nasa.gov/centers/kennedy/launchingrockets/archives/2012.html",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:046"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "references": [
+                "http://www.nasa.gov/centers/kennedy/launchingrockets/archives/elv_archive-index.html"
+            ],
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "NASA Expendable Launch Vehicle Launch Archive 2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5880/GFZ.GRACE_06_GAA",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "GRACE. 2018-08-31. GRACE NON-TIDAL ATMOSPHERE GEOPOTENTIAL COEFFICIENTS GFZ (GAA). Version 6.0. GRACE_GAA_L2_GRAV_GFZ_RL06. JPL PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, GFZ. https://doi.org/10.5880/GFZ.GRACE_06_GAA. https://podaac-tools.jpl.nasa.gov/drive/files/allData/grace/docs/. GRACE, GFZ, 2018-08-31, GRACE NON-TIDAL ATMOSPHERE GEOPOTENTIAL COEFFICIENTS GFZ RELEASE 6.0 GAA, https://podaac-tools.jpl.nasa.gov/drive/files/allData/grace/docs/.",
-            "issued": "2018-08-06",
-            "temporal": "2002-04-05T00:00:00Z/2017-07-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-08-06",
-            "keyword": [
-                "ocean pressure",
-                "earth science",
-                "oceans",
-                "solid earth",
-                "gravity/gravitational field"
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
-            "identifier": "C2491772114-POCLOUD",
-            "description": "FOR EXPERT USE ONLY.  This dataset contains estimates of geopotential field derived from the Gravity Recovery and Climate Experiment (GRACE) mission measurements and a non-tidal atmospheric model produced by the German Research Centre for Geosciences (GFZ).  The data are in spherical harmonics averaged over approximately a month.  The primary objective of the GRACE mission is to obtain accurate estimates of the mean and time-variable components of the gravity field variations.  This objective is achieved by making continuous measurements of the change in distance between twin spacecraft, co-orbiting in about 500 km altitude, near circular, polar orbit, spaced approximately 200 km apart, using a microwave ranging system.  In addition to these range change, the non-gravitional forces are measured on each satellite using a high accuracy electrostatic, room-temperature accelerometer.  The satellite orientation and position (and timing) are precisely measured using twin star cameras and a GPS receiver, respectively.  Spatial and temporal variations in the gravity field affect the orbits (or trajectories) of the twin spacecraft differently.  These differences are manifested as changes in the distance between the spacecraft, as they orbit the Earth.  This change in distance is reflected in the time-of-flight of microwave signals transmitted and received nearly simultaneously between the two spacecraft.  The change in this time of fight is continuously measured by tracking the phase of the microwave carrier signals.  The so called dual-one-way range change measurements can be reconstructed from these phase measurements.  This range change (or its numerically derived derivatives), along with other mission and ancillary data, is subsequently analyzed to extract the parameters of an Earth gravity field model.",
-            "release-place": "JPL PO.DAAC",
-            "series-name": "GRACE NON-TIDAL ATMOSPHERE GEOPOTENTIAL COEFFICIENTS GFZ (GAA)",
-            "graphic-preview-description": "Thumbnail",
             "creator": "GRACE",
-            "title": "GRACE NON-TIDAL ATMOSPHERE GEOPOTENTIAL COEFFICIENTS GFZ RELEASE 6.0 GAA",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GRACE_GAA_L2_GRAV_GFZ_RL06.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "FOR EXPERT USE ONLY.  This dataset contains estimates of geopotential field derived from the Gravity Recovery and Climate Experiment (GRACE) mission measurements and a non-tidal atmospheric model produced by the German Research Centre for Geosciences (GFZ).  The data are in spherical harmonics averaged over approximately a month.  The primary objective of the GRACE mission is to obtain accurate estimates of the mean and time-variable components of the gravity field variations.  This objective is achieved by making continuous measurements of the change in distance between twin spacecraft, co-orbiting in about 500 km altitude, near circular, polar orbit, spaced approximately 200 km apart, using a microwave ranging system.  In addition to these range change, the non-gravitional forces are measured on each satellite using a high accuracy electrostatic, room-temperature accelerometer.  The satellite orientation and position (and timing) are precisely measured using twin star cameras and a GPS receiver, respectively.  Spatial and temporal variations in the gravity field affect the orbits (or trajectories) of the twin spacecraft differently.  These differences are manifested as changes in the distance between the spacecraft, as they orbit the Earth.  This change in distance is reflected in the time-of-flight of microwave signals transmitted and received nearly simultaneously between the two spacecraft.  The change in this time of fight is continuously measured by tracking the phase of the microwave carrier signals.  The so called dual-one-way range change measurements can be reconstructed from these phase measurements.  This range change (or its numerically derived derivatives), along with other mission and ancillary data, is subsequently analyzed to extract the parameters of an Earth gravity field model.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5880%2FGFZ.GRACE_06_GAA",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5880%2FGFZ.GRACE_06_GAA",
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
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/grace/retired/docs/L2-GFZ_ProcStds_RL06_DRAFT.pdf",
-                    "description": "GFZ Level-2 Processing Standards Document For Level-2 Product Release 06",
                     "@type": "dcat:Distribution",
+                    "description": "GFZ Level-2 Processing Standards Document For Level-2 Product Release 06",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/grace/retired/docs/L2-GFZ_ProcStds_RL06_DRAFT.pdf",
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
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GRACE_GAA_L2_GRAV_GFZ_RL06.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GRACE_GAA_L2_GRAV_GFZ_RL06.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772114-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772114-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772114-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772114-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GRACE_GAA_L2_GRAV_GFZ_RL06.jpg",
+            "identifier": "C2491772114-POCLOUD",
+            "issued": "2018-08-06",
+            "keyword": [
+                "ocean pressure",
+                "earth science",
+                "oceans",
+                "solid earth",
+                "gravity/gravitational field"
+            ],
+            "landingPage": "https://doi.org/10.5880/GFZ.GRACE_06_GAA",
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
+            "series-name": "GRACE NON-TIDAL ATMOSPHERE GEOPOTENTIAL COEFFICIENTS GFZ (GAA)",
             "spatial": "-180.0 -88.0 180.0 88.0",
+            "temporal": "2002-04-05T00:00:00Z/2017-07-01T00:00:00Z",
             "theme": [
                 "GRACE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GRACE NON-TIDAL ATMOSPHERE GEOPOTENTIAL COEFFICIENTS GFZ RELEASE 6.0 GAA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/8f32-6cxc",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Kim Tolbert",
+                "hasEmail": "mailto:kim.tolbert@nasa.gov"
+            },
+            "description": "Time histories of NaI, GBO, and GOES data, with flare and day/night markers. Orbital plots are on RHESSI orbit times.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://sprg.ssl.berkeley.edu/~tohban/browser/?show=grth1+qlpcr+gbmd+gbmo&date=20131024&time=055723",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000245",
             "issued": "2018-06-25",
-            "temporal": "2008-08-12/2014-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "telescope",
                 "nai",
@@ -359693,192 +359704,160 @@
                 "gbm",
                 "gbo"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kim Tolbert",
-                "hasEmail": "mailto:kim.tolbert@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/8f32-6cxc",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000245",
-            "description": "Time histories of NaI, GBO, and GOES data, with flare and day/night markers. Orbital plots are on RHESSI orbit times.",
-            "title": "GBM Quicklook Daily and Orbital Plots",
-            "programCode": [
-                "026:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://sprg.ssl.berkeley.edu/~tohban/browser/?show=grth1+qlpcr+gbmd+gbmo&date=20131024&time=055723",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
+            "temporal": "2008-08-12/2014-01-01",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "GBM Quicklook Daily and Orbital Plots"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-UVIS-2-SSB-V1.0",
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
+            "description": "Photometric observations of stellar occultations by Saturnian rings, satellites, atmospheres, and Jovian atmosphere.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-uvis-2-ssb-v1.0_8f4p-fgnj",
+            "issued": "2018-06-26",
+            "keyword": [
+                "cassini-huygens",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-UVIS-2-SSB-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-uvis-2-ssb-v1.0_8f4p-fgnj",
-            "description": "Photometric observations of stellar occultations by Saturnian rings, satellites, atmospheres, and Jovian atmosphere.",
-            "title": "CASSINI SATURN UVIS SOLAR STELLAR BRIGHTNESS TIME SERIES 1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI SATURN UVIS SOLAR STELLAR BRIGHTNESS TIME SERIES 1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/561/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2012-03-27",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "nasa",
-                "ames",
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
-            "identifier": "DASHLINK_561",
             "description": "Please upload your BSCW grids here.  Thank you.",
-            "title": "BSCW Grid Depository",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/plain",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/README_RUAG_grids_3.txt",
-                    "description": "Information on RUAG grids",
                     "@type": "dcat:Distribution",
+                    "description": "Information on RUAG grids",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/README_RUAG_grids_3.txt",
+                    "mediaType": "text/plain",
                     "title": "README_RUAG_grids.txt"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ruag_bscw.tar.gz",
-                    "description": "RUAG BSCW grids",
                     "@type": "dcat:Distribution",
+                    "description": "RUAG BSCW grids",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ruag_bscw.tar.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "ruag_bscw.tar.gz"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ruag_3.md5sum",
-                    "description": "Checksum for RUAG grid archives",
                     "@type": "dcat:Distribution",
+                    "description": "Checksum for RUAG grid archives",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ruag_3.md5sum",
+                    "mediaType": "application/octet-stream",
                     "title": "ruag.md5sum"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_561",
+            "issued": "2012-03-27",
+            "keyword": [
+                "nasa",
+                "ames",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/561/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "BSCW Grid Depository"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-MAG-4-RDR-S3COORDS-1.92SEC-V1.1",
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
-                "jupiter"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-mag-4-rdr-s3coords-1.92sec-v1.1_8f6r-ek5j",
+            "issued": "2018-06-26",
+            "keyword": [
+                "voyager",
+                "jupiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-MAG-4-RDR-S3COORDS-1.92SEC-V1.1",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-mag-4-rdr-s3coords-1.92sec-v1.1_8f6r-ek5j",
-            "description": "not applicable",
-            "title": "VG1 JUP MAG RESAMPLED SYSTEM III (1965) COORDS 1.92SEC V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG1 JUP MAG RESAMPLED SYSTEM III (1965) COORDS 1.92SEC V1.1"
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
-            ],
-            "keyword": [
-                "weather",
-                "flight",
-                "safety",
-                "aviation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Linda J. Connell",
                 "hasEmail": "mailto:linda.j.connell@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-815",
             "description": "A sampling of reports from both air carrier flight crews and GA pilots referencing encounters with severe or unforecast weather.",
-            "title": "Aviation Safety Reporting System: Inflight Weather Encounters",
-            "programCode": [
-                "026:021"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -359886,98 +359865,133 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-815",
+            "issued": "2018-06-25",
+            "keyword": [
+                "weather",
+                "flight",
+                "safety",
+                "aviation"
+            ],
+            "landingPage": "http://asrs.arc.nasa.gov/search/reportsets.html",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:021"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "references": [
+                "http://asrs.arc.nasa.gov/"
+            ],
             "theme": [
                 "Aerospace"
-            ]
+            ],
+            "title": "Aviation Safety Reporting System: Inflight Weather Encounters"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TERRA/MODIS/L3B/FLH/2022",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/TERRA/MODIS/L3B/FLH/2022.",
-            "issued": "2019-06-23",
-            "temporal": "2000-02-24T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-08-08",
-            "keyword": [
-                "earth science",
-                "oceans",
-                "ocean optics",
-                "ngda",
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
-            "identifier": "C2331486254-OB_DAAC",
             "description": "MODIS (or Moderate-Resolution Imaging Spectroradiometer) is a key instrument aboard the Terra (EOS AM) and Aqua (EOS PM) satellites. Terra's orbit around the Earth is timed so that it passes from north to south across the equator in the morning, while Aqua passes south to north over the equator in the afternoon. Terra MODIS and Aqua MODIS are viewing the entire Earth's surface every 1 to 2 days, acquiring data in 36 spectral bands, or groups of wavelengths (see MODIS Technical Specifications). These data will improve our understanding of global dynamics and processes occurring on the land, in the oceans, and in the lower atmosphere. MODIS is playing a vital role in the development of validated, global, interactive Earth system models able to predict global change accurately enough to assist policy makers in making sound decisions concerning the protection of our environment.",
-            "title": "Terra MODIS Global Binned Fluorescence Line Height (FLH) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMODIS%2FL3B%2FFLH%2F2022",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMODIS%2FL3B%2FFLH%2F2022",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/TERRA/MODIS/L3B/FLH/2022",
-                    "description": "MODIS-Terra L3B Fluorescence Line Height (FLH) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS-Terra L3B Fluorescence Line Height (FLH) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/TERRA/MODIS/L3B/FLH/2022",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2331486254-OB_DAAC",
+            "issued": "2019-06-23",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "ocean optics",
+                "ngda",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://doi.org/10.5067/TERRA/MODIS/L3B/FLH/2022",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-08-08",
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
+            "title": "Terra MODIS Global Binned Fluorescence Line Height (FLH) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/8f83-f37e",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Physical forces greatly influence the growth and function of an organism. Altered gravity can perturb normal development and induce corresponding changes in gene expression. Understanding this relationship between the physical and biological realms is important for NASA  s space travel goals. We use combined RNA-Seq and qRT-PCR to profile changes in early Drosophila melanogaster pupae exposed to chronic hypergravity (3 g three times Earth  s gravity) to highlight gravity-dependent pathways and gene products. Robust transcriptional response was evident among the pupae developed in a hypergravity environment compared to control. 1,513 genes showed significantly (p < 0.05) altered gene expression in the 3 g samples. These findings were supported with qRT-PCR data. Major biological processes affected include ion transport redox homeostasis immune and humoral stress response proteolysis and cuticle development.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-85",
+                    "mediaType": "text/html",
+                    "title": "Transcriptomic response of Drosophila melanogaster pupae developed in hypergravity"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-85_8f83-f37e",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "nucleic acid sequencing",
                 "growth protocol",
@@ -359987,155 +360001,142 @@
                 "sequence analysis data transformation",
                 "nucleic acid extraction"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/8f83-f37e",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-85_8f83-f37e",
-            "description": "Physical forces greatly influence the growth and function of an organism. Altered gravity can perturb normal development and induce corresponding changes in gene expression. Understanding this relationship between the physical and biological realms is important for NASA  s space travel goals. We use combined RNA-Seq and qRT-PCR to profile changes in early Drosophila melanogaster pupae exposed to chronic hypergravity (3 g three times Earth  s gravity) to highlight gravity-dependent pathways and gene products. Robust transcriptional response was evident among the pupae developed in a hypergravity environment compared to control. 1,513 genes showed significantly (p < 0.05) altered gene expression in the 3 g samples. These findings were supported with qRT-PCR data. Major biological processes affected include ion transport redox homeostasis immune and humoral stress response proteolysis and cuticle development.",
-            "title": "Transcriptomic response of Drosophila melanogaster pupae developed in hypergravity",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-85",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Transcriptomic response of Drosophila melanogaster pupae developed in hypergravity"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Transcriptomic response of Drosophila melanogaster pupae developed in hypergravity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-CAL-ROMAP-3-CR2-MAG-V1.0",
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
+            "description": "This archive contains level 3 data from the ROMAP-MAG instrument onboard ROSETTA Lander, acquired during the CR2 (cruise 2) phase. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-cal-romap-3-cr2-mag-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "calibration",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-CAL-ROMAP-3-CR2-MAG-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-cal-romap-3-cr2-mag-v1.0",
-            "description": "This archive contains level 3 data from the ROMAP-MAG instrument onboard ROSETTA Lander, acquired during the CR2 (cruise 2) phase. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER CAL ROMAP 3 CR2 MAG\n                            V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-LANDER CAL ROMAP 3 CR2 MAG\n                            V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/RTOB6O2I1CDC",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "IceBridge L1B Flight Reports V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/RTOB6O2I1CDC.",
-            "issued": "2009-03-30",
-            "temporal": "2009-03-30T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-11-20",
-            "keyword": [
-                "earth science",
-                "platform characteristics",
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
-            "identifier": "C1533906518-NSIDC_ECS",
             "description": "This data set contains flight reports from NASA Operation IceBridge Greenland, Arctic, Antarctic, and Alaska missions. Flight reports contain information on region, mission, aircraft model, flight data, purpose of flight, and on-board sensors. The flight reports were collected as part of Operation IceBridge funded aircraft survey campaigns.The corresponding flight lines can be found in the IceBridge L1B Thinned Flight Lines (IPFLT1B) data set.",
-            "title": "IceBridge L1B Flight Reports V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FRTOB6O2I1CDC",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FRTOB6O2I1CDC",
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
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/IPFLR1B.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/IPFLR1B.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=IPFLR1B",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=IPFLR1B",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/IPFLR1B/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/IPFLR1B/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/RTOB6O2I1CDC",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/RTOB6O2I1CDC",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/RTOB6O2I1CDC",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/RTOB6O2I1CDC",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1533906518-NSIDC_ECS",
+            "issued": "2009-03-30",
+            "keyword": [
+                "earth science",
+                "platform characteristics",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/RTOB6O2I1CDC",
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
+            "temporal": "2009-03-30T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "2009_AK_UAF",
                 "2009_AN_NASA",
@@ -360169,299 +360170,279 @@
                 "2019_GR_NASA",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "IceBridge L1B Flight Reports V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FCAL-ALICE-2-EXT2-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains CODMAC Level 2 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the comet 67P/Churyumov-Gerasimenko Rosetta Extension 2 mission phase, which took place between 2016-04-06 and 2016-06-30.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cal-alice-2-ext2-v1.0_8fec-prwj",
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
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FCAL-ALICE-2-EXT2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cal-alice-2-ext2-v1.0_8fec-prwj",
-            "description": "This data set contains CODMAC Level 2 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the comet 67P/Churyumov-Gerasimenko Rosetta Extension 2 mission phase, which took place between 2016-04-06 and 2016-06-30.",
-            "title": "ROSETTA-ORBITER 67P/CAL ALICE 2 EXT2 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P/CAL ALICE 2 EXT2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/461",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Roulet, N.T. 1999. BOREAS TGB-04 Water and Sediment Temperature Data over the NSA-BP (Beaver Pond). ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/461",
-            "issued": "2023-11-22",
-            "temporal": "1994-05-28T00:00:00Z/1994-09-18T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-28",
-            "keyword": [
-                "earth science",
-                "erosion/sedimentation",
-                "terrestrial hydrosphere",
-                "soils",
-                "land surface",
-                "water quality/water chemistry"
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
-            "identifier": "C2808091319-ORNL_CLOUD",
             "description": "Contains TGB-04  water and sediment temperature data for northern study area (tower beaver pond site).",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS TGB-04 Water and Sediment Temperature Data over the NSA-BP (Beaver Pond)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F461",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F461",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/GRAB_BAG/tgb4wsed/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/GRAB_BAG/tgb4wsed/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TGB04_Water_Sed_Temp.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TGB04_Water_Sed_Temp.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/461",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/461",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/GRAB_BAG/tgb4wsed/comp/TGB04_Water_Sed_Temp.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/GRAB_BAG/tgb4wsed/comp/TGB04_Water_Sed_Temp.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/GRAB_BAG/tgb4wsed/comp/TGB04_Water_Sed_Temp.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/GRAB_BAG/tgb4wsed/comp/TGB04_Water_Sed_Temp.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/GRAB_BAG/tgb4wsed/comp/TGB04_Water_Sed_Temp.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/GRAB_BAG/tgb4wsed/comp/TGB04_Water_Sed_Temp.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/GRAB_BAG/tgb4wsed/comp/tgb4wsed.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/GRAB_BAG/tgb4wsed/comp/tgb4wsed.def",
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
+            "identifier": "C2808091319-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "earth science",
+                "erosion/sedimentation",
+                "terrestrial hydrosphere",
+                "soils",
+                "land surface",
+                "water quality/water chemistry"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/461",
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
             "spatial": "55.84 -98.03",
+            "temporal": "1994-05-28T00:00:00Z/1994-09-18T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS TGB-04 Water and Sediment Temperature Data over the NSA-BP (Beaver Pond)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/644/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2012-12-04",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "nasa",
-                "ames"
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
-            "identifier": "DASHLINK_644",
             "description": "The following zip files contain individual flight recorded data in Matlab file format. There are 186 parameters each with a data structure that contains the following:\r\n\r\n<pre>\r\n-sensor recordings\r\n-sampling rate\r\n-units\r\n-parameter description\r\n-parameter ID\r\n</pre>",
-            "title": "Flight Data For Tail 666",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_666_1.zip",
-                    "description": "Tail 666 Set 1",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 666 Set 1",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_666_1.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_666_1.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_666_2.zip",
-                    "description": "Tail 666 Set 2",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 666 Set 2",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_666_2.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_666_2.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_666_3.zip",
-                    "description": "Tail 666 Set 3",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 666 Set 3",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_666_3.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_666_3.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_666_4.zip",
-                    "description": "Tail 666 Set 4",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 666 Set 4",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_666_4.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_666_4.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_666_5.zip",
-                    "description": "Tail 666 Set 5",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 666 Set 5",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_666_5.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_666_5.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_666_6.zip",
-                    "description": "Tail 666 Set 6",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 666 Set 6",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_666_6.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_666_6.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_666_7.zip",
-                    "description": "Tail 666 Set 7",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 666 Set 7",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_666_7.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_666_7.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_666_10.zip",
-                    "description": "Tail_666 Set 10\n",
                     "@type": "dcat:Distribution",
+                    "description": "Tail_666 Set 10\n",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_666_10.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_666_10.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_666_11.zip",
-                    "description": "Tail_666 Set 11\n",
                     "@type": "dcat:Distribution",
+                    "description": "Tail_666 Set 11\n",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_666_11.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_666_11.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_666_8.zip",
-                    "description": "Tail_666 Set 8\n",
                     "@type": "dcat:Distribution",
+                    "description": "Tail_666 Set 8\n",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_666_8.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_666_8.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_666_9.zip",
-                    "description": "Tail_666 Set 9\n",
                     "@type": "dcat:Distribution",
+                    "description": "Tail_666 Set 9\n",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_666_9.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_666_9.zip"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_644",
+            "issued": "2012-12-04",
+            "keyword": [
+                "dashlink",
+                "nasa",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/644/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Flight Data For Tail 666"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-Release.shtml",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-26",
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
-            "identifier": "NASA-758",
             "description": "RSS",
-            "title": "PDS Odyssey Radio Science Data (43)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -360469,47 +360450,44 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-758",
+            "issued": "2018-06-26",
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
+            "title": "PDS Odyssey Radio Science Data (43)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1273652199-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA Goddard Space Flight Center (GSFC). 2013-12-27. THIRN5L1CH115. Version 001. THIR/Nimbus-5 Level 1 Meteorological Radiation Data at 11.5 microns V001. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/THIRN5L1CH115_001.html. Digital Science Data.",
-            "issued": "2013-12-27",
-            "temporal": "1972-12-19T00:00:00Z/1975-03-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2013-12-27",
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
-            "identifier": "C1273652199-GES_DISC",
-            "description": "THIRN5L1CH115 is the Nimbus-5 Temperature-Humidity Infrared Radiometer (THIR) Level 1 Meteorological Radiation Data at 11.5 microns product and contains radiances expressed in units of equivalent brightness temperature measured in the 10.5 - 12.5 (11.5) micron channel. The data, originally written on IBM 360 machines, were recovered from magnetic tapes, also referred to as Nimbus Meteorological Radiation Tapes (NMRT-THIR). The data are archived in their original IBM 36-bit word proprietary format, also referred to as a binary TAP file.\n\nThe Nimbus-5 satellite was successfully launched on December 11, 1972. The THIR experiment on Nimbus-5 continued the measurements made by its predecessor flown on Nimbus-4. The THIR instrument is a two channel high resolution scanning radiometer designed to perform two major functions:* The 11.5 micron channel provides both day and night cloud top or surface temperatures. The ground resolution at the sub-point is 8 km and operates day and night.* The 6.7 micron channel gives information on the moisture content of the upper troposphere and stratosphere and the location of jet streams and frontal systems. The water vapor channel has a resolution of the sub-point is 22 km and operates mostly at night. The THIR Principal Investigator was Andrew W. McCulloch from NASA Goddard Space Flight Center. The Nimbus-5 THIR data are available from December 19, 1972 (day of year 354) through March 1, 1975 (day of year 60). The THIRN5L1CH67 product contains the 6.7 micron channel data.\n\nThis product was previously available from the NSSDC with the identifier ESAD-00020 (old ID 72-097A-08C).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "THIRN5L1CH115",
             "creator": "NASA Goddard Space Flight Center (GSFC)",
-            "title": "THIR/Nimbus-5 Level 1 Meteorological Radiation Data at 11.5 microns V001 (THIRN5L1CH115) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/THIRN5L1CH115_001.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "THIRN5L1CH115 is the Nimbus-5 Temperature-Humidity Infrared Radiometer (THIR) Level 1 Meteorological Radiation Data at 11.5 microns product and contains radiances expressed in units of equivalent brightness temperature measured in the 10.5 - 12.5 (11.5) micron channel. The data, originally written on IBM 360 machines, were recovered from magnetic tapes, also referred to as Nimbus Meteorological Radiation Tapes (NMRT-THIR). The data are archived in their original IBM 36-bit word proprietary format, also referred to as a binary TAP file.\n\nThe Nimbus-5 satellite was successfully launched on December 11, 1972. The THIR experiment on Nimbus-5 continued the measurements made by its predecessor flown on Nimbus-4. The THIR instrument is a two channel high resolution scanning radiometer designed to perform two major functions:* The 11.5 micron channel provides both day and night cloud top or surface temperatures. The ground resolution at the sub-point is 8 km and operates day and night.* The 6.7 micron channel gives information on the moisture content of the upper troposphere and stratosphere and the location of jet streams and frontal systems. The water vapor channel has a resolution of the sub-point is 22 km and operates mostly at night. The THIR Principal Investigator was Andrew W. McCulloch from NASA Goddard Space Flight Center. The Nimbus-5 THIR data are available from December 19, 1972 (day of year 354) through March 1, 1975 (day of year 60). The THIRN5L1CH67 product contains the 6.7 micron channel data.\n\nThis product was previously available from the NSSDC with the identifier ESAD-00020 (old ID 72-097A-08C).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -360518,896 +360496,919 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/THIRN5L1CH115_001.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/THIRN5L1CH115_001.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus5_THIR_Level1/THIRN5L1CH115.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus5_THIR_Level1/THIRN5L1CH115.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=THIRN5L1CH115",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=THIRN5L1CH115",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus5_THIR_Level1/THIRN5L1CH115.001/doc/README.THIRN5L1.001.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus5_THIR_Level1/THIRN5L1CH115.001/doc/README.THIRN5L1.001.pdf",
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
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/N5_THIR_Ch115_Inventory.xlsx",
-                    "description": "N5 THIR Ch 11.5 Inventory",
                     "@type": "dcat:Distribution",
+                    "description": "N5 THIR Ch 11.5 Inventory",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/N5_THIR_Ch115_Inventory.xlsx",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/THIRN5L1CH115_001.png",
+            "identifier": "C1273652199-GES_DISC",
+            "issued": "2013-12-27",
+            "keyword": [
+                "infrared wavelengths",
+                "spectral/engineering",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1273652199-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2013-12-27",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "THIRN5L1CH115",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1972-12-19T00:00:00Z/1975-03-01T23:59:59.999Z",
             "theme": [
                 "Nimbus",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "THIR/Nimbus-5 Level 1 Meteorological Radiation Data at 11.5 microns V001 (THIRN5L1CH115) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQR50-3YMAE",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA Aquarius project. 2017-12-07. Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Ascending Monthly Data. Version 5.0. Aquarius Sea Surface Salinity Products. Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC OBPG. https://doi.org/10.5067/AQR50-3YMAE. http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius. NASA Aquarius project, NASA/GSFC OBPG, 2017-12-07, Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Ascending Monthly Data V5.0, http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius.",
-            "issued": "2017-10-21",
-            "temporal": "2011-08-25T01:55:23Z/2015-06-07T11:41:38Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-07",
-            "keyword": [
-                "oceans",
-                "salinity/density",
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
-            "identifier": "C2491757076-POCLOUD",
-            "description": "Aquarius Level 3 sea surface salinity (SSS) rain-flagged standard mapped image data contains gridded 1 degree spatial resolution SSS averaged over daily, 7 day, monthly, and seasonal time\nscales. This particular data set is the Monthly, Ascending rain-flagged rain-flagged sea surface salinity product for version 5.0 of the Aquarius data set. Only retrieved values for Ascending passes have been used to create this product.  The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
-            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA",
-            "series-name": "Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Ascending Monthly Data",
-            "graphic-preview-description": "Thumbnail",
             "creator": "NASA Aquarius project",
-            "title": "Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Ascending Monthly Data V5.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS-RainFlagged_SMIA_MONTHLY_V5.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Aquarius Level 3 sea surface salinity (SSS) rain-flagged standard mapped image data contains gridded 1 degree spatial resolution SSS averaged over daily, 7 day, monthly, and seasonal time\nscales. This particular data set is the Monthly, Ascending rain-flagged rain-flagged sea surface salinity product for version 5.0 of the Aquarius data set. Only retrieved values for Ascending passes have been used to create this product.  The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3YMAE",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3YMAE",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS-RainFlagged_SMIA_MONTHLY_V5.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS-RainFlagged_SMIA_MONTHLY_V5.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491757076-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491757076-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491757076-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491757076-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS-RainFlagged_SMIA_MONTHLY_V5.jpg",
+            "identifier": "C2491757076-POCLOUD",
+            "issued": "2017-10-21",
+            "keyword": [
+                "oceans",
+                "salinity/density",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQR50-3YMAE",
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
+            "series-name": "Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Ascending Monthly Data",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T01:55:23Z/2015-06-07T11:41:38Z",
             "theme": [
                 "AQUARIUS SAC-D",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Ascending Monthly Data V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/342OHQM9AK6Q",
             "citation": "Beaudoing, H. and M. Rodell, NASA/GSFC/HSL. 2019-11-19. GLDAS_NOAH025_3H. Version 2.0. GLDAS Noah Land Surface Model L4 3 hourly 0.25 x 0.25 degree V2.0. Greenbelt, Maryland, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/342OHQM9AK6Q. https://disc.gsfc.nasa.gov/datacollection/GLDAS_NOAH025_3H_2.0.html. Digital Science Data.",
-            "issued": "2019-11-19",
-            "temporal": "1948-01-01T00:00:00Z/2014-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-11-19",
-            "references": [
-                "https://doi.org/10.1175/BAMS-85-3-381"
-            ],
-            "keyword": [
-                "surface thermal properties",
-                "earth science",
-                "land surface",
-                "precipitation",
-                "snow/ice",
-                "atmospheric winds",
-                "terrestrial hydrosphere",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "atmospheric radiation",
-                "atmospheric pressure",
-                "surface water",
-                "soils",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "HUALAN RUI",
                 "hasEmail": "mailto:Hualan.Rui@nasa.gov"
             },
+            "creator": "Beaudoing, H. and M. Rodell, NASA/GSFC/HSL",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1233767545-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "NASA Global Land Data Assimilation System Version 2 (GLDAS-2) has three components: GLDAS-2.0, GLDAS-2.1, and GLDAS-2.2. GLDAS-2.0 is forced entirely with the Princeton meteorological forcing input data and provides a temporally consistent series from 1948 through 2014. GLDAS-2.1 is forced with a combination of model and observation data from 2000 to present. GLDAS-2.2 product suites use data assimilation (DA), whereas the GLDAS-2.0 and GLDAS-2.1 products are \"open-loop\" (i.e., no data assimilation). The choice of forcing data, as well as DA observation source, variable, and scheme, vary for different GLDAS-2.2 products.\n\nThis data product, GLDAS-2.0 0.25 degree 3-hourly, was reprocessed and replaced its previous data product on November 27, 2019.  The data product contains a series of land surface parameters simulated from the Noah Model 3.6, and currently covers from January 1948 to December 2014, but will be extended as the data becomes available.  The GLDAS-2.0 data are archived and distributed in netCDF format.\n\nThe GLDAS-2.0 model simulations were initialized on simulation date January 1, 1948, using soil moisture and other state fields from the LSM climatology for that day of the year. The simulations were forced by the global meteorological forcing data set from Princeton University (Sheffield et al., 2006). Each simulation uses the common GLDAS data sets for land water mask (MOD44W: Carroll et al., 2009) and elevation (GTOPO30) along with the model default land cover and soils datasets. Noah model uses the Modified IGBP MODIS 20-category vegetation classification and the soil texture based on the Hybrid STATSGO/FAO) datasets. The MODIS based land surface parameters are used in the current GLDAS-2.0 and GLDAS-2.1 products while the AVHRR base parameters were used in GLDAS-1 and previous GLDAS-2 products (prior to October 2012). \n\nIn October 2020, all 3-hourly and monthly GLDAS-2 data were post-processed with the MOD44W MODIS land mask.  Previously, some grid boxes over inland water were considered as over land and, thus, had non-missing values.  The post-processing corrected this issue and masked out all model output data over inland water; the post-processing did not affect the meteorological forcing variables. More information can be found in the GLDAS-2 README.  The MOD44W MODIS land mask is available on the GLDAS Project site.\n\nIf you had downloaded the GLDAS data prior to November 2020, please download the data again to receive the post-processed data.",
-            "release-place": "Greenbelt, Maryland, USA",
-            "series-name": "GLDAS_NOAH025_3H",
-            "creator": "Beaudoing, H. and M. Rodell, NASA/GSFC/HSL",
-            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
-            "title": "GLDAS Noah Land Surface Model L4 3 hourly 0.25 x 0.25 degree V2.0 (GLDAS_NOAH025_3H) at GES DISC",
-            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=GLDAS_NOAH025_3H_2_0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F342OHQM9AK6Q",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F342OHQM9AK6Q",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GLDAS_NOAH025_3H_2.0.png",
-                    "description": "GLDAS-2.0 Noah 3-ourly 0.25 Degree 0 - 10 cm soil moisture content [kg m-2] for 03Z Jan. 01, 1948.",
                     "@type": "dcat:Distribution",
+                    "description": "GLDAS-2.0 Noah 3-ourly 0.25 Degree 0 - 10 cm soil moisture content [kg m-2] for 03Z Jan. 01, 1948.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GLDAS_NOAH025_3H_2.0.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GLDAS_NOAH025_3H_2.0.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GLDAS_NOAH025_3H_2.0.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/GLDAS/GLDAS_NOAH025_3H.2.0/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/GLDAS/GLDAS_NOAH025_3H.2.0/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GLDAS_NOAH025_3H_2.0",
-                    "description": "Use the Earthdata Search Client (EDSC) to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client (EDSC) to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GLDAS_NOAH025_3H_2.0",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=GLDAS_NOAH025_3H_2_0",
-                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
                     "@type": "dcat:Distribution",
+                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=GLDAS_NOAH025_3H_2_0",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through GIOVANNI"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/opendap/hyrax/GLDAS/GLDAS_NOAH025_3H.2.0/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/opendap/hyrax/GLDAS/GLDAS_NOAH025_3H.2.0/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/dods/GLDAS_NOAH025_3H.2.0/",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/dods/GLDAS_NOAH025_3H.2.0/",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/GLDAS/GLDAS_NOAH025_3H.2.0/doc/README_GLDAS2.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/GLDAS/GLDAS_NOAH025_3H.2.0/doc/README_GLDAS2.pdf",
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
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/thredds/catalog/GLDAS_aggregation/GLDAS_NOAH025_3H.2.0/catalog.html",
-                    "description": "Time aggregated THREDDS Data Server (TDS)",
                     "@type": "dcat:Distribution",
+                    "description": "Time aggregated THREDDS Data Server (TDS)",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/thredds/catalog/GLDAS_aggregation/GLDAS_NOAH025_3H.2.0/catalog.html",
+                    "mediaType": "text/html",
                     "title": "Use THREDDS DATA to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=GLDAS_NOAH025_3H_2_0",
+            "identifier": "C1233767545-GES_DISC",
+            "issued": "2019-11-19",
+            "keyword": [
+                "surface thermal properties",
+                "earth science",
+                "land surface",
+                "precipitation",
+                "snow/ice",
+                "atmospheric winds",
+                "terrestrial hydrosphere",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "atmospheric radiation",
+                "atmospheric pressure",
+                "surface water",
+                "soils",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/342OHQM9AK6Q",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-11-19",
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
+            "series-name": "GLDAS_NOAH025_3H",
             "spatial": "-180.0 -60.0 180.0 90.0",
+            "temporal": "1948-01-01T00:00:00Z/2014-12-31T23:59:59.999Z",
             "theme": [
                 "GLDAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GLDAS Noah Land Surface Model L4 3 hourly 0.25 x 0.25 degree V2.0 (GLDAS_NOAH025_3H) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/LARGE_RIVER_DOC_EXPORT/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/LARGE_RIVER_DOC_EXPORT/DATA001.",
-            "issued": "2015-05-23",
-            "temporal": "2015-05-23T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean optics",
-                "salinity/density",
-                "ocean temperature",
-                "oceans",
-                "earth science",
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
-            "identifier": "C1633360426-OB_DAAC",
             "description": "Measurements taken as a part of a project to quanitfy and assess the export of dissolved organic carbon by large rivers.",
-            "title": "Export of dissolved organic carbon (DOC) by large rivers",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FLARGE_RIVER_DOC_EXPORT%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FLARGE_RIVER_DOC_EXPORT%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Large_River_DOC_Export/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Large_River_DOC_Export/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360426-OB_DAAC",
+            "issued": "2015-05-23",
+            "keyword": [
+                "ocean optics",
+                "salinity/density",
+                "ocean temperature",
+                "oceans",
+                "earth science",
+                "ocean chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/LARGE_RIVER_DOC_EXPORT/DATA001",
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
+            "temporal": "2015-05-23T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Export of dissolved organic carbon (DOC) by large rivers"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CL5ZRBCEF8G3",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SnowEx20 Grand Mesa IOP BSU Multi-polarization 1 GHz GPR CMP Raw V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/CL5ZRBCEF8G3.",
-            "issued": "2020-01-31",
-            "temporal": "2020-01-31T00:00:00Z/2020-02-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-02-01",
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
-            "identifier": "C1997892408-NSIDC_ECS",
             "description": "This data set was collected during the SnowEx 2020 Intensive Observation Period (IOP) in Grand Mesa, Colorado. These data contain the geolocated, unprocessed, common midpoint (CMP) gathers from a Sensors & Software pulseEKKO PRO 1 GHz multi-polarization ground penetrating radar (GPR). Multi-offset gathers were collected by placing antennas on the snow surface and expanding the antenna separation about a fixed midpoint out to a 2 m offset. CMP gathers were collected in HH and HV polarizations.\nData were collected at three locations around Grand Mesa IOP snow pits 2N12 and 1S8 (see DOI: 10.5067/DUD2VZEVBJ7S for more details on Grand Mesa IOP snow pits). Data at snow pit 2N12 were acquired on the groomed snowmobile road (CMP1), in the fresh snow behind the snow pit wall (CMP2), and in the right rut of the SUSV track (CMP3). Data at snow pit 1S8  were acquired in the right rut of the SUSV track (CMP1), in the left rut of the SUSV track (CMP2), and in the fresh snow behind the snow pit wall (CMP3). \nThese data can be used to estimate snow depth, snow density, and snow water equivalent (SWE).",
-            "title": "SnowEx20 Grand Mesa IOP BSU Multi-polarization 1 GHz GPR CMP Raw V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCL5ZRBCEF8G3",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCL5ZRBCEF8G3",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1997892408-NSIDC_ECS&pg%5B0%5D%5Bgsk%5D=-start_date&q=SNEX20_BSU_CMP_Raw&m=38.35552775499695%21-113.57226562500001%215%211%210%210%2C2&tl=1596643552%214%21%21",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1997892408-NSIDC_ECS&pg%5B0%5D%5Bgsk%5D=-start_date&q=SNEX20_BSU_CMP_Raw&m=38.35552775499695%21-113.57226562500001%215%211%210%210%2C2&tl=1596643552%214%21%21",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_BSU_CMP_Raw.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_BSU_CMP_Raw.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_BSU_CMP_Raw/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_BSU_CMP_Raw/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/CL5ZRBCEF8G3",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/CL5ZRBCEF8G3",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/CL5ZRBCEF8G3",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/CL5ZRBCEF8G3",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1997892408-NSIDC_ECS",
+            "issued": "2020-01-31",
+            "keyword": [
+                "spectral/engineering",
+                "radar",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/CL5ZRBCEF8G3",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-02-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-108.197754 39.021584 -108.197754 39.021584",
+            "temporal": "2020-01-31T00:00:00Z/2020-02-01T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SnowEx20 Grand Mesa IOP BSU Multi-polarization 1 GHz GPR CMP Raw V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TBIS4-V1.0",
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
+            "description": "The Cassini Radio Science Titan Bistatic experiments (TBIS4) Raw Data Archive is a time-ordered collection of radio science raw data acquired on November 13 and 14, 2016, during the Cassini Extended Extended Mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tbis4-v1.0_8fyd-xphh",
+            "issued": "2021-05-21",
+            "keyword": [
+                "saturn",
+                "cassini-huygens"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TBIS4-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tbis4-v1.0_8fyd-xphh",
-            "description": "The Cassini Radio Science Titan Bistatic experiments (TBIS4) Raw Data Archive is a time-ordered collection of radio science raw data acquired on November 13 and 14, 2016, during the Cassini Extended Extended Mission.",
-            "title": "CASSINI RSS RAW DATA SET - TBIS4 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI RSS RAW DATA SET - TBIS4 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GFLND-3C634",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Felix Landerer. 2024-10-01. CSR TELLUS GRACE-FO Level-3 Monthly Land Water-Equivalent-Thickness. Version RL06.3v04. CSR TELLUS GRACE-FO Level-3 Monthly Land Water-Equivalent-Thickness Surface Mass Anomaly Release 6.3 version 04. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/GFLND-3C634.",
-            "issued": "2021-03-10",
-            "temporal": "2018-05-22T00:00:00Z/2024-10-14T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-03-10",
-            "keyword": [
-                "terrestrial hydrosphere",
-                "water budget",
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
-            "identifier": "C3193285193-POCLOUD",
-            "description": "This data set is produced by the Center for Space Research (CSR) GRACE-FO (Gravity Recovery and Climate Experiment Follow-On) program and derives the terrestrial water storage anomaly given as equivalent water thickness. These monthly grids are derived from GRACE-FO time-variable gravity observations during the specified timespan, and relative to the specified time-mean reference period. This quantity represents the total terrestrial water storage anomalies from soil moisture, snow, surface water (incl. rivers, lakes, reservoirs etc.), as well as groundwater and aquifers. A glacial isostatic adjustment (GIA) correction has been applied, and standard corrections for geocenter (degree-1), C20 (degree-20) and C30 (degree-30) are incorporated. Post-processing filters have been applied to reduce correlated errors. Data grids are provided in ASCII/netCDF/GeoTIFF formats. <br><br>\n\nGRACE-FO was launched on 22 May 2018, and extends the original GRACE mission (2002 \u2013 2017) and expands its legacy of scientific achievements in tracking earth surface mass changes. Version 04 (v04) of the terrestrial water storage data uses updated and consistent C20 and Geocenter corrections (i.e., Technical Notes TN-14 and TN-13), as well as an ellipsoidal correction to account for the non-spherical shape of the Earth when mapping gravity anomalies to surface mass change. Additionally, this release 06.3 is an updated version of the Level 3 products in coordination with the release of the analogous Level 2 products used to generate them. It differs from RL06.1 only in the Level-1B accelerometer transplant data that is used for the GF2 (GRACE-FO 2) satellite; see respective L-2 data descriptions. RL06.3 uses the ACX2-L1B data products. All GRACE-FO RL06.3 Level-3 fields are fully compatible with the GRACE RL06 data.",
-            "release-place": "PO.DAAC",
-            "series-name": "CSR TELLUS GRACE-FO Level-3 Monthly Land Water-Equivalent-Thickness",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Felix Landerer",
-            "title": "CSR TELLUS GRACE-FO Level-3 Monthly Land Water-Equivalent-Thickness Surface Mass Anomaly Release 6.3 version 04",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TELLUS_GRFO_L3_CSR_RL06_LND_v04.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This data set is produced by the Center for Space Research (CSR) GRACE-FO (Gravity Recovery and Climate Experiment Follow-On) program and derives the terrestrial water storage anomaly given as equivalent water thickness. These monthly grids are derived from GRACE-FO time-variable gravity observations during the specified timespan, and relative to the specified time-mean reference period. This quantity represents the total terrestrial water storage anomalies from soil moisture, snow, surface water (incl. rivers, lakes, reservoirs etc.), as well as groundwater and aquifers. A glacial isostatic adjustment (GIA) correction has been applied, and standard corrections for geocenter (degree-1), C20 (degree-20) and C30 (degree-30) are incorporated. Post-processing filters have been applied to reduce correlated errors. Data grids are provided in ASCII/netCDF/GeoTIFF formats. <br><br>\n\nGRACE-FO was launched on 22 May 2018, and extends the original GRACE mission (2002 \u2013 2017) and expands its legacy of scientific achievements in tracking earth surface mass changes. Version 04 (v04) of the terrestrial water storage data uses updated and consistent C20 and Geocenter corrections (i.e., Technical Notes TN-14 and TN-13), as well as an ellipsoidal correction to account for the non-spherical shape of the Earth when mapping gravity anomalies to surface mass change. Additionally, this release 06.3 is an updated version of the Level 3 products in coordination with the release of the analogous Level 2 products used to generate them. It differs from RL06.1 only in the Level-1B accelerometer transplant data that is used for the GF2 (GRACE-FO 2) satellite; see respective L-2 data descriptions. RL06.3 uses the ACX2-L1B data products. All GRACE-FO RL06.3 Level-3 fields are fully compatible with the GRACE RL06 data.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGFLND-3C634",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGFLND-3C634",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gracefo.jpl.nasa.gov/",
-                    "description": "GRACE-FO Project Website",
                     "@type": "dcat:Distribution",
+                    "description": "GRACE-FO Project Website",
+                    "downloadURL": "https://gracefo.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/gracefo/open/docs/GRACE-FO_L3_Handbook_JPL.pdf",
-                    "description": "User guidance documentation for this dataset",
                     "@type": "dcat:Distribution",
+                    "description": "User guidance documentation for this dataset",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/gracefo/open/docs/GRACE-FO_L3_Handbook_JPL.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TELLUS_GRFO_L3_CSR_RL06_LND_v04.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TELLUS_GRFO_L3_CSR_RL06_LND_v04.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/GRACE-FO",
-                    "description": "PODAAC GRACE-FO Mission-Page",
                     "@type": "dcat:Distribution",
+                    "description": "PODAAC GRACE-FO Mission-Page",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/GRACE-FO",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C3193285193-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C3193285193-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C3193285193-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C3193285193-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/gravity/gracefo-documentation",
-                    "description": "Page that includes all GRACE-FO Documentation and Technical Notes",
                     "@type": "dcat:Distribution",
+                    "description": "Page that includes all GRACE-FO Documentation and Technical Notes",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/gravity/gracefo-documentation",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TELLUS_GRFO_L3_CSR_RL06_LND_v04.jpg",
+            "identifier": "C3193285193-POCLOUD",
+            "issued": "2021-03-10",
+            "keyword": [
+                "terrestrial hydrosphere",
+                "water budget",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GFLND-3C634",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-03-10",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "PO.DAAC",
+            "series-name": "CSR TELLUS GRACE-FO Level-3 Monthly Land Water-Equivalent-Thickness",
             "spatial": "-180.0 -89.5 180.0 89.5",
+            "temporal": "2018-05-22T00:00:00Z/2024-10-14T00:00:00Z",
             "theme": [
                 "GRACE-FO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CSR TELLUS GRACE-FO Level-3 Monthly Land Water-Equivalent-Thickness Surface Mass Anomaly Release 6.3 version 04"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0942%2FI0943-3-BELSKAYAPOL-V1.0",
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
+            "description": "This data set contains UBVRI polarimetric measurements of ten main belt asteroids and one potentially hazardous near-Earth asteroid (NEA), from Belskaya et al. (2009) and Belskaya et al. (2009b).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0942-i0943-3-belskayapol-v1.0_8fyn-fstk",
+            "issued": "2021-05-21",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0942%2FI0943-3-BELSKAYAPOL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0942-i0943-3-belskayapol-v1.0_8fyn-fstk",
-            "description": "This data set contains UBVRI polarimetric measurements of ten main belt asteroids and one potentially hazardous near-Earth asteroid (NEA), from Belskaya et al. (2009) and Belskaya et al. (2009b).",
-            "title": "BELSKAYA ASTEROID POLARIMETRY V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "BELSKAYA ASTEROID POLARIMETRY V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SIEB3C4B9HKK",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "IceBridge-Related Sander AIRGrav L1B Geolocated Free Air Gravity Anomalies V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/SIEB3C4B9HKK.",
-            "issued": "2012-04-29",
-            "temporal": "2012-04-29T00:00:00Z/2016-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-08-09",
-            "keyword": [
-                "gravity/gravitational field",
-                "solid earth",
-                "earth science"
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
-            "identifier": "C1543795592-NSIDC_ECS",
             "description": "This data set contains Greenland and Antarctica gravity measurements taken from the Sander Geophysics AIRGrav airborne gravity system.",
-            "title": "IceBridge-Related Sander AIRGrav L1B Geolocated Free Air Gravity Anomalies V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSIEB3C4B9HKK",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSIEB3C4B9HKK",
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
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/RGGRV1B.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/RGGRV1B.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1543795592-NSIDC_ECS&q=RGGRV1B&m=-98.56031811609174%21-26.641845703125%210%211%210%210%2C2&tl=1558419489%214%21%21",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1543795592-NSIDC_ECS&q=RGGRV1B&m=-98.56031811609174%21-26.641845703125%210%211%210%210%2C2&tl=1558419489%214%21%21",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/RGGRV1B/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/RGGRV1B/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/SIEB3C4B9HKK",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/SIEB3C4B9HKK",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/SIEB3C4B9HKK",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/SIEB3C4B9HKK",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1543795592-NSIDC_ECS",
+            "issued": "2012-04-29",
+            "keyword": [
+                "gravity/gravitational field",
+                "solid earth",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SIEB3C4B9HKK",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2016-08-09",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 -53.0",
+            "temporal": "2012-04-29T00:00:00Z/2016-12-31T23:59:59.999Z",
             "theme": [
                 "2012_GR_GBMF",
                 "2012_PA_GBMF",
@@ -361415,483 +361416,484 @@
                 "2016_PA_GBMF",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "IceBridge-Related Sander AIRGrav L1B Geolocated Free Air Gravity Anomalies V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMAG-3-ESC1-CALIBRATED-V9.0",
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
+            "description": "This dataset contains CALIBRATED (CODMAC LEVEL 3) DATA of the\nCOMET ESCORT 1 Phase (ESC1) from November 22, 2014 until March 10, 2015\nof the ROSETTA orbiter magnetometer RPCMAG. Observations are done in\nthe vicinity of comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1).\nThe current version of the dataset is V9.0.\nThe difference to the datasets of earlier versions is mainly a significantly\nimproved sensor temperature model, more detailed documentation about magnetic\ndisturbance sources, more data handling information for the user and\nalso an improved quality flagging system.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmag-3-esc1-calibrated-v9.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMAG-3-ESC1-CALIBRATED-V9.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmag-3-esc1-calibrated-v9.0",
-            "description": "This dataset contains CALIBRATED (CODMAC LEVEL 3) DATA of the\nCOMET ESCORT 1 Phase (ESC1) from November 22, 2014 until March 10, 2015\nof the ROSETTA orbiter magnetometer RPCMAG. Observations are done in\nthe vicinity of comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1).\nThe current version of the dataset is V9.0.\nThe difference to the datasets of earlier versions is mainly a significantly\nimproved sensor temperature model, more detailed documentation about magnetic\ndisturbance sources, more data handling information for the user and\nalso an improved quality flagging system.",
-            "title": "ROSETTA-ORBITER 67P RPCMAG 3 ESC1 CALIBRATED V9.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCMAG 3 ESC1 CALIBRATED V9.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/R9QDK9LWDG32",
             "citation": "Miyazaki, Kazuyuki. 2024-02-06. TRPSCRPS6H2D. Version 1. TROPESS Chemical Reanalysis Surface Pressure 6-Hourly 2-dimensional Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/R9QDK9LWDG32. https://disc.gsfc.nasa.gov/datacollection/TRPSCRPS6H2D_1.html. Digital Science Data.",
-            "issued": "2023-01-09",
-            "temporal": "2005-01-01T00:00:00Z/2024-02-12T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-09",
-            "references": [
-                "https://doi.org/10.1126/sciadv.abf7460"
-            ],
-            "keyword": [
-                "earth science",
-                "atmospheric pressure",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "KAZUYUKI MIYAZAKI",
                 "hasEmail": "mailto:kazuyuki.miyazaki@jpl.nasa.gov"
             },
+            "creator": "Miyazaki, Kazuyuki",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2837624945-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS Chemical Reanalysis PS 6-Hourly 2-dimensional Product contains surface pressure values, a meteorological field. The data are part of the Tropospheric Chemical Reanalysis v2 (TCR-2) for the period 2005-2021. TCR-2 uses JPL's Multi-mOdel Multi-cOnstituent Chemical (MOMO-Chem) data assimilation framework that simultaneously optimizes both concentrations and emissions of multiple species from multiple satellite sensors.\n\nThe data files are written in the netCDF version 4 file format, and each file contains a year of data at 6-hourly resolution, and a spatial resolution of 1.125 x 1.125 degrees. The principal investigator for the TCR-2 data is Miyazaki, Kazuyuki.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSCRPS6H2D",
-            "creator": "Miyazaki, Kazuyuki",
-            "graphic-preview-description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
-            "title": "TROPESS Chemical Reanalysis Surface Pressure 6-Hourly 2-dimensional Product V1 (TRPSCRPS6H2D) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRPS6H2D_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FR9QDK9LWDG32",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FR9QDK9LWDG32",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRPS6H2D_Sample.png",
-                    "description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRPS6H2D_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSCRPS6H2D_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSCRPS6H2D_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_6HR_DIAGNOSTICS/TRPSCRPS6H2D.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_6HR_DIAGNOSTICS/TRPSCRPS6H2D.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSCRPS6H2D_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSCRPS6H2D_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TCR2_6HR_METFIELDS/TRPSCRPS6H2D.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TCR2_6HR_METFIELDS/TRPSCRPS6H2D.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_6HR_METFIELDS/TRPSCRPS6H2D.1/doc/TROPESS_ChemReanalysis_Forward_Stream_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_6HR_METFIELDS/TRPSCRPS6H2D.1/doc/TROPESS_ChemReanalysis_Forward_Stream_README.pdf",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRPS6H2D_Sample.png",
+            "identifier": "C2837624945-GES_DISC",
+            "issued": "2023-01-09",
+            "keyword": [
+                "earth science",
+                "atmospheric pressure",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/R9QDK9LWDG32",
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
+            "series-name": "TRPSCRPS6H2D",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2005-01-01T00:00:00Z/2024-02-12T00:00:00Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS Chemical Reanalysis Surface Pressure 6-Hourly 2-dimensional Product V1 (TRPSCRPS6H2D) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-EXT1-67P-M25-REFLECT-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 1 mission phase, covering the period from 2016-01-12T23:25:00.000 to 2016-02-09T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-ext1-67p-m25-reflect-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "earth",
                 "67p/churyumov-gerasimenko 1 (1969 r1)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-EXT1-67P-M25-REFLECT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-ext1-67p-m25-reflect-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 1 mission phase, covering the period from 2016-01-12T23:25:00.000 to 2016-02-09T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 EXT1-MTP025 RDR-REFLECT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 EXT1-MTP025 RDR-REFLECT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SWOT-RASTER-2.0",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Surface Water Ocean Topography (SWOT). 2024-02-01. SWOT Level 2 Water Mask Raster Image 100m Data Product. Version 2.0. SWOT Level 2 Water Mask Raster Image 100m Data Product, Version 2.0. Jet Propulsion Laboratory. Archived by National Aeronautics and Space Administration, U.S. Government, JPL NASA. https://doi.org/10.5067/SWOT-RASTER-2.0. https://swot.jpl.nasa.gov/.",
-            "issued": "2022-06-28",
-            "temporal": "2022-12-16T00:00:00Z/2024-03-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-06-28",
-            "keyword": [
-                "terrestrial hydrosphere",
-                "surface water",
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
-            "identifier": "C2799438280-POCLOUD",
-            "description": "The SWOT Level 2 Water Mask Raster Image 100m Data Product from the Surface Water Ocean Topography (SWOT) mission provides global surface water elevation and inundation extent derived from high rate (HR) measurements from the Ka-band Radar Interferometer (KaRIn) on SWOT. SWOT launched on December 16, 2022 from Vandenberg Air Force Base in California into a 1-day repeat orbit for the \"calibration\" or \"fast-sampling\" phase of the mission, which completed in early July 2023. After the calibration phase, SWOT entered a 21-day repeat orbit in August 2023 to start the \"science\" phase of the mission, which is expected to continue through 2025.\\r\\n<br>\r\nWater surface elevation, area, water fraction, backscatter, geophysical information are provided in geographically fixed scenes at 100 meter horizontal resolution in Universal Transverse Mercator (UTM) projection. Available in netCDF-4 file format. On-demand processing available to users for different resolutions, sampling grids, scene sizes, and file formats.\\r\\n<br>\r\n<br>This collection is a sub-collection of its parent: https://podaac.jpl.nasa.gov/dataset/SWOT_L2_HR_Raster_2.0",
-            "release-place": "Jet Propulsion Laboratory",
-            "series-name": "SWOT Level 2 Water Mask Raster Image 100m Data Product",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Surface Water Ocean Topography (SWOT)",
-            "title": "SWOT Level 2 Water Mask Raster Image 100m Data Product, Version 2.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_HR_Raster_2.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The SWOT Level 2 Water Mask Raster Image 100m Data Product from the Surface Water Ocean Topography (SWOT) mission provides global surface water elevation and inundation extent derived from high rate (HR) measurements from the Ka-band Radar Interferometer (KaRIn) on SWOT. SWOT launched on December 16, 2022 from Vandenberg Air Force Base in California into a 1-day repeat orbit for the \"calibration\" or \"fast-sampling\" phase of the mission, which completed in early July 2023. After the calibration phase, SWOT entered a 21-day repeat orbit in August 2023 to start the \"science\" phase of the mission, which is expected to continue through 2025.\\r\\n<br>\r\nWater surface elevation, area, water fraction, backscatter, geophysical information are provided in geographically fixed scenes at 100 meter horizontal resolution in Universal Transverse Mercator (UTM) projection. Available in netCDF-4 file format. On-demand processing available to users for different resolutions, sampling grids, scene sizes, and file formats.\\r\\n<br>\r\n<br>This collection is a sub-collection of its parent: https://podaac.jpl.nasa.gov/dataset/SWOT_L2_HR_Raster_2.0",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSWOT-RASTER-2.0",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSWOT-RASTER-2.0",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2799438280-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2799438280-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2799438280-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2799438280-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_HR_Raster_2.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_HR_Raster_2.0.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/swot_mission_docs/pdd/D-56416_SWOT_Product_Description_L2_HR_Raster_20231026_RevBcite.pdf",
-                    "description": "Product Description Document (PDD)",
                     "@type": "dcat:Distribution",
+                    "description": "Product Description Document (PDD)",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/swot_mission_docs/pdd/D-56416_SWOT_Product_Description_L2_HR_Raster_20231026_RevBcite.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/swot_mission_docs/atbd/D-105507_SWOT_ATBD_L2_HR_Raster_20230918d_cite.pdf",
-                    "description": "Algorithm Theoretical Basis Document (ATBD)",
                     "@type": "dcat:Distribution",
+                    "description": "Algorithm Theoretical Basis Document (ATBD)",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/swot_mission_docs/atbd/D-105507_SWOT_ATBD_L2_HR_Raster_20230918d_cite.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/swot_mission_docs/releases/SWOT_VersionC_KaRIn_Products_Release_Note.pdf",
-                    "description": "Release Note",
                     "@type": "dcat:Distribution",
+                    "description": "Release Note",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/swot_mission_docs/releases/SWOT_VersionC_KaRIn_Products_Release_Note.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2799438280-POCLOUD&pg%5B0%5D%5Bid%5D=*PIC0*",
-                    "description": "Search Granules from Forward Processing (PIC0)",
                     "@type": "dcat:Distribution",
+                    "description": "Search Granules from Forward Processing (PIC0)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2799438280-POCLOUD&pg%5B0%5D%5Bid%5D=*PIC0*",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2799438280-POCLOUD&pg%5B0%5D%5Bid%5D=*PGC0*",
-                    "description": "Search Granules from Bulk Reprocessing (PGC0)",
                     "@type": "dcat:Distribution",
+                    "description": "Search Granules from Bulk Reprocessing (PGC0)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2799438280-POCLOUD&pg%5B0%5D%5Bid%5D=*PGC0*",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_HR_Raster_2.0.jpg",
+            "identifier": "C2799438280-POCLOUD",
+            "issued": "2022-06-28",
+            "keyword": [
+                "terrestrial hydrosphere",
+                "surface water",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SWOT-RASTER-2.0",
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
+            "series-name": "SWOT Level 2 Water Mask Raster Image 100m Data Product",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2022-12-16T00:00:00Z/2024-03-27T00:00:00Z",
             "theme": [
                 "SWOT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SWOT Level 2 Water Mask Raster Image 100m Data Product, Version 2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CAMEX-4/SBAND/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Gerlach, John  and Paul A Kucera.2002. CAMEX-4 NASA PORTABLE S-BAND MULTIPARAMETER WX RESEARCH RADAR [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/CAMEX-4/SBAND/DATA101",
-            "issued": "2002-12-20",
-            "temporal": "2001-08-17T16:52:50Z/2001-09-28T17:25:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-10",
-            "keyword": [
-                "spectral/engineering",
-                "radar",
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
-            "identifier": "C1979101817-GHRC_DAAC",
             "description": "The CAMEX-4 NASA Portable S-Band Multiparameter WX Research Radar dataset was collected by the NASA Portable S-band Multiparameter Weather Research Radar (NPOL), which is a Doppler S-band radar that when used continuously during an operation provides a full volume scan every ten minutes. Scans may be either 300km long range scans or 150km range for most high resolution data scans. Products available include real time PPI scans of reflectivities and velocities, and near real time displays of other radar products, including RHI's, CAPPI's, and Polarimetric products. Browse imagery is available for PPI reflectivities.",
-            "graphic-preview-description": "N/A",
-            "title": "CAMEX-4 NASA PORTABLE S-BAND MULTIPARAMETER WX RESEARCH RADAR V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex4/NPOL/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAMEX-4%2FSBAND%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAMEX-4%2FSBAND%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=c4gnpol",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=c4gnpol",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex4/NPOL/browse/NPOL_010904_0007_swp0_dz.gif.jpg",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex4/NPOL/browse/NPOL_010904_0007_swp0_dz.gif.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/camex4/c4gnpol/c4gnpol_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/camex4/c4gnpol/c4gnpol_dataset.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/camex4/c4gnpol/NPOL_SCIENCELOG.txt",
-                    "description": "NPOL Radar Science LogCAMEX/KAMP ExperimentNaval Air Station, Boca Chica Key, FloridaAugust - September, 2001 (TEXT)",
                     "@type": "dcat:Distribution",
+                    "description": "NPOL Radar Science LogCAMEX/KAMP ExperimentNaval Air Station, Boca Chica Key, FloridaAugust - September, 2001 (TEXT)",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/camex4/c4gnpol/NPOL_SCIENCELOG.txt",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/camex4/c4gnpol/NPOL_KAMP_TAPELOG.doc",
-                    "description": "NPOL Tape Log (Document)",
                     "@type": "dcat:Distribution",
+                    "description": "NPOL Tape Log (Document)",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/camex4/c4gnpol/NPOL_KAMP_TAPELOG.doc",
+                    "mediaType": "application/msword",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/camex4/c4gnpol/NPOL_KAMP_TAPELOG.txt",
-                    "description": "NPOL Tape Log (Text)",
                     "@type": "dcat:Distribution",
+                    "description": "NPOL Tape Log (Text)",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/camex4/c4gnpol/NPOL_KAMP_TAPELOG.txt",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/camex4/c4gnpol/NPOL_SCIENCELOG.doc",
-                    "description": "NPOL Radar Science Log CAMEX/KAMP Experiment Naval Air Station, Boca Chica Key, Florida August \u00bf\u00bf\u00bf September, 2001 (DOCUMENT)",
                     "@type": "dcat:Distribution",
+                    "description": "NPOL Radar Science Log CAMEX/KAMP Experiment Naval Air Station, Boca Chica Key, Florida August \u00bf\u00bf\u00bf September, 2001 (DOCUMENT)",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/camex4/c4gnpol/NPOL_SCIENCELOG.doc",
+                    "mediaType": "application/msword",
                     "title": "View the primary investigator's documentation for this dataset"
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex4/NPOL/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex4/NPOL/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex4/NPOL/browse/",
+            "identifier": "C1979101817-GHRC_DAAC",
+            "issued": "2002-12-20",
+            "keyword": [
+                "spectral/engineering",
+                "radar",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/CAMEX-4/SBAND/DATA101",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-05-10",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/MSFC/GHRC"
+            },
             "spatial": "-83.1892 23.2469 -80.1939 25.9456",
+            "temporal": "2001-08-17T16:52:50Z/2001-09-28T17:25:00Z",
             "theme": [
                 "CAMEX-4",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CAMEX-4 NASA PORTABLE S-BAND MULTIPARAMETER WX RESEARCH RADAR V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-PRL-67PCHURYUMOV-M03-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera during the PRELANDING phase of the Rosetta mission at the comet 67P, covering the period from 2014-05-07T12:48:00.000 to 2014-06-04T10:49:59.000. This version V2.0 supersedes previous deliveries of the same dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-prl-67pchuryumov-m03-v2.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "vega",
                 "16 cyg b",
@@ -361901,159 +361903,171 @@
                 "saturn",
                 "zeta cas"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-PRL-67PCHURYUMOV-M03-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-prl-67pchuryumov-m03-v2.0",
-            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera during the PRELANDING phase of the Rosetta mission at the comet 67P, covering the period from 2014-05-07T12:48:00.000 to 2014-06-04T10:49:59.000. This version V2.0 supersedes previous deliveries of the same dataset.",
-            "title": "ROSETTA-ORBITER PRELANDING OSINAC 3 RDR MTP003 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER PRELANDING OSINAC 3 RDR MTP003 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/MODST-MO9D9",
             "citation": "NASA OBPG. 2020-01-15. MODIS Terra Level 3 SST Thermal IR Monthly 9km Daytime. Version 2019.0. MODIS Terra Global Level 3 Mapped SST. OBPG, Goddard Space Flight Center  Greenbelt, MD,US. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/MODST-MO9D9. https://podaac-tools.jpl.nasa.gov/drive/files/allData/modis/L3/docs/modis_sst.html.",
-            "issued": "2019-12-14",
-            "temporal": "2000-02-24T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-12-14",
-            "references": [
-                "https://doi.org/10.1016/j.rse.2015.04.023",
-                "https://doi.org/10.1175/JTECH-D-18-0103.1"
-            ],
-            "keyword": [
-                "oceans",
-                "ngda",
-                "national geospatial data asset",
-                "ocean temperature",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
             },
-            "identifier": "C2036877995-POCLOUD",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "description": "Day and night spatially gridded global NASA skin sea surface temperature (SST) products from the Moderate-resolution Imaging Spectroradiometer (MODIS) onboard the Terra satellite.  Average daily, weekly (8 day), monthly and annual skin SST products are available at both 4.63 and 9.26 km spatial resolution. Terra was launched by NASA on December 18, 1999, into a sun synchronous, polar orbit with a daylight descending node at 10:30 am, to study the global dynamics of the Earth atmosphere, land and oceans. The MODIS captures data in 36 spectral bands at a variety of spatial resolutions. Two SST products can be present in these files. The first is a skin SST produced for both day and night observations, derived from the long wave IR 11 and 12 micron wavelength channels, using a modified nonlinear SST algorithm intended to provide continuity with SST derived from heritage and current NASA sensors. At night, a second SST product is produced using the mid-infrared 3.95 and 4.05 micron  channels which are unique to MODIS; the SST derived from these measurements is identified as SST4. The SST4 product has lower uncertainty, but due to sun glint can only be produced at night. To generate the L3 products the L2 pixels are binned into an integerized sinusoidal area grid (ISEAG) and mapped into an equidistant cylindrical (also known as Platte Carre) projection. Additional projection detailed can be found at https://oceancolor.gsfc.nasa.gov/docs/format/ The NASA MODIS L3 SST data products are generated by the NASA Ocean Biology Processing Group (OBPG) Peter Minnett and his team at the Rosenstiel School of Marine and Atmospheric Science (RSMAS) are responsible for sea surface temperature algorithm development, error statistics and quality flagging. JPL acquires and distributes MODIS ocean L3 SST data from the OBPG as the official Physical Oceanography Data Archive (PO.DAAC) for SST. The R2019 superseded the previous v2014.1 datasets which can be at https://doi.org/10.5067/MODST-MO9D4",
-            "release-place": "OBPG, Goddard Space Flight Center  Greenbelt, MD,US",
-            "series-name": "MODIS Terra Level 3 SST Thermal IR Monthly 9km Daytime",
             "creator": "NASA OBPG",
-            "title": "MODIS Terra Level 3 SST Thermal IR Monthly 9km Daytime V2019.0",
-            "graphic-preview-description": "Thumbnail",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MODIS_TERRA_L3_SST_THERMAL_MONTHLY_9KM_DAYTIME_V2019.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Day and night spatially gridded global NASA skin sea surface temperature (SST) products from the Moderate-resolution Imaging Spectroradiometer (MODIS) onboard the Terra satellite.  Average daily, weekly (8 day), monthly and annual skin SST products are available at both 4.63 and 9.26 km spatial resolution. Terra was launched by NASA on December 18, 1999, into a sun synchronous, polar orbit with a daylight descending node at 10:30 am, to study the global dynamics of the Earth atmosphere, land and oceans. The MODIS captures data in 36 spectral bands at a variety of spatial resolutions. Two SST products can be present in these files. The first is a skin SST produced for both day and night observations, derived from the long wave IR 11 and 12 micron wavelength channels, using a modified nonlinear SST algorithm intended to provide continuity with SST derived from heritage and current NASA sensors. At night, a second SST product is produced using the mid-infrared 3.95 and 4.05 micron  channels which are unique to MODIS; the SST derived from these measurements is identified as SST4. The SST4 product has lower uncertainty, but due to sun glint can only be produced at night. To generate the L3 products the L2 pixels are binned into an integerized sinusoidal area grid (ISEAG) and mapped into an equidistant cylindrical (also known as Platte Carre) projection. Additional projection detailed can be found at https://oceancolor.gsfc.nasa.gov/docs/format/ The NASA MODIS L3 SST data products are generated by the NASA Ocean Biology Processing Group (OBPG) Peter Minnett and his team at the Rosenstiel School of Marine and Atmospheric Science (RSMAS) are responsible for sea surface temperature algorithm development, error statistics and quality flagging. JPL acquires and distributes MODIS ocean L3 SST data from the OBPG as the official Physical Oceanography Data Archive (PO.DAAC) for SST. The R2019 superseded the previous v2014.1 datasets which can be at https://doi.org/10.5067/MODST-MO9D4",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODST-MO9D9",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODST-MO9D9",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MODIS_TERRA_L3_SST_THERMAL_MONTHLY_9KM_DAYTIME_V2019.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MODIS_TERRA_L3_SST_THERMAL_MONTHLY_9KM_DAYTIME_V2019.0.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2036877995-POCLOUD",
-                    "description": "Browse and download granules over HTTPS using the virtual directories",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2036877995-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2036877995-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2036877995-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MODIS_TERRA_L3_SST_THERMAL_MONTHLY_9KM_DAYTIME_V2019.0.jpg",
+            "identifier": "C2036877995-POCLOUD",
+            "issued": "2019-12-14",
+            "keyword": [
+                "oceans",
+                "ngda",
+                "national geospatial data asset",
+                "ocean temperature",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODST-MO9D9",
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
+            "series-name": "MODIS Terra Level 3 SST Thermal IR Monthly 9km Daytime",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-02-24T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "EOS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS Terra Level 3 SST Thermal IR Monthly 9km Daytime V2019.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/8gfi-6fri",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Densely ionizing radiation is a major component of the space radiation environment and has potentially greater carcinogenic effect compared to sparsely ionizing radiation that is prevalent in the terrestrial environment. It is unknown to what extent the irradiated microenvironment contributes to the differential carcinogenic potential of densely ionizing radiation. To address this gap 10-week old BALB/c mice were irradiated with 100 cGy sparsely ionizing g-radiation or 10 30 or 80 cGy of densely ionizing 350 MeV/amu Si particles and transplanted 3 days later with syngeneic Trp53 null mammary fragments. Tumor appearance was monitored for 600 days. Tumors arising in Si-particle irradiated mice had a shorter median time to appearance grew faster and were more likely to metastasize. Most tumors arising in sham-irradiated mice were ER-positive pseudo-glandular and contained both basal keratin 14 and luminal keratin 8/18 cells (designated K14/18) while most tumors arising in irradiated hosts were K8/18 positive (designated K18) and ER negative. Comparison of K18 vs K14/18 tumor expression profiles showed that genes increased in K18 tumors were associated with ERBB2 and KRAS while decreased genes overlapped with those down regulated in metastasis and by loss of E-cadherin. Consistent with this K18 tumors grew faster than K14/18 tumors and more mice with K18 tumors developed lung metastases compared to mice with K14/18 tumors. However K18 tumors arising in Si-particle irradiated mice grew even faster and were more metastatic compared to control mice. A K18 Si-irradiated host profile was enriched in genes involved in mammary stem cells stroma and Notch signaling. Thus systemic responses to densely ionizing radiation enriches for a ER-negative K18-positive tumor whose biology is more aggressive compared to similar tumors arising in non-irradiated hosts. Key Words: ionizing radiation; breast cancer; heavy ion radiation;initiation; promotion 3 different dose of Si were used. Total RNA was extracted from mammary tumors derived from transplantations of non-irradiated p53null mammary fragments into irradiated hosts. We analyzed a total of 45 Trp53-null tumors: 18 from sham-irradiated hosts 9 from 10 cGy Si-irradiated hosts 10 from 30 cGy Si-irradiated hosts and 8 from irradiated hosts.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-74",
+                    "mediaType": "text/html",
+                    "title": "Densely Ionizing Radiation Effects on the Microenvironment Promote Aggressive Trp53 Null Mammary Carcinomas"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-74_8gfi-6fri",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "p-gse56704-5",
                 "absorbed radiation dose",
@@ -362074,909 +362088,873 @@
                 "p-gse56704-7",
                 "sample treatment protocol"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/8gfi-6fri",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-74_8gfi-6fri",
-            "description": "Densely ionizing radiation is a major component of the space radiation environment and has potentially greater carcinogenic effect compared to sparsely ionizing radiation that is prevalent in the terrestrial environment. It is unknown to what extent the irradiated microenvironment contributes to the differential carcinogenic potential of densely ionizing radiation. To address this gap 10-week old BALB/c mice were irradiated with 100 cGy sparsely ionizing g-radiation or 10 30 or 80 cGy of densely ionizing 350 MeV/amu Si particles and transplanted 3 days later with syngeneic Trp53 null mammary fragments. Tumor appearance was monitored for 600 days. Tumors arising in Si-particle irradiated mice had a shorter median time to appearance grew faster and were more likely to metastasize. Most tumors arising in sham-irradiated mice were ER-positive pseudo-glandular and contained both basal keratin 14 and luminal keratin 8/18 cells (designated K14/18) while most tumors arising in irradiated hosts were K8/18 positive (designated K18) and ER negative. Comparison of K18 vs K14/18 tumor expression profiles showed that genes increased in K18 tumors were associated with ERBB2 and KRAS while decreased genes overlapped with those down regulated in metastasis and by loss of E-cadherin. Consistent with this K18 tumors grew faster than K14/18 tumors and more mice with K18 tumors developed lung metastases compared to mice with K14/18 tumors. However K18 tumors arising in Si-particle irradiated mice grew even faster and were more metastatic compared to control mice. A K18 Si-irradiated host profile was enriched in genes involved in mammary stem cells stroma and Notch signaling. Thus systemic responses to densely ionizing radiation enriches for a ER-negative K18-positive tumor whose biology is more aggressive compared to similar tumors arising in non-irradiated hosts. Key Words: ionizing radiation; breast cancer; heavy ion radiation;initiation; promotion 3 different dose of Si were used. Total RNA was extracted from mammary tumors derived from transplantations of non-irradiated p53null mammary fragments into irradiated hosts. We analyzed a total of 45 Trp53-null tumors: 18 from sham-irradiated hosts 9 from 10 cGy Si-irradiated hosts 10 from 30 cGy Si-irradiated hosts and 8 from irradiated hosts.",
-            "title": "Densely Ionizing Radiation Effects on the Microenvironment Promote Aggressive Trp53 Null Mammary Carcinomas",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-74",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Densely Ionizing Radiation Effects on the Microenvironment Promote Aggressive Trp53 Null Mammary Carcinomas"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Densely Ionizing Radiation Effects on the Microenvironment Promote Aggressive Trp53 Null Mammary Carcinomas"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LP-L-MAG-4-LUNAR-FIELD-TS-V1.0",
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
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lp-l-mag-4-lunar-field-ts-v1.0_8gfp-6icm",
+            "issued": "2018-06-26",
+            "keyword": [
+                "lunar prospector",
+                "moon"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LP-L-MAG-4-LUNAR-FIELD-TS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lp-l-mag-4-lunar-field-ts-v1.0_8gfp-6icm",
-            "description": "not applicable",
-            "title": "LP MOON MAG LEVEL 4 LUNAR MAGNETIC FIELD TIME SERIES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "LP MOON MAG LEVEL 4 LUNAR MAGNETIC FIELD TIME SERIES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-E-UVS-2-EDR-V1.0",
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
-                "galileo"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "TBD",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-e-uvs-2-edr-v1.0_8gg3-xfkk",
+            "issued": "2021-05-21",
+            "keyword": [
+                "galileo"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-E-UVS-2-EDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-e-uvs-2-edr-v1.0_8gg3-xfkk",
-            "description": "TBD",
-            "title": "GLL EARTH UVS EARTH ENCOUNTER EDR",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GLL EARTH UVS EARTH ENCOUNTER EDR"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/832",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "King, M.D., and S.E. Platnick. 2018. SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/832",
-            "issued": "2018-02-16",
-            "temporal": "2000-08-17T00:00:00Z/2000-09-25T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-08",
-            "keyword": [
-                "surface radiative properties",
-                "spectral/engineering",
-                "earth science",
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
-            "identifier": "C2763230127-ORNL_CLOUD",
             "description": "This dataset contains the Moderate Resolution Imaging Spectroradiometer (MODIS) Airborne Simulator (MAS) multispectral data collected during the SAFARI 2000 project. The flights were undertaken over Southern Africa by the NASA ER-2 aircraft during August and September, 2000.",
-            "graphic-preview-description": "Selected MAS bands from Flight 00178, Track 16, on September 21, 2000 over Southern Africa.",
-            "title": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000",
-            "graphic-preview-file": "https://daac.ornl.gov/S2K/guides/MAS_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F832",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F832",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/remote_sensing/MAS/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/remote_sensing/MAS/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/S2K/guides/MAS.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/S2K/guides/MAS.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/832",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/832",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS.pdf",
-                    "description": "guide.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "guide.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/gzip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_calibration_SRF.tar.gz",
-                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_calibration_SRF.tar.gz",
                     "@type": "dcat:Distribution",
+                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_calibration_SRF.tar.gz",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_calibration_SRF.tar.gz",
+                    "mediaType": "application/gzip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/gzip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_configuration_CFG.tar.gz",
-                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_configuration_CFG.tar.gz",
                     "@type": "dcat:Distribution",
+                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_configuration_CFG.tar.gz",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_configuration_CFG.tar.gz",
+                    "mediaType": "application/gzip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_Flight_147.pdf",
-                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_Flight_147.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_Flight_147.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_Flight_147.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_Flight_148.pdf",
-                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_Flight_148.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_Flight_148.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_Flight_148.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_Flight_149.pdf",
-                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_Flight_149.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_Flight_149.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_Flight_149.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_Flight_150.pdf",
-                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_Flight_150.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_Flight_150.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_Flight_150.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_Flight_151.pdf",
-                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_Flight_151.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_Flight_151.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_Flight_151.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_Flight_152.pdf",
-                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_Flight_152.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_Flight_152.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_Flight_152.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_Flight_153.pdf",
-                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_Flight_153.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_Flight_153.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_Flight_153.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_Flight_154.pdf",
-                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_Flight_154.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_Flight_154.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_Flight_154.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_Flight_155.pdf",
-                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_Flight_155.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_Flight_155.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_Flight_155.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_Flight_156.pdf",
-                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_Flight_156.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_Flight_156.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_Flight_156.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_Flight_157.pdf",
-                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_Flight_157.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_Flight_157.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_Flight_157.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_Flight_158.pdf",
-                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_Flight_158.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_Flight_158.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_Flight_158.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_Flight_160.pdf",
-                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_Flight_160.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_Flight_160.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_Flight_160.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_Flight_175.pdf",
-                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_Flight_175.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_Flight_175.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_Flight_175.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_Flight_176.pdf",
-                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_Flight_176.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_Flight_176.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_Flight_176.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_Flight_177.pdf",
-                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_Flight_177.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_Flight_177.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_Flight_177.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_Flight_178.pdf",
-                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_Flight_178.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_Flight_178.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_Flight_178.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_Flight_179.pdf",
-                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_Flight_179.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_Flight_179.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_Flight_179.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_Flight_180.pdf",
-                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_Flight_180.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_Flight_180.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_Flight_180.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/gzip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_flight_summary_SUM.tar.gz",
-                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_flight_summary_SUM.tar.gz",
                     "@type": "dcat:Distribution",
+                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_flight_summary_SUM.tar.gz",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_flight_summary_SUM.tar.gz",
+                    "mediaType": "application/gzip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/gzip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_images.tar.gz",
-                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_images.tar.gz",
                     "@type": "dcat:Distribution",
+                    "description": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000: MAS_images.tar.gz",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MAS/comp/MAS_images.tar.gz",
+                    "mediaType": "application/gzip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/S2K/guides/MAS_Fig1.jpg",
-                    "description": "Selected MAS bands from Flight 00178, Track 16, on September 21, 2000 over Southern Africa.",
                     "@type": "dcat:Distribution",
+                    "description": "Selected MAS bands from Flight 00178, Track 16, on September 21, 2000 over Southern Africa.",
+                    "downloadURL": "https://daac.ornl.gov/S2K/guides/MAS_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Selected MAS bands from Flight 00178, Track 16, on September 21, 2000 over Southern Africa.",
+            "graphic-preview-file": "https://daac.ornl.gov/S2K/guides/MAS_Fig1.jpg",
+            "identifier": "C2763230127-ORNL_CLOUD",
+            "issued": "2018-02-16",
+            "keyword": [
+                "surface radiative properties",
+                "spectral/engineering",
+                "earth science",
+                "infrared wavelengths",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/832",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-09-08",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "9.06 -32.67 41.07 -11.81",
+            "temporal": "2000-08-17T00:00:00Z/2000-09-25T23:59:59Z",
             "theme": [
                 "SAFARI 2000",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAFARI 2000 MODIS Airborne Simulator Data, Southern Africa, Dry Season 2000"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-PRL-67PCHURYUMOV-M04-V1.0",
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
+            "description": "This data set contains images acquired between 2014-06-04 and 2014-06-18 by\nthe OSIRIS Wide Angle Camera during the prelanding phase of the Rosetta\nmission at the comet 67P",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-prl-67pchuryumov-m04-v1.0_8gia-kgyk",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-PRL-67PCHURYUMOV-M04-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-prl-67pchuryumov-m04-v1.0_8gia-kgyk",
-            "description": "This data set contains images acquired between 2014-06-04 and 2014-06-18 by\nthe OSIRIS Wide Angle Camera during the prelanding phase of the Rosetta\nmission at the comet 67P",
-            "title": "ROSETTA-ORBITER COMET PRELANDING OSIWAC 2 EDR data",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMET PRELANDING OSIWAC 2 EDR data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-OSIWAC-3-AST2-LUTETIAFLYBY-V1.1",
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
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera\nduring the LUTETIA FLY-BY mission phase",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-osiwac-3-ast2-lutetiaflyby-v1.1_8gir-zkv8",
+            "issued": "2021-05-21",
             "keyword": [
                 "16 cyg b",
                 "international rosetta mission",
                 "vega",
                 "21 lutetia"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-OSIWAC-3-AST2-LUTETIAFLYBY-V1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-osiwac-3-ast2-lutetiaflyby-v1.1_8gir-zkv8",
-            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera\nduring the LUTETIA FLY-BY mission phase",
-            "title": "ROSETTA-ORBITER LUTETIA FLY-BY OSIWAC 3 RDR data",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER LUTETIA FLY-BY OSIWAC 3 RDR data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NPP/CERES/ES9-FM5_L3.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2020-04-30. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/NPP/CERES/ES9-FM5_L3.002.",
-            "issued": "2020-03-04",
-            "temporal": "2012-02-01T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-03-04",
-            "keyword": [
-                "earth science",
-                "atmospheric radiation",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "TAKMENG WONG",
                 "hasEmail": "mailto:takmeng.wong@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2246001720-LARC_ASDC",
             "description": "The ERBE-like Monthly Regional Averages (ES-9) product contains a month of space and time averaged Clouds and the Earth's Radiant Energy System (CERES) data for a single satellite using measurements from the primary crosstrack instrument. All instantaneous shortwave and longwave fluxes at the Top-of-the-Atmosphere (TOA) from the CERES ES-8 product for a month are sorted by 2.5-degree spatial regions, by day number, and by the local hour of observation. The mean of the instantaneous fluxes for a given region-day-hour bin is determined and recorded on the ES-9 along with other flux statistics and scene information. For each region, the daily average flux is estimated from an algorithm that uses the available hourly data, scene identification data, and diurnal models. This algorithm is \"like\" the algorithm used for the Earth Radiation Budget Experiment (ERBE). The ES-9 also contains hourly average fluxes for the month and an overall monthly average for each region. These average fluxes are given for both clear-sky and total-sky scenes.\r\nCERES is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions are a follow-on to the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument (PFM) was launched on November 27, 1997 as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the EOS flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board EOS Aqua on May 4, 2002. The CERES instrument (FM5) was launched on board the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The last CERES instrument (FM6) was launched on board the Joint Polar Satellite System 1 (JPSS-1) satellite on November 18, 2017.",
-            "title": "CERES ERBE-like Gridded Instantaneous TOA Fluxes (ES9) NPP CERES FM-5 Edition2",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNPP%2FCERES%2FES9-FM5_L3.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNPP%2FCERES%2FES9-FM5_L3.002",
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
-                    "downloadURL": "https://doi.org/10.5067/NPP/CERES/ES9-FM5_L3.002",
-                    "description": "DOI data set landing page for CER_ES9_NPP-FM5_Edition2",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CER_ES9_NPP-FM5_Edition2",
+                    "downloadURL": "https://doi.org/10.5067/NPP/CERES/ES9-FM5_L3.002",
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
-                    "downloadURL": "https://ceres.larc.nasa.gov/documents/collect_guide/pdf/ES9_CG_R1V1.pdf",
-                    "description": "ES-9 Collection Guide Release 1 Version 1",
                     "@type": "dcat:Distribution",
+                    "description": "ES-9 Collection Guide Release 1 Version 1",
+                    "downloadURL": "https://ceres.larc.nasa.gov/documents/collect_guide/pdf/ES9_CG_R1V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/guide/cer_es9.pdf",
-                    "description": "CERES ERBE-like Monthly Regional Averages (ES-9) Data Set Abstract",
                     "@type": "dcat:Distribution",
+                    "description": "CERES ERBE-like Monthly Regional Averages (ES-9) Data Set Abstract",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/guide/cer_es9.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/quality_summaries/CER_ES9_NPP_Edition2.pdf",
-                    "description": "Quality Summary: CERES ES9 NPP Edition 2",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Summary: CERES ES9 NPP Edition 2",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/quality_summaries/CER_ES9_NPP_Edition2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/DPC_ES9_R7V1.pdf",
-                    "description": "CERES Data Products Catalog R7V1 11/19/2013 ERBE-like Monthly Regional Averages (ES-9)",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Data Products Catalog R7V1 11/19/2013 ERBE-like Monthly Regional Averages (ES-9)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/DPC_ES9_R7V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's production history"
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2246001720-LARC_ASDC",
-                    "description": "Earthdata Search for CER_ES9_NPP-FM5_Edition2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CER_ES9_NPP-FM5_Edition2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2246001720-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/ES9/NPP-FM5_Edition2/",
-                    "description": "ASDC Direct Data Download for CER_ES9_NPP-FM5_Edition2",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CER_ES9_NPP-FM5_Edition2",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/ES9/NPP-FM5_Edition2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/ES9/NPP-FM5_Edition2/contents.html",
-                    "description": "OPeNDAP data access for CER_ES9_NPP-FM5_Edition2",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CER_ES9_NPP-FM5_Edition2",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/ES9/NPP-FM5_Edition2/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2246001720-LARC_ASDC",
+            "issued": "2020-03-04",
+            "keyword": [
+                "earth science",
+                "atmospheric radiation",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/NPP/CERES/ES9-FM5_L3.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-03-04",
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
+            "title": "CERES ERBE-like Gridded Instantaneous TOA Fluxes (ES9) NPP CERES FM-5 Edition2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/462/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2011-09-09",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "nasa",
-                "ames"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rajiv Shenoy",
                 "hasEmail": "mailto:rajiv.shenoy@gatech.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_462",
             "description": "This contains the remaining 5 tarballs (5 grids and associated files) for the RSW node centered grids. Each tarball contains a stream-AFLR3 grid, CGNS grid, surface grid, mapbc file, info file, and tags file.\r\n\r\nTo assemble the fine tet. grid files use the following command\r\n\r\n>> cat fine_tet_nc.tar.gz_part1 fine_tet_nc.tar.gz_part2 > fine_tet_nc.tar.gz",
-            "title": "RSW Node Centered Coarse Grid w/ Split Walls Coarse/Med/Fine",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/coarse_tet_nc.tar.gz",
-                    "description": "Coarse Tet Grid",
                     "@type": "dcat:Distribution",
+                    "description": "Coarse Tet Grid",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/coarse_tet_nc.tar.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "coarse_tet_nc.tar.gz"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/medium_mixed_nc.tar.gz",
-                    "description": "Medium MixedElem Grid",
                     "@type": "dcat:Distribution",
+                    "description": "Medium MixedElem Grid",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/medium_mixed_nc.tar.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "medium_mixed_nc.tar.gz"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/medium_tet_nc.tar.gz",
-                    "description": "Medium Tet Grid",
                     "@type": "dcat:Distribution",
+                    "description": "Medium Tet Grid",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/medium_tet_nc.tar.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "medium_tet_nc.tar.gz"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/fine_mixed_nc.tar.gz",
-                    "description": "Fine MixedElem Grid",
                     "@type": "dcat:Distribution",
+                    "description": "Fine MixedElem Grid",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/fine_mixed_nc.tar.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "fine_mixed_nc.tar.gz"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/fine_tet_nc.tar.gz_part1",
-                    "description": "Fine Tet Grid Part 1",
                     "@type": "dcat:Distribution",
+                    "description": "Fine Tet Grid Part 1",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/fine_tet_nc.tar.gz_part1",
+                    "mediaType": "application/octet-stream",
                     "title": "fine_tet_nc.tar.gz_part1"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/fine_tet_nc.tar.gz_part2",
-                    "description": "Fine Tet Grid Part 2",
                     "@type": "dcat:Distribution",
+                    "description": "Fine Tet Grid Part 2",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/fine_tet_nc.tar.gz_part2",
+                    "mediaType": "application/octet-stream",
                     "title": "fine_tet_nc.tar.gz_part2"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/coarse_mixed_nc.tar_2.gz",
-                    "description": "Coarse MixedElem Grid",
                     "@type": "dcat:Distribution",
+                    "description": "Coarse MixedElem Grid",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/coarse_mixed_nc.tar_2.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "coarse_mixed_nc.tar.gz"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_462",
+            "issued": "2011-09-09",
+            "keyword": [
+                "dashlink",
+                "nasa",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/462/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "RSW Node Centered Coarse Grid w/ Split Walls Coarse/Med/Fine"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-5-EXT2-NEL-V1.0",
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
+            "description": "This data set contains DERIVED\ndata from Rosetta RPC-LAP, acquired during the ROSETTA EXTENSION 2\nmission phase where the primary target was the comet\n67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). It contains electron density at\nhigher time resolution than in the DERIV2 data sets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-5-ext2-nel-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-5-EXT2-NEL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-5-ext2-nel-v1.0",
-            "description": "This data set contains DERIVED\ndata from Rosetta RPC-LAP, acquired during the ROSETTA EXTENSION 2\nmission phase where the primary target was the comet\n67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). It contains electron density at\nhigher time resolution than in the DERIV2 data sets.",
-            "title": "ROSETTA-ORBITER 67P RPCLAP 5\nEXT2 NEL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCLAP 5\nEXT2 NEL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA/3110",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Froidevaux, L., Livesey, N., Read, W., and Fuller, R.. 2020-04-20. ML3DBHCL. Version 004. MLS/Aura Level 3 Daily Binned Hydrogen Chloride (HCl) Mixing Ratio on Assorted Grids V004. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA/3110. https://disc.gsfc.nasa.gov/datacollection/ML3DBHCL_004.html. Digital Science Data.",
-            "issued": "2020-03-06",
-            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-03-06",
-            "keyword": [
-                "atmosphere",
-                "atmospheric chemistry",
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
-            "identifier": "C1725331497-GES_DISC",
-            "description": "ML3DBHCL is the EOS Aura Microwave Limb Sounder (MLS) daily binned on various vertical grids product for hydrogen chloride (HCl) derived from radiances measured primarily by the 640 GHz radiometer. The data version is 4.2. Spatial coverage is near-global (-82 to +82 degrees latitude), with each profile spaced 1.5  degrees or ~165 km along the orbit track (roughly 15 orbits per day). The recommended useful vertical range is from 100 to 0.316 hPa, and the vertical resolution is between 3 and 6 km. Users of the ML3DBHCL data product should read chapter 4 and section 3.10 of the EOS MLS Level 2 Version 4 Quality Document for more information.\n\nThe data files are archived in the netCDF4 format, which is also compatible with HDF5 readers and tools. Each file contains two grid objects (profile and column data), each with a set of data and geolocation fields, grid attributes, and metadata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML3DBHCL",
             "creator": "Froidevaux, L., Livesey, N., Read, W., and Fuller, R.",
-            "title": "MLS/Aura Level 3 Daily Binned Hydrogen Chloride (HCl) Mixing Ratio on Assorted Grids V004 (ML3DBHCL) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML3DBHCL_004.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "ML3DBHCL is the EOS Aura Microwave Limb Sounder (MLS) daily binned on various vertical grids product for hydrogen chloride (HCl) derived from radiances measured primarily by the 640 GHz radiometer. The data version is 4.2. Spatial coverage is near-global (-82 to +82 degrees latitude), with each profile spaced 1.5  degrees or ~165 km along the orbit track (roughly 15 orbits per day). The recommended useful vertical range is from 100 to 0.316 hPa, and the vertical resolution is between 3 and 6 km. Users of the ML3DBHCL data product should read chapter 4 and section 3.10 of the EOS MLS Level 2 Version 4 Quality Document for more information.\n\nThe data files are archived in the netCDF4 format, which is also compatible with HDF5 readers and tools. Each file contains two grid objects (profile and column data), each with a set of data and geolocation fields, grid attributes, and metadata.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA%2F3110",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA%2F3110",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -362986,426 +362964,450 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML3DBHCL_004.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML3DBHCL_004.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level3/ML3DBHCL.004/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level3/ML3DBHCL.004/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level3/ML3DBHCL.004/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level3/ML3DBHCL.004/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML3DBHCL_004",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML3DBHCL_004",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML3DBHCL_004.png",
+            "identifier": "C1725331497-GES_DISC",
+            "issued": "2020-03-06",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA/3110",
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
+            "series-name": "ML3DBHCL",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MLS/Aura Level 3 Daily Binned Hydrogen Chloride (HCl) Mixing Ratio on Assorted Grids V004 (ML3DBHCL) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/EHX9SEA85G8R",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "High Mountain Asia COAWST Daily 4km Regional Climate Model Simulations V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/EHX9SEA85G8R.",
-            "issued": "1999-10-01",
-            "temporal": "1999-10-01T00:00:00Z/2014-09-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2014-09-30",
-            "keyword": [
-                "precipitation",
-                "atmospheric radiation",
-                "atmosphere",
-                "cryosphere",
-                "atmospheric water vapor",
-                "snow/ice",
-                "atmospheric winds",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Batuhan Osmanoglu",
                 "hasEmail": "mailto:batuhan.osmanoglu@gmail.com"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1944179767-NSIDC_ECS",
             "description": "This data product contains either daily averaged or daily accumulated modeled data in the High Mountain Asia region, generated by the Coupled-Ocean-Atmosphere-Waves-Sediment Transport (COAWST) modeling system (operated as a regional climate model). These modeled data span 15 years and have been used by the NASA High Mountain Asia Team (HiMAT) to research water resource use.",
-            "title": "High Mountain Asia COAWST Daily 4km Regional Climate Model Simulations V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FEHX9SEA85G8R",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FEHX9SEA85G8R",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/HMA/HMA_RCMO_D.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/HMA/HMA_RCMO_D.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1944179767-NSIDC_ECS&pg%5B0%5D%5Bgsk%5D=-start_date&m=-2.1796875%2154.5625%212%211%210%210%2C2&tl=1586967473%214%21%21",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1944179767-NSIDC_ECS&pg%5B0%5D%5Bgsk%5D=-start_date&m=-2.1796875%2154.5625%212%211%210%210%2C2&tl=1586967473%214%21%21",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/HMA_RCMO_D/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/HMA_RCMO_D/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/EHX9SEA85G8R",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/EHX9SEA85G8R",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/EHX9SEA85G8R",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/EHX9SEA85G8R",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1944179767-NSIDC_ECS",
+            "issued": "1999-10-01",
+            "keyword": [
+                "precipitation",
+                "atmospheric radiation",
+                "atmosphere",
+                "cryosphere",
+                "atmospheric water vapor",
+                "snow/ice",
+                "atmospheric winds",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/EHX9SEA85G8R",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2014-09-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "49.1684 20.96392 120.8316 46.34996",
+            "temporal": "1999-10-01T00:00:00Z/2014-09-30T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "High Mountain Asia COAWST Daily 4km Regional Climate Model Simulations V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0510-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-12-27T15:34:15.000 to 2014-12-27T18:59:28.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0510-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0510-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0510-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-12-27T15:34:15.000 to 2014-12-27T18:59:28.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0510 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0510 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.24400/527896/A01-2023.017\r\n10.24400/527896/A01-2023.018\r\n10.24400/527896/A01-2024.003",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Surface Water Ocean Topography (SWOT). 2024-02-01. SWOT Level 2 KaRIn Low Rate Sea Surface Height Data Product. Version 2.0. SWOT Level 2 KaRIn Low Rate Sea Surface Height Data Product, Version 2.0. Jet Propulsion Laboratory. Archived by National Aeronautics and Space Administration, U.S. Government, JPL NASA. https://doi.org/10.24400/527896/A01-2023.017\r\n10.24400/527896/A01-2023.018\r\n10.24400/527896/A01-2024.003. https://swot.jpl.nasa.gov/.",
-            "issued": "2022-07-21",
-            "temporal": "2022-12-16T00:00:00Z/2024-08-26T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-07-21",
-            "keyword": [
-                "sea surface topography",
-                "oceans",
-                "earth science",
-                "ocean waves"
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
-            "identifier": "C3206530454-POCLOUD",
-            "description": "This SWOT_L3_LR_SSH product provides ocean topography measurements obtained from the SWOT KaRIn and Nadir altimeter instruments, merged into a single variable. The dataset includes measurements from KaRIn swaths on both sides of the image, while the measurements from the Nadir altimeter are located in the central columns. In the areas between the Nadir track and the two KaRIn swaths, as well as on the outer edges of each swath (restricted to cross-track distances ranging from 10 to 60 km), default values are expected. This is a cross-calibrated product from multiple missions that contains only the ocean topography content necessary for thematic research (e.g., oceanography, geodesy) and related applications. This product is designed to be simple and ready-to-use, and can be combined with other altimetry missions. The SWOT_L3_LR_SSH product is a research-orientated extension of the L2_LR_SSH product, distributed by the SWOT project (NASA/JPL and CNES). This L3 product is managed by the SWOT Science Team project DESMOS.",
-            "release-place": "Jet Propulsion Laboratory",
-            "series-name": "SWOT Level 2 KaRIn Low Rate Sea Surface Height Data Product",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Surface Water Ocean Topography (SWOT)",
-            "title": "SWOT-AVISO Level 3 KaRIn Low Rate Sea Surface Height Data Products, Version 1.0",
-            "graphic-preview-file": "https://www.aviso.altimetry.fr/fileadmin/_processed_/4/f/csm_globeComplete_SWOT_L3_f1effc71d6.png",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This SWOT_L3_LR_SSH product provides ocean topography measurements obtained from the SWOT KaRIn and Nadir altimeter instruments, merged into a single variable. The dataset includes measurements from KaRIn swaths on both sides of the image, while the measurements from the Nadir altimeter are located in the central columns. In the areas between the Nadir track and the two KaRIn swaths, as well as on the outer edges of each swath (restricted to cross-track distances ranging from 10 to 60 km), default values are expected. This is a cross-calibrated product from multiple missions that contains only the ocean topography content necessary for thematic research (e.g., oceanography, geodesy) and related applications. This product is designed to be simple and ready-to-use, and can be combined with other altimetry missions. The SWOT_L3_LR_SSH product is a research-orientated extension of the L2_LR_SSH product, distributed by the SWOT project (NASA/JPL and CNES). This L3 product is managed by the SWOT Science Team project DESMOS.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.24400%2F527896%2FA01-2023.017%0D%0A10.24400%2F527896%2FA01-2023.018%0D%0A10.24400%2F527896%2FA01-2024.003",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.24400%2F527896%2FA01-2023.017%0D%0A10.24400%2F527896%2FA01-2023.018%0D%0A10.24400%2F527896%2FA01-2024.003",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www.aviso.altimetry.fr/fileadmin/documents/data/tools/hdbk_duacs_SWOT_L3.pdf",
-                    "description": "SWOT L3 Ocean Products User Handbook",
                     "@type": "dcat:Distribution",
+                    "description": "SWOT L3 Ocean Products User Handbook",
+                    "downloadURL": "https://www.aviso.altimetry.fr/fileadmin/documents/data/tools/hdbk_duacs_SWOT_L3.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
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
-                    "downloadURL": "https://www.aviso.altimetry.fr/en/data/products/sea-surface-height-products/global/swot-l3-ocean-products.html",
-                    "description": "Dataset Landing Page at AVISO",
                     "@type": "dcat:Distribution",
+                    "description": "Dataset Landing Page at AVISO",
+                    "downloadURL": "https://www.aviso.altimetry.fr/en/data/products/sea-surface-height-products/global/swot-l3-ocean-products.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://www.aviso.altimetry.fr/fileadmin/_processed_/4/f/csm_globeComplete_SWOT_L3_f1effc71d6.png",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://www.aviso.altimetry.fr/fileadmin/_processed_/4/f/csm_globeComplete_SWOT_L3_f1effc71d6.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.aviso.altimetry.fr/en/missions/current-missions/swot/public-release-of-the-swot-level-3-l3-product.html",
-                    "description": "Release Note",
                     "@type": "dcat:Distribution",
+                    "description": "Release Note",
+                    "downloadURL": "https://www.aviso.altimetry.fr/en/missions/current-missions/swot/public-release-of-the-swot-level-3-l3-product.html",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://www.aviso.altimetry.fr/fileadmin/_processed_/4/f/csm_globeComplete_SWOT_L3_f1effc71d6.png",
+            "identifier": "C3206530454-POCLOUD",
+            "issued": "2022-07-21",
+            "keyword": [
+                "sea surface topography",
+                "oceans",
+                "earth science",
+                "ocean waves"
+            ],
+            "landingPage": "https://doi.org/10.24400/527896/A01-2023.017\r\n10.24400/527896/A01-2023.018\r\n10.24400/527896/A01-2024.003",
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
+            "series-name": "SWOT Level 2 KaRIn Low Rate Sea Surface Height Data Product",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2022-12-16T00:00:00Z/2024-08-26T00:00:00Z",
             "theme": [
                 "SWOT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SWOT-AVISO Level 3 KaRIn Low Rate Sea Surface Height Data Products, Version 1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-TNO-PHOT-V1.0",
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
+            "description": "Published colors of Trans-Neptunian objects through December 2001",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-tno-phot-v1.0_8gyk-mfg8",
+            "issued": "2018-06-26",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-TNO-PHOT-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-tno-phot-v1.0_8gyk-mfg8",
-            "description": "Published colors of Trans-Neptunian objects through December 2001",
-            "title": "TNO PHOTOMETRY",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "TNO PHOTOMETRY"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-MIRO-2-AST1-STEINS-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Spectroscopic, Continuum and Engineering data, in the form of table files, taken during the Steins swing-by phase of the Rosetta mission by the MIRO instrument.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-miro-2-ast1-steins-v1.0_8h4y-jr3t",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "2867 steins",
                 "international rosetta mission",
                 "calibration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-MIRO-2-AST1-STEINS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-miro-2-ast1-steins-v1.0_8h4y-jr3t",
-            "description": "This data set contains Spectroscopic, Continuum and Engineering data, in the form of table files, taken during the Steins swing-by phase of the Rosetta mission by the MIRO instrument.",
-            "title": "ROSETTA-ORBITER STEINS MIRO 2 AST1 STEINS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER STEINS MIRO 2 AST1 STEINS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-3-ESC3-MTP019-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This dataset contains ROSETTA NAVCAM RADIOMETRICALLY CALIBRATED DATA of the COMET ESCORT 3 MTP019 Phase from 29 Jul. 2015, 06:02:17 to 25 Aug. 2015, 23:02:18 when at the vicinity of target 67P/CG.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-3-esc3-mtp019-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "zeta cas",
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
@@ -363413,76 +363415,76 @@
                 "dust",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-3-ESC3-MTP019-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-3-esc3-mtp019-v1.0",
-            "description": "This dataset contains ROSETTA NAVCAM RADIOMETRICALLY CALIBRATED DATA of the COMET ESCORT 3 MTP019 Phase from 29 Jul. 2015, 06:02:17 to 25 Aug. 2015, 23:02:18 when at the vicinity of target 67P/CG.",
-            "title": "ROSETTA-ORBITER 67P NAVCAM 3 COMET ESCORT 3 MTP019 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P NAVCAM 3 COMET ESCORT 3 MTP019 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMAG-3-EXT2-CALIBRATED-V9.0",
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
+            "description": "This dataset contains CALIBRATED (CODMAC LEVEL 3) DATA of the\nEXTENDED MISSION PHASE 2 (EXT2) from April 6 until June 29, 2016\nof the ROSETTA orbiter magnetometer RPCMAG. Observations are done in\nthe vicinity of comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1).\nThe current version of the dataset is V9.0.\nThe difference to the datasets of earlier versions is mainly a significantly\nimproved sensor temperature model, more detailed documentation about magnetic\ndisturbance sources, more data handling information for the user and\nalso an improved quality flagging system.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmag-3-ext2-calibrated-v9.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMAG-3-EXT2-CALIBRATED-V9.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmag-3-ext2-calibrated-v9.0",
-            "description": "This dataset contains CALIBRATED (CODMAC LEVEL 3) DATA of the\nEXTENDED MISSION PHASE 2 (EXT2) from April 6 until June 29, 2016\nof the ROSETTA orbiter magnetometer RPCMAG. Observations are done in\nthe vicinity of comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1).\nThe current version of the dataset is V9.0.\nThe difference to the datasets of earlier versions is mainly a significantly\nimproved sensor temperature model, more detailed documentation about magnetic\ndisturbance sources, more data handling information for the user and\nalso an improved quality flagging system.",
-            "title": "ROSETTA-ORBITER 67P RPCMAG 3 EXT2 CALIBRATED V9.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCMAG 3 EXT2 CALIBRATED V9.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-NIMS-2-EDR-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "NIMS Experiment Data Record (EDR) files contain raw data from the Galileo Orbiter Near-Infrared Mapping Spectrometer (CARLSONETAL1992). This raw data requires considerable processing before it is readily amenable to science analysis. The EDRs comprise the base dataset from which spectral image cubes will be created by continually evolving software using successively more accurate calibration and geometry data.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-nims-2-edr-v2.0_8h6g-nwxn",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "jupiter",
                 "europa",
@@ -363492,182 +363494,158 @@
                 "ganymede",
                 "j rings"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-NIMS-2-EDR-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-nims-2-edr-v2.0_8h6g-nwxn",
-            "description": "NIMS Experiment Data Record (EDR) files contain raw data from the Galileo Orbiter Near-Infrared Mapping Spectrometer (CARLSONETAL1992). This raw data requires considerable processing before it is readily amenable to science analysis. The EDRs comprise the base dataset from which spectral image cubes will be created by continually evolving software using successively more accurate calibration and geometry data.",
-            "title": "GALILEO NIMS EXPERIMENT DATA RECORDS: JUPITER OPERATIONS",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GALILEO NIMS EXPERIMENT DATA RECORDS: JUPITER OPERATIONS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H43R0QR1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Rosensweig, C. and  A. Iglesias. 1999-12-31. Potential Impacts of Climate Change on World Food Supply: Datasets from a Major Crop Modeling Study. Version 1.00. New York, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Goddard Institute for Space Studies (GISS). https://doi.org/10.7927/H43R0QR1. https://doi.org/10.7927/H43R0QR1.",
-            "issued": "1999-12-31",
-            "temporal": "1995-01-01T00:00:00Z/2110-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "1999-12-31",
-            "references": [
-                "https://doi.org/10.7927/H4JM27JZ"
-            ],
-            "keyword": [
-                "economic resources",
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
-            "identifier": "C2211120688-SEDAC",
-            "description": "The Potential Impacts of Climate Change on World Food Supply: Datasets from a Major Crop Modeling Study contain projected country and regional changes in grain crop yields due to global climate change. Equilibrium and transient scenarios output from General Circulation Models (GCMs) with three levels of farmer adaptations to climate change were utilized to generate crop yield estimates of wheat, rice, coarse grains (barley and maize), and protein feed (soybean) at 125 agricultural sites representing major world agricultural regions. Projected yields at the agricultural sites were aggregated to major trading regions, and fed into the Basic Linked Systems (BLS) global trade model to produce country and regional estimates of potential price increases, food shortages, and risk of hunger. These datasets are produced by the Goddard Institute for Space Studies (GISS) and are distributed by the Columbia University Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "New York, NY",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Rosensweig, C. and  A. Iglesias",
-            "title": "Potential Impacts of Climate Change on World Food Supply: Datasets from a Major Crop Modeling Study",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/crop-climate/crop-climate-potential-impacts-world-food-supply/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Potential Impacts of Climate Change on World Food Supply: Datasets from a Major Crop Modeling Study contain projected country and regional changes in grain crop yields due to global climate change. Equilibrium and transient scenarios output from General Circulation Models (GCMs) with three levels of farmer adaptations to climate change were utilized to generate crop yield estimates of wheat, rice, coarse grains (barley and maize), and protein feed (soybean) at 125 agricultural sites representing major world agricultural regions. Projected yields at the agricultural sites were aggregated to major trading regions, and fed into the Basic Linked Systems (BLS) global trade model to produce country and regional estimates of potential price increases, food shortages, and risk of hunger. These datasets are produced by the Goddard Institute for Space Studies (GISS) and are distributed by the Columbia University Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH43R0QR1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH43R0QR1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/crop-climate/crop-climate-potential-impacts-world-food-supply/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/crop-climate/crop-climate-potential-impacts-world-food-supply/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/crop-climate-potential-impacts-world-food-supply/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/crop-climate-potential-impacts-world-food-supply/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/crop-climate-potential-impacts-world-food-supply/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/crop-climate-potential-impacts-world-food-supply/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/crop-climate-potential-impacts-world-food-supply",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/crop-climate-potential-impacts-world-food-supply",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/crop-climate/crop-climate-potential-impacts-world-food-supply/sedac-logo.jpg",
+            "identifier": "C2211120688-SEDAC",
+            "issued": "1999-12-31",
+            "keyword": [
+                "economic resources",
+                "earth science",
+                "human dimensions"
+            ],
+            "landingPage": "https://doi.org/10.7927/H43R0QR1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1999-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H4JM27JZ"
+            ],
+            "release-place": "New York, NY",
             "spatial": "-180.0 -58.0 180.0 90.0",
+            "temporal": "1995-01-01T00:00:00Z/2110-12-31T00:00:00Z",
             "theme": [
                 "CROPCLIM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Potential Impacts of Climate Change on World Food Supply: Datasets from a Major Crop Modeling Study"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3324-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-06-24T11:05:10.000 to 2012-06-24T14:26:24.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3324-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars express"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3324-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3324-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-06-24T11:05:10.000 to 2012-06-24T14:26:24.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3324 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3324 V1.0"
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
-                "turbulence",
-                "cases",
-                "flow",
-                "incompressible",
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
-            "identifier": "NASA-842__10",
             "description": "This grouping contains the incompressible-flow cases from the 1980-81 Data Library.",
-            "title": "Collaborative Testing of Turbulence Models: Incompressible Flow Cases from 1980-81 Data Library",
-            "programCode": [
-                "026:023"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -363675,506 +363653,504 @@
                     "mediaType": "application/txt"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-842__10",
+            "issued": "2018-06-25",
+            "keyword": [
+                "turbulence",
+                "cases",
+                "flow",
+                "incompressible",
+                "models"
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
-            "landingPage": "https://doi.org/10.5067/ECG5D-ODE44",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.. 2021-04-19. ECCO Ocean Density, Stratification, and Hydrostatic Pressure - Daily Mean 0.5 Degree (Version 4 Release 4). Version V4r4. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/ECG5D-ODE44. ECCO; ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.; 2020; ECCO Ocean Density; Stratification; and Hydrostatic Pressure - Daily Mean 0.5 Degree (Version 4 Release 4); 10.5067/ECG5D-ODE44; https://podaac.jpl.nasa.gov/ECCO.",
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
-                "ocean pressure",
-                "oceans",
-                "earth science services"
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
-            "identifier": "C1990404793-POCLOUD",
-            "description": "This dataset contains daily-averaged ocean density, stratification, and hydrostatic pressure interpolated to a regular 0.5-degree grid from the ECCO Version 4 revision 4 (V4r4) ocean and sea-ice state estimate. Estimating the Circulation and Climate of the Ocean (ECCO) ocean and sea-ice state estimates are dynamically and kinematically-consistent reconstructions of the three-dimensional, time-evolving ocean, sea-ice, and surface atmospheric states. ECCO V4r4 is a free-running solution of the 1-degree global configuration of the MIT general circulation model (MITgcm) that has been fit to observations in a least-squares sense. Observational data constraints used in V4r4 include sea surface height (SSH) from satellite altimeters [ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jason-1,2,3, CryoSat-2, and SARAL/AltiKa]; sea surface temperature (SST) from satellite radiometers [AVHRR], sea surface salinity (SSS) from the Aquarius satellite radiometer/scatterometer, ocean bottom pressure (OBP) from the GRACE satellite gravimeter; sea ice concentration from satellite radiometers [SSM/I and SSMIS], and in-situ ocean temperature and salinity measured with conductivity-temperature-depth (CTD) sensors and expendable bathythermographs (XBTs) from several programs [e.g., WOCE, GO-SHIP, Argo, and others] and platforms [e.g.,research vessels, gliders, moorings, ice-tethered profilers, and instrumented pinnipeds]. V4r4 covers the period 1992-01-01T12:00:00 to 2018-01-01T00:00:00.",
-            "release-place": "PO.DAAC",
-            "graphic-preview-description": "Thumbnail image for Website",
             "creator": "ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.",
-            "title": "ECCO Ocean Density, Stratification, and Hydrostatic Pressure - Daily Mean 0.5 Degree (Version 4 Release 4)",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_DENS_STRAT_PRESS_05DEG_DAILY_V4R4.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset contains daily-averaged ocean density, stratification, and hydrostatic pressure interpolated to a regular 0.5-degree grid from the ECCO Version 4 revision 4 (V4r4) ocean and sea-ice state estimate. Estimating the Circulation and Climate of the Ocean (ECCO) ocean and sea-ice state estimates are dynamically and kinematically-consistent reconstructions of the three-dimensional, time-evolving ocean, sea-ice, and surface atmospheric states. ECCO V4r4 is a free-running solution of the 1-degree global configuration of the MIT general circulation model (MITgcm) that has been fit to observations in a least-squares sense. Observational data constraints used in V4r4 include sea surface height (SSH) from satellite altimeters [ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jason-1,2,3, CryoSat-2, and SARAL/AltiKa]; sea surface temperature (SST) from satellite radiometers [AVHRR], sea surface salinity (SSS) from the Aquarius satellite radiometer/scatterometer, ocean bottom pressure (OBP) from the GRACE satellite gravimeter; sea ice concentration from satellite radiometers [SSM/I and SSMIS], and in-situ ocean temperature and salinity measured with conductivity-temperature-depth (CTD) sensors and expendable bathythermographs (XBTs) from several programs [e.g., WOCE, GO-SHIP, Argo, and others] and platforms [e.g.,research vessels, gliders, moorings, ice-tethered profilers, and instrumented pinnipeds]. V4r4 covers the period 1992-01-01T12:00:00 to 2018-01-01T00:00:00.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECG5D-ODE44",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECG5D-ODE44",
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_DENS_STRAT_PRESS_05DEG_DAILY_V4R4.jpg",
-                    "description": "Thumbnail image for Website",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail image for Website",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_DENS_STRAT_PRESS_05DEG_DAILY_V4R4.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ECG5D-ODE44",
-                    "description": "Access the data set landing page for the collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data set landing page for the collection.",
+                    "downloadURL": "https://doi.org/10.5067/ECG5D-ODE44",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1990404793-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1990404793-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1990404793-POCLOUD/temporal",
-                    "description": "Browse and download granules over HTTPS using the virtual directories service",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories service",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1990404793-POCLOUD/temporal",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 }
             ],
+            "graphic-preview-description": "Thumbnail image for Website",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_DENS_STRAT_PRESS_05DEG_DAILY_V4R4.jpg",
+            "identifier": "C1990404793-POCLOUD",
+            "issued": "2021-01-01",
+            "keyword": [
+                "salinity/density",
+                "earth science reanalyses/assimilation models",
+                "earth science",
+                "models",
+                "ocean pressure",
+                "oceans",
+                "earth science services"
+            ],
+            "landingPage": "https://doi.org/10.5067/ECG5D-ODE44",
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
+            "title": "ECCO Ocean Density, Stratification, and Hydrostatic Pressure - Daily Mean 0.5 Degree (Version 4 Release 4)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/143",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hall, F. G., K. F. Huemmrich, D. E. Strebel, S. J. Goetz, J. E. Nickeson, and K. D. Woods. 1996. Forest Canopy Composition (SNF). [Forest Canopy Composition (Superior National Forest)]. Data set. Available on-line [http://www.daac.ornl.gov] from Oak Ridge National Laboratory Distributed Active Archive Center, Oak Ridge, Tennessee, U.S.A. Based on F. G. Hall, K. F. Huemmrich, D. E. Strebel, S. J. Goetz, J. E. Nickeson, and K. D. Woods, Biophysical, Morphological, Canopy Optical Property, and Productivity Data from the Superior National Forest, NASA Technical Memorandum 104568, National Aeronautics and Space Administration, Goddard Space Flight Center, Greenbelt, Maryland, U.S.A., 1992. doi:10.3334/ORNLDAAC/143",
-            "issued": "2024-03-02",
-            "temporal": "1976-01-01T00:00:00Z/1986-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-04",
-            "keyword": [
-                "atmospheric radiation",
-                "biosphere",
-                "earth science",
-                "vegetation",
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
-            "identifier": "C2884972378-ORNL_CLOUD",
             "description": "SNF study site count of the number of trees over 2 meters, broken down by species code; see also SNF Plant Species Codes",
-            "graphic-preview-description": "Browse Image",
-            "title": "Forest Canopy Composition (SNF)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/snf_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F143",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F143",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/snf/SNF_CAN_COMP/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/snf/SNF_CAN_COMP/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/SNF/guides/forest_canopy_composition.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/SNF/guides/forest_canopy_composition.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/143",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/143",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_CAN_COMP/comp/can_comp.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_CAN_COMP/comp/can_comp.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_CAN_COMP/comp/can_comp.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_CAN_COMP/comp/can_comp.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_CAN_COMP/comp/forest_canopy_composition.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_CAN_COMP/comp/forest_canopy_composition.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_CAN_COMP/comp/forest_canopy_composition.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_CAN_COMP/comp/forest_canopy_composition.txt",
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
+            "identifier": "C2884972378-ORNL_CLOUD",
+            "issued": "2024-03-02",
+            "keyword": [
+                "atmospheric radiation",
+                "biosphere",
+                "earth science",
+                "vegetation",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/143",
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
+            "temporal": "1976-01-01T00:00:00Z/1986-12-31T23:59:59Z",
             "theme": [
                 "SNF",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Forest Canopy Composition (SNF)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/4FRNSHRF3TRY",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMAPVEX12 Land Cover Classification Map V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/4FRNSHRF3TRY.",
-            "issued": "2012-06-07",
-            "temporal": "2012-06-07T00:00:00Z/2012-07-19T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2012-07-19",
-            "keyword": [
-                "earth science",
-                "land surface",
-                "land use/land cover"
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
-            "identifier": "C1000000480-NSIDC_ECS",
             "description": "This data set consists of land cover classification data derived from satellite imagery as part of the Soil Moisture Active Passive Validation Experiment 2012 (SMAPVEX12). Images from the RADARSAT-2, Syst\u00e8me Pour l'Observation de la Terre (SPOT-4), and DMC International Imaging Ltd (DMCii) of the study area were retrieved for the summer of 2012. The land use classification image provides information about vegetation present in the study area at a resolution of 20 meters.",
-            "title": "SMAPVEX12 Land Cover Classification Map V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F4FRNSHRF3TRY",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F4FRNSHRF3TRY",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_VAL/SV12LC.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_VAL/SV12LC.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000480-NSIDC_ECS&m=40.359375%21-98.419921875%214%211%210%210%2C2&q=SMAPVEX12&ok=SMAPVEX12",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000480-NSIDC_ECS&m=40.359375%21-98.419921875%214%211%210%210%2C2&q=SMAPVEX12&ok=SMAPVEX12",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SV12LC/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SV12LC/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/4FRNSHRF3TRY",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/4FRNSHRF3TRY",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/4FRNSHRF3TRY",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/4FRNSHRF3TRY",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1000000480-NSIDC_ECS",
+            "issued": "2012-06-07",
+            "keyword": [
+                "earth science",
+                "land surface",
+                "land use/land cover"
+            ],
+            "landingPage": "https://doi.org/10.5067/4FRNSHRF3TRY",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2012-07-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-98.97 49.31 -98.27 50.21",
+            "temporal": "2012-06-07T00:00:00Z/2012-07-19T23:59:59.999Z",
             "theme": [
                 "SMAPVEX12",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMAPVEX12 Land Cover Classification Map V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/M4LJAG1CKOWQ",
             "citation": "Miyazaki, Kazuyuki. 2024-02-06. TRPSCRENOXSM2D. Version 1. TROPESS Chemical Reanalysis Surface Soil NOx emissions Monthly 2-dimensional Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/M4LJAG1CKOWQ. https://disc.gsfc.nasa.gov/datacollection/TRPSCRENOXSM2D_1.html. Digital Science Data.",
-            "issued": "2023-01-09",
-            "temporal": "2005-01-01T00:00:00Z/2024-02-12T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-09",
-            "references": [
-                "https://doi.org/10.1126/sciadv.abf7460"
-            ],
-            "keyword": [
-                "atmosphere",
-                "atmospheric chemistry",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "KAZUYUKI MIYAZAKI",
                 "hasEmail": "mailto:kazuyuki.miyazaki@jpl.nasa.gov"
             },
+            "creator": "Miyazaki, Kazuyuki",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2837624980-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS Chemical Reanalysis Surface Soil NOx emissions Monthly 2-dimensional Product contains nitrogen oxides (NO and NO2) emissions from surface soil sources. The data are part of the Tropospheric Chemical Reanalysis v2 (TCR-2) for the period 2005-2021. TCR-2 uses JPL's Multi-mOdel Multi-cOnstituent Chemical (MOMO-Chem) data assimilation framework that simultaneously optimizes both concentrations and emissions of multiple species from multiple satellite sensors.\n\nThe data files are written in the netCDF version 4 file format, and each file contains a year of data at monthly resolution, and a spatial resolution of 1.125 x 1.125 degrees. The principal investigator for the TCR-2 data is Miyazaki, Kazuyuki.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSCRENOXSM2D",
-            "creator": "Miyazaki, Kazuyuki",
-            "graphic-preview-description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
-            "title": "TROPESS Chemical Reanalysis Surface Soil NOx emissions Monthly 2-dimensional Product V1 (TRPSCRENOXSM2D) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRENOXSM2D_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FM4LJAG1CKOWQ",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FM4LJAG1CKOWQ",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRENOXSM2D_Sample.png",
-                    "description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRENOXSM2D_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSCRENOXSM2D_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSCRENOXSM2D_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_MON_VERTCONCS/TRPSCRENOXSM2D.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_MON_VERTCONCS/TRPSCRENOXSM2D.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSCRENOXSM2D_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSCRENOXSM2D_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TCR2_MON_VERTCONCS/TRPSCRENOXSM2D.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TCR2_MON_VERTCONCS/TRPSCRENOXSM2D.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_MON_VERTCONCS/TRPSCRENOXSM2D.1/doc/TROPESS_ChemReanalysis_Forward_Stream_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_MON_VERTCONCS/TRPSCRENOXSM2D.1/doc/TROPESS_ChemReanalysis_Forward_Stream_README.pdf",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRENOXSM2D_Sample.png",
+            "identifier": "C2837624980-GES_DISC",
+            "issued": "2023-01-09",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/M4LJAG1CKOWQ",
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
+            "series-name": "TRPSCRENOXSM2D",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2005-01-01T00:00:00Z/2024-02-12T00:00:00Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS Chemical Reanalysis Surface Soil NOx emissions Monthly 2-dimensional Product V1 (TRPSCRENOXSM2D) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-03-06",
-            "temporal": "2021-03-06T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "international",
-                "trajectory",
-                "topo",
-                "station",
-                "space",
-                "location",
-                "coordinates",
-                "coords",
-                "iss",
-                "ephemeris"
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
-            "identifier": "nasa-iss-data_2021-03-06",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2021-03-06",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -364297,291 +364273,316 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2021-03-06",
+            "issued": "2021-03-06",
+            "keyword": [
+                "international",
+                "trajectory",
+                "topo",
+                "station",
+                "space",
+                "location",
+                "coordinates",
+                "coords",
+                "iss",
+                "ephemeris"
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
+            "temporal": "2021-03-06T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2021-03-06"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GNSS/GNSS_IGSUCSUM_001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GGL/CDDIS. https://doi.org/10.5067/GNSS/GNSS_IGSUCSUM_001.",
-            "issued": "1992-01-01",
-            "temporal": "1992-01-01T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-10-28",
-            "keyword": [
-                "geodetics",
-                "earth science",
-                "gravity/gravitational field",
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
-            "identifier": "C1427048413-CDDIS",
             "description": "This derived product set consists of Global Navigation Satellite System Rapid Orbit/Reference Frame Product Summary from the NASA Crustal Dynamics Data Information System (CDDIS). GNSS provide autonomous geo-spatial positioning with global coverage. GNSS data sets from ground receivers at the CDDIS consist primarily of the data from the U.S. Global Positioning System (GPS) and the Russian GLObal NAvigation Satellite System (GLONASS). Since 2011, the CDDIS GNSS archive includes data from other GNSS (Europe\u2019s Galileo, China\u2019s Beidou, Japan\u2019s Quasi-Zenith Satellite System/QZSS, the Indian Regional Navigation Satellite System/IRNSS, and worldwide Satellite Based Augmentation Systems/SBASs), which are similar to the U.S. GPS in terms of the satellite constellation, orbits, and signal structure.  Analysis Centers (ACs) of the International GNSS Service (IGS) retrieve GNSS data on regular schedules to produce GNSS derived products. The IGS Analysis Center Coordinator (ACC) uses these individual AC solutions to generate the official IGS ultra-rapid combined orbit and ERP products. The ultra-rapid orbit and ERP is a sub-daily solution, released four times per day, at 03:00, 09:00, 15:00, and 21:00 UTC (prior to GPS week 1267 they were released twice daily). The solution summary file details information about the generation of the ultra-rapid products and comparison with the individual AC solutions. The reduced latency on availability of these products allows for significantly improved orbit predictions and reduced errors for user applications.",
-            "title": "Global Navigation Satellite System (GNSS) Ultra-Rapid Orbit/Clock/ERP Product Comparison Summary from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGNSS_IGSUCSUM_001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGNSS_IGSUCSUM_001",
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
-                    "downloadURL": "http://dx.doi.org/10.5067/GNSS/GNSS_IGSUCSUM_001",
-                    "description": "URL for more information about GNSS derived products",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about GNSS derived products",
+                    "downloadURL": "http://dx.doi.org/10.5067/GNSS/GNSS_IGSUCSUM_001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1427048413-CDDIS",
+            "issued": "1992-01-01",
+            "keyword": [
+                "geodetics",
+                "earth science",
+                "gravity/gravitational field",
+                "tectonics",
+                "solid earth"
+            ],
+            "landingPage": "https://doi.org/10.5067/GNSS/GNSS_IGSUCSUM_001",
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
+            "title": "Global Navigation Satellite System (GNSS) Ultra-Rapid Orbit/Clock/ERP Product Comparison Summary from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amisc&version=1.0",
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
-                "pds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This Bundle contains miscellaneous products, mostly stragglers",
+            "identifier": "urn:nasa:pds:misc",
+            "issued": "2021-05-21",
+            "keyword": [
+                "pds"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amisc&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:misc",
-            "description": "This Bundle contains miscellaneous products, mostly stragglers",
-            "title": "PDS4 Miscellaneous Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "PDS4 Miscellaneous Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/6C6WA3R918HJ",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Pre-IceBridge ATM L2 Icessn Elevation, Slope, and Roughness V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/6C6WA3R918HJ.",
-            "issued": "1993-06-23",
-            "temporal": "1993-06-23T00:00:00Z/2008-10-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2008-10-30",
-            "keyword": [
-                "glaciers/ice sheets",
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
-            "identifier": "C1291937280-NSIDC_ECS",
             "description": "This data set contains resampled and smoothed elevation measurements of Arctic and Antarctic sea ice, and Greenland, Antarctic and Arctic region land ice surface acquired using the NASA Airborne Topographic Mapper (ATM) instrumentation.",
-            "title": "Pre-IceBridge ATM L2 Icessn Elevation, Slope, and Roughness V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F6C6WA3R918HJ",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F6C6WA3R918HJ",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/PRE_OIB/BLATM2.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/PRE_OIB/BLATM2.001/",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1291937280-NSIDC_ECS&m=-102.375%21-34.59375%210%211%210%210%2C2&q=BLATM&ok=BLATM2",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1291937280-NSIDC_ECS&m=-102.375%21-34.59375%210%211%210%210%2C2&q=BLATM&ok=BLATM2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/BLATM2/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/BLATM2/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/PRE_OIB/BLATM2.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/PRE_OIB/BLATM2.001/",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1291937280-NSIDC_ECS&m=-102.375%21-34.59375%210%211%210%210%2C2&q=BLATM&ok=BLATM2",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1291937280-NSIDC_ECS&m=-102.375%21-34.59375%210%211%210%210%2C2&q=BLATM&ok=BLATM2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/BLATM2/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/BLATM2/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/PRE_OIB/BLATM2.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/PRE_OIB/BLATM2.001/",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1291937280-NSIDC_ECS&m=-102.375%21-34.59375%210%211%210%210%2C2&q=BLATM&ok=BLATM2",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1291937280-NSIDC_ECS&m=-102.375%21-34.59375%210%211%210%210%2C2&q=BLATM&ok=BLATM2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/BLATM2/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/BLATM2/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/PRE_OIB/BLATM2.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/PRE_OIB/BLATM2.001/",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1291937280-NSIDC_ECS&m=-102.375%21-34.59375%210%211%210%210%2C2&q=BLATM&ok=BLATM2",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1291937280-NSIDC_ECS&m=-102.375%21-34.59375%210%211%210%210%2C2&q=BLATM&ok=BLATM2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/BLATM2/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/BLATM2/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/6C6WA3R918HJ",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/6C6WA3R918HJ",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/6C6WA3R918HJ",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/6C6WA3R918HJ",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1291937280-NSIDC_ECS",
+            "issued": "1993-06-23",
+            "keyword": [
+                "glaciers/ice sheets",
+                "earth science",
+                "cryosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/6C6WA3R918HJ",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2008-10-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 60.0 180.0 90.0",
+            "temporal": "1993-06-23T00:00:00Z/2008-10-30T23:59:59.999Z",
             "theme": [
                 "1993_AN_NASA",
                 "1993_GR_NASA",
@@ -364617,567 +364618,568 @@
                 "2008_GR_NASA",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Pre-IceBridge ATM L2 Icessn Elevation, Slope, and Roughness V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/8XB4RU470FJV",
             "citation": "AIRS project. 2019-12-15. AIRX3STD. Version 7.0. Aqua/AIRS L3 Daily Standard Physical Retrieval (AIRS+AMSU) 1 degree x 1 degree V7.0. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/8XB4RU470FJV. https://disc.gsfc.nasa.gov/datacollection/AIRX3STD_7.0.html. Digital Science Data.",
-            "issued": "2002-08-31",
-            "temporal": "2002-08-31T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-09-25",
-            "references": [
-                "https://doi.org/10.1117/1.JRS.8.084994",
-                "https://doi.org/10.5194/acp-14-399-2014"
-            ],
-            "keyword": [
-                "atmospheric temperature",
-                "oceans",
-                "land surface",
-                "earth science",
-                "clouds",
-                "air quality",
-                "altitude",
-                "atmosphere",
-                "atmospheric chemistry",
-                "atmospheric pressure",
-                "atmospheric radiation",
-                "ocean temperature",
-                "atmospheric water vapor",
-                "surface thermal properties",
-                "surface radiative properties"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "LENA IREDELL",
                 "hasEmail": "mailto:lena.iredell@nasa.gov"
             },
+            "creator": "AIRS project",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1701805672-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The Atmospheric Infrared Sounder (AIRS) is a grating spectrometer (R = 1200) aboard the second Earth Observing System (EOS) polar-orbiting platform, EOS Aqua. In combination with the Advanced Microwave Sounding Unit (AMSU) AIRS constitutes an innovative atmospheric sounding group of infrared and microwave sensors. The AIRS Level 3 Daily Gridded Product contains standard retrieval means, standard deviations and input counts. Each file covers a temporal period of 24 hours for either the descending (equatorial crossing North to South at 1:30 AM local time) or ascending (equatorial crossing South to North at 1:30 PM local time) orbit. The data starts at the international dateline and progresses westward (as do the subsequent orbits of the satellite) so that neighboring gridded cells of data are no more than a swath of time apart (about 90 minutes). The two parts of a scan line crossing the dateline are included in separate L3 files, according to the date, so that data points in a grid box are always coincident in time. The edge of the AIRS Level 3 gridded cells is at the date line (the 180E/W longitude boundary). When plotted, this produces a map with 0 degrees longitude in the center of the image unless the bins are reordered. This method is preferred because the left (West) side of the image and the right (East) side of the image contain data farthest apart in time. The gridding scheme used by AIRS is the same as used by TOVS Pathfinder to create Level 3 products. The daily Level 3 products have gores between satellite paths where there is no coverage for that day. The geophysical parameters have been averaged and binned into 1 x 1 deg grid cells, from -180.0 to +180.0 deg longitude and from -90.0 to +90.0 deg latitude. The value for each grid box is the sum of the values that fall within the 1x1 area divided by the number of points in the box. For each grid map of 4-byte floating-point mean values there is a corresponding 4-byte floating-point map of standard deviation and a 2-byte integer grid map of counts. The counts map provides the user with the number of points per bin that were included in the mean and can be used to generate custom multi-day maps from the daily gridded products. The thermodynamic parameters are: Skin Temperature (land and sea surface), Air Temperature at the surface, Profiles of Air Temperature and Water Vapor, Tropopause Characteristics, Column Precipitable Water, Cloud Amount/Frequency, Cloud Height, Cloud Top Pressure, Cloud Top Temperature, Reflectance, Emissivity, Surface Pressure, Cloud Vertical Distribution. The trace gases parameters are: Total Amounts and Vertical Profiles of Carbon Monoxide, Methane, and Ozone. The actual names of the variables in the data files should be inferred from the Processing File Description document.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "AIRX3STD",
-            "creator": "AIRS project",
-            "graphic-preview-description": "Sample data of the \"AIRS/Aqua Level 3 daily standard physical retrieval product (AIRS/AMSU without HSB)\".",
-            "title": "Aqua/AIRS L3 Daily Standard Physical Retrieval (AIRS+AMSU) 1 degree x 1 degree V7.0 at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRX3STD_7.0.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F8XB4RU470FJV",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F8XB4RU470FJV",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRX3STD_7.0.png",
-                    "description": "Sample data of the \"AIRS/Aqua Level 3 daily standard physical retrieval product (AIRS/AMSU without HSB)\".",
                     "@type": "dcat:Distribution",
+                    "description": "Sample data of the \"AIRS/Aqua Level 3 daily standard physical retrieval product (AIRS/AMSU without HSB)\".",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRX3STD_7.0.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRX3STD_7.0.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRX3STD_7.0.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level3/AIRX3STD.7.0/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level3/AIRX3STD.7.0/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level3/AIRX3STD.7.0",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level3/AIRX3STD.7.0",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRX3STD+7.0",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRX3STD+7.0",
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
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/AIRS/Overview_of_AIRS_Products_and_Documentation.pdf",
-                    "description": "Overview of the AIRS Mission: Instruments, Processing Algorithms, Products, and Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Overview of the AIRS Mission: Instruments, Processing Algorithms, Products, and Documentation",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/AIRS/Overview_of_AIRS_Products_and_Documentation.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/AIRS/V7_L3_User_Guide.pdf",
-                    "description": "AIRS Version 7 Level 3 Product User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "AIRS Version 7 Level 3 Product User Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/AIRS/V7_L3_User_Guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "graphic-preview-description": "Sample data of the \"AIRS/Aqua Level 3 daily standard physical retrieval product (AIRS/AMSU without HSB)\".",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRX3STD_7.0.png",
+            "identifier": "C1701805672-GES_DISC",
+            "issued": "2002-08-31",
+            "keyword": [
+                "atmospheric temperature",
+                "oceans",
+                "land surface",
+                "earth science",
+                "clouds",
+                "air quality",
+                "altitude",
+                "atmosphere",
+                "atmospheric chemistry",
+                "atmospheric pressure",
+                "atmospheric radiation",
+                "ocean temperature",
+                "atmospheric water vapor",
+                "surface thermal properties",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/8XB4RU470FJV",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2016-09-25",
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
+            "series-name": "AIRX3STD",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-08-31T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aqua/AIRS L3 Daily Standard Physical Retrieval (AIRS+AMSU) 1 degree x 1 degree V7.0 at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/7Y7KSA1QNQP8",
             "citation": "Glen Jaross. 2017-06-15. OMPS_NPP_NMTO3_L3_DAILY. Version 2. OMPS-NPP L3 NM Ozone (O3) Total Column 1.0 deg grid daily V2. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/7Y7KSA1QNQP8. https://disc.gsfc.nasa.gov/datacollection/OMPS_NPP_NMTO3_L3_DAILY_2.html. Digital Science Data.",
-            "issued": "2016-12-31",
-            "temporal": "2012-01-25T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-12-31",
-            "keyword": [
-                "atmosphere",
-                "atmospheric chemistry",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "GLENN JAROSS, PH. D",
                 "hasEmail": "mailto:Glen.R.Jaross@nasa.gov"
             },
+            "creator": "Glen Jaross",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1393527975-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The OMPS-NPP L3 NM Ozone (O3) Total Column 1.0 deg grid daily product provides total ozone measurements from the Ozone Mapping and Profiling Suite (OMPS) Nadir-Mapper (NM) instrument on the Suomi-NPP satellite.\nThe level-3 gridding algorithm is used to combine the orbital OMPS cross track measurements into a daily map product with a fixed global grid. Grid cells are computed as weighted averages of a given parameter derived for the field-of-views that overlay the given cell. The current version of this product includes UV aerosol index and reflectivity at 331 nm retrievals as well. \n\nEach granule contains data for a full day. Spatial coverage is global (-90 to  90 degrees latitude), with a resolution of 1.0 degree in longitude and 1.0 degree in latitude, and array size of 360 by 180. The files are written using the Hierarchical Data Format Version 5 or HDF5.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OMPS_NPP_NMTO3_L3_DAILY",
-            "creator": "Glen Jaross",
-            "title": "OMPS-NPP L3 NM Ozone (O3) Total Column 1.0 deg grid daily V2",
-            "graphic-preview-description": "OMPS Logo",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMPS_NPP_NMTO3_L3_DAILY_2.jpeg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F7Y7KSA1QNQP8",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F7Y7KSA1QNQP8",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMPS_NPP_NMTO3_L3_DAILY_2.jpeg",
-                    "description": "OMPS Logo",
                     "@type": "dcat:Distribution",
+                    "description": "OMPS Logo",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMPS_NPP_NMTO3_L3_DAILY_2.jpeg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMPS_NPP_NMTO3_L3_DAILY_2.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMPS_NPP_NMTO3_L3_DAILY_2.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://snpp-omps.gesdisc.eosdis.nasa.gov/data/SNPP_OMPS_Level3/OMPS_NPP_NMTO3_L3_DAILY.2/",
-                    "description": "Access the data via HTTPS.",
+                {
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://snpp-omps.gesdisc.eosdis.nasa.gov/data/SNPP_OMPS_Level3/OMPS_NPP_NMTO3_L3_DAILY.2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://snpp-omps.gesdisc.eosdis.nasa.gov/opendap/SNPP_OMPS_Level3/OMPS_NPP_NMTO3_L3_DAILY.2/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://snpp-omps.gesdisc.eosdis.nasa.gov/opendap/SNPP_OMPS_Level3/OMPS_NPP_NMTO3_L3_DAILY.2/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMPS_NPP_NMTO3_L3_DAILY_2",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMPS_NPP_NMTO3_L3_DAILY_2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://snpp-omps.gesdisc.eosdis.nasa.gov/data/SNPP_OMPS_Level3/OMPS_NPP_NMTO3_L3_DAILY.2/doc/README.OMPS_NPP_NMTO3_L3_DAILY.2.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://snpp-omps.gesdisc.eosdis.nasa.gov/data/SNPP_OMPS_Level3/OMPS_NPP_NMTO3_L3_DAILY.2/doc/README.OMPS_NPP_NMTO3_L3_DAILY.2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://jointmission.gsfc.nasa.gov",
-                    "description": "Joint Polar Satellite System (JPSS) mission home page",
                     "@type": "dcat:Distribution",
+                    "description": "Joint Polar Satellite System (JPSS) mission home page",
+                    "downloadURL": "https://jointmission.gsfc.nasa.gov",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "graphic-preview-description": "OMPS Logo",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMPS_NPP_NMTO3_L3_DAILY_2.jpeg",
+            "identifier": "C1393527975-GES_DISC",
+            "issued": "2016-12-31",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/7Y7KSA1QNQP8",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2016-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "OMPS_NPP_NMTO3_L3_DAILY",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-25T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OMPS-NPP L3 NM Ozone (O3) Total Column 1.0 deg grid daily V2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/IS-40e/TEMPO/O3TOT_L3.003",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/IS-40e/TEMPO/O3TOT_L3.003.",
-            "issued": "2024-04-03",
-            "temporal": "2023-08-01T00:00:00Z/2025-01-06T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-02",
-            "keyword": [
-                "atmospheric chemistry",
-                "earth science",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Raid Suleiman",
                 "hasEmail": "mailto:rsuleiman@cfa.harvard.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2930764281-LARC_CLOUD",
             "description": "Total ozone Level 3 files provide ozone information on a regular grid covering the TEMPO field of regard for nominal TEMPO observations. Level 3 files are derived by combining information from all Level 2 files constituting a TEMPO East-West scan cycle. The files are provided in netCDF4 format, and contain information on total column ozone and some auxiliary derived and ancillary input parameters including effective cloud fraction, effective cloud pressure, radiative cloud fraction, SO2 index, and terrain pressure. The re-gridding algorithm uses an area-weighted approach. These data reached provisional validation on December 9, 2024.",
-            "graphic-preview-description": "Mission Logo",
-            "title": "TEMPO gridded ozone total column V03 (PROVISIONAL)",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/tempo.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIS-40e%2FTEMPO%2FO3TOT_L3.003",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIS-40e%2FTEMPO%2FO3TOT_L3.003",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://tempo.si.edu",
-                    "description": "TEMPO project page",
                     "@type": "dcat:Distribution",
+                    "description": "TEMPO project page",
+                    "downloadURL": "http://tempo.si.edu",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/IS-40e/TEMPO/O3TOT_L3.003",
-                    "description": "DOI data set landing page for TEMPO_O3TOT_L3_V03",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TEMPO_O3TOT_L3_V03",
+                    "downloadURL": "https://doi.org/10.5067/IS-40e/TEMPO/O3TOT_L3.003",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://asdc.larc.nasa.gov/static/images/project_logos/tempo.png",
-                    "description": "Mission Logo",
                     "@type": "dcat:Distribution",
+                    "description": "Mission Logo",
+                    "downloadURL": "https://asdc.larc.nasa.gov/static/images/project_logos/tempo.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization through WORLDVIEW"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/TEMPO",
-                    "description": "ASDC Data and Information for TEMPO",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for TEMPO",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/TEMPO",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2930764281-LARC_CLOUD",
-                    "description": "Earthdata Search for TEMPO_O3TOT_L3_V03 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TEMPO_O3TOT_L3_V03 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2930764281-LARC_CLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tempo/TEMPO_O3TOT_Algorithm_description_V1.1.pdf",
-                    "description": "Algorithm Description for the TEMPO Total Ozone Retrieval Algorithm",
                     "@type": "dcat:Distribution",
+                    "description": "Algorithm Description for the TEMPO Total Ozone Retrieval Algorithm",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tempo/TEMPO_O3TOT_Algorithm_description_V1.1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tempo/guide/TEMPO_User_guide_O3TOT_V1.1.pdf",
-                    "description": "Tropospheric Emissions: Monitoring Pollution (TEMPO) Project Total Ozone Level 2 and 3 Data products: User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Tropospheric Emissions: Monitoring Pollution (TEMPO) Project Total Ozone Level 2 and 3 Data products: User Guide",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tempo/guide/TEMPO_User_guide_O3TOT_V1.1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "graphic-preview-description": "Mission Logo",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/tempo.png",
+            "identifier": "C2930764281-LARC_CLOUD",
+            "issued": "2024-04-03",
+            "keyword": [
+                "atmospheric chemistry",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/IS-40e/TEMPO/O3TOT_L3.003",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-02",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>10.0 -170.0 10.0 -10.0 80.0 -10.0 80.0 -170.0 10.0 -170.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2023-08-01T00:00:00Z/2025-01-06T00:00:00Z",
             "theme": [
                 "TEMPO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TEMPO gridded ozone total column V03 (PROVISIONAL)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amsl_chemcam_psv_calibrated&version=1.0",
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
-                "mars science laboratory"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "MSL ChemCam passive surface spectra bundle.",
+            "identifier": "urn:nasa:pds:msl_chemcam_psv_calibrated",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars science laboratory"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amsl_chemcam_psv_calibrated&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:msl_chemcam_psv_calibrated",
-            "description": "MSL ChemCam passive surface spectra bundle.",
-            "title": "MSL ChemCam Passive Surface Spectra Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MSL ChemCam Passive Surface Spectra Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4BG2KWB",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for International Earth Science Information Network - CIESIN. 1996-12-31. Archive of Census Related Products (ACRP): 1990 SAS Transport Files. Version 1.00. Saginaw, MI. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H4BG2KWB. https://doi.org/10.7927/H4BG2KWB.",
-            "issued": "1996-12-31",
-            "temporal": "1990-04-01T00:00:00Z/1990-04-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "1996-12-31",
-            "references": [
-                "https://doi.org/10.7927/H4Z60KZ9",
-                "https://doi.org/10.7927/H4G44N6R",
-                "https://doi.org/10.7927/H47P8W9V",
-                "https://doi.org/10.7927/H43X84KH",
-                "https://doi.org/10.7927/H4057CV3",
-                "https://doi.org/10.7927/H4QN64NG",
-                "https://doi.org/10.7927/H46Q1V51",
-                "https://doi.org/10.7927/H4TD9V7F",
-                "https://doi.org/10.7927/H42Z13FP"
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
-            "identifier": "C179001894-SEDAC",
-            "description": "The 1990 SAS Transport Files portion of the Archive of Census Related Products (ACRP) contains housing and population data from the U.S. Census Bureau's 1990 Summary tape File (STF3A) database. The data are available by state and county, county subdivision/mcd, blockgroup, and places, as well as Indian reservations, tribal districts and congressional districts. This portion of the ACRP is produced by the Columbia University Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "Saginaw, MI",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Center for International Earth Science Information Network - CIESIN",
-            "title": "Archive of Census Related Products (ACRP): 1990 SAS Transport Files",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/acrp/acrp-sas-transport-1990/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The 1990 SAS Transport Files portion of the Archive of Census Related Products (ACRP) contains housing and population data from the U.S. Census Bureau's 1990 Summary tape File (STF3A) database. The data are available by state and county, county subdivision/mcd, blockgroup, and places, as well as Indian reservations, tribal districts and congressional districts. This portion of the ACRP is produced by the Columbia University Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4BG2KWB",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4BG2KWB",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/acrp/acrp-sas-transport-1990/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/acrp/acrp-sas-transport-1990/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/acrp-sas-transport-1990/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/acrp-sas-transport-1990/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/acrp-sas-transport-1990",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/acrp-sas-transport-1990",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/acrp/acrp-sas-transport-1990/sedac-logo.jpg",
+            "identifier": "C179001894-SEDAC",
+            "issued": "1996-12-31",
+            "keyword": [
+                "population",
+                "earth science",
+                "human dimensions"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4BG2KWB",
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
+                "https://doi.org/10.7927/H47P8W9V",
+                "https://doi.org/10.7927/H43X84KH",
+                "https://doi.org/10.7927/H4057CV3",
+                "https://doi.org/10.7927/H4QN64NG",
+                "https://doi.org/10.7927/H46Q1V51",
+                "https://doi.org/10.7927/H4TD9V7F",
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
+            "title": "Archive of Census Related Products (ACRP): 1990 SAS Transport Files"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/KIGGFNVROX9V",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Global EASE-Grid 8-day Blended SSM/I and MODIS Snow Cover, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/KIGGFNVROX9V.",
-            "issued": "2000-03-05",
-            "temporal": "2000-03-05T00:00:00Z/2008-02-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2008-02-01",
-            "keyword": [
-                "national geospatial data asset",
-                "earth science",
-                "cryosphere",
-                "ngda",
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
-            "identifier": "C1386250333-NSIDCV0",
             "description": "This data set comprises global, 8-day Snow-Covered Area (SCA) and Snow Water Equivalent (SWE) data from 2000 through 2008. Global SWE data are derived from the Special Sensor Microwave Imager (SSM/I) and are enhanced with MODIS/Terra Snow Cover 8-Day Level 3 Global 0.05 degree Climate Modeling Grid (CMG) data. Global data are gridded to the Northern and Southern 25 km Equal-Area Scalable Earth Grids (EASE-Grids). These data are suitable for continental-scale time-series studies of snow cover and snow water equivalent.",
-            "title": "Global EASE-Grid 8-day Blended SSM/I and MODIS Snow Cover, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FKIGGFNVROX9V",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FKIGGFNVROX9V",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0321_blended_ssmi_modis/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0321_blended_ssmi_modis/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0321_blended_ssmi_modis/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0321_blended_ssmi_modis/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/KIGGFNVROX9V",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/KIGGFNVROX9V",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/KIGGFNVROX9V",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/KIGGFNVROX9V",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386250333-NSIDCV0",
+            "issued": "2000-03-05",
+            "keyword": [
+                "national geospatial data asset",
+                "earth science",
+                "cryosphere",
+                "ngda",
+                "snow/ice"
+            ],
+            "landingPage": "https://doi.org/10.5067/KIGGFNVROX9V",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2008-02-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 0.0 180.0 90.0",
+            "temporal": "2000-03-05T00:00:00Z/2008-02-01T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global EASE-Grid 8-day Blended SSM/I and MODIS Snow Cover, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-3-EXT1-MTP025-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This dataset contains ROSETTA NAVCAM RADIOMETRICALLY CALIBRATED DATA of the ROSETTA EXTENSION 1 MTP025 Phase from 13 Jan. 2016, 06:02:17 to 09 Feb. 2016, 23:17:55 when at the vicinity of target 67P/CG.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-3-ext1-mtp025-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "zeta cas",
@@ -365188,39 +365190,46 @@
                 "alpha lyr",
                 "67p/churyumov-gerasimenko 1 (1969 r1)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-3-EXT1-MTP025-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-3-ext1-mtp025-v1.0",
-            "description": "This dataset contains ROSETTA NAVCAM RADIOMETRICALLY CALIBRATED DATA of the ROSETTA EXTENSION 1 MTP025 Phase from 13 Jan. 2016, 06:02:17 to 09 Feb. 2016, 23:17:55 when at the vicinity of target 67P/CG.",
-            "title": "ROSETTA-ORBITER 67P NAVCAM 3 ROSETTA EXTENSION 1 MTP025 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P NAVCAM 3 ROSETTA EXTENSION 1 MTP025 V1.0"
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
+            "description": "APXS, DESCAM, HAZCAM, MB, MI, MTES, NAVCAM, tools",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/PDS-Subscription-Service-24-Aug-04.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-632",
+            "issued": "2018-06-25",
             "keyword": [
                 "mtes",
                 "navcam",
@@ -365232,126 +365241,119 @@
                 "apxs",
                 "mb"
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
-            "identifier": "NASA-632",
-            "description": "APXS, DESCAM, HAZCAM, MB, MI, MTES, NAVCAM, tools",
-            "title": "PDS Mars Exploration Rovers Data Release 2 (MER1)",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/PDS-Subscription-Service-24-Aug-04.shtml",
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
+            "title": "PDS Mars Exploration Rovers Data Release 2 (MER1)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MOD15A2PHN.006",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MODIS Land Science Team. 2021-04-01. MODIS/Terra LAI-FPAR Phenology annual L4 Global 1km SIN Grid. Version 6. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/MODIS/MOD15A2PHN.006. https://doi.org/10.5067/MODIS/MOD15A2PHN.006.",
-            "issued": "2018-10-05",
-            "temporal": "2001-01-01T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-10-21",
-            "keyword": [
-                "earth science",
-                "vegetation",
-                "ngda",
-                "national geospatial data asset",
-                "biosphere"
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
-            "identifier": "C2055712613-LAADS",
-            "description": "The MODIS/Terra LAI-FPAR Phenology annual L4 Global 1km SIN Grid product with short-name MOD15A2PHN, is estimated from MCD15A2 8-day products. The spatial resolution is 1-km. The MOD15PHN is stored in Hierarchical Data Format (HDF) in sinusodial projection, same as other standard MODIS land products. For the first 11 phenology parameters, only the first two seasons (marked as s1 and s2) are stored if there are more than one valid seasonal cycles detected. Valid seasonal cycles should begin within the year of interest and end before the end of the second year. There are 27 Science Data Sets (SDS) in the available phenology product.",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "MODIS Land Science Team",
-            "title": "MODIS/Terra LAI-FPAR Phenology annual L4 Global 1km SIN Grid",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MODIS/Terra LAI-FPAR Phenology annual L4 Global 1km SIN Grid product with short-name MOD15A2PHN, is estimated from MCD15A2 8-day products. The spatial resolution is 1-km. The MOD15PHN is stored in Hierarchical Data Format (HDF) in sinusodial projection, same as other standard MODIS land products. For the first 11 phenology parameters, only the first two seasons (marked as s1 and s2) are stored if there are more than one valid seasonal cycles detected. Valid seasonal cycles should begin within the year of interest and end before the end of the second year. There are 27 Science Data Sets (SDS) in the available phenology product.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD15A2PHN.006",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD15A2PHN.006",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/1/MOD15A2PHN--6",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/1/MOD15A2PHN--6",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/6/MOD15A2PHN/",
-                    "description": "Direct access to MOD15A2PHN data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to MOD15A2PHN data set.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/6/MOD15A2PHN/",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/6/MOD15A2PHN/contents.html",
-                    "description": "Direct link to Collection's OPeNDAP directory",
                     "@type": "dcat:Distribution",
+                    "description": "Direct link to Collection's OPeNDAP directory",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/6/MOD15A2PHN/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2055712613-LAADS",
+            "issued": "2018-10-05",
+            "keyword": [
+                "earth science",
+                "vegetation",
+                "ngda",
+                "national geospatial data asset",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MOD15A2PHN.006",
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
+            "title": "MODIS/Terra LAI-FPAR Phenology annual L4 Global 1km SIN Grid"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-SPI-2-IREDR-RAWXMARS-EXT6-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The Mars Express SPICAM level 0B IR data set contains raw measurements from the infrared SPICAM spectrometer collected during the extension 6 MARS phases",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-spi-2-iredr-rawxmars-ext6-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "sun",
                 "deimos",
@@ -365363,139 +365365,113 @@
                 "star",
                 "mars express"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-SPI-2-IREDR-RAWXMARS-EXT6-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-spi-2-iredr-rawxmars-ext6-v1.0",
-            "description": "The Mars Express SPICAM level 0B IR data set contains raw measurements from the infrared SPICAM spectrometer collected during the extension 6 MARS phases",
-            "title": "MEX EXT 6 SPICAM MARS IR EDR-RAW V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MEX EXT 6 SPICAM MARS IR EDR-RAW V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amgs_tes_recalib_atmos&version=1.0",
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
+            "identifier": "urn:nasa:pds:mgs_tes_recalib_atmos",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "mars global surveyor (mgs)",
                 "mars",
                 "mars atmosphere spectroscopy"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amgs_tes_recalib_atmos&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:mgs_tes_recalib_atmos",
-            "description": "________",
-            "title": "Mars Global Surveyor Thermal Emission Spectrometer Atmospheric Recalibration Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Mars Global Surveyor Thermal Emission Spectrometer Atmospheric Recalibration Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCIES-2-EXT3-V1.0",
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
+            "description": "This dataset contains EDITED RAW DATA of the Rosetta RPCIES instrument taken during the extended mission 3 phase (EXT3). The target of this phase was comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). Included are the data taken between 01 Jul 2016 and 30 Sep 2016.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcies-2-ext3-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCIES-2-EXT3-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcies-2-ext3-v1.0",
-            "description": "This dataset contains EDITED RAW DATA of the Rosetta RPCIES instrument taken during the extended mission 3 phase (EXT3). The target of this phase was comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). Included are the data taken between 01 Jul 2016 and 30 Sep 2016.",
-            "title": "ROSETTA-ORBITER 67P RPCIES 2 EXT3 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCIES 2 EXT3 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1332654182-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Tropical Rainfall Measuring Mission (TRMM). 2007-01-01. TRMM_3A54. TRMM Ground Validation Radar Site Rain Type Totals Map L3 1 month 2 km V7. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/TRMM_3A54_7.html.",
-            "issued": "2011-07-01",
-            "temporal": "1997-11-01T00:00:00Z/2015-01-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-05-09",
-            "keyword": [
-                "radar",
-                "precipitation",
-                "earth science",
-                "atmosphere",
-                "spectral/engineering"
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
-            "identifier": "C1332654182-GES_DISC",
-            "description": "The 3A54 product, 'Site Rainfall Map', is a map of monthly surface rain totals derived from the instantaneous rain rate maps (2A53). The map is in Cartesian coordinates with a 2 km horizontal resolution and covers an area of 300km x 300km at single radar sites while the covered area varies for multiple radar sites - 724 km x 568 km at Texas site and 512 km x 704 km at Florida site. This monthly rainfall map is not a simple accumulation of the instantaneous maps as gaps in the data must be factored into the calculation. \n\nA key component of the TRMM project is the Ground Validation (GV) effort which consists of collecting data from ground-based radar, rain gauges and disdrometers. The data is quality-controlled, and then validation products are produced for comparison with TRMM satellite products.\n\nThe four primary GV sites are:\n\n+ Darwin, Australia; \n+ Houston, Texas; \n+ Kwajalein, Republic of the Marshall Islands;\n+ Melbourne, Florida. \n\nA significant effort is also being supported at NASA Wallops Flight Facility (WFF) and vicinity to provide high quality, long-term measurements of rain rates (via a network of rain gauges collocated with National Weather Service gauges), as well as drop size distributions (DSD) using a variety of instruments, including impact-type Joss Waldvogel, laser-optical Parsivel, as well as two-dimensional video disdrometers.  DSD measurements are also being collected at Melbourne and Kwajalein using Joss-Waldvogel disdrometers.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "TRMM_3A54",
             "creator": "Tropical Rainfall Measuring Mission (TRMM)",
-            "title": "TRMM Ground Validation Radar Site Rain Type Totals Map L3 1 month 2 km V7 (TRMM_3A54) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/3A54_BR.111201.KWAJ.7.PNG",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The 3A54 product, 'Site Rainfall Map', is a map of monthly surface rain totals derived from the instantaneous rain rate maps (2A53). The map is in Cartesian coordinates with a 2 km horizontal resolution and covers an area of 300km x 300km at single radar sites while the covered area varies for multiple radar sites - 724 km x 568 km at Texas site and 512 km x 704 km at Florida site. This monthly rainfall map is not a simple accumulation of the instantaneous maps as gaps in the data must be factored into the calculation. \n\nA key component of the TRMM project is the Ground Validation (GV) effort which consists of collecting data from ground-based radar, rain gauges and disdrometers. The data is quality-controlled, and then validation products are produced for comparison with TRMM satellite products.\n\nThe four primary GV sites are:\n\n+ Darwin, Australia; \n+ Houston, Texas; \n+ Kwajalein, Republic of the Marshall Islands;\n+ Melbourne, Florida. \n\nA significant effort is also being supported at NASA Wallops Flight Facility (WFF) and vicinity to provide high quality, long-term measurements of rain rates (via a network of rain gauges collocated with National Weather Service gauges), as well as drop size distributions (DSD) using a variety of instruments, including impact-type Joss Waldvogel, laser-optical Parsivel, as well as two-dimensional video disdrometers.  DSD measurements are also being collected at Melbourne and Kwajalein using Joss-Waldvogel disdrometers.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -365504,76 +365480,102 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRMM_3A54_7.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRMM_3A54_7.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_GV_L3/TRMM_3A54.7",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_GV_L3/TRMM_3A54.7",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRMM_3A54",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRMM_3A54",
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
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://pps.gsfc.nasa.gov/Documents/ICSVol4.pdf",
-                    "description": "File specification document",
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
-                    "downloadURL": "https://gpmweb2https.pps.eosdis.nasa.gov/tsdis/AB/docs/anomalous.html",
-                    "description": "TRMM Data Gaps",
                     "@type": "dcat:Distribution",
+                    "description": "TRMM Data Gaps",
+                    "downloadURL": "https://gpmweb2https.pps.eosdis.nasa.gov/tsdis/AB/docs/anomalous.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/3A54_BR.111201.KWAJ.7.PNG",
+            "identifier": "C1332654182-GES_DISC",
+            "issued": "2011-07-01",
+            "keyword": [
+                "radar",
+                "precipitation",
+                "earth science",
+                "atmosphere",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1332654182-GES_DISC.html",
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
+            "series-name": "TRMM_3A54",
             "spatial": "-180.0 -40.0 180.0 40.0",
+            "temporal": "1997-11-01T00:00:00Z/2015-01-01T23:59:59.999Z",
             "theme": [
                 "TRMM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TRMM Ground Validation Radar Site Rain Type Totals Map L3 1 month 2 km V7 (TRMM_3A54) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0046-3-FBIRTFSPEC-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The data set contains observations obtained with the NASA IRTF SpeX instrument covering the 0.7 to 2.5 micron near-infrared portion of the spectrum. The data set archives reduced, calibrated spectra which were obtained and used in Sherry Fieber-Beyer's Ph.D. dissertation at the University of North Dakota. The research focused on asteroids in a zone centered on the 3:1 resonance. These spectra were used to mineralogically characterize asteroids in this zone in an attempt to identify their meteorite analogs.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0046-3-fbirtfspec-v1.0_8i9e-4fid",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "3760 poutanen",
                 "495 eulalia",
@@ -365604,732 +365606,732 @@
                 "619 triberga",
                 "556 phyllis"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0046-3-FBIRTFSPEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0046-3-fbirtfspec-v1.0_8i9e-4fid",
-            "description": "The data set contains observations obtained with the NASA IRTF SpeX instrument covering the 0.7 to 2.5 micron near-infrared portion of the spectrum. The data set archives reduced, calibrated spectra which were obtained and used in Sherry Fieber-Beyer's Ph.D. dissertation at the University of North Dakota. The research focused on asteroids in a zone centered on the 3:1 resonance. These spectra were used to mineralogically characterize asteroids in this zone in an attempt to identify their meteorite analogs.",
-            "title": "FIEBER-BEYER IRTF MAINBELT ASTEROID SPECTRA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "FIEBER-BEYER IRTF MAINBELT ASTEROID SPECTRA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FCAL-ALICE-2-PRL-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains CODMAC Level 2 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the comet 67P/Churyumov-Gerasimenko Prelanding mission phase, which took place between 2014-01-21 and 2014-11-19.  The current V2.0 data set supersedes the previous V1.0 data set.  Pixel list data files have had corrections applied to their FITS formatting.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cal-alice-2-prl-v2.0",
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
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FCAL-ALICE-2-PRL-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cal-alice-2-prl-v2.0",
-            "description": "This data set contains CODMAC Level 2 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the comet 67P/Churyumov-Gerasimenko Prelanding mission phase, which took place between 2014-01-21 and 2014-11-19.  The current V2.0 data set supersedes the previous V1.0 data set.  Pixel list data files have had corrections applied to their FITS formatting.",
-            "title": "ROSETTA-ORBITER 67P/CAL ALICE 2 PRL V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P/CAL ALICE 2 PRL V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VJ103DNB.021",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "VCST Team. 2021-07-21. VIIRS/JPSS1 Day/Night Band Resolution Terrain Corrected Geolocation 6-Min L1 Swath 750 m. Version 2.1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/VIIRS/VJ103DNB.021. https://doi.org/10.5067/VIIRS/VJ103DNB.021.",
-            "issued": "2021-01-21",
-            "temporal": "2017-12-13T00:00:00Z/2024-06-10T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-05",
-            "keyword": [
-                "spectral/engineering",
-                "infrared wavelengths",
-                "sensor characteristics",
-                "earth science",
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
-            "identifier": "C2105087273-LAADS",
-            "description": "The VIIRS/JPSS1 Day/Night Band Resolution Terrain Corrected Geolocation 6-Min L1 Swath 750m product contains the derived line-of-sight (LOS) vectors for the single panchromatic Day-Night band (DNB).  The geolocation algorithm uses a number of inputs that include an Earth ellipsoid, geoid, and a digital terrain model along with the SNPP platform\u2019s ephemeris and attitude data, and knowledge of the VIIRS sensor and satellite geometry.  It provides geodetic coordinates (latitude and longitude), and related parameters for each VIIRS L1 pixel.  The VJ103DNB product includes geodetic latitude, longitude, surface height above the geoid, solar zenith and azimuth angles, lunar zenith and azimuth angles, sensor zenith and azimuth angles, land/water mask, moon illumination fraction and phase angle, and quality flag for every pixel location.",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "VCST Team",
-            "title": "VIIRS/JPSS1 Day/Night Band Resolution Terrain Corrected Geolocation L1 6-Min Swath 750 m",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The VIIRS/JPSS1 Day/Night Band Resolution Terrain Corrected Geolocation 6-Min L1 Swath 750m product contains the derived line-of-sight (LOS) vectors for the single panchromatic Day-Night band (DNB).  The geolocation algorithm uses a number of inputs that include an Earth ellipsoid, geoid, and a digital terrain model along with the SNPP platform\u2019s ephemeris and attitude data, and knowledge of the VIIRS sensor and satellite geometry.  It provides geodetic coordinates (latitude and longitude), and related parameters for each VIIRS L1 pixel.  The VJ103DNB product includes geodetic latitude, longitude, surface height above the geoid, solar zenith and azimuth angles, lunar zenith and azimuth angles, sensor zenith and azimuth angles, land/water mask, moon illumination fraction and phase angle, and quality flag for every pixel location.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ103DNB.021",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ103DNB.021",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VJ103DNB.021",
-                    "description": "The product landing page",
                     "@type": "dcat:Distribution",
+                    "description": "The product landing page",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VJ103DNB.021",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/VJ103DNB--5201",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/VJ103DNB--5201",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/5201/VJ103DNB/",
-                    "description": "Direct access to VJ103DNB C2.1 data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to VJ103DNB C2.1 data set.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/5201/VJ103DNB/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/5201/VJ103DNB/contents.html",
-                    "description": "Direct access to product's OPeNDAP directory",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to product's OPeNDAP directory",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/5201/VJ103DNB/contents.html",
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
+            "identifier": "C2105087273-LAADS",
+            "issued": "2021-01-21",
+            "keyword": [
+                "spectral/engineering",
+                "infrared wavelengths",
+                "sensor characteristics",
+                "earth science",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VJ103DNB.021",
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
+            "temporal": "2017-12-13T00:00:00Z/2024-06-10T00:00:00Z",
             "theme": [
                 "JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/JPSS1 Day/Night Band Resolution Terrain Corrected Geolocation L1 6-Min Swath 750 m"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-XGRS-2-EDR-CRUISE4-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-xgrs-2-edr-cruise4-v1.0_8i9q-hzcj",
+            "issued": "2018-06-26",
+            "keyword": [
+                "near earth asteroid rendezvous",
+                "solar system"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-XGRS-2-EDR-CRUISE4-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-xgrs-2-edr-cruise4-v1.0_8i9q-hzcj",
-            "description": "NEAR EDR volume sets contain a single data set, from one instrument and one mission phase (defined in the phase table in /AAREADME.TXT).",
-            "title": "NEAR XGRS SPECTRA FOR CRUISE4",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEAR XGRS SPECTRA FOR CRUISE4"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7265/2z30-1j49",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The Northern Bering Sea: Our Way of Life, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center. https://doi.org/10.7265/2z30-1j49.",
-            "issued": "2011-01-01",
-            "temporal": "2011-01-01T00:00:00Z/2011-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2011-12-31",
-            "keyword": [
-                "wildlife observations",
-                "animals/vertebrates",
-                "biological classification",
-                "coastal processes",
-                "sea ice",
-                "public health",
-                "oceans",
-                "marine environment monitoring",
-                "indigenous knowledge",
-                "human dimensions",
-                "environmental features & use",
-                "earth science",
-                "cryosphere",
-                "community-based monitoring"
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
-            "identifier": "C1728290886-NSIDCV0",
             "description": "The purpose of \"The Northern Bering Sea: Our Way of Life\" is to show extensive areas where Alaska Native hunters and local fishermen harvest ocean resources, and the marine waters important to the resources we rely on. It illustrates that the whole northern Bering Sea is the storehouse that supports our way of life.",
-            "title": "The Northern Bering Sea: Our Way of Life, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2F2z30-1j49",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2F2z30-1j49",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://eloka-arctic.org/communities/elders.html",
-                    "description": "Product website where you can access the data.",
                     "@type": "dcat:Distribution",
+                    "description": "Product website where you can access the data.",
+                    "downloadURL": "https://eloka-arctic.org/communities/elders.html",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/2z30-1j49",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/2z30-1j49",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/2z30-1j49",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/2z30-1j49",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
-            "theme": [
-                "geospatial"
+            "identifier": "C1728290886-NSIDCV0",
+            "issued": "2011-01-01",
+            "keyword": [
+                "wildlife observations",
+                "animals/vertebrates",
+                "biological classification",
+                "coastal processes",
+                "sea ice",
+                "public health",
+                "oceans",
+                "marine environment monitoring",
+                "indigenous knowledge",
+                "human dimensions",
+                "environmental features & use",
+                "earth science",
+                "cryosphere",
+                "community-based monitoring"
             ],
+            "landingPage": "https://doi.org/10.7265/2z30-1j49",
             "language": [
                 "en-US"
-            ]
+            ],
+            "modified": "2011-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
+            "temporal": "2011-01-01T00:00:00Z/2011-12-31T23:59:59.999Z",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "The Northern Bering Sea: Our Way of Life, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/463",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Osborne, H., K. Young, V. Wittrock, and S.R. Shewchuk. 1998. BOREAS/SRC AMS Suite A Surface Meteorological and Radiation Data: 1995. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/463",
-            "issued": "2023-11-22",
-            "temporal": "1995-01-01T00:00:00Z/1995-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-11",
-            "keyword": [
-                "terrestrial hydrosphere",
-                "atmosphere",
-                "atmospheric winds",
-                "precipitation",
-                "soils",
-                "surface thermal properties",
-                "atmospheric water vapor",
-                "atmospheric radiation",
-                "snow/ice",
-                "atmospheric pressure",
-                "land surface",
-                "vegetation",
-                "atmospheric temperature",
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
-            "identifier": "C2929131838-ORNL_CLOUD",
             "description": "Contains the data collected in 1995 by the AMS suite A instrument set operated by SRC and provided to BORIS.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS/SRC AMS Suite A Surface Meteorological and Radiation Data: 1995",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F463",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F463",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/AFM/samsa95d/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/AFM/samsa95d/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/AFM07_SRC_AMS.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/AFM07_SRC_AMS.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/463",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/463",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/samsa95d/comp/AFM07_CS_Progs.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/samsa95d/comp/AFM07_CS_Progs.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/samsa95d/comp/AFM07_CS_Progs.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/samsa95d/comp/AFM07_CS_Progs.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/samsa95d/comp/AFM07_SoilMoist.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/samsa95d/comp/AFM07_SoilMoist.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/samsa95d/comp/AFM07_SoilMoist.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/samsa95d/comp/AFM07_SoilMoist.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/samsa95d/comp/AFM07_SRC_AMS.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/samsa95d/comp/AFM07_SRC_AMS.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/samsa95d/comp/AFM07_SRC_AMS.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/samsa95d/comp/AFM07_SRC_AMS.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/samsa95d/comp/AFM07_SRC_AMS.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/samsa95d/comp/AFM07_SRC_AMS.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/samsa95d/comp/samsa95d.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/samsa95d/comp/samsa95d.def",
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
+            "identifier": "C2929131838-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "terrestrial hydrosphere",
+                "atmosphere",
+                "atmospheric winds",
+                "precipitation",
+                "soils",
+                "surface thermal properties",
+                "atmospheric water vapor",
+                "atmospheric radiation",
+                "snow/ice",
+                "atmospheric pressure",
+                "land surface",
+                "vegetation",
+                "atmospheric temperature",
+                "earth science",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/463",
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
             "spatial": "-108.51 52.15 -97.87 56.89",
+            "temporal": "1995-01-01T00:00:00Z/1995-12-31T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS/SRC AMS Suite A Surface Meteorological and Radiation Data: 1995"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1237207595-LARC_ASDC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2016-04-25. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC.",
-            "issued": "2015-08-08",
-            "temporal": "2006-06-21T00:00:00Z/2011-12-06T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-06-29",
-            "keyword": [
-                "atmosphere",
-                "clouds",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Data Manager",
                 "hasEmail": "mailto:larc@eos.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1237207595-LARC_ASDC",
             "description": "CER_GEO_Ed4_GOE11_SH_V01 is the Satellite Cloud and Radiation Property retrieval System (SatCORPS) Clouds and the Earth's Radiant Energy System (CERES) Geostationary Satellite (GEO) Edition 4 Geostationary Operational Environmental Satellite 11 (GOES-11) over the Southern Hemisphere (SH) Version 1.0 data product. Data was collected using the GOES-11 Imager on the GOES-11 Platform. Data collection for this product is complete.\r\n\r\nThis data set comprises cloud micro-physical and radiation properties derived hourly from GOES-11 geostationary satellite imager data using the Langley Research Center (LARC) SATCORPS algorithms supporting the CERES project. The cloud micro-physical and radiation properties from each active geostationary satellite are merged to create hourly global cloud properties that estimate fluxes between CERES instrument measurements to account for the changing diurnal cycle. The data set is arranged as files for each hour and in netCDF-4 format. The observations are at 4 km resolution (at nadir) and are sub-sampled to 8 km.\r\n\r\nCERES is a key Earth Observing System (EOS) program component. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions follow the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument, the protoflight model (PFM), was launched on November 27, 1997, as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the Earth Observing System (EOS) flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board Earth Observing System (EOS) Aqua on May 4, 2002. The CERES FM5 instrument was launched on board the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The newest CERES instrument (FM6) was launched on board the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite, now called NOAA-20, on November 18, 2017.",
-            "graphic-preview-description": "Mission Logo",
-            "title": "SatCORPS CERES GEO Edition 4 GOES-11 Southern Hemisphere Version 1.0",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1237207595-LARC_ASDC",
-                    "description": "Earthdata Search for CER_GEO_Ed4_GOE11_SH_V01 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CER_GEO_Ed4_GOE11_SH_V01 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1237207595-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
-                    "description": "ASDC's data citation policy",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC's data citation policy",
+                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/GEO/Edition4/GOE11_SH_V01/",
-                    "description": "ASDC Direct Data Download for CER_GEO_Ed4_GOE11_SH_V01",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CER_GEO_Ed4_GOE11_SH_V01",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/GEO/Edition4/GOE11_SH_V01/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/GEO/Edition4/GOE11_SH_V01/contents.html",
-                    "description": "OPeNDAP data access for CER_GEO_Ed4_GOE11_SH_V01",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CER_GEO_Ed4_GOE11_SH_V01",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/GEO/Edition4/GOE11_SH_V01/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Mission Logo",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/ceres.png",
+            "identifier": "C1237207595-LARC_ASDC",
+            "issued": "2015-08-08",
+            "keyword": [
+                "atmosphere",
+                "clouds",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1237207595-LARC_ASDC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-06-29",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-60.0 -180.0 -60.0 -91.0 0.0 -91.0 0.0 -180.0 -60.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2006-06-21T00:00:00Z/2011-12-06T23:59:59.999Z",
             "theme": [
                 "CERES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SatCORPS CERES GEO Edition 4 GOES-11 Southern Hemisphere Version 1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1310",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Reimer, J.J., R. Vargas, D. Rivas, G. Gaxiola-Castro, J.M. Hernandez-Ayon, and R. Lara-Lara. 2016. CMS: MODIS GPP, fPAR, and SST, and ENSO Index, Baja California, Mexico, 2000-2013. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1310",
-            "issued": "2016-03-21",
-            "temporal": "2000-01-01T00:00:00Z/2013-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "biosphere",
-                "earth science",
-                "oceans",
-                "ocean temperature",
-                "ngda",
-                "vegetation",
-                "national geospatial data asset",
-                "climate indicators",
-                "atmospheric/ocean indicators"
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
-            "identifier": "C2343141032-ORNL_CLOUD",
             "description": "This data set provides data for MODIS-derived (1) gross primary productivity (GPP) for the years 2000-2010, (2) fraction of photosynthetically active radiation (fPAR) for the years 2003-2013, (3) sea surface temperature (SST) for the years 2003-2013, and (4) the NOAA-source Multivariate ENSO Index (MEI) data for the years 2003-2013 (as a measure of the El Nino/Southern Oscillation). The study areas were three transects on the Baja California Peninsula, Mexico, and the adjacent Pacific Ocean. The terrestrial transects, in order from North to South, West to East included Punta Colonet (three sites-PC1, PC2, PC3), Punta Abreojos (two sites-PA1, PA2), and Magdalena Bay (three sites-MB1, MB2, MB3).",
-            "graphic-preview-description": "Browse Image",
-            "title": "CMS: MODIS GPP, fPAR, and SST, and ENSO Index, Baja California, Mexico, 2000-2013",
-            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/CMS_SST_GPP_Mexico_fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1310",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1310",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/cms/CMS_SST_GPP_Mexico/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/cms/CMS_SST_GPP_Mexico/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_SST_GPP_Mexico.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_SST_GPP_Mexico.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1310",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1310",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/CMS_SST_GPP_Mexico/comp/CMS_SST_GPP_Mexico.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/CMS_SST_GPP_Mexico/comp/CMS_SST_GPP_Mexico.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_SST_GPP_Mexico_fig1.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_SST_GPP_Mexico_fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/CMS_SST_GPP_Mexico_fig1.png",
+            "identifier": "C2343141032-ORNL_CLOUD",
+            "issued": "2016-03-21",
+            "keyword": [
+                "biosphere",
+                "earth science",
+                "oceans",
+                "ocean temperature",
+                "ngda",
+                "vegetation",
+                "national geospatial data asset",
+                "climate indicators",
+                "atmospheric/ocean indicators"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1310",
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
             "spatial": "-117.0 22.77 -108.0 32.64",
+            "temporal": "2000-01-01T00:00:00Z/2013-12-31T23:59:59Z",
             "theme": [
                 "CMS",
                 "NACP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CMS: MODIS GPP, fPAR, and SST, and ENSO Index, Baja California, Mexico, 2000-2013"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=HST-S-WFPC2-3-RPX-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images of the Saturn system taken by the Wide Field/Planetary Camera 2 (WFPC2) aboard the Hubble Space Telescope (HST) through November 1995. This period includes all images taken during the Saturn ring plane crossings of 1995. (No WFPC2 images of Saturn were obtained during the last ring plane crossing in February 1996 because Saturn was too close to the Sun.)",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.hst-s-wfpc2-3-rpx-v1.0_8ie5-w6bg",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "iapetus",
                 "saturn",
@@ -366354,71 +366356,44 @@
                 "hst",
                 "hyperion"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=HST-S-WFPC2-3-RPX-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.hst-s-wfpc2-3-rpx-v1.0_8ie5-w6bg",
-            "description": "This data set contains images of the Saturn system taken by the Wide Field/Planetary Camera 2 (WFPC2) aboard the Hubble Space Telescope (HST) through November 1995. This period includes all images taken during the Saturn ring plane crossings of 1995. (No WFPC2 images of Saturn were obtained during the last ring plane crossing in February 1996 because Saturn was too close to the Sun.)",
-            "title": "HST SATURN WFPC2 3 RING PLANE CROSSING V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "HST SATURN WFPC2 3 RING PLANE CROSSING V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/MEASURES/GOZCARDS/DATA3023",
             "citation": "M. J. Schwartz, L. Froidevaux, R. A. Fuller, and S. Pawson. 2013-05-02. GozSmlpT. Version 1. GOZCARDS Source Temperature 1 month L4 10 degree Zonal Averages on a Vertical Pressure Grid V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/MEASURES/GOZCARDS/DATA3023. https://disc.gsfc.nasa.gov/datacollection/GozSmlpT_1.html. Digital Science Data.",
-            "issued": "2013-05-02",
-            "temporal": "1979-01-01T00:00:00Z/2012-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2013-05-02",
-            "references": [
-                "https://doi.org/10.5194/acp-15-10471-201"
-            ],
-            "keyword": [
-                "atmosphere",
-                "atmospheric temperature",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "LUCIEN FROIDEVAUX",
                 "hasEmail": "mailto:lucien.froidevaux@jpl.nasa.gov"
             },
+            "creator": "M. J. Schwartz, L. Froidevaux, R. A. Fuller, and S. Pawson",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1251051362-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The GOZCARDS Source Data for Temperature 1 month L4 10 degree Zonal Averages on a Vertical Pressure Grid product (GozSmlpT) contains zonal means and related information (standard deviation, minimum/maximum value, etc.), calculated from the original products. The source Temperature data are from the GMAO MERRA model product DAS 3d analyzed state MAI6NVANA (v5.2.0; 1979 - onward). The vertical pressure range for Temperature is from 1000 to 0.015 hPa.\n\nThe GozSmlpT source data are distributed in netCDF4 format.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "GozSmlpT",
-            "creator": "M. J. Schwartz, L. Froidevaux, R. A. Fuller, and S. Pawson",
-            "title": "GOZCARDS Source Temperature 1 month L4 10 degree Zonal Averages on a Vertical Pressure Grid V1 (GozSmlpT) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GozSmlpT_1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FGOZCARDS%2FDATA3023",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FGOZCARDS%2FDATA3023",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -366428,392 +366403,419 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GozSmlpT_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GozSmlpT_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/GOZCARDS/GozSmlpT.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/GOZCARDS/GozSmlpT.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/GOZCARDS/GozSmlpT.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/GOZCARDS/GozSmlpT.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/GOZCARDS/GozSmlpT.1/catalog.html",
-                    "description": "Access the data using the THREDDS Catalog.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data using the THREDDS Catalog.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/GOZCARDS/GozSmlpT.1/catalog.html",
+                    "mediaType": "text/html",
                     "title": "Use THREDDS DATA to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gozcards.jpl.nasa.gov/",
-                    "description": "The project web site at JPL.",
                     "@type": "dcat:Distribution",
+                    "description": "The project web site at JPL.",
+                    "downloadURL": "https://gozcards.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/GOZCARDS/README-GOZCARDS-v1.1.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/GOZCARDS/README-GOZCARDS-v1.1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GozSmlpT_1.png",
+            "identifier": "C1251051362-GES_DISC",
+            "issued": "2013-05-02",
+            "keyword": [
+                "atmosphere",
+                "atmospheric temperature",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/GOZCARDS/DATA3023",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2013-05-02",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.5194/acp-15-10471-201"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "GozSmlpT",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1979-01-01T00:00:00Z/2012-12-31T23:59:59.999Z",
             "theme": [
                 "MEaSUREs",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GOZCARDS Source Temperature 1 month L4 10 degree Zonal Averages on a Vertical Pressure Grid V1 (GozSmlpT) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-CAL-CONSERT-4-EAR3-V1.0",
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
+            "description": "This archive contains REFORMATTED data (CODMAC level 4) that refers to target CALIBRATION from the CONSERT instrument onboard ROSETTA Orbiter and Lander, acquired during the EAR3 phase. In addition to the scientific signal of interest, it contains all the values applied to the signal for calibration. It also contains documentation which describes the CONSERT experiment. The L4 dataset includes interpolated signals using a specific CONSERT method. It also provide fine propagation travel times of the signal between Philae and Rosetta. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-cal-consert-4-ear3-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "calibration"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-CAL-CONSERT-4-EAR3-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-cal-consert-4-ear3-v1.0",
-            "description": "This archive contains REFORMATTED data (CODMAC level 4) that refers to target CALIBRATION from the CONSERT instrument onboard ROSETTA Orbiter and Lander, acquired during the EAR3 phase. In addition to the scientific signal of interest, it contains all the values applied to the signal for calibration. It also contains documentation which describes the CONSERT experiment. The L4 dataset includes interpolated signals using a specific CONSERT method. It also provide fine propagation travel times of the signal between Philae and Rosetta. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-ORBITER/ROSETTA-LANDER CAL CONSERT 4 EAR3 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER/ROSETTA-LANDER CAL CONSERT 4 EAR3 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Terra/MISR_Volcano_Research/ICEVOLC_FLOWERKAHN2020_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/Terra/MISR_Volcano_Research/ICEVOLC_FLOWERKAHN2020_1. https://asdc.larc.nasa.gov/project/MISR_Volcano_Research.",
-            "issued": "2020-08-06",
-            "temporal": "2010-04-15T00:00:00Z/2015-02-21T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-08-06",
-            "keyword": [
-                "atmosphere",
-                "tectonics",
-                "solid earth",
-                "geomorphic landforms/processes",
-                "earth science",
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
-            "identifier": "C1935878448-LARC_ASDC",
             "description": "This dataset comprises MISR-derived output from a comprehensive analysis of Icelandic volcano eruptions (Eyjafjallajokull 2010, Grimsvotn 2011, Holuhraun 2014-2015). The data presented here are analyzed and discussed in the following paper: Flower, V.J.B., and R.A. Kahn, 2020. The evolution of Icelandic volcano emissions, as observed from space in the era of NASA\u2019s Earth Observing System (EOS). J. Geophys. Res. Atmosph. (in press).\nThe data is subdivided by volcano of origin, date and MISR orbit number. Within each case folder there are up to 11 files relating to an individual MISR overpass. Files include plume height records (from both the red and blue spectral bands) derived from the MISR INteractive eXplorer (MINX) program, displayed in: map view, downwind profile plot (along with the associated wind vectors retrieved at plume elevation), a histogram of retrieved plume heights and a text file containing the digital plume height values. An additional JPG is included delineating the plume analysis region, start point for assessing downwind distance, and input wind direction used to initialize the MINX retrieval. A final two files are generated from the MISR Research Aerosol (RA) retrieval algorithm (Limbacher, J.A., and R.A. Kahn, 2014. MISR Research-Aerosol-Algorithm: Refinements For Dark Water Retrievals. Atm. Meas. Tech. 7, 1-19, doi:10.5194/amt-7-1-2014). These files include the RA model output in HDF5, and an associated JPG of key derived variables (e.g. Aerosol Optical Depth, Angstrom Exponent, Single Scattering Albedo, Fraction of Non-Spherical components, model uncertainty classifications and example camera views). \nFile numbers per folder vary depending on the retrieval conditions of specific observations. RA plume retrievals are limited when cloud cover was widespread or the solar radiance was insufficient to run the RA. In these cases the RA files are not included in the individual folders.",
-            "graphic-preview-description": "The MISR INteractive eXplorer (MINX) program, for determining the altitude of aerosol plumes and associated wind vectors using the MISR Level 1B2 multi-angle multi-spectral radiance imaging products.",
-            "title": "MISR Derived Case Study Data for Iceland Volcanic Eruptions (Eyjafjallajokull, Grimsvotn, Holuhraun) Including Geometric Plume Height and Qualitative Radiometric Particle Property Information",
-            "graphic-preview-file": "https://github.com/nasa/MINX/releases",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR_Volcano_Research%2FICEVOLC_FLOWERKAHN2020_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR_Volcano_Research%2FICEVOLC_FLOWERKAHN2020_1",
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
-                    "description": "The MISR INteractive eXplorer (MINX) program, for determining the altitude of aerosol plumes and associated wind vectors using the MISR Level 1B2 multi-angle multi-spectral radiance imaging products.",
                     "@type": "dcat:Distribution",
+                    "description": "The MISR INteractive eXplorer (MINX) program, for determining the altitude of aerosol plumes and associated wind vectors using the MISR Level 1B2 multi-angle multi-spectral radiance imaging products.",
+                    "downloadURL": "https://github.com/nasa/MINX/releases",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/Terra/MISR_Volcano_Research/ICEVOLC_FLOWERKAHN2020_1",
-                    "description": "DOI data set landing page for ICEVOLC_FlowerKahn2020_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for ICEVOLC_FlowerKahn2020_1",
+                    "downloadURL": "https://doi.org/10.5067/Terra/MISR_Volcano_Research/ICEVOLC_FLOWERKAHN2020_1",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1935878448-LARC_ASDC",
-                    "description": "Earthdata Search for ICEVOLC_FlowerKahn2020_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for ICEVOLC_FlowerKahn2020_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1935878448-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/MISR/Volcano_Research/ICEVOLC_FlowerKahn2020_1/",
-                    "description": "ASDC Direct Data Download for ICEVOLC_FlowerKahn2020_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for ICEVOLC_FlowerKahn2020_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/MISR/Volcano_Research/ICEVOLC_FlowerKahn2020_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "graphic-preview-description": "The MISR INteractive eXplorer (MINX) program, for determining the altitude of aerosol plumes and associated wind vectors using the MISR Level 1B2 multi-angle multi-spectral radiance imaging products.",
+            "graphic-preview-file": "https://github.com/nasa/MINX/releases",
+            "identifier": "C1935878448-LARC_ASDC",
+            "issued": "2020-08-06",
+            "keyword": [
+                "atmosphere",
+                "tectonics",
+                "solid earth",
+                "geomorphic landforms/processes",
+                "earth science",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.5067/Terra/MISR_Volcano_Research/ICEVOLC_FLOWERKAHN2020_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-08-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-30.0 50.0 5.0 70.0",
+            "temporal": "2010-04-15T00:00:00Z/2015-02-21T23:59:59Z",
             "theme": [
                 "MISR_Volcano_Research",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR Derived Case Study Data for Iceland Volcanic Eruptions (Eyjafjallajokull, Grimsvotn, Holuhraun) Including Geometric Plume Height and Qualitative Radiometric Particle Property Information"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-ER-3-PREMAP%2FOMNIDIR-FLUX-V1.0",
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
+            "description": "The Electron Reflectometer Data Record (ERDR) is a time ordered series of electron measurements from the Mars Global Surveyor (MGS) Mission. Each record consists of a time tag with 19 scalar data points representing measurements of the electron flux in 19 different energy channels, ranging from 10 eV to 20 keV, with an energy resolution of 25%. Each data point is a measure of the electron flux (cm-2 sec-1 ster-1 eV-1) averaged over a 360 x 14 degree disk-shaped field of view (FOV). (Parts of this FOV are masked because of spacecraft obstructions, as described below.) During the Science Phasing Orbits (SPO), the spacecraft was in Array Normal Spin (ANS) configuration, for which the ER field of view sweeps out the entire sky (4-pi ster) every 50 minutes, which is much longer than the integration time per record (2 to 48 sec, depending on energy and telemetry rate) and much longer than most timescales of interest in Mars' plasma environment.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-er-3-premap-omnidir-flux-v1.0_8iiw-k23d",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars global surveyor",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-ER-3-PREMAP%2FOMNIDIR-FLUX-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-er-3-premap-omnidir-flux-v1.0_8iiw-k23d",
-            "description": "The Electron Reflectometer Data Record (ERDR) is a time ordered series of electron measurements from the Mars Global Surveyor (MGS) Mission. Each record consists of a time tag with 19 scalar data points representing measurements of the electron flux in 19 different energy channels, ranging from 10 eV to 20 keV, with an energy resolution of 25%. Each data point is a measure of the electron flux (cm-2 sec-1 ster-1 eV-1) averaged over a 360 x 14 degree disk-shaped field of view (FOV). (Parts of this FOV are masked because of spacecraft obstructions, as described below.) During the Science Phasing Orbits (SPO), the spacecraft was in Array Normal Spin (ANS) configuration, for which the ER field of view sweeps out the entire sky (4-pi ster) every 50 minutes, which is much longer than the integration time per record (2 to 48 sec, depending on energy and telemetry rate) and much longer than most timescales of interest in Mars' plasma environment.",
-            "title": "MGS MARS/MOONS MAG/ER PRE-MAP ER OMNIDIRECTIONAL FLUX V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MGS MARS/MOONS MAG/ER PRE-MAP ER OMNIDIRECTIONAL FLUX V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-EXT2-67PCHURYUMOV-M30-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Wide Angle Camera during the ROSETTA EXTENSION 2 phase of the Rosetta mission, covering the period from 2016-05-31T23:25:00.000 to 2016-06-28T23:24:59.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-ext2-67pchuryumov-m30-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "zeta cas",
                 "vega",
                 "67p/churyumov-gerasimenko 1 (1969 r1)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-EXT2-67PCHURYUMOV-M30-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-ext2-67pchuryumov-m30-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Wide Angle Camera during the ROSETTA EXTENSION 2 phase of the Rosetta mission, covering the period from 2016-05-31T23:25:00.000 to 2016-06-28T23:24:59.000.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 EXT2-MTP030 RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 EXT2-MTP030 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TBOC7-V1.0",
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
+            "description": "The Cassini Radio Science Titan Bistatic and Occultation experiments (TBOC7) Raw Data Archive is a time-ordered collection of radio science raw data acquired on February 16, 2016, during the Cassini Extended Extended Mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tboc7-v1.0_8ipw-yydi",
+            "issued": "2021-05-21",
+            "keyword": [
+                "cassini-huygens",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TBOC7-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tboc7-v1.0_8ipw-yydi",
-            "description": "The Cassini Radio Science Titan Bistatic and Occultation experiments (TBOC7) Raw Data Archive is a time-ordered collection of radio science raw data acquired on February 16, 2016, during the Cassini Extended Extended Mission.",
-            "title": "CASSINI RSS RAW DATA SET - TBOC7 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI RSS RAW DATA SET - TBOC7 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2652675403-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC.",
-            "issued": "2023-04-04",
-            "temporal": "2022-11-10T00:00:00Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-04",
-            "keyword": [
-                "ocean optics",
-                "aerosols",
-                "oceans",
-                "atmosphere",
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
-            "identifier": "C2652675403-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "NOAA-21 VIIRS Global Mapped Remote-Sensing Reflectance (RRS) - NRT Data, version R2022.0",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NOAA21/VIIRS/L3M/RRS/2022",
-                    "description": "VIIRS-NOAA-21 L3M Remote-Sensing Reflectance (RRS) - NRT Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS-NOAA-21 L3M Remote-Sensing Reflectance (RRS) - NRT Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NOAA21/VIIRS/L3M/RRS/2022",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/VIIRSJ2/L3SMI/",
-                    "description": "OB.DAAC OPeNDAP Site for NOAA-21 VIIRS Standard Mapped Image (SMI) Product",
                     "@type": "dcat:Distribution",
+                    "description": "OB.DAAC OPeNDAP Site for NOAA-21 VIIRS Standard Mapped Image (SMI) Product",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/VIIRSJ2/L3SMI/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2652675403-OB_DAAC",
+            "issued": "2023-04-04",
+            "keyword": [
+                "ocean optics",
+                "aerosols",
+                "oceans",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2652675403-OB_DAAC.html",
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
+            "title": "NOAA-21 VIIRS Global Mapped Remote-Sensing Reflectance (RRS) - NRT Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-PWS-4-SUMM-SA60S-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains the System III (1965.0) trajectory and Sun and Earth phase angles of Galileo and selected Jovian moons when Galileo was inside 30 Jupiter radii from Jupiter. Trajectories are sampled every 20 seconds.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-pws-4-summ-sa60s-v1.0_8ira-7stw",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "jupiter",
                 "io",
@@ -366824,359 +366826,336 @@
                 "amalthea",
                 "io plasma torus"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-PWS-4-SUMM-SA60S-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-pws-4-summ-sa60s-v1.0_8ira-7stw",
-            "description": "This data set contains the System III (1965.0) trajectory and Sun and Earth phase angles of Galileo and selected Jovian moons when Galileo was inside 30 Jupiter radii from Jupiter. Trajectories are sampled every 20 seconds.",
-            "title": "GO JUPITER PWS RESAMP SUMMARY SPECTRUM ANALYZER 60S V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GO JUPITER PWS RESAMP SUMMARY SPECTRUM ANALYZER 60S V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/MC3E/SBAND/DATA102",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Williams, Christopher.2013. GPM GROUND VALIDATION NOAA S-BAND PROFILER RAW DATA SPC FORMAT MC3E [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/MC3E/SBAND/DATA102",
-            "issued": "2013-01-29",
-            "temporal": "2011-04-08T00:00:00Z/2011-06-07T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-23",
-            "keyword": [
-                "earth science",
-                "radar",
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
-            "identifier": "C1979716838-GHRC_DAAC",
             "description": "The GPM Ground Validation NOAA S-Band Profiler Raw Data SPC Format MC3E dataset is the S-band Profiler Raw dataset was saved in Vaisala SPC format. The numeric values in both formats are exactly the same. The overarching goal was to provide the most complete characterization of convective cloud systems, precipitation, and the environment that has ever been obtained, providing constraints for model cumulus parameterizations and space-based rainfall retrieval algorithms over land that had never before been available. The S-band Profiler Raw dataset in the proprietary Vaisala SPC format was gathered during the Midlatitude Continental Convective Clouds Experiment (MC3E) in Oklahoma April 8, 2011 to June 7, 2011 and consists of uncalibrated Doppler velocity spectra data in units of relative power return. The S-band 2.8 GHz profiler points vertically and measures the backscattered power from raindrops and ice particles as precipitating cloud systems pass overhead. The profiler processes radar pulses during a 7-second dwell before calculating and saving uncalibrated Doppler velocity spectra at each range gate that were separated by 60-meters vertically. Data collected during each hour are saved in two files. All precipitation mode profiles are saved in one hourly data file and all attenuated mode profiles are saved in another hourly data file. Calibrated data can be obtained from the S-band Original Dwell and Minute datasets. Specialized read software may be purchased from Vaisala.",
-            "title": "GPM GROUND VALIDATION NOAA S-BAND PROFILER RAW DATA SPC FORMAT MC3E V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FMC3E%2FSBAND%2FDATA102",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FMC3E%2FSBAND%2FDATA102",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmsbdrwspcmc3e",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmsbdrwspcmc3e",
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
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/gpmgv/mc3e/gpmsbandmc3e/gpm_noaa_sband_mc3e.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/gpmgv/mc3e/gpmsbandmc3e/gpm_noaa_sband_mc3e.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
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
+            "identifier": "C1979716838-GHRC_DAAC",
+            "issued": "2013-01-29",
+            "keyword": [
+                "earth science",
+                "radar",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/MC3E/SBAND/DATA102",
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
             "spatial": "-121.0 28.0 -91.0 43.0",
+            "temporal": "2011-04-08T00:00:00Z/2011-06-07T23:59:59Z",
             "theme": [
                 "MC3E",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM GROUND VALIDATION NOAA S-BAND PROFILER RAW DATA SPC FORMAT MC3E V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RSI-1%2F2%2F3-CR2-0028-V1.0",
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
-                "sun"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This is a Solar Conjunction measurement covering the time 2006-04-06T06:56:54.500 to 2006-04-06T09:14:58.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rsi-1-2-3-cr2-0028-v1.0_8iuj-27p9",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international rosetta mission",
+                "sun"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RSI-1%2F2%2F3-CR2-0028-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rsi-1-2-3-cr2-0028-v1.0_8iuj-27p9",
-            "description": "This is a Solar Conjunction measurement covering the time 2006-04-06T06:56:54.500 to 2006-04-06T09:14:58.500.",
-            "title": "ROSETTA-ORBITER SUN RSI 1/2/3 CRUISE 2 0028 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER SUN RSI 1/2/3 CRUISE 2 0028 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1683",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Watts, J.D., S. Natali, S. Potter, and B.M. Rogers. 2019. Gridded Winter Soil CO2 Flux Estimates for pan-Arctic and Boreal Regions, 2003-2100. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1683",
-            "issued": "2024-05-01",
-            "temporal": "1993-01-01T00:00:00Z/2100-11-30T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-02",
-            "keyword": [
-                "atmospheric chemistry",
-                "frozen ground",
-                "land surface",
-                "atmosphere",
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
-            "identifier": "C2143812328-ORNL_CLOUD",
             "description": "This dataset provides gridded estimates of soil CO2 flux (g C m-2 d-1) for the winter non-growing season (NGS) across pan-Arctic and Boreal permafrost regions (>49 Deg N), at 25 km spatial resolution. The data are the daily average flux over a monthly period for two climate periods: the baseline climate period represents 2003-2018 and the future climate scenarios period represents 2018-2100 under Representative Concentration Pathways (RCP) 4.5 and 8.5. The data were produced by applying a Boosted Regression Tree machine learning approach to create gridded estimates of emissions based on in situ observations of NGS fluxes provided in a related dataset. The resulting monthly average flux data records can be used to calculate annual NGS soil CO2 flux budgets from 2003-2100.",
-            "graphic-preview-description": "Soil CO2 flux estimates for the Arctic-boreal permafrost region, during the non-growing season (NGS), Julian days 274 through 120. (Source J.D. Watts)",
-            "title": "Gridded Winter Soil CO2 Flux Estimates for pan-Arctic and Boreal Regions, 2003-2100",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Soil_Carbon_Flux_Maps_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1683",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1683",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/above/Soil_Carbon_Flux_Maps/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/above/Soil_Carbon_Flux_Maps/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Soil_Carbon_Flux_Maps.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Soil_Carbon_Flux_Maps.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1683",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1683",
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
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Soil_Carbon_Flux_Maps/comp/Soil_Carbon_Flux_Maps.pdf",
-                    "description": "Winter Season Soil Carbon Flux Maps, Pan-Arctic Boreal Permafrost Regions, 2003-2100: Soil_Carbon_Flux_Maps.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Winter Season Soil Carbon Flux Maps, Pan-Arctic Boreal Permafrost Regions, 2003-2100: Soil_Carbon_Flux_Maps.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Soil_Carbon_Flux_Maps/comp/Soil_Carbon_Flux_Maps.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Soil_Carbon_Flux_Maps_Fig1.png",
-                    "description": "Soil CO2 flux estimates for the Arctic-boreal permafrost region, during the non-growing season (NGS), Julian days 274 through 120. (Source J.D. Watts)",
                     "@type": "dcat:Distribution",
+                    "description": "Soil CO2 flux estimates for the Arctic-boreal permafrost region, during the non-growing season (NGS), Julian days 274 through 120. (Source J.D. Watts)",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Soil_Carbon_Flux_Maps_Fig1.png",
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
+            "graphic-preview-description": "Soil CO2 flux estimates for the Arctic-boreal permafrost region, during the non-growing season (NGS), Julian days 274 through 120. (Source J.D. Watts)",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Soil_Carbon_Flux_Maps_Fig1.png",
+            "identifier": "C2143812328-ORNL_CLOUD",
+            "issued": "2024-05-01",
+            "keyword": [
+                "atmospheric chemistry",
+                "frozen ground",
+                "land surface",
+                "atmosphere",
+                "soils",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1683",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-05-02",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-180.0 -84.69 179.9 89.98",
+            "temporal": "1993-01-01T00:00:00Z/2100-11-30T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Gridded Winter Soil CO2 Flux Estimates for pan-Arctic and Boreal Regions, 2003-2100"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-RPCMIP-3-EAR2-V2.0",
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
+            "description": "This archive contains data from the RPC-MIP instrument onboard ROSETTA Orbiter acquired during the EARTH SWING-BY 2 mission phase. It also contains documentation which describes the RPC-MIP experiment. The data archived in this data set conform to the Planetary Data System Standards, Version 3.6. This is V2.0 updated after Science Review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-rpcmip-3-ear2-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "earth",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-RPCMIP-3-EAR2-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-rpcmip-3-ear2-v2.0",
-            "description": "This archive contains data from the RPC-MIP instrument onboard ROSETTA Orbiter acquired during the EARTH SWING-BY 2 mission phase. It also contains documentation which describes the RPC-MIP experiment. The data archived in this data set conform to the Planetary Data System Standards, Version 3.6. This is V2.0 updated after Science Review.",
-            "title": "ROSETTA-ORBITER EARTH RPCMIP 3 EAR2 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER EARTH RPCMIP 3 EAR2 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E%2FCAL-NAVCAM-2-EAR2-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This dataset contains RAW DATA of the EARTH 2 Swingby Phase from 16 September 2007 until 22 January 2008.  The closest approach (CA) took place on 13 November 2007",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-cal-navcam-2-ear2-v1.0_8iyd-pfza",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "moon",
                 "international rosetta mission",
                 "earth",
                 "calibration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E%2FCAL-NAVCAM-2-EAR2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-cal-navcam-2-ear2-v1.0_8iyd-pfza",
-            "description": "This dataset contains RAW DATA of the EARTH 2 Swingby Phase from 16 September 2007 until 22 January 2008.  The closest approach (CA) took place on 13 November 2007",
-            "title": "ROSETTA-ORBITER-EARTH/CAL-NAVCAM-2-EAR2-V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER-EARTH/CAL-NAVCAM-2-EAR2-V1.0"
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
-                "ask the academy",
-                "appel",
-                "knowledge",
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
-            "identifier": "NASA-862__60",
             "description": "Academy of Program/Project & Engineering Leadership's Ask the Academy magazine past issues.",
-            "title": "Academy of Program/Project & Engineering Leadership ASK the Academy Past Issues",
-            "programCode": [
-                "026:045"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -367184,134 +367163,127 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
+            "identifier": "NASA-862__60",
+            "issued": "2018-06-25",
+            "keyword": [
+                "ask the academy",
+                "appel",
+                "knowledge",
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-RSS-5-TPS-V1.0",
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
-                "mars global surveyor",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains over 21000 temperature-pressure profiles (TPS files) of the neutral atmosphere derived from Mars Global Surveyor (MGS) radio occultation data. The profiles were previously archived in the MGS-M-RSS-5-SDP-V1.0 data set along with other reduced data products from the MGS Radio Science Team (RST). Here they have been pulled from the original 38 volumes and reorganized in chronological order on a single volume. The profiles themselves have not been modified, and the labels have been edited only to conform with the requirements of the new data set. This set of profiles is accompanied by a single occultation summary file which lists key characteristics of each experiment.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-rss-5-tps-v1.0_8izz-vqwc",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars global surveyor",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-RSS-5-TPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-rss-5-tps-v1.0_8izz-vqwc",
-            "description": "This data set contains over 21000 temperature-pressure profiles (TPS files) of the neutral atmosphere derived from Mars Global Surveyor (MGS) radio occultation data. The profiles were previously archived in the MGS-M-RSS-5-SDP-V1.0 data set along with other reduced data products from the MGS Radio Science Team (RST). Here they have been pulled from the original 38 volumes and reorganized in chronological order on a single volume. The profiles themselves have not been modified, and the labels have been edited only to conform with the requirements of the new data set. This set of profiles is accompanied by a single occultation summary file which lists key characteristics of each experiment.",
-            "title": "MGS RS: ATMOSPHERIC TEMPERATURE-PRESSURE PROFILES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MGS RS: ATMOSPHERIC TEMPERATURE-PRESSURE PROFILES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-ESC3-67PCHURYUMOV-M20-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera during the COMET ESCORT 3 phase of the Rosetta mission at the comet 67P, covering the period from 2015-08-25T23:25:00.000 to 2015-09-22T23:24:59.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-esc3-67pchuryumov-m20-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "bias",
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "dark"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-ESC3-67PCHURYUMOV-M20-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-esc3-67pchuryumov-m20-v1.0",
-            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera during the COMET ESCORT 3 phase of the Rosetta mission at the comet 67P, covering the period from 2015-08-25T23:25:00.000 to 2015-09-22T23:24:59.000.",
-            "title": "ROSETTA-ORBITER COMET ESCORT 3 OSIWAC 2 EDR MTP020 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMET ESCORT 3 OSIWAC 2 EDR MTP020 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TLTYU661EXN6",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Charles Gatebe; Michael King; Rajesh Poudyal. 2019-03-11. CAR_KUWAITOILFIRE_BRDF. Version 2. CAR Kuwait Oil Fire Spectral Reflectance BRDF V2. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/TLTYU661EXN6. https://disc.gsfc.nasa.gov/datacollection/CAR_KUWAITOILFIRE_BRDF_2.html.",
-            "issued": "2019-03-11",
-            "temporal": "1991-05-18T00:00:00Z/1991-06-02T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-26",
-            "keyword": [
-                "earth science",
-                "surface radiative properties",
-                "oceans",
-                "ocean optics",
-                "land surface",
-                "clouds",
-                "atmospheric radiation",
-                "atmosphere",
-                "aerosols"
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
-            "identifier": "C1617621689-GES_DISC",
-            "description": "CAR Kuwait Oil Fire mission measured bidirectional reflectance function of smoke from Kuwait oil fires during the Kuwait Oil Fire Smoke Experiment. Measurements were also taken over the Saudi Arabian desert with overlying desert dust, and Persian Gulf waters with some overlying aerosols. This experiment was a part of an international research effort in response to an environmental crisis, when over 600 oil wells in Kuwait were ignited by Iraqi forces in 1991. The resulting fires produced large plumes of smoke that had significant effects on the Persian Gulf region but limited global effects. Between May 16 and June 12, 1991, the Kuwait Oil Fire Smoke Experiment (KOFSE) was conducted in the Persian Gulf Region. The purpose of KOFSE was to determine the chemical and physical nature of the smoke and to investigate its potential effects on air quality, weather, and climate.\n\nThis data set consists of observations made with the CAR instrument and includes values for bidirectional reflectance factor at varying spectral bands.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "CAR_KUWAITOILFIRE_BRDF",
             "creator": "Charles Gatebe; Michael King; Rajesh Poudyal",
-            "title": "CAR Kuwait Oil Fire BRDF V2 (CAR_KUWAITOILFIRE_BRDF) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/CAR_KUWAITOILFIRE_L1C_1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "CAR Kuwait Oil Fire mission measured bidirectional reflectance function of smoke from Kuwait oil fires during the Kuwait Oil Fire Smoke Experiment. Measurements were also taken over the Saudi Arabian desert with overlying desert dust, and Persian Gulf waters with some overlying aerosols. This experiment was a part of an international research effort in response to an environmental crisis, when over 600 oil wells in Kuwait were ignited by Iraqi forces in 1991. The resulting fires produced large plumes of smoke that had significant effects on the Persian Gulf region but limited global effects. Between May 16 and June 12, 1991, the Kuwait Oil Fire Smoke Experiment (KOFSE) was conducted in the Persian Gulf Region. The purpose of KOFSE was to determine the chemical and physical nature of the smoke and to investigate its potential effects on air quality, weather, and climate.\n\nThis data set consists of observations made with the CAR instrument and includes values for bidirectional reflectance factor at varying spectral bands.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTLTYU661EXN6",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTLTYU661EXN6",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -367321,299 +367293,329 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CAR_KUWAITOILFIRE_BRDF_2.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CAR_KUWAITOILFIRE_BRDF_2.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/CAR/CAR_KUWAITOILFIRE_BRDF.2/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/CAR/CAR_KUWAITOILFIRE_BRDF.2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/opendap/CAR/CAR_KUWAITOILFIRE_BRDF.2/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/opendap/CAR/CAR_KUWAITOILFIRE_BRDF.2/contents.html",
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
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/CAR/CAR_BRDF_README-v2.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/CAR/CAR_BRDF_README-v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=CAR_KUWAITOILFIRE_BRDF",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=CAR_KUWAITOILFIRE_BRDF",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/CAR_KUWAITOILFIRE_L1C_1.jpg",
+            "identifier": "C1617621689-GES_DISC",
+            "issued": "2019-03-11",
+            "keyword": [
+                "earth science",
+                "surface radiative properties",
+                "oceans",
+                "ocean optics",
+                "land surface",
+                "clouds",
+                "atmospheric radiation",
+                "atmosphere",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.5067/TLTYU661EXN6",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-05-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "CAR_KUWAITOILFIRE_BRDF",
             "spatial": "46.9617 27.8542 49.3732 28.602",
+            "temporal": "1991-05-18T00:00:00Z/1991-06-02T23:59:59.999Z",
             "theme": [
                 "CAR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CAR Kuwait Oil Fire BRDF V2 (CAR_KUWAITOILFIRE_BRDF) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CALIOP/CALIPSO/LID_L2_BLOWINGSNOW_GREENLAND-STANDARD-V1-00",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/CALIOP/CALIPSO/LID_L2_BLOWINGSNOW_GREENLAND-STANDARD-V1-00.",
-            "issued": "2018-10-03",
-            "temporal": "2006-06-12T00:00:00Z/2023-07-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-01",
-            "keyword": [
-                "earth science",
-                "atmospheric winds",
-                "precipitation",
-                "weather events",
-                "atmosphere",
-                "atmospheric temperature",
-                "atmospheric radiation"
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
-            "identifier": "C2828847685-LARC_ASDC",
             "description": "CAL_LID_L2_BlowingSnow_Greenland-Standard-V1-00 is the Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) Lidar Level 2 Blowing Snow - Greenland, Version 1-00 data product. This product was collected using the CALIPSO Cloud-Aerosol Lidar with Orthogonal Polarization (CALIOP) instrument and reports the distribution of blowing snow properties based on back-scatter retrievals over Greenland. The CALIPSO satellite comprises three instruments: CALIOP, Imaging Infrared Radiometer (IIR), and Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency CNES (Centre National d'Etudes Spatiales). CALIPSO was launched on April 28, 2006, to study the impact of clouds and aerosols on the Earth's radiation budget and climate. From June 13, 2006, to September 13, 2018, CALIPSO was part of the A-Train constellation for coincident Earth Observations. After September 13, 2018, the satellite was lowered from 705 to 688 km to resume flying in formation with CloudSat, called the C-Train.",
-            "graphic-preview-description": "Mission Logo",
-            "title": "CALIPSO Lidar Level 2 Blowing Snow - Greenland, V1-00",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/calipso.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCALIOP%2FCALIPSO%2FLID_L2_BLOWINGSNOW_GREENLAND-STANDARD-V1-00",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCALIOP%2FCALIPSO%2FLID_L2_BLOWINGSNOW_GREENLAND-STANDARD-V1-00",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2828847685-LARC_ASDC",
-                    "description": "Earthdata Search for CAL_LID_L2_BlowingSnow_Greenland-Standard-V1-00_V1-00 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CAL_LID_L2_BlowingSnow_Greenland-Standard-V1-00_V1-00 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2828847685-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/CALIOP/CALIPSO/LID_L2_BLOWINGSNOW_GREENLAND-STANDARD-V1-00",
-                    "description": "DOI data set landing page for CAL_LID_L2_BlowingSnow_Greenland-Standard-V1-00_V1-00",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CAL_LID_L2_BlowingSnow_Greenland-Standard-V1-00_V1-00",
+                    "downloadURL": "https://doi.org/10.5067/CALIOP/CALIPSO/LID_L2_BLOWINGSNOW_GREENLAND-STANDARD-V1-00",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
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
                     "title": "View this dataset's how-to documentation"
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
-                    "downloadURL": "https://www.icare.univ-lille.fr/category/icare-news/tools/",
-                    "description": "ICARE Programmers Toolbox",
                     "@type": "dcat:Distribution",
+                    "description": "ICARE Programmers Toolbox",
+                    "downloadURL": "https://www.icare.univ-lille.fr/category/icare-news/tools/",
+                    "mediaType": "text/html",
                     "title": "Use this dataset in a web based map viewerf"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://asdc.larc.nasa.gov/static/images/project_logos/calipso.png",
-                    "description": "Mission Logo",
                     "@type": "dcat:Distribution",
+                    "description": "Mission Logo",
+                    "downloadURL": "https://asdc.larc.nasa.gov/static/images/project_logos/calipso.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization through WORLDVIEW"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/products/CALIPSO_DPC_Rev4x97.pdf",
-                    "description": "CALIPSO\u2019s Data Products Catalog Release 4.97",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO\u2019s Data Products Catalog Release 4.97",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/products/CALIPSO_DPC_Rev4x97.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CALIPSO/LID_L2_BlowingSnow_Greenland-Standard-V1-00/",
-                    "description": "ASDC Direct Data Download for CAL_LID_L2_BlowingSnow_Greenland-Standard-V1-00_V1-00",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CAL_LID_L2_BlowingSnow_Greenland-Standard-V1-00_V1-00",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CALIPSO/LID_L2_BlowingSnow_Greenland-Standard-V1-00/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CALIPSO/LID_L2_BlowingSnow_Greenland-Standard-V1-00/contents.html",
-                    "description": "OPeNDAP data access for CAL_LID_L2_BlowingSnow_Greenland-Standard-V1-00_V1-00",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CAL_LID_L2_BlowingSnow_Greenland-Standard-V1-00_V1-00",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CALIPSO/LID_L2_BlowingSnow_Greenland-Standard-V1-00/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Mission Logo",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/calipso.png",
+            "identifier": "C2828847685-LARC_ASDC",
+            "issued": "2018-10-03",
+            "keyword": [
+                "earth science",
+                "atmospheric winds",
+                "precipitation",
+                "weather events",
+                "atmosphere",
+                "atmospheric temperature",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://doi.org/10.5067/CALIOP/CALIPSO/LID_L2_BLOWINGSNOW_GREENLAND-STANDARD-V1-00",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-07-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>58.0 90.0 90.0 90.0 90.0 -76.0 58.0 -76.0 58.0 90.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2006-06-12T00:00:00Z/2023-07-01T00:00:00Z",
             "theme": [
                 "CALIPSO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CALIPSO Lidar Level 2 Blowing Snow - Greenland, V1-00"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-EXT1-67PCHURYUMOV-M25-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera during the ROSETTA EXTENSION 1 phase of the Rosetta mission at the comet 67P, covering the period from 2016-01-12T23:25:00.000 to 2016-02-09T23:24:59.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-ext1-67pchuryumov-m25-v1.0_8j8v-gqxs",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "earth",
                 "international rosetta mission",
@@ -367621,37 +367623,46 @@
                 "vega",
                 "67p/churyumov-gerasimenko 1 (1969 r1)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-EXT1-67PCHURYUMOV-M25-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-ext1-67pchuryumov-m25-v1.0_8j8v-gqxs",
-            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera during the ROSETTA EXTENSION 1 phase of the Rosetta mission at the comet 67P, covering the period from 2016-01-12T23:25:00.000 to 2016-02-09T23:24:59.000.",
-            "title": "ROSETTA-ORBITER ROSETTA EXTENSION 1 OSINAC 3 RDR MTP025 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER ROSETTA EXTENSION 1 OSINAC 3 RDR MTP025 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/8jam-432k",
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
+                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_wfc_l1_iir-valstage1-v3-02_table",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000206",
             "issued": "2018-06-25",
-            "temporal": "2006-06-13/2011-10-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "satellite",
                 "aerosol",
@@ -367661,342 +367672,309 @@
                 "eos",
                 "radiation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John M. Kusterer",
-                "hasEmail": "mailto:john.m.kusterer@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/8jam-432k",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:004"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000206",
-            "description": "Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) was launched on April 28, 2006 to study the impact of clouds and aerosols on the Earth\u2019s radiation budget and climate. It flies in formation with five other satellites in the international \u201cA-Train\u201d (PDF) constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments, the Cloud-Aerosol LIdar with Orthogonal Polarization (CALIOP), the Imaging Infrared Radiometer (IIR), and the Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES. These data consist 5 km aerosol layer data.",
-            "title": "CALIPSO Wide Field Camera (WFC)  L1B Science 1 km Registered  Science Data V3-01",
-            "programCode": [
-                "026:004"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_wfc_l1_iir-valstage1-v3-02_table",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
+            "temporal": "2006-06-13/2011-10-31",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CALIPSO Wide Field Camera (WFC)  L1B Science 1 km Registered  Science Data V3-01"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0098",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1999-11-15. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/FIRE/0098.",
-            "issued": "1999-11-04",
-            "temporal": "1991-11-21T00:00:00Z/1991-12-07T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-13",
-            "keyword": [
-                "atmosphere",
-                "spectral/engineering",
-                "radar",
-                "earth science",
-                "clouds",
-                "atmospheric winds",
-                "altitude"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JANET INTRIERI",
                 "hasEmail": "mailto:jmi@etl.noaa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1000001186-LARC_ASDC",
             "description": "The First ISCCP Regional Experiments have been designed to improve data products and cloud/radiation parameterizations used in general circulation models (GCMs). Specifically, the goals of FIRE are (1) to improve basic understanding of the interaction of physical processes in determining life cycles of cirrus and marine stratocumulus systems and the radiative properties of these clouds during their life cycles and (2) to investigate the interrelationships between the ISCCP data, GCM parameterizations, and higher space and time resolution cloud data.To-date, four intensive field-observation periods were planned and executed: a cirrus IFO (October 13-November 2, 1986); a marine stratocumulus IFO off the southwestern coast of California (June 29-July 20, 1987); a second cirrus IFO in southeastern Kansas (November 13-December 7, 1991); and a second marine stratocumulus IFO in the eastern North Atlantic Ocean (June 1-June 28, 1992). Each mission combined coordinated satellite, airborne, and surface observations with modeling studies to investigate the cloud properties and physical processes of the cloud systems.The Doppler lidar data set includes wind profiles derived by the VAD method for the FIRE-II top 5 priority days (21,25,28,30 of Nov. 1991, and Dec. 5, 1991). Vertical profiles of the horizontal wind speed and direction were acquired by the lidar using a classical method commonly referred to as the VAD technique, where VAD stands for Velocity Azimuth Display.The Doppler lidar experiment objective was to obtain lidar measurements of relative backscatter signal intensity and radial velocity from cirrus clouds to study their microphysical and radiative properties. This data set provides vertical profiles (approx. 1.5 - 20.0 km agl).",
-            "title": "First ISCCP Regional Experiment (FIRE) Cirrus Phase II NOAA Carbon Dioxide (CO2) Doppler & Lidar",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0098",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0098",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001186-LARC_ASDC",
-                    "description": "Earthdata Search for FIRE_CI2_DOPLR_LIDAR_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FIRE_CI2_DOPLR_LIDAR_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001186-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_CI2_DOPLR_LIDAR/contents.html",
-                    "description": "OPeNDAP data access for FIRE_CI2_DOPLR_LIDAR_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for FIRE_CI2_DOPLR_LIDAR_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_CI2_DOPLR_LIDAR/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ci2_doplr_lidar_dataset.pdf",
-                    "description": "FIRE Cirrus 2 National Oceanic and Atmospheric Administration (NOAA) Carbon Dioxide (CO2) Doppler LIDAR (FIRE_CI2_DOPLR_LIDAR) Langley DAAC Data Set Document",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE Cirrus 2 National Oceanic and Atmospheric Administration (NOAA) Carbon Dioxide (CO2) Doppler LIDAR (FIRE_CI2_DOPLR_LIDAR) Langley DAAC Data Set Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ci2_doplr_lidar_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/postscript",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ci2_doplr_lidar.ps",
-                    "description": "FIRE Cirrus 2 - Direct File Download (.ps)",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE Cirrus 2 - Direct File Download (.ps)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ci2_doplr_lidar.ps",
+                    "mediaType": "application/postscript",
                     "title": "View this dataset's science data product software documentation"
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
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0098",
-                    "description": "DOI data set landing page for FIRE_CI2_DOPLR_LIDAR_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIRE_CI2_DOPLR_LIDAR_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0098",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_CI2_DOPLR_LIDAR/",
-                    "description": "ASDC Direct Data Download for FIRE_CI2_DOPLR_LIDAR_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIRE_CI2_DOPLR_LIDAR_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_CI2_DOPLR_LIDAR/",
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
+            "identifier": "C1000001186-LARC_ASDC",
+            "issued": "1999-11-04",
+            "keyword": [
+                "atmosphere",
+                "spectral/engineering",
+                "radar",
+                "earth science",
+                "clouds",
+                "atmospheric winds",
+                "altitude"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0098",
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
             "spatial": "37.06 -95.34",
+            "temporal": "1991-11-21T00:00:00Z/1991-12-07T23:59:59.999Z",
             "theme": [
                 "FIRE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "First ISCCP Regional Experiment (FIRE) Cirrus Phase II NOAA Carbon Dioxide (CO2) Doppler & Lidar"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-PANCAM-3-RADCAL-RDR-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-pancam-3-radcal-rdr-v1.0_8jc7-yshu",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-PANCAM-3-RADCAL-RDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-pancam-3-radcal-rdr-v1.0_8jc7-yshu",
-            "description": "not applicable",
-            "title": "MER 1 MARS PANCAM RADIOMETRICALLY CALIBRATED RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MER 1 MARS PANCAM RADIOMETRICALLY CALIBRATED RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSINAC-4-CR2-CHKOUT-STR-REFL-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units  (normalized and thus without unit),  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the CRUISE 2 mission phase, covering the period  from 2005-04-05T00:00:00.000 to 2006-07-28T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. This version V1.0 is the first version of this dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osinac-4-cr2-chkout-str-refl-v1.0_8jcz-cgyd",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "9p/tempel 1 (1867 g1)",
                 "2867 steins"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSINAC-4-CR2-CHKOUT-STR-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osinac-4-cr2-chkout-str-refl-v1.0_8jcz-cgyd",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units  (normalized and thus without unit),  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the CRUISE 2 mission phase, covering the period  from 2005-04-05T00:00:00.000 to 2006-07-28T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. This version V1.0 is the first version of this dataset.",
-            "title": "ROSETTA-ORBITER CHECKOUT OSINAC 4 CR2 RDR-STR-REFL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECKOUT OSINAC 4 CR2 RDR-STR-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5270/S5P-tjlxfd2",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Copernicus Sentinel data processed by ESA, German Aerospace Center (DLR). 2019-08-19. S5P_L2__HCHO___HiR. Version 1. Sentinel-5P TROPOMI Tropospheric Formaldehyde HCHO 1-Orbit L2 5.5km x 3.5km. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5270/S5P-tjlxfd2. https://disc.gsfc.nasa.gov/datacollection/S5P_L2__HCHO___HiR_1.html. Digital Science Data.",
-            "issued": "2017-05-05",
-            "temporal": "2019-08-06T02:41:41Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-05-05",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric chemistry"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Nicolas Theys",
                 "hasEmail": "mailto:nicolas.theys@aeronomie.be"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1627516292-GES_DISC",
-            "description": "Starting from August 6th in 2019, Sentinel-5P TROPOMI along-track high spatial resolution (~5.5km at nadir) has been implemented.\nStarting from July 13th in 2020, five Sentinel-5P TROPOMI level-2 products including total and tropospheric column ozone, sulfur dioxide, CLOUD, and formaldehyde have been generated in processor version 2.\nFor data before August 6th of 2019, please check S5P_L2__HCHO___1 data collection.\nFor data between August 6th of 2019 and July 13th of 2020, please check S5P_L2__HCHO___HiR_1 data collection.\nFor data after July 13th of 2020, please check S5P_L2__HCHO___HiR_2 data collection.\n\nThe Copernicus Sentinel-5 Precursor (Sentinel-5P or S5P) satellite mission is one of the European Space Agency's (ESA) new mission family - Sentinels, and it is a joint initiative between the Kingdom of the Netherlands and the ESA. The sole payload on Sentinel-5P is the TROPOspheric Monitoring Instrument (TROPOMI), which is a nadir-viewing 108 degree Field-of-View push-broom grating hyperspectral spectrometer, covering the wavelength of ultraviolet-visible (UV-VIS, 270nm to 495nm), near infrared (NIR, 675nm to 775nm), and shortwave infrared (SWIR, 2305nm-2385nm). Sentinel-5P is the first of the Atmospheric Composition Sentinels and is expected to provide measurements of ozone, NO2, SO2, CH4, CO, formaldehyde, aerosols and cloud at high spatial, temporal and spectral resolutions.\n\nThe retrieval algorithm for Sentinel-5P TROPOMI HCHO from ultraviolet spectral measurements is the Differential Optical Absorption Spectroscopy (DOAS) method. The relevant information of absorption cross section, instrument characteristics, cloud cover as well as aerosol index are utilized to derive HCHO slant column density (SCD). The air mass factor (AMF) Look-up table has been created with the VLIDORT 2.6 radiative transfer model at the wavelength of 340 nm, and the AMF is used to compute the total column averaging kernels (AK). The background normalization of the slant columns is essential for weak absorbent like formaldehyde to compensate for possible systematic offsets. The main outputs of the DOAS algorithm are the vertical column density (VCD), SCD, AMF, uncertainty, AK, and quality flags.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "S5P_L2__HCHO___HiR",
             "creator": "Copernicus Sentinel data processed by ESA, German Aerospace Center (DLR)",
-            "title": "Sentinel-5P TROPOMI Tropospheric Formaldehyde HCHO 1-Orbit L2 5.5km x 3.5km V1 (S5P_L2__HCHO___HiR) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/S5P_OFFL_L2__HCHO___HiR_1.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Starting from August 6th in 2019, Sentinel-5P TROPOMI along-track high spatial resolution (~5.5km at nadir) has been implemented.\nStarting from July 13th in 2020, five Sentinel-5P TROPOMI level-2 products including total and tropospheric column ozone, sulfur dioxide, CLOUD, and formaldehyde have been generated in processor version 2.\nFor data before August 6th of 2019, please check S5P_L2__HCHO___1 data collection.\nFor data between August 6th of 2019 and July 13th of 2020, please check S5P_L2__HCHO___HiR_1 data collection.\nFor data after July 13th of 2020, please check S5P_L2__HCHO___HiR_2 data collection.\n\nThe Copernicus Sentinel-5 Precursor (Sentinel-5P or S5P) satellite mission is one of the European Space Agency's (ESA) new mission family - Sentinels, and it is a joint initiative between the Kingdom of the Netherlands and the ESA. The sole payload on Sentinel-5P is the TROPOspheric Monitoring Instrument (TROPOMI), which is a nadir-viewing 108 degree Field-of-View push-broom grating hyperspectral spectrometer, covering the wavelength of ultraviolet-visible (UV-VIS, 270nm to 495nm), near infrared (NIR, 675nm to 775nm), and shortwave infrared (SWIR, 2305nm-2385nm). Sentinel-5P is the first of the Atmospheric Composition Sentinels and is expected to provide measurements of ozone, NO2, SO2, CH4, CO, formaldehyde, aerosols and cloud at high spatial, temporal and spectral resolutions.\n\nThe retrieval algorithm for Sentinel-5P TROPOMI HCHO from ultraviolet spectral measurements is the Differential Optical Absorption Spectroscopy (DOAS) method. The relevant information of absorption cross section, instrument characteristics, cloud cover as well as aerosol index are utilized to derive HCHO slant column density (SCD). The air mass factor (AMF) Look-up table has been created with the VLIDORT 2.6 radiative transfer model at the wavelength of 340 nm, and the AMF is used to compute the total column averaging kernels (AK). The background normalization of the slant columns is essential for weak absorbent like formaldehyde to compensate for possible systematic offsets. The main outputs of the DOAS algorithm are the vertical column density (VCD), SCD, AMF, uncertainty, AK, and quality flags.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5270%2FS5P-tjlxfd2",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5270%2FS5P-tjlxfd2",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -368006,90 +367984,114 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/S5P_L2__HCHO___HiR_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/S5P_L2__HCHO___HiR_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/opendap/S5P_TROPOMI_Level2/S5P_L2__HCHO___HiR.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/opendap/S5P_TROPOMI_Level2/S5P_L2__HCHO___HiR.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/data/S5P_TROPOMI_Level2/S5P_L2__HCHO___HiR.1",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/data/S5P_TROPOMI_Level2/S5P_L2__HCHO___HiR.1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=S5P_L2__HCHO___HiR_1",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=S5P_L2__HCHO___HiR_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sentinel.esa.int/documents/247904/2476257/Sentinel-5P-ATBD-HCHO-TROPOMI",
-                    "description": "Algorithm Theoretical Basis Document",
                     "@type": "dcat:Distribution",
+                    "description": "Algorithm Theoretical Basis Document",
+                    "downloadURL": "https://sentinel.esa.int/documents/247904/2476257/Sentinel-5P-ATBD-HCHO-TROPOMI",
+                    "mediaType": "text/html",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://sentinel.esa.int/documents/247904/3541451/Sentinel-5P-Formaldehyde-Readme.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://sentinel.esa.int/documents/247904/3541451/Sentinel-5P-Formaldehyde-Readme.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sentinel.esa.int/documents/247904/2474726/Sentinel-5P-Level-2-Product-User-Manual-Formaldehyde",
-                    "description": "Product User Manual Document",
                     "@type": "dcat:Distribution",
+                    "description": "Product User Manual Document",
+                    "downloadURL": "https://sentinel.esa.int/documents/247904/2474726/Sentinel-5P-Level-2-Product-User-Manual-Formaldehyde",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/S5P_OFFL_L2__HCHO___HiR_1.png",
+            "identifier": "C1627516292-GES_DISC",
```

