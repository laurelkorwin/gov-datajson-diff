# Change History for nasa.json (Part 27)

### Changes from 31606f9 to dd2190f (Part 16/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001422-NSIDC_ECS&m=25.751953125%21-97.716796875%214%211%210%210%2C2&q=CLASIC07&ok=CLASIC07",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/CL07PLTB/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/CL07PLTB/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/58ILBIVGP1RC",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/58ILBIVGP1RC",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/58ILBIVGP1RC",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/58ILBIVGP1RC",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1000001422-NSIDC_ECS",
+            "issued": "2007-06-11",
+            "keyword": [
+                "spectral/engineering",
+                "microwave",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/58ILBIVGP1RC",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2007-07-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-98.7 34.91 -97.75 35.21",
+            "temporal": "2007-06-11T00:00:00Z/2007-07-06T23:59:59.999Z",
             "theme": [
                 "CLASIC07",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CLASIC07 PALS Brightness Temperature Data V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GGDAS-3NH33",
             "citation": "Rodell M, et. al. 2020-04-09. Monthly gridded Global Land Data Assimilation System (GLDAS) from Noah-v3.3 land hydrology model for GRACE and GRACE-FO over nominal months. Version 3.3. TELLUS_GLDAS-NOAH-3.3_TWS-ANOMALY_MONTHLY. JPL TELLUS. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/GGDAS-3NH33. https://doi.org/10.1175/BAMS-85-3-381. Rodell M, et. al, TELLUS, 2020-04-09, Monthly gridded Global Land Data Assimilation System (GLDAS) from Noah-v3.3 land hydrology model for GRACE and GRACE-FO over nominal months, THE GLOBAL LAND DATA ASSIMILATION SYSTEM, https://doi.org/10.1175/BAMS-85-3-381.",
-            "issued": "2020-03-12",
-            "temporal": "2002-04-04T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-03-12",
-            "references": [
-                "https://doi.org/10.1029/2011WR011453"
-            ],
-            "keyword": [
-                "gravity/gravitational field",
-                "solid earth",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
             },
-            "identifier": "C2036877565-POCLOUD",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "description": "The total land water storage anomalies are aggregated from the Global Land Data Assimilation System (GLDAS) NOAH model. GLDAS outputs land water content by using numerous land surface models and data assimilation. For more information on the GLDAS project and model outputs please visit https://ldas.gsfc.nasa.gov/gldas. The aggregated land water anomalies (sum of soil moisture, snow, canopy water) provided here can be used for comparison against and evaluations of the observations of Gravity Recovery and Climate Experiment (GRACE) and GRACE-FO over land. The monthly anomalies are computed over the same days during each month as GRACE and GRACE-FO data, and are provided on monthly 1 degree lat/lon grids in NetCDF format.",
-            "release-place": "JPL TELLUS",
-            "series-name": "Monthly gridded Global Land Data Assimilation System (GLDAS) from Noah-v3.3 land hydrology model for GRACE and GRACE-FO over nominal months",
             "creator": "Rodell M, et. al",
-            "title": "Monthly gridded Global Land Data Assimilation System (GLDAS) from Noah-v3.3 land hydrology model for GRACE and GRACE-FO over nominal months",
-            "graphic-preview-description": "Thumbnail",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TELLUS_GLDAS-NOAH-3.3_TWS-ANOMALY_MONTHLY.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The total land water storage anomalies are aggregated from the Global Land Data Assimilation System (GLDAS) NOAH model. GLDAS outputs land water content by using numerous land surface models and data assimilation. For more information on the GLDAS project and model outputs please visit https://ldas.gsfc.nasa.gov/gldas. The aggregated land water anomalies (sum of soil moisture, snow, canopy water) provided here can be used for comparison against and evaluations of the observations of Gravity Recovery and Climate Experiment (GRACE) and GRACE-FO over land. The monthly anomalies are computed over the same days during each month as GRACE and GRACE-FO data, and are provided on monthly 1 degree lat/lon grids in NetCDF format.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGGDAS-3NH33",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGGDAS-3NH33",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/allData/tellus/L3/docs/GRACE_GRACE-FO_Months_RL06.pdf",
-                    "description": "GRACE monthly data integration range",
                     "@type": "dcat:Distribution",
+                    "description": "GRACE monthly data integration range",
+                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/allData/tellus/L3/docs/GRACE_GRACE-FO_Months_RL06.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TELLUS_GLDAS-NOAH-3.3_TWS-ANOMALY_MONTHLY.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TELLUS_GLDAS-NOAH-3.3_TWS-ANOMALY_MONTHLY.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/BAMS-85-3-381",
-                    "description": "The Global Land Data Assimilation System",
                     "@type": "dcat:Distribution",
+                    "description": "The Global Land Data Assimilation System",
+                    "downloadURL": "https://doi.org/10.1175/BAMS-85-3-381",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/forum/viewforum.php?f=27",
-                    "description": "PO.DAAC Forum Page",
                     "@type": "dcat:Distribution",
+                    "description": "PO.DAAC Forum Page",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/forum/viewforum.php?f=27",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gracefo.jpl.nasa.gov/",
-                    "description": "GRACE-FO Project",
                     "@type": "dcat:Distribution",
+                    "description": "GRACE-FO Project",
+                    "downloadURL": "https://gracefo.jpl.nasa.gov/",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2036877565-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2036877565-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2036877565-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2036877565-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TELLUS_GLDAS-NOAH-3.3_TWS-ANOMALY_MONTHLY.jpg",
+            "identifier": "C2036877565-POCLOUD",
+            "issued": "2020-03-12",
+            "keyword": [
+                "gravity/gravitational field",
+                "solid earth",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GGDAS-3NH33",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-03-12",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.1029/2011WR011453"
+            ],
+            "release-place": "JPL TELLUS",
+            "series-name": "Monthly gridded Global Land Data Assimilation System (GLDAS) from Noah-v3.3 land hydrology model for GRACE and GRACE-FO over nominal months",
             "spatial": "-180.0 -89.5 180.0 89.5",
+            "temporal": "2002-04-04T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "GRACE",
                 "GRACE-FO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Monthly gridded Global Land Data Assimilation System (GLDAS) from Noah-v3.3 land hydrology model for GRACE and GRACE-FO over nominal months"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TSIS/SIM/DATA324",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Erik Richard. 2024-03-01. TSIS_SSI_L3_24HR. Version 12. TSIS SIM Level 3 Solar Spectral Irradiance 24-Hour Means V12. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/TSIS/SIM/DATA324. https://disc.gsfc.nasa.gov/datacollection/TSIS_SSI_L3_24HR_12.html. Digital Science Data.",
-            "issued": "2024-03-01",
-            "temporal": "2018-03-14T00:00:00Z/2024-04-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-01",
-            "references": [
-                "https://doi.org/10.1007/s11207-005-5007-5",
-                "https://doi.org/10.1007/s11207-005-1528-1"
-            ],
-            "keyword": [
-                "solar activity",
-                "sun-earth interactions",
-                "earth science"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ERIK RICHARD",
                 "hasEmail": "mailto:Erik.Richard@lasp.colorado.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C2881895235-GES_DISC",
-            "description": "Version 12 is the current release of this data product, and supercedes all previous versions.\n\nThe TSIS SIM Level 3 Solar Spectral Irradiance (SSI) 24-Hour Means data product (TSIS_SSI_L3_24HR) uses measurements from the Spectral Irradiance Monitor (SIM) instrument, and averages them over a 24-hour period. TSIS-1 was launched on December 15, 2017 and mounted on the International Space Station (ISS) on December 30, 2017. Solar spectra are measured over the spectral range from 200 to 2400 nm at a spectral resolution ranging from 2 nm (<0.28 microns) to 45 nm (>0.4 microns). Irradiances are reported at a mean solar distance of 1 AU and zero relative line-of-sight velocity with respect to the Sun. The SIM absolute uncertainty is about 0.2%.\n\nAll of the data from this product are arranged into a single file in a tabular ASCII text format which can be easily read into a spreadsheet application. New data are appended to the file on a daily basis. The columns contain the date, Julian day, minimum wavelength, maximum wavelength, instrument mode, data version number, irradiance value, irradiance uncertainty, and data quality. The rows are arranged with data at each wavelength over the full SIM wavelength range, repeating for each day for the length of the mission.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TSIS_SSI_L3_24HR",
             "creator": "Erik Richard",
-            "title": "TSIS SIM Level 3 Solar Spectral Irradiance 24-Hour Means V12 (TSIS_SSI_L3_24HR) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TSIS/images/TSIS_SSI_L3_24HR_12.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Version 12 is the current release of this data product, and supercedes all previous versions.\n\nThe TSIS SIM Level 3 Solar Spectral Irradiance (SSI) 24-Hour Means data product (TSIS_SSI_L3_24HR) uses measurements from the Spectral Irradiance Monitor (SIM) instrument, and averages them over a 24-hour period. TSIS-1 was launched on December 15, 2017 and mounted on the International Space Station (ISS) on December 30, 2017. Solar spectra are measured over the spectral range from 200 to 2400 nm at a spectral resolution ranging from 2 nm (<0.28 microns) to 45 nm (>0.4 microns). Irradiances are reported at a mean solar distance of 1 AU and zero relative line-of-sight velocity with respect to the Sun. The SIM absolute uncertainty is about 0.2%.\n\nAll of the data from this product are arranged into a single file in a tabular ASCII text format which can be easily read into a spreadsheet application. New data are appended to the file on a daily basis. The columns contain the date, Julian day, minimum wavelength, maximum wavelength, instrument mode, data version number, irradiance value, irradiance uncertainty, and data quality. The rows are arranged with data at each wavelength over the full SIM wavelength range, repeating for each day for the length of the mission.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTSIS%2FSIM%2FDATA324",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTSIS%2FSIM%2FDATA324",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -156973,572 +156947,580 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TSIS_SSI_L3_24HR_12.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TSIS_SSI_L3_24HR_12.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/TSIS_Level3/TSIS_SSI_L3_24HR.12/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/TSIS_Level3/TSIS_SSI_L3_24HR.12/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TSIS_SSI_L3_24HR_12",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TSIS_SSI_L3_24HR_12",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/TSIS_Level3/TSIS_SSI_L3_24HR.12/doc/README.TSIS.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/TSIS_Level3/TSIS_SSI_L3_24HR.12/doc/README.TSIS.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TSIS/159520RevA_TSIS_Data_User_Guide.pdf",
-                    "description": "TSIS-1 Science Data Products Guide",
                     "@type": "dcat:Distribution",
+                    "description": "TSIS-1 Science Data Products Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TSIS/159520RevA_TSIS_Data_User_Guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TSIS/TSIS_SIM_V12_Release_Notes.pdf",
-                    "description": "Release Notes",
                     "@type": "dcat:Distribution",
+                    "description": "Release Notes",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TSIS/TSIS_SIM_V12_Release_Notes.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://lasp.colorado.edu/home/tsis/instruments/sim-spectral-irradiance-monitor/",
-                    "description": "SIM Instrument Information",
                     "@type": "dcat:Distribution",
+                    "description": "SIM Instrument Information",
+                    "downloadURL": "https://lasp.colorado.edu/home/tsis/instruments/sim-spectral-irradiance-monitor/",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TSIS/TSIS_Algorithm_Theoretical_Basis_Document_151430RevA.pdf",
-                    "description": "TSIS ATBD",
                     "@type": "dcat:Distribution",
+                    "description": "TSIS ATBD",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TSIS/TSIS_Algorithm_Theoretical_Basis_Document_151430RevA.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://lasp.colorado.edu/home/tsis/reference/publications/",
-                    "description": "List of publications.",
                     "@type": "dcat:Distribution",
+                    "description": "List of publications.",
+                    "downloadURL": "https://lasp.colorado.edu/home/tsis/reference/publications/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://lasp.colorado.edu/home/tsis/",
-                    "description": "TSIS Project Home Page.",
                     "@type": "dcat:Distribution",
+                    "description": "TSIS Project Home Page.",
+                    "downloadURL": "https://lasp.colorado.edu/home/tsis/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://lasp.colorado.edu/data/tsis/file_readers/read_lasp_ascii_file.pro",
-                    "description": "IDL-based read software.",
                     "@type": "dcat:Distribution",
+                    "description": "IDL-based read software.",
+                    "downloadURL": "https://lasp.colorado.edu/data/tsis/file_readers/read_lasp_ascii_file.pro",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TSIS/images/TSIS_SSI_L3_24HR_12.png",
+            "identifier": "C2881895235-GES_DISC",
+            "issued": "2024-03-01",
+            "keyword": [
+                "solar activity",
+                "sun-earth interactions",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/TSIS/SIM/DATA324",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-03-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1007/s11207-005-5007-5",
+                "https://doi.org/10.1007/s11207-005-1528-1"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "TSIS_SSI_L3_24HR",
+            "temporal": "2018-03-14T00:00:00Z/2024-04-01T00:00:00Z",
             "theme": [
                 "TSIS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TSIS SIM Level 3 Solar Spectral Irradiance 24-Hour Means V12 (TSIS_SSI_L3_24HR) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206883-NSIDCV0.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Air Temperatures at High Altitude, Kanchanjunga Himal, Eastern Nepal, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center.",
-            "issued": "1998-11-04",
-            "temporal": "1998-11-04T00:00:00Z/1999-11-17T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1999-11-17",
-            "keyword": [
-                "earth science",
-                "atmospheric temperature",
-                "atmosphere"
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
-            "identifier": "C1386206883-NSIDCV0",
             "description": "This data set provides air temperature (1.5 m above ground surface) data from the Kanchanjunga Himal, eastern Nepal. Air temperature was monitored from November 1998 to November 1999 at three locations (Tengkoma, Lhonak, and Ghunsa) at altitudes of 3410, 4750 and 6012 m ASL. Although temperature was measured at one-hour intervals, only daily mean values are provided.",
-            "title": "Air Temperatures at High Altitude, Kanchanjunga Himal, Eastern Nepal, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/GGD611_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/GGD611_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD611/versions/1",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://nsidc.org/data/GGD611/versions/1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD611/versions/1",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://nsidc.org/data/GGD611/versions/1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386206883-NSIDCV0",
+            "issued": "1998-11-04",
+            "keyword": [
+                "earth science",
+                "atmospheric temperature",
+                "atmosphere"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206883-NSIDCV0.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1999-11-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "87.933 27.65 88.067 27.8",
+            "temporal": "1998-11-04T00:00:00Z/1999-11-17T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Air Temperatures at High Altitude, Kanchanjunga Himal, Eastern Nepal, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-MAG-4-RDR-L1COORDS-9.6SEC-V1.1",
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
+            "description": "This data set includes Voyager 2 Saturn encounter magnetometer data from the Low Field Magnetometer (LFM) resampled at a 9.6 second sample rate from the 60 msec instrument sampling rate. Data coverage begins in the solar wind and continues until at least the first magnetopause crossing. The data are given in Kronographic (L1) coordinates. The data set is composed of the following columns: 1) time - UT of the sample in the format yyyy-mm-ddThh:mm:ss.sssZ, 2) spacecraft clock values (m65536:mod60:fds_line), 3) mag_id - magnetometer id (1 = LFM, 2 = HFM), 4) Br - radial (Saturn to spacecraft) B-field component, 5) Btheta - North/South (L1) B-field component (positive southward), 6) Bphi - azimuthal (L1) B-field component (positive eastward), 7) Bmag - magnitude of the averaged magnetic field components, 8) avg_Bmag - average of the magnetic field magnitudes, 9) delta - magnetic latitude = arcsin(Btheta/Bmag), 10) lambda - longitude = 180. - atan(Bphi/-Br), 11-13) rms_br, rms_bt, and rms_bn - rms vectors, 14) npts - number of points in average.  All magnetic field observations are measured in nanoTesla. All of the magnetic field data are calibrated (see the instrument calibration description for more details).  These data are provided in a Saturn centered spherical system (L1), based on the Saturn Longitude System (Voyager Measurements of the Rotation Period of Saturn's Magnetic Field, Desch and Kaiser, JGR, 8, 253, 1981).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-mag-4-rdr-l1coords-9.6sec-v1.1_4u5p-rbga",
+            "issued": "2021-05-21",
+            "keyword": [
+                "saturn",
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-MAG-4-RDR-L1COORDS-9.6SEC-V1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-mag-4-rdr-l1coords-9.6sec-v1.1_4u5p-rbga",
-            "description": "This data set includes Voyager 2 Saturn encounter magnetometer data from the Low Field Magnetometer (LFM) resampled at a 9.6 second sample rate from the 60 msec instrument sampling rate. Data coverage begins in the solar wind and continues until at least the first magnetopause crossing. The data are given in Kronographic (L1) coordinates. The data set is composed of the following columns: 1) time - UT of the sample in the format yyyy-mm-ddThh:mm:ss.sssZ, 2) spacecraft clock values (m65536:mod60:fds_line), 3) mag_id - magnetometer id (1 = LFM, 2 = HFM), 4) Br - radial (Saturn to spacecraft) B-field component, 5) Btheta - North/South (L1) B-field component (positive southward), 6) Bphi - azimuthal (L1) B-field component (positive eastward), 7) Bmag - magnitude of the averaged magnetic field components, 8) avg_Bmag - average of the magnetic field magnitudes, 9) delta - magnetic latitude = arcsin(Btheta/Bmag), 10) lambda - longitude = 180. - atan(Bphi/-Br), 11-13) rms_br, rms_bt, and rms_bn - rms vectors, 14) npts - number of points in average.  All magnetic field observations are measured in nanoTesla. All of the magnetic field data are calibrated (see the instrument calibration description for more details).  These data are provided in a Saturn centered spherical system (L1), based on the Saturn Longitude System (Voyager Measurements of the Rotation Period of Saturn's Magnetic Field, Desch and Kaiser, JGR, 8, 253, 1981).",
-            "title": "VG2 SAT MAG RESAMPLED KRONOGRAPHIC (L1)\n                                     COORDS 9.6SEC V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG2 SAT MAG RESAMPLED KRONOGRAPHIC (L1)\n                                     COORDS 9.6SEC V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-OSIWAC-4-AST1-STEINS-STRLIGHT-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the STEINS FLY-BY mission phase, covering the period  from 2008-08-04T00:00:00.000 to 2008-10-05T23:59:59.000. The prime target is asteroid 2867 Steins. This version V1.0 is the first version of this dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-osiwac-4-ast1-steins-strlight-v1.0_4u69-hvnz",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "vega",
                 "16 cyg b",
                 "2867 steins",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-OSIWAC-4-AST1-STEINS-STRLIGHT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-osiwac-4-ast1-steins-strlight-v1.0_4u69-hvnz",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the STEINS FLY-BY mission phase, covering the period  from 2008-08-04T00:00:00.000 to 2008-10-05T23:59:59.000. The prime target is asteroid 2867 Steins. This version V1.0 is the first version of this dataset.",
-            "title": "ROSETTA-ORBITER STEINS OSIWAC 4 AST1 RDR-STRLIGHT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER STEINS OSIWAC 4 AST1 RDR-STRLIGHT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=FEXP-E-SHYG-3-RDR-OPT-DEP-V1.0",
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
-                "geologic remote sensing field experiment",
-                "earth"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Spectral hygrometer (SHYG) data  were gathered on September 29, 1989 at Lunar Lake. The spectral  hygrometer provided the ratio Rsh=L(935)/L(880), where L(935) is  the radiance at 935 nm. The measurement is acquired by aiming the  optics at the sun. The Spectral Hygrometer data files consist of  data acquired on September 29, 1989. Columns are time in PDT,  ratio of L(935) / L(880) for instrument SH015, time in PDT and  corresponding ratio for instrument SH004.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.fexp-e-shyg-3-rdr-opt-dep-v1.0_4u7f-zw3z",
+            "issued": "2021-05-21",
+            "keyword": [
+                "geologic remote sensing field experiment",
+                "earth"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=FEXP-E-SHYG-3-RDR-OPT-DEP-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.fexp-e-shyg-3-rdr-opt-dep-v1.0_4u7f-zw3z",
-            "description": "Spectral hygrometer (SHYG) data  were gathered on September 29, 1989 at Lunar Lake. The spectral  hygrometer provided the ratio Rsh=L(935)/L(880), where L(935) is  the radiance at 935 nm. The measurement is acquired by aiming the  optics at the sun. The Spectral Hygrometer data files consist of  data acquired on September 29, 1989. Columns are time in PDT,  ratio of L(935) / L(880) for instrument SH015, time in PDT and  corresponding ratio for instrument SH004.",
-            "title": "FIELD EXP E SHYG CALIBRATED RDR \n                                     OPTICAL DEPTH V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "FIELD EXP E SHYG CALIBRATED RDR \n                                     OPTICAL DEPTH V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-D-HRD-3-COHRD-V11.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The High Rate Detector (HRD) from the University of Chicago is an independent part of the CDA instrument on the Cassini Orbiter that measures the dust flux and particle mass distribution of dust particles hitting the HRD detectors. This data set includes all data from the HRD through December 31, 2011. Please refer to Srama et al. (2004) for a detailed HRD description.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-d-hrd-3-cohrd-v11.0_4ubd-hwbc",
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
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-D-HRD-3-COHRD-V11.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-d-hrd-3-cohrd-v11.0_4ubd-hwbc",
-            "description": "The High Rate Detector (HRD) from the University of Chicago is an independent part of the CDA instrument on the Cassini Orbiter that measures the dust flux and particle mass distribution of dust particles hitting the HRD detectors. This data set includes all data from the HRD through December 31, 2011. Please refer to Srama et al. (2004) for a detailed HRD description.",
-            "title": "CASSINI HIGH RATE DETECTOR V11.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI HIGH RATE DETECTOR V11.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-RPCLAP-3-EAR2-CALIB2-V1.0",
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
+            "description": "This data set contains\nCALIBRATED data from Rosetta RPC-LAP, acquired during the EARTH SWING-BY\n2 mission phase where the primary target was the planet EARTH. It\ncontains instrument outputs in volts and amperes, calibrated and\ncorrected for instrument offsets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-rpclap-3-ear2-calib2-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "earth",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-RPCLAP-3-EAR2-CALIB2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-rpclap-3-ear2-calib2-v1.0",
-            "description": "This data set contains\nCALIBRATED data from Rosetta RPC-LAP, acquired during the EARTH SWING-BY\n2 mission phase where the primary target was the planet EARTH. It\ncontains instrument outputs in volts and amperes, calibrated and\ncorrected for instrument offsets.",
-            "title": "ROSETTA-ORBITER EARTH RPCLAP\n3 EAR2 CALIB2 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER EARTH RPCLAP\n3 EAR2 CALIB2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/722",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Myers, J.S. 2004. SAFARI 2000 ER-2 Color-IR Aerial Photography, Dry Season 2000. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/722",
-            "issued": "2023-10-18",
-            "temporal": "2000-08-13T00:00:00Z/2000-09-25T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-24",
-            "keyword": [
-                "spectral/engineering",
-                "earth science",
-                "infrared wavelengths"
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
-            "identifier": "C2788402747-ORNL_CLOUD",
             "description": "Aerial photography from the NASA ER-2 high-altitude aircraft was collected to provide detailed and spatially extensive documentation over parts of the SAFARI study area. The ER-2 aerial photography consists of 3,046 color-infrared (IR) transparencies collected during the SAFARI 2000 Dry Season Aircraft Campaign in August and September of 2000. ORNL DAAC has archived scanned subsets of the ER-2 aerial photography. In addition, 515 image frames have been scanned from copies of the original level-0 ER-2 aerial photography by the University of the Witwatersrand (Wits), in Pretoria, South Africa. ORNL DAAC has archived subsets of the available imagery from ARC and Wits.",
-            "graphic-preview-description": "Browse Image",
-            "title": "SAFARI 2000 ER-2 Color-IR Aerial Photography, Dry Season 2000",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/safari_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F722",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F722",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/remote_sensing/er2_aerial_photos/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/remote_sensing/er2_aerial_photos/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/S2K/guides/er2_aerial_photos.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/S2K/guides/er2_aerial_photos.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/722",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/722",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/er2_aerial_photos/comp/er2_aerial_photos_readme.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/er2_aerial_photos/comp/er2_aerial_photos_readme.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/vnd.ms-excel",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/er2_aerial_photos/comp/inventory_ver1.2.xls",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/er2_aerial_photos/comp/inventory_ver1.2.xls",
+                    "mediaType": "application/vnd.ms-excel",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/er2_aerial_photos/comp/SAFARIv1.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/er2_aerial_photos/comp/SAFARIv1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/er2_aerial_photos/comp/SAFARIV2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/er2_aerial_photos/comp/SAFARIV2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/gzip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/er2_aerial_photos/comp/thumbnails.tar.gz",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/er2_aerial_photos/comp/thumbnails.tar.gz",
+                    "mediaType": "application/gzip",
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
+            "identifier": "C2788402747-ORNL_CLOUD",
+            "issued": "2023-10-18",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "infrared wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/722",
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
             "spatial": "15.0 -30.0 43.0 -12.0",
+            "temporal": "2000-08-13T00:00:00Z/2000-09-25T23:59:59Z",
             "theme": [
                 "SAFARI 2000",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAFARI 2000 ER-2 Color-IR Aerial Photography, Dry Season 2000"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2246",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hulley, G.C., R.J. Freepartner, and S.J. Hook. 2023. SHIFT: HyTES L2 Geolocated Land Surface Temperature and Emissivity, March 23 2022. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2246",
-            "issued": "2023-12-06",
-            "temporal": "2022-03-23T17:14:36Z/2022-03-23T21:58:53Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-12-08",
-            "keyword": [
-                "surface thermal properties",
-                "surface radiative properties",
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
-            "identifier": "C2814122609-ORNL_CLOUD",
             "description": "This dataset holds Level 2 (L2) data for surface emissivity and land surface temperature (LST) collected by the Hyperspectral Thermal Emission Spectrometer (HyTES) instrument. This imagery was acquired as part of the Surface Biology and Geology High-Frequency Time Series (SHIFT) campaign on March 23, 2022. The SHIFT campaign generated precise, high-frequency data on plant communities for nearly 1,656 square kilometers across Santa Barbara County, California, US, and the nearby ocean. HyTES is a compact image spectrometer that acquires data in 256 spectral bands between 7.5 and 12 micrometers; it was deployed on a Twin Otter aircraft. The SHIFT campaign sought to demonstrate the joint use of both VSWIR and thermal infrared (TIR) data. TIR data are used to measure land surface temperature (LST), which informs models of water flux from land surface through processes such as evapotranspiration. LST is sensitive to solar heat gains and local cooling effects due to evaporative cooling. The HyTES instrument measures TIR radiances that can be used to derive LST, emissivity and Level 3 products such as latent heat flux and detection of air pollution sources. The HyTES data are provided in HDF5 format and include 91 flight scenes. In addition, overlay images for emissivity and LST are provided in compressed Keyhole Markup Language (KMZ) along with a quicklook image.",
-            "graphic-preview-description": "Portion of quicklook image of land surface temperature derived from HyTES data collected on 2022-03-23 for the SHIFT campaign. Image shows the coast in the vicinity of Carpinteria, California, east of Santa Barbara (latitude 34.395, longitude -119.525). Source: 20220323t215708_SantaBarbaraCA_L2-LST_B103_V01.png",
-            "title": "SHIFT: HyTES L2 Geolocated Land Surface Temperature and Emissivity, March 23 2022",
-            "graphic-preview-file": "https://daac.ornl.gov/SHIFT/guides/SHIFT_HyTES_L2_2022_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2246",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2246",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/shift/SHIFT_HyTES_L2_2022/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/shift/SHIFT_HyTES_L2_2022/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/SHIFT/guides/SHIFT_HyTES_L2_2022.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/SHIFT/guides/SHIFT_HyTES_L2_2022.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2246",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2246",
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
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/SHIFT/guides/SHIFT_HyTES_L2_2022_Fig1.jpg",
-                    "description": "Portion of quicklook image of land surface temperature derived from HyTES data collected on 2022-03-23 for the SHIFT campaign. Image shows the coast in the vicinity of Carpinteria, California, east of Santa Barbara (latitude 34.395, longitude -119.525). Source: 20220323t215708_SantaBarbaraCA_L2-LST_B103_V01.png",
                     "@type": "dcat:Distribution",
+                    "description": "Portion of quicklook image of land surface temperature derived from HyTES data collected on 2022-03-23 for the SHIFT campaign. Image shows the coast in the vicinity of Carpinteria, California, east of Santa Barbara (latitude 34.395, longitude -119.525). Source: 20220323t215708_SantaBarbaraCA_L2-LST_B103_V01.png",
+                    "downloadURL": "https://daac.ornl.gov/SHIFT/guides/SHIFT_HyTES_L2_2022_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Portion of quicklook image of land surface temperature derived from HyTES data collected on 2022-03-23 for the SHIFT campaign. Image shows the coast in the vicinity of Carpinteria, California, east of Santa Barbara (latitude 34.395, longitude -119.525). Source: 20220323t215708_SantaBarbaraCA_L2-LST_B103_V01.png",
+            "graphic-preview-file": "https://daac.ornl.gov/SHIFT/guides/SHIFT_HyTES_L2_2022_Fig1.jpg",
+            "identifier": "C2814122609-ORNL_CLOUD",
+            "issued": "2023-12-06",
+            "keyword": [
+                "surface thermal properties",
+                "surface radiative properties",
+                "land surface",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2246",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-12-08",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-120.6 34.18 -118.78 34.89",
+            "temporal": "2022-03-23T17:14:36Z/2022-03-23T21:58:53Z",
             "theme": [
                 "SHIFT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SHIFT: HyTES L2 Geolocated Land Surface Temperature and Emissivity, March 23 2022"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/4uhk-uh6p",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "temporal": "1977-01-01/1996-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "geography",
-                "space science",
-                "wise",
-                "nen"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Stefanov",
                 "hasEmail": "mailto:jsc-earthweb@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-0000037__15",
+            "describedBy": "http://www.lpi.usra.edu/resources/gc/gcreadme.html",
             "description": "Planetary nomenclature, like terrestrial nomenclature, is used to uniquely identify a feature on the surface of a planet or satellite so that the feature can be easily located, described, and discussed. This gazetteer contains detailed information about all names of topographic and albedo features on planets and satellites (and some planetary ring and ring-gap systems) that the International Astronomical Union (IAU) has named and approved from its founding in 1919 through the present time.",
-            "title": "Gateway to Astronaut Photography of Earth",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -157546,456 +157528,452 @@
                     "mediaType": "text/html"
                 }
             ],
-            "describedBy": "http://www.lpi.usra.edu/resources/gc/gcreadme.html",
-            "accrualPeriodicity": "irregular"
+            "identifier": "NASA-0000037__15",
+            "issued": "2018-06-25",
+            "keyword": [
+                "geography",
+                "space science",
+                "wise",
+                "nen"
+            ],
+            "landingPage": "https://data.nasa.gov/d/4uhk-uh6p",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "temporal": "1977-01-01/1996-01-01",
+            "title": "Gateway to Astronaut Photography of Earth"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-CAL-CONSERT-3-PDCS-V1.1",
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
+            "description": "This archive contains CALIBRATED data (CODMAC level 3) that refers to target CALIBRATION from the CONSERT instrument onboard ROSETTA Orbiter and Lander, acquired during the PDCS phase. In addition to the scientific signal of interest, it contains all the values applied to the signal for calibration. It also contains documentation which describes the CONSERT experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6. V1.1 of this dataset includes corrections on the data and label files (add missing keywords, correct files name into .txt files, add missing inteference parameters for FSS_RANGING).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-cal-consert-3-pdcs-v1.1",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "calibration"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-CAL-CONSERT-3-PDCS-V1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-cal-consert-3-pdcs-v1.1",
-            "description": "This archive contains CALIBRATED data (CODMAC level 3) that refers to target CALIBRATION from the CONSERT instrument onboard ROSETTA Orbiter and Lander, acquired during the PDCS phase. In addition to the scientific signal of interest, it contains all the values applied to the signal for calibration. It also contains documentation which describes the CONSERT experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6. V1.1 of this dataset includes corrections on the data and label files (add missing keywords, correct files name into .txt files, add missing inteference parameters for FSS_RANGING).",
-            "title": "ROSETTA-ORBITER/ROSETTA-LANDER CAL CONSERT 3 PDCS V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER/ROSETTA-LANDER CAL CONSERT 3 PDCS V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC3-67P-M20-STR-REFL-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units (normalized and thus without unit), acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-08-25T23:25:00.000 to 2015-09-22T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc3-67p-m20-str-refl-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC3-67P-M20-STR-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc3-67p-m20-str-refl-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units (normalized and thus without unit), acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-08-25T23:25:00.000 to 2015-09-22T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC3-MTP020 RDR-STR-REFL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC3-MTP020 RDR-STR-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSINAC-4-CR4A-CHECKOUT-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the CRUISE 4-1 mission phase, covering the period  from 2008-01-28T00:00:00.000 to 2008-08-03T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. This version V1.0 is the first version of this dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osinac-4-cr4a-checkout-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "58 aql",
                 "16 cyg b",
                 "jupiter"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSINAC-4-CR4A-CHECKOUT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osinac-4-cr4a-checkout-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the CRUISE 4-1 mission phase, covering the period  from 2008-01-28T00:00:00.000 to 2008-08-03T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. This version V1.0 is the first version of this dataset.",
-            "title": "ROSETTA-ORBITER CHECKOUT OSINAC 4 CR4A RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECKOUT OSINAC 4 CR4A RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1274625674-GES_DISC.html",
             "citation": "Goddard Laboratory for Atmospheres at NASA/GSFC. 1995-01-01. TOVSB5NG. Version 01. TOVS LMD 5 DAY GRIDS from NOAA-10 V01. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/TOVSB5NG_01.html. Digital Science Data.",
-            "issued": "1986-12-31",
-            "temporal": "1986-12-31T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "1991-09-03",
-            "keyword": [
-                "atmospheric chemistry",
-                "atmosphere",
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "clouds",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "THOMAS HEARTY",
                 "hasEmail": "mailto:Thomas.J.Hearty@nasa.gov"
             },
+            "creator": "Goddard Laboratory for Atmospheres at NASA/GSFC",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1274625674-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Level 3 parameters from HIRS/2 and MSU radiances using the Improved Initialization Inversion (3I) classification retrieval scheme by the Laboratoire de  Meteorologie Dynamique (Ecole Polytechnique) averaged over 5 days and mapped on to a 1x1 degree grid. This data was run as part of the NASA TOVS Pathfinder project and designated as Path-B. This dataset contains data from the NOAA-10 satellite.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TOVSB5NG",
-            "creator": "Goddard Laboratory for Atmospheres at NASA/GSFC",
-            "title": "TOVS LMD 5 DAY GRIDS from NOAA-10 V01 (TOVSB5NG) at GES DISC",
-            "graphic-preview-description": "TOVSB5NG image",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOVSB5NG_01.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOVSB5NG_01.png",
-                    "description": "TOVSB5NG image",
                     "@type": "dcat:Distribution",
+                    "description": "TOVSB5NG image",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOVSB5NG_01.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TOVSB5NG_01.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TOVSB5NG_01.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc1.gesdisc.eosdis.nasa.gov/data/tovs/TOVSB5NG/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://disc1.gesdisc.eosdis.nasa.gov/data/tovs/TOVSB5NG/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TOVSB5NG+001",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TOVSB5NG+001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc1.gesdisc.eosdis.nasa.gov/data/tovs/TOVSB5NG/doc/README.TOVSPathB.txt",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://disc1.gesdisc.eosdis.nasa.gov/data/tovs/TOVSB5NG/doc/README.TOVSPathB.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 }
             ],
+            "graphic-preview-description": "TOVSB5NG image",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOVSB5NG_01.png",
+            "identifier": "C1274625674-GES_DISC",
+            "issued": "1986-12-31",
+            "keyword": [
+                "atmospheric chemistry",
+                "atmosphere",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "clouds",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1274625674-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1991-09-03",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "TOVSB5NG",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1986-12-31T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "CWIC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TOVS LMD 5 DAY GRIDS from NOAA-10 V01 (TOVSB5NG) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1237207603-LARC_ASDC.html",
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
-            "identifier": "C1237207603-LARC_ASDC",
             "description": "CER_GEO_Ed4_GOE11_NH_V01 is the Satellite Cloud and Radiation Property retrieval System (SatCORPS) Clouds and the Earth's Radiant Energy System (CERES) Geostationary Satellite (GEO) Edition 4 Geostationary Operational Environmental Satellite 11 (GOES-11) over the Northern Hemisphere (NH) Version 1.0 data product. Data was collected using the GOES-11 Imager on the GOES-11 Platform. Data collection for this product is complete. \r\n\r\nThis data set comprises cloud micro-physical and radiation properties derived hourly from GOES-11 geostationary satellite imager data using the Langley Research Center (LaRC) SATCORPS algorithms supporting the CERES project. The cloud micro-physical and radiation properties from each active geostationary satellite are merged to create hourly global cloud properties that estimate fluxes between CERES instrument measurements to account for the changing diurnal cycle. The data set is arranged as files for each hour and in netCDF-4 format. The observations are at 4 km resolution (at nadir) and are sub-sampled to 8 km.\r\n\r\nCERES is a key Earth Observing System (EOS) program component. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions follow the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument, the protoflight model (PFM), was launched on November 27, 1997, as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the Earth Observing System (EOS) flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board Earth Observing System (EOS) Aqua on May 4, 2002. The CERES FM5 instrument was launched on board the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The newest CERES instrument (FM6) was launched on board the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite, now called NOAA-20, on November 18, 2017.",
-            "graphic-preview-description": "Mission Logo",
-            "title": "SatCORPS CERES GEO Edition 4 GOES-11 Northern Hemisphere Version 1.0",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1237207603-LARC_ASDC",
-                    "description": "Earthdata Search for CER_GEO_Ed4_GOE11_NH_V01 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CER_GEO_Ed4_GOE11_NH_V01 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1237207603-LARC_ASDC",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
-                    "description": "ASDC's data citation policy",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC's data citation policy",
+                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data citation policy"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/GEO/Edition4/GOE11_NH_V01/",
-                    "description": "ASDC Direct Data Download for CER_GEO_Ed4_GOE11_NH_V01",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CER_GEO_Ed4_GOE11_NH_V01",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/GEO/Edition4/GOE11_NH_V01/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/GEO/Edition4/GOE11_NH_V01/contents.html",
-                    "description": "OPeNDAP data access for CER_GEO_Ed4_GOE11_NH_V01",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CER_GEO_Ed4_GOE11_NH_V01",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/GEO/Edition4/GOE11_NH_V01/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Mission Logo",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/ceres.png",
+            "identifier": "C1237207603-LARC_ASDC",
+            "issued": "2015-08-08",
+            "keyword": [
+                "atmosphere",
+                "clouds",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1237207603-LARC_ASDC.html",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>0.0 -180.0 0.0 -91.0 60.0 -91.0 60.0 -180.0 0.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2006-06-21T00:00:00Z/2011-12-06T23:59:59.999Z",
             "theme": [
                 "CERES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SatCORPS CERES GEO Edition 4 GOES-11 Northern Hemisphere Version 1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1273652159-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Goddard Space Flight Center (GSFC). THIRN4IMCH67. Version 001. THIR/Nimbus-4 Images of Daytime and Nighttime Brightness Temperature at 6.7 microns on 70 mm Film V001. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/THIRN4IMCH67_001.html. Digital Science Data.",
-            "issued": "2011-06-15",
-            "temporal": "1970-05-23T00:00:00Z/1970-06-06T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2011-06-15",
-            "keyword": [
-                "spectral/engineering",
-                "earth science",
-                "infrared wavelengths"
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
-            "identifier": "C1273652159-GES_DISC",
-            "description": "THIRN4IMCH67 is the Nimbus-4 Temperature-Humidity Infrared Radiometer (THIR) data product consisting of daily montages of brightness temperatures measured at 6.7 microns on 70 mm photofacsimile film strips. Daytime and nighttime orbital swaths are displayed in strips, each corresponding to a distance approximately from pole to pole and a width from horizon to horizon. The ground resolution of 22.6 km at nadir decreases as the horizontal distance from the subsatellite track increases. Each film strip is gridded with geographic coordinates and is identified by orbit number, time, and an indication of whether it is daytime (D) or nighttime (N). The images are saved as JPEG 2000 digital files. About 1 week of images are archived into a TAR file. Additional information can be found in section 3.4.1 of \"The Nimbus IV User's Guide\".\n\nThe THIR instrument was designed to detect emitted thermal radiation in both the 10.5- to 12.5-micrometer region (IR window) and the 6.5- to 7.0-micrometer region (water vapor). The window channel measured cloudtop temperatures day and night. The other channel operated primarily at night to map the water vapor distribution in the upper troposphere and stratosphere. The THIR experiment made measurements from April 18, 1970 until April 8, 1971.\n\nThis product was previously available from the NSSDC with the identifier ESAD-00194 (old ID 70-025A-02B).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "THIRN4IMCH67",
             "creator": "Goddard Space Flight Center (GSFC)",
-            "title": "THIR/Nimbus-4 Images of Daytime and Nighttime Brightness Temperature at 6.7 microns on 70 mm Film V001 (THIRN4IMCH67) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/THIRN4IMCH67_001.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "THIRN4IMCH67 is the Nimbus-4 Temperature-Humidity Infrared Radiometer (THIR) data product consisting of daily montages of brightness temperatures measured at 6.7 microns on 70 mm photofacsimile film strips. Daytime and nighttime orbital swaths are displayed in strips, each corresponding to a distance approximately from pole to pole and a width from horizon to horizon. The ground resolution of 22.6 km at nadir decreases as the horizontal distance from the subsatellite track increases. Each film strip is gridded with geographic coordinates and is identified by orbit number, time, and an indication of whether it is daytime (D) or nighttime (N). The images are saved as JPEG 2000 digital files. About 1 week of images are archived into a TAR file. Additional information can be found in section 3.4.1 of \"The Nimbus IV User's Guide\".\n\nThe THIR instrument was designed to detect emitted thermal radiation in both the 10.5- to 12.5-micrometer region (IR window) and the 6.5- to 7.0-micrometer region (water vapor). The window channel measured cloudtop temperatures day and night. The other channel operated primarily at night to map the water vapor distribution in the upper troposphere and stratosphere. The THIR experiment made measurements from April 18, 1970 until April 8, 1971.\n\nThis product was previously available from the NSSDC with the identifier ESAD-00194 (old ID 70-025A-02B).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -158004,1352 +157982,1348 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/THIRN4IMCH67_001.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/THIRN4IMCH67_001.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus4_THIR_Level2/THIRN4IMCH67.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
-                    "title": "Download this dataset through a directory map"
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus4_THIR_Level2/THIRN4IMCH67.001/",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=THIRN4IMCH67",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=THIRN4IMCH67",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus4_THIR_Level1/THIRN4IMCH67.001/doc/README.THIRN4L1.001.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus4_THIR_Level1/THIRN4IMCH67.001/doc/README.THIRN4L1.001.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/NimbusIVUG.pdf",
-                    "description": "Nimbus 4 User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Nimbus 4 User's Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/NimbusIVUG.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
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
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/THIRN4IMCH67_001.png",
+            "identifier": "C1273652159-GES_DISC",
+            "issued": "2011-06-15",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "infrared wavelengths"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1273652159-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2011-06-15",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "THIRN4IMCH67",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1970-05-23T00:00:00Z/1970-06-06T23:59:59.999Z",
             "theme": [
                 "Nimbus",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "THIR/Nimbus-4 Images of Daytime and Nighttime Brightness Temperature at 6.7 microns on 70 mm Film V001 (THIRN4IMCH67) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-EXT2-MTP030-V1.0",
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
+            "description": "This data set contains\nEDITED data from Rosetta RPC-LAP, acquired during the ROSETTA\nEXTENSION 2 MTP030 mission phase. Comet C-G/67P was the primary target.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-ext2-mtp030-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-EXT2-MTP030-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-ext2-mtp030-v1.0",
-            "description": "This data set contains\nEDITED data from Rosetta RPC-LAP, acquired during the ROSETTA\nEXTENSION 2 MTP030 mission phase. Comet C-G/67P was the primary target.",
-            "title": "ROSETTA-ORBITER 67P RPCLAP 2\nEXT2 MTP030 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCLAP 2\nEXT2 MTP030 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/577/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2012-05-11",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "nasa",
-                "ames"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "WILLIAM STEVENS",
                 "hasEmail": "mailto:william.l.stevens@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_577",
             "description": "Downloadable Presentation Recordings",
-            "title": "Video Recordings in WMV Format",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "video/x-ms-wmv",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Coen_Schmidt_20120418080258.wmv",
-                    "description": "Greeting and Interaction Between ASE & Simulation - Peter Coen & Dr. David K. Schmidt",
                     "@type": "dcat:Distribution",
+                    "description": "Greeting and Interaction Between ASE & Simulation - Peter Coen & Dr. David K. Schmidt",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Coen_Schmidt_20120418080258.wmv",
+                    "mediaType": "video/x-ms-wmv",
                     "title": "Coen_Schmidt_20120418080258.wmv"
                 },
                 {
-                    "mediaType": "video/x-ms-wmv",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Silva_20120418094402.wmv",
-                    "description": "Aeroservoelasticity and Reduced Order Models - Walt Silva - NASA Langley",
                     "@type": "dcat:Distribution",
+                    "description": "Aeroservoelasticity and Reduced Order Models - Walt Silva - NASA Langley",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Silva_20120418094402.wmv",
+                    "mediaType": "video/x-ms-wmv",
                     "title": "Silva_20120418094402.wmv"
                 },
                 {
-                    "mediaType": "video/x-ms-wmv",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Raney_20120418110411.wmv",
-                    "description": "Sim Study of Impact of ASE on Flying Qualities of a High Speed Civil Transport (HSCT) - Dave Raney - NASA Langley ",
                     "@type": "dcat:Distribution",
+                    "description": "Sim Study of Impact of ASE on Flying Qualities of a High Speed Civil Transport (HSCT) - Dave Raney - NASA Langley ",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Raney_20120418110411.wmv",
+                    "mediaType": "video/x-ms-wmv",
                     "title": "Raney_20120418110411.wmv"
                 },
                 {
-                    "mediaType": "video/x-ms-wmv",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Cowen_20120418130055.wmv",
-                    "description": "Structural Modes and Aircraft Handling Qualities - Brandon Cowen - Adaptive Aerospace Group",
                     "@type": "dcat:Distribution",
+                    "description": "Structural Modes and Aircraft Handling Qualities - Brandon Cowen - Adaptive Aerospace Group",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Cowen_20120418130055.wmv",
+                    "mediaType": "video/x-ms-wmv",
                     "title": "Cowen_20120418130055.wmv"
                 },
                 {
-                    "mediaType": "video/x-ms-wmv",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Ohme_20120418134645.wmv",
-                    "description": "System ID of Flexible Aircraft - Per Ohme - German Aerospace Center",
                     "@type": "dcat:Distribution",
+                    "description": "System ID of Flexible Aircraft - Per Ohme - German Aerospace Center",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Ohme_20120418134645.wmv",
+                    "mediaType": "video/x-ms-wmv",
                     "title": "Ohme_20120418134645.wmv"
                 },
                 {
-                    "mediaType": "video/x-ms-wmv",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Chen_20120418153411.wmv",
-                    "description": "Dynamic Flight Simulation (DFS) for MAD/MUTT - P. C. Chen - Zonatech",
                     "@type": "dcat:Distribution",
+                    "description": "Dynamic Flight Simulation (DFS) for MAD/MUTT - P. C. Chen - Zonatech",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Chen_20120418153411.wmv",
+                    "mediaType": "video/x-ms-wmv",
                     "title": "Chen_20120418153411.wmv"
                 },
                 {
-                    "mediaType": "video/x-ms-wmv",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Heim_20120419080024.wmv",
-                    "description": "Ares 1-X - Eugene Heim - NASA Langley",
                     "@type": "dcat:Distribution",
+                    "description": "Ares 1-X - Eugene Heim - NASA Langley",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Heim_20120419080024.wmv",
+                    "mediaType": "video/x-ms-wmv",
                     "title": "Heim_20120419080024.wmv"
                 },
                 {
-                    "mediaType": "video/x-ms-wmv",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Lindsley_20120419084507.wmv",
-                    "description": "Stick-to-Stress Real-Time Simulator - Dr. Ned Lindsley - Air Force Research Laboratory",
                     "@type": "dcat:Distribution",
+                    "description": "Stick-to-Stress Real-Time Simulator - Dr. Ned Lindsley - Air Force Research Laboratory",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Lindsley_20120419084507.wmv",
+                    "mediaType": "video/x-ms-wmv",
                     "title": "Lindsley_20120419084507.wmv"
                 },
                 {
-                    "mediaType": "video/x-ms-wmv",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Discussion_20120419100419.wmv",
-                    "description": "Discussion",
                     "@type": "dcat:Distribution",
+                    "description": "Discussion",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Discussion_20120419100419.wmv",
+                    "mediaType": "video/x-ms-wmv",
                     "title": "Discussion_20120419100419.wmv"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_577",
+            "issued": "2012-05-11",
+            "keyword": [
+                "dashlink",
+                "nasa",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/577/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Video Recordings in WMV Format"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GNSS/GNSS_HIGHRATE_N_001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "International GNSS Service, High-rate GPS broadcast ephemeris data, Greenbelt, MD, USA: NASA Crustal Dynamics Data Information System (CDDIS), Accessed [[enter user data access date]] at doi:10.5067/GNSS/gnss_highrate_n_001",
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
-            "identifier": "C1422110518-CDDIS",
             "description": "This dataset consists of ground-based Global Navigation Satellite System (GNSS) GPS Broadcast Ephemeris Data (sub-hourly files) from the NASA Crustal Dynamics Data Information System (CDDIS). GNSS provide autonomous geo-spatial positioning with global coverage. GNSS data sets from ground receivers at the CDDIS consist primarily of the data from the U.S. Global Positioning System (GPS) and the Russian GLObal NAvigation Satellite System (GLONASS). Since 2011, the CDDIS GNSS archive includes data from other GNSS (Europe\u2019s Galileo, China\u2019s Beidou, Japan\u2019s Quasi-Zenith Satellite System/QZSS, the Indian Regional Navigation Satellite System/IRNSS, and worldwide Satellite Based Augmentation Systems/SBASs), which are similar to the U.S. GPS in terms of the satellite constellation, orbits, and signal structure. The sub-hourly GPS broadcast ephemeris files contain 15 minutes of GPS broadcast navigation data in RINEX format from a global permanent network of ground-based receivers, one file per 15 minutes per site. More information about these data is available on the CDDIS website at https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/high-rate_data.html.",
-            "title": "Ground-Based Global Navigation Satellite System (GNSS) GPS Broadcast Ephemeris Data (sub-hourly files) from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGNSS_HIGHRATE_N_001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGNSS_HIGHRATE_N_001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/archive/gnss/data/highrate",
-                    "description": "URL for retrieval of GNSS sub-hourly data through https",
                     "@type": "dcat:Distribution",
+                    "description": "URL for retrieval of GNSS sub-hourly data through https",
+                    "downloadURL": "https://cddis.nasa.gov/archive/gnss/data/highrate",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/broadcast_ephemeris_data.html",
-                    "description": "URL for more information about GNSS sub-hourly GPS broadcast navigation data",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about GNSS sub-hourly GPS broadcast navigation data",
+                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/broadcast_ephemeris_data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/GNSS/GNSS_HIGHRATE_N_001",
-                    "description": "URL for more information about GNSS sub-hourly GPS broadcast navigation data",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about GNSS sub-hourly GPS broadcast navigation data",
+                    "downloadURL": "https://doi.org/10.5067/GNSS/GNSS_HIGHRATE_N_001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1422110518-CDDIS",
+            "issued": "1992-01-01",
+            "keyword": [
+                "earth science",
+                "solid earth",
+                "geodetics",
+                "gravity/gravitational field",
+                "tectonics"
+            ],
+            "landingPage": "https://doi.org/10.5067/GNSS/GNSS_HIGHRATE_N_001",
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
+            "title": "Ground-Based Global Navigation Satellite System (GNSS) GPS Broadcast Ephemeris Data (sub-hourly files) from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LP-L-MAG-5-LUNAR-FIELD-BINS-V1.0",
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
-                "lunar prospector"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lp-l-mag-5-lunar-field-bins-v1.0_4uwf-xkns",
+            "issued": "2018-06-26",
+            "keyword": [
+                "moon",
+                "lunar prospector"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LP-L-MAG-5-LUNAR-FIELD-BINS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lp-l-mag-5-lunar-field-bins-v1.0_4uwf-xkns",
-            "description": "not applicable",
-            "title": "LP MOON MAG LEVEL 5 LUNAR MAGNETIC FIELD BINS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "LP MOON MAG LEVEL 5 LUNAR MAGNETIC FIELD BINS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/2E096JV59PK7",
             "citation": "Global Modeling and Assimilation Office (GMAO). 2015-06-30. M2IMNPASM. Version 5.12.4. MERRA-2 instM_3d_asm_Np: 3d,Monthly mean,Instantaneous,Pressure-Level,Assimilation,Assimilated Meteorological Fields V5.12.4. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/2E096JV59PK7. https://disc.gsfc.nasa.gov/datacollection/M2IMNPASM_5.12.4.html. Digital Science Data.",
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
-                "atmospheric pressure",
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "atmospheric winds",
-                "clouds",
-                "altitude",
-                "atmosphere",
-                "atmospheric chemistry"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DANA OSTRENGA",
                 "hasEmail": "mailto:dana.ostrenga@nasa.gov"
             },
+            "creator": "Global Modeling and Assimilation Office (GMAO)",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1276812904-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "M2IMNPASM (or  instM_3d_asm_Np) is an instantaneous 3-dimensional monthly mean data collection in Modern-Era Retrospective analysis for Research and Applications version 2 (MERRA-2).  This collection consists of assimilations of meteorological parameters at 42 pressure levels, such as  temperature, wind components, vertical pressure velocity, water vapor, ozone mass mixing ratio, and layer height. The information on the pressure levels can be found in the section 4.2 of the MERRA-2 File Specification document.  The collection also includes certain quadratic information (such as the variance and covariance of certain parameters).\n\nMERRA-2 is the latest version of global atmospheric reanalysis for the satellite era produced by NASA Global Modeling and Assimilation Office (GMAO) using the Goddard Earth Observing System Model (GEOS) version 5.12.4.  The dataset covers the period of 1980-present with the latency of ~3 weeks after the end of a month. \n\nData Reprocessing:  Please check \u201cRecords of MERRA-2 Data Reprocessing and Service Changes\u201d linked from the \u201cDocumentation\u201d tab on this page.  Note that a reprocessed data filename is different from the original file.\n\nMERRA-2 Mailing List: Sign up to receive information on reprocessing of data, changing of tools and services, as well as data announcements from GMAO. Contact the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov) to be added to the list.\n\nQuestions: If you have a question, please read \"MERRA-2 File Specification Document\",  \u201cMERRA-2 Data Access \u2013 Quick Start Guide\u201d, and FAQs linked from the \u201dDocumentation\u201d tab on this page.  If that does not answer your question, you may email the question on data access to the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov), or the question on science to the MERRA-2 science team (merra-questions@lists.nasa.gov).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "M2IMNPASM",
-            "creator": "Global Modeling and Assimilation Office (GMAO)",
-            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
-            "title": "MERRA-2 instM_3d_asm_Np: 3d,Monthly mean,Instantaneous,Pressure-Level,Assimilation,Assimilated Meteorological Fields 0.625 x 0.5 degree V5.12.4 (M2IMNPASM) at GES DISC",
-            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=M2IMNPASM",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F2E096JV59PK7",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F2E096JV59PK7",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2IMNPASM_5.12.4.png",
-                    "description": "M2IMNPASM variable",
                     "@type": "dcat:Distribution",
+                    "description": "M2IMNPASM variable",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2IMNPASM_5.12.4.png",
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
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2IMNPASM_5.12.4.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2IMNPASM_5.12.4.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2_MONTHLY/M2IMNPASM.5.12.4/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2_MONTHLY/M2IMNPASM.5.12.4/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=M2IMNPASM",
-                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
                     "@type": "dcat:Distribution",
+                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=M2IMNPASM",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through GIOVANNI"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2IMNPASM",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2IMNPASM",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/dods/M2IMNPASM.info",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/dods/M2IMNPASM.info",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/opendap/MERRA2_MONTHLY/M2IMNPASM.5.12.4/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/opendap/MERRA2_MONTHLY/M2IMNPASM.5.12.4/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_MONTHLY_aggregation/catalog.html?dataset=merra2_monthly_aggregation%2FM2IMNPASM.5.12.4_Aggregation.ncml",
-                    "description": "Time aggregated THREDDS Data Server (TDS) ",
                     "@type": "dcat:Distribution",
+                    "description": "Time aggregated THREDDS Data Server (TDS) ",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_MONTHLY_aggregation/catalog.html?dataset=merra2_monthly_aggregation%2FM2IMNPASM.5.12.4_Aggregation.ncml",
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
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2_MONTHLY/M2IMNPASM.5.12.4/doc/MERRA2.README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2_MONTHLY/M2IMNPASM.5.12.4/doc/MERRA2.README.pdf",
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
+            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=M2IMNPASM",
+            "identifier": "C1276812904-GES_DISC",
+            "issued": "2007-06-14",
+            "keyword": [
+                "earth science",
+                "atmospheric pressure",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "atmospheric winds",
+                "clouds",
+                "altitude",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/2E096JV59PK7",
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
+            "series-name": "M2IMNPASM",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1980-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "MERRA-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MERRA-2 instM_3d_asm_Np: 3d,Monthly mean,Instantaneous,Pressure-Level,Assimilation,Assimilated Meteorological Fields 0.625 x 0.5 degree V5.12.4 (M2IMNPASM) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/3XE38KNUZX0A",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "CLPX-Ground: ISA Soil Moisture Measurements, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/3XE38KNUZX0A.",
-            "issued": "2001-09-01",
-            "temporal": "2001-09-01T00:00:00Z/2003-04-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2003-04-30",
-            "keyword": [
-                "earth science",
-                "soils",
-                "land surface"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kelly Elder",
                 "hasEmail": "mailto:kelder@fs.fed.us"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1386250228-NSIDCV0",
             "description": "This data set consists of in-situ point measurements of soil moisture within three 25-km by 25-km Meso-cell Study Areas (MSAs) in northern Colorado (Fraser, North Park , and Rabbit Ears).",
-            "title": "CLPX-Ground: ISA Soil Moisture Measurements, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F3XE38KNUZX0A",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F3XE38KNUZX0A",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/CLP/data/ground_data/nsidc0178_soil_moisture/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/CLP/data/ground_data/nsidc0178_soil_moisture/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/CLP/data/ground_data/nsidc0178_soil_moisture/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/CLP/data/ground_data/nsidc0178_soil_moisture/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/3XE38KNUZX0A",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/3XE38KNUZX0A",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/3XE38KNUZX0A",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/3XE38KNUZX0A",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386250228-NSIDCV0",
+            "issued": "2001-09-01",
+            "keyword": [
+                "earth science",
+                "soils",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/3XE38KNUZX0A",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2003-04-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-106.4 40.625 -106.15 40.8",
+            "temporal": "2001-09-01T00:00:00Z/2003-04-30T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CLPX-Ground: ISA Soil Moisture Measurements, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-3-PRL-MTP005-V1.0",
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
+            "description": "This dataset contains ROSETTA NAVCAM RADIOMETRICALLY CALIBRATED DATA of the PRELANDING MTP005 Phase from 03 Jul. 2014, 09:00:01 to 01 Aug. 2014, 09:53:18 when at the vicinity of target 67P/CG.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-3-prl-mtp005-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-3-PRL-MTP005-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-3-prl-mtp005-v1.0",
-            "description": "This dataset contains ROSETTA NAVCAM RADIOMETRICALLY CALIBRATED DATA of the PRELANDING MTP005 Phase from 03 Jul. 2014, 09:00:01 to 01 Aug. 2014, 09:53:18 when at the vicinity of target 67P/CG.",
-            "title": "ROSETTA-ORBITER 67P NAVCAM 3 PRELANDING MTP005 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P NAVCAM 3 PRELANDING MTP005 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1148-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-01T08:32:30.000 to 2015-11-01T17:11:56.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1148-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1148-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1148-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-01T08:32:30.000 to 2015-11-01T17:11:56.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1148 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1148 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/166",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hall, F. G., K. F. Huemmrich, D. E. Strebel, S. J. Goetz, J. E. Nickeson, and K. D. Woods. 1996. NWS Daily Climatology Data: 1979 (SNF). [National Weather Service Daily Climatology Data: 1979 (Superior National Forest)]. Data set. Available on-line [http://www.daac.ornl.gov] from Oak Ridge National Laboratory Distributed Active Archive Center, Oak Ridge, Tennessee, U.S.A. Based on F. G. Hall, K. F. Huemmrich, D. E. Strebel, S. J. Goetz, J. E. Nickeson, and K. D. Woods, Biophysical, Morphological, Canopy Optical Property, and Productivity Data from the Superior National Forest, NASA Technical Memorandum 104568, National Aeronautics and Space Administration, Goddard Space Flight Center, Greenbelt, Maryland, U.S.A., 1992. doi:10.3334/ORNLDAAC/166",
-            "issued": "2024-03-01",
-            "temporal": "1979-01-01T00:00:00Z/1979-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-04",
-            "keyword": [
-                "atmospheric temperature",
-                "precipitation",
-                "atmospheric radiation",
-                "atmosphere",
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
-            "identifier": "C2884977417-ORNL_CLOUD",
             "description": "Daily min, max, average temperature (F), precipitation (water equivalent in inches), and daily insolation (Langleys) for the Superior National Forest area as collected by NWS and U. of Minnesota",
-            "graphic-preview-description": "Browse Image",
-            "title": "NWS Daily Climatology Data: 1979 (SNF)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/snf_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F166",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F166",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/snf/SNF_MET_1979/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/snf/SNF_MET_1979/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/SNF/guides//nws_daily_climate_1979.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/SNF/guides//nws_daily_climate_1979.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/166",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/166",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1979/comp/met_1979.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1979/comp/met_1979.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1979/comp/met_1979.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1979/comp/met_1979.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1979/comp/nws_daily_climate_1979.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1979/comp/nws_daily_climate_1979.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1979/comp/nws_daily_climate_1979.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1979/comp/nws_daily_climate_1979.txt",
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
+            "identifier": "C2884977417-ORNL_CLOUD",
+            "issued": "2024-03-01",
+            "keyword": [
+                "atmospheric temperature",
+                "precipitation",
+                "atmospheric radiation",
+                "atmosphere",
+                "atmospheric water vapor",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/166",
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
+            "temporal": "1979-01-01T00:00:00Z/1979-12-31T23:59:59Z",
             "theme": [
                 "SNF",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NWS Daily Climatology Data: 1979 (SNF)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/439/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2011-07-18",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "nasa",
-                "dashlink",
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
-            "identifier": "DASHLINK_439",
             "description": "This is the RSW Fully tetrahedral medium cell-centered unstructured grid with a viscous wall.\r\n\r\nUG3      : Grid File Name    = rsw_med_tetcc.b8.ugrid\r\nUG3      : Quad Surface Faces=         0\r\nUG3      : Tria Surface Faces=    133698\r\nUG3      : Nodes             =   3823266\r\nUG3      : Total Elements    =  22726678\r\nUG3      : Hex Elements      =         0\r\nUG3      : Pent_5 Elements   =         0\r\nUG3      : Pent_6 Elements   =         0\r\nUG3      : Tet Elements      =  22726678\r\nUG3      : BL Tet Elements   =  21106651",
-            "title": "RSW Fully Tet Medium Cell-Centered Mesh",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_med_tetcc.b8.ugrid",
-                    "description": "ugrid file",
                     "@type": "dcat:Distribution",
+                    "description": "ugrid file",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_med_tetcc.b8.ugrid",
+                    "mediaType": "application/octet-stream",
                     "title": "rsw_med_tetcc.b8.ugrid"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_med_tetcc.cgns",
-                    "description": "CGNS Format Grid File",
                     "@type": "dcat:Distribution",
+                    "description": "CGNS Format Grid File",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_med_tetcc.cgns",
+                    "mediaType": "application/octet-stream",
                     "title": "rsw_med_tetcc.cgns"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_med_tetcc.info",
-                    "description": "Grid Information",
                     "@type": "dcat:Distribution",
+                    "description": "Grid Information",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_med_tetcc.info",
+                    "mediaType": "application/octet-stream",
                     "title": "rsw_med_tetcc.info"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_med_tetcc.mapbc",
-                    "description": "Mapbc file (FUN3D)",
                     "@type": "dcat:Distribution",
+                    "description": "Mapbc file (FUN3D)",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_med_tetcc.mapbc",
+                    "mediaType": "application/octet-stream",
                     "title": "rsw_med_tetcc.mapbc"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_med_tetcc.surf.gz",
-                    "description": "surface grid (gzipped)",
                     "@type": "dcat:Distribution",
+                    "description": "surface grid (gzipped)",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_med_tetcc.surf.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "rsw_med_tetcc.surf.gz"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_med_tetcc.tags",
-                    "description": "tag file",
                     "@type": "dcat:Distribution",
+                    "description": "tag file",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_med_tetcc.tags",
+                    "mediaType": "application/octet-stream",
                     "title": "rsw_med_tetcc.tags"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_439",
+            "issued": "2011-07-18",
+            "keyword": [
+                "nasa",
+                "dashlink",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/439/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "RSW Fully Tet Medium Cell-Centered Mesh"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-OSIWAC-4-AST1-STEINS-REFLECT-V1.0",
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
-                "2867 steins",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled)  image data in reflectance units (normalized and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the STEINS FLY-BY mission phase, covering the period  from 2008-08-04T00:00:00.000 to 2008-10-05T23:59:59.000. The prime target is asteroid 2867 Steins. This version V1.0 is the first version of this dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-osiwac-4-ast1-steins-reflect-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "2867 steins",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-OSIWAC-4-AST1-STEINS-REFLECT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-osiwac-4-ast1-steins-reflect-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled)  image data in reflectance units (normalized and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the STEINS FLY-BY mission phase, covering the period  from 2008-08-04T00:00:00.000 to 2008-10-05T23:59:59.000. The prime target is asteroid 2867 Steins. This version V1.0 is the first version of this dataset.",
-            "title": "ROSETTA-ORBITER STEINS OSIWAC 4 AST1 RDR-REFLECT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER STEINS OSIWAC 4 AST1 RDR-REFLECT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2331331878-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC.",
-            "issued": "2019-06-23",
-            "temporal": "2002-07-04T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-10-01",
-            "keyword": [
-                "ocean optics",
-                "ngda",
-                "national geospatial data asset",
-                "aerosols",
-                "earth science",
-                "oceans",
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
-            "identifier": "C2331331878-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "Aqua MODIS Global Binned Remote-Sensing Reflectance (RRS) - NRT Data, version R2022.0",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/AQUA/MODIS/L3B/RRS/2022",
-                    "description": "MODIS-Aqua L3B Remote-Sensing Reflectance (RRS) - NRT Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS-Aqua L3B Remote-Sensing Reflectance (RRS) - NRT Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/AQUA/MODIS/L3B/RRS/2022",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2331331878-OB_DAAC",
+            "issued": "2019-06-23",
+            "keyword": [
+                "ocean optics",
+                "ngda",
+                "national geospatial data asset",
+                "aerosols",
+                "earth science",
+                "oceans",
+                "atmosphere"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2331331878-OB_DAAC.html",
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
+            "title": "Aqua MODIS Global Binned Remote-Sensing Reflectance (RRS) - NRT Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-C-MRI-2-EPOXI-HARTLEY2-V1.0",
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
+            "description": "This dataset contains raw images of comet 103/P Hartley 2 acquired by the Medium Resolution Visible CCD (MRI) from 05 September through 26 November 2010 during the Hartley 2 encounter phase of the EPOXI mission. Clear-filter and CN images of the comet were acquired throughout this phase; OH, C2, and dust continuum images were only acquired for several days spanning closest approach.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-c-mri-2-epoxi-hartley2-v1.0_4v8k-9dab",
+            "issued": "2021-05-21",
+            "keyword": [
+                "epoxi",
+                "103p/hartley 2 (1986 e2)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-C-MRI-2-EPOXI-HARTLEY2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-c-mri-2-epoxi-hartley2-v1.0_4v8k-9dab",
-            "description": "This dataset contains raw images of comet 103/P Hartley 2 acquired by the Medium Resolution Visible CCD (MRI) from 05 September through 26 November 2010 during the Hartley 2 encounter phase of the EPOXI mission. Clear-filter and CN images of the comet were acquired throughout this phase; OH, C2, and dust continuum images were only acquired for several days spanning closest approach.",
-            "title": "EPOXI 103P/HARTLEY2 ENCOUNTER - MRI RAW IMAGES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "EPOXI 103P/HARTLEY2 ENCOUNTER - MRI RAW IMAGES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGN-V-RSS-5-LOSAPDR-L2-V1.0",
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
+            "description": "Line of Sight Acceleration Profile Data Records (LOSAPDR) consist of data from Doppler tracking of the orbiting spacecraft. The relative motion of the spacecraft and the earth-based radio receiver is measured very precisely, and known motions are removed a priori (i.e. earth rotation, planetary motions, spacecraft orbital motion, solar pressure, drag), leaving small velocity changes caused by variations in the mass distribution of the planet. The residual Doppler frequency shifts are linearly proportional to the component of velocity in the Earth direction. Numerical differentiation of these velocity residuals with respect to time produces line-of-sight (LOS) gravity. These measures are accelerations at spacecraft altitude which can be modeled for geophysical interpretation.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgn-v-rss-5-losapdr-l2-v1.0_4v9p-n2y9",
+            "issued": "2021-05-21",
+            "keyword": [
+                "magellan",
+                "venus"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGN-V-RSS-5-LOSAPDR-L2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgn-v-rss-5-losapdr-l2-v1.0_4v9p-n2y9",
-            "description": "Line of Sight Acceleration Profile Data Records (LOSAPDR) consist of data from Doppler tracking of the orbiting spacecraft. The relative motion of the spacecraft and the earth-based radio receiver is measured very precisely, and known motions are removed a priori (i.e. earth rotation, planetary motions, spacecraft orbital motion, solar pressure, drag), leaving small velocity changes caused by variations in the mass distribution of the planet. The residual Doppler frequency shifts are linearly proportional to the component of velocity in the Earth direction. Numerical differentiation of these velocity residuals with respect to time produces line-of-sight (LOS) gravity. These measures are accelerations at spacecraft altitude which can be modeled for geophysical interpretation.",
-            "title": "MGN V RSS LINE OF SIGHT ACCELERATION PROFILES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MGN V RSS LINE OF SIGHT ACCELERATION PROFILES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SMP53-3SMCS",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Remote Sensing Systems (RSS). 2024-04-30. RSS SMAP Level 3 Sea Surface Salinity Standard Mapped Image Monthly Vaidated Dataset. Version 5.3. SMAP Sea Surface Salinity Products. Remote Sensing Systems, 444 Tenth Street, Suite 200, Santa Rosa, CA 95401, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Remote Sensing Systems (RSS). https://doi.org/10.5067/SMP53-3SMCS. http://podaac.jpl.nasa.gov/smap. Remote Sensing Systems (RSS), Remote Sensing Systems (RSS), 2022-02-25, RSS SMAP Level 3 Sea Surface Salinity Standard Mapped Image Monthly V5.0 Validated Dataset, http://podaac.jpl.nasa.gov/smap.",
-            "issued": "2021-01-13",
-            "temporal": "2015-04-01T00:00:00Z/2024-01-01T00:00:00Z",
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
-            "identifier": "C2936708691-POCLOUD",
-            "description": "The RSS SMAP Level 3 Sea Surface Salinity Standard Mapped Image Monthly V5.3 Validated Dataset produced by the Remote Sensing Systems (RSS) and sponsored by the NASA Ocean Salinity Science Team, is a validated product that provides orbital/swath data on sea surface salinity (SSS) derived from the NASA's Soil Moisture Active Passive (SMAP) mission. The SMAP satellite was launched on 31 January 2015 with a near-polar orbit at an inclination of 98 degrees and an altitude of 685 km. It has an ascending node time of 6 pm and is sun-synchronous. With its 1000km swath, SMAP achieves global coverage in approximately 3 days, but has an exact orbit repeat cycle of 8 days. Malfunction of the SMAP scatterometer on 7 July, 2015, has necessitated the use of collocated wind speed, primarily from WindSat, for the surface roughness correction required for the surface salinity retrieval.\r\n<br><br>\r\nThe evaluation Version 5.3 is identical to the Version 6.0 validated release with the exception that Version 5.3 uses the Version 5 L1B TA as input. The V6 L1B TA uses a lower TA threshold for RFI exclusion. Until the full back-processing of V6.0 is complete, the evaluation Version 5.3 can and should be used instead. Version 5.3 has been processed from the beginning of the SMAP mission to the end of 2023, and each data file is available in netCDF-4 file format. Observations are global in extent with an approximate spatial resolution of 40KM. Note that while a SSS 40KM variable is also included in the product for most open ocean applications, The standard product of the SMAP Version 5.3 release is the smoothed salinity product with a spatial resolution of approximately 70 km.",
-            "release-place": "Remote Sensing Systems, 444 Tenth Street, Suite 200, Santa Rosa, CA 95401, USA",
-            "series-name": "RSS SMAP Level 3 Sea Surface Salinity Standard Mapped Image Monthly Vaidated Dataset",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Remote Sensing Systems (RSS)",
-            "title": "RSS SMAP Level 3 Sea Surface Salinity Standard Mapped Image Monthly V5.3 Validated Dataset",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SMAP_RSS_L3_SSS_SMI_MONTHLY_V6.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The RSS SMAP Level 3 Sea Surface Salinity Standard Mapped Image Monthly V5.3 Validated Dataset produced by the Remote Sensing Systems (RSS) and sponsored by the NASA Ocean Salinity Science Team, is a validated product that provides orbital/swath data on sea surface salinity (SSS) derived from the NASA's Soil Moisture Active Passive (SMAP) mission. The SMAP satellite was launched on 31 January 2015 with a near-polar orbit at an inclination of 98 degrees and an altitude of 685 km. It has an ascending node time of 6 pm and is sun-synchronous. With its 1000km swath, SMAP achieves global coverage in approximately 3 days, but has an exact orbit repeat cycle of 8 days. Malfunction of the SMAP scatterometer on 7 July, 2015, has necessitated the use of collocated wind speed, primarily from WindSat, for the surface roughness correction required for the surface salinity retrieval.\r\n<br><br>\r\nThe evaluation Version 5.3 is identical to the Version 6.0 validated release with the exception that Version 5.3 uses the Version 5 L1B TA as input. The V6 L1B TA uses a lower TA threshold for RFI exclusion. Until the full back-processing of V6.0 is complete, the evaluation Version 5.3 can and should be used instead. Version 5.3 has been processed from the beginning of the SMAP mission to the end of 2023, and each data file is available in netCDF-4 file format. Observations are global in extent with an approximate spatial resolution of 40KM. Note that while a SSS 40KM variable is also included in the product for most open ocean applications, The standard product of the SMAP Version 5.3 release is the smoothed salinity product with a spatial resolution of approximately 70 km.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSMP53-3SMCS",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSMP53-3SMCS",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://images.remss.com/figures/missions/smap/bad_ancillaries.txt",
-                    "description": "Dynamically updated RSS webpage listing L2 files with missing ancillary data inputs",
                     "@type": "dcat:Distribution",
+                    "description": "Dynamically updated RSS webpage listing L2 files with missing ancillary data inputs",
+                    "downloadURL": "http://images.remss.com/figures/missions/smap/bad_ancillaries.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's documented anomalies"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/smap/open/docs/V6/ATBD_EOM_final.pdf",
-                    "description": "SMAP-SSS V6.0 Technical Guide (ATBD, Validation Analysis, Product Format Specification)",
                     "@type": "dcat:Distribution",
+                    "description": "SMAP-SSS V6.0 Technical Guide (ATBD, Validation Analysis, Product Format Specification)",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/smap/open/docs/V6/ATBD_EOM_final.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
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
-                    "downloadURL": "http://images.remss.com/figures/missions/smap/bad_orbits.txt",
-                    "description": "Dynamically updated RSS webpage listing L2 files with Bad Orbits",
                     "@type": "dcat:Distribution",
+                    "description": "Dynamically updated RSS webpage listing L2 files with Bad Orbits",
+                    "downloadURL": "http://images.remss.com/figures/missions/smap/bad_orbits.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's documented anomalies"
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SMAP_RSS_L3_SSS_SMI_MONTHLY_V6.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SMAP_RSS_L3_SSS_SMI_MONTHLY_V6.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
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
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/smap/open/L3/RSS/README.txt",
-                    "description": "Known issues README",
                     "@type": "dcat:Distribution",
+                    "description": "Known issues README",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/smap/open/L3/RSS/README.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's documented anomalies"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/smap/open/docs/V6/Release_V6.0.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/smap/open/docs/V6/Release_V6.0.pdf",
+                    "mediaType": "application/pdf",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2936708691-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2936708691-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2936708691-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2936708691-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SMAP_RSS_L3_SSS_SMI_MONTHLY_V6.jpg",
+            "identifier": "C2936708691-POCLOUD",
+            "issued": "2021-01-13",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "salinity/density"
+            ],
+            "landingPage": "https://doi.org/10.5067/SMP53-3SMCS",
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
+            "series-name": "RSS SMAP Level 3 Sea Surface Salinity Standard Mapped Image Monthly Vaidated Dataset",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2015-04-01T00:00:00Z/2024-01-01T00:00:00Z",
             "theme": [
                 "SMAP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "RSS SMAP Level 3 Sea Surface Salinity Standard Mapped Image Monthly V5.3 Validated Dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC1-67P-M12-INFLDSTR-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 1 mission phase, covering the period  from 2015-01-13T23:25:00.000 to 2015-02-10T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc1-67p-m12-infldstr-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC1-67P-M12-INFLDSTR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc1-67p-m12-infldstr-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 1 mission phase, covering the period  from 2015-01-13T23:25:00.000 to 2015-02-10T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC1-MTP012 RDR-INFLDSTR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC1-MTP012 RDR-INFLDSTR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/jmc9-q708",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "CUNY Institute for Demographic Research - CIDR - City University of New York, Center for International Earth Science Information Network - CIESIN - Columbia University, and The World Bank. 2023-06-29. Groundswell Africa Spatial Population and Migration Projections at One-Eighth Degree According to SSPs and RCPs, 2010-2050. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/jmc9-q708. https://doi.org/10.7927/jmc9-q708.",
-            "issued": "2023-06-29",
-            "temporal": "2010-01-01T00:00:00Z/2050-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-29",
-            "keyword": [
-                "earth science",
-                "atmospheric/ocean indicators",
-                "climate indicators"
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
-            "identifier": "C2738394378-SEDAC",
-            "description": "The Groundswell Africa Spatial Population and Migration Projections at One-Eighth Degree According to SSPs and RCPs, 2010-2050 data set provides a baseline population distribution for 2010 and projections from 2020 to 2050, in five-year increments, of population distribution and internal climate-related and other migration for West Africa and the Lake Victoria Basin. The projections are produced using the NCAR-CIDR Spatial Population Downscaling Model developed by the CUNY Institute for Demographic Research (CIDR) and the National Center for Atmospheric Research (NCAR). The model incorporates assumptions based on future development scenarios (Shared Socioeconomic Pathways or SSPs) and emissions trajectories (Representative Concentration Pathways or RCPs). The SSPs include SSP2, representing a middle-of-the road future, and SSP4, representing an unequal development future. Climate models using low and high emissions scenarios, RCP2.6 and RCP8.5, then drive climate impact models on water availability, crop productivity, and pasturelands (where cropping does not occur), as well as flood impacts, from the Inter-Sectoral Impacts Model Intercomparison Project (ISIMIP). Sea-level rise impacts in the coastal zone are estimated to be 1 meter under RCP2.6 and 2 meters under RCP8.5, to account for potential storm surge or coastal flooding. Four scenarios are generated, a pessimistic reference scenario combining SSP4 and RCP8.5, a more climate-friendly scenario combining SSP4 and RCP2.6, a more inclusive development scenario combining SSP2 and RCP8.5, and an optimistic scenario combining SSP2 and RCP2.6. Each scenario provides an ensemble average of four model runs combining different climate impact models as well as confidence intervals to better capture uncertainties. The modeling work was funded and developed jointly with The World Bank.",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "CUNY Institute for Demographic Research - CIDR - City University of New York, Center for International Earth Science Information Network - CIESIN - Columbia University, and The World Bank",
-            "title": "Groundswell Africa Spatial Population and Migration Projections at One-Eighth Degree According to SSPs and RCPs, 2010-2050",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/climmig/climmig-groundswell-africa-pop-mig-proj-1-km-ssps-rcps-2010-2050/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Groundswell Africa Spatial Population and Migration Projections at One-Eighth Degree According to SSPs and RCPs, 2010-2050 data set provides a baseline population distribution for 2010 and projections from 2020 to 2050, in five-year increments, of population distribution and internal climate-related and other migration for West Africa and the Lake Victoria Basin. The projections are produced using the NCAR-CIDR Spatial Population Downscaling Model developed by the CUNY Institute for Demographic Research (CIDR) and the National Center for Atmospheric Research (NCAR). The model incorporates assumptions based on future development scenarios (Shared Socioeconomic Pathways or SSPs) and emissions trajectories (Representative Concentration Pathways or RCPs). The SSPs include SSP2, representing a middle-of-the road future, and SSP4, representing an unequal development future. Climate models using low and high emissions scenarios, RCP2.6 and RCP8.5, then drive climate impact models on water availability, crop productivity, and pasturelands (where cropping does not occur), as well as flood impacts, from the Inter-Sectoral Impacts Model Intercomparison Project (ISIMIP). Sea-level rise impacts in the coastal zone are estimated to be 1 meter under RCP2.6 and 2 meters under RCP8.5, to account for potential storm surge or coastal flooding. Four scenarios are generated, a pessimistic reference scenario combining SSP4 and RCP8.5, a more climate-friendly scenario combining SSP4 and RCP2.6, a more inclusive development scenario combining SSP2 and RCP8.5, and an optimistic scenario combining SSP2 and RCP2.6. Each scenario provides an ensemble average of four model runs combining different climate impact models as well as confidence intervals to better capture uncertainties. The modeling work was funded and developed jointly with The World Bank.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2Fjmc9-q708",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2Fjmc9-q708",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/climmig/climmig-groundswell-africa-pop-mig-proj-1-km-ssps-rcps-2010-2050/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/climmig/climmig-groundswell-africa-pop-mig-proj-1-km-ssps-rcps-2010-2050/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/climmig-groundswell-africa-pop-mig-proj-1-8-ssps-rcps-2010-2050/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/climmig-groundswell-africa-pop-mig-proj-1-8-ssps-rcps-2010-2050/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/climmig-groundswell-africa-pop-mig-proj-1-8-ssps-rcps-2010-2050/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/climmig-groundswell-africa-pop-mig-proj-1-8-ssps-rcps-2010-2050/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/climmig-groundswell-africa-pop-mig-proj-1-8-ssps-rcps-2010-2050",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/climmig-groundswell-africa-pop-mig-proj-1-8-ssps-rcps-2010-2050",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/climmig/climmig-groundswell-africa-pop-mig-proj-1-km-ssps-rcps-2010-2050/sedac-logo.jpg",
+            "identifier": "C2738394378-SEDAC",
+            "issued": "2023-06-29",
+            "keyword": [
+                "earth science",
+                "atmospheric/ocean indicators",
+                "climate indicators"
+            ],
+            "landingPage": "https://doi.org/10.7927/jmc9-q708",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-06-29",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -58.0 180.0 85.0",
+            "temporal": "2010-01-01T00:00:00Z/2050-12-31T00:00:00Z",
             "theme": [
                 "CLIMMIG",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Groundswell Africa Spatial Population and Migration Projections at One-Eighth Degree According to SSPs and RCPs, 2010-2050"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC1-67P-M10-STRLIGHT-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 1 mission phase, covering the period from 2014-11-21T23:25:00.000 to 2014-12-19T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc1-67p-m10-strlight-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC1-67P-M10-STRLIGHT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc1-67p-m10-strlight-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 1 mission phase, covering the period from 2014-11-21T23:25:00.000 to 2014-12-19T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC1-MTP010 RDR-STRLIGHT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC1-MTP010 RDR-STRLIGHT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MEASURES/SO2/DATA405",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Simon Carn. 2022-05-01. MSVOLSO2L4. Version 4. Multi-Satellite Volcanic Sulfur Dioxide L4 Long-Term Global Database V4. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Science Data and Information Services Center (GES DISC). https://doi.org/10.5067/MEASURES/SO2/DATA405. https://disc.gsfc.nasa.gov/datacollection/MSVOLSO2L4_4.html. Digital Science Data.",
-            "issued": "2022-05-01",
-            "temporal": "1978-10-31T00:00:00Z/2022-05-04T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-01",
-            "keyword": [
-                "air quality",
-                "human dimensions",
-                "earth science",
-                "aerosols",
-                "atmosphere",
-                "atmospheric chemistry",
-                "natural hazards"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "SIMON CARN",
                 "hasEmail": "mailto:scarn@mtu.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C2027429276-GES_DISC",
-            "description": "Version 4 is the current version of the data set. Older versions are no longer available and have been superseded by Version 4.\n\nThese data are a part of MEaSUREs 2012 projects. The particular project, \"Multi-Decadal Sulfur Dioxide Climatology from Satellite Instruments\", is expected to produce SO2 Earth Science Data Record by means of combining measurements from backscatter Ultraviolet (BUV), thermal infrared (IR) and microwave (MLS) instruments on multiple satellites. The data represent best estimates of the volcanic and anthropogenic contribution to global atmospheric SO2 concentrations. Since SO2 is the major precursor of sulfate aerosol, which has climate and air quality impact, SO2 measurements will contribute to better understanding of the sulfate aerosol distributions and its atmospheric impact.\"\n\nThe released data file is a long-term database of volcanic SO2 emission derived from ultraviolet satellite measurements from October 31, 1978, to present.\n\nData are in a table format in simple ASCII format:\n\nColumn Descriptions:\nColumn 1 = Name of volcano.\nColumn 2 = Latitude of volcano.\nColumn 3 = Longitude of volcano.\nColumn 4 = Altitude of volcano (km).\nColumn 5 = Eruption year.\nColumn 6 = Eruption month of year.\nColumn 7 = Eruption day of month.\nColumn 8 = Eruption style: exp = explosive, eff = effusive.\nColumn 9 = Eruption volcanic explosivity index (nd = no data or undetermined).\nColumn 10 = Observed plume altitude (km) where known.\nColumn 11 = Estimated plume altitude (km) above vent: 10 km for explosive, 5 km for effusive.\nColumn 12 = Measured SO2 mass in kilotons (= 1000 metric tons).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "MSVOLSO2L4",
             "creator": "Simon Carn",
-            "title": "Multi-Satellite Volcanic Sulfur Dioxide L4 Long-Term Global Database V4 (MSVOLSO2L4) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/Krotkov/MSVOLSO2L4.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Version 4 is the current version of the data set. Older versions are no longer available and have been superseded by Version 4.\n\nThese data are a part of MEaSUREs 2012 projects. The particular project, \"Multi-Decadal Sulfur Dioxide Climatology from Satellite Instruments\", is expected to produce SO2 Earth Science Data Record by means of combining measurements from backscatter Ultraviolet (BUV), thermal infrared (IR) and microwave (MLS) instruments on multiple satellites. The data represent best estimates of the volcanic and anthropogenic contribution to global atmospheric SO2 concentrations. Since SO2 is the major precursor of sulfate aerosol, which has climate and air quality impact, SO2 measurements will contribute to better understanding of the sulfate aerosol distributions and its atmospheric impact.\"\n\nThe released data file is a long-term database of volcanic SO2 emission derived from ultraviolet satellite measurements from October 31, 1978, to present.\n\nData are in a table format in simple ASCII format:\n\nColumn Descriptions:\nColumn 1 = Name of volcano.\nColumn 2 = Latitude of volcano.\nColumn 3 = Longitude of volcano.\nColumn 4 = Altitude of volcano (km).\nColumn 5 = Eruption year.\nColumn 6 = Eruption month of year.\nColumn 7 = Eruption day of month.\nColumn 8 = Eruption style: exp = explosive, eff = effusive.\nColumn 9 = Eruption volcanic explosivity index (nd = no data or undetermined).\nColumn 10 = Observed plume altitude (km) where known.\nColumn 11 = Estimated plume altitude (km) above vent: 10 km for explosive, 5 km for effusive.\nColumn 12 = Measured SO2 mass in kilotons (= 1000 metric tons).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FSO2%2FDATA405",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FSO2%2FDATA405",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -159359,182 +159333,210 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/MSVOLSO2L4_4.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/MSVOLSO2L4_4.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/SO2/MSVOLSO2L4.4",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/SO2/MSVOLSO2L4.4",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthdata.nasa.gov/community/community-data-system-programs/measures-projects/multi-decadal-sulfur-dioxide-climatology-from-satellite-instruments",
-                    "description": "Project summary goals and description",
                     "@type": "dcat:Distribution",
+                    "description": "Project summary goals and description",
+                    "downloadURL": "https://earthdata.nasa.gov/community/community-data-system-programs/measures-projects/multi-decadal-sulfur-dioxide-climatology-from-satellite-instruments",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://measures.gsfc.nasa.gov/data/SO2/MSVOLSO2L4.4/doc/README.MSVOLSO2L4_V4.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://measures.gsfc.nasa.gov/data/SO2/MSVOLSO2L4.4/doc/README.MSVOLSO2L4_V4.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=MSVOLSO2L4",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=MSVOLSO2L4",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/Krotkov/MSVOLSO2L4.png",
+            "identifier": "C2027429276-GES_DISC",
+            "issued": "2022-05-01",
+            "keyword": [
+                "air quality",
+                "human dimensions",
+                "earth science",
+                "aerosols",
+                "atmosphere",
+                "atmospheric chemistry",
+                "natural hazards"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/SO2/DATA405",
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
+            "series-name": "MSVOLSO2L4",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1978-10-31T00:00:00Z/2022-05-04T23:59:59Z",
             "theme": [
                 "MEaSUREs",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Multi-Satellite Volcanic Sulfur Dioxide L4 Long-Term Global Database V4 (MSVOLSO2L4) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "http://techport.nasa.gov/view/90",
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
-                "program",
-                "active"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jeffrey Newmark",
                 "hasEmail": "mailto:jeffrey.newmark@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Science Mission Directorate"
-            },
-            "identifier": "TECHPORT_90",
             "description": "HELIOS Program",
-            "title": "HELIOS Program",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "http://techport.nasa.gov/xml-api/90",
                     "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "TECHPORT_90",
+            "issued": "2018-06-25",
+            "keyword": [
+                "program",
+                "active"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/90",
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
+            "title": "HELIOS Program"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0703-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-11T08:30:50.000 to 2015-04-11T14:54:07.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0703-v1.0_4vm2-88v2",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0703-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0703-v1.0_4vm2-88v2",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-11T08:30:50.000 to 2015-04-11T14:54:07.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0703 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0703 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-VIR-2-EDR-VIS-VESTA-SPECTRA-V2.0",
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
-                "dawn mission to vesta and ceres",
-                "4 vesta"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This volume contains the digital         numbers (DN) contained in the telemetry (TM) packages of the VIR        instrument on board of the spacecraft DAWN. The data are from the       Vesta Encounter phase, which occurred 2011-05-03 to 2012-07-18.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-vir-2-edr-vis-vesta-spectra-v2.0_4vm9-39n2",
+            "issued": "2021-05-21",
+            "keyword": [
+                "dawn mission to vesta and ceres",
+                "4 vesta"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-VIR-2-EDR-VIS-VESTA-SPECTRA-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-vir-2-edr-vis-vesta-spectra-v2.0_4vm9-39n2",
-            "description": "This volume contains the digital         numbers (DN) contained in the telemetry (TM) packages of the VIR        instrument on board of the spacecraft DAWN. The data are from the       Vesta Encounter phase, which occurred 2011-05-03 to 2012-07-18.",
-            "title": "DAWN VIR RAW (EDR) VESTA VISIBLE SPECTRA V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "DAWN VIR RAW (EDR) VESTA VISIBLE SPECTRA V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-PWS-2-EDR-WAVEFORM-10KHZ-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set includes wideband waveform measurements from the Galileo plasma wave receiver obtained during Jupiter orbital operations. These data were obtained during selected observation periods near perijove, satellite encounters and other select times. These measurements are electric waveforms obtained by rapidly sampling the potential at the input to the receiver from the electric dipole antenna.  The sample rates are 201,600/s, 25,200/s, or 3,150/s taken through bandpass filters of 80, 10, or 1 kHz, respectively.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-pws-2-edr-waveform-10khz-v1.0_4vn8-3n73",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "galileo",
                 "amalthea",
@@ -159545,613 +159547,581 @@
                 "io",
                 "europa"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-PWS-2-EDR-WAVEFORM-10KHZ-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-pws-2-edr-waveform-10khz-v1.0_4vn8-3n73",
-            "description": "This data set includes wideband waveform measurements from the Galileo plasma wave receiver obtained during Jupiter orbital operations. These data were obtained during selected observation periods near perijove, satellite encounters and other select times. These measurements are electric waveforms obtained by rapidly sampling the potential at the input to the receiver from the electric dipole antenna.  The sample rates are 201,600/s, 25,200/s, or 3,150/s taken through bandpass filters of 80, 10, or 1 kHz, respectively.",
-            "title": "GO JUPITER PWS EDITED EDR 10KHZ WAVEFORM RECEIVER V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GO JUPITER PWS EDITED EDR 10KHZ WAVEFORM RECEIVER V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT5-3692-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2015-01-01 to 2016-12-31. It is a Occultation measurement and covers the time 2015-02-06T23:26:07 to 2015-02-08T21:49:50.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext5-3692-v1.0_4vpd-5t9f",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars express"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT5-3692-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext5-3692-v1.0_4vpd-5t9f",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2015-01-01 to 2016-12-31. It is a Occultation measurement and covers the time 2015-02-06T23:26:07 to 2015-02-08T21:49:50.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 5 3692 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 5 3692 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-ASTERMAG-V6.0",
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
+            "description": "IAU-adopted absolute V magnitude and slope parameters for numbered asteroids.\"",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-astermag-v6.0_4vq5-zmv3",
+            "issued": "2018-06-26",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-ASTERMAG-V6.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-astermag-v6.0_4vq5-zmv3",
-            "description": "IAU-adopted absolute V magnitude and slope parameters for numbered asteroids.\"",
-            "title": "ASTEROID ABSOLUTE MAGNITUDES V6.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ASTEROID ABSOLUTE MAGNITUDES V6.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0047",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2000-04-07. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/FIRE/0047.",
-            "issued": "2000-03-17",
-            "temporal": "1992-06-06T00:00:00Z/1992-06-28T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-06",
-            "keyword": [
-                "ocean temperature",
-                "oceans",
-                "precipitation",
-                "spectral/engineering",
-                "infrared wavelengths",
-                "earth science",
-                "clouds",
-                "atmospheric winds",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "atmospheric radiation",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "WILLIAM SYRETT",
                 "hasEmail": "mailto:syrett@essc.psu.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1000001060-LARC_ASDC",
             "description": "The First ISCCP Regional Experiments have been designed to improve data products and cloud/radiation parameterizations used in general circulation models (GCMs). Specifically, the goals of FIRE are (1) to improve the basic understanding of the interaction of physical processes in determining life cycles of cirrus and marine stratocumulus systems and the radiative properties of these clouds during their life cycles and (2) to investigate the interrelationships between the ISCCP data, GCM parameterizations, and higher space and time resolution cloud data. To-date, four intensive field-observation periods were planned and executed: a cirrus IFO (October 13 - November 2, 1986); a marine stratocumulus IFO off the southwestern coast of California (June 29 - July 20, 1987); a second cirrus IFO in southeastern Kansas (November 13 - December 7, 1991); and a second marine stratocumulus IFO in the eastern North Atlantic Ocean (June 1 - June 28, 1992). Each mission combined coordinated satellite, airborne, and surface observations with modeling studies to investigate the cloud properties and physical processes of the cloud systems.",
-            "title": "First ISCCP Regional Experiment (FIRE) Atlantic Stratocumulus Transition Experiment (ASTEX) PSU Malcolm Baldridge Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0047",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0047",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001060-LARC_ASDC",
-                    "description": "Earthdata Search for FIRE_AX_PSU_MALBAL_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FIRE_AX_PSU_MALBAL_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001060-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fax_psu_malbal_read.c",
-                    "description": "Readme to read the FIRE ASTEX Malcolm Baldrige Data Set - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "Readme to read the FIRE ASTEX Malcolm Baldrige Data Set - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fax_psu_malbal_read.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "application/postscript",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ax_psu_malbal_part2.ps",
-                    "description": "FIRE ASTEX Readme - Direct File Download (.ps)",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE ASTEX Readme - Direct File Download (.ps)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ax_psu_malbal_part2.ps",
+                    "mediaType": "application/postscript",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0047",
-                    "description": "DOI data set landing page for FIRE_AX_PSU_MALBAL_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIRE_AX_PSU_MALBAL_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0047",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ax_mage_dataset.pdf",
-                    "description": "FIRE ASTEX Marine Aerosol Gas Exchange (MAGE) Langley DAAC Data Set Document",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE ASTEX Marine Aerosol Gas Exchange (MAGE) Langley DAAC Data Set Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ax_mage_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_AX_PSU_MALBAL/",
-                    "description": "ASDC Direct Data Download for FIRE_AX_PSU_MALBAL_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIRE_AX_PSU_MALBAL_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_AX_PSU_MALBAL/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_AX_PSU_MALBAL/contents.html",
-                    "description": "OPeNDAP data access for FIRE_AX_PSU_MALBAL_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for FIRE_AX_PSU_MALBAL_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_AX_PSU_MALBAL/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1000001060-LARC_ASDC",
+            "issued": "2000-03-17",
+            "keyword": [
+                "ocean temperature",
+                "oceans",
+                "precipitation",
+                "spectral/engineering",
+                "infrared wavelengths",
+                "earth science",
+                "clouds",
+                "atmospheric winds",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "atmospheric radiation",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0047",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-07-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>20.0 -70.0 20.0 0.0 60.0 0.0 60.0 -70.0 20.0 -70.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1992-06-06T00:00:00Z/1992-06-28T23:59:59.999Z",
             "theme": [
                 "FIRE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "First ISCCP Regional Experiment (FIRE) Atlantic Stratocumulus Transition Experiment (ASTEX) PSU Malcolm Baldridge Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H41J97NM",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for Hazards and Risk Research - CHRR - Columbia University, Center for International Earth Science Information Network - CIESIN - Columbia University, and International Bank for Reconstruction and Development - The World Bank. 2005-12-31. Global Multihazard Mortality Risks and Distribution. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, Center for Hazards and Risk Research (CHRR)/Columbia University. https://doi.org/10.7927/H41J97NM. https://doi.org/10.7927/H41J97NM.",
-            "issued": "2005-12-31",
-            "temporal": "2000-01-01T00:00:00Z/2000-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2005-12-31",
-            "references": [
-                "https://doi.org/10.7927/H4S180F9",
-                "https://doi.org/10.7927/H45718Z5",
-                "https://doi.org/10.7927/H4WS8R5B"
-            ],
-            "keyword": [
-                "human dimensions",
-                "earth science",
-                "population",
-                "terrestrial hydrosphere",
-                "snow/ice",
-                "natural hazards"
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
-            "identifier": "C179001785-SEDAC",
-            "description": "The Global Multihazard Mortality Risks and Distribution is a 2.5 minute grid identifying and characterizing the nature of multihazard risk at the global scale. For this study, multihazard considers the hazards posed by cyclones, droughts, earthquakes, floods, landslides and volcanoes. The specific hazards are grouped into the following hazard categories: drought (drought), seismic (earthquakes and volcanoes), and hydro (cyclones, floods, and landslides). Each grid cell is assessed for each hazard category; and is considered at high risk or not at high risk. Treated as a binary value, the at-risk values of the hazards categories function as a 3-digit index of multihazard.\n\n\n\n\n\nFor each of the hazard category combinations, aggregate analyses determine the total population, area, and length of major transportation features, as well as, the value of Gross Domestic Product (GDP) and agricultural GDP. This data set is the result of collaboration among the Columbia University Center for Hazards and Risk Research (CHRR), International Bank for Reconstruction and Development/The World Bank, and Columbia University Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Center for Hazards and Risk Research - CHRR - Columbia University, Center for International Earth Science Information Network - CIESIN - Columbia University, and International Bank for Reconstruction and Development - The World Bank",
-            "title": "Global Multihazard Mortality Risks and Distribution",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/ndh-multihazard-mortality-risks-distribution/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Global Multihazard Mortality Risks and Distribution is a 2.5 minute grid identifying and characterizing the nature of multihazard risk at the global scale. For this study, multihazard considers the hazards posed by cyclones, droughts, earthquakes, floods, landslides and volcanoes. The specific hazards are grouped into the following hazard categories: drought (drought), seismic (earthquakes and volcanoes), and hydro (cyclones, floods, and landslides). Each grid cell is assessed for each hazard category; and is considered at high risk or not at high risk. Treated as a binary value, the at-risk values of the hazards categories function as a 3-digit index of multihazard.\n\n\n\n\n\nFor each of the hazard category combinations, aggregate analyses determine the total population, area, and length of major transportation features, as well as, the value of Gross Domestic Product (GDP) and agricultural GDP. This data set is the result of collaboration among the Columbia University Center for Hazards and Risk Research (CHRR), International Bank for Reconstruction and Development/The World Bank, and Columbia University Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH41J97NM",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH41J97NM",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/ndh/ndh-multihazard-mortality-risks-distribution/multihazard-mortality-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/ndh/ndh-multihazard-mortality-risks-distribution/multihazard-mortality-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-multihazard-mortality-risks-distribution/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-multihazard-mortality-risks-distribution/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-multihazard-mortality-risks-distribution/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-multihazard-mortality-risks-distribution/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-multihazard-mortality-risks-distribution",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-multihazard-mortality-risks-distribution",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/ndh-multihazard-mortality-risks-distribution/maps",
+            "identifier": "C179001785-SEDAC",
+            "issued": "2005-12-31",
+            "keyword": [
+                "human dimensions",
+                "earth science",
+                "population",
+                "terrestrial hydrosphere",
+                "snow/ice",
+                "natural hazards"
+            ],
+            "landingPage": "https://doi.org/10.7927/H41J97NM",
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
+                "https://doi.org/10.7927/H4S180F9",
+                "https://doi.org/10.7927/H45718Z5",
+                "https://doi.org/10.7927/H4WS8R5B"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -58.0 180.0 85.0",
+            "temporal": "2000-01-01T00:00:00Z/2000-12-31T00:00:00Z",
             "theme": [
                 "NDH",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Multihazard Mortality Risks and Distribution"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/4JTLIQJJMARO",
             "citation": "Miyazaki, Kazuyuki. 2024-01-08. TRPSCRHNO32H2D. Version 1. TROPESS Chemical Reanalysis Surface HNO3 2-Hourly 2-dimensional Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/4JTLIQJJMARO. https://disc.gsfc.nasa.gov/datacollection/TRPSCRHNO32H2D_1.html. Digital Science Data.",
-            "issued": "2023-01-09",
-            "temporal": "2005-01-01T00:00:00Z/2021-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-02-17",
-            "references": [
-                "https://doi.org/10.5194/essd-12-2223-2020"
-            ],
-            "keyword": [
-                "atmospheric chemistry",
-                "atmosphere",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "KAZUYUKI MIYAZAKI",
                 "hasEmail": "mailto:kazuyuki.miyazaki@jpl.nasa.gov"
             },
+            "creator": "Miyazaki, Kazuyuki",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2816184416-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS Chemical Reanalysis HNO3 2-Hourly 2-dimensional Product contains the surface concentrations of nitric acid. The data are part of the Tropospheric Chemical Reanalysis v2 (TCR-2) for the period 2005-2021. TCR-2 uses JPL's Multi-mOdel Multi-cOnstituent Chemical (MOMO-Chem) data assimilation framework that simultaneously optimizes both concentrations and emissions of multiple species from multiple satellite sensors.\n\nThe data files are written in the netCDF version 4 file format, and each file contains a year of data at 2-hourly resolution, and a spatial resolution of 1.125 x 1.125 degrees. The principal investigator for the TCR-2 data is Miyazaki, Kazuyuki.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSCRHNO32H2D",
-            "creator": "Miyazaki, Kazuyuki",
-            "graphic-preview-description": "TCR-2 01 April 2005.",
-            "title": "TROPESS Chemical Reanalysis Surface HNO3 2-Hourly 2-dimensional Product V1 (TRPSCRHNO32H2D) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRHNO32H2D_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F4JTLIQJJMARO",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F4JTLIQJJMARO",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRHNO32H2D_Sample.png",
-                    "description": "TCR-2 01 April 2005.",
                     "@type": "dcat:Distribution",
+                    "description": "TCR-2 01 April 2005.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRHNO32H2D_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSCRHNO32H2D_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSCRHNO32H2D_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_2HR_SURFCONCS/TRPSCRHNO32H2D.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_2HR_SURFCONCS/TRPSCRHNO32H2D.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSCRHNO32H2D_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSCRHNO32H2D_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TCR2_2HR_SURFCONCS/TRPSCRHNO32H2D.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TCR2_2HR_SURFCONCS/TRPSCRHNO32H2D.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_2HR_SURFCONCS/TRPSCRHNO32H2D.1/doc/TROPESS_ChemReanalysis_Forward_Stream_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_2HR_SURFCONCS/TRPSCRHNO32H2D.1/doc/TROPESS_ChemReanalysis_Forward_Stream_README.pdf",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRHNO32H2D_Sample.png",
+            "identifier": "C2816184416-GES_DISC",
+            "issued": "2023-01-09",
+            "keyword": [
+                "atmospheric chemistry",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/4JTLIQJJMARO",
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
+            "series-name": "TRPSCRHNO32H2D",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2005-01-01T00:00:00Z/2021-12-31T23:59:59.999Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS Chemical Reanalysis Surface HNO3 2-Hourly 2-dimensional Product V1 (TRPSCRHNO32H2D) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/819/",
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
-            "identifier": "DASHLINK_819",
             "description": "This paper describes how damage propagation can be tracked and modeled for a range of fault modes in some modules of commercial high bypass aircraft engines. To that end, response surfaces of all sensors are generated via a thermo-dynamical simulation model for the engine (cycle deck) as a function of variations of flow and efficiency of the modules of interest. These surfaces are normalized and superimposed. Next, sensor readings are matched to those surfaces and \u2013 using an optimization approach \u2013 the corresponding flow and efficiency pair is found that best explains the sensor data. This flow and efficiency pair is then compared to previous pairs and the direction of the change as well as the rate of change is determined. The whole trajectory is then projected into the time domain. An extrapolation of the curve to the limit (which is established via operational margins) yields the remaining life. In a backward mode, the extrapolated curve is discretized and estimated future flow and efficiency pairs are retrieved. These pairs are then input to the cycle deck to produce future anticipated sensor readings as well as confirmatory trips of operational margins. Changes of the future sensor readings with real readings are used to adjust the remaining life calculations. The method is demonstrated on time series of historical engine faults.",
-            "title": "Modeling Propagation of Gas Path Damage",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2008_IEEEPHM_CMAPPSDamagePropagation_2.pdf",
-                    "description": "2008_IEEEPHM_CMAPPSDamagePropagation.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "2008_IEEEPHM_CMAPPSDamagePropagation.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2008_IEEEPHM_CMAPPSDamagePropagation_2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "2008_IEEEPHM_CMAPPSDamagePropagation.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_819",
+            "issued": "2013-07-29",
+            "keyword": [
+                "nasa",
+                "ames",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/819/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Modeling Propagation of Gas Path Damage"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GPM/SSMIS/F18/1C/07",
             "citation": "Wesley Berg. 2021-07-29. GPM_1CF18SSMIS. GPM SSMIS on F18 Common Calibrated Brightness Temperatures L1C 1.5 hours 12 km V07. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/SSMIS/F18/1C/07. https://disc.gsfc.nasa.gov/datacollection/GPM_1CF18SSMIS_07.html. Digital Science Data.",
-            "issued": "2021-07-21",
-            "temporal": "2010-03-08T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-07-21",
-            "references": [
-                "https://doi.org/10.1175/JTECH-D-16-0100.1",
-                "https://doi.org/10.3390/rs10081306"
-            ],
-            "keyword": [
-                "earth science",
-                "atmospheric water vapor",
-                "atmosphere",
-                "spectral/engineering",
-                "precipitation",
-                "microwave"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "WESLEY BERG",
                 "hasEmail": "mailto:berg@atmos.colostate.edu"
             },
+            "creator": "Wesley Berg",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2264132936-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Version 07 is the current version of the data set. Older versions will no longer be available and have been superseded by Version 07.\n\nAll 1C products have a common L1C data structure, simple and generic. Each L1C swath includes scan time, latitude and longitude, scan status, quality, incidence angle, Sun glint angle, and the intercalibrated brightness temperature (Tc). One or more swaths are included in a product. The radiometer data are recalibrated to a common basis so that precipitation products derived from them are consistent. 1CSSMIS contains common calibrated brightness temperature from the SSMIS passive microwave instruments flown on the DMSP satellites. Swath S1 has 3 low frequency channels (19V 19H 22V). Swath S2 has 2 low frequency channels (37V 37H). Swath S3 has 4 high frequency channels (150H 183+/-1H 183+/-3H 183+/-7H). S4 has 2 high frequency channels (91V 91H). All the above frequencies are in GHz. Earth observations for all four swaths are taken during a 144o segment of the instrument rotation when SSMIS scans in the direction of foreward satellite motion. We define the spacecraft vector (v) at the center of this segment.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "GPM_1CF18SSMIS",
-            "creator": "Wesley Berg",
-            "graphic-preview-description": "Common Calibrated Brightness Temperature from F18 SSMIS (GPM_1CF18SSMIS)",
-            "title": "GPM SSMIS on F18 Common Calibrated Brightness Temperatures L1C 1.5 hours 12 km V07 (GPM_1CF18SSMIS) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/1C-BR.F18.SSMIS.XCAL2016-V.20150101-S002530-E020727.026833.V05A.PNG",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FSSMIS%2FF18%2F1C%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FSSMIS%2FF18%2F1C%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/1C-BR.F18.SSMIS.XCAL2016-V.20150101-S002530-E020727.026833.V05A.PNG",
-                    "description": "Common Calibrated Brightness Temperature from F18 SSMIS (GPM_1CF18SSMIS)",
                     "@type": "dcat:Distribution",
+                    "description": "Common Calibrated Brightness Temperature from F18 SSMIS (GPM_1CF18SSMIS)",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/1C-BR.F18.SSMIS.XCAL2016-V.20150101-S002530-E020727.026833.V05A.PNG",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_1CF18SSMIS_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_1CF18SSMIS_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L1C/GPM_1CF18SSMIS.07/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L1C/GPM_1CF18SSMIS.07/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_1CF18SSMIS_07",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_1CF18SSMIS_07",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L1C/GPM_1CF18SSMIS.07/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L1C/GPM_1CF18SSMIS.07/contents.html",
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
-                    "title": "View this dataset's read me document"
+                    "description": "README Document",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L2/doc/README.GPM.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "View this dataset's read me document"
                 },
                 {
                     "@type": "dcat:Distribution",
@@ -160160,338 +160130,348 @@
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
+            "graphic-preview-description": "Common Calibrated Brightness Temperature from F18 SSMIS (GPM_1CF18SSMIS)",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/1C-BR.F18.SSMIS.XCAL2016-V.20150101-S002530-E020727.026833.V05A.PNG",
+            "identifier": "C2264132936-GES_DISC",
+            "issued": "2021-07-21",
+            "keyword": [
+                "earth science",
+                "atmospheric water vapor",
+                "atmosphere",
+                "spectral/engineering",
+                "precipitation",
+                "microwave"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/SSMIS/F18/1C/07",
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
+            "series-name": "GPM_1CF18SSMIS",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2010-03-08T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "GPM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM SSMIS on F18 Common Calibrated Brightness Temperatures L1C 1.5 hours 12 km V07 (GPM_1CF18SSMIS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RPCMAG-4-CR4A-RESAMPLED-V9.0",
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
+            "description": "This dataset contains RESAMPLED DATA (CODMAC LEVEL 4) of the Cruise 4-1\nphase, called CRUISE PHASE CR4A, of the ROSETTA orbiter magnetometer RPCMAG.\nIncluded are data from the Passive Checkout PC8 from July 11, 2008 until\nAugust 1, 2008.\nThe current version of the dataset is V9.0.\nThe difference to the datasets of earlier versions is mainly a significantly\nimproved sensor temperature model, more detailed documentation about magnetic\ndisturbance sources, more data handling information for the user and\nalso an improved quality flagging system.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rpcmag-4-cr4a-resampled-v9.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "checkout"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RPCMAG-4-CR4A-RESAMPLED-V9.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rpcmag-4-cr4a-resampled-v9.0",
-            "description": "This dataset contains RESAMPLED DATA (CODMAC LEVEL 4) of the Cruise 4-1\nphase, called CRUISE PHASE CR4A, of the ROSETTA orbiter magnetometer RPCMAG.\nIncluded are data from the Passive Checkout PC8 from July 11, 2008 until\nAugust 1, 2008.\nThe current version of the dataset is V9.0.\nThe difference to the datasets of earlier versions is mainly a significantly\nimproved sensor temperature model, more detailed documentation about magnetic\ndisturbance sources, more data handling information for the user and\nalso an improved quality flagging system.",
-            "title": "ROSETTA-ORBITER CHECK RPCMAG 2 CR4A RESAMPLED V9.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECK RPCMAG 2 CR4A RESAMPLED V9.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GHRC/MULTIPLE/DATA201",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Meyer, Paul .1998. INFRARED GLOBAL GEOSTATIONARY COMPOSITE [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GHRC/MULTIPLE/DATA201",
-            "issued": "1998-01-01",
-            "temporal": "1995-06-04T00:00:00Z/2022-05-30T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-23",
-            "keyword": [
-                "earth science",
-                "spectral/engineering",
-                "infrared wavelengths"
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
-            "identifier": "C1996543397-GHRC_DAAC",
             "description": "The Infrared Global Geostationary Composite dataset contains global composite images from the infrared channels of multiple weather satellites in geosynchronous orbit. These satellites include the Global Mobility Service (GMS) from Japan, Geostationary Operational Environmental Satellite (GOES) from the United States, NOAA satellites, and Meteorological Satellite (METEOSAT) from Europe spanning  nearly the entire globe. The spatial resolution is 14 km before December 18, 2017 and 4 km thereafter with the data remapped into a Mercator projection. The data have not necessarily been cross calibrated between sensors. The data are available in AREA McIDAS format from June 4, 1995 to present.",
-            "title": "INFRARED GLOBAL GEOSTATIONARY COMPOSITE V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHRC%2FMULTIPLE%2FDATA201",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHRC%2FMULTIPLE%2FDATA201",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=globalir",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=globalir",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/globalir/doc/globalir_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/globalir/doc/globalir_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/data-recipes/infrared-global-geostationary-composite-quick-view",
-                    "description": "Infrared Global Geostationary Composite Quick View Data Recipe",
                     "@type": "dcat:Distribution",
+                    "description": "Infrared Global Geostationary Composite Quick View Data Recipe",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/data-recipes/infrared-global-geostationary-composite-quick-view",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data recipes"
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
+            "identifier": "C1996543397-GHRC_DAAC",
+            "issued": "1998-01-01",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "infrared wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/GHRC/MULTIPLE/DATA201",
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
             "spatial": "-180.0 -61.0 180.0 66.0",
+            "temporal": "1995-06-04T00:00:00Z/2022-05-30T00:00:00Z",
             "theme": [
                 "NOT APPLICABLE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "INFRARED GLOBAL GEOSTATIONARY COMPOSITE V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-2-CR4A-V1.0",
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
+            "description": "This data set contains count rates (1/s) as measured by the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, along with their standard deviations.  These are CODMAC Level 2 Experiment Data Record data, and provide a measure of the radiation in the spacecraft environment during the CRUISE 4A mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-2-cr4a-v1.0_4w6n-4xt4",
+            "issued": "2021-05-21",
+            "keyword": [
+                "calibration",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-2-CR4A-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-2-cr4a-v1.0_4w6n-4xt4",
-            "description": "This data set contains count rates (1/s) as measured by the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, along with their standard deviations.  These are CODMAC Level 2 Experiment Data Record data, and provide a measure of the radiation in the spacecraft environment during the CRUISE 4A mission phase.",
-            "title": "ROSETTA-ORBITER X SREM 2 CRUISE 4A\n    V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER X SREM 2 CRUISE 4A\n    V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567223-USGS_LTA.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "U.S. Geological Survey. 2010-01-01. USGS Global Forest Observations Initiative (GFOI) Cambodia. Archived by National Aeronautics and Space Administration, U.S. Government, U.S. Geological Survey. http://lsiexplorer.cr.usgs.gov.",
-            "issued": "1972-12-15",
-            "temporal": "1972-12-15T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-03-25",
-            "keyword": [
-                "biosphere",
-                "human dimensions",
-                "terrestrial ecosystems",
-                "vegetation",
-                "forest science",
-                "earth science",
-                "habitat conversion/fragmentation",
-                "agriculture"
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
-            "identifier": "C1220567223-USGS_LTA",
-            "description": "The Global Forest Observations Initiative (GFOI) is an initiative of the inter-governmental Group on Earth Observations (GEO) that aims to:\n\nfoster the sustained availability of observations for national forest monitoring systems; support governments that are establishing national systems by providing a platform for coordinating observations, providing assistance and guidance on utilizing observations, developing accepted methods and protocols, and promoting ongoing research and development; and work with national governments that report into international forest assessments (such as the global Forest Resources Assessment (FRA) of the Food and Agriculture Organization, FAO) and the national greenhouse gas inventories reported to the UN Framework Convention on Climate Change (UNFCCC) using methods of the Intergovernmental Panel on Climate Change (IPCC).",
             "creator": "U.S. Geological Survey",
-            "title": "USGS Global Forest Observations Initiative (GFOI) Cambodia",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Global Forest Observations Initiative (GFOI) is an initiative of the inter-governmental Group on Earth Observations (GEO) that aims to:\n\nfoster the sustained availability of observations for national forest monitoring systems; support governments that are establishing national systems by providing a platform for coordinating observations, providing assistance and guidance on utilizing observations, developing accepted methods and protocols, and promoting ongoing research and development; and work with national governments that report into international forest assessments (such as the global Forest Resources Assessment (FRA) of the Food and Agriculture Organization, FAO) and the national greenhouse gas inventories reported to the UN Framework Convention on Climate Change (UNFCCC) using methods of the Intergovernmental Panel on Climate Change (IPCC).",
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
-                    "downloadURL": "http://www.gfoi.org/",
-                    "description": "\n         Group on Earth Observations (GEO) Global Forest Observations Initiative (GFOI)\n      ",
                     "@type": "dcat:Distribution",
+                    "description": "\n         Group on Earth Observations (GEO) Global Forest Observations Initiative (GFOI)\n      ",
+                    "downloadURL": "http://www.gfoi.org/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "identifier": "C1220567223-USGS_LTA",
+            "issued": "1972-12-15",
+            "keyword": [
+                "biosphere",
+                "human dimensions",
+                "terrestrial ecosystems",
+                "vegetation",
+                "forest science",
+                "earth science",
+                "habitat conversion/fragmentation",
+                "agriculture"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567223-USGS_LTA.html",
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
             "spatial": "100.57 9.09 109.65 15.53",
+            "temporal": "1972-12-15T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "CWIC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "USGS Global Forest Observations Initiative (GFOI) Cambodia"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TESHNO3L_L2.006",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The data used in this study were produced by the TES Science Team at the TES SIPS and archived at the Langley DAAC. See ProductionDateTime for Published date.",
-            "issued": "2013-03-29",
-            "temporal": "2004-07-15T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-10-28",
-            "keyword": [
-                "air quality",
-                "earth science",
-                "atmospheric chemistry/nitrogen compounds",
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
-            "identifier": "C191856319-LARC",
             "description": "Atmospheric vertical profile estimates and associated errors (diagonals and covariance matrices), along with retrieved surface temperature, cloud effective optical depth, column estimates, quality flags, averaging kernels and a priori constraint vectors.",
-            "title": "TES/Aura L2 HNO3 Limb V006",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTESHNO3L_L2.006",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTESHNO3L_L2.006",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 }
             ],
+            "identifier": "C191856319-LARC",
+            "issued": "2013-03-29",
+            "keyword": [
+                "air quality",
+                "earth science",
+                "atmospheric chemistry/nitrogen compounds",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TESHNO3L_L2.006",
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
+            "title": "TES/Aura L2 HNO3 Limb V006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/4waf-c72d",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "temporal": "1977-01-01/1996-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "planetary science",
-                "geography",
-                "forums",
-                "space science",
-                "safety",
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
-            "identifier": "NASA-0000036__4",
+            "describedBy": "http://www.lpi.usra.edu/resources/gc/gcreadme.html",
             "description": "This web page leads to a database of images and information about the 150 major impact craters on Ganymede and is updated semi-regularly based on continuing analysis of Voyager 2 images.",
-            "title": "Ganymede Crater Database",
-            "programCode": [
-                "026:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -160499,446 +160479,475 @@
                     "mediaType": "text/html"
                 }
             ],
-            "describedBy": "http://www.lpi.usra.edu/resources/gc/gcreadme.html",
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-0000036__4",
+            "issued": "2018-06-25",
+            "keyword": [
+                "planetary science",
+                "geography",
+                "forums",
+                "space science",
+                "safety",
+                "knowledge sharing"
+            ],
+            "landingPage": "https://data.nasa.gov/d/4waf-c72d",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "temporal": "1977-01-01/1996-01-01",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "Ganymede Crater Database"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SWTPR-WW001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SWOT pre-launch field campaign. 2022-05-31. GPS sea surface height, Conductivity, Temperature and Depth (CTD) data from the 2019-2020 SWOT pre-launch field campaign. Version 1.0. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/JPL/PODAAC. https://doi.org/10.5067/SWTPR-WW001. https://podaac-tools.jpl.nasa.gov/drive/files/misc/web/misc/SWOT/SWOT_Prelaunch_2019_2020/User_Guide_SWOT_Prelaunch_2019_2020.pdf .",
-            "issued": "2022-03-02",
-            "temporal": "2019-09-05T00:00:00Z/2019-12-03T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-12-03",
-            "references": [
-                "https://doi.org/10.1175/jtech-d-21-0039.1"
-            ],
-            "keyword": [
-                "oceans",
-                "ocean pressure",
-                "ocean temperature",
-                "salinity/density",
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
-            "identifier": "C2229635761-POCLOUD",
-            "description": "This dataset provides the conductivity, temperature and depth (CTD) measurements from the CTD sensors on a WireWalker profiler on a full-depth mooring deployed by the SWOT prelaunch field campaign. The campaign was designed to test the performance of several instruments/platforms in meeting the SWOT Calibration/Validation (CalVal) requirement. It was conducted near the SWOT CalVal crossover location, about 300 kilometers west of Monterey, California between September, 2019 and January, 2020. The WW samples the upper 500 m of the water column, while the deep ocean below 500 m are measured by fixed-depth CTDs https://doi.org/10.5067/SWTPR-CTD01. The campaign also deployed another two CTD moorings, a slocum glider, one bottom pressure recorder and one Pressure Inverted Echo Sounder.  Details can be found in the user guide and the journal reference given in the documentation section.",
-            "graphic-preview-description": "Thumbnail",
             "creator": "SWOT pre-launch field campaign",
-            "title": "SWOT 2019-2020 Prelaunch Oceanography Field Campaign SIO Mooring WireWalker (WW)",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_PRELAUNCH_L2_WW_V1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset provides the conductivity, temperature and depth (CTD) measurements from the CTD sensors on a WireWalker profiler on a full-depth mooring deployed by the SWOT prelaunch field campaign. The campaign was designed to test the performance of several instruments/platforms in meeting the SWOT Calibration/Validation (CalVal) requirement. It was conducted near the SWOT CalVal crossover location, about 300 kilometers west of Monterey, California between September, 2019 and January, 2020. The WW samples the upper 500 m of the water column, while the deep ocean below 500 m are measured by fixed-depth CTDs https://doi.org/10.5067/SWTPR-CTD01. The campaign also deployed another two CTD moorings, a slocum glider, one bottom pressure recorder and one Pressure Inverted Echo Sounder.  Details can be found in the user guide and the journal reference given in the documentation section.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSWTPR-WW001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSWTPR-WW001",
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_PRELAUNCH_L2_WW_V1.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_PRELAUNCH_L2_WW_V1.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2229635761-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2229635761-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2229635761-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2229635761-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_PRELAUNCH_L2_WW_V1.jpg",
+            "identifier": "C2229635761-POCLOUD",
+            "issued": "2022-03-02",
+            "keyword": [
+                "oceans",
+                "ocean pressure",
+                "ocean temperature",
+                "salinity/density",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SWTPR-WW001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-12-03",
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
+            "temporal": "2019-09-05T00:00:00Z/2019-12-03T23:59:59.999Z",
             "theme": [
                 "SWOT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SWOT 2019-2020 Prelaunch Oceanography Field Campaign SIO Mooring WireWalker (WW)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSX-L-SPIRIT3-2%2F4-V1.0",
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
-                "midcourse space experiment"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Midcourse Space Experiment (MSX) lunar eclipse observation on September 27, 1996 resulted in six 4.3 micron brightness temperature maps of the moon. In addition, qualitative observations were made at 8.3 microns.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msx-l-spirit3-2-4-v1.0_4whp-gw6s",
+            "issued": "2018-06-26",
+            "keyword": [
+                "moon",
+                "midcourse space experiment"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSX-L-SPIRIT3-2%2F4-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msx-l-spirit3-2-4-v1.0_4whp-gw6s",
-            "description": "The Midcourse Space Experiment (MSX) lunar eclipse observation on September 27, 1996 resulted in six 4.3 micron brightness temperature maps of the moon. In addition, qualitative observations were made at 8.3 microns.",
-            "title": "MSX LUNAR ECLIPSE OBSERVATION V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MSX LUNAR ECLIPSE OBSERVATION V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/795",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Frost, P.G.H. 2005. SAFARI 2000 Vegetation Structure of Kataba Forest, Zambia, Wet Season 2000. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/795",
-            "issued": "2023-10-18",
-            "temporal": "2000-02-15T00:00:00Z/2000-03-15T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-25",
-            "keyword": [
-                "biosphere",
-                "vegetation",
-                "earth science",
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
-            "identifier": "C2789733347-ORNL_CLOUD",
             "description": "Tree basal area, percent tree canopy cover, and proportional contribution of main species to canopy cover were measured at 60 sampling points at 50 m intervals along six transects in the vicinity of the MODIS validation site tower in Kataba Forest, near Mongu, Zambia, in late February to early March 2000 as part of the SAFARI 2000 Wet Season Campaign. The aim of the study was to provide a broad description of the tree canopy layer around the tower.Tree and shrub species composition was recorded for each grid and measurements of canopy cover (% and rank) and frequency of occurrence (%) were made. Basal area was estimated at each grid site in a single 360 degree sweep using a basal area prism. Four estimates of canopy cover, oriented north, south, east, and west around the sample point, were taken at each grid site using a spherical densiometer and the data were averaged to give a single value for each grid. Only the canopies of trees and shrubs above 1.5 m height were measured.The data are stored in an ASCII file, in csv format. The file lists all tree and shrub species recorded and provides the proportional contribution of these species to canopy cover in each grid. Total tree basal area (m2 ha-1) and overall tree canopy cover (%) in each grid is also provided. The companion file provides additional vegetation data, graphics, long-term meteorological data, a discussion of the study results, and photographs of the study site.",
-            "graphic-preview-description": "Browse Image",
-            "title": "SAFARI 2000 Vegetation Structure of Kataba Forest, Zambia, Wet Season 2000",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/safari_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F795",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F795",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/field_campaign/mongu_veg_structure/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/field_campaign/mongu_veg_structure/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/S2K/guides/mongu_veg_structure.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/S2K/guides/mongu_veg_structure.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/795",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/795",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/field_campaign/mongu_veg_structure/comp/kataba_veg_survey.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/field_campaign/mongu_veg_structure/comp/kataba_veg_survey.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/field_campaign/mongu_veg_structure/comp/mongu_veg_structure_readme.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/field_campaign/mongu_veg_structure/comp/mongu_veg_structure_readme.pdf",
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
+            "identifier": "C2789733347-ORNL_CLOUD",
+            "issued": "2023-10-18",
+            "keyword": [
+                "biosphere",
+                "vegetation",
+                "earth science",
+                "ecosystems"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/795",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-10-25",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-15.44 23.25",
+            "temporal": "2000-02-15T00:00:00Z/2000-03-15T23:59:59Z",
             "theme": [
                 "SAFARI 2000",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAFARI 2000 Vegetation Structure of Kataba Forest, Zambia, Wet Season 2000"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0903-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-07-17T10:03:05.000 to 2015-07-17T16:02:44.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0903-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0903-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0903-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-07-17T10:03:05.000 to 2015-07-17T16:02:44.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0903 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0903 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RSI-1%2F2%2F3-CVP1-0003-V1.0",
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
+            "description": "This is a Commissioning measurement covering the time 2004-03-28T21:51:03.500 to 2004-03-29T06:51:57.950.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rsi-1-2-3-cvp1-0003-v1.0_4wr4-vaac",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "unknown"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RSI-1%2F2%2F3-CVP1-0003-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rsi-1-2-3-cvp1-0003-v1.0_4wr4-vaac",
-            "description": "This is a Commissioning measurement covering the time 2004-03-28T21:51:03.500 to 2004-03-29T06:51:57.950.",
-            "title": "ROSETTA-ORBITER CHECK RSI 1/2/3 COMMISSIONING 1 0003 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECK RSI 1/2/3 COMMISSIONING 1 0003 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-RPCMAG-2-EAR2-RAW-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This dataset contains EDITED RAW DATA of the second Earth Flyby\n(EAR2). The closest approach (CA) took place on November 13, 2007 at 20:57",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-rpcmag-2-ear2-raw-v3.0_4wrf-7dan",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "earth",
                 "international rosetta mission",
                 "checkout"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-RPCMAG-2-EAR2-RAW-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-rpcmag-2-ear2-raw-v3.0_4wrf-7dan",
-            "description": "This dataset contains EDITED RAW DATA of the second Earth Flyby\n(EAR2). The closest approach (CA) took place on November 13, 2007 at 20:57",
-            "title": "ROSETTA-ORBITER EARTH RPCMAG 2 EAR2 RAW V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER EARTH RPCMAG 2 EAR2 RAW V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1031-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-09-13T21:20:30.000 to 2015-09-14T05:26:11.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1031-v1.0_4wva-pnjh",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1031-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1031-v1.0_4wva-pnjh",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-09-13T21:20:30.000 to 2015-09-14T05:26:11.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1031 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1031 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0782-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-05-16T22:33:05.000 to 2015-05-17T04:14:43.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0782-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0782-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0782-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-05-16T22:33:05.000 to 2015-05-17T04:14:43.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0782 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0782 V1.0"
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
+            "description": "APXS, HAZCAM, NAVCAM, MI, PANCAM, RAT, Rover Motion Counter, SPICE",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20140609.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-440",
+            "issued": "2018-06-25",
             "keyword": [
                 "rover motion counter",
                 "apxs",
@@ -160949,1119 +160958,1112 @@
                 "mi",
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
-            "identifier": "NASA-440",
-            "description": "APXS, HAZCAM, NAVCAM, MI, PANCAM, RAT, Rover Motion Counter, SPICE",
-            "title": "PDS Mars Exploration Rovers Data Release 40",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20140609.shtml",
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
+            "title": "PDS Mars Exploration Rovers Data Release 40"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0187-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-07T19:55:45.000 to 2014-08-08T02:32:41.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0187-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0187-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0187-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-07T19:55:45.000 to 2014-08-08T02:32:41.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0187 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0187 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amaven.swia.calibrated&version=1.11",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This bundle contains fully calibrated MAVEN SWIA data, including ion velocity distributions,  energy spectra, and density, temperature, and velocity moments from onboard calculations.  Tables of sensitivity and energy/angle maps are included in files.",
+            "identifier": "urn:nasa:pds:maven.swia.calibrated_4x4k-dszb",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "maven swia calibrated data",
                 "mars atmosphere and volatile evolution mission",
                 "mars",
                 "solar wind"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amaven.swia.calibrated&version=1.11",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:maven.swia.calibrated_4x4k-dszb",
-            "description": "This bundle contains fully calibrated MAVEN SWIA data, including ion velocity distributions,  energy spectra, and density, temperature, and velocity moments from onboard calculations.  Tables of sensitivity and energy/angle maps are included in files.",
-            "title": "MAVEN SWIA Calibrated Data Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MAVEN SWIA Calibrated Data Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGN-V-RDRS-5-GDR-REFLECTIVITY-V1.0",
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
+            "description": "This data set contains the Magellan Global Reflectivity Data Record (GREDR). The power reflection coefficients are derived by fitting altimeter echoes from the fan-beam altimetry antenna as a function of time to Hagfors' radar backscatter model templates. The values are then corrected for the presence of multiple echo peaks and further corrected for diffuse scattering using backscatter data obtained by the side-looking mode of the Magellan radar. Each GREDR image pixel is represented by a 8-bit unsigned integer.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgn-v-rdrs-5-gdr-reflectivity-v1.0_4x7c-r7sm",
+            "issued": "2021-05-21",
+            "keyword": [
+                "venus",
+                "magellan"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGN-V-RDRS-5-GDR-REFLECTIVITY-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgn-v-rdrs-5-gdr-reflectivity-v1.0_4x7c-r7sm",
-            "description": "This data set contains the Magellan Global Reflectivity Data Record (GREDR). The power reflection coefficients are derived by fitting altimeter echoes from the fan-beam altimetry antenna as a function of time to Hagfors' radar backscatter model templates. The values are then corrected for the presence of multiple echo peaks and further corrected for diffuse scattering using backscatter data obtained by the side-looking mode of the Magellan radar. Each GREDR image pixel is represented by a 8-bit unsigned integer.",
-            "title": "MGN V RDRS 5 GLOBAL DATA RECORD REFLECTIVITY V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MGN V RDRS 5 GLOBAL DATA RECORD REFLECTIVITY V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/api-documents/foundry/#/data.nasa.gov/7qz6-zrqt",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2015-11-30",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "https://data.nasa.gov/developer",
-                "http://neo.jpl.nasa.gov/stats/wise/"
-            ],
-            "keyword": [
-                "audio",
-                "sound cloud file",
-                "api",
-                "planetary science research"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jason Duley",
                 "hasEmail": "mailto:Jason.Duley@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "API-37",
             "description": "This API uses data that show discovery statistics for NEAs and comets discovered by NASA's WISE mission - now renamed to NEOWISE.",
-            "title": "WISE NEA/COMET DISCOVERY STATISTICS API",
-            "programCode": [
-                "026:007"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.nasa.gov/resource/7qz6-zrqt.json",
-                    "description": "This API uses data that show discovery statistics for NEAs and comets discovered by NASA's WISE mission - now renamed to NEOWISE.",
                     "@type": "dcat:Distribution",
+                    "description": "This API uses data that show discovery statistics for NEAs and comets discovered by NASA's WISE mission - now renamed to NEOWISE.",
+                    "downloadURL": "https://data.nasa.gov/resource/7qz6-zrqt.json",
+                    "mediaType": "text/html",
                     "title": "WISE NEA/COMET DISCOVERY STATISTICS API"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "API-37",
+            "issued": "2015-11-30",
+            "keyword": [
+                "audio",
+                "sound cloud file",
+                "api",
+                "planetary science research"
+            ],
+            "landingPage": "https://data.nasa.gov/api-documents/foundry/#/data.nasa.gov/7qz6-zrqt",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:007"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "references": [
+                "https://data.nasa.gov/developer",
+                "http://neo.jpl.nasa.gov/stats/wise/"
+            ],
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "WISE NEA/COMET DISCOVERY STATISTICS API"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7265/N5H41PBV",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Great Lakes Ice Charts, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center. https://doi.org/10.7265/N5H41PBV.",
-            "issued": "1973-12-01",
-            "temporal": "1973-12-01T00:00:00Z/2002-05-09T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2002-05-09",
-            "keyword": [
-                "snow/ice",
-                "cryosphere",
-                "terrestrial hydrosphere",
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
-            "identifier": "C1386246219-NSIDCV0",
             "description": "These charts show ice extent and concentration three times weekly during the ice season, for all lakes except Ontario, from the 1973/74 ice season through the 2001/2002 ice season. Most charts are annotated to indicate data sources. The Straits of Mackinac, Green Bay, and Sault Ste. Marie are enlarged as insets; and in some cases, provided as separate charts. From 1973/74 through 1986/87, charts were prepared by the National Weather Service Forecast Office in Ann Arbor, Michigan. Beginning with the 1987/88 season, the National Ice Center (formerly known as the Navy/NOAA Joint Ice Center) in Suitland, Maryland prepared the charts. Charts are available as GIF files.",
-            "title": "Great Lakes Ice Charts, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN5H41PBV",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN5H41PBV",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/G00486_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/G00486_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5H41PBV",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/N5H41PBV",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5H41PBV",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/N5H41PBV",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386246219-NSIDCV0",
+            "issued": "1973-12-01",
+            "keyword": [
+                "snow/ice",
+                "cryosphere",
+                "terrestrial hydrosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.7265/N5H41PBV",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2002-05-09",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "-93.0 41.0 -79.0 49.0",
+            "temporal": "1973-12-01T00:00:00Z/2002-05-09T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Great Lakes Ice Charts, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-C-HRIV%2FITS%2FMRI-5-TEMPEL1-SHAPE-V1.0",
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
+            "description": "Shape model of comet 9P/Tempel 1, as derived from the Deep Impact images obtained around the time of closest approach to the comet.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-c-hriv-its-mri-5-tempel1-shape-v1.0_4xam-vijs",
+            "issued": "2021-05-21",
+            "keyword": [
+                "9p/tempel 1 (1867 g1)",
+                "deep impact"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-C-HRIV%2FITS%2FMRI-5-TEMPEL1-SHAPE-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-c-hriv-its-mri-5-tempel1-shape-v1.0_4xam-vijs",
-            "description": "Shape model of comet 9P/Tempel 1, as derived from the Deep Impact images obtained around the time of closest approach to the comet.",
-            "title": "PLATE SHAPE MODEL OF COMET 9P/TEMPEL 1, V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "PLATE SHAPE MODEL OF COMET 9P/TEMPEL 1, V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1123-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-23T14:27:30.000 to 2015-10-23T17:20:36.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1123-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1123-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1123-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-23T14:27:30.000 to 2015-10-23T17:20:36.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1123 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1123 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/406",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Atkinson, G.B., and B. Funk. 1998. BOREAS/AES Campbell Scientific 15-minute Surface Meteorological Data: 1996. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/406",
-            "issued": "2023-11-22",
-            "temporal": "1996-01-01T00:00:00Z/1996-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-28",
-            "keyword": [
-                "atmosphere",
-                "terrestrial hydrosphere",
-                "snow/ice",
-                "precipitation",
-                "earth science",
-                "atmospheric winds",
-                "atmospheric water vapor",
-                "atmospheric temperature",
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
-            "identifier": "C2808090091-ORNL_CLOUD",
             "description": "Contains data from 1996 from the Atmospheric Environment Service Campbell Scientific autostations collecting continuous fifteen minute data for BOREAS.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS/AES Campbell Scientific 15-minute Surface Meteorological Data: 1996",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F406",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F406",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/STAFF/ams_cs96/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/STAFF/ams_cs96/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/AES_CS.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/AES_CS.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/406",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/406",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/ams_cs96/comp/AES_CS.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/ams_cs96/comp/AES_CS.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/ams_cs96/comp/AES_CS.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/ams_cs96/comp/AES_CS.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/ams_cs96/comp/AES_CS.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/ams_cs96/comp/AES_CS.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/ams_cs96/comp/ams_cs96.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/ams_cs96/comp/ams_cs96.def",
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
+            "identifier": "C2808090091-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "atmosphere",
+                "terrestrial hydrosphere",
+                "snow/ice",
+                "precipitation",
+                "earth science",
+                "atmospheric winds",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "atmospheric pressure"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/406",
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
             "spatial": "-108.52 50.95 -94.7 58.18",
+            "temporal": "1996-01-01T00:00:00Z/1996-12-31T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS/AES Campbell Scientific 15-minute Surface Meteorological Data: 1996"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GNSS/GLONASS_DAILY_O_001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "International GLONASS Service, Daily 30-second observation data, Greenbelt, MD, USA:NASA Crustal Dynamics Data Information System (CDDIS), Accessed [[enter user data access date]] at doi:10.5067/GLONASS/glonass_daily_o_001",
-            "issued": "1998-01-01",
-            "temporal": "1998-01-01T00:00:00Z/2025-01-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-17",
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
-            "identifier": "C1419744852-CDDIS",
             "description": "This dataset consists of ground-based Global Navigation Satellite System GLONASS Observation Data (30-second sampling, daily files) from the NASA Crustal Dynamics Data Information System (CDDIS). GNSS provide autonomous geo-spatial positioning with global coverage. The GLONASS data sets from ground receivers at the CDDIS consist of observations from the Russian GLObal NAvigation Satellite System (GLONASS); Russia's GLONASS is similar to the U.S. GPS in terms of the satellite constellation, orbits, and signal structure. The daily GLONASS GNSS observation files (un-compacted) contain one day of GLONASS observation (30-second sampling) data in RINEX format from a global permanent network of ground-based receivers, one file per site. More information about these data is available on the CDDIS website at https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/daily_30second_data.html.",
-            "title": "Ground-Based Global Navigation Satellite System GLONASS (GLObal NAvigation Satellite System) Observation Data (30-second sampling, daily files) from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGLONASS_DAILY_O_001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGLONASS_DAILY_O_001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/archive/glonass/data/daily",
-                    "description": "URL for retrieval of GNSS daily data through https",
                     "@type": "dcat:Distribution",
+                    "description": "URL for retrieval of GNSS daily data through https",
+                    "downloadURL": "https://cddis.nasa.gov/archive/glonass/data/daily",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/daily_30second_data.html",
-                    "description": "URL for more information about daily GLONASS observation data",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about daily GLONASS observation data",
+                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/daily_30second_data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/GNSS/GLONASS_DAILY_O_001",
-                    "description": "URL for more information about daily GLONASS observation data",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about daily GLONASS observation data",
+                    "downloadURL": "https://doi.org/10.5067/GNSS/GLONASS_DAILY_O_001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1419744852-CDDIS",
+            "issued": "1998-01-01",
+            "keyword": [
+                "earth science",
+                "solid earth",
+                "geodetics",
+                "gravity/gravitational field",
+                "tectonics"
+            ],
+            "landingPage": "https://doi.org/10.5067/GNSS/GLONASS_DAILY_O_001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "CDDIS"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1998-01-01T00:00:00Z/2025-01-20T00:00:00Z",
             "theme": [
                 "IGS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Ground-Based Global Navigation Satellite System GLONASS (GLObal NAvigation Satellite System) Observation Data (30-second sampling, daily files) from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PVO-V-ONMS-3-NEUTRALDENSITY-HIRES-V1.0",
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
+            "description": "This data set has at least preliminary composition for every data point measured but not necessarily final composition values. The instrument was designed to determine the composition of the neutral thermosphere/exosphere of Venus. The term composition includes both the type of neutral gases present and their quantitative amount. The measurements begin at the orbit's periapsis altitude and extend to a limiting altitude at which the ambient signal becomes comparable to the gas background and/or detector measurement threshold. The neutral composition includes helium, atomic nitrogen, atomic oxygen, molecular nitrogen, carbon monoxide and carbon dioxide. The data reduction has been described in [NIEMANNETAL1980A] and [KASPRZAKETAL1980].",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.pvo-v-onms-3-neutraldensity-hires-v1.0_4xmz-qbnz",
+            "issued": "2018-06-26",
+            "keyword": [
+                "pioneer venus",
+                "venus"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PVO-V-ONMS-3-NEUTRALDENSITY-HIRES-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.pvo-v-onms-3-neutraldensity-hires-v1.0_4xmz-qbnz",
-            "description": "This data set has at least preliminary composition for every data point measured but not necessarily final composition values. The instrument was designed to determine the composition of the neutral thermosphere/exosphere of Venus. The term composition includes both the type of neutral gases present and their quantitative amount. The measurements begin at the orbit's periapsis altitude and extend to a limiting altitude at which the ambient signal becomes comparable to the gas background and/or detector measurement threshold. The neutral composition includes helium, atomic nitrogen, atomic oxygen, molecular nitrogen, carbon monoxide and carbon dioxide. The data reduction has been described in [NIEMANNETAL1980A] and [KASPRZAKETAL1980].",
-            "title": "PVO VENUS ONMS CALIBRATED NEUTRAL DENSITY HIGH RES. V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "PVO VENUS ONMS CALIBRATED NEUTRAL DENSITY HIGH RES. V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S%2FJ%2FE%2FV-SPICE-6-V1.0",
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
+            "description": "This data set includes the complete set of Cassini SPICE data files (``kernel files''), which can be accessed using SPICE software. The SPICE data contains geometric and other ancillary information needed to recover the full value of science instrument data. In particular SPICE kernels provide spacecraft and planetary ephemerides, instrument mounting alignments, spacecraft orientation, spacecraft sequences of events, and data needed for relevant time conversions.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-j-e-v-spice-6-v1.0_4xnz-rijx",
+            "issued": "2018-06-26",
+            "keyword": [
+                "cassini-huygens",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S%2FJ%2FE%2FV-SPICE-6-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-j-e-v-spice-6-v1.0_4xnz-rijx",
-            "description": "This data set includes the complete set of Cassini SPICE data files (``kernel files''), which can be accessed using SPICE software. The SPICE data contains geometric and other ancillary information needed to recover the full value of science instrument data. In particular SPICE kernels provide spacecraft and planetary ephemerides, instrument mounting alignments, spacecraft orientation, spacecraft sequences of events, and data needed for relevant time conversions.",
-            "title": "CASSINI SPICE KERNELS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI SPICE KERNELS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-NAVCAM-5-MOSAIC-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-navcam-5-mosaic-ops-v1.0_4xpr-ncsz",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-NAVCAM-5-MOSAIC-OPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-navcam-5-mosaic-ops-v1.0_4xpr-ncsz",
-            "description": "NULL",
-            "title": "MER 2 MARS NAVIGATION CAMERA\n                                      MOSAICS RDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MER 2 MARS NAVIGATION CAMERA\n                                      MOSAICS RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D25.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang. 2021-02-22. MODIS/Terra+Aqua BRDF/Albedo Parameter1 NIR Daily L3 Global 30ArcSec CMG V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MCD43D25.061. https://doi.org/10.5067/MODIS/MCD43D25.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-02-22",
-            "temporal": "2000-02-16T00:00:00Z/2024-05-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-22",
-            "keyword": [
-                "national geospatial data asset",
-                "ngda",
-                "surface radiative properties",
-                "land surface",
-                "earth science"
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
-            "identifier": "C2540268566-LPCLOUD",
-            "description": "The MCD43D25 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) Model Parameter dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. Each of the three model parameters (isotropic, volumetric, and geometric) for each of the MODIS bands 1 through 7 and the visible, near infrared (NIR), and shortwave bands included in MCD43C1 (https://doi.org/10.5067/MODIS/MCD43C1.061) are stored in a separate file as MCD43D01 through MCD43D30. \r\n\r\nMCD43D25 is the BRDF isotropic parameter for the MODIS NIR broadband. The isotropic parameter, in conjunction with the volumetric and geometric parameters, is used to derive the BRDF/Albedo values for the MODIS NIR broadband. \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
-            "release-place": "Sioux Falls, South Dakota, USA",
             "creator": "Crystal Schaaf, Zhuosen Wang",
-            "title": "MODIS/Terra+Aqua BRDF/Albedo Parameter1 NIR Daily L3 Global 30ArcSec CMG V061",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MCD43D25 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) Model Parameter dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. Each of the three model parameters (isotropic, volumetric, and geometric) for each of the MODIS bands 1 through 7 and the visible, near infrared (NIR), and shortwave bands included in MCD43C1 (https://doi.org/10.5067/MODIS/MCD43C1.061) are stored in a separate file as MCD43D01 through MCD43D30. \r\n\r\nMCD43D25 is the BRDF isotropic parameter for the MODIS NIR broadband. The isotropic parameter, in conjunction with the volumetric and geometric parameters, is used to derive the BRDF/Albedo values for the MODIS NIR broadband. \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D25.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D25.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D25.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D25.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2540268566-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2540268566-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D25.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D25.061",
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
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MCD43D25",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MCD43D25",
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
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D25.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D25.061/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2540268566-LPCLOUD",
+            "issued": "2021-02-22",
+            "keyword": [
+                "national geospatial data asset",
+                "ngda",
+                "surface radiative properties",
+                "land surface",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D25.061",
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
+            "title": "MODIS/Terra+Aqua BRDF/Albedo Parameter1 NIR Daily L3 Global 30ArcSec CMG V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1350",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Newcomer, J.A., D.R. Landis, S. Conrad, S. Curd, K.F. Huemmrich, D.E. Knapp, A. Morrell, J.E. Nickeson, A. Papagno, D. Rinker, R.F. Strub, T. Twine, F.G. Hall, and P.J. Sellers. 2016. Collected Data from The Boreal Ecosystem-Atmosphere Study, NASA, CD-ROM. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1350",
-            "issued": "2022-05-10",
-            "temporal": "1993-01-01T00:00:00Z/1997-03-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-15",
-            "keyword": [
-                "land surface",
-                "atmosphere",
-                "atmospheric chemistry",
-                "atmospheric pressure",
-                "atmospheric radiation",
-                "atmospheric temperature",
-                "biosphere",
-                "earth science",
-                "ecological dynamics",
-                "ecosystems",
-                "soils",
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
-            "identifier": "C2767504386-ORNL_CLOUD",
             "description": "This data set provides Boreal Ecosystem-Atmosphere Study (BOREAS) project information and data collected at selected sites in the boreal forest of Saskatchewan and Manitoba, Canada from 1993 through 1996. The data include surface, airborne, and satellite-based observations. Note that all of the data products on these CDs have been archived as separate BOREAS data sets by the ORNL DAAC and in many cases the published data are later versions. Users should search for BOREAS data among these individual data sets. These data were originally distributed on 12 CD-ROMs, but are now archived as 12 zip files to ensure historical completeness of the BOREAS data record.",
-            "graphic-preview-description": "Browse Image",
-            "title": "Collected Data from The Boreal Ecosystem-Atmosphere Study, NASA, CD-ROM",
-            "graphic-preview-file": "https://daac.ornl.gov/BOREAS/guides/BOREAS_CDS_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1350",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1350",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/STAFF/BOREAS_CDS/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/STAFF/BOREAS_CDS/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/BOREAS_CDS.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/BOREAS_CDS.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1350",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1350",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/BOREAS_CDS/comp/BOREAS_CDS.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/BOREAS_CDS/comp/BOREAS_CDS.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/BOREAS_CDS/comp/BOREAS_CDS_Fig1.png",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/BOREAS_CDS/comp/BOREAS_CDS_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/BOREAS_CDS_Fig1.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/BOREAS_CDS_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/BOREAS/guides/BOREAS_CDS_Fig1.png",
+            "identifier": "C2767504386-ORNL_CLOUD",
+            "issued": "2022-05-10",
+            "keyword": [
+                "land surface",
+                "atmosphere",
+                "atmospheric chemistry",
+                "atmospheric pressure",
+                "atmospheric radiation",
+                "atmospheric temperature",
+                "biosphere",
+                "earth science",
+                "ecological dynamics",
+                "ecosystems",
+                "soils",
+                "surface radiative properties",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1350",
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
             "spatial": "-111.0 50.09 -93.5 59.98",
+            "temporal": "1993-01-01T00:00:00Z/1997-03-31T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Collected Data from The Boreal Ecosystem-Atmosphere Study, NASA, CD-ROM"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC3-67P-M19-REFLECT-V1.0",
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
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-07-28T23:25:00.000 to 2015-08-25T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc3-67p-m19-reflect-v1.0_4xr6-u3c2",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC3-67P-M19-REFLECT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc3-67p-m19-reflect-v1.0_4xr6-u3c2",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-07-28T23:25:00.000 to 2015-08-25T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC3-MTP019 RDR-REFLECT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC3-MTP019 RDR-REFLECT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1237207594-LARC_ASDC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2016-04-25. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC.",
-            "issued": "2016-02-13",
-            "temporal": "2000-03-01T00:00:00Z/2007-12-12T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-02-13",
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
-            "identifier": "C1237207594-LARC_ASDC",
             "description": "CER_GEO_Ed4_GOE10_SH_V01 is the Satellite Cloud and Radiation Property retrieval System (SatCORPS) Clouds and the Earth's Radiant Energy System (CERES) Geostationary Satellite (GEO) Edition 4 Geostationary Operational Environmental Satellite 10 (GOES-10) over the Southern Hemisphere (SH) Version 1.0 data product. Data was collected using the GOES-I-M Imager on the GOES-10 Platform. Data collection for this product is complete.\r\n\r\nThis data set comprises cloud micro-physical and radiation properties derived hourly from GOES-10 geostationary satellite imager data using the Langley Research Center's (LARC) SATCORPS algorithms supporting the CERES project. The cloud micro-physical and radiation properties from each active geostationary satellite are merged to create hourly global cloud properties that estimate fluxes between CERES instrument measurements to account for the changing diurnal cycle. The data set is arranged as files for each hour and in netCDF-4 format. The observations are at 4 km resolution (at nadir) and are sub-sampled to 8 km.\r\n\r\nCERES is a key Earth Observing System (EOS) program component. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions follow the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument, the protoflight model (PFM), was launched on November 27, 1997, as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the Earth Observing System (EOS) flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board Earth Observing System (EOS) Aqua on May 4, 2002. The CERES FM5 instrument was launched on board the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The newest CERES instrument (FM6) was launched on board the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite, now called NOAA-20, on November 18, 2017.",
-            "graphic-preview-description": "Mission Logo",
-            "title": "SatCORPS CERES GEO Edition 4 GOES-10 Southern Hemisphere Version 1.0",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1237207594-LARC_ASDC",
-                    "description": "Earthdata Search for CER_GEO_Ed4_GOE10_SH_V01 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CER_GEO_Ed4_GOE10_SH_V01 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1237207594-LARC_ASDC",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
-                    "description": "ASDC's data citation policy",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC's data citation policy",
+                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data citation policy"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/GEO/Edition4/GOE10_SH_V01/",
-                    "description": "ASDC Direct Data Download for CER_GEO_Ed4_GOE10_SH_V01",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CER_GEO_Ed4_GOE10_SH_V01",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/GEO/Edition4/GOE10_SH_V01/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/GEO/Edition4/GOE10_SH_V01/contents.html",
-                    "description": "OPeNDAP data access for CER_GEO_Ed4_GOE10_SH_V01",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CER_GEO_Ed4_GOE10_SH_V01",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/GEO/Edition4/GOE10_SH_V01/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Mission Logo",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/ceres.png",
+            "identifier": "C1237207594-LARC_ASDC",
+            "issued": "2016-02-13",
+            "keyword": [
+                "atmosphere",
+                "clouds",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1237207594-LARC_ASDC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2016-02-13",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-60.0 -180.0 -60.0 -30.0 0.0 -30.0 0.0 -180.0 -60.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2000-03-01T00:00:00Z/2007-12-12T23:59:59.999Z",
             "theme": [
                 "CERES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SatCORPS CERES GEO Edition 4 GOES-10 Southern Hemisphere Version 1.0"
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
+            "description": "This data set contains Calibrated data taken by the New Horizons Long Range Reconnaissance Imager instrument during the pluto cruise mission phase.  This is VERSION 1.0 of this data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-lorri-3-plutocruise-v1.0_4xtg-az7w",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "uranus",
                 "styx",
@@ -162080,224 +162082,198 @@
                 "pluto",
                 "star"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-LORRI-3-PLUTOCRUISE-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-lorri-3-plutocruise-v1.0_4xtg-az7w",
-            "description": "This data set contains Calibrated data taken by the New Horizons Long Range Reconnaissance Imager instrument during the pluto cruise mission phase.  This is VERSION 1.0 of this data set.",
-            "title": "NEW HORIZONS\n      LORRI PLUTO CRUISE\n      CALIBRATED V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS\n      LORRI PLUTO CRUISE\n      CALIBRATED V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2153",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Fichot, C.G., and J. Harringmeyer. 2023. Delta-X: In Situ Water Surface Reflectance across MRD, LA, USA, 2021, V3. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2153",
-            "issued": "2023-09-21",
-            "temporal": "2021-03-25T14:43:00Z/2021-09-24T16:44:22Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-26",
-            "keyword": [
-                "geomorphic landforms/processes",
-                "ecosystems",
-                "earth science",
-                "biosphere",
-                "surface radiative properties",
-                "water quality/water chemistry",
-                "terrestrial hydrosphere",
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
-            "identifier": "C2772847105-ORNL_CLOUD",
             "description": "This dataset includes above water measurements of remote-sensing reflectance measured in situ at field sampling stations during the Delta-X 2021 field efforts. Measurements were collected in the Atchafalaya River and Terrebonne Basins on the southern coast of Louisiana from 2021-03-25 to 2021-04-22 (spring) and from 2021-08-14 to 2021-09-24 (fall). Field sampling was paused on 2021-08-25 and resumed on 2021-09-13 due to the landfall of Hurricane Ida on 2021-08-26 approximately 70 km east of the study site. Water quality changes caused by the hurricane were expected to be minimal. Reflectance was measured near-simultaneously with collection of field samples and in-water sediment parameters in multiple channels of varying width (from a few meters to >100 m), near Delta-X intensive study sites, in open bays and lakes, and at a few locations in the nearshore Gulf of Mexico. For each in situ collection, a handheld Portable SpectroRadiometer (PSR-1100f, Spectral Evolution) was used to measure radiance from: (a) a highly reflective (>99% reflectance) Lambertian Spectralon panel (b) from the sky, measured at 40 degrees from the solar zenith and at 135 degrees from the sun azimuthal plane, (c) from the water, measured at 40 degrees from nadir and at 135 degrees from the sun azimuthal plane. These measurements were used to calculate remote-sensing reflectance and the water-leaving radiance relative to downwelling irradiance, including a correction for the influence of reflected skylight. In Version 3, the data files with this dataset replace and update the data files in Version 2. A minor update was made to the code used to calculate the remote sensing reflectance (Rrs). These data are provided in comma-separated values (.csv) format.",
-            "graphic-preview-description": "Figure 1: Collection of water-leaving radiance measurement using the Portable SpectroRadiometer (PSR).",
-            "title": "Delta-X: In Situ Water Surface Reflectance across MRD, LA, USA, 2021, V3",
-            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Insitu_Reflectance_V3_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2153",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2153",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/deltax/DeltaX_Insitu_Reflectance_V3/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/deltax/DeltaX_Insitu_Reflectance_V3/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Insitu_Reflectance_V3.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Insitu_Reflectance_V3.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2153",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2153",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/DeltaX_Insitu_Reflectance_V3/comp/DeltaX_Insitu_Reflectance_V3.pdf",
-                    "description": "Delta-X: In Situ Water Surface Reflectance across MRD, LA, USA, 2021, V3: DeltaX_Insitu_Reflectance_V3.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Delta-X: In Situ Water Surface Reflectance across MRD, LA, USA, 2021, V3: DeltaX_Insitu_Reflectance_V3.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/DeltaX_Insitu_Reflectance_V3/comp/DeltaX_Insitu_Reflectance_V3.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Insitu_Reflectance_V3_Fig1.jpg",
-                    "description": "Figure 1: Collection of water-leaving radiance measurement using the Portable SpectroRadiometer (PSR).",
                     "@type": "dcat:Distribution",
+                    "description": "Figure 1: Collection of water-leaving radiance measurement using the Portable SpectroRadiometer (PSR).",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Insitu_Reflectance_V3_Fig1.jpg",
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
+            "graphic-preview-description": "Figure 1: Collection of water-leaving radiance measurement using the Portable SpectroRadiometer (PSR).",
+            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Insitu_Reflectance_V3_Fig1.jpg",
+            "identifier": "C2772847105-ORNL_CLOUD",
+            "issued": "2023-09-21",
+            "keyword": [
+                "geomorphic landforms/processes",
+                "ecosystems",
+                "earth science",
+                "biosphere",
+                "surface radiative properties",
+                "water quality/water chemistry",
+                "terrestrial hydrosphere",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2153",
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
             "spatial": "-91.47 28.79 -90.57 29.75",
+            "temporal": "2021-03-25T14:43:00Z/2021-09-24T16:44:22Z",
             "theme": [
                 "Delta-X",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Delta-X: In Situ Water Surface Reflectance across MRD, LA, USA, 2021, V3"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GPM/AMSR2/GCOMW1/3A-MONTH/07",
             "citation": "GPM Science Team. 2022-05-09. GPM_3GPROFGCOMW1AMSR2. Version 07. GPM AMSR-2 on GCOM-W1 (GPROF) Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/AMSR2/GCOMW1/3A-MONTH/07. https://disc.gsfc.nasa.gov/datacollection/GPM_3GPROFGCOMW1AMSR2_07.html. Digital Science Data.",
-            "issued": "2022-05-09",
-            "temporal": "2014-02-01T00:00:00Z/2023-03-01T00:00:00Z",
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
-            "identifier": "C2264134680-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Version 07 is the current version of the data set. Older versions will no longer be available and have been superseded by Version 07.\n\n3GPROF products provide global gridded monthly/daily precipitation averages from multiple satellites that can be used for climate studies. The 3GPROF products are based on retrievals from high-quality microwave sensors, which are sensitive to liquid and ice-phase precipitation hydrometeors in the atmosphere.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "GPM_3GPROFGCOMW1AMSR2",
-            "creator": "GPM Science Team",
-            "title": "GPM AMSR-2 on GCOM-W1 (GPROF) Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFGCOMW1AMSR2) at GES DISC",
-            "graphic-preview-description": "Surface Precipitation from AMSR2 (25 km x 25 km)(GPM_3GPROFGCOMW1AMSR2)",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFGCOMW1AMSR2_07.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FAMSR2%2FGCOMW1%2F3A-MONTH%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FAMSR2%2FGCOMW1%2F3A-MONTH%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFGCOMW1AMSR2_07.png",
-                    "description": "Surface Precipitation from AMSR2 (25 km x 25 km)(GPM_3GPROFGCOMW1AMSR2)",
                     "@type": "dcat:Distribution",
+                    "description": "Surface Precipitation from AMSR2 (25 km x 25 km)(GPM_3GPROFGCOMW1AMSR2)",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFGCOMW1AMSR2_07.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3GPROFGCOMW1AMSR2_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3GPROFGCOMW1AMSR2_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3GPROFGCOMW1AMSR2.07/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3GPROFGCOMW1AMSR2.07/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L3/GPM_3GPROFGCOMW1AMSR2.07/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L3/GPM_3GPROFGCOMW1AMSR2.07/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/dods/GPM_3GPROFGCOMW1AMSR2_07.info",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/dods/GPM_3GPROFGCOMW1AMSR2_07.info",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3GPROFGCOMW1AMSR2_07",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3GPROFGCOMW1AMSR2_07",
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
@@ -162307,135 +162283,136 @@
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
+            "graphic-preview-description": "Surface Precipitation from AMSR2 (25 km x 25 km)(GPM_3GPROFGCOMW1AMSR2)",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFGCOMW1AMSR2_07.png",
+            "identifier": "C2264134680-GES_DISC",
+            "issued": "2022-05-09",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "precipitation",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/AMSR2/GCOMW1/3A-MONTH/07",
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
+            "series-name": "GPM_3GPROFGCOMW1AMSR2",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2014-02-01T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "GPM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM AMSR-2 on GCOM-W1 (GPROF) Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFGCOMW1AMSR2) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1625796323-LARC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MISR Science Team (2006), Terra/MISR Level 1, Terrain Product subset for the GoMACCS region, version 3, Hampton, VA, USA: NASA Atmospheric Science Data Center (ASDC), Accessed <author citing data inserts date here> at doi: TBD",
-            "issued": "2019-07-22",
-            "temporal": "2006-07-30T16:36:08.530Z/2006-10-16T17:49:35.096Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-07-22",
-            "keyword": [
-                "earth science",
-                "visible wavelengths",
-                "spectral/engineering"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Veljko Jovanovic",
                 "hasEmail": "mailto:veljko.m.jovanovic@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1625796323-LARC",
             "description": "Multi-angle Imaging SpectroRadiometer (MISR) is an instrument designed to view Earth with cameras pointed in 9 different directions. As the instrument flies overhead, each piece of Earth's surface below is successively imaged by all 9 cameras, in each of 4 wavelengths (blue, green, red, and near-infrared). The goal of MISR is to improve our understanding of the fate of sunlight in Earth environment, as well as distinguish different types of clouds, particles and surfaces. Specifically, MISR monitors the monthly, seasonal, and long-term trends in three areas: 1) amount and type of atmospheric particles (aerosols), including those formed by natural sources and by human activities; 2) amounts, types, and heights of clouds, and 3) distribution of land surface cover, including vegetation canopy structure. MISR Level 1B2 Terrain Product subset for the GoMACCS region V003 contains Terrain-projected TOA Radiance, resampled at the surface and topographically corrected, as well as geometrically corrected by PGE22.",
-            "title": "MISR Level 1B2 Terrain Product subset for the GoMACCS region V003",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1625796323-LARC.html",
-                    "description": "View this dataset on the CMR (Common Metadata Repository)",
                     "@type": "dcat:Distribution",
+                    "description": "View this dataset on the CMR (Common Metadata Repository)",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1625796323-LARC.html",
+                    "mediaType": "text/html",
                     "title": "CMR"
                 }
             ],
+            "identifier": "C1625796323-LARC",
+            "issued": "2019-07-22",
+            "keyword": [
+                "earth science",
+                "visible wavelengths",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1625796323-LARC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-07-22",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2006-07-30T16:36:08.530Z/2006-10-16T17:49:35.096Z",
             "theme": [
                 "GOMACCS_2006",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR Level 1B2 Terrain Product subset for the GoMACCS region V003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/HXRNU4HCIPA6",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wilcox, E. M., Yuan, T. and Song, H., . MOD_L2_DC. Version 001. MODIS Terra L2 deep-convective cloud classification. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/HXRNU4HCIPA6. https://disc.gsfc.nasa.gov/datacollection/MOD_L2_DC_001.html. Digital Science Data.",
-            "issued": "2023-02-05",
-            "temporal": "2001-01-01T00:00:00Z/2023-12-31T23:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-02-05",
-            "keyword": [
-                "national geospatial data asset",
-                "clouds",
-                "earth science",
-                "atmosphere",
-                "ngda"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ashley Heath",
                 "hasEmail": "mailto:ashley.l.heath@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C2767303254-GES_DISC",
-            "description": "MODIS Terra L2 deep-convective cloud classification (DC) are part of our global MODIS Terra data from the 2017 MEaSUREs project, A Comprehensive Data Record of Marine Low-level and Deep Convective Cloud Systems Using an Object-Oriented Approach.",
-            "series-name": "MOD_L2_DC",
             "creator": "Wilcox, E. M., Yuan, T. and Song, H.,",
-            "title": "MODIS Terra L2 deep-convective cloud classification",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/MOD_L2_DC_001.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "MODIS Terra L2 deep-convective cloud classification (DC) are part of our global MODIS Terra data from the 2017 MEaSUREs project, A Comprehensive Data Record of Marine Low-level and Deep Convective Cloud Systems Using an Object-Oriented Approach.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FHXRNU4HCIPA6",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FHXRNU4HCIPA6",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -162445,82 +162422,85 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/MOD_L2_DC_001.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/MOD_L2_DC_001.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/CloudObjects/MOD_L2_DC.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/CloudObjects/MOD_L2_DC.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=MOD_L2_DC_001",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=MOD_L2_DC_001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/CloudObjects/MOD_L2_DC.001/doc/README.CLOUD_MODIS_DC.001.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/CloudObjects/MOD_L2_DC.001/doc/README.CLOUD_MODIS_DC.001.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/MOD_L2_DC_001.png",
+            "identifier": "C2767303254-GES_DISC",
+            "issued": "2023-02-05",
+            "keyword": [
+                "national geospatial data asset",
+                "clouds",
+                "earth science",
+                "atmosphere",
+                "ngda"
+            ],
+            "landingPage": "https://doi.org/10.5067/HXRNU4HCIPA6",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-02-05",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "series-name": "MOD_L2_DC",
             "spatial": "-180.0 -60.0 180.0 60.0",
+            "temporal": "2001-01-01T00:00:00Z/2023-12-31T23:00:00Z",
             "theme": [
                 "MEaSUREs",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS Terra L2 deep-convective cloud classification"
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
-                "validation",
-                "tool",
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
-            "identifier": "NASA-786",
             "description": "PDS Validation Tool (1.0.0)",
-            "title": "PDS Software Release Validation Tool (1.0.0)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -162528,642 +162508,638 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-786",
+            "issued": "2018-06-25",
+            "keyword": [
+                "validation",
+                "tool",
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
+            "title": "PDS Software Release Validation Tool (1.0.0)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/AIRMISR_SNOW_ICE_2001_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2001-05-24. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/AIRMISR_SNOW_ICE_2001_1.",
-            "issued": "2001-06-29",
-            "temporal": "2001-03-08T00:00:00Z/2001-03-08T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-04-26",
-            "keyword": [
-                "spectral/engineering",
-                "visible wavelengths",
-                "infrared wavelengths",
-                "earth science"
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
-            "identifier": "C1000000728-LARC_ASDC",
             "description": "The AIRMISR_SNOW_ICE_2001 data were acquired during the Colorado snow albedo field experiment in the Yampa Valley of Colorado during February and March, 2001. This experiment focused on snow albedo and atmospheric characterization as part of a validation effort for estimating snow albedo from the Multiangle Imaging SpectroRadiometer (MISR) and the Moderate Resolution Imaging Spectroradiometer (MODIS) data. The validation site is located at 40.4N, 106.8W, just south of Steamboat Springs, Colorado. AirMISR and MODIS Airborne Simulator (MAS) data were collected on March 8, 2001. The Airborne Multi-angle Imaging SpectroRadiometer (AirMISR) is an airborne instrument for obtaining multi-angle imagery similar to that of the satellite-borne Multi-angle Imaging SpectroRadiometer (MISR) instrument, which is designed to contribute to studies of the Earth's ecology and climate. AirMISR flies on the NASA ER-2 aircraft. The Jet Propulsion Laboratory in Pasadena, California built the instrument for NASA. Unlike the satellite-borne MISR instrument, which has nine cameras oriented at various angles, AirMISR uses a single camera in a pivoting gimbal mount. A data run by the ER-2 aircraft is divided into nine segments, each with the camera positioned to a MISR look angle. The gimbal rotates between successive segments, such that each segment acquires data over the same area on the ground as the previous segment. This process is repeated until all nine angles of the target area are collected. The swath width, which varies from 11 km in the nadir to 32 km at the most oblique angle, is governed by the camera's instantaneous field-of-view of 7 meters cross-track x 6 meters along-track in the nadir view and 21 meters x 55 meters at the most oblique angle. The along-track image length at each angle is dictated by the timing required to obtain overlap imagery at all angles, and varies from about 9 km in the nadir to 26 km at the most oblique angle. Thus, the nadir image dictates the area of overlap that is obtained from all nine angles. A complete flight run takes approximately 13 minutes.The 9 camera viewing angles are:0 degrees or nadir26.1 degrees, fore and aft45.6 degrees, fore and aft60.0 degrees, fore and aft70.5 degrees, fore and aftFor each of the camera angles, images are obtained at 4 spectral bands. The spectral bands can be used to identify vegetation and aerosols, estimate surface reflectance and ocean color studies. The center wavelengths of the 4 spectral bands are:443 nanometers, blue555 nanometers, green670 nanometers, red865 nanometers, near-infraredTwo types of AirMISR data products are available - the Level 1 Radiometric product (L1B1) and the Level 1 Georectified radiance product (L1B2).",
-            "graphic-preview-description": "AirMISR Campaign Imagery: Red Band Browse Images from the AIRMISR_SNOW_ICE_2001 Field Mission, March 8, 2001",
-            "title": "Airborne Multi-angle Imaging SpectroRadiometer (AirMISR) Data from the Snow and Ice 2001 Campaign",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/airmisr/airmisr_SNOW_ICE_2001_images.html",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FAIRMISR_SNOW_ICE_2001_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FAIRMISR_SNOW_ICE_2001_1",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000728-LARC_ASDC",
-                    "description": "Earthdata Search for AIRMISR_SNOW_ICE_2001_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for AIRMISR_SNOW_ICE_2001_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000728-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/readme/readme_airmisr_snow_ice_2001",
-                    "description": "Readme Information about the AirMISR field mission which focused on the reflective properties of snow over the Yampa Valley of Colorado from February to March, 2001",
                     "@type": "dcat:Distribution",
+                    "description": "Readme Information about the AirMISR field mission which focused on the reflective properties of snow over the Yampa Valley of Colorado from February to March, 2001",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/readme/readme_airmisr_snow_ice_2001",
+                    "mediaType": "text/html",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/quality_summaries/airmisr_snow_ice_2001.pdf",
-                    "description": "Quality Summary: AirMISR SNOW_ICE_2001",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Summary: AirMISR SNOW_ICE_2001",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/quality_summaries/airmisr_snow_ice_2001.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/AIRMISR_SNOW_ICE_2001_1",
-                    "description": "DOI data set landing page for AIRMISR_SNOW_ICE_2001_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for AIRMISR_SNOW_ICE_2001_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/AIRMISR_SNOW_ICE_2001_1",
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
-                    "downloadURL": "https://eospso.gsfc.nasa.gov/atbd-category/45",
-                    "description": "NASA EOS ATB Documents: MISR",
                     "@type": "dcat:Distribution",
+                    "description": "NASA EOS ATB Documents: MISR",
+                    "downloadURL": "https://eospso.gsfc.nasa.gov/atbd-category/45",
+                    "mediaType": "text/html",
                     "title": "View this dataset's algorithm theoretical basis document"
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
-                    "downloadURL": "https://www.fs.usda.gov/rmrs/groups/larse",
-                    "description": "USDA Overview of Laboratory for Applications of Remote Sensing in Ecology (LARSE)",
                     "@type": "dcat:Distribution",
+                    "description": "USDA Overview of Laboratory for Applications of Remote Sensing in Ecology (LARSE)",
+                    "downloadURL": "https://www.fs.usda.gov/rmrs/groups/larse",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/tools/coregister_L1B2_L2AS.pro",
-                    "description": "AirMISR L1B2/L2AS Coregistration Tool IDL source code - Direct File Download (.pro)",
                     "@type": "dcat:Distribution",
+                    "description": "AirMISR L1B2/L2AS Coregistration Tool IDL source code - Direct File Download (.pro)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/tools/coregister_L1B2_L2AS.pro",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/tools/coregister_L1B2_L2AS.sav",
-                    "description": "AirMISR L1B2/L2AS Coregistration Tool  IDL executable save file (use with the IDL Virtual Machine) - Direct File Download (.sav)",
                     "@type": "dcat:Distribution",
+                    "description": "AirMISR L1B2/L2AS Coregistration Tool  IDL executable save file (use with the IDL Virtual Machine) - Direct File Download (.sav)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/tools/coregister_L1B2_L2AS.sav",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/tools/readme_L1B2_L2AS_coregistration_tool.txt",
-                    "description": "AirMISR L1B2/L2AS Coregistration Tool Readme",
                     "@type": "dcat:Distribution",
+                    "description": "AirMISR L1B2/L2AS Coregistration Tool Readme",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/tools/readme_L1B2_L2AS_coregistration_tool.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/airmisr_SNOW_ICE_2001_images.html",
-                    "description": "AirMISR Campaign Imagery: Red Band Browse Images from the AIRMISR_SNOW_ICE_2001 Field Mission, March 8, 2001",
                     "@type": "dcat:Distribution",
+                    "description": "AirMISR Campaign Imagery: Red Band Browse Images from the AIRMISR_SNOW_ICE_2001 Field Mission, March 8, 2001",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/airmisr_SNOW_ICE_2001_images.html",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/AirMISR/AIRMISR_SNOW_ICE_2001/",
-                    "description": "ASDC Direct Data Download for AIRMISR_SNOW_ICE_2001_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for AIRMISR_SNOW_ICE_2001_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/AirMISR/AIRMISR_SNOW_ICE_2001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/AirMISR/AIRMISR_SNOW_ICE_2001/contents.html",
-                    "description": "OPeNDAP data access for AIRMISR_SNOW_ICE_2001_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for AIRMISR_SNOW_ICE_2001_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/AirMISR/AIRMISR_SNOW_ICE_2001/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "graphic-preview-description": "AirMISR Campaign Imagery: Red Band Browse Images from the AIRMISR_SNOW_ICE_2001 Field Mission, March 8, 2001",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/airmisr/airmisr_SNOW_ICE_2001_images.html",
+            "identifier": "C1000000728-LARC_ASDC",
+            "issued": "2001-06-29",
+            "keyword": [
+                "spectral/engineering",
+                "visible wavelengths",
+                "infrared wavelengths",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/AIRMISR_SNOW_ICE_2001_1",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>36.27 -114.4 36.27 -106.38 40.75 -106.38 40.75 -114.4 36.27 -114.4</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2001-03-08T00:00:00Z/2001-03-08T23:59:59.999Z",
             "theme": [
                 "AIRMISR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Airborne Multi-angle Imaging SpectroRadiometer (AirMISR) Data from the Snow and Ice 2001 Campaign"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-GRS-2-EDR-EROS%2FSURFACE-V1.0",
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
+            "description": "This data set contains Gamma Ray Spectrometer (GRS) observations made during the Eros surface phase of the NEAR mission. Only the GRF sensor made observations from the surface of Eros.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-grs-2-edr-eros-surface-v1.0_4y5x-evr9",
+            "issued": "2021-05-21",
+            "keyword": [
+                "eros",
+                "near earth asteroid rendezvous"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-GRS-2-EDR-EROS%2FSURFACE-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-grs-2-edr-eros-surface-v1.0_4y5x-evr9",
-            "description": "This data set contains Gamma Ray Spectrometer (GRS) observations made during the Eros surface phase of the NEAR mission. Only the GRF sensor made observations from the surface of Eros.",
-            "title": "NEAR GRS SPECTRA FOR EROS SURFACE PHASE",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEAR GRS SPECTRA FOR EROS SURFACE PHASE"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-PRL-67PCHURYUMOV-M07-V1.0",
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
+            "description": "This data set contains raw EDR images acquired by the OSIRIS Wide Angle\nCamera during the prelanding phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-09-02 to 2014-09-16.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-prl-67pchuryumov-m07-v1.0_4y6s-724z",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-PRL-67PCHURYUMOV-M07-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-prl-67pchuryumov-m07-v1.0_4y6s-724z",
-            "description": "This data set contains raw EDR images acquired by the OSIRIS Wide Angle\nCamera during the prelanding phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-09-02 to 2014-09-16.",
-            "title": "ROSETTA-ORBITER COMET PRELANDING OSIWAC 2 EDR MTP 007 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMET PRELANDING OSIWAC 2 EDR MTP 007 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0604-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-02-26T00:07:05.000 to 2015-02-26T02:30:12.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0604-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0604-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0604-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-02-26T00:07:05.000 to 2015-02-26T02:30:12.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0604 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0604 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-OCCULTATIONS-V13.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set is intended to include all reported timings of observed asteroid, planet, and planetary satellite occultation events as well as occultation axes derived from those timings by David W. Dunham and David Herald. This version is complete through the end of 2014.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-occultations-v13.0_4y7p-7ynu",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "asteroid",
                 "satellite",
                 "support archives"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-OCCULTATIONS-V13.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-occultations-v13.0_4y7p-7ynu",
-            "description": "This data set is intended to include all reported timings of observed asteroid, planet, and planetary satellite occultation events as well as occultation axes derived from those timings by David W. Dunham and David Herald. This version is complete through the end of 2014.",
-            "title": "ASTEROID OCCULTATIONS V13.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ASTEROID OCCULTATIONS V13.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0879-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-07-06T03:21:40.000 to 2015-07-06T09:47:10.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0879-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0879-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0879-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-07-06T03:21:40.000 to 2015-07-06T09:47:10.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0879 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0879 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2022-01-27",
-            "temporal": "2022-01-27T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "location",
-                "trajectory",
-                "topo",
-                "station",
-                "space",
-                "iss",
-                "coordinates",
-                "coords",
-                "ephemeris",
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
-            "identifier": "nasa-iss-data_2022-01-27_4y9c-fn5g",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2022-01-27",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -163286,84 +163262,90 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2022-01-27_4y9c-fn5g",
+            "issued": "2022-01-27",
+            "keyword": [
+                "location",
+                "trajectory",
+                "topo",
+                "station",
+                "space",
+                "iss",
+                "coordinates",
+                "coords",
+                "ephemeris",
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
+            "temporal": "2022-01-27T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2022-01-27"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1078-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-04T20:53:10.000 to 2015-10-05T05:22:30.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1078-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1078-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1078-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-04T20:53:10.000 to 2015-10-05T05:22:30.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1078 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1078 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/4yfa-w3yk",
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
-                "geography",
-                "wise",
-                "space science"
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
-            "identifier": "NASA-0000038__13",
+            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
             "description": "Planetary nomenclature, like terrestrial nomenclature, is used to uniquely identify a feature on the surface of a planet or satellite so that the feature can be easily located, described, and discussed. This gazetteer contains detailed information about all names of topographic and albedo features on planets and satellites (and some planetary ring and ring-gap systems) that the International Astronomical Union (IAU) has named and approved from its founding in 1919 through the present time.",
-            "title": "Gazetteer of Planetary Nomenclature",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -163371,210 +163353,207 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
-            "accrualPeriodicity": "irregular"
+            "identifier": "NASA-0000038__13",
+            "issued": "2018-06-25",
+            "keyword": [
+                "nen",
+                "geography",
+                "wise",
+                "space science"
+            ],
+            "landingPage": "https://data.nasa.gov/d/4yfa-w3yk",
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-3-EXT3-MTP034-V1.0",
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
+            "description": "This dataset contains ROSETTA NAVCAM RADIOMETRICALLY CALIBRATED DATA of the ROSETTA EXTENSION 3 MTP034 Phase from 02 Sep. 2016, 11:19:32 to 26 Sep. 2016, 06:02:03 when at the vicinity of target 67P/CG.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-3-ext3-mtp034-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-3-EXT3-MTP034-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-3-ext3-mtp034-v1.0",
-            "description": "This dataset contains ROSETTA NAVCAM RADIOMETRICALLY CALIBRATED DATA of the ROSETTA EXTENSION 3 MTP034 Phase from 02 Sep. 2016, 11:19:32 to 26 Sep. 2016, 06:02:03 when at the vicinity of target 67P/CG.",
-            "title": "ROSETTA-ORBITER 67P NAVCAM 3 ROSETTA EXTENSION 3 MTP034 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P NAVCAM 3 ROSETTA EXTENSION 3 MTP034 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/LAKESUPERIOR/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/LAKESUPERIOR/DATA001.",
-            "issued": "2013-05-24",
-            "temporal": "2013-05-24T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean optics",
-                "oceans",
-                "ocean temperature",
-                "salinity/density",
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
-            "identifier": "C1633360420-OB_DAAC",
             "description": "Measurements made in Lake Superior by researchers at the University of Rhode Island.",
-            "title": "University of Rhode Island measurements in Lake Superior",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FLAKESUPERIOR%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FLAKESUPERIOR%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/LakeSuperior/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/LakeSuperior/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360420-OB_DAAC",
+            "issued": "2013-05-24",
+            "keyword": [
+                "ocean optics",
+                "oceans",
+                "ocean temperature",
+                "salinity/density",
+                "earth science",
+                "ocean chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/LAKESUPERIOR/DATA001",
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
+            "temporal": "2013-05-24T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "University of Rhode Island measurements in Lake Superior"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0942-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-08-05T03:04:30.000 to 2015-08-05T04:37:18.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0942-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0942-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0942-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-08-05T03:04:30.000 to 2015-08-05T04:37:18.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0942 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0942 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MR6%2FMR7-M-IRS-3-V1.0",
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
-                "mariner69"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set is a partial collection of spectra in digital form from the Mariner 6 and 7 Infrared Spectrometer experiments. All Mars and near-Mars sky spectra are included here, as well as some relevant laboratory spectra of blackbody sources. Lacking are the inflight spectra of reference targets including the wavelength calibration spectra. The IRS data are arranged as a single set of 512 spectra calibration spectra, followed by 122 Mariner 6 spectra, followed by 354 Mariner 7 spectra. The latter set is larger because the long-wavelength channel detector system failed on Mariner 6. These spectra are presented here in raw form, as originally supplied to the NSSDC on microfiche. Note that the geometry information in the spectrum headers was revised by the producer in 1984 to account for the revision in the location of the Mars pole following Mariner 9 observations.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mr6-mr7-m-irs-3-v1.0_4yj4-ih4v",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "mariner69"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MR6%2FMR7-M-IRS-3-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mr6-mr7-m-irs-3-v1.0_4yj4-ih4v",
-            "description": "This data set is a partial collection of spectra in digital form from the Mariner 6 and 7 Infrared Spectrometer experiments. All Mars and near-Mars sky spectra are included here, as well as some relevant laboratory spectra of blackbody sources. Lacking are the inflight spectra of reference targets including the wavelength calibration spectra. The IRS data are arranged as a single set of 512 spectra calibration spectra, followed by 122 Mariner 6 spectra, followed by 354 Mariner 7 spectra. The latter set is larger because the long-wavelength channel detector system failed on Mariner 6. These spectra are presented here in raw form, as originally supplied to the NSSDC on microfiche. Note that the geometry information in the spectrum headers was revised by the producer in 1984 to account for the revision in the location of the Mars pole following Mariner 9 observations.",
-            "title": "MR6/MR7 MARS INFRARED SPECTROMETER CALIBRATED DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MR6/MR7 MARS INFRARED SPECTROMETER CALIBRATED DATA V1.0"
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
-            "identifier": "NASA-862__13",
             "description": "Academy of Program/Project & Engineering Leadership's Ask the Academy magazine past issues.",
-            "title": "Academy of Program/Project & Engineering Leadership ASK the Academy Past Issues",
-            "programCode": [
-                "026:045"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -163582,146 +163561,143 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
+            "identifier": "NASA-862__13",
+            "issued": "2018-06-25",
+            "keyword": [
+                "ask the academy",
+                "appel",
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
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1349",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hilton, T.W., K.J. Davis, K. Keller, and N.M. Urban. 2016. NACP VPRM NEE Parameters Optimized to North American Flux Tower Sites, 2000-2006. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1349",
-            "issued": "2016-11-17",
-            "temporal": "2000-01-01T00:00:00Z/2007-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "earth science",
-                "atmospheric chemistry",
-                "atmosphere",
-                "biosphere",
-                "national geospatial data asset",
-                "vegetation",
-                "ngda",
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
-            "identifier": "C2517710454-ORNL_CLOUD",
             "description": "This data set provides Vegetation Photosynthesis Respiration Model (VPRM) net ecosystem exchange (NEE) parameter values optimized to 65 flux tower sites across North America. The parameters include the basal rate of ecosystem respiration (beta), the slope of respiration with respect to temperature (alpha), light-use efficiency (LUE) (lambda), and LUE curve half-saturation (PAR_0). Observed eddy covariance data from the 65 tower sites, locally observed temperature and photosynthetically active radiation (PAR) along with satellite-derived phenology and moisture were used as input data to optimize the VPRM parameters for the 65 sites. The data are provided by individual site, plant functional types (PFTs), and all sites together, and as monthly, annual, and all available data. The data are for the conterminous USA, Alaska, and Canada for the period 2000 to 2006.",
-            "graphic-preview-description": "Browse Image",
-            "title": "NACP VPRM NEE Parameters Optimized to North American Flux Tower Sites, 2000-2006",
-            "graphic-preview-file": "https://daac.ornl.gov/NACP/guides/VPRM_North_America_Parameters_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1349",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1349",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/nacp/VPRM_North_America_Parameters/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/nacp/VPRM_North_America_Parameters/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/NACP/guides/VPRM_North_America_Parameters.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/NACP/guides/VPRM_North_America_Parameters.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1349",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1349",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/VPRM_North_America_Parameters/comp/VPRM_North_America_Parameters.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/VPRM_North_America_Parameters/comp/VPRM_North_America_Parameters.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/NACP/guides/VPRM_North_America_Parameters_Fig1.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/NACP/guides/VPRM_North_America_Parameters_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/NACP/guides/VPRM_North_America_Parameters_Fig1.png",
+            "identifier": "C2517710454-ORNL_CLOUD",
+            "issued": "2016-11-17",
+            "keyword": [
+                "earth science",
+                "atmospheric chemistry",
+                "atmosphere",
+                "biosphere",
+                "national geospatial data asset",
+                "vegetation",
+                "ngda",
+                "ecological dynamics"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1349",
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
             "spatial": "-156.63 28.46 -68.74 71.32",
+            "temporal": "2000-01-01T00:00:00Z/2007-12-31T23:59:59Z",
             "theme": [
                 "NACP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NACP VPRM NEE Parameters Optimized to North American Flux Tower Sites, 2000-2006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aqua/AIRS/DATA330",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "AIRS Science Team/Joao Teixeira. 2013-03-12. AIRS3QPM. Version 006. AIRS/Aqua L3 Monthly Quantization in Physical Units (AIRS-only) 5 degrees x 5 degrees V006. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aqua/AIRS/DATA330. https://disc.gsfc.nasa.gov/datacollection/AIRS3QPM_006.html. Digital Science Data.",
-            "issued": "2002-09-01",
-            "temporal": "2002-09-01T00:00:00Z/2024-04-08T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-01",
-            "keyword": [
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "atmosphere",
-                "clouds",
-                "earth science"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ED ESFANDIARI",
                 "hasEmail": "mailto:asghar.e.esfandiari@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1238517283-GES_DISC",
-            "description": "The Atmospheric Infrared Sounder (AIRS) is a grating spectrometer (R = 1200) aboard the second Earth Observing System (EOS) polar-orbiting platform, EOS Aqua. In combination with the Advanced Microwave Sounding Unit (AMSU) and the Humidity Sounder for Brazil (HSB), AIRS constitutes an innovative atmospheric sounding group of visible, infrared, and microwave sensors. AIRS/Aqua Level 3 monthly quantization product is in physical units (AIRS Only). The quantization products (QP) are distributional summaries derived from the Level-2 standard retrieval products (of swath type) to provide a more comprehensive set of statistical summaries than the traditional means and standard deviation. The QP products combine the Level 2 standard data parameters over grid cells of 5 x 5 deg spatial extent for temporal periods of a month. They preserve the multivariate distributional features of the original data and so provide a compressed data set that more accurately describes the disparate atmospheric states that is in the original Level-2 swath data set. The geophysical parameters are: Air Temperature and Water Vapor profiles (11 levels/layers), Cloud fraction (vertical distribution).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "AIRS3QPM",
             "creator": "AIRS Science Team/Joao Teixeira",
-            "title": "AIRS/Aqua L3 Monthly Quantization in Physical Units (AIRS-only) 5 degrees x 5 degrees V006 (AIRS3QPM) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRS3QPM_006.gif",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The Atmospheric Infrared Sounder (AIRS) is a grating spectrometer (R = 1200) aboard the second Earth Observing System (EOS) polar-orbiting platform, EOS Aqua. In combination with the Advanced Microwave Sounding Unit (AMSU) and the Humidity Sounder for Brazil (HSB), AIRS constitutes an innovative atmospheric sounding group of visible, infrared, and microwave sensors. AIRS/Aqua Level 3 monthly quantization product is in physical units (AIRS Only). The quantization products (QP) are distributional summaries derived from the Level-2 standard retrieval products (of swath type) to provide a more comprehensive set of statistical summaries than the traditional means and standard deviation. The QP products combine the Level 2 standard data parameters over grid cells of 5 x 5 deg spatial extent for temporal periods of a month. They preserve the multivariate distributional features of the original data and so provide a compressed data set that more accurately describes the disparate atmospheric states that is in the original Level-2 swath data set. The geophysical parameters are: Air Temperature and Water Vapor profiles (11 levels/layers), Cloud fraction (vertical distribution).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAqua%2FAIRS%2FDATA330",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAqua%2FAIRS%2FDATA330",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -163731,108 +163707,108 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRS3QPM_006.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRS3QPM_006.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level3/AIRS3QPM.006/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level3/AIRS3QPM.006/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level3/AIRS3QPM.006/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level3/AIRS3QPM.006/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRS3QPM+006",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRS3QPM+006",
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
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRS3QPM_006.gif",
+            "identifier": "C1238517283-GES_DISC",
+            "issued": "2002-09-01",
+            "keyword": [
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "atmosphere",
+                "clouds",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aqua/AIRS/DATA330",
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
+            "series-name": "AIRS3QPM",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-09-01T00:00:00Z/2024-04-08T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AIRS/Aqua L3 Monthly Quantization in Physical Units (AIRS-only) 5 degrees x 5 degrees V006 (AIRS3QPM) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5270/S5P-j7aj4gr",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Copernicus Sentinel data processed by ESA, Koninklijk Nederlands Meteorologisch Instituut (KNMI). 2019-10-09. S5P_L2__AER_LH. Version 1. Sentinel-5P TROPOMI Aerosol Layer Height 1-Orbit L2 7km x 3.5km. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5270/S5P-j7aj4gr. https://disc.gsfc.nasa.gov/datacollection/S5P_L2__AER_LH_1.html. Digital Science Data.",
-            "issued": "2017-05-05",
-            "temporal": "2018-04-30T00:41:24Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-05-05",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "air quality",
-                "aerosols",
-                "atmospheric chemistry"
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
-            "identifier": "C1442068491-GES_DISC",
-            "description": "Starting from August 6th in 2019, Sentinel-5P TROPOMI along-track high spatial resolution (~5.5km at nadir) has been implemented.\nFor data after August 6th of 2019, please check S5P_L2__AER_LH data collection.\n\nThe Copernicus Sentinel-5 Precursor (Sentinel-5P or S5P) satellite mission is one of the European Space Agency's (ESA) new mission family - Sentinels, and it is a joint initiative between the Kingdom of the Netherlands and the ESA. The sole payload on Sentinel-5P is the TROPOspheric Monitoring Instrument (TROPOMI), which is a nadir-viewing 108 degree Field-of-View push-broom grating hyperspectral spectrometer, covering the wavelength of ultraviolet-visible (UV-VIS, 270nm to 495nm), near infrared (NIR, 675nm to 775nm), and shortwave infrared (SWIR, 2305nm-2385nm). Sentinel-5P is the first of the Atmospheric Composition Sentinels and is expected to provide measurements of ozone, NO2, SO2, CH4, CO, formaldehyde, aerosols and cloud at high spatial, temporal and spectral resolutions.\n\nCopernicus Sentinel-5P TROPOMI aerosol layer height algorithm applies a forward model, which includes DISAMAR (Determining Instrument Specifications and Analyzing Methods for Atmospheric Retrieval, a Layer-Based Orders of Scattering algorithm) to calculate monochromatic reflectance, and also employs a neural network scheme for speedy processor performance. Data retrieval uses the Optimal Estimation Method (OEM) for spectral fitting with various aerosol layer pressures and aerosol optical thicknesses in the Oxygen-A band (758 -770nm). The aerosol baseline model assumes a single uniformly distributed aerosol layer with a fixed pressure thickness and a constant aerosol volume extinction coefficient and single scattering albedo. The aerosol parameterization is particularly suitable for elevated non-scattering aerosols such as volcanic ash, desert dust and biomass burning plume. The product main outputs include the mid-pressure and mid-altitude of aerosol layers, aerosol optical thickness at 760nm, error estimates, and other relevant diagnostics.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "S5P_L2__AER_LH",
             "creator": "Copernicus Sentinel data processed by ESA, Koninklijk Nederlands Meteorologisch Instituut (KNMI)",
-            "title": "Sentinel-5P TROPOMI Aerosol Layer Height 1-Orbit L2 7km x 3.5km V1 (S5P_L2__AER_LH) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/S5P_OFFL_L2__AER_LH_1.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Starting from August 6th in 2019, Sentinel-5P TROPOMI along-track high spatial resolution (~5.5km at nadir) has been implemented.\nFor data after August 6th of 2019, please check S5P_L2__AER_LH data collection.\n\nThe Copernicus Sentinel-5 Precursor (Sentinel-5P or S5P) satellite mission is one of the European Space Agency's (ESA) new mission family - Sentinels, and it is a joint initiative between the Kingdom of the Netherlands and the ESA. The sole payload on Sentinel-5P is the TROPOspheric Monitoring Instrument (TROPOMI), which is a nadir-viewing 108 degree Field-of-View push-broom grating hyperspectral spectrometer, covering the wavelength of ultraviolet-visible (UV-VIS, 270nm to 495nm), near infrared (NIR, 675nm to 775nm), and shortwave infrared (SWIR, 2305nm-2385nm). Sentinel-5P is the first of the Atmospheric Composition Sentinels and is expected to provide measurements of ozone, NO2, SO2, CH4, CO, formaldehyde, aerosols and cloud at high spatial, temporal and spectral resolutions.\n\nCopernicus Sentinel-5P TROPOMI aerosol layer height algorithm applies a forward model, which includes DISAMAR (Determining Instrument Specifications and Analyzing Methods for Atmospheric Retrieval, a Layer-Based Orders of Scattering algorithm) to calculate monochromatic reflectance, and also employs a neural network scheme for speedy processor performance. Data retrieval uses the Optimal Estimation Method (OEM) for spectral fitting with various aerosol layer pressures and aerosol optical thicknesses in the Oxygen-A band (758 -770nm). The aerosol baseline model assumes a single uniformly distributed aerosol layer with a fixed pressure thickness and a constant aerosol volume extinction coefficient and single scattering albedo. The aerosol parameterization is particularly suitable for elevated non-scattering aerosols such as volcanic ash, desert dust and biomass burning plume. The product main outputs include the mid-pressure and mid-altitude of aerosol layers, aerosol optical thickness at 760nm, error estimates, and other relevant diagnostics.",
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
@@ -163842,274 +163818,276 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/S5P_L2__AER_LH_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/S5P_L2__AER_LH_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/opendap/S5P_TROPOMI_Level2/S5P_L2__AER_LH.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/opendap/S5P_TROPOMI_Level2/S5P_L2__AER_LH.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/opendap/S5P_TROPOMI_Level2/S5P_L2__AER_LH.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/opendap/S5P_TROPOMI_Level2/S5P_L2__AER_LH.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/data/S5P_TROPOMI_Level2/S5P_L2__AER_LH.1",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/data/S5P_TROPOMI_Level2/S5P_L2__AER_LH.1",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=S5P_L2__AER_LH_1",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=S5P_L2__AER_LH_1",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/S5P_OFFL_L2__AER_LH_1.png",
+            "identifier": "C1442068491-GES_DISC",
+            "issued": "2017-05-05",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "air quality",
+                "aerosols",
+                "atmospheric chemistry"
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
+            "series-name": "S5P_L2__AER_LH",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-04-30T00:41:24Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Sentinel-5P",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sentinel-5P TROPOMI Aerosol Layer Height 1-Orbit L2 7km x 3.5km V1 (S5P_L2__AER_LH) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=P10-J-HVM-4-SUMM-NEAR-ENC-1MIN-V1.0",
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
-                "pioneer 10",
-                "jupiter"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Pioneer 10 Vector Helium Magnetometer (HVM) data from the Jupiter encounter period between 1973-12-03T21:50 and 1973-12-04T07:54.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.p10-j-hvm-4-summ-near-enc-1min-v1.0_4yq3-fckh",
+            "issued": "2021-05-21",
+            "keyword": [
+                "pioneer 10",
+                "jupiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=P10-J-HVM-4-SUMM-NEAR-ENC-1MIN-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.p10-j-hvm-4-summ-near-enc-1min-v1.0_4yq3-fckh",
-            "description": "Pioneer 10 Vector Helium Magnetometer (HVM) data from the Jupiter encounter period between 1973-12-03T21:50 and 1973-12-04T07:54.",
-            "title": "P10 JUPITER HVM B-FIELD INSIDE 7 RJ JG\n                                      COORDS 1 MIN AVG V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "P10 JUPITER HVM B-FIELD INSIDE 7 RJ JG\n                                      COORDS 1 MIN AVG V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SPUR2-XBT00",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Janet Sprintall. 2019-03-28. SPURS-2 research vessel Expendable Bathythermograph (XBT) profile data for E. Tropical Pacific R/V Revelle cruises. Version 1.0. SPURS Field Campaign XBT Products. Scripps Institution of Oceanography, University of California San Diego, La Jolla, CA, USA. Archived by National Aeronautics and Space Administration, U.S. Government, SPURS Data Management PI, Fred Bingham. https://doi.org/10.5067/SPUR2-XBT00. http://podaac.jpl.nasa.gov/SPURS. Janet Sprintall, SPURS Data Management PI, Fred Bingham, 2019-03-28, SPURS-2 research vessel Expendable Bathythermograph (XBT) profile data for E. Tropical Pacific R/V Revelle cruises, http://podaac.jpl.nasa.gov/SPURS.",
-            "issued": "2019-02-25",
-            "temporal": "2016-08-14T05:21:45Z/2017-11-15T21:51:33Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-02-25",
-            "keyword": [
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
-            "identifier": "C2491772372-POCLOUD",
-            "description": "The SPURS (Salinity Processes in the Upper Ocean Regional Study) project is NASA-funded oceanographic process study and associated field program that aim to elucidate key mechanisms responsible for near-surface salinity variations in the oceans. The project involves two field campaigns and a series of cruises in regions of the Atlantic and Pacific Oceans exhibiting salinity extremes. SPURS employs a suite of state-of-the-art in-situ sampling technologies that, combined with remotely sensed salinity fields from the Aquarius/SAC-D, SMAP and SMOS satellites, provide a detailed characterization of salinity structure over a continuum of spatio-temporal scales. The SPURS-2 campaign involved two month-long cruises by the R/V Revelle in August 2016 and October 2017 combined with complementary sampling on a more continuous basis over this period by the schooner Lady Amber. Focused around a central mooring located near 10N,125W, the objective of SPURS-2 was to study the dynamics of the rainfall-dominated surface ocean at the western edge of the eastern Pacific fresh pool subject to high seasonal variability and strong zonal flows associated with the North Equatorial Current and Countercurrent.  Expendable bathythermograph (XBT) casts were undertaken at stations during both of the SPURS-2 R/V Revelle cruises. Launched off the side of the ship, XBT probes provide vertical profile measurements of the water column at fixed locations. There were a total of 25 and 11 XBT deployments made during the first and second R/V Revelle cruises respectively.  There is one XBT data file per cruise, each containing the temperature profile data from all instrument deployments undertaken during that cruise.",
-            "release-place": "Scripps Institution of Oceanography, University of California San Diego, La Jolla, CA, USA",
-            "series-name": "SPURS-2 research vessel Expendable Bathythermograph (XBT) profile data for E. Tropical Pacific R/V Revelle cruises",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Janet Sprintall",
-            "title": "SPURS-2 research vessel Expendable Bathythermograph (XBT) profile data for E. Tropical Pacific R/V Revelle cruises",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_XBT.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The SPURS (Salinity Processes in the Upper Ocean Regional Study) project is NASA-funded oceanographic process study and associated field program that aim to elucidate key mechanisms responsible for near-surface salinity variations in the oceans. The project involves two field campaigns and a series of cruises in regions of the Atlantic and Pacific Oceans exhibiting salinity extremes. SPURS employs a suite of state-of-the-art in-situ sampling technologies that, combined with remotely sensed salinity fields from the Aquarius/SAC-D, SMAP and SMOS satellites, provide a detailed characterization of salinity structure over a continuum of spatio-temporal scales. The SPURS-2 campaign involved two month-long cruises by the R/V Revelle in August 2016 and October 2017 combined with complementary sampling on a more continuous basis over this period by the schooner Lady Amber. Focused around a central mooring located near 10N,125W, the objective of SPURS-2 was to study the dynamics of the rainfall-dominated surface ocean at the western edge of the eastern Pacific fresh pool subject to high seasonal variability and strong zonal flows associated with the North Equatorial Current and Countercurrent.  Expendable bathythermograph (XBT) casts were undertaken at stations during both of the SPURS-2 R/V Revelle cruises. Launched off the side of the ship, XBT probes provide vertical profile measurements of the water column at fixed locations. There were a total of 25 and 11 XBT deployments made during the first and second R/V Revelle cruises respectively.  There is one XBT data file per cruise, each containing the temperature profile data from all instrument deployments undertaken during that cruise.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSPUR2-XBT00",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSPUR2-XBT00",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_XBT.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_XBT.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772372-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772372-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772372-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772372-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_XBT.jpg",
+            "identifier": "C2491772372-POCLOUD",
+            "issued": "2019-02-25",
+            "keyword": [
+                "ocean temperature",
+                "oceans",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SPUR2-XBT00",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-02-25",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "Scripps Institution of Oceanography, University of California San Diego, La Jolla, CA, USA",
+            "series-name": "SPURS-2 research vessel Expendable Bathythermograph (XBT) profile data for E. Tropical Pacific R/V Revelle cruises",
             "spatial": "-157.88 5.06 -118.32 21.26",
+            "temporal": "2016-08-14T05:21:45Z/2017-11-15T21:51:33Z",
             "theme": [
                 "SPURS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SPURS-2 research vessel Expendable Bathythermograph (XBT) profile data for E. Tropical Pacific R/V Revelle cruises"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA/3518",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Read, W., Livesey, N., and Fuller, R.. 2021-04-29. ML3DBRHI. Version 005. MLS/Aura Level 3 Daily Binned Relative Humidity With Respect To Ice (RHI) on Assorted Grids V005. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA/3518. https://disc.gsfc.nasa.gov/datacollection/ML3DBRHI_005.html. Digital Science Data.",
-            "issued": "2021-04-29",
-            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-04-29",
-            "keyword": [
-                "atmosphere",
-                "atmospheric water vapor",
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
-            "identifier": "C2042566207-GES_DISC",
-            "description": "ML3DBRHI is the EOS Aura Microwave Limb Sounder (MLS) daily binned on various vertical grids product for relative humidity with respect to ice (RHI) derived from radiances measured by the 118 and 190 GHz radiometers. The data version is 5.1. Spatial coverage is near-global (-82 to +82 degrees latitude) at a spatial resolution of 4 degrees latitude by 5 degrees longitude. The recommended useful vertical range is from 316 to 0.0215 hPa, and the vertical resolution is between 3 and 6 km. Users of the ML3DBRHI data product should read chapter 4 and section 3.20 of the EOS MLS Level 2 Version 5 Quality Document for more information.\n\nThe data files are archived in the netCDF4 format, which is also compatible with HDF5 readers and tools. Each file contains six group objects: lat-lon map vs pressure, lat vs pressure zonal mean, lat-lon map vs theta, lat vs theta zonal mean, equivalent lat vs theta zonal mean, and vortex average vs theta. Each group has a set of data (average, min, max, std dev, rms) and geolocation fields, grid attributes, and metadata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML3DBRHI",
             "creator": "Read, W., Livesey, N., and Fuller, R.",
-            "title": "MLS/Aura Level 3 Daily Binned Relative Humidity With Respect To Ice (RHI) on Assorted Grids V005 (ML3DBRHI) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML3DBRHI_005.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "ML3DBRHI is the EOS Aura Microwave Limb Sounder (MLS) daily binned on various vertical grids product for relative humidity with respect to ice (RHI) derived from radiances measured by the 118 and 190 GHz radiometers. The data version is 5.1. Spatial coverage is near-global (-82 to +82 degrees latitude) at a spatial resolution of 4 degrees latitude by 5 degrees longitude. The recommended useful vertical range is from 316 to 0.0215 hPa, and the vertical resolution is between 3 and 6 km. Users of the ML3DBRHI data product should read chapter 4 and section 3.20 of the EOS MLS Level 2 Version 5 Quality Document for more information.\n\nThe data files are archived in the netCDF4 format, which is also compatible with HDF5 readers and tools. Each file contains six group objects: lat-lon map vs pressure, lat vs pressure zonal mean, lat-lon map vs theta, lat vs theta zonal mean, equivalent lat vs theta zonal mean, and vortex average vs theta. Each group has a set of data (average, min, max, std dev, rms) and geolocation fields, grid attributes, and metadata.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA%2F3518",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA%2F3518",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -164119,152 +164097,150 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML3DBRHI_005.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML3DBRHI_005.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level3/ML3DBRHI.005/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level3/ML3DBRHI.005/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level3/ML3DBRHI.005/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level3/ML3DBRHI.005/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML3DBRHI_005",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML3DBRHI_005",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML3DBRHI_005.png",
+            "identifier": "C2042566207-GES_DISC",
+            "issued": "2021-04-29",
+            "keyword": [
+                "atmosphere",
+                "atmospheric water vapor",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA/3518",
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
+            "series-name": "ML3DBRHI",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MLS/Aura Level 3 Daily Binned Relative Humidity With Respect To Ice (RHI) on Assorted Grids V005 (ML3DBRHI) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-SS-RPCLAP-2-CR4B-EDITED2-V1.0",
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
+            "description": "This data set contains EDITED\ndata from Rosetta RPC-LAP, acquired during the CRUISE 4-2 mission phase\nwhere the primary target was the SOLAR WIND. It contains uncalibrated\nraw data, i.e. the digital output of the instrument.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-ss-rpclap-2-cr4b-edited2-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "solar wind"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-SS-RPCLAP-2-CR4B-EDITED2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-ss-rpclap-2-cr4b-edited2-v1.0",
-            "description": "This data set contains EDITED\ndata from Rosetta RPC-LAP, acquired during the CRUISE 4-2 mission phase\nwhere the primary target was the SOLAR WIND. It contains uncalibrated\nraw data, i.e. the digital output of the instrument.",
-            "title": "ROSETTA-ORBITER SW RPCLAP 2\nCR4B EDITED2 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER SW RPCLAP 2\nCR4B EDITED2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2022-01-15",
-            "temporal": "2022-01-15T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "international",
-                "location",
-                "coordinates",
-                "coords",
-                "trajectory",
-                "ephemeris",
-                "topo",
-                "station",
-                "iss",
-                "space"
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
-            "identifier": "nasa-iss-data_2022-01-15_4ywn-y3sp",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2022-01-15",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -164387,26 +164363,61 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2022-01-15_4ywn-y3sp",
+            "issued": "2022-01-15",
+            "keyword": [
+                "international",
+                "location",
+                "coordinates",
+                "coords",
+                "trajectory",
+                "ephemeris",
+                "topo",
+                "station",
+                "iss",
+                "space"
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
+            "temporal": "2022-01-15T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2022-01-15"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://fermi.gsfc.nasa.gov/ssc/data/access/lat/1FHL/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Phil Newman",
+                "hasEmail": "mailto:panewman@lheapop.gsfc.nasa.gov"
+            },
+            "description": "The Fermi Gamma-ray Space Telescope (Fermi) Large Area Telescope (LAT) is a successor to EGRET, with greatly improved sensitivity, resolution, and energy range. This web page presents the first full catalog of LAT sources, based on the first eleven months of survey data. For a full explanation about the catalog and its construction see the LAT 1-year Catalog Paper.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://fermi.gsfc.nasa.gov/ssc/data/access/lat/1yr_catalog/1FGL_column_descriptions_v2.pdf",
+                    "mediaType": "application/pdf"
+                }
+            ],
+            "identifier": "NASA-0000221__3",
             "issued": "2018-06-25",
-            "temporal": "2008-08-01/2009-07-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "gamma-ray",
                 "acd",
@@ -164424,429 +164435,397 @@
                 "gssc",
                 "high-energy"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Phil Newman",
-                "hasEmail": "mailto:panewman@lheapop.gsfc.nasa.gov"
-            },
+            "landingPage": "http://fermi.gsfc.nasa.gov/ssc/data/access/lat/1FHL/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:014"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000221__3",
-            "description": "The Fermi Gamma-ray Space Telescope (Fermi) Large Area Telescope (LAT) is a successor to EGRET, with greatly improved sensitivity, resolution, and energy range. This web page presents the first full catalog of LAT sources, based on the first eleven months of survey data. For a full explanation about the catalog and its construction see the LAT 1-year Catalog Paper.",
-            "title": "LAT 1-year Point Source Catalog",
-            "programCode": [
-                "026:014"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://fermi.gsfc.nasa.gov/ssc/data/access/lat/1yr_catalog/1FGL_column_descriptions_v2.pdf",
-                    "mediaType": "application/pdf"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
+            "temporal": "2008-08-01/2009-07-01",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "LAT 1-year Point Source Catalog"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/TRICHOTOTO/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/TRICHOTOTO/DATA001.",
-            "issued": "1999-11-01",
-            "temporal": "1999-11-01T02:29:43Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "salinity/density",
-                "oceans",
-                "earth science",
-                "ocean chemistry",
-                "ocean temperature",
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
-            "identifier": "C1633360687-OB_DAAC",
             "description": "Measurements from the North Australian Coast in the Timur and Arafura Seas in 1999.",
-            "title": "Trichodesmium Toto (TRICHOTOTO) cruise",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FTRICHOTOTO%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FTRICHOTOTO%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/trichototo/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/trichototo/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360687-OB_DAAC",
+            "issued": "1999-11-01",
+            "keyword": [
+                "salinity/density",
+                "oceans",
+                "earth science",
+                "ocean chemistry",
+                "ocean temperature",
+                "ocean optics"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/TRICHOTOTO/DATA001",
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
+            "temporal": "1999-11-01T02:29:43Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Trichodesmium Toto (TRICHOTOTO) cruise"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1274625680-GES_DISC.html",
             "citation": "Goddard Laboratory for Atmospheres at NASA GSFC. 1995-01-01. TOVSADNG. Version 01. TOVS GLA DAILY GRIDS from NOAA-10 V01. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/TOVSADNG_01.html. Digital Science Data.",
-            "issued": "1986-11-25",
-            "temporal": "1986-11-25T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "1991-09-01",
-            "keyword": [
-                "oceans",
-                "atmospheric chemistry",
-                "precipitation",
-                "ocean temperature",
-                "atmospheric pressure",
-                "earth science",
-                "clouds",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "atmospheric radiation",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JOEL SUSSKIND",
                 "hasEmail": "mailto:joel.susskind-1@nasa.gov"
             },
+            "creator": "Goddard Laboratory for Atmospheres at NASA GSFC",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1274625680-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "This dataset (TOVSADNG) contains the TIROS Operational Vertical Sounder (TOVS) level 3 geophysical parameters derived using data from NOAA-10 and the physical retrieval method of Susskind et al. (1984) and processed by the Satellite Data Utilization Office of the Goddard Laboratory for Atmospheres at NASA/GSFC. This method, which is hydrodynamic model- and a priori data-dependent, is designated as the so-called Path A scheme by the TOVS Pathfinder Science Working Group. The 20 channel High resolution Infrared Radiation Sounder 2 (HIRS2) and the 4 channel Microwave Sounding Unit (MSU) aboard the NOAA-xx series of Polar Orbiting Satellites are used to produce global fields of the 3-dimensional temperature-moisture structure of the atmosphere. In addition to profiles of temperature and moisture, the HIRS2/MSU data are used to derive important quantities such as land and sea surface temperature, outgoing longwave radiation, cloud fraction, cloudtop height, total ozone overburden and precipitation estimates.\n\nThe Path A system steps through an interactive forecast-retrieval-analysis cycle. In each 6 hour synoptic period, a 2nd order General Circulation Model (Takacs et al., 1994) is used to generate the 6 hour forecast fields of temperature and humidity. These global fields are used as the first guess for all soundings occuring within a 6 hour time window centered upon the forecast time. These retrievals are then assimilated with all available insitu measurements (such as radiosonde and ship reports) in the 6 hour interval using an Optimal Interpolation (OI) analysis scheme developed by the Data Assimilation Office of the Goddard Laboratory for Atmospheres. This analysis is then used to specify the initial conditions for the next 6 hour forecast, thus completing the cycle.\n\nThe retrieval algorithm itself is a physical method based on the iterative relaxation technique originally proposed by Chahine (1968). The basic approach consists of modifying the temperature profile from the previous iteration by an amount proportional to the difference between the observed brightness temperatures and the brightness temperatures computed from the trial parameters using the full radiative transfer equation applied at the observed satellite zenith angle. For the case of the temperature profile, the updated layer mean temperatures are given as a linear combination of multichannel brightness temperature differences with the coefficients given by the channel weighting functions. Constraints are imposed upon the solution in order to ensure stability and convergence of the iterative process. For more details see Susskind et al (1984).\n\nThere are level 3 data product files for five TOVS satellites, each of which is in the HDF format and each representative of a different averaging time period. All files contain the same number of geophysical parameter arrays stored as HDF Scientific Data Sets (SDSs). The time periods include daily, 5 day (pentad) and monthly, with the AM and PM portions of the orbits treated separately.  All data are mapped to a 1 degree longitude by 1 degree latitude global grid.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TOVSADNG",
-            "creator": "Goddard Laboratory for Atmospheres at NASA GSFC",
-            "title": "TOVS GLA DAILY GRIDS from NOAA-10 V01 (TOVSADNG) at GES DISC",
-            "graphic-preview-description": "TOVSADNG image",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOVSADNG_01.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOVSADNG_01.png",
-                    "description": "TOVSADNG image",
                     "@type": "dcat:Distribution",
+                    "description": "TOVSADNG image",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOVSADNG_01.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TOVSADNG_01.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TOVSADNG_01.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TOVS/TOVS_Starter_Kit.pdf",
-                    "description": "This document is TOVS legacy documentation.  Some information may be obsolete.",
                     "@type": "dcat:Distribution",
+                    "description": "This document is TOVS legacy documentation.  Some information may be obsolete.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TOVS/TOVS_Starter_Kit.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc1.gesdisc.eosdis.nasa.gov/data/tovs/TOVSADNG",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://disc1.gesdisc.eosdis.nasa.gov/data/tovs/TOVSADNG",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TOVSADNG+001",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TOVSADNG+001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc1.gesdisc.eosdis.nasa.gov/data/tovs/TOVSADND/doc/README.TOVSPathA.txt",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://disc1.gesdisc.eosdis.nasa.gov/data/tovs/TOVSADND/doc/README.TOVSPathA.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TOVS/TOVS_PATHFINDER_PATH_A_DATASET_GUIDE.pdf",
-                    "description": "This document is a TOVS legacy data guide.  Some\ninformation may be obsolete.",
                     "@type": "dcat:Distribution",
+                    "description": "This document is a TOVS legacy data guide.  Some\ninformation may be obsolete.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TOVS/TOVS_PATHFINDER_PATH_A_DATASET_GUIDE.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "TOVSADNG image",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOVSADNG_01.png",
+            "identifier": "C1274625680-GES_DISC",
+            "issued": "1986-11-25",
+            "keyword": [
+                "oceans",
+                "atmospheric chemistry",
+                "precipitation",
+                "ocean temperature",
+                "atmospheric pressure",
+                "earth science",
+                "clouds",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "atmospheric radiation",
+                "atmosphere"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1274625680-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1991-09-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "TOVSADNG",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1986-11-25T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "TOVS Pathfinder",
                 "CWIC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TOVS GLA DAILY GRIDS from NOAA-10 V01 (TOVSADNG) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=P10-J-HVM%2FPA-4-SUMM-MERGED-1HR-V1.0",
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
-                "jupiter",
-                "pioneer 10"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This directory contains the Pioneer 10 plasma (PA) and magnetic field (HVM)\ndata from the Jupiter close encounter period between 1973-11-26T00:00:00\nand 1974-01-01T00:00:00. The data include 1 hour averages.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.p10-j-hvm-pa-4-summ-merged-1hr-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "jupiter",
+                "pioneer 10"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=P10-J-HVM%2FPA-4-SUMM-MERGED-1HR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.p10-j-hvm-pa-4-summ-merged-1hr-v1.0",
-            "description": "This directory contains the Pioneer 10 plasma (PA) and magnetic field (HVM)\ndata from the Jupiter close encounter period between 1973-11-26T00:00:00\nand 1974-01-01T00:00:00. The data include 1 hour averages.",
-            "title": "P10 JUPITER HVM PA SUMM MERGED 1 HOUR",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "P10 JUPITER HVM PA SUMM MERGED 1 HOUR"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567894-USGS_LTA.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "U.S. Geological Survey Earth Resources Observation and Science (EROS) Center. 2014-01-01. U.S. Geological Survey. USGS Global Forest Observations Initiative (GFOI) REPUBLIC OF THE CONGO. Archived by National Aeronautics and Space Administration, U.S. Government, DOI/USGS/EROS.",
-            "issued": "2013-02-01",
-            "temporal": "2013-02-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-03-25",
-            "keyword": [
-                "agriculture",
-                "forest science",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "LTA REPRESENTATIVE USGS EROS CENTER",
                 "hasEmail": "mailto:lta@usgs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOI/USGS/EROS"
-            },
-            "identifier": "C1220567894-USGS_LTA",
-            "description": "The Global Forest Observations Initiative (GFOI) is an initiative of the inter-governmental Group on Earth Observations (GEO) that aims to:\n\nfoster the sustained availability of observations for national forest monitoring systems; support governments that are establishing national systems by providing a platform for coordinating observations, providing assistance and guidance on utilizing observations, developing accepted methods and protocols, and promoting ongoing research and development; and work with national governments that report into international forest assessments (such as the global Forest Resources Assessment (FRA) of the Food and Agriculture Organization, FAO) and the national greenhouse gas inventories reported to the UN Framework Convention on Climate Change (UNFCCC) using methods of the Intergovernmental Panel on Climate Change (IPCC).",
-            "series-name": "U.S. Geological Survey",
             "creator": "U.S. Geological Survey Earth Resources Observation and Science (EROS) Center",
-            "title": "USGS Global Forest Observations Initiative (GFOI) REPUBLIC OF THE CONGO",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Global Forest Observations Initiative (GFOI) is an initiative of the inter-governmental Group on Earth Observations (GEO) that aims to:\n\nfoster the sustained availability of observations for national forest monitoring systems; support governments that are establishing national systems by providing a platform for coordinating observations, providing assistance and guidance on utilizing observations, developing accepted methods and protocols, and promoting ongoing research and development; and work with national governments that report into international forest assessments (such as the global Forest Resources Assessment (FRA) of the Food and Agriculture Organization, FAO) and the national greenhouse gas inventories reported to the UN Framework Convention on Climate Change (UNFCCC) using methods of the Intergovernmental Panel on Climate Change (IPCC).",
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
                 }
             ],
+            "identifier": "C1220567894-USGS_LTA",
+            "issued": "2013-02-01",
+            "keyword": [
+                "agriculture",
+                "forest science",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567894-USGS_LTA.html",
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
+            "series-name": "U.S. Geological Survey",
             "spatial": "13.0 -1.0 15.5 0.5",
+            "temporal": "2013-02-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "USGS Global Forest Observations Initiative (GFOI) REPUBLIC OF THE CONGO"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3055-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2011-08-02T01:35:44.000 to 2011-08-02T02:00:26.949.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3055-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars express"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3055-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3055-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2011-08-02T01:35:44.000 to 2011-08-02T02:00:26.949.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3055 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3055 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=M10-H-POS-6-M1-FLYBY-TRAJ-V1.0",
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
-                "mariner 10"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Mariner 10 trajectory (POS)  M1 FLYBY  data at Mercury.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.m10-h-pos-6-m1-flyby-traj-v1.0_4z7v-zywi",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mercury",
+                "mariner 10"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=M10-H-POS-6-M1-FLYBY-TRAJ-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.m10-h-pos-6-m1-flyby-traj-v1.0_4z7v-zywi",
-            "description": "Mariner 10 trajectory (POS)  M1 FLYBY  data at Mercury.",
-            "title": "MARINER 10 MERC POS M1 FLYBY TRAJ V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARINER 10 MERC POS M1 FLYBY TRAJ V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-ESC2-67PCHURYUMOV-M17-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera during the COMET ESCORT 2 phase of the Rosetta mission at the comet 67P, covering the period from 2015-06-02T23:25:00.000 to 2015-06-30T23:24:59.000. This version V2.0 supersedes previous deliveries of the same dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-esc2-67pchuryumov-m17-v2.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "international rosetta mission",
                 "16 cyg b"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-ESC2-67PCHURYUMOV-M17-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-esc2-67pchuryumov-m17-v2.0",
-            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera during the COMET ESCORT 2 phase of the Rosetta mission at the comet 67P, covering the period from 2015-06-02T23:25:00.000 to 2015-06-30T23:24:59.000. This version V2.0 supersedes previous deliveries of the same dataset.",
-            "title": "ROSETTA-ORBITER COMET ESCORT 2 OSIWAC 3 RDR MTP017 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMET ESCORT 2 OSIWAC 3 RDR MTP017 V2.0"
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
-                "appel",
-                "ask the academy",
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
-            "identifier": "NASA-862__26",
             "description": "Academy of Program/Project & Engineering Leadership's Ask the Academy magazine past issues.",
-            "title": "Academy of Program/Project & Engineering Leadership ASK the Academy Past Issues",
-            "programCode": [
-                "026:045"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -164854,171 +164833,170 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
+            "identifier": "NASA-862__26",
+            "issued": "2018-06-25",
+            "keyword": [
+                "sharing",
+                "appel",
+                "ask the academy",
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
-            "landingPage": "https://doi.org/10.5067/PRESW-CBJ10",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Menemenlis, D., Hill, C., Henze, C. E., Wang, J., & Fenty, I.. 2021-02-10. Cape Basin Pre-SWOT Level-4 Hourly MITgcm LLC4320 Native Grid 2km Oceanographic Dataset Version 1.0. Version 1.0. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/PRESW-CBJ10. Menemenlis, D., Hill, C., Henze, C. E., Wang, J., & Fenty, I. 2021. Cape Basin Pre-SWOT Level-4 Hourly MITgcm LLC4320 Native Grid 2km Oceanographic Dataset Version 1.0. PO.DAAC, CA, USA. Dataset accessed[YYYY-MM-DD] at https://doi.org/10.5067/PRESW-CBJ10.",
-            "issued": "2021-01-20",
-            "temporal": "2011-09-13T00:00:00Z/2012-11-15T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2012-11-14",
-            "references": [
-                "https://doi.org/10.1029/2019gl083074",
-                "https://doi.org/10.1029/2018JC014438",
-                "https://doi.org/10.17125/gov2018.ch13",
-                "https://doi.org/10.1038/s41467-018-02983-w",
-                "https://doi.org/10.1175/jtech-d-17-0076.1",
-                "https://doi.org/810.1175/JPO-D-15-0087.1"
-            ],
-            "keyword": [
-                "ocean heat budget",
-                "salinity/density",
-                "earth science",
-                "ocean circulation",
-                "oceans",
-                "ocean temperature"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dimitris Menemenlis",
                 "hasEmail": "mailto:menemenlis@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "identifier": "C2006849794-POCLOUD",
-            "description": "This dataset provides a regional multivariate oceanographic state estimate from a global ocean numerical simulation with a focus on the Cape Basin region. The global ocean simulation is based on the MIT general circulation model (MITgcm) with Lat-Lon-Cap grid (LLC) layout and 1/48-degree (2km at equator) nominal horizontal resolution. This simulation is often referred to as LLC4320 in the community and existing publications. The simulation has 90 vertical levels, with about 1-m vertical resolution at the surface and 30 m down to 500 m, for optimized resolution of the upper-ocean processes. The model has zero parameterized horizontal diffusivity. In the vertical direction, the K-Profile Parameterization (KPP) is used for boundary layer turbulent mixing. It is spun up progressively from the lower resolution MITgcm simulation from the Estimating the Circulation & Climate of the Ocean (ECCO), and forced by the 6-hourly ERA-Interim atmosphere reanalysis ( https://www.ecmwf.int/en/forecasts/datasets/reanalysis-datasets/era-interim ). A synthetic surface pressure field consisting of the 16 most dominant tidal constituents is used to dynamically mimic the tidal forcing. The dataset provides hourly oceanographic variables at native grid. Three-dimensional variables include temperature, salinity, and velocity. Two-dimensional variables include sea level anomaly, ocean mixed layer thickness, bottom pressure anomaly, net freshwater flux, net heat flux, shortwave radiative flux, net salt flux, and ocean surface stress.",
-            "release-place": "PO.DAAC",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Menemenlis, D., Hill, C., Henze, C. E., Wang, J., & Fenty, I.",
-            "title": "Cape Basin Pre-SWOT Level-4 Hourly MITgcm LLC4320 Native Grid 2km Oceanographic Dataset Version 1.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MITgcm_LLC4320_Pre-SWOT_JPL_L4_CapeBasin_v1.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset provides a regional multivariate oceanographic state estimate from a global ocean numerical simulation with a focus on the Cape Basin region. The global ocean simulation is based on the MIT general circulation model (MITgcm) with Lat-Lon-Cap grid (LLC) layout and 1/48-degree (2km at equator) nominal horizontal resolution. This simulation is often referred to as LLC4320 in the community and existing publications. The simulation has 90 vertical levels, with about 1-m vertical resolution at the surface and 30 m down to 500 m, for optimized resolution of the upper-ocean processes. The model has zero parameterized horizontal diffusivity. In the vertical direction, the K-Profile Parameterization (KPP) is used for boundary layer turbulent mixing. It is spun up progressively from the lower resolution MITgcm simulation from the Estimating the Circulation & Climate of the Ocean (ECCO), and forced by the 6-hourly ERA-Interim atmosphere reanalysis ( https://www.ecmwf.int/en/forecasts/datasets/reanalysis-datasets/era-interim ). A synthetic surface pressure field consisting of the 16 most dominant tidal constituents is used to dynamically mimic the tidal forcing. The dataset provides hourly oceanographic variables at native grid. Three-dimensional variables include temperature, salinity, and velocity. Two-dimensional variables include sea level anomaly, ocean mixed layer thickness, bottom pressure anomaly, net freshwater flux, net heat flux, shortwave radiative flux, net salt flux, and ocean surface stress.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FPRESW-CBJ10",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FPRESW-CBJ10",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/SWOT",
-                    "description": "Mission and Instrument Overview",
                     "@type": "dcat:Distribution",
+                    "description": "Mission and Instrument Overview",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/SWOT",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/MEaSUREs-SSH",
-                    "description": "Mission and Instrument Overview",
                     "@type": "dcat:Distribution",
+                    "description": "Mission and Instrument Overview",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/MEaSUREs-SSH",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/PRESW-CBJ10",
-                    "description": "Access the dataset landing page for the collection",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page for the collection",
+                    "downloadURL": "https://doi.org/10.5067/PRESW-CBJ10",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/common/sw/generic_nc_readers",
-                    "description": "Generic netCDF read software provided in IDL, MATLAB, Python, and R",
                     "@type": "dcat:Distribution",
+                    "description": "Generic netCDF read software provided in IDL, MATLAB, Python, and R",
+                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/common/sw/generic_nc_readers",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MITgcm_LLC4320_Pre-SWOT_JPL_L4_CapeBasin_v1.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MITgcm_LLC4320_Pre-SWOT_JPL_L4_CapeBasin_v1.0.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2006849794-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2006849794-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2006849794-POCLOUD",
-                    "description": "Browse and download granules over HTTPS using the virtual directories",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2006849794-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/misc/web/misc/SWOT/Pre-SWOT_LLC4320/preswot_llc4320_user_guide.pdf",
-                    "description": "PRE-SWOT NUMERICAL SIMULATION VERSION 1 USER GUIDE",
                     "@type": "dcat:Distribution",
+                    "description": "PRE-SWOT NUMERICAL SIMULATION VERSION 1 USER GUIDE",
+                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/misc/web/misc/SWOT/Pre-SWOT_LLC4320/preswot_llc4320_user_guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/misc/web/misc/SWOT/Pre-SWOT_LLC4320/README",
-                    "description": "Readme File",
                     "@type": "dcat:Distribution",
+                    "description": "Readme File",
+                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/misc/web/misc/SWOT/Pre-SWOT_LLC4320/README",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MITgcm_LLC4320_Pre-SWOT_JPL_L4_CapeBasin_v1.0.jpg",
+            "identifier": "C2006849794-POCLOUD",
+            "issued": "2021-01-20",
+            "keyword": [
+                "ocean heat budget",
+                "salinity/density",
+                "earth science",
+                "ocean circulation",
+                "oceans",
+                "ocean temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/PRESW-CBJ10",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2012-11-14",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.1029/2019gl083074",
+                "https://doi.org/10.1029/2018JC014438",
+                "https://doi.org/10.17125/gov2018.ch13",
+                "https://doi.org/10.1038/s41467-018-02983-w",
+                "https://doi.org/10.1175/jtech-d-17-0076.1",
+                "https://doi.org/810.1175/JPO-D-15-0087.1"
+            ],
+            "release-place": "PO.DAAC",
             "spatial": "11.82292 -44.99279 15.80208 -41.01421",
+            "temporal": "2011-09-13T00:00:00Z/2012-11-15T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Cape Basin Pre-SWOT Level-4 Hourly MITgcm LLC4320 Native Grid 2km Oceanographic Dataset Version 1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://nasa3d.arc.nasa.gov/detail/crew-lock-bag",
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
-                "3d model",
-                "shuttle",
-                "crew lock bag",
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
-            "identifier": "NASA-331",
             "description": "Crew lock bag. Polygons: 405 Vertices: 514",
-            "title": "NASA 3D Models: Crew Lock Bag",
-            "programCode": [
-                "026:045",
-                "026:046"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -165026,21 +165004,54 @@
                     "mediaType": "image/x-3ds"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-331",
+            "issued": "2018-06-25",
+            "keyword": [
+                "3d model",
+                "shuttle",
+                "crew lock bag",
+                "astronaut"
+            ],
+            "landingPage": "http://nasa3d.arc.nasa.gov/detail/crew-lock-bag",
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
+            "title": "NASA 3D Models: Crew Lock Bag"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/4zf8-gxsi",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Robert O. Shelton",
+                "hasEmail": "mailto:Robert.o.Shelton@nasa.gov"
+            },
+            "description": "Earth+ makes NASA satellite photos and data accessible to blind students.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://prime.jsc.nasa.gov/earthplus/Katrina/KatrinaCoordinates.doc",
+                    "mediaType": "application/msword"
+                }
+            ],
+            "identifier": "NASA-0000033__6",
             "issued": "2018-06-25",
-            "temporal": "2004-01-01/2005-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "education outreach",
                 "power",
@@ -165050,294 +165061,292 @@
                 "hdf5",
                 "climatology"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Robert O. Shelton",
-                "hasEmail": "mailto:Robert.o.Shelton@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/4zf8-gxsi",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000033__6",
-            "description": "Earth+ makes NASA satellite photos and data accessible to blind students.",
-            "title": "Earth+",
-            "programCode": [
-                "026:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://prime.jsc.nasa.gov/earthplus/Katrina/KatrinaCoordinates.doc",
-                    "mediaType": "application/msword"
-                }
-            ],
             "spatial": "Earth",
-            "accrualPeriodicity": "irregular"
+            "temporal": "2004-01-01/2005-01-01",
+            "title": "Earth+"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ACES/CLOCKS/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Blakeslee, Richard J..2004. ACES TIMING DATA [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/ACES/CLOCKS/DATA101",
-            "issued": "2004-09-15",
-            "temporal": "2002-07-10T00:00:00Z/2002-08-30T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "earth science",
-                "spectral/engineering",
-                "platform characteristics"
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
-            "identifier": "C1977855412-GHRC_DAAC",
             "description": "The ALTUS Cloud Electrification Study (ACES) was based at the Naval Air Facility Key West in Florida. During August or 2002, ACES researchers overflights of thunderstorms over the southwestern corner of Florida. For the first time in NASA research, an uninhabited aerial vehicle (UAV) named ALTUS was used to collect cloud electrification data. Carrying field mills, optical sensors, electric field sensors and other instruments, ALTUS allowed scientists to collect cloud electrification data for the first time from above the storm, from its birth through dissipation. This experiment allowed scientists to achieve the dual goals of gathering weather data safely and testing new aircraft technology. This dataset consists of timing data used for the experiment. When used it provides: syncclock_time = time found at the syncclock (VSI-SYnCCLOCK-32) in seconds from first file name, syncclock_m_time = time found at the syncclock (VSI-SYnCCLOCK-32) in Matlab dateform format, system_time = system time in seconds from first file name, system_m_time = system time in dateform format, gps_time = time found at the GPS unit in seconds from first file name, gps_m_time = time found at GPS unit in dateform, cmos_time = time found at the computer CMOS in seconds from first file name, cmos_m_time = time found at the computer CMOS in dateform.",
-            "title": "ACES TIMING DATA V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FACES%2FCLOCKS%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FACES%2FCLOCKS%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=aces1time",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=aces1time",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/aces/aces1_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/aces/aces1_dataset.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/x-tar",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/aces/ACES_TOOLKIT.tar",
-                    "description": "ACES TOOLKIT",
                     "@type": "dcat:Distribution",
+                    "description": "ACES TOOLKIT",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/aces/ACES_TOOLKIT.tar",
+                    "mediaType": "application/x-tar",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/ACES",
-                    "description": "The home page for the project or program which sponsored the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The home page for the project or program which sponsored the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/ACES",
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
+            "identifier": "C1977855412-GHRC_DAAC",
+            "issued": "2004-09-15",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "platform characteristics"
+            ],
+            "landingPage": "https://doi.org/10.5067/ACES/CLOCKS/DATA101",
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
             "spatial": "-85.0 23.0 -81.0 26.0",
+            "temporal": "2002-07-10T00:00:00Z/2002-08-30T23:59:59Z",
             "theme": [
                 "ACES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ACES TIMING DATA V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LP-L-ENG-6-SUNPULSE-V1.0",
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
+            "description": "The sun pulse data set is a record of times that the Lunar Prospector sun sensor detects the Sun. These sun pulse times are derived from ground processing of the sun sensor data, earth-moon limb sensor data, and the spacecraft ephemeris. This data set is part of the Lunar Prospector Level 0 data archive. The sun pulse times are used in determining the spacecraft spin rate and orientation as a function of time. Because the Lunar Prospector spacecraft is sometimes in eclipse with the Sun, the sun pulse data set is generated on the ground to include both actual sun pulse times based on the sun sensor measurements and estimated sun pulse times based on the history of spin rate change during all prior eclipses.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lp-l-eng-6-sunpulse-v1.0_4zh3-y4uq",
+            "issued": "2018-06-26",
+            "keyword": [
+                "lunar prospector",
+                "moon"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LP-L-ENG-6-SUNPULSE-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lp-l-eng-6-sunpulse-v1.0_4zh3-y4uq",
-            "description": "The sun pulse data set is a record of times that the Lunar Prospector sun sensor detects the Sun. These sun pulse times are derived from ground processing of the sun sensor data, earth-moon limb sensor data, and the spacecraft ephemeris. This data set is part of the Lunar Prospector Level 0 data archive. The sun pulse times are used in determining the spacecraft spin rate and orientation as a function of time. Because the Lunar Prospector spacecraft is sometimes in eclipse with the Sun, the sun pulse data set is generated on the ground to include both actual sun pulse times based on the sun sensor measurements and estimated sun pulse times based on the history of spin rate change during all prior eclipses.",
-            "title": "LP MOON SUN PULSE DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "LP MOON SUN PULSE DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-CAL-COSAC-3-PDCS-V1.0",
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
+            "description": "This archive contains calibrated data (CODMAC level 3) from the COSAC instrument onboard ROSETTA Lander, acquired during the PDCS phase. It also contains documentation which describes the COSAC experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-cal-cosac-3-pdcs-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "calibration"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-CAL-COSAC-3-PDCS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-cal-cosac-3-pdcs-v1.0",
-            "description": "This archive contains calibrated data (CODMAC level 3) from the COSAC instrument onboard ROSETTA Lander, acquired during the PDCS phase. It also contains documentation which describes the COSAC experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER CAL COSAC 3 PDCS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-LANDER CAL COSAC 3 PDCS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VEGA2-C-SP2-2-RDR-HALLEY-V1.0",
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
+            "description": "The SP-2 experiment on Vega spacecraft was intended for studying the spatial and mass distributions of dust particles in the cometary coma over the mass range 1.e-16 to 1.e-6 g. Covering such a broad mass range was made possible by using sensors of two types, namely, impact plasma and acoustic.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vega2-c-sp2-2-rdr-halley-v1.0_4zkx-uurn",
+            "issued": "2018-06-26",
+            "keyword": [
+                "halley",
+                "vega 2"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VEGA2-C-SP2-2-RDR-HALLEY-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vega2-c-sp2-2-rdr-halley-v1.0_4zkx-uurn",
-            "description": "The SP-2 experiment on Vega spacecraft was intended for studying the spatial and mass distributions of dust particles in the cometary coma over the mass range 1.e-16 to 1.e-6 g. Covering such a broad mass range was made possible by using sensors of two types, namely, impact plasma and acoustic.",
-            "title": "VEGA2 DUST PARTICLE IMPACT DETECTOR DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VEGA2 DUST PARTICLE IMPACT DETECTOR DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/CRP/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/CRP/DATA001.",
-            "issued": "2010-03-27",
-            "temporal": "2010-03-27T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean chemistry",
-                "ocean temperature",
-                "oceans",
-                "ocean optics",
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
-            "identifier": "C1633360197-OB_DAAC",
             "description": "The coastal marine system of the Gulf of Alaska (GoA) is connected hydrologically, biogeochemically and biologically with the upriver systems of the Copper River basin. Glacially weathered rock yields highly reactive particulate iron (Fe) into rivers that yields an important flux of bioavailable iron to the open ocean. North Pacific deep water is extremely nutrient-rich, and upwelling of deep water in estuaries and at river plumes results in very high biological productivity. The world-renowned fisheries in the vicinity of the Copper River region of the GoA thrive, in part, due to pristine riparian and lacustrine habitats for spawning and rearing. Pacific salmon spawn in the upper reaches of coastal watersheds, and their progeny spend a significant amount of time in freshwater habitats before migrating to the ocean. Prior to making the transition to a fully marine lifestyle, salmon smolts benefit from the enhanced biological productivity at plumes and within estuaries.The coastal GoA region is currently experiencing rapid and accelerating climate change as manifested by rapid recession of glaciers; climate models predict up to a 40% increase in river runoff from Alaska rivers by 2050. Over the coming decades an increase in glacier-dominated river discharge is likely, followed by decreases as glaciers recede. In addition, there will be a change in the seasonality of river discharge. Changes in freshwater discharge are likely to alter the flux of reactive particulate Fe, as well as dissolved organic and inorganic carbon (DIC and DOC) from glacier-dominated rivers, as well as the nitrate flux to surface water from estuarine upwelling, with cascading effects throughout the ecosystem. Furthermore, the freshwater supply of dissolved organic nitrogen (DON) and nitrate may increase over time due to recolonization of deglaciated watersheds by opportunistic nitrogen-fixing plants. New habitats for salmon and other members of the headwater ecosystem are likely to become available as glaciers retreat and as permafrost melts in the upper watershed. Conversely, decreased permafrost and decreased river flows may lead to the loss of habitat as freshwater sources dry seasonally or permanently. In addition, the positive or negative feedbacks to rising atmospheric CO2 concentrations, which are responsible for the warming and the subsequent melting of the glaciers, have not been addressed. As landscapes become ice free, the evolution of vegetation on these areas may act as net C sinks./The specific changes that will be manifested in the Copper River watershed and associated marine systems are difficult to predict and monitor. Using NASA products and a combination of remote sensing and field-based studies, this project seeks to establish a framework to document and monitor physical, biogeochemical biological changes in the coastal Gulf of Alaska adjacent to the Copper River.",
-            "title": "Remote sensing and field-based studies in the coastal Gulf of Alaska adjacent to the Copper River",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FCRP%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FCRP%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/CRP/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/CRP/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360197-OB_DAAC",
+            "issued": "2010-03-27",
+            "keyword": [
+                "ocean chemistry",
+                "ocean temperature",
+                "oceans",
+                "ocean optics",
+                "salinity/density",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/CRP/DATA001",
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
+            "temporal": "2010-03-27T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Remote sensing and field-based studies in the coastal Gulf of Alaska adjacent to the Copper River"
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
+            "description": "Exp: Shock Boundary Layer Interaction at M=2.05. This web page provides data from experiments that may be useful for the validation of turbulence models. This resource is expected to grow gradually over time. All data herein arepublicly available.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://turbmodels.larc.nasa.gov/Other_exp_Data/SBLI2.05/Baseline_experiments_3mm_and_5mm_ramps.tar.gz",
+                    "mediaType": "application/x-gzip"
+                }
             ],
+            "identifier": "NASA-855__1",
+            "issued": "2018-06-25",
             "keyword": [
                 "shock",
                 "layer",
@@ -165347,64 +165356,36 @@
                 "boundary",
                 "experiment"
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
-            "identifier": "NASA-855__1",
-            "description": "Exp: Shock Boundary Layer Interaction at M=2.05. This web page provides data from experiments that may be useful for the validation of turbulence models. This resource is expected to grow gradually over time. All data herein arepublicly available.",
-            "title": "Turbulence Models: Shock Boundary Layer Interaction at M=2.05",
-            "programCode": [
-                "026:023"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://turbmodels.larc.nasa.gov/Other_exp_Data/SBLI2.05/Baseline_experiments_3mm_and_5mm_ramps.tar.gz",
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
+            "title": "Turbulence Models: Shock Boundary Layer Interaction at M=2.05"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/4znx-aihc",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "temporal": "1967-01-01/1973-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "wise",
-                "space science",
-                "imagery",
-                "circulation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Site Admin",
                 "hasEmail": "mailto:rpif@lpi.usra.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-0000071",
             "description": "The Lunar Sample Atlas provides pictures of the Apollo samples taken in the Lunar Sample Laboratory, full-color views of the samples in microscopic thin-sections, cutting views and diagrams that illustrate how the samples were subdivided for scientific analyses, and in situ views of the samples on the lunar surface. The atlas contains information about the type of sample (e.g., rock, soil), the lithology (e.g., basalt, norite), and a description of the sample.",
-            "title": "Lunar Sample Atlas",
-            "programCode": [
-                "026:046"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -165412,60 +165393,88 @@
                     "mediaType": "text/html"
                 }
             ],
+            "identifier": "NASA-0000071",
+            "issued": "2018-06-25",
+            "keyword": [
+                "wise",
+                "space science",
+                "imagery",
+                "circulation"
+            ],
+            "landingPage": "https://data.nasa.gov/d/4znx-aihc",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:046"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
             "spatial": "Lunar",
-            "accrualPeriodicity": "irregular",
+            "temporal": "1967-01-01/1973-01-01",
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "Lunar Sample Atlas"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-EDC-IDA%2FGASPRA-APC%2FLC-V1.0",
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
+            "description": "Collected groundbased lightcurves of the asteroids Ida and Gaspra, extracted from the Asteroid Photometric Catalog of published lightcurves.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-edc-ida-gaspra-apc-lc-v1.0_4zqq-4e84",
+            "issued": "2018-06-26",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-EDC-IDA%2FGASPRA-APC%2FLC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-edc-ida-gaspra-apc-lc-v1.0_4zqq-4e84",
-            "description": "Collected groundbased lightcurves of the asteroids Ida and Gaspra, extracted from the Asteroid Photometric Catalog of published lightcurves.",
-            "title": "IDA/GASPRA GROUNDBASED LIGHTCURVES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "IDA/GASPRA GROUNDBASED LIGHTCURVES V1.0"
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
+            "description": "CIRS, ISS, RADAR, RPWS, RSS, SPICE, UVIS, VIMS",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20121002.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-498",
+            "issued": "2018-06-25",
             "keyword": [
                 "iss",
                 "rss",
@@ -165477,701 +165486,675 @@
                 "pds",
                 "radar"
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
-            "identifier": "NASA-498",
-            "description": "CIRS, ISS, RADAR, RPWS, RSS, SPICE, UVIS, VIMS",
-            "title": "PDS Cassini Data Release 31",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20121002.shtml",
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
+            "title": "PDS Cassini Data Release 31"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/yzp7-sm30",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Joint Research Centre - JRC - European Commission. 2022-02-25. INFORM Global Risk Index 2019 Mid Year, v0.3.7. Version 0.3.7. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/yzp7-sm30. https://doi.org/10.7927/yzp7-sm30.",
-            "issued": "2022-02-25",
-            "temporal": "2019-01-01T00:00:00Z/2019-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-25",
-            "keyword": [
-                "earth science",
-                "human dimensions",
-                "social behavior",
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
-            "identifier": "C2225516175-SEDAC",
-            "description": "The INFORM Global Risk Index 2019 Mid Year, v0.3.7 data set identifies the countries at a high risk of humanitarian crisis that are more likely to require international assistance. The INFORM Global Risk Index (GRI) model is based on risk concepts published in the scientific literature and envisages three dimensions of risk: Hazard & Exposure, Vulnerability, and Lack of Coping Capacity. The INFORM GRI model is split into different levels to provide a quick overview of the underlying factors leading to humanitarian risk. The INFORM GRI model supports a proactive crisis management framework, and will be helpful for an objective allocation of resources for disaster management, as well as for coordinated actions focused on anticipating, mitigating, and preparing for humanitarian emergencies. Only the two main sections, Vulnerability and Lack of Coping Capacity, not the Hazard & Exposure section, were used in the IPCC AR6.",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Joint Research Centre - JRC - European Commission",
-            "title": "INFORM Global Risk Index 2019 Mid Year, v0.3.7",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/ipcc/ipcc-inform-gri-2019-v0-3-7/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The INFORM Global Risk Index 2019 Mid Year, v0.3.7 data set identifies the countries at a high risk of humanitarian crisis that are more likely to require international assistance. The INFORM Global Risk Index (GRI) model is based on risk concepts published in the scientific literature and envisages three dimensions of risk: Hazard & Exposure, Vulnerability, and Lack of Coping Capacity. The INFORM GRI model is split into different levels to provide a quick overview of the underlying factors leading to humanitarian risk. The INFORM GRI model supports a proactive crisis management framework, and will be helpful for an objective allocation of resources for disaster management, as well as for coordinated actions focused on anticipating, mitigating, and preparing for humanitarian emergencies. Only the two main sections, Vulnerability and Lack of Coping Capacity, not the Hazard & Exposure section, were used in the IPCC AR6.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2Fyzp7-sm30",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2Fyzp7-sm30",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/ipcc/ipcc-inform-gri-2019-v0-3-7/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/ipcc/ipcc-inform-gri-2019-v0-3-7/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ipcc-inform-gri-2019-v0-3-7/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ipcc-inform-gri-2019-v0-3-7/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/ipcc/inform-gri-2019-v0-3-7/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/ipcc/inform-gri-2019-v0-3-7/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ipcc-inform-gri-2019-v0-3-7",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ipcc-inform-gri-2019-v0-3-7",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/ipcc/ipcc-inform-gri-2019-v0-3-7/sedac-logo.jpg",
+            "identifier": "C2225516175-SEDAC",
+            "issued": "2022-02-25",
+            "keyword": [
+                "earth science",
+                "human dimensions",
+                "social behavior",
+                "socioeconomics"
+            ],
+            "landingPage": "https://doi.org/10.7927/yzp7-sm30",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-02-25",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2019-01-01T00:00:00Z/2019-12-31T00:00:00Z",
             "theme": [
                 "IPCC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "INFORM Global Risk Index 2019 Mid Year, v0.3.7"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=JNO-J-UVS-2-EDR-V1.0",
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
-                "juno"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Juno Ultraviolet Spectrograph (UVS) CODMAC Level 2 Experiment Data Record\nis a collection of the far ultraviolet photon detections obtained by the UVS\ninstrument, in raw form.  As such, it constitutes the permanent record of the \nraw UVS data.  These data include both the instrument science and \nhousekeeping data, organized into extensions within files formatted \naccording to the Flexible Image Transport System (FITS) standard,\nversion 2.1b.  The UVS EDR archive enables reprocessing of the raw science\ndata as radiometric and geometric calibration processing routines improve.\nInvestigators interested in applying advanced calibration methods or needing\nto understand the properties of the raw data will find the EDR products \nuseful.  Most investigators, however, will be interested in using either the\nUVS data products contained in the CODMAC Level 3 Reduced Data Record,\nas radiometric and geometric calibration processing has already been done\nfor these products, or the UVS CODMAC Level 5 far ultraviolet map products.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.jno-j-uvs-2-edr-v1.0_4zv9-yegy",
+            "issued": "2021-05-21",
+            "keyword": [
+                "jupiter",
+                "juno"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=JNO-J-UVS-2-EDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.jno-j-uvs-2-edr-v1.0_4zv9-yegy",
-            "description": "The Juno Ultraviolet Spectrograph (UVS) CODMAC Level 2 Experiment Data Record\nis a collection of the far ultraviolet photon detections obtained by the UVS\ninstrument, in raw form.  As such, it constitutes the permanent record of the \nraw UVS data.  These data include both the instrument science and \nhousekeeping data, organized into extensions within files formatted \naccording to the Flexible Image Transport System (FITS) standard,\nversion 2.1b.  The UVS EDR archive enables reprocessing of the raw science\ndata as radiometric and geometric calibration processing routines improve.\nInvestigators interested in applying advanced calibration methods or needing\nto understand the properties of the raw data will find the EDR products \nuseful.  Most investigators, however, will be interested in using either the\nUVS data products contained in the CODMAC Level 3 Reduced Data Record,\nas radiometric and geometric calibration processing has already been done\nfor these products, or the UVS CODMAC Level 5 far ultraviolet map products.",
-            "title": "JUNO JUPITER UVS 2 \n\t\t\t\t   EXPERIMENT DATA RECORD V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "JUNO JUPITER UVS 2 \n\t\t\t\t   EXPERIMENT DATA RECORD V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-DERIVED-LIGHTCURVE-V12.0",
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
+            "description": "This is a compilation of published rotational parameters derived from lightcurve data for asteroids, based on the Warner et al. (2009) Asteroid Lightcurve Database. This is the version released on Mar. 2, 2011. In addition to reported rotational parameters by individual paper, there is a summary file with the values adopted by Harris, Warner, and Pravec as the most likely correct values for each asteroid. The data set also contains files listing known binary asteroids and 'tumbling' asteroids.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-derived-lightcurve-v12.0_4zyk-zi6g",
+            "issued": "2021-05-21",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-DERIVED-LIGHTCURVE-V12.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-derived-lightcurve-v12.0_4zyk-zi6g",
-            "description": "This is a compilation of published rotational parameters derived from lightcurve data for asteroids, based on the Warner et al. (2009) Asteroid Lightcurve Database. This is the version released on Mar. 2, 2011. In addition to reported rotational parameters by individual paper, there is a summary file with the values adopted by Harris, Warner, and Pravec as the most likely correct values for each asteroid. The data set also contains files listing known binary asteroids and 'tumbling' asteroids.",
-            "title": "ASTEROID LIGHTCURVE DERIVED DATA V12.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ASTEROID LIGHTCURVE DERIVED DATA V12.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-TEGA-4-EGSRDR-V1.0",
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
+            "description": "Calibrated or converted engineering, housekeeping and scientific data collected from the Thermal Evolved Gas Analyzer (TEGA) aboard the 2007 Mars Phoenix Lander.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-tega-4-egsrdr-v1.0_4zzi-urus",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "phoenix"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-TEGA-4-EGSRDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-tega-4-egsrdr-v1.0_4zzi-urus",
-            "description": "Calibrated or converted engineering, housekeeping and scientific data collected from the Thermal Evolved Gas Analyzer (TEGA) aboard the 2007 Mars Phoenix Lander.",
-            "title": "PHX MARS THERMAL EVOLVED GAS ANALYZER 4 EGSRDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "PHX MARS THERMAL EVOLVED GAS ANALYZER 4 EGSRDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-GRAND-2-EDR-VESTA-COUNTS-V1.0",
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
-                "dawn mission to vesta and ceres",
-                "4 vesta"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The GRaND EDR are a time-ordered collection of gamma ray   \nand neutron counting data and histograms acquired by GRaND during all         \nphases of the Dawn mission.  The dataset includes state-of-health data,       \nsuch as temperature and voltage readings, needed for the analysis of the      \ncounting data.  The EDR is an intermediate data product derived from the      \nraw data records using reversible operations.  All higher order data          \nproducts are derived from the EDR.  An automated pipeline is used to          \nprocess the EDR from the raw data records.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-grand-2-edr-vesta-counts-v1.0_4zzs-awzj",
+            "issued": "2018-06-26",
+            "keyword": [
+                "dawn mission to vesta and ceres",
+                "4 vesta"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-GRAND-2-EDR-VESTA-COUNTS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-grand-2-edr-vesta-counts-v1.0_4zzs-awzj",
-            "description": "The GRaND EDR are a time-ordered collection of gamma ray   \nand neutron counting data and histograms acquired by GRaND during all         \nphases of the Dawn mission.  The dataset includes state-of-health data,       \nsuch as temperature and voltage readings, needed for the analysis of the      \ncounting data.  The EDR is an intermediate data product derived from the      \nraw data records using reversible operations.  All higher order data          \nproducts are derived from the EDR.  An automated pipeline is used to          \nprocess the EDR from the raw data records.",
-            "title": "DAWN GRAND RAW (EDR) VESTA COUNTS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "DAWN GRAND RAW (EDR) VESTA COUNTS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2337",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Zheng, T., N. Queally, K.D. Chadwick, J. Cryer, P. Reim, C. Villanueva-Weeks, P. Townsend, M. Berg, Z. Breuer, N. Burkard, A. Hanson, E. Johnson, E. Kanski, D. Lacey, C. Lapinskas, A. Lee, E. Lisenbee, E. Marsh, L. Pfau, I. Shifrin, B. Skalitzky, S. Stroschein, J. Van beek, C. Vanden heuvel, and A. Williams. 2024. SHIFT: Laboratory Foliar Chemical Analysis Results for Field Samples, CA, 2022. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2337",
-            "issued": "2024-04-25",
-            "temporal": "2022-02-23T00:00:00Z/2022-09-27T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-26",
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
-            "identifier": "C2953889427-ORNL_CLOUD",
             "description": "This dataset holds laboratory foliar chemical analyses results for field samples collected during the 2022 NASA Surface Biology Geology (SBG) High Frequency Time series (SHIFT) campaign in Santa Barbara County, California, USA. Leaf samples were collected from plots within the Dangermond Preserve, Sedgwick Reserve, and Carpinteria Salt Marsh Reserve during the period of 2022-02-23 to 2022-09-27 and dried for later analysis. This project collected field data contemporaneously with weekly flights of the NASA's Airborne Visible-Infrared Imaging Spectrometer-Next Generation (AVIRIS-NG) facility instrument over the study areas. Sixteen chemical traits from two different lab analyses are provided. (a) Elemental analysis: foliar nitrogen (%), phosphorus (%), magnesium (%), potassium (%), calcium (%), sulfur (%), boron (ppm), iron (ppm), manganese (ppm), copper (ppm), zinc (ppm), aluminum (ppm), and sodium (ppm). (b) AnkomFiber analysis: foliar hemicellulose and bound protein (%), cellulose (%), and lignin (%). Related data packages contain additional plot-level characterization, biogeochemical, reflectance, and foliar data. These data are provided in comma separated values (CSV) format.",
-            "graphic-preview-description": "Scanned image of black mustard (Brassica nigra) leaves. Source: 001_LMA.jpeg from Chadwick et al. (2024).",
-            "title": "SHIFT: Laboratory Foliar Chemical Analysis Results for Field Samples, CA, 2022",
-            "graphic-preview-file": "https://daac.ornl.gov/SHIFT/guides/SHIFT_Foliar_Chemical_Analysis_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2337",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2337",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/shift/SHIFT_Foliar_Chemical_Analysis/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/shift/SHIFT_Foliar_Chemical_Analysis/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/SHIFT/guides/SHIFT_Foliar_Chemical_Analysis.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/SHIFT/guides/SHIFT_Foliar_Chemical_Analysis.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2337",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2337",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/shift/SHIFT_Foliar_Chemical_Analysis/comp/SHIFT_Foliar_Chemical_Analysis.pdf",
-                    "description": "SHIFT: Laboratory Foliar Chemical Analysis Results for Field Samples, CA, 2022: SHIFT_Foliar_Chemical_Analysis.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "SHIFT: Laboratory Foliar Chemical Analysis Results for Field Samples, CA, 2022: SHIFT_Foliar_Chemical_Analysis.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/shift/SHIFT_Foliar_Chemical_Analysis/comp/SHIFT_Foliar_Chemical_Analysis.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/SHIFT/guides/SHIFT_Foliar_Chemical_Analysis_Fig1.jpg",
-                    "description": "Scanned image of black mustard (Brassica nigra) leaves. Source: 001_LMA.jpeg from Chadwick et al. (2024).",
                     "@type": "dcat:Distribution",
+                    "description": "Scanned image of black mustard (Brassica nigra) leaves. Source: 001_LMA.jpeg from Chadwick et al. (2024).",
+                    "downloadURL": "https://daac.ornl.gov/SHIFT/guides/SHIFT_Foliar_Chemical_Analysis_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Scanned image of black mustard (Brassica nigra) leaves. Source: 001_LMA.jpeg from Chadwick et al. (2024).",
+            "graphic-preview-file": "https://daac.ornl.gov/SHIFT/guides/SHIFT_Foliar_Chemical_Analysis_Fig1.jpg",
+            "identifier": "C2953889427-ORNL_CLOUD",
+            "issued": "2024-04-25",
+            "keyword": [
+                "earth science",
+                "biosphere",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2337",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-04-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-120.49 34.4 -119.53 34.74",
+            "temporal": "2022-02-23T00:00:00Z/2022-09-27T23:59:59Z",
             "theme": [
                 "SHIFT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SHIFT: Laboratory Foliar Chemical Analysis Results for Field Samples, CA, 2022"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Suborbital/LISTOS/SurfaceMobile_InSitu_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2020-12-16. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/Suborbital/LISTOS/SurfaceMobile_InSitu_Data_1.",
-            "issued": "2020-09-08",
-            "temporal": "2018-05-23T00:00:00Z/2019-07-09T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-18",
-            "keyword": [
-                "air quality",
-                "atmosphere",
-                "atmospheric chemistry",
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
-            "identifier": "C1981412726-LARC_ASDC",
             "description": "LISTOS_SurfaceMobile_InSitu_Data is the Long Island Sound Tropospheric Ozone Study (LISTOS) surface mobile data collected via mobile platforms during the LISTOS field campaign. This product is a result of a joint effort across multiple agencies, including NASA, NOAA, the EPA Northeast States for Coordinated Air Use Management (NESCAUM), Maine Department of Environmental Protection, New Jersey Department of Environmental Protection, New York State Department of Environmental Conservation and several research groups at universities. Data collection is complete.\r\n\r\nThe New York City (NYC) metropolitan area (comprised of portions of New Jersey, New York, and Connecticut in and around NYC) is home to over 20 million people, but also millions of people living downwind in neighboring states. This area continues to persistently have challenges meeting past and recently revised federal health-based air quality standards for ground-level ozone, which impacts the health and well-being of residents living in the area. A unique feature of this chronic ozone problem is the pollution transported in a northeast direction out of NYC over Long Island Sound. The relatively cool waters of Long Island Sound confine the pollutants in a shallow and stable marine boundary layer. Afternoon heating over coastal land creates a sea breeze that carries the air pollution inland from the confined marine layer, resulting in high ozone concentrations in Connecticut and, at times, farther east into Rhode Island and Massachusetts. To investigate the evolving nature of ozone formation and transport in the NYC region and downwind, Northeast States for Coordinated Air Use Management (NESCAUM) launched the Long Island Sound Tropospheric Ozone Study (LISTOS). LISTOS was a multi-agency collaborative study focusing on Long Island Sound and the surrounding coastlines that continually suffer from poor air quality exacerbated by land/water circulation. The primary measurement observations took place between June-September 2018 and include in-situ and remote sensing instrumentation that were integrated aboard three aircraft, a network of ground sites, mobile vehicles, boat measurements, and ozonesondes. The goal of LISTOS was to improve the understanding of ozone chemistry and sea breeze transported pollution over Long Island Sound and its coastlines. LISTOS also provided NASA the opportunity to test air quality remote sensing retrievals with the use of its airborne simulators (GEOstationary Coastal and Air Pollution Events (GEO-CAPE) Airborne Simulator (GCAS), and Geostationary Trace gas and Aerosol Sensory Optimization (GeoTASO)) for the preparation of the Tropospheric Emissions; Monitoring of Pollution (TEMPO) observations for monitoring air quality from space. LISTOS also helped collaborators in the validation of Tropospheric Monitoring Instrument (TROPOMI) science products, with use of airborne- and ground-based measurements of ozone, NO2, and HCHO.",
-            "title": "LISTOS Surface Mobile Platform In-Situ Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSuborbital%2FLISTOS%2FSurfaceMobile_InSitu_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSuborbital%2FLISTOS%2FSurfaceMobile_InSitu_Data_1",
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
-                    "downloadURL": "http://www.nescaum.org/documents/listos",
-                    "description": "NESCAUM Project Page for Long Island Sound Tropospheric Ozone Study (LISTOS)",
                     "@type": "dcat:Distribution",
+                    "description": "NESCAUM Project Page for Long Island Sound Tropospheric Ozone Study (LISTOS)",
+                    "downloadURL": "http://www.nescaum.org/documents/listos",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/listos/index.html",
-                    "description": "LISTOS Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "LISTOS Project Home Page",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/listos/index.html",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ui.adsabs.harvard.edu/abs/2018AGUFM.A34B..01M/abstract",
-                    "description": "Overview of the Long Island Sound Tropospheric Ozone Study (LISTOS) by Miller, P. J.",
                     "@type": "dcat:Distribution",
+                    "description": "Overview of the Long Island Sound Tropospheric Ozone Study (LISTOS) by Miller, P. J.",
+                    "downloadURL": "https://ui.adsabs.harvard.edu/abs/2018AGUFM.A34B..01M/abstract",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.epa.gov/epa/sites/production/files/2018-06/documents/listos_factsheet_final.pdf",
-                    "description": "EPA Fact Sheet for Long Island Sound Tropospheric Ozone Study (LISTOS)",
                     "@type": "dcat:Distribution",
+                    "description": "EPA Fact Sheet for Long Island Sound Tropospheric Ozone Study (LISTOS)",
+                    "downloadURL": "https://archive.epa.gov/epa/sites/production/files/2018-06/documents/listos_factsheet_final.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1981412726-LARC_ASDC",
-                    "description": "Earthdata Search for LISTOS_SurfaceMobile_InSitu_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for LISTOS_SurfaceMobile_InSitu_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1981412726-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/feature/langley/nasa-joins-effort-to-sniff-out-ozone-in-the-northeast",
-                    "description": "LISTOS Nasa.gov \u201cNASA Joins Effort to Sniff Out Ozone in the Northeast\u201d Article",
                     "@type": "dcat:Distribution",
+                    "description": "LISTOS Nasa.gov \u201cNASA Joins Effort to Sniff Out Ozone in the Northeast\u201d Article",
+                    "downloadURL": "https://www.nasa.gov/feature/langley/nasa-joins-effort-to-sniff-out-ozone-in-the-northeast",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.epa.gov/sciencematters/air-land-and-sea-tackling-ozone-issue-lake-michigans-shores",
-                    "description": "LISTOS EPA \u201cBy Air, Land, and Sea: Tackling the Ozone Issue on Lake Michigan\u2019s Shores\u201d Article",
                     "@type": "dcat:Distribution",
+                    "description": "LISTOS EPA \u201cBy Air, Land, and Sea: Tackling the Ozone Issue on Lake Michigan\u2019s Shores\u201d Article",
+                    "downloadURL": "https://www.epa.gov/sciencematters/air-land-and-sea-tackling-ozone-issue-lake-michigans-shores",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/LISTOS/2017#",
-                    "description": "LISTOS Data on the Sub-Orbital Order Tool (SOOT) Power User Interface (UI)",
                     "@type": "dcat:Distribution",
+                    "description": "LISTOS Data on the Sub-Orbital Order Tool (SOOT) Power User Interface (UI)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/LISTOS/2017#",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/LISTOS/SurfaceMobile_InSitu_Data_1/",
-                    "description": "ASDC Direct Data Download for LISTOS_SurfaceMobile_InSitu_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for LISTOS_SurfaceMobile_InSitu_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/LISTOS/SurfaceMobile_InSitu_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1981412726-LARC_ASDC",
+            "issued": "2020-09-08",
+            "keyword": [
+                "air quality",
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Suborbital/LISTOS/SurfaceMobile_InSitu_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-04-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>35.0 -80.0 35.0 -70.0 45.0 -70.0 45.0 -80.0 35.0 -80.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2018-05-23T00:00:00Z/2019-07-09T23:59:59.999Z",
             "theme": [
                 "LISTOS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LISTOS Surface Mobile Platform In-Situ Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/TRATLEQ1/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/TRATLEQ1/DATA001.",
-            "issued": "2019-09-19",
-            "temporal": "2019-09-19T00:00:00Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "oceans",
-                "salinity/density",
-                "ocean temperature",
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
-            "identifier": "C1976625960-OB_DAAC",
             "description": "TRATLEQ1 was an interdisciplinary cruise focusing on upwelling in the tropical Atlantic, its physical forcing, its importance for biological production and plankton communities, associated chemical cycles, as well as on the current system setting the background conditions for the downward carbon export. This cruise represents the first physical, chemical, biogeochemical and biological measurement program covering a whole equatorial section from the eastern to the western boundary and from the surface to the bottom. TRATLEQ I is a contribution to the GEOMAR research program OCEANS, to the EU projects TRIATLAS, the Make Our Planet Great Again project by R. Kiko and to the BMBF cooperative project BANINO in the frame of the BMBF SPACES program.",
-            "title": "The Transatlantic Equatorial Cruise I, TRIATLAS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FTRATLEQ1%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FTRATLEQ1%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/TRATLEQ1/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/TRATLEQ1/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1976625960-OB_DAAC",
+            "issued": "2019-09-19",
+            "keyword": [
+                "oceans",
+                "salinity/density",
+                "ocean temperature",
+                "earth science",
+                "ocean chemistry",
+                "ocean optics"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/TRATLEQ1/DATA001",
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
+            "temporal": "2019-09-19T00:00:00Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "The Transatlantic Equatorial Cruise I, TRIATLAS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1422-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-02-14T02:48:35.000 to 2016-02-14T11:55:25.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1422-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1422-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1422-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-02-14T02:48:35.000 to 2016-02-14T11:55:25.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1422 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1422 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0813-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-05-28T14:06:20.000 to 2015-05-28T15:57:45.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0813-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0813-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0813-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-05-28T14:06:20.000 to 2015-05-28T15:57:45.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0813 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0813 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-RSS-1%2F5-EROS%2FORBIT-V1.0",
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
+            "description": "The NEAR Eros Radio Science Data Set is a time-ordered collection of raw and partially processed data collected during the NEAR orbital mapping of the asteroid 433 Eros.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-rss-1-5-eros-orbit-v1.0_529n-6f8p",
+            "issued": "2021-05-21",
+            "keyword": [
+                "eros",
+                "near earth asteroid rendezvous"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-RSS-1%2F5-EROS%2FORBIT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-rss-1-5-eros-orbit-v1.0_529n-6f8p",
-            "description": "The NEAR Eros Radio Science Data Set is a time-ordered collection of raw and partially processed data collected during the NEAR orbital mapping of the asteroid 433 Eros.",
-            "title": "NEAR EROS RADIO SCIENCE DATA SET - EROS/ORBIT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEAR EROS RADIO SCIENCE DATA SET - EROS/ORBIT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ICE-C-ULECA-3-RDR-GIACOBINI-ZIN-V1.0",
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
+            "description": "Energetic particle observations made with the ULECA sensor on the International Cometary Explorer encounter with comet Giacobini-Zinner in Sept, 1985.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ice-c-uleca-3-rdr-giacobini-zin-v1.0_52c7-hmrz",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international cometary explorer",
+                "giacobini-zinner"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ICE-C-ULECA-3-RDR-GIACOBINI-ZIN-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ice-c-uleca-3-rdr-giacobini-zin-v1.0_52c7-hmrz",
-            "description": "Energetic particle observations made with the ULECA sensor on the International Cometary Explorer encounter with comet Giacobini-Zinner in Sept, 1985.",
-            "title": "ULECA SELECTED COUNTS FOR GZ ENCOUNTER",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ULECA SELECTED COUNTS FOR GZ ENCOUNTER"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1000000001-CDDIS.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GGL/CDDIS.",
-            "issued": "2009-04-29",
-            "temporal": "2008-06-20T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2012-05-31",
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
-            "identifier": "C1000000001-CDDIS",
             "description": "The Doppler Orbitography by Radiopositioning Integrated on Satellite (DORIS) was developed by the Centre National d'Etudes Spatiales (CNES) with cooperation from other French government agencies. The system was developed to provide precise orbit determination and high accuracy location of ground beacons for point positioning. DORIS is a dual-frequency Doppler system that has been included as an experiment on various space missions such as TOPEX/Poseidon, SPOT-2, -3, -4, and -5, Envisat, and Jason satellites. Unlike many other navigation systems, DORIS is based on an uplink device. The receivers are on board the satellite with the transmitters are on the ground. This creates a centralized system in which the complete set of observations is downloaded by the satellite to the ground center, from where they are distributed after editing and processing. An accurate measurment is made of the Doppler shift on radiofrequency signals emitted by the ground beacons and received on the spacecraft.",
-            "title": "CDDIS_DORIS_data_rinex",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -166180,610 +166163,599 @@
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1000000001-CDDIS",
+            "issued": "2009-04-29",
+            "keyword": [
+                "nasa"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1000000001-CDDIS.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2012-05-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GGL/CDDIS"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2008-06-20T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "IDS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CDDIS_DORIS_data_rinex"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-RADAR-V18.0",
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
+            "description": "This data set is intended to include all published groundbased asteroid radar detections. The file is based on the collection of asteroid radar detections established by Steven J. Ostro and currently maintained by Lance A.M. Benner. The file includes disc-integrated radar properties extracted from the published papers.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-radar-v18.0_52ds-4dcn",
+            "issued": "2021-05-21",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-RADAR-V18.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-radar-v18.0_52ds-4dcn",
-            "description": "This data set is intended to include all published groundbased asteroid radar detections. The file is based on the collection of asteroid radar detections established by Steven J. Ostro and currently maintained by Lance A.M. Benner. The file includes disc-integrated radar properties extracted from the published papers.",
-            "title": "ASTEROID RADAR V18.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ASTEROID RADAR V18.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ROS-E%2FM%2FA%2FC-SPICE-6-V1.0",
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
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "SPICE deals with ancillary data needed to support the planning for, and analysis of, science instrument data. As well as software (the SPICE toolkit) and documentation, SPICE provides data files, called kernels, that contain ancillary information which has been created in such a way as to allow easy access and correct usage by the space science and engineering communities.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ros-e-m-a-c-spice-6-v1.0_52is-3kcw",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ROS-E%2FM%2FA%2FC-SPICE-6-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ros-e-m-a-c-spice-6-v1.0_52is-3kcw",
-            "description": "SPICE deals with ancillary data needed to support the planning for, and analysis of, science instrument data. As well as software (the SPICE toolkit) and documentation, SPICE provides data files, called kernels, that contain ancillary information which has been created in such a way as to allow easy access and correct usage by the space science and engineering communities.",
-            "title": "ROSETTA SPICE KERNELS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA SPICE KERNELS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/Aqua/AIRS/DATA319",
             "citation": "AIRS Science Team/Joao Teixeira. 2013-03-12. AIRX3STM. Version 006. AIRS/Aqua L3 Monthly Standard Physical Retrieval (AIRS+AMSU) 1 degree x 1 degree V006. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aqua/AIRS/DATA319. https://disc.gsfc.nasa.gov/datacollection/AIRX3STM_006.html. Digital Science Data.",
-            "issued": "2002-09-01",
-            "temporal": "2002-09-01T00:00:00Z/2016-10-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-10-01",
-            "references": [
-                "https://doi.org/10.1117/1.JRS.8.084994",
-                "https://doi.org/10.5194/acp-14-399-2014"
-            ],
-            "keyword": [
-                "atmospheric radiation",
-                "clouds",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "earth science",
-                "land surface",
-                "atmospheric pressure",
-                "air quality",
-                "atmosphere",
-                "oceans",
-                "altitude",
-                "atmospheric chemistry",
-                "ocean temperature",
-                "surface thermal properties",
-                "surface radiative properties"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ED ESFANDIARI",
                 "hasEmail": "mailto:asghar.e.esfandiari@nasa.gov"
             },
+            "creator": "AIRS Science Team/Joao Teixeira",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1238517346-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The Atmospheric Infrared Sounder (AIRS) is a grating spectrometer (R = 1200) aboard the second Earth Observing System (EOS) polar-orbiting platform, EOS Aqua. In combination with the Advanced Microwave Sounding Unit (AMSU) and the Humidity Sounder for Brazil (HSB), AIRS constitutes an innovative atmospheric sounding group of visible, infrared, and microwave sensors. The AIRS Level 3 Monthly Gridded Retrieval Product contains standard retrieval means, standard deviations and input counts. Each file covers a calendar month. The mean values are simply the arithmetic means of the daily products, weighted by the number of input counts for each day in that grid box. The geophysical parameters have been averaged and binned into 1 x1 deg grid cells, from -180.0 to +180.0 deg longitude and from -90.0 to +90.0 deg latitude. For each grid map of 4-byte floating-point mean values there is a corresponding 4-byte floating-point map of standard deviation and a 2-byte integer grid map of counts. The counts map provides the user with the number of points per bin that were included in the mean and can be used to generate custom multi-day maps from the daily gridded products. The thermodynamic parameters are: Skin Temperature (land and sea surface), Air Temperature at the surface, Profiles of Air Temperature and Water Vapor, Tropopause Characteristics, Column Precipitable Water, Cloud Amount/Frequency, Cloud Height, Cloud Top Pressure, Cloud Top Temperature, Reflectance, Emissivity, Surface Pressure, Cloud Vertical Distribution. The trace gases parameters are: Total Amounts and Vertical Profiles of Carbon Monoxide, Methane, and Ozone. The actual names of the variables in the data files should be inferred from the Processing File Description document.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "AIRX3STM",
-            "creator": "AIRS Science Team/Joao Teixeira",
-            "graphic-preview-description": "Sample data of the \"AIRS/Aqua Level 3 monthly standard physical retrieval product (Without HSB)\".",
-            "title": "AIRS/Aqua L3 Monthly Standard Physical Retrieval (AIRS+AMSU) 1 degree x 1 degree V006 (AIRX3STM) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRX3STM_006.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAqua%2FAIRS%2FDATA319",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAqua%2FAIRS%2FDATA319",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRX3STM_006.png",
-                    "description": "Sample data of the \"AIRS/Aqua Level 3 monthly standard physical retrieval product (Without HSB)\".",
                     "@type": "dcat:Distribution",
+                    "description": "Sample data of the \"AIRS/Aqua Level 3 monthly standard physical retrieval product (Without HSB)\".",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRX3STM_006.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRX3STM_006.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRX3STM_006.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level3/AIRX3STM.006/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level3/AIRX3STM.006/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level3/AIRX3STM.006/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level3/AIRX3STM.006/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRX3STM+006",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRX3STM+006",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc1.gsfc.nasa.gov/daac-bin/wms_airs?service=WMS&version=1.1.1&request=GetCapabilities",
-                    "description": "NASA GES DISC AIRS Gridded L3 data Web Map Service.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA GES DISC AIRS Gridded L3 data Web Map Service.",
+                    "downloadURL": "https://disc1.gsfc.nasa.gov/daac-bin/wms_airs?service=WMS&version=1.1.1&request=GetCapabilities",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc1.gsfc.nasa.gov/daac-bin/wms_airs?LAYERS=AIRX3STM_TOTH2OVAP_A&TRANSPARENT=TRUE&HEIGHT=360&VERSION=1.1.1&WIDTH=720&SRS=EPSG%3A4326&bbox=-180%2C-90%2C180%2C90&FORMAT=image%2Fpng&service=WMS&REQUEST=GetMap",
-                    "description": "Get map example for NASA GES DISC AIRS Gridded L3 data Web Map Service.",
                     "@type": "dcat:Distribution",
+                    "description": "Get map example for NASA GES DISC AIRS Gridded L3 data Web Map Service.",
+                    "downloadURL": "https://disc1.gsfc.nasa.gov/daac-bin/wms_airs?LAYERS=AIRX3STM_TOTH2OVAP_A&TRANSPARENT=TRUE&HEIGHT=360&VERSION=1.1.1&WIDTH=720&SRS=EPSG%3A4326&bbox=-180%2C-90%2C180%2C90&FORMAT=image%2Fpng&service=WMS&REQUEST=GetMap",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/daac-bin/wcsAIRSL3?service=WCS&version=1.0.0&request=GetCapabilities",
-                    "description": "NASA GES DISC AIRS Gridded L3 data Web Coverage Service.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA GES DISC AIRS Gridded L3 data Web Coverage Service.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/daac-bin/wcsAIRSL3?service=WCS&version=1.0.0&request=GetCapabilities",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/daac-bin/wcsAIRSL3?Coverage=AIRX3STM%3ACO_VMR_A&resy=1.0&BBOX=-197.5%2C-89.5%2C179.5%2C89.5&CRS=EPSG%3A4326&request=GetCoverage&version=1.0.0&resx=1.0&service=WCS&Time=2013-07&format=netCDF",
-                    "description": "Example of getting coverage data from the NASA GES DISC AIRS Gridded L3 data Web Coverage Service. It requests one of the variables, AIRX3STM:CO_VMR_A as listed in the GetCapabilities response, at given TIME and BBOX.",
                     "@type": "dcat:Distribution",
+                    "description": "Example of getting coverage data from the NASA GES DISC AIRS Gridded L3 data Web Coverage Service. It requests one of the variables, AIRX3STM:CO_VMR_A as listed in the GetCapabilities response, at given TIME and BBOX.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/daac-bin/wcsAIRSL3?Coverage=AIRX3STM%3ACO_VMR_A&resy=1.0&BBOX=-197.5%2C-89.5%2C179.5%2C89.5&CRS=EPSG%3A4326&request=GetCoverage&version=1.0.0&resx=1.0&service=WCS&Time=2013-07&format=netCDF",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
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
+            "graphic-preview-description": "Sample data of the \"AIRS/Aqua Level 3 monthly standard physical retrieval product (Without HSB)\".",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRX3STM_006.png",
+            "identifier": "C1238517346-GES_DISC",
+            "issued": "2002-09-01",
+            "keyword": [
+                "atmospheric radiation",
+                "clouds",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "earth science",
+                "land surface",
+                "atmospheric pressure",
+                "air quality",
+                "atmosphere",
+                "oceans",
+                "altitude",
+                "atmospheric chemistry",
+                "ocean temperature",
+                "surface thermal properties",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aqua/AIRS/DATA319",
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
+            "series-name": "AIRX3STM",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-09-01T00:00:00Z/2016-10-01T23:59:59.999Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AIRS/Aqua L3 Monthly Standard Physical Retrieval (AIRS+AMSU) 1 degree x 1 degree V006 (AIRX3STM) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TERRA/CERES/SYN1DEGMONTH_L3.004A",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2017-09-19. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/TERRA/CERES/SYN1DEGMONTH_L3.004A.",
-            "issued": "2015-06-17",
-            "temporal": "2000-03-01T00:00:00Z/2002-06-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-13",
-            "keyword": [
-                "atmospheric temperature",
-                "aerosols",
-                "atmospheric water vapor",
-                "atmosphere",
-                "atmospheric pressure",
-                "atmospheric radiation",
-                "vegetation",
-                "national geospatial data asset",
-                "earth science",
-                "clouds",
-                "biosphere",
-                "ngda"
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
-            "identifier": "C1419910530-LARC_ASDC",
             "description": "CER_SYN1deg-Month_Terra-MODIS_Edition4A is the Clouds and the Earth's Radiant Energy System (CERES) and and geostationary (GEO)-Enhanced Top of Atmosphere (TOA), Within-Atmosphere and Surface Fluxes Clouds and Aerosols Monthly Terra Edition4A data product, which was collected using Imaging Radiometers on Geostationary Satellites platform as well as CERES Flight Model 1 (FM1), CERES FM2, and MODIS on Terra. Data collection for this product is complete.\r\n\r\nCERES Synoptic (SYN)1 degree products provide CERES-observed temporally interpolated TOA radiative fluxes and coincident MODIS-derived cloud and aerosol properties and include geostationary-derived cloud properties and broadband fluxes that have been carefully normalized with CERES fluxes in order to maintain the CERES calibration. They also contain computed initial TOA, in-atmosphere, and surface fluxes and computed fluxes that have been adjusted or constrained to the CERES-observed TOA fluxes. The computed fluxes are produced using the Langley Fu-Liou radiative transfer model. Computations use MODIS and geostationary satellite cloud properties along with atmospheric profiles provided by the NASA Global Modeling and Assimilation Office (GMAO). The adjustments to clouds and atmospheric properties are also provided. The computations are made for all-sky, clear-sky, pristine (clear-sky without aerosols), and all-sky without aerosol conditions. This product provides parameters on a three-hourly temporal resolution and 1\u00b0-regional spatial scales. Fluxes are provided for clear-sky and all-sky conditions in the longwave (LW), shortwave (SW), and window (WN) regions.\r\n\r\nCERES SYN1deg products use 1-hourly radiances and cloud property data from geostationary (GEO) imagers to more accurately model variability between CERES observations. To use GEO data to enhance diurnal sampling, several steps are involved. First, GEO radiances are cross-calibrated with the MODIS imager using only data that is coincident in time and ray-matched in angle. Next, the GEO cloud retrievals are inferred from the calibrated GEO radiances. The GEO radiances are converted from narrowband to broadband using empirical regressions and then to broadband GEO TOA fluxes using Angular Distribution Models (ADMs) and directional models. To ensure GEO and CERES TOA fluxes are consistent, a normalization technique is used. Instantaneous matched gridded fluxes from CERES and GEO are regressed against one another over a month from 5\u00b0x5 \u00b0 latitude-longitude regions. The regression relation is then applied to all GEO fluxes to remove biases that depend upon cloud amount, solar and view zenith angles, and regional dependencies. The regional means are determined for 1\u00b0 equal-angle grid boxes calculated by first interpolating each parameter for any missing times of the CERES/GEO observations to produce a complete 1-hourly time series for the month. Monthly means are calculated using the combination of observed and interpolated parameters from all days containing at least one CERES observation.\r\n\r\nCERES is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions are a follow-on to the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument, protoflight model (PFM), was launched on November 27, 1997 as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the Earth Observing System (EOS) flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board Earth Observing System (EOS) Aqua on May 4, 2002. The CERES FM5 instrument was launched on board the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The newest CERES instrument (FM6) was launched on board the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite, no",
-            "title": "CERES and GEO-Enhanced TOA, Within-Atmosphere, and Surface Fluxes Clouds and Aerosols Monthly Terra Edition4A",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FCERES%2FSYN1DEGMONTH_L3.004A",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FCERES%2FSYN1DEGMONTH_L3.004A",
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
-                    "downloadURL": "https://doi.org/10.5067/TERRA+AQUA/CERES/SYN1DEGMONTH_L3.004A",
-                    "description": "DOI data set landing page for CERES SYN 1 degree Month Level 3 Edition 4A data products",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CERES SYN 1 degree Month Level 3 Edition 4A data products",
+                    "downloadURL": "https://doi.org/10.5067/TERRA+AQUA/CERES/SYN1DEGMONTH_L3.004A",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1419910530-LARC_ASDC",
-                    "description": "Earthdata Search for CER_SYN1deg-Month_Terra-MODIS_Edition4A (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CER_SYN1deg-Month_Terra-MODIS_Edition4A (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1419910530-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
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
@@ -166793,781 +166765,787 @@
                     "title": "Download this dataset through the CERES Ordering Tool"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/SYN1deg-Month/Terra-MODIS_Edition4A/",
-                    "description": "ASDC Direct Data Download for CER_SYN1deg-Month_Terra-MODIS_Edition4A",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CER_SYN1deg-Month_Terra-MODIS_Edition4A",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/SYN1deg-Month/Terra-MODIS_Edition4A/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/SYN1deg-Month/Terra-MODIS_Edition4A/contents.html",
-                    "description": "OPeNDAP data access for CER_SYN1deg-Month_Terra-MODIS_Edition4A",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CER_SYN1deg-Month_Terra-MODIS_Edition4A",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/SYN1deg-Month/Terra-MODIS_Edition4A/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1419910530-LARC_ASDC",
+            "issued": "2015-06-17",
+            "keyword": [
+                "atmospheric temperature",
+                "aerosols",
+                "atmospheric water vapor",
+                "atmosphere",
+                "atmospheric pressure",
+                "atmospheric radiation",
+                "vegetation",
+                "national geospatial data asset",
+                "earth science",
+                "clouds",
+                "biosphere",
+                "ngda"
+            ],
+            "landingPage": "https://doi.org/10.5067/TERRA/CERES/SYN1DEGMONTH_L3.004A",
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
+            "temporal": "2000-03-01T00:00:00Z/2002-06-30T23:59:59.999Z",
             "theme": [
                 "CERES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CERES and GEO-Enhanced TOA, Within-Atmosphere, and Surface Fluxes Clouds and Aerosols Monthly Terra Edition4A"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1593",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Davis, K.J., M.D. Obland, B. Lin, T. Lauvaux, C. O'Dell, B. Meadows, E.V. Browell, J.P. DiGangi, C. Sweeney, M.J. McGill, J.D. Barrick, A.R. Nehrir, M.M. Yang, J.R. Bennett, B.C. Baier, A. Roiger, S. Pal, T. Gerken, A. Fried, S. Feng, R. Shrestha, M.A. Shook, G. Chen, L.J. Campbell, Z.R. Barkley, and R.M. Pauly. 2018. ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1593",
-            "issued": "2020-07-20",
-            "temporal": "2016-07-11T14:16:00Z/2019-07-27T20:10:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-17",
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
-            "identifier": "C2367023363-ORNL_CLOUD",
             "description": "This dataset provides merged data products acquired during flights over the central and eastern United States as part of the Atmospheric Carbon and Transport - America (ACT-America) project. Two aircraft platforms, the NASA Langley Beechcraft B200 King Air and the NASA Goddard Space Flight Center's C-130H Hercules, were used to collect high-quality in situ measurements across a variety of continental surfaces and atmospheric conditions. The merged data products are composed of continuous in situ measurements of atmospheric carbon dioxide (CO2), methane (CH4), carbon monoxide (CO), ozone (O3), and ethane (C2H6, B200 aircraft only) that were averaged to uniform intervals and merged with aircraft navigation and meteorological variables as well as trace gas concentrations from discrete flask samples collected with the Programmable Flask Package (PFP). These merged data products provide integrated measurements at intervals useful to the modeling community for studying the transport and fluxes of atmospheric carbon dioxide and methane across North America.",
-            "graphic-preview-description": "ACT-America 2019 summer airborne campaign showing the flight paths for the two aircrafts and location of ground towers. Flights were concentrated on three study domains: northeast, south-central, and midwest regions of the United States.",
-            "title": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA",
-            "graphic-preview-file": "https://daac.ornl.gov/ACTAMERICA/guides/ACTAMERICA_Merge_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1593",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1593",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/actamerica/ACTAMERICA_Merge/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/actamerica/ACTAMERICA_Merge/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ACTAMERICA/guides/ACTAMERICA_Merge.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ACTAMERICA/guides/ACTAMERICA_Merge.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1593",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1593",
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrg01-b200_merge_R0_fall2017_README.txt",
-                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrg01-b200_merge_R0_fall2017_README.txt",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrg01-b200_merge_R0_fall2017_README.txt",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrg01-b200_merge_R0_fall2017_README.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrg01-b200_merge_R0_spring2018_README.txt",
-                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrg01-b200_merge_R0_spring2018_README.txt",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrg01-b200_merge_R0_spring2018_README.txt",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrg01-b200_merge_R0_spring2018_README.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrg01-b200_merge_R0_summer2016_README.txt",
-                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrg01-b200_merge_R0_summer2016_README.txt",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrg01-b200_merge_R0_summer2016_README.txt",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrg01-b200_merge_R0_summer2016_README.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrg01-b200_merge_R0_summer2019_README.txt",
-                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrg01-b200_merge_R0_summer2019_README.txt",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrg01-b200_merge_R0_summer2019_README.txt",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrg01-b200_merge_R0_summer2019_README.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrg01-b200_merge_R1_winter2017_README.txt",
-                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrg01-b200_merge_R1_winter2017_README.txt",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrg01-b200_merge_R1_winter2017_README.txt",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrg01-b200_merge_R1_winter2017_README.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrg01-c130_merge_R0_fall2017_README.txt",
-                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrg01-c130_merge_R0_fall2017_README.txt",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrg01-c130_merge_R0_fall2017_README.txt",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrg01-c130_merge_R0_fall2017_README.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrg01-c130_merge_R0_spring2018_README.txt",
-                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrg01-c130_merge_R0_spring2018_README.txt",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrg01-c130_merge_R0_spring2018_README.txt",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrg01-c130_merge_R0_spring2018_README.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrg01-c130_merge_R0_summer2019_README.txt",
-                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrg01-c130_merge_R0_summer2019_README.txt",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrg01-c130_merge_R0_summer2019_README.txt",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrg01-c130_merge_R0_summer2019_README.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrg01-c130_merge_R1_winter2017_README.txt",
-                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrg01-c130_merge_R1_winter2017_README.txt",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrg01-c130_merge_R1_winter2017_README.txt",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrg01-c130_merge_R1_winter2017_README.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrg01-c130_merge_R3_summer2016_README.txt",
-                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrg01-c130_merge_R3_summer2016_README.txt",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrg01-c130_merge_R3_summer2016_README.txt",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrg01-c130_merge_R3_summer2016_README.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrg05-b200_merge_R0_fall2017_README.txt",
-                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrg05-b200_merge_R0_fall2017_README.txt",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrg05-b200_merge_R0_fall2017_README.txt",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrg05-b200_merge_R0_fall2017_README.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrg05-b200_merge_R0_spring2018_README.txt",
-                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrg05-b200_merge_R0_spring2018_README.txt",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrg05-b200_merge_R0_spring2018_README.txt",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrg05-b200_merge_R0_spring2018_README.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrg05-b200_merge_R0_summer2016_README.txt",
-                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrg05-b200_merge_R0_summer2016_README.txt",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrg05-b200_merge_R0_summer2016_README.txt",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrg05-b200_merge_R0_summer2016_README.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrg05-b200_merge_R0_summer2019_README.txt",
-                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrg05-b200_merge_R0_summer2019_README.txt",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrg05-b200_merge_R0_summer2019_README.txt",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrg05-b200_merge_R0_summer2019_README.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrg05-b200_merge_R1_winter2017_README.txt",
-                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrg05-b200_merge_R1_winter2017_README.txt",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrg05-b200_merge_R1_winter2017_README.txt",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrg05-b200_merge_R1_winter2017_README.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrg05-c130_merge_R0_fall2017_README.txt",
-                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrg05-c130_merge_R0_fall2017_README.txt",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrg05-c130_merge_R0_fall2017_README.txt",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrg05-c130_merge_R0_fall2017_README.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrg05-c130_merge_R0_spring2018_README.txt",
-                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrg05-c130_merge_R0_spring2018_README.txt",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrg05-c130_merge_R0_spring2018_README.txt",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrg05-c130_merge_R0_spring2018_README.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrg05-c130_merge_R0_summer2019_README.txt",
-                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrg05-c130_merge_R0_summer2019_README.txt",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrg05-c130_merge_R0_summer2019_README.txt",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrg05-c130_merge_R0_summer2019_README.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrg05-c130_merge_R1_winter2017_README.txt",
-                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrg05-c130_merge_R1_winter2017_README.txt",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrg05-c130_merge_R1_winter2017_README.txt",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrg05-c130_merge_R1_winter2017_README.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrg05-c130_merge_R3_summer2016_README.txt",
-                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrg05-c130_merge_R3_summer2016_README.txt",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrg05-c130_merge_R3_summer2016_README.txt",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrg05-c130_merge_R3_summer2016_README.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrgPFP-b200_merge_R0_fall2017_README.txt",
-                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrgPFP-b200_merge_R0_fall2017_README.txt",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrgPFP-b200_merge_R0_fall2017_README.txt",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrgPFP-b200_merge_R0_fall2017_README.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrgPFP-b200_merge_R0_spring2018_README.txt",
-                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrgPFP-b200_merge_R0_spring2018_README.txt",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrgPFP-b200_merge_R0_spring2018_README.txt",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrgPFP-b200_merge_R0_spring2018_README.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrgPFP-b200_merge_R0_summer2016_README.txt",
-                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrgPFP-b200_merge_R0_summer2016_README.txt",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrgPFP-b200_merge_R0_summer2016_README.txt",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrgPFP-b200_merge_R0_summer2016_README.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrgPFP-b200_merge_R0_summer2019_README.txt",
-                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrgPFP-b200_merge_R0_summer2019_README.txt",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrgPFP-b200_merge_R0_summer2019_README.txt",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrgPFP-b200_merge_R0_summer2019_README.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrgPFP-b200_merge_R1_winter2017_README.txt",
-                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrgPFP-b200_merge_R1_winter2017_README.txt",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrgPFP-b200_merge_R1_winter2017_README.txt",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrgPFP-b200_merge_R1_winter2017_README.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrgPFP-c130_merge_R0_fall2017_README.txt",
-                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrgPFP-c130_merge_R0_fall2017_README.txt",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrgPFP-c130_merge_R0_fall2017_README.txt",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrgPFP-c130_merge_R0_fall2017_README.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrgPFP-c130_merge_R0_spring2018_README.txt",
-                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrgPFP-c130_merge_R0_spring2018_README.txt",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrgPFP-c130_merge_R0_spring2018_README.txt",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrgPFP-c130_merge_R0_spring2018_README.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrgPFP-c130_merge_R0_summer2019_README.txt",
-                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrgPFP-c130_merge_R0_summer2019_README.txt",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrgPFP-c130_merge_R0_summer2019_README.txt",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrgPFP-c130_merge_R0_summer2019_README.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrgPFP-c130_merge_R1_winter2017_README.txt",
-                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrgPFP-c130_merge_R1_winter2017_README.txt",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrgPFP-c130_merge_R1_winter2017_README.txt",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrgPFP-c130_merge_R1_winter2017_README.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrgPFP-c130_merge_R3_summer2016_README.txt",
-                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrgPFP-c130_merge_R3_summer2016_README.txt",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA-mrgPFP-c130_merge_R3_summer2016_README.txt",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA-mrgPFP-c130_merge_R3_summer2016_README.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA_Merge.pdf",
-                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA_Merge.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: ACTAMERICA_Merge.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/ACTAMERICA_Merge.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/TAD-Documentation.pdf",
-                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: TAD-Documentation.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA: TAD-Documentation.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_Merge/comp/TAD-Documentation.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ACTAMERICA/guides/ACTAMERICA_Merge_Fig1.png",
-                    "description": "ACT-America 2019 summer airborne campaign showing the flight paths for the two aircrafts and location of ground towers. Flights were concentrated on three study domains: northeast, south-central, and midwest regions of the United States.",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America 2019 summer airborne campaign showing the flight paths for the two aircrafts and location of ground towers. Flights were concentrated on three study domains: northeast, south-central, and midwest regions of the United States.",
+                    "downloadURL": "https://daac.ornl.gov/ACTAMERICA/guides/ACTAMERICA_Merge_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://actamerica.ornl.gov",
-                    "description": "ACT-America Campaign Site",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America Campaign Site",
+                    "downloadURL": "https://actamerica.ornl.gov",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1593/catalog.html",
-                    "description": "The THREDDS location for this Collection.",
                     "@type": "dcat:Distribution",
+                    "description": "The THREDDS location for this Collection.",
+                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1593/catalog.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "ACT-America 2019 summer airborne campaign showing the flight paths for the two aircrafts and location of ground towers. Flights were concentrated on three study domains: northeast, south-central, and midwest regions of the United States.",
+            "graphic-preview-file": "https://daac.ornl.gov/ACTAMERICA/guides/ACTAMERICA_Merge_Fig1.png",
+            "identifier": "C2367023363-ORNL_CLOUD",
+            "issued": "2020-07-20",
+            "keyword": [
+                "atmospheric chemistry",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1593",
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
             "spatial": "-106.49 27.23 -72.66 50.55",
+            "temporal": "2016-07-11T14:16:00Z/2019-07-27T20:10:00Z",
             "theme": [
                 "ACT-America",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ACT-America: L3 Merged In Situ Atmospheric Trace Gases and Flask Data, Eastern USA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CALIOP/CALIPSO/LID_L2_05KMALAY-STANDARD-V4-20",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2018-10-17. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/CALIOP/CALIPSO/LID_L2_05KMALAY-STANDARD-V4-20. https://asdc.larc.nasa.gov/project/CALIPSO.",
-            "issued": "2018-09-06",
-            "temporal": "2006-06-12T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-09-06",
-            "keyword": [
-                "lidar",
-                "aerosols",
-                "atmosphere",
-                "earth science",
-                "spectral/engineering"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DAVID WINKER",
                 "hasEmail": "mailto:david.m.winker@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1556717897-LARC_ASDC",
             "description": "CAL_LID_L2_05kmALay-Standard-V4-20 is the Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observation (CALIPSO) Lidar Level 2 5 km Aerosol Layer Data, Version 4-20 data product. This data product was collected using the Cloud-Aerosol LIdar with Orthogonal Polarization (CALIOP) instrument. Data collection for this product is ongoing.\nWithin the Lidar Aerosol Layer Product there are two general classes of data:- Column Properties (including position data and viewing geometry), and Layer Properties, the lidar layer products consist of a sequence of column descriptors, each one of which is associated with a variable number of layer descriptors. The column descriptors specify the temporal and geophysical location of the column of the atmosphere through which a given lidar pulse travels. Also included in the column descriptors are indicators of surface lighting conditions, information about the surface type, and the number of features (e.g., aerosol layers) identified within the column. \nCALIPSO was launched on April 28, 2006 and continues to collect data necessary to study the impact of clouds and aerosols on the Earth's radiation budget and climate . It flies in the international A-Train constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments, CALIOP, Imaging Infrared Radiometer (IIR), and Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES.",
-            "title": "CALIPSO Lidar Level 2 5 km Aerosol Layer Data, V4-20",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCALIOP%2FCALIPSO%2FLID_L2_05KMALAY-STANDARD-V4-20",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCALIOP%2FCALIPSO%2FLID_L2_05KMALAY-STANDARD-V4-20",
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
-                    "downloadURL": "https://doi.org/10.5067/CALIOP/CALIPSO/LID_L2_05KMALAY-STANDARD-V4-20",
-                    "description": "DOI data set landing page for CAL_LID_L2_05kmALay-Standard-V4-20_V4-20",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CAL_LID_L2_05kmALay-Standard-V4-20_V4-20",
+                    "downloadURL": "https://doi.org/10.5067/CALIOP/CALIPSO/LID_L2_05KMALAY-STANDARD-V4-20",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1556717897-LARC_ASDC",
-                    "description": "Earthdata Search for CAL_LID_L2_05kmALay-Standard-V4-20_V4-20 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CAL_LID_L2_05kmALay-Standard-V4-20_V4-20 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1556717897-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CALIPSO/LID_L2_05kmALay-Standard-V4-20/contents.html",
-                    "description": "OPeNDAP data access for CAL_LID_L2_05kmALay-Standard-V4-20_V4-20",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CAL_LID_L2_05kmALay-Standard-V4-20_V4-20",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CALIPSO/LID_L2_05kmALay-Standard-V4-20/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/qs/cal_lid_l2_all_v4-20.php",
-                    "description": "Data Quality Summary for the CALIPSO Version 4.20 Lidar Level 2 Data Products",
                     "@type": "dcat:Distribution",
+                    "description": "Data Quality Summary for the CALIPSO Version 4.20 Lidar Level 2 Data Products",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/qs/cal_lid_l2_all_v4-20.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/products/CALIPSO_DPC_Rev4x50.pdf",
-                    "description": "CALIPSO - Data Management System - Data Products Catalog - Release 4.50",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO - Data Management System - Data Products Catalog - Release 4.50",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/products/CALIPSO_DPC_Rev4x50.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's production history"
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
```

