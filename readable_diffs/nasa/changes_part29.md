# Change History for nasa.json (Part 29)

### Changes from 31606f9 to dd2190f (Part 18/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
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
+            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-01T21:36:45.000 to 2016-01-02T00:17:10.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1305-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1305-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1305-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-01T21:36:45.000 to 2016-01-02T00:17:10.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1305 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1305 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-PLS-5-SUMM-IONMOM-96SEC-V1.0",
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
+            "description": "THIS DATA SET CONTAINS ESTIMATES OF THE ION MOMENT DENSITY IN THE PLS VOLTAGE RANGE (10-5950 EV/Q) AT SATURN DURING THE VOYAGER 1 ENCOUNTER.  RIGID COROTATION IS ASSUMED, WHICH LEADS TO AN UNDERESTIMATE OF THE DENSITY IN SOME REGIONS, AS DOES THE USE OF AN ACCEPTANCE AREA RELEVANT FOR A COLD BEAM FOR PLASMA WHICH IS TRANSONIC IN SOME REGIONS.  DENSITIES MAY BE UNDERESTIMATED BY A FACTOR OF 2-3 IN THE INNER MAGNETOSPHERE, SO THIS DATA SET SHOULD BE USED PRIMARILY FOR STUDIES USING VARIATIONS IN PLASMA DENSITY.  THE FIT DENSITIES GIVE A BETTER ESTIMATE OF THE ABSOLUTE DENSITY.  THIS IS THE DATA SHOWN AND DESCRIBED IN DETAIL IN LAZARUS AND MCNUTT (1983).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-pls-5-summ-ionmom-96sec-v1.0_58si-brct",
+            "issued": "2021-05-21",
+            "keyword": [
+                "saturn",
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-PLS-5-SUMM-IONMOM-96SEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-pls-5-summ-ionmom-96sec-v1.0_58si-brct",
-            "description": "THIS DATA SET CONTAINS ESTIMATES OF THE ION MOMENT DENSITY IN THE PLS VOLTAGE RANGE (10-5950 EV/Q) AT SATURN DURING THE VOYAGER 1 ENCOUNTER.  RIGID COROTATION IS ASSUMED, WHICH LEADS TO AN UNDERESTIMATE OF THE DENSITY IN SOME REGIONS, AS DOES THE USE OF AN ACCEPTANCE AREA RELEVANT FOR A COLD BEAM FOR PLASMA WHICH IS TRANSONIC IN SOME REGIONS.  DENSITIES MAY BE UNDERESTIMATED BY A FACTOR OF 2-3 IN THE INNER MAGNETOSPHERE, SO THIS DATA SET SHOULD BE USED PRIMARILY FOR STUDIES USING VARIATIONS IN PLASMA DENSITY.  THE FIT DENSITIES GIVE A BETTER ESTIMATE OF THE ABSOLUTE DENSITY.  THIS IS THE DATA SHOWN AND DESCRIBED IN DETAIL IN LAZARUS AND MCNUTT (1983).",
-            "title": "VOYAGER 1 SATURN PLASMA DERIVED ION\n                                      MOMENTS 96 SEC",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VOYAGER 1 SATURN PLASMA DERIVED ION\n                                      MOMENTS 96 SEC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1936",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Apel, E.C., E.C. Asher, A.J. Hills, and R.S. Hornbrook. 2021. ATom: Volatile Organic Compounds (VOCs) from the TOGA instrument, Version 2. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1936",
-            "issued": "2021-11-29",
-            "temporal": "2016-07-29T00:00:00Z/2018-05-21T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "air quality",
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
-            "identifier": "C2677099477-ORNL_CLOUD",
             "description": "This dataset provides concentrations of volatile organic compounds (VOCs) measured by the Trace Organic Gas Analyzer (TOGA) during the four ATom campaigns. These data are relevant to the impact of human-produced air pollution on greenhouse gases and on chemically reactive gases in the atmosphere. Specific data were obtained for radical precursors, tracers of anthropogenic and biogenic activities, tracers of urban and biomass combustion emissions, products of oxidative processing, precursors to aerosol formation, and compounds important for aerosol modification and transformation. TOGA measures a wide range of VOCs with high sensitivity (ppt or lower), frequency (2-minutes), accuracy (often 15% or better), and precision (<3%).",
-            "graphic-preview-description": "Measurements of atmospheric acetone concentration from samples collected by the Trace Organic Gas Analyzer (TOGA) during ATom-3 flights in 2017.",
-            "title": "ATom: Volatile Organic Compounds (VOCs) from the TOGA instrument, Version 2",
-            "graphic-preview-file": "https://daac.ornl.gov/ATOM/guides/ATom_TOGA_Instrument_Data_V2_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1936",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1936",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/atom/ATom_TOGA_Instrument_Data_V2/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/atom/ATom_TOGA_Instrument_Data_V2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_TOGA_Instrument_Data_V2.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_TOGA_Instrument_Data_V2.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1936",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1936",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_TOGA_Instrument_Data_V2/comp/ATom_TOGA_Instrument_Data_V2.pdf",
-                    "description": "ATom: Volatile Organic Compounds (VOCs) from the TOGA instrument, Version 2: ATom_TOGA_Instrument_Data_V2.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ATom: Volatile Organic Compounds (VOCs) from the TOGA instrument, Version 2: ATom_TOGA_Instrument_Data_V2.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_TOGA_Instrument_Data_V2/comp/ATom_TOGA_Instrument_Data_V2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_TOGA_Instrument_Data_V2_Fig1.png",
-                    "description": "Measurements of atmospheric acetone concentration from samples collected by the Trace Organic Gas Analyzer (TOGA) during ATom-3 flights in 2017.",
                     "@type": "dcat:Distribution",
+                    "description": "Measurements of atmospheric acetone concentration from samples collected by the Trace Organic Gas Analyzer (TOGA) during ATom-3 flights in 2017.",
+                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_TOGA_Instrument_Data_V2_Fig1.png",
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
+            "graphic-preview-description": "Measurements of atmospheric acetone concentration from samples collected by the Trace Organic Gas Analyzer (TOGA) during ATom-3 flights in 2017.",
+            "graphic-preview-file": "https://daac.ornl.gov/ATOM/guides/ATom_TOGA_Instrument_Data_V2_Fig1.png",
+            "identifier": "C2677099477-ORNL_CLOUD",
+            "issued": "2021-11-29",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "air quality",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1936",
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
+            "temporal": "2016-07-29T00:00:00Z/2018-05-21T23:59:59Z",
             "theme": [
                 "ATom",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ATom: Volatile Organic Compounds (VOCs) from the TOGA instrument, Version 2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1928",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Stell, E., D.L. Warner, J. Jian, B.P. Bond-Lamberty, and R. Vargas. 2021. Global Gridded 1-km Soil and Soil Heterotrophic Respiration Derived from SRDB v5. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1928",
-            "issued": "2021-12-08",
-            "temporal": "1961-01-01T00:00:00Z/2016-06-01T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "soils",
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
-            "identifier": "C2345796019-ORNL_CLOUD",
             "description": "This dataset provides global gridded estimates of annual soil respiration (Rs) and soil heterotrophic respiration (Rh) and associated uncertainties at 1 km resolution. Mean soil respiration was estimated using a quantile regression forest model utilizing data from the global Soil Respiration Database Version 5 (SRDB-V5) and covariates of mean annual temperature, seasonal precipitation, and vegetative cover. The SRDB holds results of field studies of soil respiration from around the globe. A total of 4,115 records from 1,036 studies were selected from SRDB-V5. SRDB-V5 features more soil respiration data published in Russian and Chinese scientific literature for better global spatio-temporal coverage and improved global climate-space representation. These soil respiration records were combined with global meteorological, land cover, and topographic data and then evaluated with variable selection using random forests. The standard deviation and coefficient of variation of Rs are included and were also derived from the same model. Global heterotrophic respiration was calculated from Rs estimates. The data are produced in part from SRDB-V5 inputs that cover the period 1961-2016.",
-            "graphic-preview-description": "Mean global soil respiration derived from global Soil Respiration Database Version 5 (SRDB-V5). Units are g C m-2 y-1. Source: soil_Rs_mean.tif",
-            "title": "Global Gridded 1-km Soil and Soil Heterotrophic Respiration Derived from SRDB v5",
-            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/SoilResp_HeterotrophicResp_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1928",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1928",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/cms/SoilResp_HeterotrophicResp/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/cms/SoilResp_HeterotrophicResp/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/SoilResp_HeterotrophicResp.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/SoilResp_HeterotrophicResp.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1928",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1928",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/SoilResp_HeterotrophicResp/comp/SoilResp_HeterotrophicResp.pdf",
-                    "description": "Global Gridded 1-km Soil and Soil Heterotrophic Respiration Derived from SRDB v5: SoilResp_HeterotrophicResp.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Global Gridded 1-km Soil and Soil Heterotrophic Respiration Derived from SRDB v5: SoilResp_HeterotrophicResp.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/SoilResp_HeterotrophicResp/comp/SoilResp_HeterotrophicResp.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/SoilResp_HeterotrophicResp_Fig1.jpg",
-                    "description": "Mean global soil respiration derived from global Soil Respiration Database Version 5 (SRDB-V5). Units are g C m-2 y-1. Source: soil_Rs_mean.tif",
                     "@type": "dcat:Distribution",
+                    "description": "Mean global soil respiration derived from global Soil Respiration Database Version 5 (SRDB-V5). Units are g C m-2 y-1. Source: soil_Rs_mean.tif",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/SoilResp_HeterotrophicResp_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Mean global soil respiration derived from global Soil Respiration Database Version 5 (SRDB-V5). Units are g C m-2 y-1. Source: soil_Rs_mean.tif",
+            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/SoilResp_HeterotrophicResp_Fig1.jpg",
+            "identifier": "C2345796019-ORNL_CLOUD",
+            "issued": "2021-12-08",
+            "keyword": [
+                "soils",
+                "earth science",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1928",
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
+            "temporal": "1961-01-01T00:00:00Z/2016-06-01T23:59:59Z",
             "theme": [
                 "CMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Gridded 1-km Soil and Soil Heterotrophic Respiration Derived from SRDB v5"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ATLAS/ATL15.003",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "ATLAS/ICESat-2 L3B Gridded Antarctic and Arctic Land Ice Height Change V003. Version 003. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/ATLAS/ATL15.003.",
-            "issued": "2019-03-29",
-            "temporal": "2019-03-29T00:00:00Z/2023-10-30T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-16",
-            "keyword": [
-                "cryosphere",
-                "glaciers/ice sheets",
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
-            "identifier": "C2776464171-NSIDC_ECS",
             "description": "ATL14 and ATL15 bring the time-varying height estimates provided in ATLAS/ICESat-2 L3B Annual Land Ice Height (ATL11) into a gridded format. ATL14 is a high-resolution (100 m) digital elevation model (DEM) that provides spatially continuous gridded data of ice sheet surface height. The data can be used to initialize ice sheet models, as boundary conditions for atmospheric models, or to help with the reduction of other satellite data such as optical imagery or synthetic aperture radar (SAR). \n\nATL15 provides coarser resolution (1 km, 10 km, 20 km, and 40 km) height-change maps at 3-month intervals, allowing for visualization of height-change patterns and calculation of integrated regional volume change.",
-            "title": "ATLAS/ICESat-2 L3B Gridded Antarctic and Arctic Land Ice Height Change V003",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FATLAS%2FATL15.003",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FATLAS%2FATL15.003",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ATLAS/ATL15.003/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ATLAS/ATL15.003/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ATL15+V003",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ATL15+V003",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/ATL15/versions/3/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/ATL15/versions/3/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL15.003",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL15.003",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL15.003",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL15.003",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2776464171-NSIDC_ECS",
+            "issued": "2019-03-29",
+            "keyword": [
+                "cryosphere",
+                "glaciers/ice sheets",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ATLAS/ATL15.003",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-04-16",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 59.0 180.0 90.0",
+            "temporal": "2019-03-29T00:00:00Z/2023-10-30T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ATLAS/ICESat-2 L3B Gridded Antarctic and Arctic Land Ice Height Change V003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/58ug-7fgc",
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
+                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_iir_l1_prov_v1_11_table",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000188",
             "issued": "2018-06-25",
-            "temporal": "2008-08-20/2011-10-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "atmospheric science",
                 "satellite",
@@ -178058,77 +178069,42 @@
                 "climate",
                 "aerosol"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John M. Kusterer",
-                "hasEmail": "mailto:john.m.kusterer@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/58ug-7fgc",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:004"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000188",
-            "description": "Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) was launched on April 28, 2006 to study the impact of clouds and aerosols on the Earth\u2019s radiation budget and climate. It flies in formation with five other satellites in the international \u201cA-Train\u201d (PDF) constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments, the Cloud-Aerosol LIdar with Orthogonal Polarization (CALIOP), the Imaging Infrared Radiometer (IIR), and the Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES. These data consist 5 km aerosol layer data.",
-            "title": "CALIPSO Imaging Infrared Radiometer (IIR) L1B Radiance Data V1-11",
-            "programCode": [
-                "026:004"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_iir_l1_prov_v1_11_table",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
+            "temporal": "2008-08-20/2011-10-31",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CALIPSO Imaging Infrared Radiometer (IIR) L1B Radiance Data V1-11"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/1XO0PZEZOR1H",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Junjie Liu and Kevin Bowman. 2020-09-28. CMSFluxLandPrior. Version 3. Carbon Monitoring System Carbon Flux Land Prior L4 V3. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/1XO0PZEZOR1H. https://disc.gsfc.nasa.gov/datacollection/CMSFluxLandPrior_3.html. Digital Science Data.",
-            "issued": "2017-04-26",
-            "temporal": "2010-01-01T00:00:00Z/2022-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-08-18",
-            "keyword": [
-                "atmosphere",
-                "atmospheric chemistry",
-                "ocean chemistry",
-                "earth science",
-                "oceans"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kevin Bowman",
                 "hasEmail": "mailto:kevin.w.bowman@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C3005726562-GES_DISC",
-            "description": "This dataset provides the Prior for the Land Carbon Flux.\n\nThe NASA Carbon Monitoring System (CMS) is designed to make significant contributions in characterizing, quantifying, understanding, and predicting the evolution of global carbon sources and sinks through improved monitoring of carbon stocks and fluxes. The System will use the full range of NASA satellite observations and modeling/analysis capabilities to establish the accuracy, quantitative uncertainties, and utility of products for supporting national and international policy, regulatory, and management activities. CMS will maintain a global emphasis while providing finer scale regional information, utilizing space-based and surface-based data and will rapidly initiate generation and distribution of products both for user evaluation and to inform near-term policy development and planning.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "CMSFluxLandPrior",
             "creator": "Junjie Liu and Kevin Bowman",
-            "title": "Carbon Monitoring System Carbon Flux Land Prior L4 V3 (CMSFluxLandPrior)",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/CMS/CMSFluxLandPrior_3.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "This dataset provides the Prior for the Land Carbon Flux.\n\nThe NASA Carbon Monitoring System (CMS) is designed to make significant contributions in characterizing, quantifying, understanding, and predicting the evolution of global carbon sources and sinks through improved monitoring of carbon stocks and fluxes. The System will use the full range of NASA satellite observations and modeling/analysis capabilities to establish the accuracy, quantitative uncertainties, and utility of products for supporting national and international policy, regulatory, and management activities. CMS will maintain a global emphasis while providing finer scale regional information, utilizing space-based and surface-based data and will rapidly initiate generation and distribution of products both for user evaluation and to inform near-term policy development and planning.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F1XO0PZEZOR1H",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F1XO0PZEZOR1H",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -178138,125 +178114,131 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CMSFluxLandPrior_3.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CMSFluxLandPrior_3.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/CMSFluxLandPrior.3/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/CMSFluxLandPrior.3/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/opendap/CMS/CMSFluxLandPrior.3/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/opendap/CMS/CMSFluxLandPrior.3/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/CMS/README.CMS_Flux_V3.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/CMS/README.CMS_Flux_V3.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=CMSFluxLandPrior",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=CMSFluxLandPrior",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/CMS/CMSFluxLandPrior_3.png",
+            "identifier": "C3005726562-GES_DISC",
+            "issued": "2017-04-26",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "ocean chemistry",
+                "earth science",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/1XO0PZEZOR1H",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-08-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "CMSFluxLandPrior",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2010-01-01T00:00:00Z/2022-12-31T23:59:59.999Z",
             "theme": [
                 "CMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Carbon Monitoring System Carbon Flux Land Prior L4 V3 (CMSFluxLandPrior)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1011-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-09-04T03:06:50.000 to 2015-09-04T09:51:05.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1011-v1.0_58yz-wkcm",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1011-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1011-v1.0_58yz-wkcm",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-09-04T03:06:50.000 to 2015-09-04T09:51:05.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1011 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1011 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/58zb-szgw",
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
-            "identifier": "NASA-0000038__38",
+            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
             "description": "Planetary nomenclature, like terrestrial nomenclature, is used to uniquely identify a feature on the surface of a planet or satellite so that the feature can be easily located, described, and discussed. This gazetteer contains detailed information about all names of topographic and albedo features on planets and satellites (and some planetary ring and ring-gap systems) that the International Astronomical Union (IAU) has named and approved from its founding in 1919 through the present time.",
-            "title": "Gazetteer of Planetary Nomenclature",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -178264,266 +178246,295 @@
                     "mediaType": "application/vnd.google-earth.kmz"
                 }
             ],
-            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
-            "accrualPeriodicity": "irregular"
+            "identifier": "NASA-0000038__38",
+            "issued": "2018-06-25",
+            "keyword": [
+                "nen",
+                "geography",
+                "wise",
+                "space science"
+            ],
+            "landingPage": "https://data.nasa.gov/d/58zb-szgw",
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
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/CYGNU-L3S32",
             "citation": "CYGNSS. 2024-06-28. CYGNSS Level 3 Soil Moisture. Version 3.2. CYGNSS Level 3 Soil Moisture Version 3.2. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/CYGNU-L3S32. https://cygnss.engin.umich.edu/. CYGNSS, PO.DAAC, 2020-10-16, UCAR-CU CYGNSS Level 3 Soil Moisture Version 1.0, https://cygnss.engin.umich.edu/.",
-            "issued": "2020-10-16",
-            "temporal": "2017-03-18T00:00:00Z/2024-06-24T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-10-16",
-            "references": [
-                "https://doi.org/10.3390/rs12101558"
-            ],
-            "keyword": [
-                "soils",
-                "land surface",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
             },
-            "identifier": "C2927902887-POCLOUD",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "description": "The CYGNSS Level 3 Soil Moisture V3.2 dataset is produced by CYGNSS investigators at the University Corporation for Atmospheric Research (UCAR) and the University Colorado at Boulder (CU),  it provides volumetric water content estimates for soils between 0-5 cm depth at a 6-hour discretization for most of the subtropics. and is derived from version 3.2 of the CYGNSS L1 SDR dataset (https://doi.org/10.5067/CYGNS-L1X32). \r\nCYGNSS was launched on 15 December 2016, it is a NASA Earth System Science Pathfinder Mission that was launched with the purpose of collecting the first frequent space\u2010based measurements of surface wind speeds in the inner core of tropical cyclones. Originally made up of a constellation of eight micro-satellites, the observatories provide nearly gap-free Earth coverage using an orbital inclination of approximately 35\u00b0 from the equator, with a mean (i.e., average) revisit time of seven hours and a median revisit time of three hours.\r\n<br><br>\r\nThe soil moisture algorithm uses collocated soil moisture retrievals from SMAP to calibrate CYGNSS observations from the same day. For a given location, a linear relationship between the SMAP soil moisture and CYGNSS reflectivity is determined and used to transform the CYGNSS observations into soil moisture. The data are archived in daily files in netCDF-4 format. Two soil moisture variables report the volumetric water content in units of cm3/cm3. The variable SM_subdaily includes up to four soil moisture estimates per day. Another variable SM_daily provides a daily average. The time series covers the period from March 2017 to present.",
-            "release-place": "PO.DAAC",
-            "series-name": "CYGNSS Level 3 Soil Moisture",
             "creator": "CYGNSS",
-            "title": "CYGNSS Level 3 Soil Moisture Version 3.2",
-            "graphic-preview-description": "Thumbnail",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_L3_SOIL_MOISTURE_V1.1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The CYGNSS Level 3 Soil Moisture V3.2 dataset is produced by CYGNSS investigators at the University Corporation for Atmospheric Research (UCAR) and the University Colorado at Boulder (CU),  it provides volumetric water content estimates for soils between 0-5 cm depth at a 6-hour discretization for most of the subtropics. and is derived from version 3.2 of the CYGNSS L1 SDR dataset (https://doi.org/10.5067/CYGNS-L1X32). \r\nCYGNSS was launched on 15 December 2016, it is a NASA Earth System Science Pathfinder Mission that was launched with the purpose of collecting the first frequent space\u2010based measurements of surface wind speeds in the inner core of tropical cyclones. Originally made up of a constellation of eight micro-satellites, the observatories provide nearly gap-free Earth coverage using an orbital inclination of approximately 35\u00b0 from the equator, with a mean (i.e., average) revisit time of seven hours and a median revisit time of three hours.\r\n<br><br>\r\nThe soil moisture algorithm uses collocated soil moisture retrievals from SMAP to calibrate CYGNSS observations from the same day. For a given location, a linear relationship between the SMAP soil moisture and CYGNSS reflectivity is determined and used to transform the CYGNSS observations into soil moisture. The data are archived in daily files in netCDF-4 format. Two soil moisture variables report the volumetric water content in units of cm3/cm3. The variable SM_subdaily includes up to four soil moisture estimates per day. Another variable SM_daily provides a daily average. The time series covers the period from March 2017 to present.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCYGNU-L3S32",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCYGNU-L3S32",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "downloadURL": "https://doi.org/10.3390/rs12101558",
-                    "description": "Chew, C.C., E.E. Small. 'Description of the UCAR/CU Soil Moisture Product'. Remote Sens. 2020, 12, 1558. https://doi.org/10.3390/rs12101558",
                     "@type": "dcat:Distribution",
+                    "description": "Chew, C.C., E.E. Small. 'Description of the UCAR/CU Soil Moisture Product'. Remote Sens. 2020, 12, 1558. https://doi.org/10.3390/rs12101558",
+                    "downloadURL": "https://doi.org/10.3390/rs12101558",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/2018GL077905",
-                    "description": "Chew, C. C., & Small, E. E. (2018). Soil Moisture Sensing Using Spaceborne GNSSReflections: Comparison of CYGNSS Reflectivity to SMAP Soil Moisture.Geophysical Research Letters, 45(9), 4049-4057.https://doi.org/10.1029/2018GL077905",
                     "@type": "dcat:Distribution",
+                    "description": "Chew, C. C., & Small, E. E. (2018). Soil Moisture Sensing Using Spaceborne GNSSReflections: Comparison of CYGNSS Reflectivity to SMAP Soil Moisture.Geophysical Research Letters, 45(9), 4049-4057.https://doi.org/10.1029/2018GL077905",
+                    "downloadURL": "https://doi.org/10.1029/2018GL077905",
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
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_L3_SOIL_MOISTURE_V1.1.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_L3_SOIL_MOISTURE_V1.1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L3/soil_moisture/docs/ucar_cu_sm_handbook.pdf",
-                    "description": "User Guide for the UCAR/CU CYGNSS Soil Moisture Product",
                     "@type": "dcat:Distribution",
+                    "description": "User Guide for the UCAR/CU CYGNSS Soil Moisture Product",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L3/soil_moisture/docs/ucar_cu_sm_handbook.pdf",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2927902887-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2927902887-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2927902887-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2927902887-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
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
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "description": "Quality Flags (.nc)",
                     "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L3/soil_moisture/docs/ucar_cu_cygnss_sm_v1_static_flags.nc",
-                    "mediaType": "application/x-netcdf",
-                    "description": "Quality Flags (.nc)"
+                    "mediaType": "application/x-netcdf"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L3/docs/148-0414-1_Level_3_Soil_Moisture_netCDF_Data_Dictionary.xlsx",
-                    "description": "Soil Moisture netCDF Data Dictionary",
                     "@type": "dcat:Distribution",
+                    "description": "Soil Moisture netCDF Data Dictionary",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L3/docs/148-0414-1_Level_3_Soil_Moisture_netCDF_Data_Dictionary.xlsx",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.github.io/tutorials/",
-                    "description": "PO.DAAC Cookbook",
                     "@type": "dcat:Distribution",
+                    "description": "PO.DAAC Cookbook",
+                    "downloadURL": "https://podaac.github.io/tutorials/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data recipes"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_L3_SOIL_MOISTURE_V1.1.jpg",
+            "identifier": "C2927902887-POCLOUD",
+            "issued": "2020-10-16",
+            "keyword": [
+                "soils",
+                "land surface",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/CYGNU-L3S32",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-10-16",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.3390/rs12101558"
+            ],
+            "release-place": "PO.DAAC",
+            "series-name": "CYGNSS Level 3 Soil Moisture",
             "spatial": "-135.0 -38.0 164.0 38.0",
+            "temporal": "2017-03-18T00:00:00Z/2024-06-24T00:00:00Z",
             "theme": [
                 "CYGNSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CYGNSS Level 3 Soil Moisture Version 3.2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=JNO-J-MWR-2-EDR-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The Juno MWR EDR data sets will ultimately include all uncalibrated MWR science data records for the entire Juno mission.  The set in this volume will contain only those data obtained during the orbital phase of the Juno mission, when this phase of the mission is completed. These data comprise the raw data that address the primary objectives of the Juno  mission. They consist of data obtained at the full MWR data rate during a five-hour period around each perijove pass, and data obtained at all other times for the purpose of instrument calibration and perform- ance monitoring. This volume consists of reformatted and uncalibrated  data records. The reformatting operation reassembles received instrument data packets into one-hour-long records of time-ordered data correspond- ing to 100-ms observations made by the MWR instrument. This data set is intended to preserve the full content of the uncalibrated instrument  packets and is to be used only as a last resort.  The level 3 MWR  archived data are designed to be complete and more easily used.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.jno-j-mwr-2-edr-v1.0_592s-2jvu",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "juno",
                 "sky",
                 "jupiter"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=JNO-J-MWR-2-EDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.jno-j-mwr-2-edr-v1.0_592s-2jvu",
-            "description": "The Juno MWR EDR data sets will ultimately include all uncalibrated MWR science data records for the entire Juno mission.  The set in this volume will contain only those data obtained during the orbital phase of the Juno mission, when this phase of the mission is completed. These data comprise the raw data that address the primary objectives of the Juno  mission. They consist of data obtained at the full MWR data rate during a five-hour period around each perijove pass, and data obtained at all other times for the purpose of instrument calibration and perform- ance monitoring. This volume consists of reformatted and uncalibrated  data records. The reformatting operation reassembles received instrument data packets into one-hour-long records of time-ordered data correspond- ing to 100-ms observations made by the MWR instrument. This data set is intended to preserve the full content of the uncalibrated instrument  packets and is to be used only as a last resort.  The level 3 MWR  archived data are designed to be complete and more easily used.",
-            "title": "JUNO JUPITER MWR 2 EXPERIMENT DATA RECORDS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "JUNO JUPITER MWR 2 EXPERIMENT DATA RECORDS V1.0"
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
+                    "downloadURL": "http://fermi.gsfc.nasa.gov/ssc/data/access/lat/1yr_catalog/gll_psc_v02.reg",
+                    "mediaType": "text/plain"
+                }
+            ],
+            "identifier": "NASA-0000221__5",
             "issued": "2018-06-25",
-            "temporal": "2008-08-01/2009-07-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "gro",
                 "cgro",
@@ -178541,62 +178552,34 @@
                 "fermi",
                 "balloon"
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
-            "identifier": "NASA-0000221__5",
-            "description": "The Fermi Gamma-ray Space Telescope (Fermi) Large Area Telescope (LAT) is a successor to EGRET, with greatly improved sensitivity, resolution, and energy range. This web page presents the first full catalog of LAT sources, based on the first eleven months of survey data. For a full explanation about the catalog and its construction see the LAT 1-year Catalog Paper.",
-            "title": "LAT 1-year Point Source Catalog",
-            "programCode": [
-                "026:014"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://fermi.gsfc.nasa.gov/ssc/data/access/lat/1yr_catalog/gll_psc_v02.reg",
-                    "mediaType": "text/plain"
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
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1000000020-CDDIS.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GGL/CDDIS.",
-            "issued": "2003-01-24",
-            "temporal": "1990-03-31T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2012-06-14",
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
-            "identifier": "C1000000020-CDDIS",
             "description": "Station position and velocity solutions (weekly and cumulative) in Software INdependent EXchange (SINEX) format derived from analysis of Doppler Orbitography by Radiopositioning Integrated on Satellite (DORIS) data. The solutions include daily values of Earth Orientation Parameters (EOPs). These products are the generated by analysis centers in support of the International DORIS Service (IDS). Time series of station coordinate solutions in Station Coordinate Difference (STCD) are also generated by the IDS analysis centers. Weekly solutions represent the IDS contribution to the International Terrestrial Reference Frame (ITRF) determination.",
-            "title": "CDDIS_DORIS_products_positions",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -178605,24 +178588,52 @@
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1000000020-CDDIS",
+            "issued": "2003-01-24",
+            "keyword": [
+                "nasa"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1000000020-CDDIS.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2012-06-14",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GGL/CDDIS"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1990-03-31T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "IDS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CDDIS_DORIS_products_positions"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/docs/datasets/aerothermodynamics/EAST/index.html",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brett Cruden",
+                "hasEmail": "mailto:brett.a.cruden@nasa.gov"
+            },
+            "description": "The Ames Electric Arc Shock Tube (EAST) Facility is the only shock tube in the U.S. capable of simulating shock-heated gas environments at the very high enthalpies encountered by atmospheric entry vehicles. The facility generates conditions for measurements of spectrally resolved radiance and kinetics of shock-heated gases from the vacuum ultraviolet through mid-infrared. The EAST program provides ground-based hyperthermal and hypervelocity environments in support of the nation\u2019s research and development activities in thermal protection materials, aerothermodynamics, vehicle structures, and hypersonic propulsion and flight.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.nasa.gov/docs/datasets/aerothermodynamics/EAST/index.html",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "https://data.nasa.gov/api/views/5949-2pyk",
             "issued": "2018-07-31",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
             "keyword": [
                 "arc",
                 "thermophysics",
@@ -178637,273 +178648,264 @@
                 "electric",
                 "electric arc shock tube"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brett Cruden",
-                "hasEmail": "mailto:brett.a.cruden@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/docs/datasets/aerothermodynamics/EAST/index.html",
+            "modified": "2023-01-31",
+            "programCode": [
+                "026:009"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.nasa.gov"
             },
-            "identifier": "https://data.nasa.gov/api/views/5949-2pyk",
-            "description": "The Ames Electric Arc Shock Tube (EAST) Facility is the only shock tube in the U.S. capable of simulating shock-heated gas environments at the very high enthalpies encountered by atmospheric entry vehicles. The facility generates conditions for measurements of spectrally resolved radiance and kinetics of shock-heated gases from the vacuum ultraviolet through mid-infrared. The EAST program provides ground-based hyperthermal and hypervelocity environments in support of the nation\u2019s research and development activities in thermal protection materials, aerothermodynamics, vehicle structures, and hypersonic propulsion and flight.",
-            "title": "Electric Arc Shock Tube (EAST)",
-            "programCode": [
-                "026:009"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.nasa.gov/docs/datasets/aerothermodynamics/EAST/index.html",
-                    "mediaType": "text/html"
-                }
-            ],
             "theme": [
                 "Aerospace"
-            ]
+            ],
+            "title": "Electric Arc Shock Tube (EAST)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0048",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2000-04-07. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/FIRE/0048.",
-            "issued": "2000-03-17",
-            "temporal": "1992-06-12T00:00:00Z/1992-06-28T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-06",
-            "keyword": [
-                "earth science",
-                "altitude",
-                "atmosphere",
-                "atmospheric winds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DR. ALLEN WHITE",
                 "hasEmail": "mailto:awhite@etl.noaa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1000001032-LARC_ASDC",
             "description": "The First ISCCP Regional Experiments have been designed to improve data products and cloud/radiation parameterizations used in general circulation models (GCMs). Specifically, the goals of FIRE are (1) to improve the basic understanding of the interaction of physical processes in determining life cycles of cirrus and marine stratocumulus systems and the radiative properties of these clouds during their life cycles and (2) to investigate the interrelationships between the ISCCP data, GCM parameterizations, and higher space and time resolution cloud data. To-date, four intensive field-observation periods were planned and executed: a cirrus IFO (October 13 - November 2, 1986); a marine stratocumulus IFO off the southwestern coast of California (June 29 - July 20, 1987); a second cirrus IFO in southeastern Kansas (November 13 - December 7, 1991); and a second marine stratocumulus IFO in the eastern North Atlantic Ocean (June 1 - June 28, 1992). Each mission combined coordinated satellite, airborne, and surface observations with modeling studies to investigate the cloud properties and physical processes of the cloud systems.",
-            "title": "First ISCCP Regional Experiment (FIRE) Atlantic Stratocumulus Transition Experiment (ASTEX) PSU Malcolm Baldridge Wind Profiler Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0048",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0048",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001032-LARC_ASDC",
-                    "description": "Earthdata Search for FIRE_AX_PSU_WND_MAL_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FIRE_AX_PSU_WND_MAL_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001032-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fax_psu_wndmal_read.c",
-                    "description": "Code to read the FIRE ASTEX wind profiles on Malcolm Baldrige (WND_MAL) Data Set - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "Code to read the FIRE ASTEX wind profiles on Malcolm Baldrige (WND_MAL) Data Set - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fax_psu_wndmal_read.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "application/postscript",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ax_psu_wnd_mal_part2.ps",
-                    "description": "FIRE ASTEX Readme - Direct File Download (.ps)",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE ASTEX Readme - Direct File Download (.ps)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ax_psu_wnd_mal_part2.ps",
+                    "mediaType": "application/postscript",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0048",
-                    "description": "DOI data set landing page for FIRE_AX_PSU_WND_MAL_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIRE_AX_PSU_WND_MAL_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0048",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_AX_PSU_WND_MAL/",
-                    "description": "ASDC Direct Data Download for FIRE_AX_PSU_WND_MAL_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIRE_AX_PSU_WND_MAL_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_AX_PSU_WND_MAL/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_AX_PSU_WND_MAL/contents.html",
-                    "description": "OPeNDAP data access for FIRE_AX_PSU_WND_MAL_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for FIRE_AX_PSU_WND_MAL_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_AX_PSU_WND_MAL/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1000001032-LARC_ASDC",
+            "issued": "2000-03-17",
+            "keyword": [
+                "earth science",
+                "altitude",
+                "atmosphere",
+                "atmospheric winds"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0048",
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
+            "temporal": "1992-06-12T00:00:00Z/1992-06-28T23:59:59.999Z",
             "theme": [
                 "FIRE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "First ISCCP Regional Experiment (FIRE) Atlantic Stratocumulus Transition Experiment (ASTEX) PSU Malcolm Baldridge Wind Profiler Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67P-M07-STR-REFL-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units (normalized and thus without unit), acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-09-02T10:00:00.000 to 2014-09-23T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67p-m07-str-refl-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67P-M07-STR-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67p-m07-str-refl-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units (normalized and thus without unit), acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-09-02T10:00:00.000 to 2014-09-23T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP007 RDR-STR-REFL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP007 RDR-STR-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-LECP-4-SUMM-SECTOR-15MIN-V1.0",
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
+            "description": "This data set consists of resampled data from the Low Energy Charged Particle (LECP) experiment on Voyager 1 while the spacecraft was in the vicinity of Saturn. This instrument measures the intensities of in-situ charged particles (>26 keV electrons and >30 keV ions) with various levels of discrimination based on energy, mass species, and angular arrival direction. A subset of almost 100 LECP channels are included with this data set. The LECP data are globally calibrated to the extent possible (see below) and they are time averaged to about 15 minute time intervals with the exact beginning and ending times for those intervals matching the LECP instrumental cycle periods (the angular scanning periods).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-lecp-4-summ-sector-15min-v1.0_599m-m5z2",
+            "issued": "2021-05-21",
+            "keyword": [
+                "saturn",
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-LECP-4-SUMM-SECTOR-15MIN-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-lecp-4-summ-sector-15min-v1.0_599m-m5z2",
-            "description": "This data set consists of resampled data from the Low Energy Charged Particle (LECP) experiment on Voyager 1 while the spacecraft was in the vicinity of Saturn. This instrument measures the intensities of in-situ charged particles (>26 keV electrons and >30 keV ions) with various levels of discrimination based on energy, mass species, and angular arrival direction. A subset of almost 100 LECP channels are included with this data set. The LECP data are globally calibrated to the extent possible (see below) and they are time averaged to about 15 minute time intervals with the exact beginning and ending times for those intervals matching the LECP instrumental cycle periods (the angular scanning periods).",
-            "title": "VG1 SAT LECP CALIBRATED RESAMPLED\n                                      SECTORED 15MIN V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG1 SAT LECP CALIBRATED RESAMPLED\n                                      SECTORED 15MIN V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-LORRI-2-PLUTO-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Raw data taken by the New Horizons                Long Range Reconnaissance Imager                                       instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 3.0 of this data set.                    This data set contains LORRI observations taken during the               the Approach (Jan-Jul, 2015), Encounter, Departure, and                  Transition mission sub-phases, including flyby observations              taken on 14 July, 2015, and departure and calibration data               through late October, 2016. Departure observations include               a ring search of the Pluto system and 1994 JR1 observations.             This data set completes the Pluto mission phase deliveries for           LORRI.                                                                   This is version 3.0 of this dataset. Changes since version 2.0 include   the addition of data downlinked between the end of January, 2016 and the end of October, 2016, completing the delivery of all data covering the   Pluto Encounter and subsequent Calibration Campaign. It includes multi-  map observations from the Approach phase, observations of the moons, hi- res, full-frame observations from Pluto Encounter and Departure, sliver  maps, and ring search observations.  There may be some overlap between   prior datasets and this dataset, due to only partial, windowed, or lossy data in prior datasets.  Observations at closest approach to Pluto are   marked with _CA in the Request ID. This dataset also includes functional tests from the Calibration Campaign, including a regular observation of  NGC3532. Finally it includes the first set of distant KBO observations.  Also, updates were made to the calibration files, documentation, and     catalog files.                                                           There were minor changes to the level 2 LORRI calibration process, as    well as to the LORRI calibration constants for the final Pluto P3 PDS    delivery.                                                                The process change involves gap removal during calibration.  Files       with gaps come in many flavors, depending on where the gap lies within   the image. This update recognizes some additional possiblities, mainly   that the gap might be close to the bottom or top of the image (and       therefore the previous algorithm would fail because it filled the gap    with median pixel info from both above and below the gap). The new       algorithm will take the info from one side of the gap exclusively,       when appropriate.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-lorri-2-pluto-v3.0_59dj-bxep",
             "issued": "2018-09-05",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "kerberos",
                 "styx",
@@ -178914,544 +178916,520 @@
                 "new horizons",
                 "calibration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-LORRI-2-PLUTO-V3.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-lorri-2-pluto-v3.0_59dj-bxep",
-            "description": "This data set contains Raw data taken by the New Horizons                Long Range Reconnaissance Imager                                       instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 3.0 of this data set.                    This data set contains LORRI observations taken during the               the Approach (Jan-Jul, 2015), Encounter, Departure, and                  Transition mission sub-phases, including flyby observations              taken on 14 July, 2015, and departure and calibration data               through late October, 2016. Departure observations include               a ring search of the Pluto system and 1994 JR1 observations.             This data set completes the Pluto mission phase deliveries for           LORRI.                                                                   This is version 3.0 of this dataset. Changes since version 2.0 include   the addition of data downlinked between the end of January, 2016 and the end of October, 2016, completing the delivery of all data covering the   Pluto Encounter and subsequent Calibration Campaign. It includes multi-  map observations from the Approach phase, observations of the moons, hi- res, full-frame observations from Pluto Encounter and Departure, sliver  maps, and ring search observations.  There may be some overlap between   prior datasets and this dataset, due to only partial, windowed, or lossy data in prior datasets.  Observations at closest approach to Pluto are   marked with _CA in the Request ID. This dataset also includes functional tests from the Calibration Campaign, including a regular observation of  NGC3532. Finally it includes the first set of distant KBO observations.  Also, updates were made to the calibration files, documentation, and     catalog files.                                                           There were minor changes to the level 2 LORRI calibration process, as    well as to the LORRI calibration constants for the final Pluto P3 PDS    delivery.                                                                The process change involves gap removal during calibration.  Files       with gaps come in many flavors, depending on where the gap lies within   the image. This update recognizes some additional possiblities, mainly   that the gap might be close to the bottom or top of the image (and       therefore the previous algorithm would fail because it filled the gap    with median pixel info from both above and below the gap). The new       algorithm will take the info from one side of the gap exclusively,       when appropriate.",
-            "title": "NEW HORIZONS                            \n      LORRI PLUTO ENCOUNTER                                                   \n      RAW V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS                            \n      LORRI PLUTO ENCOUNTER                                                   \n      RAW V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2102",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hook, S.J., J.S. Myers, K.J. Thome, M. Fitzgerald, A.B. Kahle,  Airborne Sensor Facility NASA Ames Research Center, and J.M. Stock. 2022. MASTER: Airborne Science, Baja Mexico-Nevada, April-May, 1999. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2102",
-            "issued": "2023-07-09",
-            "temporal": "1999-04-23T19:58:15Z/1999-05-05T19:34:39Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-13",
-            "keyword": [
-                "earth science",
-                "visible wavelengths",
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
-            "identifier": "C2731778271-ORNL_CLOUD",
             "description": "This dataset includes Level 1B (L1B) data products from the MODIS/ASTER Airborne Simulator (MASTER) instrument. The spectral data were collected during 7 flights aboard a DOE B-200 aircraft over Baja California, Mexico, and Nevada, U.S., on 1999-04-23 to 1999-05-05. Data products include L1B georeferenced multispectral imagery of calibrated radiance in 50 bands covering wavelengths of 0.460 to 12.879 micrometers at approximately 20-meter spatial resolution. The L1B file format is HDF-4. In addition, the dataset includes flight paths, spectral band information, instrument configuration, ancillary notes, and summary information for each flight, and browse images derived from each L1B data file.",
-            "graphic-preview-description": "Single-band images and a RGB composite image from flight track 12 acquired on 30 April 1999 over Tres Virgenes volcano complex in Baja California Sur, Mexico. Source: MASTERL1B_9900303_12_19990430_1825_1827_V01.jpg",
-            "title": "MASTER: Airborne Science, Baja Mexico-Nevada, April-May, 1999",
-            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_Baja_Mexico_1999_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2102",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2102",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/master/MASTER_Baja_Mexico_1999/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/master/MASTER_Baja_Mexico_1999/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_Baja_Mexico_1999.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_Baja_Mexico_1999.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2102",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2102",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_Baja_Mexico_1999/comp/MASTER_Baja_Mexico_1999.pdf",
-                    "description": "MASTER: Airborne Science, Baja Mexico-Nevada, April-May, 1999: MASTER_Baja_Mexico_1999.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "MASTER: Airborne Science, Baja Mexico-Nevada, April-May, 1999: MASTER_Baja_Mexico_1999.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_Baja_Mexico_1999/comp/MASTER_Baja_Mexico_1999.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_Baja_Mexico_1999_Fig1.jpg",
-                    "description": "Single-band images and a RGB composite image from flight track 12 acquired on 30 April 1999 over Tres Virgenes volcano complex in Baja California Sur, Mexico. Source: MASTERL1B_9900303_12_19990430_1825_1827_V01.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Single-band images and a RGB composite image from flight track 12 acquired on 30 April 1999 over Tres Virgenes volcano complex in Baja California Sur, Mexico. Source: MASTERL1B_9900303_12_19990430_1825_1827_V01.jpg",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_Baja_Mexico_1999_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Single-band images and a RGB composite image from flight track 12 acquired on 30 April 1999 over Tres Virgenes volcano complex in Baja California Sur, Mexico. Source: MASTERL1B_9900303_12_19990430_1825_1827_V01.jpg",
+            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_Baja_Mexico_1999_Fig1.jpg",
+            "identifier": "C2731778271-ORNL_CLOUD",
+            "issued": "2023-07-09",
+            "keyword": [
+                "earth science",
+                "visible wavelengths",
+                "infrared wavelengths",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2102",
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
             "spatial": "-114.91 27.23 -112.27 36.48",
+            "temporal": "1999-04-23T19:58:15Z/1999-05-05T19:34:39Z",
             "theme": [
                 "MASTER",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MASTER: Airborne Science, Baja Mexico-Nevada, April-May, 1999"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQR50-3S3CS",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA Aquarius project. 2017-12-07. Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Seasonal Data. Version 5.0. Aquarius Sea Surface Salinity Products. Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC OBPG. https://doi.org/10.5067/AQR50-3S3CS. http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius. NASA Aquarius project, NASA/GSFC OBPG, 2017-12-07, Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Seasonal Data V5.0, http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius.",
-            "issued": "2017-10-21",
-            "temporal": "2011-08-25T01:55:23Z/2015-06-07T12:45:21Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-07",
-            "keyword": [
-                "salinity/density",
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
-            "identifier": "C2491756368-POCLOUD",
-            "description": "Aquarius Level 3 sea surface salinity (SSS) standard mapped image data contains gridded 1 degree spatial resolution SSS averaged over daily, 7 day, monthly, and seasonal time scales.\nThis particular data set is the Seasonal sea surface salinity product for version 5.0 of the Aquarius data set, which is the official end of mission public data release from the AQUARIUS/SAC-D mission. The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
-            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA",
-            "series-name": "Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Seasonal Data",
-            "graphic-preview-description": "Thumbnail",
             "creator": "NASA Aquarius project",
-            "title": "Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Seasonal Data V5.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS_SMI_3MONTH_V5.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Aquarius Level 3 sea surface salinity (SSS) standard mapped image data contains gridded 1 degree spatial resolution SSS averaged over daily, 7 day, monthly, and seasonal time scales.\nThis particular data set is the Seasonal sea surface salinity product for version 5.0 of the Aquarius data set, which is the official end of mission public data release from the AQUARIUS/SAC-D mission. The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3S3CS",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3S3CS",
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
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS_SMI_3MONTH_V5.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS_SMI_3MONTH_V5.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491756368-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491756368-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491756368-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491756368-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS_SMI_3MONTH_V5.jpg",
+            "identifier": "C2491756368-POCLOUD",
+            "issued": "2017-10-21",
+            "keyword": [
+                "salinity/density",
+                "oceans",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQR50-3S3CS",
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
+            "series-name": "Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Seasonal Data",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T01:55:23Z/2015-06-07T12:45:21Z",
             "theme": [
                 "AQUARIUS SAC-D",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Seasonal Data V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0984-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-08-25T03:05:20.000 to 2015-08-25T09:55:46.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0984-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0984-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0984-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-08-25T03:05:20.000 to 2015-08-25T09:55:46.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0984 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0984 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/SORTIE/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/SORTIE/DATA001.",
-            "issued": "2007-03-02",
-            "temporal": "2007-03-02T18:23:00Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean temperature",
-                "salinity/density",
-                "earth science",
-                "ocean chemistry",
-                "ocean optics",
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
-            "identifier": "C1633360665-OB_DAAC",
             "description": "Measurements made under the SORTIE (Spectral Ocean Radiance Transfer Investigation and Experiment) program between 2007 and 2009.",
-            "title": "Spectral Ocean Radiance Transfer Investigation and Experiment (SORTIE) program",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FSORTIE%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FSORTIE%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/SORTIE/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/SORTIE/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360665-OB_DAAC",
+            "issued": "2007-03-02",
+            "keyword": [
+                "ocean temperature",
+                "salinity/density",
+                "earth science",
+                "ocean chemistry",
+                "ocean optics",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/SORTIE/DATA001",
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
+            "temporal": "2007-03-02T18:23:00Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Spectral Ocean Radiance Transfer Investigation and Experiment (SORTIE) program"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-PRL-67PCHURYUMOV-M04B-V1.0",
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
+            "description": "This data set contains calibrated images acquired by the OSIRIS Narrow Angle\nCamera during the prelanding phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-06-18 to 2014-07-02.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-prl-67pchuryumov-m04b-v1.0_59q5-svps",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-PRL-67PCHURYUMOV-M04B-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-prl-67pchuryumov-m04b-v1.0_59q5-svps",
-            "description": "This data set contains calibrated images acquired by the OSIRIS Narrow Angle\nCamera during the prelanding phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-06-18 to 2014-07-02.",
-            "title": "ROSETTA-ORBITER COMET PRELANDING OSINAC 3 RDR MTP 004B V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMET PRELANDING OSINAC 3 RDR MTP 004B V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2020-10-10",
-            "temporal": "2020-10-10T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "topo",
-                "international",
-                "coords",
-                "station",
-                "space",
-                "coordinates",
-                "location",
-                "iss"
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
-            "identifier": "nasa-iss-data_2020-10-10",
+            "dataQuality": true,
             "description": "A boilerplate description provided by the TOPO team or Scott Goodwin",
-            "title": "ISS_COORDS_2020-10-10",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -179574,171 +179552,195 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2020-10-10",
+            "issued": "2020-10-10",
+            "keyword": [
+                "topo",
+                "international",
+                "coords",
+                "station",
+                "space",
+                "coordinates",
+                "location",
+                "iss"
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
+            "temporal": "2020-10-10T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2020-10-10"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-A-LEISA-3-KEM1-V1.0",
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
-                "vega",
-                "new horizons kuiper belt extended mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Calibrated data taken by the New Horizons Linear Etalon Imaging Spectral Array instrument during the KEM1 ENCOUNTER mission phase.  This is VERSION 1.0 of this data set. This data set contains LEISA observations taken for functional testing, and MU69 [ASTEROID 486958 (2014 MU69)] Encounter operations, including a test of a slow scan rate. This data set contains data acquired by the spacecraft between 08/14/2018 and 12/31/2018. It only includes data downlinked before 01/01/2019. Future datasets may include more data acquired by the spacecraft after 08/13/2018 but downlinked after 12/31/2018.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-a-leisa-3-kem1-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "vega",
+                "new horizons kuiper belt extended mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-A-LEISA-3-KEM1-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-a-leisa-3-kem1-v1.0",
-            "description": "This data set contains Calibrated data taken by the New Horizons Linear Etalon Imaging Spectral Array instrument during the KEM1 ENCOUNTER mission phase.  This is VERSION 1.0 of this data set. This data set contains LEISA observations taken for functional testing, and MU69 [ASTEROID 486958 (2014 MU69)] Encounter operations, including a test of a slow scan rate. This data set contains data acquired by the spacecraft between 08/14/2018 and 12/31/2018. It only includes data downlinked before 01/01/2019. Future datasets may include more data acquired by the spacecraft after 08/13/2018 but downlinked after 12/31/2018.",
-            "title": "NEW HORIZONS\n      LEISA KEM1\n      CALIBRATED V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS\n      LEISA KEM1\n      CALIBRATED V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ICESAT/GLAS/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "GLAS/ICESat L1A Global Altimetry Data (HDF5) V033. Version 033. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/ICESAT/GLAS/DATA101.",
-            "issued": "2003-02-20",
-            "temporal": "2003-02-20T00:00:00Z/2009-10-11T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2009-10-11",
-            "keyword": [
-                "earth science",
-                "infrared wavelengths",
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
-            "identifier": "C2153547306-NSIDC_CPRD",
             "description": "Level-1A altimetry data (GLAH01) include the transmitted and received waveform from the altimeter.  Each data granule has an associated browse product.",
-            "title": "GLAS/ICESat L1A Global Altimetry Data (HDF5) V033",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FICESAT%2FGLAS%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FICESAT%2FGLAS%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GLAH01+V033",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GLAH01+V033",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ICESAT/GLAS/DATA101",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/ICESAT/GLAS/DATA101",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ICESAT/GLAS/DATA101",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ICESAT/GLAS/DATA101",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2153547306-NSIDC_CPRD",
+            "issued": "2003-02-20",
+            "keyword": [
+                "earth science",
+                "infrared wavelengths",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/ICESAT/GLAS/DATA101",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2009-10-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -86.0 180.0 86.0",
+            "temporal": "2003-02-20T00:00:00Z/2009-10-11T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GLAS/ICESat L1A Global Altimetry Data (HDF5) V033"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=P11-J-SW-PA-4-SUMM-1HR-V1.0",
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
+            "description": "Pioneer 11 Plasma Analyzer (PA) data\nfrom the Jupiter close encounter period between 1974-11-03T00:00:00 and\n1975-01-01T00:00:00. The data include 1 hour averaged data.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.p11-j-sw-pa-4-summ-1hr-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "pioneer 11",
+                "jupiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=P11-J-SW-PA-4-SUMM-1HR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.p11-j-sw-pa-4-summ-1hr-v1.0",
-            "description": "Pioneer 11 Plasma Analyzer (PA) data\nfrom the Jupiter close encounter period between 1974-11-03T00:00:00 and\n1975-01-01T00:00:00. The data include 1 hour averaged data.",
-            "title": "P11 J SW PA 4 SUMM 1HR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "P11 J SW PA 4 SUMM 1HR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSINAC-2-CR4A-CRUISE4A-V1.4",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera during the CRUISE 4-1 mission phase",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osinac-2-cr4a-cruise4a-v1.4_59tv-vjbp",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "unknown",
@@ -179748,54 +179750,35 @@
                 "58 aql",
                 "16 cyg b"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSINAC-2-CR4A-CRUISE4A-V1.4",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osinac-2-cr4a-cruise4a-v1.4_59tv-vjbp",
-            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera during the CRUISE 4-1 mission phase",
-            "title": "ROSETTA-ORBITER CRUISE 4-1 OSINAC 2 EDR V1.4",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER CRUISE 4-1 OSINAC 2 EDR V1.4"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/59ui-jv2j",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2015-10-14",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "candida",
-                "albicans"
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
-            "identifier": "https://data.nasa.gov/api/views/59ui-jv2j",
             "description": "https://c3.nasa.gov/genelab/accession/GLDS-20/\r\n\r\nThis study presents the first global transcriptional profiling and phenotypic characterization of the major human opportunistic fungal pathogen, Candida albicans, grown in spaceflight conditions. Microarray analysis revealed that C. albicans subjected to short-term spaceflight culture differentially regulated 454 genes compared to synchronous ground controls, which represented 8.4% of the analyzed ORFs. Spaceflight-cultured C. albicans induced genes involved in cell aggregation (similar to flocculation), which was validated by microscopic and flow cytometry analysis. We also observed enhanced random budding of spaceflight-cultured cells as opposed to more normal bipolar budding patterns for ground samples, in accordance with the gene expression data. Furthermore, genes involved in antifungal agent and stress resistance were differentially regulated in spaceflight, including induction of ABC transporters and members of the major facilitator family, downregulation of ergosterol-encoding genes, and upregulation of genes involved in oxidative stress resistance. Finally, downregulation of genes involved in the actin cytoskeleton was observed. Interestingly, the transcriptional regulator Cap1 and over 30% of the Cap1 regulon was differentially expressed in spaceflight-cultured C. albicans. A potential role for Cap1 in the spaceflight response of C. albicans is suggested, as this regulator is involved in random budding, cell aggregation, actin cytoskeleton, and oxidative stress resistance; all related to observed spaceflight-associated changes of C. albicans. While culture of C. albicans in microgravity potentiates a global change in gene expression that could induce a virulence-related phenotype, no increased virulence in a murine intraperitoneal (i.p.) infection model was observed. This study represents an important basis for the assessment of the risk that commensal flora could play during spaceflight missions. Furthermore, since the low fluid-shear environment of microgravity is relevant to physical forces encountered by pathogens during the infection process, insights gained from this study could identify novel infectious disease mechanisms, with downstream benefits for the general public. Cells were grown for 24 hours on the space shuttle or as ground-based controls, preserved in RNALater, and stored at -80C. Four samples of each flight- and ground-based controls were harvested for microarray analysis. GAP is Group Activation Pack and each GAP contains 8 FPAs. The numbers represent the # assigned to the particular GAP and the number assigned to the specific FPA (1-8) within the indicated GAP. The same hardware is used for the flight samples and the ground samples.",
-            "title": "Candida albicans response to spaceflight (NASA STS-115) --- GSM1231690_Slide_43",
-            "programCode": [
-                "026:035"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -179803,597 +179786,616 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.nasa.gov/api/views/59ui-jv2j/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.nasa.gov/api/views/59ui-jv2j/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.nasa.gov/api/views/59ui-jv2j/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.nasa.gov/api/views/59ui-jv2j/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.nasa.gov/api/views/59ui-jv2j/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.nasa.gov/api/views/59ui-jv2j/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.nasa.gov/api/views/59ui-jv2j/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.nasa.gov/api/views/59ui-jv2j/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.nasa.gov/api/views/59ui-jv2j/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.nasa.gov/api/views/59ui-jv2j",
+            "issued": "2015-10-14",
+            "keyword": [
+                "candida",
+                "albicans"
+            ],
+            "landingPage": "https://data.nasa.gov/d/59ui-jv2j",
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
+            "title": "Candida albicans response to spaceflight (NASA STS-115) --- GSM1231690_Slide_43"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0506-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-12-25T12:29:05.000 to 2014-12-25T18:14:13.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0506-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0506-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0506-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-12-25T12:29:05.000 to 2014-12-25T18:14:13.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0506 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0506 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MOD15A2GFS.006",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MODIS Land Science Team. 2021-04-01. MODIS/Terra Gap-Filled, Smoothed LAI-FPAR 8-Day L4 Global 1km SIN Grid. Version 6. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/MODIS/MOD15A2GFS.006. https://doi.org/10.5067/MODIS/MOD15A2GFS.006.",
-            "issued": "2018-10-05",
-            "temporal": "2001-01-01T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-10-21",
-            "keyword": [
-                "biosphere",
-                "national geospatial data asset",
-                "earth science",
-                "vegetation",
-                "ngda"
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
-            "identifier": "C2055696477-LAADS",
-            "description": "The MODIS/Terra Gap-Filled, Smoothed Leaf Area Index (LAI) and Fraction of Photosynthetically Active Radiation (FPAR) 8-Day L4 Global 1km SIN Grid product with short-name MOD15A2GFS, is composited every 8 days at 1-kilometer resolution on a Sinusoidal grid. The LAI variable defines the number of equivalent layers of leaves relative to a unit of ground area, whereas FPAR measures the proportion of available radiation in the photosynthetically active wavelengths that are absorbed by a canopy. Both variables are used as satellite-derived parameters for calculating surface photosynthesis, evapotranspiration, and net primary production, which in turn are used to calculate terrestrial energy, carbon, water cycle processes, and biogeochemistry of vegetation.",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "MODIS Land Science Team",
-            "title": "MODIS/Terra Gap-Filled, Smoothed LAI-FPAR 8-Day L4 Global 1km SIN Grid",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MODIS/Terra Gap-Filled, Smoothed Leaf Area Index (LAI) and Fraction of Photosynthetically Active Radiation (FPAR) 8-Day L4 Global 1km SIN Grid product with short-name MOD15A2GFS, is composited every 8 days at 1-kilometer resolution on a Sinusoidal grid. The LAI variable defines the number of equivalent layers of leaves relative to a unit of ground area, whereas FPAR measures the proportion of available radiation in the photosynthetically active wavelengths that are absorbed by a canopy. Both variables are used as satellite-derived parameters for calculating surface photosynthesis, evapotranspiration, and net primary production, which in turn are used to calculate terrestrial energy, carbon, water cycle processes, and biogeochemistry of vegetation.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD15A2GFS.006",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD15A2GFS.006",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/1/MOD15A2GFS--6",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/1/MOD15A2GFS--6",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/6/MOD15A2GFS/",
-                    "description": "Direct access to MOD15A2GFS data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to MOD15A2GFS data set.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/6/MOD15A2GFS/",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/6/MOD15A2GFS/contents.html",
-                    "description": "Direct link to Collection's OPeNDAP directory",
                     "@type": "dcat:Distribution",
+                    "description": "Direct link to Collection's OPeNDAP directory",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/6/MOD15A2GFS/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2055696477-LAADS",
+            "issued": "2018-10-05",
+            "keyword": [
+                "biosphere",
+                "national geospatial data asset",
+                "earth science",
+                "vegetation",
+                "ngda"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MOD15A2GFS.006",
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
+            "title": "MODIS/Terra Gap-Filled, Smoothed LAI-FPAR 8-Day L4 Global 1km SIN Grid"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-U-PLS-5-RDR-IONFIT-48SEC-V1.0",
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
-                "uranus"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains the ion densities and temperatures along with formal 1 Sigma errors obtained from Voyager 2 PLS data (voltage range 10-5950 eV/Q) at Uranus by fitting the measured spectra with isotropic Maxwellian distributions. Up to three isotropic proton components (warm, hot and intermediate) were used to match the observations. The plasma was assumed to be rigidly corotating. Uncertainties in plasma parameters are a factor of 2 in the charging region from 19:39-21:58 on day 24, less than 20% elsewhere. A complete description of this data set is given in McNutt et al. (1987) and Selesnick and McNutt (1987).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-u-pls-5-rdr-ionfit-48sec-v1.0_5a4d-7z6t",
+            "issued": "2021-05-21",
+            "keyword": [
+                "voyager",
+                "uranus"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-U-PLS-5-RDR-IONFIT-48SEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-u-pls-5-rdr-ionfit-48sec-v1.0_5a4d-7z6t",
-            "description": "This data set contains the ion densities and temperatures along with formal 1 Sigma errors obtained from Voyager 2 PLS data (voltage range 10-5950 eV/Q) at Uranus by fitting the measured spectra with isotropic Maxwellian distributions. Up to three isotropic proton components (warm, hot and intermediate) were used to match the observations. The plasma was assumed to be rigidly corotating. Uncertainties in plasma parameters are a factor of 2 in the charging region from 19:39-21:58 on day 24, less than 20% elsewhere. A complete description of this data set is given in McNutt et al. (1987) and Selesnick and McNutt (1987).",
-            "title": "VG2 URA PLS DERIVED RDR ION FIT\n                                      48SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG2 URA PLS DERIVED RDR ION FIT\n                                      48SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-5-PRL-MTP004-V1.0",
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
+            "description": "This data set contains derived electron and proton flux energies in MeV from the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, which had the primary target of comet 67P/Churyumov-Gerasimenko. These are CODMAC Level 5 derived data, and measure the radiation in the spacecraft environment during the Medium Term Plan 4 period of the PRELANDING mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-5-prl-mtp004-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-5-PRL-MTP004-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-5-prl-mtp004-v1.0",
-            "description": "This data set contains derived electron and proton flux energies in MeV from the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, which had the primary target of comet 67P/Churyumov-Gerasimenko. These are CODMAC Level 5 derived data, and measure the radiation in the spacecraft environment during the Medium Term Plan 4 period of the PRELANDING mission phase.",
-            "title": "ROSETTA-ORBITER 67P SREM 5 PRELANDING\n    MTP004 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P SREM 5 PRELANDING\n    MTP004 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1302-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-31T07:49:50.000 to 2015-12-31T15:05:08.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1302-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1302-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1302-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-31T07:49:50.000 to 2015-12-31T15:05:08.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1302 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1302 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GIO-C-JPA-4-DDR-HALLEY-MERGE-V1.0",
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
-                "giotto"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains results from the Implanted Ion Sensor (IIS) 4DH mode and the Fast Ion Sensor SW and HAR modes of the Three- Dimensional Particle Analyzer (JPA) experiment on the GIOTTO spacecraft for the mission to comet Halley. The results of the Fast Ion Sensor (FIS - inbound) and IIS (outbound) have been merged with results from other Giotto instruments. In the first submitted table, magnetometer measurements are included.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.gio-c-jpa-4-ddr-halley-merge-v1.0_5a7b-mfx4",
+            "issued": "2021-05-21",
+            "keyword": [
+                "halley",
+                "giotto"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GIO-C-JPA-4-DDR-HALLEY-MERGE-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.gio-c-jpa-4-ddr-halley-merge-v1.0_5a7b-mfx4",
-            "description": "This dataset contains results from the Implanted Ion Sensor (IIS) 4DH mode and the Fast Ion Sensor SW and HAR modes of the Three- Dimensional Particle Analyzer (JPA) experiment on the GIOTTO spacecraft for the mission to comet Halley. The results of the Fast Ion Sensor (FIS - inbound) and IIS (outbound) have been merged with results from other Giotto instruments. In the first submitted table, magnetometer measurements are included.",
-            "title": "GIOTTO JOHNSTONE PARTICLE ANALYZER MERGED DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GIOTTO JOHNSTONE PARTICLE ANALYZER MERGED DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1053",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Aldrich, S.P., and R.T. Walker. 2011. LBA-ECO LC-24 Land Cover Classes from Landsat TM, Uruara, Para: 1986-1991. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1053",
-            "issued": "2023-10-06",
-            "temporal": "1986-01-01T00:00:00Z/1999-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-11",
-            "keyword": [
-                "land use/land cover",
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
-            "identifier": "C2779741137-ORNL_CLOUD",
             "description": "This data set provides course land cover classifications derived from Landsat TM images for 1986, 1988, and 1991 for the area surrounding the municipality of Uruara, Para, Brazil. Five land cover classes (Water, Clouds/Shadow, Forest, Not Forest, and Background) were derived (Aldrich et al. 2006). The Land Cover is in a compressed (*.zip) GeoTIFF file for each year.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO LC-24 Land Cover Classes from Landsat TM, Uruara, Para: 1986-1991",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1053_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1053",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1053",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC24_Land_Cover_Uruara_Para/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC24_Land_Cover_Uruara_Para/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC24_Land_Cover_Uruara_Para.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC24_Land_Cover_Uruara_Para.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1053",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1053",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC24_Land_Cover_Uruara_Para/comp/LC24_Land_Cover_Uruara_Para.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC24_Land_Cover_Uruara_Para/comp/LC24_Land_Cover_Uruara_Para.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1053_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1053_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1053",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1053",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1053_1_fit.png",
+            "identifier": "C2779741137-ORNL_CLOUD",
+            "issued": "2023-10-06",
+            "keyword": [
+                "land use/land cover",
+                "earth science",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1053",
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
             "spatial": "-55.6 -5.3 -51.7 -1.8",
+            "temporal": "1986-01-01T00:00:00Z/1999-12-31T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO LC-24 Land Cover Classes from Landsat TM, Uruara, Para: 1986-1991"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2263929265-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC.",
-            "issued": "2022-09-13",
-            "temporal": "2016-04-25T00:00:00Z/2024-04-22T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-13",
-            "keyword": [
-                "atmospheric radiation",
-                "atmosphere",
-                "oceans",
-                "ocean optics",
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
-            "identifier": "C2263929265-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "Sentinel-3A OLCI Level-3B Global Binned Earth-observation Reduced Resolution (ERR) Diffuse Attenuation Coefficient for Downwelling Irradiance (KD) - Near Real-time (NRT) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-3%20Binned/S3A-OLCI/",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-3%20Binned/S3A-OLCI/",
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
+            "identifier": "C2263929265-OB_DAAC",
+            "issued": "2022-09-13",
+            "keyword": [
+                "atmospheric radiation",
+                "atmosphere",
+                "oceans",
+                "ocean optics",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2263929265-OB_DAAC.html",
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
+            "title": "Sentinel-3A OLCI Level-3B Global Binned Earth-observation Reduced Resolution (ERR) Diffuse Attenuation Coefficient for Downwelling Irradiance (KD) - Near Real-time (NRT) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67P-M06-STRLIGHT-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-08-01T10:00:00.000 to 2014-09-02T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67p-m06-strlight-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "16 cyg b",
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67P-M06-STRLIGHT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67p-m06-strlight-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-08-01T10:00:00.000 to 2014-09-02T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP006 RDR-STRLIGHT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP006 RDR-STRLIGHT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/O8UCOA2D6ZE3",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "LVIS Classic L1B Geolocated Return Energy Waveforms V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/O8UCOA2D6ZE3.",
-            "issued": "2019-05-21",
-            "temporal": "2019-05-21T00:00:00Z/2023-11-13T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-05-31",
-            "keyword": [
-                "earth science",
-                "spectral/engineering",
-                "infrared wavelengths"
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
-            "identifier": "C1703031208-NSIDC_ECS",
             "description": "This data set contains Level-1B geolocated return energy waveforms collected by the NASA Land, Vegetation, and Ice Sensor (LVIS) Facility, an imaging lidar and camera sensor suite.",
-            "title": "LVIS Classic L1B Geolocated Return Energy Waveforms V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FO8UCOA2D6ZE3",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FO8UCOA2D6ZE3",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/LVISC1B.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/LVISC1B.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=LVISC1B+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=LVISC1B+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/LVISC1B/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/LVISC1B/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/O8UCOA2D6ZE3",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/O8UCOA2D6ZE3",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/O8UCOA2D6ZE3",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/O8UCOA2D6ZE3",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1703031208-NSIDC_ECS",
+            "issued": "2019-05-21",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "infrared wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/O8UCOA2D6ZE3",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-05-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-168.0 -3.0 -17.0 72.0",
+            "temporal": "2019-05-21T00:00:00Z/2023-11-13T00:00:00Z",
             "theme": [
                 "ABoVE",
                 "GEDI",
                 "MULTI_NASA",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LVIS Classic L1B Geolocated Return Energy Waveforms V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSINAC-4-CVP2-CHKOUT-STRLIGHT-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the COMMISSIONING 2 mission phase, covering the period  from 2004-09-06T00:00:00.000 to 2004-10-16T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. This version V1.0 is the first version of this dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osinac-4-cvp2-chkout-strlight-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "16 cyg b",
                 "venus",
@@ -180405,99 +180407,75 @@
                 "area 98",
                 "58 aql"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSINAC-4-CVP2-CHKOUT-STRLIGHT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osinac-4-cvp2-chkout-strlight-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the COMMISSIONING 2 mission phase, covering the period  from 2004-09-06T00:00:00.000 to 2004-10-16T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. This version V1.0 is the first version of this dataset.",
-            "title": "ROSETTA-ORBITER CHECKOUT OSINAC 4 CVP2 RDR-STRLIGHT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECKOUT OSINAC 4 CVP2 RDR-STRLIGHT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-MAG-4-RDR-S3COORDS-1.92SEC-V1.1",
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
-                "voyager"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-mag-4-rdr-s3coords-1.92sec-v1.1_5akq-fa65",
+            "issued": "2021-05-21",
+            "keyword": [
+                "jupiter",
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-MAG-4-RDR-S3COORDS-1.92SEC-V1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-mag-4-rdr-s3coords-1.92sec-v1.1_5akq-fa65",
-            "description": "not applicable",
-            "title": "VG1 JUP MAG RESAMPLED SYSTEM III (1965) COORDS 1.92SEC V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG1 JUP MAG RESAMPLED SYSTEM III (1965) COORDS 1.92SEC V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1282032628-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Tropical Rainfall Measuring Mission (TRMM). 2011-07-01. TRMM_3A26. TRMM Radar Rain Distributions L3 1 month 5 degree x 5 degree V7. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/TRMM_3A26_7.html.",
-            "issued": "2011-07-01",
-            "temporal": "1997-12-01T00:00:00Z/2015-04-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-04-20",
-            "keyword": [
-                "earth science",
-                "precipitation",
-                "atmosphere"
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
-            "identifier": "C1282032628-GES_DISC",
-            "description": "The new version of these data is in GPM-like format (consistent with the GPM Dual-frequency Radar data format), and can be found under the name GPM_3PR.\n\nThis dataset contains distributions of monthly surface rainfall. These data were derived from rain rate statistics and include the estimated values of the probability distribution function of the space-time rain rates at four levels (2 km, 4 km, 6 km, and path-averaged) and the mean, standard deviation, and probability of rain derived from these distributions. Three different rain rate estimates are used as input to the algorithm: (1) the standard Z-R (or 0th-order estimate having no attenuation correction); (2) the Hitschfield-Bordan (H-B); and (3) the rain rates taken from 2A25.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "TRMM_3A26",
             "creator": "Tropical Rainfall Measuring Mission (TRMM)",
-            "title": "TRMM Radar Rain Distributions L3 1 month 5 degree x 5 degree V7 (TRMM_3A26) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TRMM_3A26_7.png",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The new version of these data is in GPM-like format (consistent with the GPM Dual-frequency Radar data format), and can be found under the name GPM_3PR.\n\nThis dataset contains distributions of monthly surface rainfall. These data were derived from rain rate statistics and include the estimated values of the probability distribution function of the space-time rain rates at four levels (2 km, 4 km, 6 km, and path-averaged) and the mean, standard deviation, and probability of rain derived from these distributions. Three different rain rate estimates are used as input to the algorithm: (1) the standard Z-R (or 0th-order estimate having no attenuation correction); (2) the Hitschfield-Bordan (H-B); and (3) the rain rates taken from 2A25.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -180506,524 +180484,524 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRMM_3A26_7.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRMM_3A26_7.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L3/TRMM_3A26.7",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L3/TRMM_3A26.7",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/opendap/TRMM_L3/TRMM_3A26.7/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/opendap/TRMM_L3/TRMM_3A26.7/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/thredds/catalog/aggregation/TRMM_3A26.7/catalog.html",
-                    "description": "Access the data via the THREDDS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the THREDDS.",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/thredds/catalog/aggregation/TRMM_3A26.7/catalog.html",
+                    "mediaType": "text/html",
                     "title": "Use THREDDS DATA to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRMM_3A26",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRMM_3A26",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://trmm.gsfc.nasa.gov/",
-                    "description": "TRMM Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "TRMM Project Home Page",
+                    "downloadURL": "https://trmm.gsfc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://pps.gsfc.nasa.gov/Documents/filespec.TRMM.V7.pdf",
-                    "description": "File specification document.",
                     "@type": "dcat:Distribution",
+                    "description": "File specification document.",
+                    "downloadURL": "https://pps.gsfc.nasa.gov/Documents/filespec.TRMM.V7.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://pps.gsfc.nasa.gov/Documents/formatChangesV7.pdf",
-                    "description": "Comparison between TRMM versions 6 and 7.",
                     "@type": "dcat:Distribution",
+                    "description": "Comparison between TRMM versions 6 and 7.",
+                    "downloadURL": "https://pps.gsfc.nasa.gov/Documents/formatChangesV7.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.eorc.jaxa.jp/TRMM/documents/PR_algorithm_product_information/pr_manual/PR_Instruction_Manual_V7_L1.pdf",
-                    "description": "TRMM Precipitation Radar Instruction Manual (provided by JAXA)",
                     "@type": "dcat:Distribution",
+                    "description": "TRMM Precipitation Radar Instruction Manual (provided by JAXA)",
+                    "downloadURL": "http://www.eorc.jaxa.jp/TRMM/documents/PR_algorithm_product_information/pr_manual/PR_Instruction_Manual_V7_L1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L3/TRMM_3A26/doc/README.TRMM_V7.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L3/TRMM_3A26/doc/README.TRMM_V7.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TRMM_3A26_7.png",
+            "identifier": "C1282032628-GES_DISC",
+            "issued": "2011-07-01",
+            "keyword": [
+                "earth science",
+                "precipitation",
+                "atmosphere"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1282032628-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2016-04-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD",
+            "series-name": "TRMM_3A26",
             "spatial": "-180.0 -40.0 180.0 40.0",
+            "temporal": "1997-12-01T00:00:00Z/2015-04-01T23:59:59.999Z",
             "theme": [
                 "TRMM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TRMM Radar Rain Distributions L3 1 month 5 degree x 5 degree V7 (TRMM_3A26) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7265/N5BG2KW2",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Great Lakes Surface Ice Reports from U.S. Coast Guard, 1961 - 2004, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center. https://doi.org/10.7265/N5BG2KW2.",
-            "issued": "1961-11-10",
-            "temporal": "1961-11-10T00:00:00Z/2004-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2004-12-31",
-            "keyword": [
-                "earth science",
-                "cryosphere",
-                "snow/ice",
-                "atmosphere",
-                "atmospheric temperature"
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
-            "identifier": "C2205522291-NSIDCV0",
             "description": "Data consist of ice observations from U.S. Coast Guard vessels operating on the Great Lakes and from Coast Guard shore stations reported via teletype messages and ice logging forms. Observations include ice thickness and concentration, weather conditions, and ice breaking activity. Data from 1961/1962 through 1966/1967 have been processed to a standard format and sorted by year and stations, and are available via FTP as ASCII files, one for each of the five lakes.",
-            "title": "Great Lakes Surface Ice Reports from U.S. Coast Guard, 1961 - 2004, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN5BG2KW2",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN5BG2KW2",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/G00805_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/G00805_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5BG2KW2",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/N5BG2KW2",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5BG2KW2",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/N5BG2KW2",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2205522291-NSIDCV0",
+            "issued": "1961-11-10",
+            "keyword": [
+                "earth science",
+                "cryosphere",
+                "snow/ice",
+                "atmosphere",
+                "atmospheric temperature"
+            ],
+            "landingPage": "https://doi.org/10.7265/N5BG2KW2",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2004-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "-93.0 41.0 -76.0 49.0",
+            "temporal": "1961-11-10T00:00:00Z/2004-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Great Lakes Surface Ice Reports from U.S. Coast Guard, 1961 - 2004, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/BEST/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/BEST/DATA001.",
-            "issued": "2008-07-04",
-            "temporal": "2008-07-04T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "earth science",
-                "ocean optics",
-                "salinity/density",
-                "oceans",
-                "ocean chemistry",
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
-            "identifier": "C1633360145-OB_DAAC",
             "description": "The HLY0803 cruise of the USCG cutter Healy was an NSF funded cruise for the Bering Ecosystem Study (BEST) project that was focused on the impact of sea ice on the marine ecology of the region. In particular it focused on pathways of nutrients and organic matter that lead to the abundant upper trophic levels and valuable fisheries on the Bering Sea continental shelf. The cruise covered most of the eastern Bering Sea shelf from the Aleutian Islands to St. Lawrence Island with 177 unique stations that included CTD casts, bio-optics casts, MOCNESS tows, CALVet tows, bongo tows, multicore drops and sediment trap deployments.",
-            "title": "Bering Ecosystem STudy (BEST) project",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FBEST%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FBEST%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/BEST/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/BEST/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360145-OB_DAAC",
+            "issued": "2008-07-04",
+            "keyword": [
+                "earth science",
+                "ocean optics",
+                "salinity/density",
+                "oceans",
+                "ocean chemistry",
+                "ocean temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/BEST/DATA001",
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
+            "temporal": "2008-07-04T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Bering Ecosystem STudy (BEST) project"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-PLS-5-SUMM-ELE-BR-96SEC-V1.0",
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
-                "voyager"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-pls-5-summ-ele-br-96sec-v1.0_5aqs-fnnm",
+            "issued": "2018-06-26",
+            "keyword": [
+                "saturn",
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-PLS-5-SUMM-ELE-BR-96SEC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-pls-5-summ-ele-br-96sec-v1.0_5aqs-fnnm",
-            "description": "not applicable",
-            "title": "VOYAGER 2 SATURN PLASMA DERIVED ELECTRON BROWSE 96 SEC",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VOYAGER 2 SATURN PLASMA DERIVED ELECTRON BROWSE 96 SEC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ECG5M-OTS44",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.. 2021-04-19. ECCO Ocean Temperature and Salinity - Monthly Mean 0.5 Degree (Version 4 Release 4). Version V4r4. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/ECG5M-OTS44. ECCO; ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.; 2020; ECCO Ocean Temperature and Salinity - Monthly Mean 0.5 Degree (Version 4 Release 4); 10.5067/ECG5M-OTS44; https://podaac.jpl.nasa.gov/ECCO.",
-            "issued": "2021-01-01",
-            "temporal": "1992-01-01T00:00:00Z/2018-01-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-31",
-            "references": [
-                "https://doi.org/10.5281/zenodo.3765928"
-            ],
-            "keyword": [
-                "earth science services",
-                "salinity/density",
-                "earth science",
-                "models",
-                "ocean temperature",
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
-            "identifier": "C1990404795-POCLOUD",
-            "description": "This dataset contains monthly-averaged ocean potential temperature and salinity interpolated to a regular 0.5-degree grid from the ECCO Version 4 revision 4 (V4r4) ocean and sea-ice state estimate. Estimating the Circulation and Climate of the Ocean (ECCO) ocean and sea-ice state estimates are dynamically and kinematically-consistent reconstructions of the three-dimensional, time-evolving ocean, sea-ice, and surface atmospheric states. ECCO V4r4 is a free-running solution of the 1-degree global configuration of the MIT general circulation model (MITgcm) that has been fit to observations in a least-squares sense. Observational data constraints used in V4r4 include sea surface height (SSH) from satellite altimeters [ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jason-1,2,3, CryoSat-2, and SARAL/AltiKa]; sea surface temperature (SST) from satellite radiometers [AVHRR], sea surface salinity (SSS) from the Aquarius satellite radiometer/scatterometer, ocean bottom pressure (OBP) from the GRACE satellite gravimeter; sea ice concentration from satellite radiometers [SSM/I and SSMIS], and in-situ ocean temperature and salinity measured with conductivity-temperature-depth (CTD) sensors and expendable bathythermographs (XBTs) from several programs [e.g., WOCE, GO-SHIP, Argo, and others] and platforms [e.g.,research vessels, gliders, moorings, ice-tethered profilers, and instrumented pinnipeds]. V4r4 covers the period 1992-01-01T12:00:00 to 2018-01-01T00:00:00.",
-            "release-place": "PO.DAAC",
-            "graphic-preview-description": "Thumbnail image for Website",
             "creator": "ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.",
-            "title": "ECCO Ocean Temperature and Salinity - Monthly Mean 0.5 Degree (Version 4 Release 4)",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_TEMP_SALINITY_05DEG_MONTHLY_V4R4.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset contains monthly-averaged ocean potential temperature and salinity interpolated to a regular 0.5-degree grid from the ECCO Version 4 revision 4 (V4r4) ocean and sea-ice state estimate. Estimating the Circulation and Climate of the Ocean (ECCO) ocean and sea-ice state estimates are dynamically and kinematically-consistent reconstructions of the three-dimensional, time-evolving ocean, sea-ice, and surface atmospheric states. ECCO V4r4 is a free-running solution of the 1-degree global configuration of the MIT general circulation model (MITgcm) that has been fit to observations in a least-squares sense. Observational data constraints used in V4r4 include sea surface height (SSH) from satellite altimeters [ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jason-1,2,3, CryoSat-2, and SARAL/AltiKa]; sea surface temperature (SST) from satellite radiometers [AVHRR], sea surface salinity (SSS) from the Aquarius satellite radiometer/scatterometer, ocean bottom pressure (OBP) from the GRACE satellite gravimeter; sea ice concentration from satellite radiometers [SSM/I and SSMIS], and in-situ ocean temperature and salinity measured with conductivity-temperature-depth (CTD) sensors and expendable bathythermographs (XBTs) from several programs [e.g., WOCE, GO-SHIP, Argo, and others] and platforms [e.g.,research vessels, gliders, moorings, ice-tethered profilers, and instrumented pinnipeds]. V4r4 covers the period 1992-01-01T12:00:00 to 2018-01-01T00:00:00.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECG5M-OTS44",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECG5M-OTS44",
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_TEMP_SALINITY_05DEG_MONTHLY_V4R4.jpg",
-                    "description": "Thumbnail image for Website",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail image for Website",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_TEMP_SALINITY_05DEG_MONTHLY_V4R4.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ECG5M-OTS44",
-                    "description": "Access the data set landing page for the collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data set landing page for the collection.",
+                    "downloadURL": "https://doi.org/10.5067/ECG5M-OTS44",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1990404795-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1990404795-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1990404795-POCLOUD/temporal",
-                    "description": "Browse and download granules over HTTPS using the virtual directories service",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories service",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1990404795-POCLOUD/temporal",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 }
             ],
+            "graphic-preview-description": "Thumbnail image for Website",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_TEMP_SALINITY_05DEG_MONTHLY_V4R4.jpg",
+            "identifier": "C1990404795-POCLOUD",
+            "issued": "2021-01-01",
+            "keyword": [
+                "earth science services",
+                "salinity/density",
+                "earth science",
+                "models",
+                "ocean temperature",
+                "earth science reanalyses/assimilation models",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/ECG5M-OTS44",
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
+            "title": "ECCO Ocean Temperature and Salinity - Monthly Mean 0.5 Degree (Version 4 Release 4)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-RAT-2-EDR-OPS-V1.0",
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
+            "description": "This archive contains Mars Exploration Rover Operations (Ops) Rock\nAbrasion Tool (RAT) Experiment Data Record (EDR) products and\nancillary files.  The RAT Operations EDR products archived on this volume are the original products used during mission operations by the Mars\nExploration Rover project.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-rat-2-edr-ops-v1.0_5arv-kx8r",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-RAT-2-EDR-OPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-rat-2-edr-ops-v1.0_5arv-kx8r",
-            "description": "This archive contains Mars Exploration Rover Operations (Ops) Rock\nAbrasion Tool (RAT) Experiment Data Record (EDR) products and\nancillary files.  The RAT Operations EDR products archived on this volume are the original products used during mission operations by the Mars\nExploration Rover project.",
-            "title": "MER 1 MARS ROCK ABRASION TOOL EDR OPS\n                                      VERSION 1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MER 1 MARS ROCK ABRASION TOOL EDR OPS\n                                      VERSION 1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-SDC-2-JUPITER-V2.0",
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
-                "dust",
-                "new horizons"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Raw data taken by the New Horizons Student Dust Counter instrument during the Jupiter encounter mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-sdc-2-jupiter-v2.0_5ass-2cv6",
+            "issued": "2018-06-26",
+            "keyword": [
+                "dust",
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-SDC-2-JUPITER-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-sdc-2-jupiter-v2.0_5ass-2cv6",
-            "description": "This data set contains Raw data taken by the New Horizons Student Dust Counter instrument during the Jupiter encounter mission phase.",
-            "title": "NEW HORIZONS SDC JUPITER ENCOUNTER V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS SDC JUPITER ENCOUNTER V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1237114196-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "TOMS Science Team. 1996-07-25. TOMSEPL3dery. Version 008. TOMS Earth Probe UV-B Erythemal Local Noon Irradiance Daily L3  Global 1 deg x 1.25 deg Lat/Lon Grid V008. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/TOMSEPL3dery_008.html. Digital Science Data.",
-            "issued": "2004-04-30",
-            "temporal": "1996-07-22T00:00:00Z/2005-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2004-04-30",
-            "keyword": [
-                "atmosphere",
-                "earth science",
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
-            "identifier": "C1237114196-GES_DISC",
-            "description": "This Earth Probe (EP) Total Ozone Mapping Spectrometer (TOMS) version 8 daily global gridded data product contains UV-B erythemal local noon irradiance values. The data are mapped to a global grid of size 180 x 288 with a lat-long resolution of 1.00 x 1.25 degrees. These data are stored in an ASCII format.\n\nThe TOMS data were produced by the Laboratory for Atmospheres at NASA Goddard Space Flight Center (Code 614).",
-            "release-place": "Greenbelt, MD",
-            "series-name": "TOMSEPL3dery",
             "creator": "TOMS Science Team",
-            "title": "TOMS Earth Probe UV-B Erythemal Local Noon Irradiance Daily L3 Global 1 deg x 1.25 deg Lat/Lon Grid V008 (TOMSEPL3dery) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOMSEPL3dery_008.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "This Earth Probe (EP) Total Ozone Mapping Spectrometer (TOMS) version 8 daily global gridded data product contains UV-B erythemal local noon irradiance values. The data are mapped to a global grid of size 180 x 288 with a lat-long resolution of 1.00 x 1.25 degrees. These data are stored in an ASCII format.\n\nThe TOMS data were produced by the Laboratory for Atmospheres at NASA Goddard Space Flight Center (Code 614).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -181032,69 +181010,100 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TOMSEPL3dery_008.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TOMSEPL3dery_008.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/EarthProbe_TOMS_Level3/TOMSEPL3dery.008/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/EarthProbe_TOMS_Level3/TOMSEPL3dery.008/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TOMSEPL3dery_008",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TOMSEPL3dery_008",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOMSEPL3dery_008.png",
+            "identifier": "C1237114196-GES_DISC",
+            "issued": "2004-04-30",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1237114196-GES_DISC.html",
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
+            "series-name": "TOMSEPL3dery",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1996-07-22T00:00:00Z/2005-12-31T23:59:59.999Z",
             "theme": [
                 "TOMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TOMS Earth Probe UV-B Erythemal Local Noon Irradiance Daily L3 Global 1 deg x 1.25 deg Lat/Lon Grid V008 (TOMSEPL3dery) at GES DISC"
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
+            "description": "CIRS, HRD, INMS, ISS, MAG, MIMI, RADAR, RPWS, RSS, SPICE, UVIS, VIMS",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20140704.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-436",
+            "issued": "2018-06-25",
             "keyword": [
                 "rpws",
                 "vims",
@@ -181111,118 +181120,84 @@
                 "data",
                 "cirs"
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
-            "identifier": "NASA-436",
-            "description": "CIRS, HRD, INMS, ISS, MAG, MIMI, RADAR, RPWS, RSS, SPICE, UVIS, VIMS",
-            "title": "PDS Cassini Data Release 38",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20140704.shtml",
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
+            "title": "PDS Cassini Data Release 38"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/KARIN-2MEC1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SWOT. 2022-01-31. SWOT Level-2 Simulated SSH from MITgcm LLC4320 Science Quality Version 1.0. Version 1.0. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/KARIN-2MEC1.",
-            "issued": "2022-01-31",
-            "temporal": "2011-11-13T00:00:00Z/2012-11-12T00:50:15.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2012-11-12",
-            "references": [
-                "https://doi.org/10.1175/JTECH-D-15-0160.1"
-            ],
-            "keyword": [
-                "earth science",
-                "oceans",
-                "sea surface topography"
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
-            "identifier": "C2147947806-POCLOUD",
-            "description": "This dataset provides simulated sea surface height (SSH) in a format similar to the future SWOT Level 2 (L2) SSH data from KaRIn. The simulated data were generated by the \"ECCO LLC4320\" global ocean simulation. ECCO, which means \"Estimating the Circulation and Climate of the Ocean\", is a data assimilation and model (and the international consortium of scientists who maintains it) based on the MIT general circulation model (MITgcm) that assimilates and constrains observational data from numerous sources to estimate the ocean state. The model operates on the Lat-Lon-Cap (LLC) grid with a nominal horizontal resolution of 1/48-degrees (when approximated over the entire model domain, corresponding to ~2-km cell size at the equator). SSH data produced by ECCO LLC4320 were rendered from the native output format into the format prescribed in the SWOT L2 SSH PDD to aid ongoing data product development and to benefit future users of data produced during operational phases of the SWOT mission.",
-            "release-place": "PO.DAAC",
-            "graphic-preview-description": "Thumbnail",
             "creator": "SWOT",
-            "title": "SWOT Simulated Level-2 KaRIn SSH from MITgcm ECCO LLC4320 for Cal/Val Version 1",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_SIMULATED_L2_KARIN_SSH_ECCO_LLC4320_CALVAL_V1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset provides simulated sea surface height (SSH) in a format similar to the future SWOT Level 2 (L2) SSH data from KaRIn. The simulated data were generated by the \"ECCO LLC4320\" global ocean simulation. ECCO, which means \"Estimating the Circulation and Climate of the Ocean\", is a data assimilation and model (and the international consortium of scientists who maintains it) based on the MIT general circulation model (MITgcm) that assimilates and constrains observational data from numerous sources to estimate the ocean state. The model operates on the Lat-Lon-Cap (LLC) grid with a nominal horizontal resolution of 1/48-degrees (when approximated over the entire model domain, corresponding to ~2-km cell size at the equator). SSH data produced by ECCO LLC4320 were rendered from the native output format into the format prescribed in the SWOT L2 SSH PDD to aid ongoing data product development and to benefit future users of data produced during operational phases of the SWOT mission.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FKARIN-2MEC1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FKARIN-2MEC1",
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/SWOT",
-                    "description": "Mission and Instrument Overview",
                     "@type": "dcat:Distribution",
+                    "description": "Mission and Instrument Overview",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/SWOT",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "description": "Generic Data Readers",
                     "downloadURL": "https://github.com/podaac/data-readers",
-                    "mediaType": "text/html",
-                    "description": "Generic Data Readers"
+                    "mediaType": "text/html"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_SIMULATED_L2_KARIN_SSH_ECCO_LLC4320_CALVAL_V1.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_SIMULATED_L2_KARIN_SSH_ECCO_LLC4320_CALVAL_V1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2147947806-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2147947806-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2147947806-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2147947806-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
@@ -181233,28 +181208,67 @@
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_SIMULATED_L2_KARIN_SSH_ECCO_LLC4320_CALVAL_V1.jpg",
+            "identifier": "C2147947806-POCLOUD",
+            "issued": "2022-01-31",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "sea surface topography"
+            ],
+            "landingPage": "https://doi.org/10.5067/KARIN-2MEC1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2012-11-12",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.1175/JTECH-D-15-0160.1"
+            ],
+            "release-place": "PO.DAAC",
             "spatial": "-180.0 -77.6 180.0 77.6",
+            "temporal": "2011-11-13T00:00:00Z/2012-11-12T00:50:15.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SWOT Simulated Level-2 KaRIn SSH from MITgcm ECCO LLC4320 for Cal/Val Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/5azr-yp3p",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "We differentiated mouse bone marrow cells in the presence of recombinant macrophage colony stimulating (rM-CSF) factor for 14 days during the flight of space shuttle Space Transportation System (STS)-126. We tested the hypothesis that the receptor expression for M-CSF c-Fms was reduced. We used flow cytometry to assess molecules on cells that were preserved during flight to define the differentiation state of the developing bone marrow macrophages; including CD11b CD31 CD44 Ly6C Ly6G F4/80 Mac2 c-Fos as well as c-Fms. In addition RNA was preserved during the flight and was used to perform a gene microarray. We found that there were significant differences in the number of macrophages that developed in space compared to controls maintained on Earth. We found that there were significant changes in the distribution of cells that expressed CD11b CD31 F4/80 Mac2 Ly6C and c-Fos. However there were no changes in c-Fms expression and no consistent pattern of advanced or retarded differentiation during space flight. We also found a pattern of transcript levels that would be consistent with a relatively normal differentiation outcome but increased proliferation by the bone marrow macrophages that were assayed after 14 days of space flight. There also was a surprising pattern of space flight influence on genes of the coagulation pathway. These data confirm that a space flight can have an impact on the in vitro development of macrophages from mouse bone marrow cells.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-50",
+                    "mediaType": "text/html",
+                    "title": "Evaluation of in vitro macrophage differentiation during space flight"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-50_5azr-yp3p",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "sample collection",
                 "treatment protocol",
@@ -181271,611 +181285,575 @@
                 "rna extraction",
                 "spaceflight"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/5azr-yp3p",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-50_5azr-yp3p",
-            "description": "We differentiated mouse bone marrow cells in the presence of recombinant macrophage colony stimulating (rM-CSF) factor for 14 days during the flight of space shuttle Space Transportation System (STS)-126. We tested the hypothesis that the receptor expression for M-CSF c-Fms was reduced. We used flow cytometry to assess molecules on cells that were preserved during flight to define the differentiation state of the developing bone marrow macrophages; including CD11b CD31 CD44 Ly6C Ly6G F4/80 Mac2 c-Fos as well as c-Fms. In addition RNA was preserved during the flight and was used to perform a gene microarray. We found that there were significant differences in the number of macrophages that developed in space compared to controls maintained on Earth. We found that there were significant changes in the distribution of cells that expressed CD11b CD31 F4/80 Mac2 Ly6C and c-Fos. However there were no changes in c-Fms expression and no consistent pattern of advanced or retarded differentiation during space flight. We also found a pattern of transcript levels that would be consistent with a relatively normal differentiation outcome but increased proliferation by the bone marrow macrophages that were assayed after 14 days of space flight. There also was a surprising pattern of space flight influence on genes of the coagulation pathway. These data confirm that a space flight can have an impact on the in vitro development of macrophages from mouse bone marrow cells.",
-            "title": "Evaluation of in vitro macrophage differentiation during space flight",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-50",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Evaluation of in vitro macrophage differentiation during space flight"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Evaluation of in vitro macrophage differentiation during space flight"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/Aqua/AIRS/DATA303",
             "citation": "AIRS Science Team/Joao Teixeira. 2013-03-12. AIRS3STD. Version 006. AIRS/Aqua L3 Daily Standard Physical Retrieval (AIRS-only) 1 degree x 1 degree V006. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aqua/AIRS/DATA303. https://disc.gsfc.nasa.gov/datacollection/AIRS3STD_006.html. Digital Science Data.",
-            "issued": "2002-08-31",
-            "temporal": "2002-08-31T00:00:00Z/2025-01-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-17",
-            "references": [
-                "https://doi.org/10.1117/1.JRS.8.084994",
-                "https://doi.org/10.5194/acp-14-399-2014"
-            ],
-            "keyword": [
-                "altitude",
-                "atmospheric temperature",
-                "surface thermal properties",
-                "air quality",
-                "atmosphere",
-                "atmospheric radiation",
-                "clouds",
-                "earth science",
-                "land surface",
-                "atmospheric chemistry",
-                "atmospheric pressure",
-                "oceans",
-                "ocean temperature",
-                "atmospheric water vapor",
-                "surface radiative properties"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ED ESFANDIARI",
                 "hasEmail": "mailto:asghar.e.esfandiari@nasa.gov"
             },
+            "creator": "AIRS Science Team/Joao Teixeira",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1238517289-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The Atmospheric Infrared Sounder (AIRS) is a grating spectrometer (R = 1200) aboard the second Earth Observing System (EOS) polar-orbiting platform, EOS Aqua. In combination with the Advanced Microwave Sounding Unit (AMSU) and the Humidity Sounder for Brazil (HSB), AIRS constitutes an innovative atmospheric sounding group of visible, infrared, and microwave sensors. The AIRS Only Level 3 Daily Gridded Product contains standard retrieval means, standard deviations and input counts. Each file covers a temporal period of 24 hours for either the descending (equatorial crossing North to South @1:30 AM local time) or ascending (equatorial crossing South to North @1:30 PM local time) orbit. The data starts at the international dateline and progresses westward (as do the subsequent orbits of the satellite) so that neighboring gridded cells of data are no more than a swath of time apart (about 90 minutes). The two parts of a scan line crossing the dateline are included in separate L3 files, according to the date, so that data points in a grid box are always coincident in time. The edge of the AIRS Level 3 gridded cells is at the date line (the 180E/W longitude boundary). When plotted, this produces a map with 0 degrees longitude in the center of the image unless the bins are reordered. This method is preferred because the left (West) side of the image and the right (East) side of the image contain data farthest apart in time. The gridding scheme used by AIRS is the same as used by TOVS Pathfinder to create Level 3 products. The daily Level 3 products have gores between satellite paths where there is no coverage for that day. The geophysical parameters have been averaged and binned into 1 x 1 deg grid cells, from -180.0 to +180.0 deg longitude and from -90.0 to +90.0 deg latitude. For each grid map of 4-byte floating-point mean values there is a corresponding 4-byte floating-point map of standard deviation and a 2-byte integer grid map of counts. The counts map provides the user with the number of points per bin that were included in the mean and can be used to generate custom multi-day maps from the daily gridded products. The thermodynamic parameters are: Skin Temperature (land and sea surface), Air Temperature at the surface, Profiles of Air Temperature and Water Vapor, Tropopause Characteristics, Column Precipitable Water, Cloud Amount/Frequency, Cloud Height, Cloud Top Pressure, Cloud Top Temperature, Reflectance, Emissivity, Surface Pressure, Cloud Vertical Distribution. The trace gases parameters are: Total Amounts and Vertical Profiles of Carbon Monoxide, Methane, and Ozone. The actual names of the variables in the data files should be inferred from the Processing File Description document.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "AIRS3STD",
-            "creator": "AIRS Science Team/Joao Teixeira",
-            "graphic-preview-description": "Sample data of the \"AIRS/Aqua Level 3 daily standard physical retrieval product (AIRS only)\".",
-            "title": "AIRS/Aqua L3 Daily Standard Physical Retrieval (AIRS-only) 1 degree x 1 degree V006 (AIRS3STD) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRS3STD_006.jpeg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAqua%2FAIRS%2FDATA303",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAqua%2FAIRS%2FDATA303",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRS3STD_006.jpeg",
-                    "description": "Sample data of the \"AIRS/Aqua Level 3 daily standard physical retrieval product (AIRS only)\".",
                     "@type": "dcat:Distribution",
+                    "description": "Sample data of the \"AIRS/Aqua Level 3 daily standard physical retrieval product (AIRS only)\".",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRS3STD_006.jpeg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRS3STD_006.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRS3STD_006.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level3/AIRS3STD.006/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level3/AIRS3STD.006/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level3/AIRS3STD.006/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level3/AIRS3STD.006/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRS3STD+006",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRS3STD+006",
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
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/AIRS/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithms/V6_Released_Processing_Files_Description.pdf",
-                    "description": "AIRS Version 6 Processing Files Description Document.",
                     "@type": "dcat:Distribution",
+                    "description": "AIRS Version 6 Processing Files Description Document.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/AIRS/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithms/V6_Released_Processing_Files_Description.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample data of the \"AIRS/Aqua Level 3 daily standard physical retrieval product (AIRS only)\".",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRS3STD_006.jpeg",
+            "identifier": "C1238517289-GES_DISC",
+            "issued": "2002-08-31",
+            "keyword": [
+                "altitude",
+                "atmospheric temperature",
+                "surface thermal properties",
+                "air quality",
+                "atmosphere",
+                "atmospheric radiation",
+                "clouds",
+                "earth science",
+                "land surface",
+                "atmospheric chemistry",
+                "atmospheric pressure",
+                "oceans",
+                "ocean temperature",
+                "atmospheric water vapor",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aqua/AIRS/DATA303",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-17",
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
+            "series-name": "AIRS3STD",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-08-31T00:00:00Z/2025-01-20T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AIRS/Aqua L3 Daily Standard Physical Retrieval (AIRS-only) 1 degree x 1 degree V006 (AIRS3STD) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-NAVCAM-5-WEDGE-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-navcam-5-wedge-ops-v1.0_5b3v-9t4s",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-NAVCAM-5-WEDGE-OPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-navcam-5-wedge-ops-v1.0_5b3v-9t4s",
-            "description": "NULL",
-            "title": "MER 2 MARS NAVIGATION CAMERA TERRAIN\n                                      WEDGE RDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MER 2 MARS NAVIGATION CAMERA TERRAIN\n                                      WEDGE RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=P11-J-HVM-4-SUMM-S3COORDS-1MIN-V1.0",
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
-                "pioneer 11"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Pioneer 11 HVM data near Jupiter in System III [1965] coordinates. The magnetic field components are the standard right handed spherical triad (R, Theta, Phi) for a Jupiter centered system. The trajectory data are in a left handed, spherical coordinate system.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.p11-j-hvm-4-summ-s3coords-1min-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "jupiter",
+                "pioneer 11"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=P11-J-HVM-4-SUMM-S3COORDS-1MIN-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.p11-j-hvm-4-summ-s3coords-1min-v1.0",
-            "description": "Pioneer 11 HVM data near Jupiter in System III [1965] coordinates. The magnetic field components are the standard right handed spherical triad (R, Theta, Phi) for a Jupiter centered system. The trajectory data are in a left handed, spherical coordinate system.",
-            "title": "P11 JUPITER HVM SUMMARY S3 COORDS 1 MINUTE",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "P11 JUPITER HVM SUMMARY S3 COORDS 1 MINUTE"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-ER-4-MAP1%2FANGULAR-FLUX-V1.0",
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
+            "description": "This data set consists of calibrated, time-ordered, angle-resolved electron flux data from the Electron Reflectometer (ER) instrument on the Mars Global Surveyor (MGS) spacecraft. The primary data consist of time-series tables with descriptive headers. The data set also includes ancillary data (including geometry), documentation, and browse plots.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-er-4-map1-angular-flux-v1.0_5b4w-bdkw",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars global surveyor",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-ER-4-MAP1%2FANGULAR-FLUX-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-er-4-map1-angular-flux-v1.0_5b4w-bdkw",
-            "description": "This data set consists of calibrated, time-ordered, angle-resolved electron flux data from the Electron Reflectometer (ER) instrument on the Mars Global Surveyor (MGS) spacecraft. The primary data consist of time-series tables with descriptive headers. The data set also includes ancillary data (including geometry), documentation, and browse plots.",
-            "title": "MGS MARS/MOONS MAG/ER MAPPING ER ANGULAR FLUX V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MGS MARS/MOONS MAG/ER MAPPING ER ANGULAR FLUX V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/826",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Pinheiro, A.C. 2005. SAFARI 2000 AVHRR-derived Land Surface Temperature Maps, Africa, 1995-2000. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/826",
-            "issued": "2023-10-18",
-            "temporal": "1995-01-01T00:00:00Z/2000-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-24",
-            "keyword": [
-                "earth science",
-                "atmospheric radiation",
-                "surface thermal properties",
-                "atmosphere",
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
-            "identifier": "C2788408061-ORNL_CLOUD",
             "description": "Land Surface Temperature (LST) is a key indicator of land surface states, and can provide information on surface-atmosphere heat and mass fluxes, vegetation water stress, and soil moisture. A daily, day and night, LST data set for continental Africa, including Madagascar, was derived from Advanced Very High Resolution Radiometer (AVHRR) Global Area Coverage (GAC; 4 km resolution) data for the 6-year lifetime of the NOAA-14 satellite (from 1995 to 2000) using a modified version of the Global Inventory Mapping and Monitoring System (GIMMS) (Tucker et al., 1994). The data were projected into Albers Equal Area and aggregated to 8 km spatial resolution. The data were cloud-filtered with CLAVR-1 algorithm (Stowe et al., 1999). The LST values were estimated with a split-window technique (Ulivieri et al., 1994) that takes advantage of differential absorption of the thermal infrared signal in bands 4 and 5. The emissivity of the surface was generated using a land cover classification map (Hansen et al., 2000) combined with the FAO soil map of Africa (FAO-UNESCO, 1977) and additional maps of tree, herbaceous, and bare soil percent cover (DeFries et al., 2000). Collateral products include cloud mask, time-of-scan, latitude and longitude, and land/water mask files.The data are in flat binary files. Each data file contains 1152 columns and 1152 rows, in signed integer format (2 bytes), with 8 km by 8 km spatial resolution. A unique map exists for each day and each night of the 6-year NOAA-14 lifetime. The data are best used to infer broad temporal and spatial trends rather than pixel-by-pixel values.",
-            "graphic-preview-description": "Browse Image",
-            "title": "SAFARI 2000 AVHRR-derived Land Surface Temperature Maps, Africa, 1995-2000",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/safari_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F826",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F826",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/remote_sensing/AVHRR_LST/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/remote_sensing/AVHRR_LST/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/S2K/guides/AVHRR_LST.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/S2K/guides/AVHRR_LST.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/826",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/826",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/AVHRR_LST/comp/AVHRR_LST_readme.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/AVHRR_LST/comp/AVHRR_LST_readme.pdf",
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
+            "identifier": "C2788408061-ORNL_CLOUD",
+            "issued": "2023-10-18",
+            "keyword": [
+                "earth science",
+                "atmospheric radiation",
+                "surface thermal properties",
+                "atmosphere",
+                "land use/land cover",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/826",
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
             "spatial": "-24.6 -42.24 64.52 43.71",
+            "temporal": "1995-01-01T00:00:00Z/2000-12-31T23:59:59Z",
             "theme": [
                 "SAFARI 2000",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAFARI 2000 AVHRR-derived Land Surface Temperature Maps, Africa, 1995-2000"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H44B2Z74",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for International Earth Science Information Network - CIESIN - Columbia University, International Food Policy Research Institute - IFPRI, The World Bank, and Centro Internacional de Agricultura Tropical - CIAT. 2011-09-26. Global Rural-Urban Mapping Project, Version 1 (GRUMPv1): National Administrative Boundaries. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H44B2Z74. https://doi.org/10.7927/H44B2Z74.",
-            "issued": "2011-09-26",
-            "temporal": "2000-07-01T00:00:00Z/2000-07-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2011-09-26",
-            "references": [
-                "https://doi.org/10.7927/H4VT1Q1H",
-                "https://doi.org/10.7927/H4CR5R8J",
-                "https://doi.org/10.7927/H40K26HS",
-                "https://doi.org/10.7927/H4R20Z93",
-                "https://doi.org/10.7927/H4M906KR",
-                "https://doi.org/10.7927/H4GH9FVG"
-            ],
-            "keyword": [
-                "human dimensions",
-                "earth science",
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
-            "identifier": "C2210239480-SEDAC",
-            "description": "The Global Rural-Urban Mapping Project, Version 1 (GRUMPv1): National Administrative Boundaries are derived from the land area grid to show the outlines of pixels (cells) that contain administrative Units in GRUMPv1 on a per-country/territory basis. They are derived from the pixels as polygons and thus have rectilinear boundaries at a large scale. The polygons that outline the countries and territories are not official representations; rather they represent the area covered by the statistical data as provided. This data set is produced by the Columbia University Center for International Earth Science Information Network (CIESIN) in collaboration with the International Food Policy Research Institute (IFPRI), The World Bank, and Centro Internacional de Agricultura Tropical (CIAT).",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Center for International Earth Science Information Network - CIESIN - Columbia University, International Food Policy Research Institute - IFPRI, The World Bank, and Centro Internacional de Agricultura Tropical - CIAT",
-            "title": "Global Rural-Urban Mapping Project, Version 1 (GRUMPv1): National Administrative Boundaries",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/grump-v1/grump-v1-national-admin-boundaries/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Global Rural-Urban Mapping Project, Version 1 (GRUMPv1): National Administrative Boundaries are derived from the land area grid to show the outlines of pixels (cells) that contain administrative Units in GRUMPv1 on a per-country/territory basis. They are derived from the pixels as polygons and thus have rectilinear boundaries at a large scale. The polygons that outline the countries and territories are not official representations; rather they represent the area covered by the statistical data as provided. This data set is produced by the Columbia University Center for International Earth Science Information Network (CIESIN) in collaboration with the International Food Policy Research Institute (IFPRI), The World Bank, and Centro Internacional de Agricultura Tropical (CIAT).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH44B2Z74",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH44B2Z74",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/grump-v1/grump-v1-national-admin-boundaries/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/grump-v1/grump-v1-national-admin-boundaries/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/grump-v1-national-admin-boundaries/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/grump-v1-national-admin-boundaries/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/grump-v1-national-admin-boundaries",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/grump-v1-national-admin-boundaries",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/grump-v1/grump-v1-national-admin-boundaries/sedac-logo.jpg",
+            "identifier": "C2210239480-SEDAC",
+            "issued": "2011-09-26",
+            "keyword": [
+                "human dimensions",
+                "earth science",
+                "boundaries"
+            ],
+            "landingPage": "https://doi.org/10.7927/H44B2Z74",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2011-09-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H4VT1Q1H",
+                "https://doi.org/10.7927/H4CR5R8J",
+                "https://doi.org/10.7927/H40K26HS",
+                "https://doi.org/10.7927/H4R20Z93",
+                "https://doi.org/10.7927/H4M906KR",
+                "https://doi.org/10.7927/H4GH9FVG"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -58.0 180.0 85.0",
+            "temporal": "2000-07-01T00:00:00Z/2000-07-01T00:00:00Z",
             "theme": [
                 "GRUMP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Rural-Urban Mapping Project, Version 1 (GRUMPv1): National Administrative Boundaries"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/728/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-05-09",
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
-            "identifier": "DASHLINK_728",
             "description": "This paper proposes a combined energy-based model with an empirical physics of failure model for degradation analysis and prognosis of electrolytic capacitors in DC-DC power converters. Electrolytic capacitors and MOSFET\u2019s have higher failure rates than other components in DC-DC converter systems. For example, in avionics systems where the power supply drives a GPS unit, ripple currents can cause glitches in the GPS position and velocity output, and this may cause errors in the Inertial Navigation (INAV) system causing the aircraft to fly off course. We have employed a topological energy based modeling scheme based on the bond graph (BG) modeling language for building parametric models of electrical domain systems. Our current work adopts a physics of failure model (Arrhenius Law) for equivalent series resistance (ESR) increase in electrolytic capacitors subjected to electrical and thermal stresses. Experiments for capacitor degradation were conducted for collecting degradation ESR data. Parameter re-estimation for the failure model is done using the experimental data. The derived degradation model of the capacitor is reintroduced into the DC-DC converter system model to study changes in the system performance using Monte Carlo simulation methods. Stochastic simulation methods applied to the combined model help us predict how system performance deteriorates with time.",
-            "title": "Physics of Failure Models for Capacitor Degradation in DC-DC Converters",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2010_MARCON_DCDCConverter.pdf",
-                    "description": "2010_MARCON_DCDCConverter.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "2010_MARCON_DCDCConverter.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2010_MARCON_DCDCConverter.pdf",
+                    "mediaType": "application/pdf",
                     "title": "2010_MARCON_DCDCConverter.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_728",
+            "issued": "2013-05-09",
+            "keyword": [
+                "nasa",
+                "ames",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/728/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Physics of Failure Models for Capacitor Degradation in DC-DC Converters"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1615905765-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, OB.DAAC.",
-            "issued": "2019-06-23",
-            "temporal": "2002-07-04T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-10-01",
-            "keyword": [
-                "ngda",
-                "earth science",
-                "national geospatial data asset",
-                "ocean temperature",
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
-            "identifier": "C1615905765-OB_DAAC",
             "description": "MODIS (or Moderate Resolution Imaging Spectroradiometer) is a key instrument aboard the Terra (EOS AM) and Aqua (EOS PM) satellites. Terra's orbit around the Earth is timed so that it passes from north to south across the equator in the morning, while Aqua passes south to north over the equator in the afternoon. Terra MODIS and Aqua MODIS are viewing the entire Earth's surface every 1 to 2 days, acquiring data in 36 spectral bands, or groups of wavelengths (see MODIS Technical Specifications). These data will improve our understanding of global dynamics and processes occurring on the land, in the oceans, and in the lower atmosphere. MODIS is playing a vital role in the development of validated, global, interactive Earth system models able to predict global change accurately enough to assist policy makers in making sound decisions concerning the protection of our environment.",
-            "title": "Aqua MODIS Regional 11\u00b5m Day/Night Sea Surface Temperature (SST) Data, version R2019.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directaccess/MODIS-Aqua/L2/",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directaccess/MODIS-Aqua/L2/",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/AQUA/MODIS/L2/SST/R2019.0",
-                    "description": "MODIS-Aqua L2 11\u00b5m Daytime Sea Surface Temperature (SST) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS-Aqua L2 11\u00b5m Daytime Sea Surface Temperature (SST) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/AQUA/MODIS/L2/SST/R2019.0",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1615905765-OB_DAAC",
+            "issued": "2019-06-23",
+            "keyword": [
+                "ngda",
+                "earth science",
+                "national geospatial data asset",
+                "ocean temperature",
+                "oceans"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1615905765-OB_DAAC.html",
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
+            "title": "Aqua MODIS Regional 11\u00b5m Day/Night Sea Surface Temperature (SST) Data, version R2019.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA2010",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Froidevaux, L., Livesey, N. and Read, W.. 2015-02-19. ML2HCL. Version 004. MLS/Aura Level 2 Hydrogen Chloride (HCl) Mixing Ratio V004. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA2010. https://disc.gsfc.nasa.gov/datacollection/ML2HCL_004.html. Digital Science Data.",
-            "issued": "2015-02-19",
-            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-02-19",
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
-            "identifier": "C1223720291-GES_DISC",
-            "description": "ML2HCL is the EOS Aura Microwave Limb Sounder (MLS) standard product for  hydrogen chloride derived from radiances measured primarily by the 640 GHz radiometer. The data version is 4.2. Spatial coverage is near-global (-82  degrees to +82  degrees latitude), with each profile spaced 1.5  degrees or ~165 km along the orbit track (roughly 15 orbits per day). The recommended useful vertical range is from 100 to 0.316 hPa, and the vertical resolution is between 3 and 6 km. Users of the ML2HCL data product should read section 3.10 of the EOS MLS Level 2 Version 4 Quality Document for more information.\n\nThe data are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5), which is based on the version 5 Hierarchical Data Format, or HDF-5. Each file contains two swath objects (profile and column data), each with a set of data and geolocation fields, swath attributes, and metadata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML2HCL",
             "creator": "Froidevaux, L., Livesey, N. and Read, W.",
-            "title": "MLS/Aura Level 2 Hydrogen Chloride (HCl) Mixing Ratio V004 (ML2HCL) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2HCL_004.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "ML2HCL is the EOS Aura Microwave Limb Sounder (MLS) standard product for  hydrogen chloride derived from radiances measured primarily by the 640 GHz radiometer. The data version is 4.2. Spatial coverage is near-global (-82  degrees to +82  degrees latitude), with each profile spaced 1.5  degrees or ~165 km along the orbit track (roughly 15 orbits per day). The recommended useful vertical range is from 100 to 0.316 hPa, and the vertical resolution is between 3 and 6 km. Users of the ML2HCL data product should read section 3.10 of the EOS MLS Level 2 Version 4 Quality Document for more information.\n\nThe data are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5), which is based on the version 5 Hierarchical Data Format, or HDF-5. Each file contains two swath objects (profile and column data), each with a set of data and geolocation fields, swath attributes, and metadata.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA2010",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA2010",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -181885,180 +181863,176 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML2HCL_004.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML2HCL_004.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level2/ML2HCL.004/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level2/ML2HCL.004/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level2/ML2HCL.004/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level2/ML2HCL.004/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML2HCL_004",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML2HCL_004",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2HCL_004.png",
+            "identifier": "C1223720291-GES_DISC",
+            "issued": "2015-02-19",
+            "keyword": [
+                "atmospheric chemistry",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA2010",
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
+            "series-name": "ML2HCL",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MLS/Aura Level 2 Hydrogen Chloride (HCl) Mixing Ratio V004 (ML2HCL) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-DERIVED-LIGHTCURVE-V11.0",
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
+            "description": "This is a compilation of published rotational parameters derived from lightcurve data for asteroids, based on the Warner et al. (2009) Asteroid Lightcurve Database. This is the version released on Mar. 9, 2010. In addition to reported rotational parameters by individual paper, there is a summary file with the values adopted by Harris, Warner, and Pravec as the most likely correct values for each asteroid. The data set also contains files listing known binary asteroids and 'tumbling' asteroids.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-derived-lightcurve-v11.0_5bbt-vt2f",
+            "issued": "2021-05-21",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-DERIVED-LIGHTCURVE-V11.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-derived-lightcurve-v11.0_5bbt-vt2f",
-            "description": "This is a compilation of published rotational parameters derived from lightcurve data for asteroids, based on the Warner et al. (2009) Asteroid Lightcurve Database. This is the version released on Mar. 9, 2010. In addition to reported rotational parameters by individual paper, there is a summary file with the values adopted by Harris, Warner, and Pravec as the most likely correct values for each asteroid. The data set also contains files listing known binary asteroids and 'tumbling' asteroids.",
-            "title": "ASTEROID LIGHTCURVE DERIVED DATA V11.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ASTEROID LIGHTCURVE DERIVED DATA V11.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1386",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Walker, D.A., and M.K. Raynolds. 2018. Maps of Vegetation, NDVI, Snow and Thaw Depths: North Slope, Alaska and NWT, Canada. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1386",
-            "issued": "2018-12-31",
-            "temporal": "2000-08-01T00:00:00Z/2012-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "snow/ice",
-                "vegetation",
-                "terrestrial hydrosphere",
-                "land use/land cover",
-                "land surface",
-                "frozen ground",
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
-            "identifier": "C2162118968-ORNL_CLOUD",
             "description": "This dataset includes vegetation cover maps, Normalized Difference Vegetation Index (NDVI) maps, snow depth and thaw depth data that were obtained as part of a biocomplexity project on the North Slope of Alaska, USA, and the Northwest Territories (NWT), Canada. In Alaska, seven sites are located along the Dalton Highway and in the Prudhoe Bay Oilfield area, forming a transect across the climate gradient of the North Slope. From South to North, the sites are Happy Valley, Sagwon (an acidic and nonacidic site), Franklin Bluffs, Deadhorse, West Dock and Howe Island. Four sites are in the NWT, forming a latitudinal gradient from South to North; the sites include Inuvik, Green Cabin, Mould Bay, and Isachsen.",
-            "graphic-preview-description": "Browse Image",
-            "title": "Maps of Vegetation, NDVI, Snow and Thaw Depths: North Slope, Alaska and NWT, Canada",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/North_Slope_Transect_Veg_Maps_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1386",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1386",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/North_Slope_Transect_Veg_Maps/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/North_Slope_Transect_Veg_Maps/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/North_Slope_Transect_Veg_Maps.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/North_Slope_Transect_Veg_Maps.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1386",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1386",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
@@ -182068,673 +182042,677 @@
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/North_Slope_Transect_Veg_Maps_Fig1.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/North_Slope_Transect_Veg_Maps_Fig1.png",
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
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/North_Slope_Transect_Veg_Maps_Fig1.png",
+            "identifier": "C2162118968-ORNL_CLOUD",
+            "issued": "2018-12-31",
+            "keyword": [
+                "snow/ice",
+                "vegetation",
+                "terrestrial hydrosphere",
+                "land use/land cover",
+                "land surface",
+                "frozen ground",
+                "earth science",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1386",
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
             "spatial": "-148.85 68.36 -103.55 78.79",
+            "temporal": "2000-08-01T00:00:00Z/2012-12-31T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Maps of Vegetation, NDVI, Snow and Thaw Depths: North Slope, Alaska and NWT, Canada"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567953-USGS_LTA.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, DOI/USGS/EROS.",
-            "issued": "2019-09-20",
-            "temporal": "1970-01-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-03-25",
-            "keyword": [
-                "soils",
-                "land use/land cover",
-                "earth science",
-                "landscape",
-                "land surface",
-                "topography",
-                "surface radiative properties",
-                "geomorphic landforms/processes",
-                "erosion/sedimentation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNIEPAT JOHNSON",
                 "hasEmail": "mailto:lta@usgs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOI/USGS/EROS"
-            },
-            "identifier": "C1220567953-USGS_LTA",
             "description": "The U.S. Geological Survey (USGS) National Geospatial Program (NGP) developed the Alaska Mapping Initiative (AMI) to collaborate with the State and other Federal partners to acquire 3-dimensional elevation data to improve statewide topographic maps for Alaska. AMI coordinates Federal activities through the Alaska Mapping Executive Committee (AMEC) and State efforts through Alaska's Statewide Digital Mapping Initiative (SDMI) to ensure a unified approach for consistent data acquisition and enhancement of elevation data products.  AMI attained interferometric synthetic aperture radar (IFSAR) to generate digital elevation model (DEM) data. This radar mapping technology is an effective tool for collecting data in challenging circumstances such as cloud cover, extreme weather conditions, rugged terrain, and remote locations. Airborne IFSAR data were flown over South Central Alaska in the summer of 2010 and over Northwest Alaska in 2012.",
-            "title": "Interferometric Synthetic Aperture Radar (IFSAR) Alaska",
-            "programCode": [
-                "026:001"
-            ],
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
-                    "downloadURL": "http://nationalmap.gov/alaska/",
-                    "description": "\n         USGS Alaska Mapping Initiative\n      ",
                     "@type": "dcat:Distribution",
+                    "description": "\n         USGS Alaska Mapping Initiative\n      ",
+                    "downloadURL": "http://nationalmap.gov/alaska/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://www.alaskamapped.org/dem",
-                    "description": "\n         Alaska\u2019s Statewide Digital Mapping Initiative\n      ",
                     "@type": "dcat:Distribution",
+                    "description": "\n         Alaska\u2019s Statewide Digital Mapping Initiative\n      ",
+                    "downloadURL": "http://www.alaskamapped.org/dem",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://nationalmap.gov/alaska/about_ak_excomm.html",
-                    "description": "\n         Alaska Mapping Executive Committee\n      ",
                     "@type": "dcat:Distribution",
+                    "description": "\n         Alaska Mapping Executive Committee\n      ",
+                    "downloadURL": "http://nationalmap.gov/alaska/about_ak_excomm.html",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://pubs.usgs.gov/fs/2013/3083/pdf/fs2013-3083.pdf",
-                    "description": "\n         USGS Factsheet - The 3D Elevation Program \u2013 Summary for Alaska\n      ",
                     "@type": "dcat:Distribution",
+                    "description": "\n         USGS Factsheet - The 3D Elevation Program \u2013 Summary for Alaska\n      ",
+                    "downloadURL": "http://pubs.usgs.gov/fs/2013/3083/pdf/fs2013-3083.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product history"
                 }
             ],
+            "identifier": "C1220567953-USGS_LTA",
+            "issued": "2019-09-20",
+            "keyword": [
+                "soils",
+                "land use/land cover",
+                "earth science",
+                "landscape",
+                "land surface",
+                "topography",
+                "surface radiative properties",
+                "geomorphic landforms/processes",
+                "erosion/sedimentation"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567953-USGS_LTA.html",
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
             "spatial": "130.0 54.666668 173.0 71.833336",
+            "temporal": "1970-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "AMI",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Interferometric Synthetic Aperture Radar (IFSAR) Alaska"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VJ103DNB_NRT.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "VCST Team. 2019-04-08. VIIRS/JPSS1 VIIRS/VJ1 Day/Night Band Resolution Terrain Corrected Geolocation 6-Min L1 Swath 750m NRT. Version 2. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, LANCEMODIS. https://doi.org/10.5067/VIIRS/VJ103DNB_NRT.002. https://dx.doi.org/10.5067/VIIRS/VJ103DNB_NRT.002.",
-            "issued": "2019-04-08",
-            "temporal": "2019-04-08T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-04-04",
-            "keyword": [
-                "visible wavelengths",
-                "infrared wavelengths",
-                "earth science",
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
-            "identifier": "C1604621211-LANCEMODIS",
-            "description": "The Near Real Time (NRT) VIIRS/VJ1 Day/Night Band Resolution Terrain Corrected Geolocation 6-Min L1 Swath 750m (VJ103DNB_NRT) product includes the geolocation fields that are calculated for VIIRS day-night band (DNB) Line of sight (LOS) for all orbits at the nominal resolution of 750 m. The locations and ancillary information correspond to the intersection of the centers of each Field of View (FOV) from 16 detectors in the DNB on the Earth's surface. A digital terrain model is used to model the Earth's surface. The main inputs are the spacecraft attitude and orbit ephemeris data, the instrument telemetry and the digital elevation model. The geolocation fields contained within the VNP03DNB Geolocation files include geodetic latitude, longitude, surface height above the geoid, solar and lunar zenith and azimuth angles, lunar phase angle and illumination fraction, satellite zenith and azimuth angles, and a land/water mask for each 750m sample. Additional information is included in the header to enable the calculation of the approximate location of the center of the detectors for any of the VIIRS bands. This product is used as input by subsequent VIIRS day/night band products, particularly those produced by the Land team.",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "VCST Team",
-            "title": "VIIRS/JPSS1 Day/Night Band Resolution Terrain Corrected Geolocation 6-Min L1 Swath 750m NRT",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Near Real Time (NRT) VIIRS/VJ1 Day/Night Band Resolution Terrain Corrected Geolocation 6-Min L1 Swath 750m (VJ103DNB_NRT) product includes the geolocation fields that are calculated for VIIRS day-night band (DNB) Line of sight (LOS) for all orbits at the nominal resolution of 750 m. The locations and ancillary information correspond to the intersection of the centers of each Field of View (FOV) from 16 detectors in the DNB on the Earth's surface. A digital terrain model is used to model the Earth's surface. The main inputs are the spacecraft attitude and orbit ephemeris data, the instrument telemetry and the digital elevation model. The geolocation fields contained within the VNP03DNB Geolocation files include geodetic latitude, longitude, surface height above the geoid, solar and lunar zenith and azimuth angles, lunar phase angle and illumination fraction, satellite zenith and azimuth angles, and a land/water mask for each 750m sample. Additional information is included in the header to enable the calculation of the approximate location of the center of the detectors for any of the VIIRS bands. This product is used as input by subsequent VIIRS day/night band products, particularly those produced by the Land team.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ103DNB_NRT.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ103DNB_NRT.002",
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
+            "identifier": "C1604621211-LANCEMODIS",
+            "issued": "2019-04-08",
+            "keyword": [
+                "visible wavelengths",
+                "infrared wavelengths",
+                "earth science",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VJ103DNB_NRT.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-04-04",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2019-04-08T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "JPSS1",
                 "LANCE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/JPSS1 Day/Night Band Resolution Terrain Corrected Geolocation 6-Min L1 Swath 750m NRT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/614",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Zheng, D.L., S.D. Prince, and R. Wright. 2013. NPP Multi-Biome: Gridded Estimates for Selected Regions Worldwide, 1954-1998, R3. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/614",
-            "issued": "2023-08-20",
-            "temporal": "1954-01-01T00:00:00Z/1998-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-23",
-            "keyword": [
-                "vegetation",
-                "biosphere",
-                "ecological dynamics",
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
-            "identifier": "C2755571426-ORNL_CLOUD",
             "description": "This data set provides two data files (.csv format) containing gridded (0.5-degree) estimates of net primary productivity (NPP), elevation, temperature, precipitation, NDVI, and biome type for selected terrestrial regions of the world. The field data used to develop NPP estimates came from 15 worldwide data sources in several different biomes covering the period 1954-1998. NPP values were developed from natural resource field inventories (e.g., forest, rangeland, crop) at different scales, from plot to county; from data compiled from published literature and high resolution maps; from simulation models using key independent variables; from regression analyses with environmental variables; and by using relationships between remotely-sensed spectral vegetation indices and field observations. The first file, NPP_Gridded_3654_cells_R3.csv with 3,654 0.5-degree grid cells, is suitable for biome level and overall analyses because of a larger sample size. In this file, 36 cells have above-ground net primary production (ANPP) only, 320 cells have total net promary production (TNPP) only, and 3,298 cells have both TNPP and ANPP. The second file, NPP_Gridded_2335_unique_cell_R3s.csv, was derived from the larger file and contains 2,335 0.5-degree grid cells after outliers were excluded, replicate measurements were averaged out for each unique geographic location, and cells classified as water, bare ground, and urban were excluded. This smaller data file is more appropriate for model/data inter-comparisons. Overall, gridded ANPP values ranged from 3 to 890 gC/m2/yr, and gridded TNPP values ranged from 3 to 1,235 gC/m2/yr. The lowest values are for sparsely vegetated ground (e.g., open shrublands) and the highest values are for forests. Revision Notes: This data set has been revised to correct the previously reported temporal coverage of field data measurements that were used to develop NPP estimates and the data set title was also corrected to reflect the date change. Missing value codes were added. Please see the Data Set Revisions section of this document for detailed information.",
-            "graphic-preview-description": "Browse Image",
-            "title": "NPP Multi-Biome: Gridded Estimates for Selected Regions Worldwide, 1954-1998, R3",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/npp_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F614",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F614",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/npp/multi_biome/NPP_GRIDDED_GPPDI/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/npp/multi_biome/NPP_GRIDDED_GPPDI/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_GRIDDED_GPPDI.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_GRIDDED_GPPDI.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/614",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/614",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/multi_biome/NPP_GRIDDED_GPPDI/comp/NPP_GRIDDED_GPPDI.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/multi_biome/NPP_GRIDDED_GPPDI/comp/NPP_GRIDDED_GPPDI.pdf",
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
+            "identifier": "C2755571426-ORNL_CLOUD",
+            "issued": "2023-08-20",
+            "keyword": [
+                "vegetation",
+                "biosphere",
+                "ecological dynamics",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/614",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-08-23",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-122.25 -33.75 152.75 63.75",
+            "temporal": "1954-01-01T00:00:00Z/1998-12-31T23:59:59Z",
             "theme": [
                 "NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NPP Multi-Biome: Gridded Estimates for Selected Regions Worldwide, 1954-1998, R3"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TERRA/MOPITT/MOP02T_L2.109",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/TERRA/MOPITT/MOP02T_L2.109. https://asdc.larc.nasa.gov/project/MOPITT.",
-            "issued": "2020-12-23",
-            "temporal": "2018-03-25T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-23",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric chemistry"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "HELEN WORDEN",
                 "hasEmail": "mailto:hmw@ucar.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2103889027-LARC",
             "description": "MOP02T_109 is the Measurements Of Pollution In The Troposphere (MOPITT) Beta Derived CO (Thermal Infrared Radiances) version 109 product. It is an unvalidated beta product subject to recalibration, consists of the geo-located, retrieved carbon monoxide profiles and total column amounts for carbon monoxide. Ancillary data concerning surface properties and cloud conditions at the locations of the retrieved parameters are also included. Each retrieval is accompanied by an estimated error. Version 109 products are beta versions for version 9 products, they are unvalidated beta products subject to recalibration. Data collection for this version is ongoing. \r\rMOPITT was successfully launched into sun-synchronous polar orbit aboard Terra, NASA's first Earth Observing System spacecraft on December 18, 1999. The MOPITT instrument was constructed by a consortium of Canadian companies and funded by the Space Science Division of the Canadian Space Agency.",
-            "graphic-preview-description": "NASA Worldview",
-            "title": "MOPITT Beta Derived CO (Thermal Infrared Radiances) V109",
-            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMOPITT%2FMOP02T_L2.109",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMOPITT%2FMOP02T_L2.109",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www2.acom.ucar.edu/mopitt",
-                    "description": "U.S. MOPITT project home page",
                     "@type": "dcat:Distribution",
+                    "description": "U.S. MOPITT project home page",
+                    "downloadURL": "https://www2.acom.ucar.edu/mopitt",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.atmosp.physics.utoronto.ca/MOPITT/home.html",
-                    "description": "Canadian MOPITT project home page",
                     "@type": "dcat:Distribution",
+                    "description": "Canadian MOPITT project home page",
+                    "downloadURL": "https://www.atmosp.physics.utoronto.ca/MOPITT/home.html",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://mopitt.physics.utoronto.ca/",
-                    "description": "University of Toronto MOPITT Overview",
                     "@type": "dcat:Distribution",
+                    "description": "University of Toronto MOPITT Overview",
+                    "downloadURL": "https://mopitt.physics.utoronto.ca/",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://eospso.gsfc.nasa.gov/atbd-category/48",
-                    "description": "NASA EOS ATB Documents: MOPITT",
                     "@type": "dcat:Distribution",
+                    "description": "NASA EOS ATB Documents: MOPITT",
+                    "downloadURL": "https://eospso.gsfc.nasa.gov/atbd-category/48",
+                    "mediaType": "text/html",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/mopitt/guide/ASDC_MOPITT_Overview_2015.pdf",
-                    "description": "Overview of MOPITT Data at the ASDC",
                     "@type": "dcat:Distribution",
+                    "description": "Overview of MOPITT Data at the ASDC",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/mopitt/guide/ASDC_MOPITT_Overview_2015.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://terra.nasa.gov/",
-                    "description": "Terra Instrument home page",
                     "@type": "dcat:Distribution",
+                    "description": "Terra Instrument home page",
+                    "downloadURL": "https://terra.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/mopitt/tools/README_MOPITT_L2Viewer.txt",
-                    "description": "MOPITT Level 2 Viewer Software Readme File",
                     "@type": "dcat:Distribution",
+                    "description": "MOPITT Level 2 Viewer Software Readme File",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/mopitt/tools/README_MOPITT_L2Viewer.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/x-tar",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/mopitt/tools/MOPITT_L2Viewer.tar",
-                    "description": "MOPITT Level 2 Viewer Tool Software Package - Direct File Download (.tar)",
                     "@type": "dcat:Distribution",
+                    "description": "MOPITT Level 2 Viewer Tool Software Package - Direct File Download (.tar)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/mopitt/tools/MOPITT_L2Viewer.tar",
+                    "mediaType": "application/x-tar",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/mopitt/mopitt_quality_statements.html",
-                    "description": "ASDC List of MOPITT Quality Statements",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC List of MOPITT Quality Statements",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/mopitt/mopitt_quality_statements.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data quality document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www2.acom.ucar.edu/mopitt/visualization",
-                    "description": "MOPITT Visualizations",
                     "@type": "dcat:Distribution",
+                    "description": "MOPITT Visualizations",
+                    "downloadURL": "https://www2.acom.ucar.edu/mopitt/visualization",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/MOPITT",
-                    "description": "ASDC Data and Information for MOPITT",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for MOPITT",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/MOPITT",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthdata.nasa.gov/learn/sensing-our-planet/on-the-trail-of-global-pollution-drift",
-                    "description": "Earth Observing System Data and InformationSystem (EOSDIS) Article: On The Trail of Global Pollution Drift",
                     "@type": "dcat:Distribution",
+                    "description": "Earth Observing System Data and InformationSystem (EOSDIS) Article: On The Trail of Global Pollution Drift",
+                    "downloadURL": "https://earthdata.nasa.gov/learn/sensing-our-planet/on-the-trail-of-global-pollution-drift",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/",
-                    "description": "Goddard Earth Sciences Data and Information Services Center (GES DISC): Giovanni - Interactive Visualization and Analysis software",
                     "@type": "dcat:Distribution",
+                    "description": "Goddard Earth Sciences Data and Information Services Center (GES DISC): Giovanni - Interactive Visualization and Analysis software",
+                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/",
+                    "mediaType": "text/html",
                     "title": "Subset this dataset using a web based subsetter"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.harrisgeospatial.com/Support/Forums/aft/2540",
-                    "description": "L3 Harris Geospatial Forum: Reading multiple HDF/NCDF files in IDL running under Fedora 13",
                     "@type": "dcat:Distribution",
+                    "description": "L3 Harris Geospatial Forum: Reading multiple HDF/NCDF files in IDL running under Fedora 13",
+                    "downloadURL": "https://www.harrisgeospatial.com/Support/Forums/aft/2540",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/10775/bushfires-raging-in-southeast-australia",
-                    "description": "NASA Earth Observatory Article: Bushfires Raging in Southeast Australia : Natural Hazards\u00a0- Data taken by the Measurements Of Pollution In The Troposphere (MOPITT) instrument aboard NASA's Terra satellite have been combined for 6 days from January 15-20, 2003",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Bushfires Raging in Southeast Australia : Natural Hazards\u00a0- Data taken by the Measurements Of Pollution In The Troposphere (MOPITT) instrument aboard NASA's Terra satellite have been combined for 6 days from January 15-20, 2003",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/10775/bushfires-raging-in-southeast-australia",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/13721/carbon-monoxide-from-tropical-fires",
-                    "description": "NASA Earth Observatory Article: Carbon Monoxide from Tropical Fires : Natural Hazards\u00a0-\u00a0The Terra MOPITT sensor observed large plumes of carbon monoxide produced by biomass burning in South America and Africa in early August 2004.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Carbon Monoxide from Tropical Fires : Natural Hazards\u00a0-\u00a0The Terra MOPITT sensor observed large plumes of carbon monoxide produced by biomass burning in South America and Africa in early August 2004.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/13721/carbon-monoxide-from-tropical-fires",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/19011/fires-and-thick-smoke-over-south-america",
-                    "description": "NASA Earth Observatory Article: Fires and Thick Smoke over South America : Natural Hazards\u00a0-\u00a0Places where MOPITT could not collect enough data to make an estimate of carbon monoxide (probably due to clouds) are gray.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Fires and Thick Smoke over South America : Natural Hazards\u00a0-\u00a0Places where MOPITT could not collect enough data to make an estimate of carbon monoxide (probably due to clouds) are gray.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/19011/fires-and-thick-smoke-over-south-america",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/533/mopitt-first-light-image",
-                    "description": "NASA Earth Observatory Article: MOPITT First Light Image : Image of the Day\u00a0-\u00a0MOPITT measures radiances in several channels to determine the amount of carbon monoxide (CO) and methane in the atmosphere.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: MOPITT First Light Image : Image of the Day\u00a0-\u00a0MOPITT measures radiances in several channels to determine the amount of carbon monoxide (CO) and methane in the atmosphere.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/533/mopitt-first-light-image",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/852/mopitt-views-carbon-monoxide-concentration",
-                    "description": "NASA Earth Observatory Article: MOPITT Views Carbon Monoxide Concentration, there were widespread wildfires across Montana and Idaho.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: MOPITT Views Carbon Monoxide Concentration, there were widespread wildfires across Montana and Idaho.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/852/mopitt-views-carbon-monoxide-concentration",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/559/mopitt-views-north-america",
-                    "description": "NASA Earth Observatory Article: MOPITT Views North America : Image of the Day\u00a0-\u00a0Measurement of Pollution in the Troposphere, MOPITT, measures two important pollutants in the Earth's atmosphere\u2014carbon monoxide (CO) and methane.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: MOPITT Views North America : Image of the Day\u00a0-\u00a0Measurement of Pollution in the Troposphere, MOPITT, measures two important pollutants in the Earth's atmosphere\u2014carbon monoxide (CO) and methane.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/559/mopitt-views-north-america",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthdata.nasa.gov/learn/sensing-our-planet/nature-s-contribution",
-                    "description": "NASA Earthdata Article: Nature's contribution: Researchers investigate how much wildfires contribute to pollution, and how far this pollution can travel - By Jane Beitler",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earthdata Article: Nature's contribution: Researchers investigate how much wildfires contribute to pollution, and how far this pollution can travel - By Jane Beitler",
+                    "downloadURL": "https://earthdata.nasa.gov/learn/sensing-our-planet/nature-s-contribution",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://forum.earthdata.nasa.gov/app.php/tag/MOPITT",
-                    "description": "NASA Earthdata Forum - MOPITT Project Specific Forum",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earthdata Forum - MOPITT Project Specific Forum",
+                    "downloadURL": "https://forum.earthdata.nasa.gov/app.php/tag/MOPITT",
+                    "mediaType": "text/html",
                     "title": "Access this dataset's users feedback page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/feature/langley/longstanding-carbon-monoxide-measuring-instrument-mopitt-celebrated/",
-                    "description": "NASA Langley Article: Fourteen Years of Carbon Monoxide from MOPITT, which has truly unlocked a pathway for groundbreaking studies of air pollution transport and atmospheric chemical processes.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Langley Article: Fourteen Years of Carbon Monoxide from MOPITT, which has truly unlocked a pathway for groundbreaking studies of air pollution transport and atmospheric chemical processes.",
+                    "downloadURL": "https://www.nasa.gov/feature/langley/longstanding-carbon-monoxide-measuring-instrument-mopitt-celebrated/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://worldview.earthdata.nasa.gov/",
-                    "description": "NASA Worldview",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Worldview",
+                    "downloadURL": "https://worldview.earthdata.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through WORLDVIEW"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.pnas.org/content/115/20/5099",
-                    "description": "Proceedings of the National Academy of Sciences (PNAS) Article: Unexpected slowdown of US pollutant emission reduction in the past decade\u00a0(Ground and satellite observations show that air pollution regulations in the United States (US) have resulted in substantial reductions in emissions and corresponding improvements in air quality over the last several decades)",
                     "@type": "dcat:Distribution",
+                    "description": "Proceedings of the National Academy of Sciences (PNAS) Article: Unexpected slowdown of US pollutant emission reduction in the past decade\u00a0(Ground and satellite observations show that air pollution regulations in the United States (US) have resulted in substantial reductions in emissions and corresponding improvements in air quality over the last several decades)",
+                    "downloadURL": "https://www.pnas.org/content/115/20/5099",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
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
-                    "downloadURL": "https://hdfeos.org/zoo/",
-                    "description": "Examples on how to access and visualize various NASA HDF/HDF-EOS files using Python (pyhdf/h5py), NCL, MATLAB\u00ae, and IDL\u00ae, NCL, MATLAB\u00ae, and IDL\u00ae",
                     "@type": "dcat:Distribution",
+                    "description": "Examples on how to access and visualize various NASA HDF/HDF-EOS files using Python (pyhdf/h5py), NCL, MATLAB\u00ae, and IDL\u00ae, NCL, MATLAB\u00ae, and IDL\u00ae",
+                    "downloadURL": "https://hdfeos.org/zoo/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/TERRA/MOPITT/MOP02T_L2.109",
-                    "description": "DOI data set landing page for MOP02T_109",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for MOP02T_109",
+                    "downloadURL": "https://doi.org/10.5067/TERRA/MOPITT/MOP02T_L2.109",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "graphic-preview-description": "NASA Worldview",
+            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/",
+            "identifier": "C2103889027-LARC",
+            "issued": "2020-12-23",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/TERRA/MOPITT/MOP02T_L2.109",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-12-23",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-03-25T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "MOPITT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MOPITT Beta Derived CO (Thermal Infrared Radiances) V109"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0948-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-08-07T10:10:25.000 to 2015-08-07T17:26:29.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0948-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0948-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0948-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-08-07T10:10:25.000 to 2015-08-07T17:26:29.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0948 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0948 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2140",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Green, R.O., P.G. Brodrick, J.W. Chapman, M. Eastwood, S. Geier, M. Helmlinger, S.R. Lundeen, W. Olson-Duvall, R. Pavlick, L.M. Rios, D.R. Thompson, and A.K. Thorpe. 2023. AVIRIS Facility Instruments: Flight Line Geospatial and Contextual Data. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2140",
-            "issued": "2024-02-02",
-            "temporal": "2006-04-11T00:00:00Z/2022-11-03T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-02-06",
-            "keyword": [
-                "earth science",
-                "spectral/engineering",
-                "platform characteristics",
-                "sensor characteristics"
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
-            "identifier": "C2662360177-ORNL_CLOUD",
             "description": "This dataset provides attributed geospatial and tabular information for identifying and querying flight lines of interest for the Airborne Visible InfraRed Imaging Spectrometer-Classic (AVIRIS-C) and Airborne Visible InfraRed Imaging Spectrometer-Next Generation (AVIRIS-NG) Facility Instrument collections. It includes attributed shapefile and GeoJSON files containing polygon representation of individual flights lines for all years and separate KMZ files for each year. These files allow users to visualize and query flight line locations using Geographic Information System (GIS) software. Tables of AVIRIS-C and AVIRIS-NG flight lines with attributed information include dates, bounding coordinates, site names, investigators involved, flight attributes, associated campaigns, and corresponding file names for associated L1B (radiance) and L2 (reflectance) files in the AVIRIS-C and AVIRIS-NG Facility Instrument Collections. Tabular information is also provided in comma-separated values (CSV) format.",
-            "graphic-preview-description": "Location of AVIRIS-NG flight lines in the conterminous US for 2014 - 2021.  Inset shows detail of flight lines in coastal Louisiana associated with the Delta-X project.",
-            "title": "AVIRIS Facility Instruments: Flight Line Geospatial and Contextual Data",
-            "graphic-preview-file": "https://daac.ornl.gov/AVIRIS/guides/AVIRIS_FlightLine_Locator_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2140",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2140",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/aviris/AVIRIS_FlightLine_Locator/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/aviris/AVIRIS_FlightLine_Locator/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/AVIRIS/guides/AVIRIS_FlightLine_Locator.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/AVIRIS/guides/AVIRIS_FlightLine_Locator.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2140",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2140",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/aviris/AVIRIS_FlightLine_Locator/comp/AVIRIS_FlightLine_Locator.pdf",
-                    "description": "AVIRIS Facility Instruments: Flight Line Geospatial and Contextual Data: AVIRIS_FlightLine_Locator.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "AVIRIS Facility Instruments: Flight Line Geospatial and Contextual Data: AVIRIS_FlightLine_Locator.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/aviris/AVIRIS_FlightLine_Locator/comp/AVIRIS_FlightLine_Locator.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/AVIRIS/guides/AVIRIS_FlightLine_Locator_Fig1.jpg",
-                    "description": "Location of AVIRIS-NG flight lines in the conterminous US for 2014 - 2021.  Inset shows detail of flight lines in coastal Louisiana associated with the Delta-X project.",
                     "@type": "dcat:Distribution",
+                    "description": "Location of AVIRIS-NG flight lines in the conterminous US for 2014 - 2021.  Inset shows detail of flight lines in coastal Louisiana associated with the Delta-X project.",
+                    "downloadURL": "https://daac.ornl.gov/AVIRIS/guides/AVIRIS_FlightLine_Locator_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Location of AVIRIS-NG flight lines in the conterminous US for 2014 - 2021.  Inset shows detail of flight lines in coastal Louisiana associated with the Delta-X project.",
+            "graphic-preview-file": "https://daac.ornl.gov/AVIRIS/guides/AVIRIS_FlightLine_Locator_Fig1.jpg",
+            "identifier": "C2662360177-ORNL_CLOUD",
+            "issued": "2024-02-02",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "platform characteristics",
+                "sensor characteristics"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2140",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-02-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-171.85 9.2 118.95 84.36",
+            "temporal": "2006-04-11T00:00:00Z/2022-11-03T23:59:59Z",
             "theme": [
                 "AVIRIS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AVIRIS Facility Instruments: Flight Line Geospatial and Contextual Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1273652201-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Goddard Space Flight Center (GSFC). 2009-05-29. THIRN4L1CH67. Version 001. THIR/Nimbus-4 Level 1 Meteorological Radiation Data at 6.7 microns V001. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/THIRN4L1CH67_001.html. Digital Science Data.",
-            "issued": "2014-03-19",
-            "temporal": "1970-04-14T00:00:00Z/1971-03-25T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2014-03-19",
-            "keyword": [
-                "infrared wavelengths",
-                "earth science",
-                "spectral/engineering"
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
-            "identifier": "C1273652201-GES_DISC",
-            "description": "THIRN4L1CH67 is the Nimbus-4 Temperature-Humidity Infrared Radiometer (THIR) Level 1 Meteorological Radiation Data at 6.7 microns product contains radiances expressed in units of equivalent brightness temperature measured in the 6.7 micron channel. The data, originally written on IBM 360 machines, were recovered from magnetic tapes, also referred to as Nimbus Meteorological Radiation Tapes (NMRT-THIR). The data are archived in their original IBM 36-bit word proprietary format, also referred to as a binary TAP file.\n\nThe Nimbus-4 satellite was successfully launched on April 8, 1970. The THIR experiment on Nimbus-4 replaced the measurements made the HRIR and MRIR instruments flown on previous Nimbus satellites. The THIR instrument is a two channel high resolution scanning radiometer designed to perform two major functions:* The 11.5 micron channel provides both day and night cloud top or surface temperatures. The ground resolution at the sub-point is 8 km and operates day and night.* The 6.7 micron channel gives information on the moisture content of the upper troposphere and stratosphere and the location of jet streams and frontal systems. The water vapor channel has a resolution of the sub-point is 22 km and operates mostly at night.\n\nThe THIR Principal Investigator was Andrew W. McCulloch from NASA Goddard Space Flight Center. The Nimbus-4 THIR data are available from April 14, 1970 (day of year 104) through March 25, 1971 (day of year 84). The THIRN4L1CH115 product contains the 11.5 micron channel data.\n\nThis product was previously available from the NSSDC with the identifier ESAD-00071 (old ID 70-025A-02E).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "THIRN4L1CH67",
             "creator": "Goddard Space Flight Center (GSFC)",
-            "title": "THIR/Nimbus-4 Level 1 Meteorological Radiation Data at 6.7 microns V001 (THIRN4L1CH67) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/THIRN4L1CH67_001.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "THIRN4L1CH67 is the Nimbus-4 Temperature-Humidity Infrared Radiometer (THIR) Level 1 Meteorological Radiation Data at 6.7 microns product contains radiances expressed in units of equivalent brightness temperature measured in the 6.7 micron channel. The data, originally written on IBM 360 machines, were recovered from magnetic tapes, also referred to as Nimbus Meteorological Radiation Tapes (NMRT-THIR). The data are archived in their original IBM 36-bit word proprietary format, also referred to as a binary TAP file.\n\nThe Nimbus-4 satellite was successfully launched on April 8, 1970. The THIR experiment on Nimbus-4 replaced the measurements made the HRIR and MRIR instruments flown on previous Nimbus satellites. The THIR instrument is a two channel high resolution scanning radiometer designed to perform two major functions:* The 11.5 micron channel provides both day and night cloud top or surface temperatures. The ground resolution at the sub-point is 8 km and operates day and night.* The 6.7 micron channel gives information on the moisture content of the upper troposphere and stratosphere and the location of jet streams and frontal systems. The water vapor channel has a resolution of the sub-point is 22 km and operates mostly at night.\n\nThe THIR Principal Investigator was Andrew W. McCulloch from NASA Goddard Space Flight Center. The Nimbus-4 THIR data are available from April 14, 1970 (day of year 104) through March 25, 1971 (day of year 84). The THIRN4L1CH115 product contains the 11.5 micron channel data.\n\nThis product was previously available from the NSSDC with the identifier ESAD-00071 (old ID 70-025A-02E).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -182743,287 +182721,287 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/THIRN4L1CH67_001.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/THIRN4L1CH67_001.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus4_THIR_Level1/THIRN4L1CH67.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus4_THIR_Level1/THIRN4L1CH67.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=THIRN4L1CH67",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=THIRN4L1CH67",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus4_THIR_Level1/THIRN4L1CH67.001/doc/README.THIRN4L1.001.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus4_THIR_Level1/THIRN4L1CH67.001/doc/README.THIRN4L1.001.pdf",
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
-                    "mediaType": "application/gzip",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/DataCatalogNimbus4.tar.gz",
-                    "description": "Nimbus 4 Data Catalog",
                     "@type": "dcat:Distribution",
+                    "description": "Nimbus 4 Data Catalog",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/DataCatalogNimbus4.tar.gz",
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
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/N4_THIR_Ch67_Inventory.xlsx",
-                    "description": "N4 THIR Ch 6.7 Inventory",
                     "@type": "dcat:Distribution",
+                    "description": "N4 THIR Ch 6.7 Inventory",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/N4_THIR_Ch67_Inventory.xlsx",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/THIRN4L1CH67_001.png",
+            "identifier": "C1273652201-GES_DISC",
+            "issued": "2014-03-19",
+            "keyword": [
+                "infrared wavelengths",
+                "earth science",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1273652201-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2014-03-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "THIRN4L1CH67",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1970-04-14T00:00:00Z/1971-03-25T23:59:59.999Z",
             "theme": [
                 "Nimbus",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "THIR/Nimbus-4 Level 1 Meteorological Radiation Data at 6.7 microns V001 (THIRN4L1CH67) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0687-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-01T13:59:55.000 to 2015-04-01T15:38:20.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0687-v1.0_5bsm-ii9n",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0687-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0687-v1.0_5bsm-ii9n",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-01T13:59:55.000 to 2015-04-01T15:38:20.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0687 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0687 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SMODE-RVSUN",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "S-MODE Team. 2022-09-01. S-MODE Shipboard SUNA nitrate data Version 1. Version 1. S-MODE Shipboard SUNA nitrate data Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, S-MODE Project Data Manager, Fred Bingham. https://doi.org/10.5067/SMODE-RVSUN. http://podaac.jpl.nasa.gov/S-MODE.",
-            "issued": "2021-10-22",
-            "temporal": "2021-10-22T00:00:00Z/2021-10-23T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-10-22",
-            "keyword": [
-                "oceans",
-                "earth science",
-                "ocean chemistry"
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
-            "identifier": "C2832216518-POCLOUD",
-            "description": "This dataset contains Submersible Ultraviolet Nitrate Analyzer (SUNA) nitrate measurements taken during the Sub-Mesoscale Ocean Dynamics Experiment (S-MODE) pilot campaign conducted approximately 300 km offshore of San Francisco over two weeks in October 2021. S-MODE aims to understand how ocean dynamics acting on short spatial scales influence the vertical exchange of physical and biological variables in the ocean. SUNA is a standalone optical nitrate sensor that mounts onto the shipboard CTD rosette cast from the R/V Oceanus. The SUNA measurements are calibrated against bottle nutrient samples taken from the underway flow-through system on the ship and later analyzed with a Lachat Nutrient Analyzer. From the Lachat data, the average concentration of nitrate+nitrite are used for each sample. Data are available in netCDF format.",
-            "series-name": "S-MODE Shipboard SUNA nitrate data Version 1",
-            "graphic-preview-description": "Thumbnail",
             "creator": "S-MODE Team",
-            "title": "S-MODE L2 Shipboard SUNA nitrate data Version 1",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SMODE_LX_SHIPBOARD_SUNA_V1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset contains Submersible Ultraviolet Nitrate Analyzer (SUNA) nitrate measurements taken during the Sub-Mesoscale Ocean Dynamics Experiment (S-MODE) pilot campaign conducted approximately 300 km offshore of San Francisco over two weeks in October 2021. S-MODE aims to understand how ocean dynamics acting on short spatial scales influence the vertical exchange of physical and biological variables in the ocean. SUNA is a standalone optical nitrate sensor that mounts onto the shipboard CTD rosette cast from the R/V Oceanus. The SUNA measurements are calibrated against bottle nutrient samples taken from the underway flow-through system on the ship and later analyzed with a Lachat Nutrient Analyzer. From the Lachat data, the average concentration of nitrate+nitrite are used for each sample. Data are available in netCDF format.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSMODE-RVSUN",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSMODE-RVSUN",
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SMODE_LX_SHIPBOARD_SUNA_V1.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SMODE_LX_SHIPBOARD_SUNA_V1.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2110184932-POCLOUD",
-                    "description": "Browse and download granules over HTTPS using the virtual directories",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2110184932-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2110184932-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2110184932-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SMODE_LX_SHIPBOARD_SUNA_V1.jpg",
+            "identifier": "C2832216518-POCLOUD",
+            "issued": "2021-10-22",
+            "keyword": [
+                "oceans",
+                "earth science",
+                "ocean chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/SMODE-RVSUN",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-10-22",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "series-name": "S-MODE Shipboard SUNA nitrate data Version 1",
             "spatial": "-125.4 36.3 -122.9 38.1",
+            "temporal": "2021-10-22T00:00:00Z/2021-10-23T00:00:00Z",
             "theme": [
                 "S-MODE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "S-MODE L2 Shipboard SUNA nitrate data Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA/3314",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Froidevaux, L., Livesey, N., Read, W., and Fuller, R.. 2020-04-20. ML3DZHOCL. Version 004. MLS/Aura Level 3 Daily Binned Hypochlorous Acid (HOCl) Mixing Ratio on Zonal and Similar Grids V004. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA/3314. https://disc.gsfc.nasa.gov/datacollection/ML3DZHOCL_004.html. Digital Science Data.",
-            "issued": "2020-03-06",
-            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-03-06",
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
-            "identifier": "C1725336044-GES_DISC",
-            "description": "ML3DZHOCL is the EOS Aura Microwave Limb Sounder (MLS) daily binned on zonal and assorted vertical grids product for hypochlorous acid (HOCl) derived from radiances measured primarily by the 640 GHz radiometer. The data version is 4.2. Spatial coverage is near-global (-82 to +82 degrees latitude) at 4 degree latitude zonal increments. The recommended useful vertical range is from 10 to 2.15 hPa, and the vertical resolution is about 6 km. Users of the ML3DZOHCL data product should read chapter 4 and section 3.14 of the EOS MLS Level 2 Version 4 Quality Document for more information.\n\nThe data files contain one year of data and are archived in the netCDF4 format, which is also compatible with HDF5 readers and tools. Each file contains four group objects: lat vs pressure zonal mean, lat vs \"potential temperature\" zonal mean, \"equivalent latitude\" vs \"potential temperature\" zonal mean, and vortex average vs \"potential temperature\". These are further subdivided into groups with all valid, ascending orbit, descending orbit, daytime (SZA < 90), and nighttime (SZA > 110) profiles. Each group has a set of data (average, min, max, std dev, rms) and geolocation fields, grid attributes, and metadata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML3DZHOCL",
             "creator": "Froidevaux, L., Livesey, N., Read, W., and Fuller, R.",
-            "title": "MLS/Aura Level 3 Daily Binned Hypochlorous Acid (HOCl) Mixing Ratio on Zonal and Similar Grids V004 (ML3DZHOCL) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML3DZHOCL_004.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "ML3DZHOCL is the EOS Aura Microwave Limb Sounder (MLS) daily binned on zonal and assorted vertical grids product for hypochlorous acid (HOCl) derived from radiances measured primarily by the 640 GHz radiometer. The data version is 4.2. Spatial coverage is near-global (-82 to +82 degrees latitude) at 4 degree latitude zonal increments. The recommended useful vertical range is from 10 to 2.15 hPa, and the vertical resolution is about 6 km. Users of the ML3DZOHCL data product should read chapter 4 and section 3.14 of the EOS MLS Level 2 Version 4 Quality Document for more information.\n\nThe data files contain one year of data and are archived in the netCDF4 format, which is also compatible with HDF5 readers and tools. Each file contains four group objects: lat vs pressure zonal mean, lat vs \"potential temperature\" zonal mean, \"equivalent latitude\" vs \"potential temperature\" zonal mean, and vortex average vs \"potential temperature\". These are further subdivided into groups with all valid, ascending orbit, descending orbit, daytime (SZA < 90), and nighttime (SZA > 110) profiles. Each group has a set of data (average, min, max, std dev, rms) and geolocation fields, grid attributes, and metadata.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA%2F3314",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA%2F3314",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -183033,595 +183011,595 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML3DZHOCL_004.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML3DZHOCL_004.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level3/ML3DZHOCL.004/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level3/ML3DZHOCL.004/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level3/ML3DZHOCL.004/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level3/ML3DZHOCL.004/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML3DZHOCL_004",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML3DZHOCL_004",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML3DZHOCL_004.png",
+            "identifier": "C1725336044-GES_DISC",
+            "issued": "2020-03-06",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA/3314",
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
+            "series-name": "ML3DZHOCL",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MLS/Aura Level 3 Daily Binned Hypochlorous Acid (HOCl) Mixing Ratio on Zonal and Similar Grids V004 (ML3DZHOCL) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2309",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wang, D., G. Salter, and M.P. Lamb. 2023. Delta-X: Matlab Model for Wax Lake Delta Land Accretion. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2309",
-            "issued": "2024-10-31",
-            "temporal": "2021-03-20T00:00:00Z/2021-08-27T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-01",
-            "keyword": [
-                "biosphere",
-                "oceans",
-                "earth science",
-                "land surface",
-                "ecosystems",
-                "erosion/sedimentation",
-                "coastal processes"
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
-            "identifier": "C3281998337-ORNL_CLOUD",
             "description": "This dataset provides the Matlab sediment transport and land accretion model at Wax Lake Delta (WLD), Atchafalaya Basin, in coastal Louisiana. The data include the Matlab scripts that solve the advection and Exner equations to simulate the suspended sediment transport and accretion at WLD. The model requires modeled flow information from a separate ANUGA hydrodynamic model as inputs. For this study, ANUGA modeled flow information from the Delta-X Spring and Fall 2021 campaigns were used as inputs. The ANUGA output files are converted to variables used by this Matlab model using pre-processing tools. The main code calculates suspended sediment fluxes and accretion rates of mud and sand as a function of space and time. The cumulative sediment accretion from each campaign was then used to estimate an annualized land accretion map using a weighted-average formula presented. The final product, the one-yr upscaled land accretion map, is archived as a separate dataset.",
-            "graphic-preview-description": "The difference between modeled depth-average suspended sediment concentration (SSC) and AVIRIS-NG inferred surface suspended sediment concentration at the two flyover times: 2021-04-02 (left) and 2021-04-01 (right). Modeled values may be slightly larger because they are the depth-averaged concentration, whereas the AVIRIS-NG data reflect the near surface concentration.",
-            "title": "Delta-X: Matlab Model for Wax Lake Delta Land Accretion",
-            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/DeltaX_LandAccretion_WLD_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2309",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2309",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/deltax/DeltaX_LandAccretion_WLD/data/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/deltax/DeltaX_LandAccretion_WLD/data/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/DeltaX_LandAccretion_WLD_2309.zip",
-                    "description": "Collection bundle",
                     "@type": "dcat:Distribution",
+                    "description": "Collection bundle",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/DeltaX_LandAccretion_WLD_2309.zip",
+                    "mediaType": "application/zip",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_LandAccretion_WLD.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_LandAccretion_WLD.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2309",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2309",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/DeltaX_LandAccretion_WLD_2309.zip",
-                    "description": "Collection bundle",
                     "@type": "dcat:Distribution",
+                    "description": "Collection bundle",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/DeltaX_LandAccretion_WLD_2309.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/DeltaX_LandAccretion_WLD/comp/DeltaX_LandAccretion_WLD.pdf",
-                    "description": "Delta-X: Matlab Model for Wax Lake Delta Land Accretion: DeltaX_LandAccretion_WLD.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Delta-X: Matlab Model for Wax Lake Delta Land Accretion: DeltaX_LandAccretion_WLD.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/DeltaX_LandAccretion_WLD/comp/DeltaX_LandAccretion_WLD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_LandAccretion_WLD_Fig1.png",
-                    "description": "The difference between modeled depth-average suspended sediment concentration (SSC) and AVIRIS-NG inferred surface suspended sediment concentration at the two flyover times: 2021-04-02 (left) and 2021-04-01 (right). Modeled values may be slightly larger because they are the depth-averaged concentration, whereas the AVIRIS-NG data reflect the near surface concentration.",
                     "@type": "dcat:Distribution",
+                    "description": "The difference between modeled depth-average suspended sediment concentration (SSC) and AVIRIS-NG inferred surface suspended sediment concentration at the two flyover times: 2021-04-02 (left) and 2021-04-01 (right). Modeled values may be slightly larger because they are the depth-averaged concentration, whereas the AVIRIS-NG data reflect the near surface concentration.",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_LandAccretion_WLD_Fig1.png",
+                    "mediaType": "image/png",
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
+            "graphic-preview-description": "The difference between modeled depth-average suspended sediment concentration (SSC) and AVIRIS-NG inferred surface suspended sediment concentration at the two flyover times: 2021-04-02 (left) and 2021-04-01 (right). Modeled values may be slightly larger because they are the depth-averaged concentration, whereas the AVIRIS-NG data reflect the near surface concentration.",
+            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/DeltaX_LandAccretion_WLD_Fig1.png",
+            "identifier": "C3281998337-ORNL_CLOUD",
+            "issued": "2024-10-31",
+            "keyword": [
+                "biosphere",
+                "oceans",
+                "earth science",
+                "land surface",
+                "ecosystems",
+                "erosion/sedimentation",
+                "coastal processes"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2309",
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
             "spatial": "-91.58 29.39 -91.33 29.59",
+            "temporal": "2021-03-20T00:00:00Z/2021-08-27T23:59:59Z",
             "theme": [
                 "Delta-X",
                 "Model Archive",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Delta-X: Matlab Model for Wax Lake Delta Land Accretion"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amaven.rose.calibrated&version=1.9",
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
-                "mars atmosphere and volatile evolution mission",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This bundle contains the predicted and residual frequency received at Earth, and  transmitted from Earth.",
+            "identifier": "urn:nasa:pds:maven.rose.calibrated",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars atmosphere and volatile evolution mission",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amaven.rose.calibrated&version=1.9",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:maven.rose.calibrated",
-            "description": "This bundle contains the predicted and residual frequency received at Earth, and  transmitted from Earth.",
-            "title": "MAVEN ROSE Calibrated Data Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MAVEN ROSE Calibrated Data Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-SUN-RSS-1-ROCC-V1.0",
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
-                "mars global surveyor"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Mars Global Surveyor (MGS) Solar Conjunction Raw Data Archive is a time-ordered collection of raw data acquired during the Solar Conjunction in 2000, while MGS was in its Mars Mapping (MAP) mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-sun-rss-1-rocc-v1.0_5c2k-p9sf",
+            "issued": "2018-06-26",
+            "keyword": [
+                "sun",
+                "mars global surveyor"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-SUN-RSS-1-ROCC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-sun-rss-1-rocc-v1.0_5c2k-p9sf",
-            "description": "The Mars Global Surveyor (MGS) Solar Conjunction Raw Data Archive is a time-ordered collection of raw data acquired during the Solar Conjunction in 2000, while MGS was in its Mars Mapping (MAP) mission phase.",
-            "title": "MGS SOLAR CONJUNCTION RAW DATA SET - ROCC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MGS SOLAR CONJUNCTION RAW DATA SET - ROCC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/792/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-06-19",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "nasa",
-                "dashlink",
-                "ames"
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
-            "identifier": "DASHLINK_792",
             "description": "The focus of this work is the analysis of different degradation phenomena based on thermal overstress and electrical overstress accelerated aging systems and the use of accelerated aging techniques for prognostics algorithm development. Results on thermal overstress and electrical overstress experiments are presented. In addition, preliminary results toward the development of physics-based degradation models are presented focusing on the electrolyte evaporation failure mechanism. An empirical degradation model based on percentage capacitance loss under electrical overstress is presented and used in: (i) a Bayesian-based implementation of model-based prognostics using a discrete Kalman filter for health state estimation, and (ii) a dynamic system representation of the degradation model for forecasting and remaining useful life (RUL) estimation. A leave-one-out validation methodology is used to assess the validity of the methodology under the small sample size constrain.\r\nThe results observed on the RUL estimation are consistent through the validation tests comparing relative accuracy and prediction error. It has been observed that the inaccuracy of the model to represent the change in degradation behavior observed at the end of the test data is consistent throughout the validation tests, indicating the need of a more detailed degradation model or the use of an algorithm that could estimate model parameters on-line. Based on the observed degradation process under different stress intensity with rest periods, the need for more sophisticated degradation models is further supported. The current degradation model does not represent the capacitance recovery over rest periods following an accelerated aging stress period.",
-            "title": "Accelerated Aging in Electrolytic Capacitors for Prognostics",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2012_RAMS_Capacitor.pdf",
-                    "description": "2012_RAMS_Capacitor.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "2012_RAMS_Capacitor.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2012_RAMS_Capacitor.pdf",
+                    "mediaType": "application/pdf",
                     "title": "2012_RAMS_Capacitor.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_792",
+            "issued": "2013-06-19",
+            "keyword": [
+                "nasa",
+                "dashlink",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/792/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Accelerated Aging in Electrolytic Capacitors for Prognostics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Terra-Aqua/CERES/FLUXBYCLDTYP-DAY_L3.004A",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2020-06-17. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/Terra-Aqua/CERES/FLUXBYCLDTYP-DAY_L3.004A.",
-            "issued": "2019-03-12",
-            "temporal": "2002-07-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-03-12",
-            "keyword": [
-                "clouds",
-                "atmospheric radiation",
-                "atmosphere",
-                "ngda",
-                "national geospatial data asset",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DAVID Doelling",
                 "hasEmail": "mailto:david.r.doelling@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1886238385-LARC_ASDC",
             "description": "CER_FluxByCldTyp-Day_Terra-Aqua-MODIS_Edition4A is the Clouds and the Earth's Radiant Energy System (CERES) Daily Daytime Mean Regionally Averaged Terra and Aqua Top-of-Atmosphere (TOA) Fluxes and associated cloud properties stratified by optical depth and effective pressure Edition4A data product. Data was collected using CERES Flight Model 1 (FM1), FM2, and Moderate-Resolution Imaging Spectroradiometer (MODIS) on Terra along with CERES-FM3, FM4, and MODIS on Aqua. Data collection is ongoing. \r\n\r\nCER_FluxByCldTyp-Day_Terra-Aqua-MODIS_Edition4A provides instantaneous daytime CERES fluxes and CERES-MODIS cloud properties that have been spatially gridded into 1\u00b0 regions along both the Terra and Aqua ground tracks where the TOA fluxes and cloud properties have been stratified by six cloud optical depth bins and seven cloud effective pressure layers. The CERES FluxByCldTyp-Day Edition4A product uses Single Scanner Footprint (SSF) Edition4A footprint data as input. Within each footprint, all 1-km pixel-level MODIS-retrieved cloud properties are stratified into three possible sub-footprint components: two cloud layers and a clear portion. For each sub-footprint component, the MODIS channel radiances are converted to broadband (BB) radiances. The CERES angular directional models are then applied to obtain BB fluxes. Each of the CERES sub-footprint cloud layers and associated fluxes are assigned to one of the 42 cloud types, similarly to the stratification process in the CldTypHist product. FluxByCloudTyp is an hourly instantaneous gridded daytime- only product with global extent. Each netCDF4 file covers a single day.\r\n\r\nCERES is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions are a follow-on to the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument, protoflight model (PFM), was launched on November 27, 1997 as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the Earth Observing System (EOS) flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board Earth Observing System (EOS) Aqua on May 4, 2002. The CERES FM5 instrument was launched on board the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The newest CERES instrument (FM6) was launched on board the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite, now called NOAA-20, on November 18, 2017.",
-            "title": "CERES Daily Daytime Mean Regionally Averaged Terra and Aqua TOA Fluxes and Associated Cloud Properties Stratified by Optical Depth and Effective Pressure Edition4A",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra-Aqua%2FCERES%2FFLUXBYCLDTYP-DAY_L3.004A",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra-Aqua%2FCERES%2FFLUXBYCLDTYP-DAY_L3.004A",
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
-                    "downloadURL": "https://doi.org/10.5067/Terra-Aqua/CERES/FLUXBYCLDTYP-DAY_L3.004A",
-                    "description": "DOI data set landing page for CER_FluxByCldTyp-Day_Terra-Aqua-MODIS_Edition4A",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CER_FluxByCldTyp-Day_Terra-Aqua-MODIS_Edition4A",
+                    "downloadURL": "https://doi.org/10.5067/Terra-Aqua/CERES/FLUXBYCLDTYP-DAY_L3.004A",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/quality_summaries/CERES_FluxByCldTyp_Ed4A_DQS_055292020.pdf",
-                    "description": "Quality Summary: CERES_FluxByCldTyp-Day/Month_Ed4A (5/29/2020)",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Summary: CERES_FluxByCldTyp-Day/Month_Ed4A (5/29/2020)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/quality_summaries/CERES_FluxByCldTyp_Ed4A_DQS_055292020.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product quality assessment"
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
-                    "downloadURL": "https://ceres.larc.nasa.gov/documents/publications/pdfs/CERES_pubs_1993-present.pdf",
-                    "description": "CERES publications by year - 1993 through present",
                     "@type": "dcat:Distribution",
+                    "description": "CERES publications by year - 1993 through present",
+                    "downloadURL": "https://ceres.larc.nasa.gov/documents/publications/pdfs/CERES_pubs_1993-present.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
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
-                    "downloadURL": "https://www.unidata.ucar.edu/software/netcdf/",
-                    "description": "Unidata Overview of Network Common Data Form (NetCDF)",
                     "@type": "dcat:Distribution",
+                    "description": "Unidata Overview of Network Common Data Form (NetCDF)",
+                    "downloadURL": "https://www.unidata.ucar.edu/software/netcdf/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1886238385-LARC_ASDC",
-                    "description": "Earthdata Search for CER_FluxByCldTyp-Day_Terra-Aqua-MODIS_Edition4A (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CER_FluxByCldTyp-Day_Terra-Aqua-MODIS_Edition4A (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1886238385-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
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
-                    "downloadURL": "https://ceres.larc.nasa.gov/data/#fluxbycldtyp-level-3",
-                    "description": "CERES Data Page",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Data Page",
+                    "downloadURL": "https://ceres.larc.nasa.gov/data/#fluxbycldtyp-level-3",
+                    "mediaType": "text/html",
                     "title": "Subset this dataset using a web based subsetter"
                 },
                 {
@@ -183631,66 +183609,64 @@
                     "title": "Download this dataset through the CERES Ordering Tool"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/FluxByCldTyp-Day/Terra-Aqua-MODIS_Edition4A/",
-                    "description": "ASDC Direct Data Download for CER_FluxByCldTyp-Day_Terra-Aqua-MODIS_Edition4A",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CER_FluxByCldTyp-Day_Terra-Aqua-MODIS_Edition4A",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/FluxByCldTyp-Day/Terra-Aqua-MODIS_Edition4A/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/FluxByCldTyp-Day/Terra-Aqua-MODIS_Edition4A/contents.html",
-                    "description": "OPeNDAP data access for CER_FluxByCldTyp-Day_Terra-Aqua-MODIS_Edition4A",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CER_FluxByCldTyp-Day_Terra-Aqua-MODIS_Edition4A",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/FluxByCldTyp-Day/Terra-Aqua-MODIS_Edition4A/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1886238385-LARC_ASDC",
+            "issued": "2019-03-12",
+            "keyword": [
+                "clouds",
+                "atmospheric radiation",
+                "atmosphere",
+                "ngda",
+                "national geospatial data asset",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Terra-Aqua/CERES/FLUXBYCLDTYP-DAY_L3.004A",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-03-12",
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
+            "title": "CERES Daily Daytime Mean Regionally Averaged Terra and Aqua TOA Fluxes and Associated Cloud Properties Stratified by Optical Depth and Effective Pressure Edition4A"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-06-05",
-            "temporal": "2021-06-05T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "space",
-                "station",
-                "coordinates",
-                "location",
-                "topo",
-                "ephemeris",
-                "international",
-                "iss",
-                "trajectory",
-                "coords"
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
-            "identifier": "nasa-iss-data_2021-06-05_5cbw-jpgh",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2021-06-05",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -183813,90 +183789,90 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2021-06-05_5cbw-jpgh",
+            "issued": "2021-06-05",
+            "keyword": [
+                "space",
+                "station",
+                "coordinates",
+                "location",
+                "topo",
+                "ephemeris",
+                "international",
+                "iss",
+                "trajectory",
+                "coords"
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
+            "temporal": "2021-06-05T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2021-06-05"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-SDC-3-PLUTO-V2.0",
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
-                "dust",
-                "new horizons"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Calibrated data taken by the New Horizons         Student Dust Counter                                                   instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 2.0 of this data set.                    This data set contains SDC observations taken during the                 the Approach (Jan-Jul, 2015), Encounter and Departure mission            sub-phases, including flyby observations taken on 14.July, 2015,         and including data through 2015 and into January, 2016; the data are     limited to those downlinked from the spacecraft as of the end of         January, 2016.  The rest of the downlinked data for this mission         phase will be delivered in a future data set.                            This is version 2.0 of this data set.  Changes since version 1.0         include data downlinked between the end of July, 2015 and the end of     January, 2016.  Also, updates were made to the documentation and         catalog files, primarily to resolve liens from the V1.0 peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-sdc-3-pluto-v2.0_5cgx-gh5g",
+            "issued": "2021-05-21",
+            "keyword": [
+                "dust",
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-SDC-3-PLUTO-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-sdc-3-pluto-v2.0_5cgx-gh5g",
-            "description": "This data set contains Calibrated data taken by the New Horizons         Student Dust Counter                                                   instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 2.0 of this data set.                    This data set contains SDC observations taken during the                 the Approach (Jan-Jul, 2015), Encounter and Departure mission            sub-phases, including flyby observations taken on 14.July, 2015,         and including data through 2015 and into January, 2016; the data are     limited to those downlinked from the spacecraft as of the end of         January, 2016.  The rest of the downlinked data for this mission         phase will be delivered in a future data set.                            This is version 2.0 of this data set.  Changes since version 1.0         include data downlinked between the end of July, 2015 and the end of     January, 2016.  Also, updates were made to the documentation and         catalog files, primarily to resolve liens from the V1.0 peer review.",
-            "title": "NEW HORIZONS                            \n      SDC PLUTO ENCOUNTER                                                     \n      CALIBRATED V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS                            \n      SDC PLUTO ENCOUNTER                                                     \n      CALIBRATED V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-08-15",
-            "temporal": "2021-08-15T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "coordinates",
-                "ephemeris",
-                "location",
-                "space",
-                "iss",
-                "station",
-                "topo",
-                "international",
-                "coords",
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
-            "identifier": "nasa-iss-data_2021-08-15_5ci6-2yti",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2021-08-15",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -184019,720 +183995,746 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2021-08-15_5ci6-2yti",
+            "issued": "2021-08-15",
+            "keyword": [
+                "coordinates",
+                "ephemeris",
+                "location",
+                "space",
+                "iss",
+                "station",
+                "topo",
+                "international",
+                "coords",
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
+            "temporal": "2021-08-15T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2021-08-15"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TIGR4-V1.0",
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
+            "description": "The Cassini Radio Science Titan Gravity Science Experiment (TIGR4) Raw Data Archive is a time-ordered collection of radio science raw data acquired on April 29, May 1, 19, and 21, 2006 during the Tour subphase of the Cassini mission. DATA_SET_DESC =",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tigr4-v1.0_5cki-sypy",
+            "issued": "2021-05-21",
+            "keyword": [
+                "cassini-huygens",
+                "titan"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TIGR4-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tigr4-v1.0_5cki-sypy",
-            "description": "The Cassini Radio Science Titan Gravity Science Experiment (TIGR4) Raw Data Archive is a time-ordered collection of radio science raw data acquired on April 29, May 1, 19, and 21, 2006 during the Tour subphase of the Cassini mission. DATA_SET_DESC =",
-            "title": "CASSINI RSS RAW DATA SET - TIGR4 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI RSS RAW DATA SET - TIGR4 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/MEASURES/GPCP/DATA305",
             "citation": "Huffman, G.J., A. Behrangi, D.T. Bolvin, E.J. Nelkin. Huffman, G.J., A. Behrangi, D.T. Bolvin, E.J. Nelkin. 2022-02-02. GPCPDAY. Version 3.2. GPCP Version 3.2 Daily Precipitation Data Set. Greenbelt, Maryland, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/MEASURES/GPCP/DATA305. https://disc.gsfc.nasa.gov/datacollection/GPCPDAY_3.2.html. Digital Science Data.",
-            "issued": "2022-02-02",
-            "temporal": "2000-06-01T00:00:00Z/2021-09-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-02",
-            "keyword": [
-                "atmosphere",
-                "precipitation",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "GEORGE HUFFMAN",
                 "hasEmail": "mailto:George.J.Huffman@nasa.gov"
             },
+            "creator": "Huffman, G.J., A. Behrangi, D.T. Bolvin, E.J. Nelkin",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2211141201-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Version 3.2 is the current version. Older versions have been superseded by Version 3.2.\n\nThe Global Precipitation Climatology Project (GPCP) is the precipitation component of an internationally coordinated set of (mainly) satellite-based global products dealing with the Earth's water and energy cycles, under the auspices of the Global Water and Energy Exchange (GEWEX) Data and Assessment Panel (GDAP) of the World Climate Research Program.  As the follow on to the GPCP Version 1.3 One Degree Daily product, GPCP Version 3 (GPCP V3.2) seeks to continue the long, homogeneous precipitation record using modern merging techniques and input data sets.  The GPCPV3 suite currently consists of the 0.5-degree Monthly and 0.5-degree Daily. Additional products may be added, which consist of (1) 0.5-degree pentad and (2) 0.1-degree 3-hourly.  All GPCPV3 products will be internally consistent.  The Daily product spans June 2000-December 2020. Inputs consist of GPM IMERG in the span 55\u00b0N-S, and TOVS/AIRS estimates, adjusted climatologically to IMERG, outside 55\u00b0N-S.  The Daily estimates are scaled to approximately sum to the Monthly value at each 0.5\u00b0 grid box.  In addition to the final precipitation field, probability of liquid phase estimates are provided globally.",
-            "editor": "Huffman, G.J., A. Behrangi, D.T. Bolvin, E.J. Nelkin",
-            "release-place": "Greenbelt, Maryland, USA",
-            "series-name": "GPCPDAY",
-            "creator": "Huffman, G.J., A. Behrangi, D.T. Bolvin, E.J. Nelkin",
-            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a Web-based tool that allows users to interactively visualize and analyze data.",
-            "title": "GPCP Precipitation Level 3 Daily 0.5-Degree V3.2 (GPCPDAY) at GES DISC",
-            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=GPCP%20daily%20V3.2",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FGPCP%2FDATA305",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FGPCP%2FDATA305",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GPCPDAY_V32.png",
-                    "description": "A sample map for precip",
                     "@type": "dcat:Distribution",
+                    "description": "A sample map for precip",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GPCPDAY_V32.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPCPDAY_3.2.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPCPDAY_3.2.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/GPCP/GPCPDAY.3.2/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/GPCP/GPCPDAY.3.2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPCPDAY_3.2",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPCPDAY_3.2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=GPCP%20daily%20V3.2",
-                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a Web-based tool that allows users to interactively visualize and analyze data.",
                     "@type": "dcat:Distribution",
+                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a Web-based tool that allows users to interactively visualize and analyze data.",
+                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=GPCP%20daily%20V3.2",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through GIOVANNI"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/GPCP/GPCPDAY.3.2/",
-                    "description": "Access to the data via OPeNDAP protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access to the data via OPeNDAP protocol",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/GPCP/GPCPDAY.3.2/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/GPCP/GPCPDAY.3.2/doc/README.GPCPV3.2_Daily.pdf",
-                    "description": "README document",
                     "@type": "dcat:Distribution",
+                    "description": "README document",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/GPCP/GPCPDAY.3.2/doc/README.GPCPV3.2_Daily.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/GPCP_ATBD_V3.2_Daily.pdf",
-                    "description": "GPCP_ATBD_V3.2_Daily.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "GPCP_ATBD_V3.2_Daily.pdf",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/GPCP_ATBD_V3.2_Daily.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/Release_Notes.GPCPV3.2.pdf",
-                    "description": "GPCP V3.2 Release Notes",
                     "@type": "dcat:Distribution",
+                    "description": "GPCP V3.2 Release Notes",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/Release_Notes.GPCPV3.2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 }
             ],
+            "editor": "Huffman, G.J., A. Behrangi, D.T. Bolvin, E.J. Nelkin",
+            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a Web-based tool that allows users to interactively visualize and analyze data.",
+            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=GPCP%20daily%20V3.2",
+            "identifier": "C2211141201-GES_DISC",
+            "issued": "2022-02-02",
+            "keyword": [
+                "atmosphere",
+                "precipitation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/GPCP/DATA305",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-02-02",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, Maryland, USA",
+            "series-name": "GPCPDAY",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-06-01T00:00:00Z/2021-09-30T23:59:59.999Z",
             "theme": [
                 "MEaSUREs",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPCP Precipitation Level 3 Daily 0.5-Degree V3.2 (GPCPDAY) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MCD15A3H.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MCD15A3H.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-03-01",
-            "temporal": "2002-07-04T00:00:00Z/2024-06-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-03-01",
-            "keyword": [
-                "vegetation",
-                "earth science",
-                "biosphere",
-                "ngda",
-                "national geospatial data asset"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ranga Myneni",
                 "hasEmail": "mailto:rmyneni@bu.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
-            "identifier": "C2343110937-LPCLOUD",
             "description": "The MCD15A3H Version 6.1 Moderate Resolution Imaging Spectroradiometer (MODIS) Level 4, Combined Fraction of Photosynthetically Active Radiation (FPAR), and Leaf Area Index (LAI) product is a 4-day composite data set with 500 meter pixel size. The algorithm chooses the best pixel available from all the acquisitions of both MODIS sensors located on NASA\u2019s Terra and Aqua satellites from within the 4-day period.\n\nLAI is defined as the one-sided green leaf area per unit ground area in broadleaf canopies and as one-half the total needle surface area per unit ground area in coniferous canopies. FPAR is defined as the fraction of incident photosynthetically active radiation (400-700 nm) absorbed by the green elements of a vegetation canopy.\n\nThe LAI product has attained stage 2 (https://landweb.modaps.eosdis.nasa.gov/cgi-bin/QA_WWW/newPage.cgi?fileName=maturity) validation and the FPAR product has attained stage 1 (https://landweb.modaps.eosdis.nasa.gov/cgi-bin/QA_WWW/newPage.cgi?fileName=maturity) validation.\n\nImprovements/Changes from Previous Versions\n\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "graphic-preview-description": "Browse image for Earthdata Search",
-            "title": "MODIS/Terra+Aqua Leaf Area Index/FPAR 4-Day L4 Global 500m SIN Grid V061",
-            "graphic-preview-file": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/MCD15A3H.061/MCD15A3H.A2022281.h19v04.061.2022287191333/BROWSE.MCD15A3H.A2022281.h19v04.061.2022287191333.1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD15A3H.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD15A3H.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD15A3H.061/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2343110937-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2343110937-LPCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD15A3H.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD15A3H.061",
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
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/926/MOD15_User_Guide_V61.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/926/MOD15_User_Guide_V61.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/90/MOD15_ATBD.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/90/MOD15_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MCD15A3H",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MCD15A3H",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/MODLAND_val.html",
-                    "description": "The LAI product has attained stage 2 validation and the FPAR product has attained stage 1 validation.",
                     "@type": "dcat:Distribution",
+                    "description": "The LAI product has attained stage 2 validation and the FPAR product has attained stage 1 validation.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/MODLAND_val.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD15",
-                    "description": "Further details regarding MODIS land product validation for the LAI/FPAR data products are available from the MODIS land team validation site.",
                     "@type": "dcat:Distribution",
+                    "description": "Further details regarding MODIS land product validation for the LAI/FPAR data products are available from the MODIS land team validation site.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD15",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP131/MOTA/MCD15A3H.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP131/MOTA/MCD15A3H.061/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/MCD15A3H.061/MCD15A3H.A2022281.h19v04.061.2022287191333/BROWSE.MCD15A3H.A2022281.h19v04.061.2022287191333.1.jpg",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/MCD15A3H.061/MCD15A3H.A2022281.h19v04.061.2022287191333/BROWSE.MCD15A3H.A2022281.h19v04.061.2022287191333.1.jpg",
+                    "mediaType": "image/jpeg",
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
+            "graphic-preview-file": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/MCD15A3H.061/MCD15A3H.A2022281.h19v04.061.2022287191333/BROWSE.MCD15A3H.A2022281.h19v04.061.2022287191333.1.jpg",
+            "identifier": "C2343110937-LPCLOUD",
+            "issued": "2021-03-01",
+            "keyword": [
+                "vegetation",
+                "earth science",
+                "biosphere",
+                "ngda",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MCD15A3H.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-03-01",
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
                 "Terra",
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Terra+Aqua Leaf Area Index/FPAR 4-Day L4 Global 500m SIN Grid V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-EXT3-67PCHURYUMOV-M35-V3.0",
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
+            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 3 mission phase, covering the period from 2016-09-26T06:40:00.000 to 2016-10-01T00:00:00.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-ext3-67pchuryumov-m35-v3.0_5ctq-42eg",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-EXT3-67PCHURYUMOV-M35-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-ext3-67pchuryumov-m35-v3.0_5ctq-42eg",
-            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 3 mission phase, covering the period from 2016-09-26T06:40:00.000 to 2016-10-01T00:00:00.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 3 EXT3-MTP035 RDR V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 3 EXT3-MTP035 RDR V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2345",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hunka, N., L. Duncanson, J. Armston, R.O. Dubayah, S.P. Healey, M. Santoro, P. May, A. Araza, C. Bourgain, P.M. Montesano, C.S. Neigh, H. Grantham, V. Potapov, S. Turubanova, A. Tyukavina, J. Richter, N. Harris, M. Urbazaev, A. Pascual, D. Requena Suarez, M. Herold, B. Poulter, S.N. Wilson, G. Grassi, S. Federici, M.J. Sanz Sanchez, and J. Melo. 2024. Classification of Global Forests for IPCC Aboveground Biomass Tier 1 Estimates, 2020. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2345",
-            "issued": "2024-06-12",
-            "temporal": "2020-01-01T00:00:00Z/2020-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-13",
-            "keyword": [
-                "ecosystems",
-                "land surface",
-                "biosphere",
-                "land use/land cover",
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
-            "identifier": "C3091153379-ORNL_CLOUD",
             "description": "This dataset provides classes of global forests delineated by status/condition in 2020 at approximately 30-m resolution. The data support generating Tier 1 estimates for Aboveground dry woody Biomass Density (AGBD) in natural forests in the 2019 Refinement to the 2006 IPCC Guidelines for National Greenhouse Gas Inventories. Forest classes include primary, young secondary (<=20 years), and old secondary forests (>20 years). Classification was based on a Boolean combination of a suite of existing Earth Observation (EO) products of forest tree cover, height, age, and land use classification layers representing years 2000 to 2020. This forest status/condition classification prioritizes the reduction of potential errors of commission in the delineations by minimizing the inclusion of ambiguous pixels. Hence, it provides a conservative estimate of global forest area, identifying approximately 3.26 billion ha of forests worldwide. The classification was created on the collaborative open-science cloud-computing system, the ESA-NASA Multi-mission Analysis and Algorithm Platform (MAAP). The data are provided in cloud-optimized GeoTIFF format.",
-            "graphic-preview-description": "Status/condition of natural forests for 2020.",
-            "title": "Classification of Global Forests for IPCC Aboveground Biomass Tier 1 Estimates, 2020",
-            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/CMS_Global_Forest_Age_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2345",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2345",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/cms/CMS_Global_Forest_Age/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/cms/CMS_Global_Forest_Age/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_Global_Forest_Age.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_Global_Forest_Age.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2345",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2345",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/CMS_Global_Forest_Age/comp/CMS_Global_Forest_Age.pdf",
-                    "description": "Classification of Global Forests for IPCC Aboveground Biomass Tier 1 Estimates, 2020: CMS_Global_Forest_Age.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Classification of Global Forests for IPCC Aboveground Biomass Tier 1 Estimates, 2020: CMS_Global_Forest_Age.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/CMS_Global_Forest_Age/comp/CMS_Global_Forest_Age.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_Global_Forest_Age_Fig1.jpg",
-                    "description": "Status/condition of natural forests for 2020.",
                     "@type": "dcat:Distribution",
+                    "description": "Status/condition of natural forests for 2020.",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_Global_Forest_Age_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Status/condition of natural forests for 2020.",
+            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/CMS_Global_Forest_Age_Fig1.jpg",
+            "identifier": "C3091153379-ORNL_CLOUD",
+            "issued": "2024-06-12",
+            "keyword": [
+                "ecosystems",
+                "land surface",
+                "biosphere",
+                "land use/land cover",
+                "vegetation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2345",
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
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2020-01-01T00:00:00Z/2020-12-31T23:59:59Z",
             "theme": [
                 "CMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Classification of Global Forests for IPCC Aboveground Biomass Tier 1 Estimates, 2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1538",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Dubayah, R.O., A. Swatantran, W. Huang, L. Duncanson, K. Johnson, H. Tang, J.O. Dunne, and G.C. Hurtt. 2018. LiDAR Derived Biomass, Canopy Height and Cover for Tri-State (MD, PA, DE) Region, V2. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1538",
-            "issued": "2018-11-08",
-            "temporal": "2004-01-01T00:00:00Z/2014-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
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
-            "identifier": "C2398117778-ORNL_CLOUD",
             "description": "This dataset provides 30-meter gridded estimates of aboveground biomass (AGB), forest canopy height, and canopy coverage for Maryland, Pennsylvania, and Delaware in 2011. Leaf-off LiDAR data were combined with high-resolution leaf-on agricultural imagery in a model-based stratification that was used to select 848 sampling sites for AGB estimation. Field-based estimates were then related to LiDAR height and volume metrics through random forest regression models across three physiographic regions. Spatial errors were estimated at the pixel level using standard prediction intervals to assess the accuracy of the modeling approach. Estimates of biomass were further validated against the permanent network of FIA plots and compared with existing coarse resolution national biomass maps.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LiDAR Derived Biomass, Canopy Height and Cover for Tri-State (MD, PA, DE) Region, V2",
-            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/CMS_LiDAR_Biomass_MD_PA_DE_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1538",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1538",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/cms/CMS_LiDAR_Biomass_MD_PA_DE/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/cms/CMS_LiDAR_Biomass_MD_PA_DE/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_LiDAR_Biomass_MD_PA_DE.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_LiDAR_Biomass_MD_PA_DE.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1538",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1538",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/CMS_LiDAR_Biomass_MD_PA_DE/comp/CMS_LiDAR_Biomass_MD_PA_DE.pdf",
-                    "description": "LiDAR Derived Biomass, Canopy Height and Cover for Tri-State (MD, PA, DE) Region, V2: CMS_LiDAR_Biomass_MD_PA_DE.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "LiDAR Derived Biomass, Canopy Height and Cover for Tri-State (MD, PA, DE) Region, V2: CMS_LiDAR_Biomass_MD_PA_DE.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/CMS_LiDAR_Biomass_MD_PA_DE/comp/CMS_LiDAR_Biomass_MD_PA_DE.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_LiDAR_Biomass_MD_PA_DE_Fig1.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_LiDAR_Biomass_MD_PA_DE_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1538",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1538",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/CMS_LiDAR_Biomass_MD_PA_DE_Fig1.png",
+            "identifier": "C2398117778-ORNL_CLOUD",
+            "issued": "2018-11-08",
+            "keyword": [
+                "earth science",
+                "biosphere",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1538",
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
             "spatial": "-81.23 37.8 -74.02 42.71",
+            "temporal": "2004-01-01T00:00:00Z/2014-12-31T23:59:59Z",
             "theme": [
                 "CMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LiDAR Derived Biomass, Canopy Height and Cover for Tri-State (MD, PA, DE) Region, V2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=FEXP-E-RMTR%2FTHRM-3-RDR-TEMPERATURE-V1.0",
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
-                "geologic remote sensing field experiment"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "As part of GRSFE the directional variations in thermal emission of different surfaces were investigated. Results were obtained using hand-held thermistor probes (to determine local kinetic temperature) and a ground-based, hand-held infrared radiometer (to determine scene-averaged infrared brightness temperature from multiple view angles).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.fexp-e-rmtr-thrm-3-rdr-temperature-v1.0_5cwn-32bk",
+            "issued": "2021-05-21",
+            "keyword": [
+                "earth",
+                "geologic remote sensing field experiment"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=FEXP-E-RMTR%2FTHRM-3-RDR-TEMPERATURE-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.fexp-e-rmtr-thrm-3-rdr-temperature-v1.0_5cwn-32bk",
-            "description": "As part of GRSFE the directional variations in thermal emission of different surfaces were investigated. Results were obtained using hand-held thermistor probes (to determine local kinetic temperature) and a ground-based, hand-held infrared radiometer (to determine scene-averaged infrared brightness temperature from multiple view angles).",
-            "title": "FIELD EXP E RANGER II PLUS RDMT & THRM CALIB RDR TEMP V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "FIELD EXP E RANGER II PLUS RDMT & THRM CALIB RDR TEMP V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Y4W64RE5RWBF",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMAPVEX16 Manitoba CropScan Data V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/Y4W64RE5RWBF.",
-            "issued": "2016-06-13",
-            "temporal": "2016-06-13T00:00:00Z/2016-07-12T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-07-12",
-            "keyword": [
-                "land surface",
-                "earth science",
-                "surface radiative properties"
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
-            "identifier": "C1452805085-NSIDC_ECS",
             "description": "This data set contains CropScan observations (solar irradiance and incidence angle) collected for the Soil Moisture Active Passive Validation Experiment 2016 Manitoba (SMAPVEX16 Manitoba) campaign.",
-            "title": "SMAPVEX16 Manitoba CropScan Data V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FY4W64RE5RWBF",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FY4W64RE5RWBF",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_VAL/SV16M_CRS.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_VAL/SV16M_CRS.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1452805085-NSIDC_ECS&m=45.6064453125%21-98.0771484375%215%211%210%210%2C2&q=sv16m_crs&ok=sv16m_crs",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1452805085-NSIDC_ECS&m=45.6064453125%21-98.0771484375%215%211%210%210%2C2&q=sv16m_crs&ok=sv16m_crs",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SV16M_CRS/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SV16M_CRS/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_VAL/SV16M_CRS.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_VAL/SV16M_CRS.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1452805085-NSIDC_ECS&m=45.6064453125%21-98.0771484375%215%211%210%210%2C2&q=sv16m_crs&ok=sv16m_crs",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1452805085-NSIDC_ECS&m=45.6064453125%21-98.0771484375%215%211%210%210%2C2&q=sv16m_crs&ok=sv16m_crs",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SV16M_CRS/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SV16M_CRS/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/Y4W64RE5RWBF",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/Y4W64RE5RWBF",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/Y4W64RE5RWBF",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/Y4W64RE5RWBF",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1452805085-NSIDC_ECS",
+            "issued": "2016-06-13",
+            "keyword": [
+                "land surface",
+                "earth science",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/Y4W64RE5RWBF",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2016-07-12",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-98.098417 49.38533 -97.756264 49.761171",
+            "temporal": "2016-06-13T00:00:00Z/2016-07-12T23:59:59.999Z",
             "theme": [
                 "SMAPVEX16 Manitoba",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMAPVEX16 Manitoba CropScan Data V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SS-RSS-1-SCC5-V1.0",
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
-                "cassini-huygens"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Cassini Radio Science Solar Corona Characterization Experiment (SCC5) Raw Data Archive is a time-ordered collection of radio science raw data acquired from September 2 to September 30, 2009 during the Cassini Extended Mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ss-rss-1-scc5-v1.0_5cyp-rxec",
+            "issued": "2018-06-26",
+            "keyword": [
+                "solar system",
+                "cassini-huygens"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SS-RSS-1-SCC5-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ss-rss-1-scc5-v1.0_5cyp-rxec",
-            "description": "The Cassini Radio Science Solar Corona Characterization Experiment (SCC5) Raw Data Archive is a time-ordered collection of radio science raw data acquired from September 2 to September 30, 2009 during the Cassini Extended Mission.",
-            "title": "CASSINI RSS RAW DATA SET - SCC5 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI RSS RAW DATA SET - SCC5 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-C-COMPIL-5-LIGHTCURVES-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This is a dataset that compiles the data from various papers, which reported observations of brightness changes in comets that allowed to produce the comet lightcurves. Specifically, the data were based on the references in the paper by Samarasinha et al. (2004), i.e. they are those lightcurves, which were used to find out the rotational properties of the comet nuclei (periods, rotation vector coordinates, spin mode, etc.) reported by Samarasinha et al. (2004).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-c-compil-5-lightcurves-v1.0_5czy-ph2p",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "support archives",
                 "133p/elst-pizarro (1996 n2)",
@@ -184753,1091 +184755,1091 @@
                 "49p/arend-rigaux 1 (1951 c2)",
                 "48p/johnson (1949 q1)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-C-COMPIL-5-LIGHTCURVES-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-c-compil-5-lightcurves-v1.0_5czy-ph2p",
-            "description": "This is a dataset that compiles the data from various papers, which reported observations of brightness changes in comets that allowed to produce the comet lightcurves. Specifically, the data were based on the references in the paper by Samarasinha et al. (2004), i.e. they are those lightcurves, which were used to find out the rotational properties of the comet nuclei (periods, rotation vector coordinates, spin mode, etc.) reported by Samarasinha et al. (2004).",
-            "title": "SURVEY OF COMET LIGHTCURVES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "SURVEY OF COMET LIGHTCURVES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMAG-2-ESC1-RAW-V5.0",
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
+            "description": "This dataset contains EDITED RAW DATA (CODMAC LEVEL 2) of the COMET\nESCORT1 Phase from November 22, 2014 until March 10, 2015 of the\nROSETTA orbiter magnetometer RPCMAG. Observations are done in the\nvicinity of comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1).\nVersion V5.0 is the first version being released.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmag-2-esc1-raw-v5.0_5czy-vzr2",
+            "issued": "2018-06-26",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMAG-2-ESC1-RAW-V5.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmag-2-esc1-raw-v5.0_5czy-vzr2",
-            "description": "This dataset contains EDITED RAW DATA (CODMAC LEVEL 2) of the COMET\nESCORT1 Phase from November 22, 2014 until March 10, 2015 of the\nROSETTA orbiter magnetometer RPCMAG. Observations are done in the\nvicinity of comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1).\nVersion V5.0 is the first version being released.",
-            "title": "ROSETTA-ORBITER 67P RPCMAG 2 ESC1 RAW V5.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER 67P RPCMAG 2 ESC1 RAW V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-3-TNO-CEN-COLOR-V2.0",
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
+            "description": "This data set is intended to include published broadband colors of centaurs and Transneptunian Objects (TNOs) published through December 2004. It supersedes all versions of the TNO colors data set EAR-A-3-RDR-TNO-PHOT.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-3-tno-cen-color-v2.0_5d2p-yxtt",
+            "issued": "2018-06-26",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-3-TNO-CEN-COLOR-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-3-tno-cen-color-v2.0_5d2p-yxtt",
-            "description": "This data set is intended to include published broadband colors of centaurs and Transneptunian Objects (TNOs) published through December 2004. It supersedes all versions of the TNO colors data set EAR-A-3-RDR-TNO-PHOT.",
-            "title": "TNO AND CENTAUR COLORS V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "TNO AND CENTAUR COLORS V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MEASURES/DMSP-F15/SSMI/DATA304",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wentz, Frank J, Kyle Hilburn and Deborah K Smith.2012. RSS SSM/I OCEAN PRODUCT GRIDS MONTHLY AVERAGE FROM DMSP F15 NETCDF [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/MEASURES/DMSP-F15/SSMI/DATA304",
-            "issued": "2012-08-08",
-            "temporal": "1999-12-01T00:00:00Z/2011-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "clouds",
-                "ocean winds",
-                "atmosphere",
-                "atmospheric water vapor",
-                "atmospheric winds",
-                "earth science",
-                "oceans",
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
-            "identifier": "C1979943148-GHRC_DAAC",
             "description": "The RSS SSM/I Ocean Product Grids Monthly Average from DMSP F15 netCDF dataset is part of the collection of Special Sensor Microwave/Imager (SSM/I) and Special Sensor Microwave Imager Sounder (SSMIS) data products produced as part of NASA's MEaSUREs Program. Remote Sensing Systems generates SSM/I and SSMIS binary data products using a unified, physically based algorithm to simultaneously retrieve ocean wind speed, water vapor, cloud water, and rain rate. The SSMIS data have been carefully intercalibrated to the brightness temperature level of the previous SSM/I and therefore extend this important time series of ocean winds, vapor, cloud and rain values. This algorithm is a product of 20 years of refinements, improvements, and verifications. The Global Hydrology Resource Center has reformatted the binary data into a netCDF data product for each temporal group for each satellite. The netCDF SSMI/SSMIS collection will be available for F15 for a monthly average.",
-            "graphic-preview-description": "N/A",
-            "title": "RSS SSM/I OCEAN PRODUCT GRIDS MONTHLY AVERAGE FROM DMSP F15 NETCDF V7",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f15/monthly/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FDMSP-F15%2FSSMI%2FDATA304",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FDMSP-F15%2FSSMI%2FDATA304",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=rssmif15m",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=rssmif15m",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f15/monthly/browse/2009/f15_ssmi_200904v7_WS.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f15/monthly/browse/2009/f15_ssmi_200904v7_WS.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f15/monthly/browse/2009/f15_ssmi_200904v7_RR.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f15/monthly/browse/2009/f15_ssmi_200904v7_RR.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f15/monthly/browse/2009/f15_ssmi_200904v7_CW.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f15/monthly/browse/2009/f15_ssmi_200904v7_CW.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f15/monthly/browse/2009/f15_ssmi_200904v7_WV.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f15/monthly/browse/2009/f15_ssmi_200904v7_WV.png",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/opendap/ssmi/f15/monthly/",
-                    "description": "OPeNDAP server dataset access",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP server dataset access",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/opendap/ssmi/f15/monthly/",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f15/monthly/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f15/monthly/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f15/monthly/browse/",
+            "identifier": "C1979943148-GHRC_DAAC",
+            "issued": "2012-08-08",
+            "keyword": [
+                "clouds",
+                "ocean winds",
+                "atmosphere",
+                "atmospheric water vapor",
+                "atmospheric winds",
+                "earth science",
+                "oceans",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/DMSP-F15/SSMI/DATA304",
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
+            "temporal": "1999-12-01T00:00:00Z/2011-12-31T23:59:59Z",
             "theme": [
                 "DISCOVER",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "RSS SSM/I OCEAN PRODUCT GRIDS MONTHLY AVERAGE FROM DMSP F15 NETCDF V7"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A%2FCAL-NAVCAM-2-AST2-V1.1",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This dataset contains RAW DATA of the LUTETIA flyby Phase from 30 May 2010 until 10 July 2010.  The closest approach (CA) took place on 10 July 2010 at 15:45. This data set V1.1 supersedes the V1.0. It includes updates of the Browse images, adding of the FITS version, clarification of calibration target, document updates and resolve other minor outstanding errata.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-cal-navcam-2-ast2-v1.1",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "dark sky",
                 "international rosetta mission",
                 "21 lutetia"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A%2FCAL-NAVCAM-2-AST2-V1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-cal-navcam-2-ast2-v1.1",
-            "description": "This dataset contains RAW DATA of the LUTETIA flyby Phase from 30 May 2010 until 10 July 2010.  The closest approach (CA) took place on 10 July 2010 at 15:45. This data set V1.1 supersedes the V1.0. It includes updates of the Browse images, adding of the FITS version, clarification of calibration target, document updates and resolve other minor outstanding errata.",
-            "title": "ROSETTA-ORBITER LUTETIA/CAL NAVCAM 2 LUTETIA FLY-BY V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER LUTETIA/CAL NAVCAM 2 LUTETIA FLY-BY V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSIWAC-4-CR2-CHKOUT-STR-REFL-V1.0",
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
-                "9p/tempel 1 (1867 g1)"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units  (normalized and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the CRUISE 2 mission phase, covering the period  from 2005-04-05T00:00:00.000 to 2006-07-28T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. This version V1.0 is the first version of this dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osiwac-4-cr2-chkout-str-refl-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "9p/tempel 1 (1867 g1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSIWAC-4-CR2-CHKOUT-STR-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osiwac-4-cr2-chkout-str-refl-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units  (normalized and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the CRUISE 2 mission phase, covering the period  from 2005-04-05T00:00:00.000 to 2006-07-28T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. This version V1.0 is the first version of this dataset.",
-            "title": "ROSETTA-ORBITER CHECKOUT OSIWAC 4 CR2 RDR-STR-REFL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECKOUT OSIWAC 4 CR2 RDR-STR-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GRIP/HIRAD/DATA202",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Cecil, Daniel J and Sayak Biswas K..2015. GRIP HURRICANE IMAGING RADIOMETER (HIRAD) V1 [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GRIP/HIRAD/DATA202",
-            "issued": "2015-12-08",
-            "temporal": "2010-09-01T22:10:09Z/2010-09-16T23:18:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "microwave",
-                "earth science",
-                "spectral/engineering",
-                "atmospheric winds",
-                "ocean temperature",
-                "platform characteristics",
-                "oceans",
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
-            "identifier": "C1979853044-GHRC_DAAC",
             "description": "The GRIP Hurricane Imaging Radiometer (HIRAD) V1 dataset contains measurements of brightness temperature taken at 4, 5, 6 and 6.6 GHz, as well as MERRA 2 m wind speed data and JPL MUR Sea Surface Temperature data. The data is provided in netCDF format. The data were collected during the Genesis and Rapid Intensification Processes (GRIP) experiment from September 1, 2010 through September 16, 2010 for storms EARL and KARL. Rain rate and wind speed files may be obtained from the V0 HIRAD dataset. The major goal was to better understandhow tropical storms form and develop into major hurricanes. NASA used the DC-8 aircraft, the WB-57 aircraft and the Global Hawk Unmanned AirborneSystem (UAS), configuredwith a suite of in situ and remote sensing instruments that were used to observe and characterize the lifecycle of hurricanes.HIRAD is a hurricane imaging, single-polarization passive C-band radiometer with both cross-track and along-track resolution that measures strong ocean surface winds through heavy rain from an aircraft or space-based platform. Its swath width is approximately 60 degrees in either direction.",
-            "graphic-preview-description": "N/A",
-            "title": "GRIP HURRICANE IMAGING RADIOMETER (HIRAD) V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/grip/HIRAD/v1/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGRIP%2FHIRAD%2FDATA202",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGRIP%2FHIRAD%2FDATA202",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=griphirad1",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=griphirad1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/grip/HIRAD/v0/browse/EARL/grip_hirad_20100901_EARL_leg123456.jpg",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/grip/HIRAD/v0/browse/EARL/grip_hirad_20100901_EARL_leg123456.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/vnd.google-earth.kmz",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/grip/HIRAD/v1/browse/GRIP2010_karlFLT_Sep16/grip_flighttrack_20100916_20100916_karl_extrude.kmz",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/grip/HIRAD/v1/browse/GRIP2010_karlFLT_Sep16/grip_flighttrack_20100916_20100916_karl_extrude.kmz",
+                    "mediaType": "application/vnd.google-earth.kmz",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/grip/HIRAD/v1/doc/griphirad_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/grip/HIRAD/v1/doc/griphirad_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/grip/HIRAD/v1/doc/HIRAD_GoogleEarth_kmz-GUIDE.pdf",
-                    "description": "HIRAD Google Earth KMZ Guide",
                     "@type": "dcat:Distribution",
+                    "description": "HIRAD Google Earth KMZ Guide",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/grip/HIRAD/v1/doc/HIRAD_GoogleEarth_kmz-GUIDE.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/grip/HIRAD/v1/doc/read_v1_grip_HIRADnc.m",
-                    "description": "Reads HIRAD netcdf files and generates MATLAB binary files",
                     "@type": "dcat:Distribution",
+                    "description": "Reads HIRAD netcdf files and generates MATLAB binary files",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/grip/HIRAD/v1/doc/read_v1_grip_HIRADnc.m",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/GRIP",
-                    "description": "The home page for the project or program which sponsored the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The home page for the project or program which sponsored the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/GRIP",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/micro-articles/hurricane",
-                    "description": "Hurricane Micro Article",
                     "@type": "dcat:Distribution",
+                    "description": "Hurricane Micro Article",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/micro-articles/hurricane",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/grip/HIRAD/v1/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/grip/HIRAD/v1/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/grip/HIRAD/v1/browse/",
+            "identifier": "C1979853044-GHRC_DAAC",
+            "issued": "2015-12-08",
+            "keyword": [
+                "microwave",
+                "earth science",
+                "spectral/engineering",
+                "atmospheric winds",
+                "ocean temperature",
+                "platform characteristics",
+                "oceans",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/GRIP/HIRAD/DATA202",
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
             "spatial": "-95.5915 18.2751 -71.0313 30.1404",
+            "temporal": "2010-09-01T22:10:09Z/2010-09-16T23:18:00Z",
             "theme": [
                 "GRIP (HURRICANE)",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GRIP HURRICANE IMAGING RADIOMETER (HIRAD) V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D32.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang. 2021-02-22. MODIS/Terra+Aqua BRDF/Albedo QA LocalSolarNoon Daily L3 Global 30ArcSec CMG V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MCD43D32.061. https://doi.org/10.5067/MODIS/MCD43D32.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-02-22",
-            "temporal": "2000-02-16T00:00:00Z/2024-05-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-22",
-            "keyword": [
-                "earth science",
-                "national geospatial data asset",
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
-            "identifier": "C2540270742-LPCLOUD",
-            "description": "The MCD43D32 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) QA Local Solar Noon dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter (m)) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. MCD43D32 provides local solar noon information for the MCD43D products. \r\n\r\nThe MCD43D32 layer contains the local solar zenith angle at the local solar noon of the representative pixel for the retrieval period.  \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
-            "release-place": "Sioux Falls, South Dakota, USA",
             "creator": "Crystal Schaaf, Zhuosen Wang",
-            "title": "MODIS/Terra+Aqua BRDF/Albedo QA LocalSolarNoon Daily L3 Global 30ArcSec CMG V061",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MCD43D32 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) QA Local Solar Noon dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter (m)) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. MCD43D32 provides local solar noon information for the MCD43D products. \r\n\r\nThe MCD43D32 layer contains the local solar zenith angle at the local solar noon of the representative pixel for the retrieval period.  \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D32.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D32.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D32.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D32.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2540270742-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2540270742-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D32.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D32.061",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MCD43D32",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MCD43D32",
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
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D32.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D32.061/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2540270742-LPCLOUD",
+            "issued": "2021-02-22",
+            "keyword": [
+                "earth science",
+                "national geospatial data asset",
+                "ngda",
+                "land surface",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D32.061",
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
+            "title": "MODIS/Terra+Aqua BRDF/Albedo QA LocalSolarNoon Daily L3 Global 30ArcSec CMG V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-RADAR-V7.0",
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
+            "description": "Groundbased radar detections of asteroids, collected from the published literature by S. J. Ostro.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-radar-v7.0_5dg4-3wxu",
+            "issued": "2018-06-26",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-RADAR-V7.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-radar-v7.0_5dg4-3wxu",
-            "description": "Groundbased radar detections of asteroids, collected from the published literature by S. J. Ostro.",
-            "title": "ASTEROID RADAR V7.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ASTEROID RADAR V7.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1335",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "FLUXNET CANADA TEAM. 2016. FLUXNET Canada Research Network - Canadian Carbon Program Data Collection, 1993-2014. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1335",
-            "issued": "2022-03-04",
-            "temporal": "1993-01-01T00:00:00Z/2014-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-02",
-            "keyword": [
-                "atmospheric chemistry",
-                "atmospheric radiation",
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "atmospheric winds",
-                "biosphere",
-                "earth science",
-                "ecological dynamics",
-                "ecosystems",
-                "vegetation",
-                "soils",
-                "precipitation",
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
-            "identifier": "C2773250697-ORNL_CLOUD",
             "description": "FLUXNET Canada is a Fluxnet research network comprised of the Fluxnet-Canada Research Network (FCRN) and the Canadian Carbon Program (CCP) operating from 1993 through 2014. It was a national research network of university and government scientists studying the influence of climate and disturbance on carbon cycling along an east-west transect of Canadian forest and peat land ecosystems. The data provided are measured and modeled results as obtained from the site investigators. They were not standardized and quality-controlled. Data include: atmospheric carbon dioxide (CO2) and water vapor fluxes and many ancillary meteorological variables; soil CO2 efflux and soil moisture; stable carbon isotopes; site soil and vegetation characteristics, plus documentation and descriptions for the 32 tower sites across 12 flux research stations. The time period is from 1993 - 2014; most reported data for a site does not cover the entire period.",
-            "graphic-preview-description": "Locations of the 32 Eddy-Covariance towers of FLUXNET Canada included in this data set.",
-            "title": "FLUXNET Canada Research Network - Canadian Carbon Program Data Collection, 1993-2014",
-            "graphic-preview-file": "https://daac.ornl.gov/FLUXNET/guides/FLUXNET_Canada_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1335",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1335",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/fluxnet/FLUXNET_Canada/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/fluxnet/FLUXNET_Canada/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/FLUXNET/guides/FLUXNET_Canada.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/FLUXNET/guides/FLUXNET_Canada.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1335",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1335",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fluxnet/FLUXNET_Canada/comp/0_FCRN_Data_Policy.txt",
-                    "description": "FLUXNET Canada Research Network - Canadian Carbon Program Data Collection, 1993-2014: 0_FCRN_Data_Policy.txt",
                     "@type": "dcat:Distribution",
+                    "description": "FLUXNET Canada Research Network - Canadian Carbon Program Data Collection, 1993-2014: 0_FCRN_Data_Policy.txt",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fluxnet/FLUXNET_Canada/comp/0_FCRN_Data_Policy.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fluxnet/FLUXNET_Canada/comp/0_Flux_and_Met_File_Type_Definitions.txt",
-                    "description": "FLUXNET Canada Research Network - Canadian Carbon Program Data Collection, 1993-2014: 0_Flux_and_Met_File_Type_Definitions.txt",
                     "@type": "dcat:Distribution",
+                    "description": "FLUXNET Canada Research Network - Canadian Carbon Program Data Collection, 1993-2014: 0_Flux_and_Met_File_Type_Definitions.txt",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fluxnet/FLUXNET_Canada/comp/0_Flux_and_Met_File_Type_Definitions.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fluxnet/FLUXNET_Canada/comp/FLUXNET_Canada.pdf",
-                    "description": "FLUXNET Canada Research Network - Canadian Carbon Program Data Collection, 1993-2014: FLUXNET_Canada.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "FLUXNET Canada Research Network - Canadian Carbon Program Data Collection, 1993-2014: FLUXNET_Canada.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fluxnet/FLUXNET_Canada/comp/FLUXNET_Canada.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/FLUXNET/guides/FLUXNET_Canada_Fig1.png",
-                    "description": "Locations of the 32 Eddy-Covariance towers of FLUXNET Canada included in this data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Locations of the 32 Eddy-Covariance towers of FLUXNET Canada included in this data set.",
+                    "downloadURL": "https://daac.ornl.gov/FLUXNET/guides/FLUXNET_Canada_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Locations of the 32 Eddy-Covariance towers of FLUXNET Canada included in this data set.",
+            "graphic-preview-file": "https://daac.ornl.gov/FLUXNET/guides/FLUXNET_Canada_Fig1.png",
+            "identifier": "C2773250697-ORNL_CLOUD",
+            "issued": "2022-03-04",
+            "keyword": [
+                "atmospheric chemistry",
+                "atmospheric radiation",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "atmospheric winds",
+                "biosphere",
+                "earth science",
+                "ecological dynamics",
+                "ecosystems",
+                "vegetation",
+                "soils",
+                "precipitation",
+                "land surface",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1335",
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
             "spatial": "-125.33 42.66 -67.1 55.88",
+            "temporal": "1993-01-01T00:00:00Z/2014-12-31T23:59:59Z",
             "theme": [
                 "Fluxnet",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FLUXNET Canada Research Network - Canadian Carbon Program Data Collection, 1993-2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/IFLOODS/NEXRAD/DATA501",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Unidata  and   NWS Radar Operations Center.2018. GPM Ground Validation NEXRAD Level III KMPX IFloodS [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/IFLOODS/NEXRAD/DATA501",
-            "issued": "2018-03-05",
-            "temporal": "2013-03-29T21:05:00Z/2013-06-18T15:03:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-09",
-            "keyword": [
-                "atmosphere",
-                "spectral/engineering",
-                "radar",
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
-            "identifier": "C1982587652-GHRC_DAAC",
             "description": "The GPM Ground Validation NEXRAD Level III KMPX IFloodS dataset   contain precipitation products derived from selected NEXt Generation Weather RADar system (NEXRAD) radars in operation during the Iowa Flood Studies (IFloodS) field campaign to help support the ground validation of the Global Precipitation Measurement (GPM). NEXRAD is a network of 160 stationary S-Band radars dispersed throughout the United States and select locations abroad. Data were gathered from four NEXRAD stations in the vicinity of the IFloodS campaign during  March 29, 2013 through June 18, 2013. This dataset contains data files of digital instantaneous precipitation rate (DPR) and storm total accumulation estimates (DTA) in NIDS binary format.",
-            "title": "GPM Ground Validation NEXRAD Level III KMPX IFloodS V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FIFLOODS%2FNEXRAD%2FDATA501",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FIFLOODS%2FNEXRAD%2FDATA501",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmkmpx3ifld",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmkmpx3ifld",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www.ofcm.gov/publications/fmh/FMH11/fmh11partC.pdf",
-                    "description": "WSR-88D Meteorological Observations: Part C WSR-88D Products and Algorithms",
                     "@type": "dcat:Distribution",
+                    "description": "WSR-88D Meteorological Observations: Part C WSR-88D Products and Algorithms",
+                    "downloadURL": "https://www.ofcm.gov/publications/fmh/FMH11/fmh11partC.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/NEXRAD3/KMPX/doc/gpmnexrad3iflds_dataset.pdf",
-                    "description": "GPM Ground Validation NEXRAD Level III IFloodS User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "GPM Ground Validation NEXRAD Level III IFloodS User Guide",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/NEXRAD3/KMPX/doc/gpmnexrad3iflds_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/JHM-D-14-0148.1",
-                    "description": "NEXRAD NWS Polarimetric Precipitation Product Evaluation for IFloodS",
                     "@type": "dcat:Distribution",
+                    "description": "NEXRAD NWS Polarimetric Precipitation Product Evaluation for IFloodS",
+                    "downloadURL": "https://doi.org/10.1175/JHM-D-14-0148.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/2008JAMC1753.1",
-                    "description": "Estimation of Rainfall Based on the Results of Polarimetric Echo Classification",
                     "@type": "dcat:Distribution",
+                    "description": "Estimation of Rainfall Based on the Results of Polarimetric Echo Classification",
+                    "downloadURL": "https://doi.org/10.1175/2008JAMC1753.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/ifloods",
-                    "description": "GHRC IFloodS project web page",
                     "@type": "dcat:Distribution",
+                    "description": "GHRC IFloodS project web page",
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
+            "identifier": "C1982587652-GHRC_DAAC",
+            "issued": "2018-03-05",
+            "keyword": [
+                "atmosphere",
+                "spectral/engineering",
+                "radar",
+                "precipitation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/IFLOODS/NEXRAD/DATA501",
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
             "spatial": "-94.0144 44.3998 -93.1162 45.298",
+            "temporal": "2013-03-29T21:05:00Z/2013-06-18T15:03:00Z",
             "theme": [
                 "IFloodS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM Ground Validation NEXRAD Level III KMPX IFloodS V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/TEMSC-GT634",
             "citation": "D. N. Wiese, D.-N. Yuan, C. Boening, F. W. Landerer, M. M. Watkins. 2024-01-25. Tellus Level-4 Greenland Mass Anomaly Time Series. Version RL06.3Mv04. Tellus Level-4 Greenland Mass Anomaly Time Series from JPL GRACE/GRACE-FO Mascon CRI Filtered Release 06.3 version 04. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/TEMSC-GT634. http://grace.jpl.nasa.gov/data/get-data/jpl_global_mascons/.",
-            "issued": "2020-02-14",
-            "temporal": "2002-04-01T00:00:00Z/2024-11-11T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-02-14",
-            "references": [
-                "https://doi.org/10.1002/2014JB011547"
-            ],
-            "keyword": [
-                "climate indicators",
-                "glaciers/ice sheets",
-                "earth science",
-                "cryospheric indicators",
-                "cryosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
             },
-            "identifier": "C3206299308-POCLOUD",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "description": "This dataset is a time series of mass variability averaged over all of the global ocean. It provides the non-steric or mass only sea level changes over time. The mass variability are derived from JPL GRACE Mascon Ocean, Ice, and Hydrology Equivalent Water Height CRI Filtered RL06.3Mv04 dataset, which can be found at https://podaac.jpl.nasa.gov/dataset/TELLUS_GRAC-GRFO_MASCON_CRI_GRID_RL06.3_V3. A more detailed description on the Mascon solution, including the mathematical derivation, implementation of geophysical constraints, and solution validation, please see Watkins et al., 2015, doi: 10.1002/2014JB011547. The mass variability is provided as an ASCII table.",
-            "release-place": "PO.DAAC",
-            "series-name": "Tellus Level-4 Greenland Mass Anomaly Time Series",
             "creator": "D. N. Wiese, D.-N. Yuan, C. Boening, F. W. Landerer, M. M. Watkins",
-            "title": "Tellus Level-4 Greenland Mass Anomaly Time Series from JPL GRACE/GRACE-FO Mascon CRI Filtered Release 06.3 version 04",
-            "graphic-preview-description": "Thumbnail",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GREENLAND_MASS_TELLUS_MASCON_CRI_TIME_SERIES_RL06.3_V4.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset is a time series of mass variability averaged over all of the global ocean. It provides the non-steric or mass only sea level changes over time. The mass variability are derived from JPL GRACE Mascon Ocean, Ice, and Hydrology Equivalent Water Height CRI Filtered RL06.3Mv04 dataset, which can be found at https://podaac.jpl.nasa.gov/dataset/TELLUS_GRAC-GRFO_MASCON_CRI_GRID_RL06.3_V3. A more detailed description on the Mascon solution, including the mathematical derivation, implementation of geophysical constraints, and solution validation, please see Watkins et al., 2015, doi: 10.1002/2014JB011547. The mass variability is provided as an ASCII table.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTEMSC-GT634",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTEMSC-GT634",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://grace.jpl.nasa.gov/data/get-data/jpl_global_mascons/",
-                    "description": "Additional resource and information site for the Global Mascon datasets. This includes update announcements, user feedback page, and FAQ's.",
                     "@type": "dcat:Distribution",
+                    "description": "Additional resource and information site for the Global Mascon datasets. This includes update announcements, user feedback page, and FAQ's.",
+                    "downloadURL": "http://grace.jpl.nasa.gov/data/get-data/jpl_global_mascons/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/GRACE-FO",
-                    "description": "PODAAC's GRACE-FO Project-Page",
                     "@type": "dcat:Distribution",
+                    "description": "PODAAC's GRACE-FO Project-Page",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/GRACE-FO",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/GRACE",
-                    "description": "PODAAC's GRACE Project-Page",
                     "@type": "dcat:Distribution",
+                    "description": "PODAAC's GRACE Project-Page",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/GRACE",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GREENLAND_MASS_TELLUS_MASCON_CRI_TIME_SERIES_RL06.3_V4.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GREENLAND_MASS_TELLUS_MASCON_CRI_TIME_SERIES_RL06.3_V4.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C3206299308-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C3206299308-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C3206299308-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C3206299308-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/gravity/gracefo-documentation",
-                    "description": "Page with GRACE-FO documentation and technical notes for many of the project's data products",
                     "@type": "dcat:Distribution",
+                    "description": "Page with GRACE-FO documentation and technical notes for many of the project's data products",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/gravity/gracefo-documentation",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/gracefo/open/docs/GRACE_GRACE-FO_ReleaseNotes_JPL_MASCON.txt",
-                    "description": "RL0.63 Version 4 Release Note",
                     "@type": "dcat:Distribution",
+                    "description": "RL0.63 Version 4 Release Note",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/gracefo/open/docs/GRACE_GRACE-FO_ReleaseNotes_JPL_MASCON.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GREENLAND_MASS_TELLUS_MASCON_CRI_TIME_SERIES_RL06.3_V4.jpg",
+            "identifier": "C3206299308-POCLOUD",
+            "issued": "2020-02-14",
+            "keyword": [
+                "climate indicators",
+                "glaciers/ice sheets",
+                "earth science",
+                "cryospheric indicators",
+                "cryosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/TEMSC-GT634",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-02-14",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.1002/2014JB011547"
+            ],
+            "release-place": "PO.DAAC",
+            "series-name": "Tellus Level-4 Greenland Mass Anomaly Time Series",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-04-01T00:00:00Z/2024-11-11T00:00:00Z",
             "theme": [
                 "GRACE",
                 "GRACE-FO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Tellus Level-4 Greenland Mass Anomaly Time Series from JPL GRACE/GRACE-FO Mascon CRI Filtered Release 06.3 version 04"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1762",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Minions, C., S. Natali, J.D. Watts, S. Ludwig, and D. Risk. 2019. ABoVE: Year-Round Soil CO2 Efflux in Alaskan Ecosystems, Version 2.1. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1762",
-            "issued": "2024-05-02",
-            "temporal": "2016-08-18T00:00:00Z/2023-09-02T12:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-03",
-            "keyword": [
-                "climate indicators",
-                "atmospheric chemistry",
-                "earth science",
-                "carbon flux",
-                "atmosphere",
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
-            "identifier": "C2143811850-ORNL_CLOUD",
             "description": "This dataset provides soil-surface carbon dioxide (CO2) efflux derived from measurements of soil respiration with forced diffusion (FD) chambers. Soil Respiration Stations (SRS) were installed at 11 boreal and tundra sites along a broad south-to-north transect starting from near Fairbanks in interior Alaska and extending to Atqasuk in northern Alaska. Each SRS measures soil respiration and ambient atmospheric CO2 concentrations with a forced diffusion (FD) chamber to derive soil CO2 flux. The SRS also measures soil CO2 concentrations and temperatures using instrumented chambers buried at 5, 10, and 15 cm depths in the soil profile. At the highest measurement frequency, data are collected hourly, and during the lowest winter frequency, every 48 hours. The data include flux values and running median filtered values from the two or three FD chambers at each site. Soil CO2 and temperature profile data (beginning June 2017) were collected beginning 2016-08-18 through 2023-09-02. This dataset updates four sites with extended temporal coverage. As of this publication, sampling is continuing, and new data will be added as available.",
-            "graphic-preview-description": "a)  A Soil Respiration Station (SRS) deployed at a boreal forest site in central Alaska; b)  the SRS data logger; c) a Forced Diffusion Chamber (FD chamber) installed at a site.",
-            "title": "ABoVE: Year-Round Soil CO2 Efflux in Alaskan Ecosystems, Version 2.1",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Arctic_Winter_Respiration_v2_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1762",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1762",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/above/Arctic_Winter_Respiration_v2/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/above/Arctic_Winter_Respiration_v2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Arctic_Winter_Respiration_v2.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Arctic_Winter_Respiration_v2.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1762",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1762",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Arctic_Winter_Respiration_v2/comp/Arctic_Winter_Respiration_v2.pdf",
-                    "description": "ABoVE: Year-Round Soil CO2 Efflux in Alaskan Ecosystems, Version 2.1: Arctic_Winter_Respiration_v2.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Year-Round Soil CO2 Efflux in Alaskan Ecosystems, Version 2.1: Arctic_Winter_Respiration_v2.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Arctic_Winter_Respiration_v2/comp/Arctic_Winter_Respiration_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Arctic_Winter_Respiration_v2_Fig1.png",
-                    "description": "a)  A Soil Respiration Station (SRS) deployed at a boreal forest site in central Alaska; b)  the SRS data logger; c) a Forced Diffusion Chamber (FD chamber) installed at a site.",
                     "@type": "dcat:Distribution",
+                    "description": "a)  A Soil Respiration Station (SRS) deployed at a boreal forest site in central Alaska; b)  the SRS data logger; c) a Forced Diffusion Chamber (FD chamber) installed at a site.",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Arctic_Winter_Respiration_v2_Fig1.png",
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
+            "graphic-preview-description": "a)  A Soil Respiration Station (SRS) deployed at a boreal forest site in central Alaska; b)  the SRS data logger; c) a Forced Diffusion Chamber (FD chamber) installed at a site.",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Arctic_Winter_Respiration_v2_Fig1.png",
+            "identifier": "C2143811850-ORNL_CLOUD",
+            "issued": "2024-05-02",
+            "keyword": [
+                "climate indicators",
+                "atmospheric chemistry",
+                "earth science",
+                "carbon flux",
+                "atmosphere",
+                "land surface",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1762",
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
             "spatial": "-157.41 63.88 -146.56 70.47",
+            "temporal": "2016-08-18T00:00:00Z/2023-09-02T12:00:00Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE: Year-Round Soil CO2 Efflux in Alaskan Ecosystems, Version 2.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-NEO-LIGHTCURVES-V1.1",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set is a collection of photometric lightcurves for 42 near-earth asteroids obtained at Ondrejov Observatory from 1984 through 1998.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-neo-lightcurves-v1.1_5dq5-us7b",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "asteroid 1994 cb",
                 "7341",
@@ -185884,900 +185886,874 @@
                 "2212 hephaistos",
                 "2100 ra-shalom"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-NEO-LIGHTCURVES-V1.1",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-neo-lightcurves-v1.1_5dq5-us7b",
-            "description": "This data set is a collection of photometric lightcurves for 42 near-earth asteroids obtained at Ondrejov Observatory from 1984 through 1998.",
-            "title": "NEAR EARTH ASTEROID LIGHTCURVES V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEAR EARTH ASTEROID LIGHTCURVES V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC2-67P-M15-INFLDSTR-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 2 mission phase, covering the period  from 2015-04-08T11:25:00.000 to 2015-05-05T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc2-67p-m15-infldstr-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC2-67P-M15-INFLDSTR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc2-67p-m15-infldstr-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 2 mission phase, covering the period  from 2015-04-08T11:25:00.000 to 2015-05-05T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC2-MTP015 RDR-INFLDSTR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC2-MTP015 RDR-INFLDSTR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/PJ579BN9KVSD",
             "citation": "Glen Jaross. 2024-09-16. OMPS_N21_LP_L1G_EV. Version 1.0. OMPS-N21 L1G LP Radiance EV Wavelength-Altitude Grid swath orbital 3slit V1.0. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/PJ579BN9KVSD. https://disc.gsfc.nasa.gov/datacollection/OMPS_N21_LP_L1G_EV_1.0.html. Digital Science Data.",
-            "issued": "2024-05-10",
-            "temporal": "2022-11-10T00:00:00Z/2024-10-07T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-10",
-            "keyword": [
-                "infrared wavelengths",
-                "earth science",
-                "spectral/engineering",
-                "ultraviolet wavelengths",
-                "visible wavelengths"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "GLENN JAROSS, PH. D",
                 "hasEmail": "mailto:Glen.R.Jaross@nasa.gov"
             },
+            "creator": "Glen Jaross",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C3117300814-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The OMPS-N21 L1G LP Radiance EV Wavelength-Altitude Grid swath orbital 3slit product contains the calibrated earth-viewing radiances measured by the Ozone Mapping and Profiling Suite (OMPS) Limb-Profiler (LP) sensor on the NOAA 21 (JPSS-2) satellite. The LP L1G product measures radiances in the wavelength region from 280 nm to 1000 nm.\n\nEach granule contains data from the daylight portion of each orbit measured for a full day. Spatial coverage is global (-90 to  90 degrees latitude), and there are about 14.5 orbits per day each measuring three limb profiles spaced approximately 250 km in the cross-track direction. The profiles are measured from the ground up to about 80 km with a vertical resolution of the retrieved profiles of approximately 1-2 km.\n\nThe data are written using the Hierarchical Data Format Version 5 or HDF5.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OMPS_N21_LP_L1G_EV",
-            "creator": "Glen Jaross",
-            "title": "OMPS-N21 L1G LP Radiance EV Wavelength-Altitude Grid swath orbital 3slit V1.0 (OMPS_N21_LP_L1G_EV) at GES DISC",
-            "graphic-preview-description": "OMPS Logo",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMPS_NPP_LP_L1G_EV_2.6.jpeg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FPJ579BN9KVSD",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FPJ579BN9KVSD",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMPS_NPP_LP_L1G_EV_2.6.jpeg",
-                    "description": "OMPS Logo",
                     "@type": "dcat:Distribution",
+                    "description": "OMPS Logo",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMPS_NPP_LP_L1G_EV_2.6.jpeg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMPS_N21_LP_L1G_EV_1.0.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMPS_N21_LP_L1G_EV_1.0.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://snpp-omps.gesdisc.eosdis.nasa.gov/data/NOAA21_OMPS_Level1B/OMPS_N21_LP_L1G_EV.1.0/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://snpp-omps.gesdisc.eosdis.nasa.gov/data/NOAA21_OMPS_Level1B/OMPS_N21_LP_L1G_EV.1.0/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMPS_N21_LP_L1G_EV_1.0",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMPS_N21_LP_L1G_EV_1.0",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://snpp-omps.gesdisc.eosdis.nasa.gov/data/NOAA21_OMPS_Level1B/OMPS_N21_LP_L1G_EV.1.0/doc/README.OMPS_N21_LP_L1G_EV.1.0.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://snpp-omps.gesdisc.eosdis.nasa.gov/data/NOAA21_OMPS_Level1B/OMPS_N21_LP_L1G_EV.1.0/doc/README.OMPS_N21_LP_L1G_EV.1.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nesdis.noaa.gov/our-satellites/currently-flying/joint-polar-satellite-system",
-                    "description": "Joint Polar Satellite System (JPSS) mission home page",
                     "@type": "dcat:Distribution",
+                    "description": "Joint Polar Satellite System (JPSS) mission home page",
+                    "downloadURL": "https://www.nesdis.noaa.gov/our-satellites/currently-flying/joint-polar-satellite-system",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "graphic-preview-description": "OMPS Logo",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMPS_NPP_LP_L1G_EV_2.6.jpeg",
+            "identifier": "C3117300814-GES_DISC",
+            "issued": "2024-05-10",
+            "keyword": [
+                "infrared wavelengths",
+                "earth science",
+                "spectral/engineering",
+                "ultraviolet wavelengths",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/PJ579BN9KVSD",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-05-10",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "OMPS_N21_LP_L1G_EV",
             "spatial": "-180.0 -84.0 180.0 84.0",
+            "temporal": "2022-11-10T00:00:00Z/2024-10-07T00:00:00Z",
             "theme": [
                 "JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OMPS-N21 L1G LP Radiance EV Wavelength-Altitude Grid swath orbital 3slit V1.0 (OMPS_N21_LP_L1G_EV) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MIDAS-3-EXT2-SAMPLES-V1.0",
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
+            "description": "The Micro-Imaging Dust Analysis System (MIDAS) is an instrument on the\nROSETTA Orbiter that will provide 3D images and statistical parameters\nof pristine cometary particles, collected in the vicinity of comet\n67P/Churyumov-Gerasimenko. This data set\nincludes all data from the ROSETTA EXTENSION 2 mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-midas-3-ext2-samples-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MIDAS-3-EXT2-SAMPLES-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-midas-3-ext2-samples-v1.0",
-            "description": "The Micro-Imaging Dust Analysis System (MIDAS) is an instrument on the\nROSETTA Orbiter that will provide 3D images and statistical parameters\nof pristine cometary particles, collected in the vicinity of comet\n67P/Churyumov-Gerasimenko. This data set\nincludes all data from the ROSETTA EXTENSION 2 mission phase.",
-            "title": "ROSETTA-ORBITER 67P MIDAS 3 EXT2 SAMPLES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P MIDAS 3 EXT2 SAMPLES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VCO-V-LIR-3-SEDR-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The VCO LIR SEDR data set contains products of geometry information calculated by SPICE toolkit using SPICE kernels VCO-V-SPICE-6-V1.0, associated with images acquired by the LIR instrument onboard the Venus Climate Orbiter (VCO, also known as PLANET-C and AKATSUKI) spacecraft. The data files are provided in FITS format with several HDUs as IMAGE extension, and it also contains metadata to the header of the HDUs.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vco-v-lir-3-sedr-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "earth",
                 "venus",
                 "venus climate orbiter"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VCO-V-LIR-3-SEDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vco-v-lir-3-sedr-v1.0",
-            "description": "The VCO LIR SEDR data set contains products of geometry information calculated by SPICE toolkit using SPICE kernels VCO-V-SPICE-6-V1.0, associated with images acquired by the LIR instrument onboard the Venus Climate Orbiter (VCO, also known as PLANET-C and AKATSUKI) spacecraft. The data files are provided in FITS format with several HDUs as IMAGE extension, and it also contains metadata to the header of the HDUs.",
-            "title": "VENUS CLIMATE ORBITER LIR GEOMETRY\n                                      INFORMATION V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VENUS CLIMATE ORBITER LIR GEOMETRY\n                                      INFORMATION V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Texas_Ground_ManvelCroix_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2022-08-22. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Texas_Ground_ManvelCroix_Data_1.",
-            "issued": "2021-08-26",
-            "temporal": "2013-08-28T00:00:00Z/2013-09-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-08-22",
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
-            "identifier": "C2417019975-LARC_ASDC",
             "description": "DISCOVERAQ_Texas_Ground_ManvelCroix_Data contains data collected at the Manvel Croix ground site during the Texas (Houston) deployment of NASA's DISCOVER-AQ field study. This data product contains data for only the Texas deployment and data collection is complete.\r\n\r\nUnderstanding the factors that contribute to near surface pollution is difficult using only satellite-based observations. The incorporation of surface-level measurements from aircraft and ground-based platforms provides the crucial information necessary to validate and expand upon the use of satellites in understanding near surface pollution. Deriving Information on Surface conditions from Column and Vertically Resolved Observations Relevant to Air Quality (DISCOVER-AQ) was a four-year campaign conducted in collaboration between NASA Langley Research Center, NASA Goddard Space Flight Center, NASA Ames Research Center, and multiple universities to improve the use of satellites to monitor air quality for public health and environmental benefit. Through targeted airborne and ground-based observations, DISCOVER-AQ enabled more effective use of current and future satellites to diagnose ground level conditions influencing air quality.\r\n\r\nDISCOVER-AQ employed two NASA aircraft, the P-3B and King Air, with the P-3B completing in-situ spiral profiling of the atmosphere (aerosol properties, meteorological variables, and trace gas species). The King Air conducted both passive and active remote sensing of the atmospheric column extending below the aircraft to the surface. Data from an existing network of surface air quality monitors, AERONET sun photometers, Pandora UV/vis spectrometers and model simulations were also collected. Further, DISCOVER-AQ employed many surface monitoring sites, with measurements being made on the ground, in conjunction with the aircraft. The B200 and P-3B conducted flights in Baltimore-Washington, D.C. in 2011, Houston, TX in 2013, San Joaquin Valley, CA in 2013, and Denver, CO in 2014. These regions were targeted due to being in violation of the National Ambient Air Quality Standards (NAAQS).\r\n\r\nThe first objective of DISCOVER-AQ was to determine and investigate correlations between surface measurements and satellite column observations for the trace gases ozone (O3), nitrogen dioxide (NO2), and formaldehyde (CH2O) to understand how satellite column observations can diagnose surface conditions. DISCOVER-AQ also had the objective of using surface-level measurements to understand how satellites measure diurnal variability and to understand what factors control diurnal variability. Lastly, DISCOVER-AQ aimed to explore horizontal scales of variability, such as regions with steep gradients and urban plumes.",
-            "title": "DISCOVER-AQ Texas Deployment Manvel Croix Ground Site Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDISCOVERAQ_Texas_Ground_ManvelCroix_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDISCOVERAQ_Texas_Ground_ManvelCroix_Data_1",
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
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Texas_Ground_ManvelCroix_Data_1",
-                    "description": "DOI for DISCOVERAQ_TEXAS_GROUND_MANVELCROIX_DATA_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for DISCOVERAQ_TEXAS_GROUND_MANVELCROIX_DATA_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Texas_Ground_ManvelCroix_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2417019975-LARC_ASDC",
-                    "description": "Earthdata Search client for DISCOVERAQ_TEXAS_GROUND_MANVELCROIX_DATA_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search client for DISCOVERAQ_TEXAS_GROUND_MANVELCROIX_DATA_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2417019975-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/DISCOVER-AQ/Texas_Ground_ManvelCroix_Data_1/",
-                    "description": "ASDC Direct Data Download for DISCOVERAQ_Texas_Ground_ManvelCroix_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for DISCOVERAQ_Texas_Ground_ManvelCroix_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/DISCOVER-AQ/Texas_Ground_ManvelCroix_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2417019975-LARC_ASDC",
+            "issued": "2021-08-26",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Texas_Ground_ManvelCroix_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-08-22",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>23.0 -100.0 23.0 -70.0 43.0 -70.0 43.0 -100.0 23.0 -100.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2013-08-28T00:00:00Z/2013-09-30T23:59:59.999Z",
             "theme": [
                 "DISCOVER-AQ",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "DISCOVER-AQ Texas Deployment Manvel Croix Ground Site Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206865-NSIDCV0.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Permafrost-related micrometeorology and soil temperatures, Qingzang Plateau, China, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center.",
-            "issued": "1991-01-01",
-            "temporal": "1991-01-01T00:00:00Z/1993-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1993-12-31",
-            "keyword": [
-                "atmospheric radiation",
-                "agriculture",
-                "atmosphere",
-                "soils",
-                "land surface",
-                "frozen ground",
-                "atmospheric pressure",
-                "earth science",
-                "cryosphere",
-                "atmospheric winds",
-                "atmospheric water vapor",
-                "atmospheric temperature"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Takeshi Ohta",
                 "hasEmail": "mailto:takeshi@iwate-u.ac.jp"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NSIDC"
-            },
-            "identifier": "C1386206865-NSIDCV0",
             "description": "These data sets include Surface Meteorological Data (D100, D105, Tanggula Pass, Wetland), Ground Temperature (D100, D105, Tanggula Pass, Wetland), Soil Moisture Data, Evaporation, and soil physical properties. These data sets include maximum, mean, minimum air temperature, wind speed, relative humidity, global solar radiation, reflected solar radiation, atmospheric pressure, ground surface and soil temperature, soil moisture content, and soil physical properties. Numerous papers have been published by the investigators using these data sets; references are not available as of March 1998. These data are presented on the CAPS Version 1.0 CD-ROM, June 1998.",
-            "title": "Permafrost-related micrometeorology and soil temperatures, Qingzang Plateau, China, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/GGD486_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/GGD486_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD486/versions/1",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://nsidc.org/data/GGD486/versions/1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD486/versions/1",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://nsidc.org/data/GGD486/versions/1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386206865-NSIDCV0",
+            "issued": "1991-01-01",
+            "keyword": [
+                "atmospheric radiation",
+                "agriculture",
+                "atmosphere",
+                "soils",
+                "land surface",
+                "frozen ground",
+                "atmospheric pressure",
+                "earth science",
+                "cryosphere",
+                "atmospheric winds",
+                "atmospheric water vapor",
+                "atmospheric temperature"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206865-NSIDCV0.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1993-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "90.0 31.0 93.0 33.0",
+            "temporal": "1991-01-01T00:00:00Z/1993-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Permafrost-related micrometeorology and soil temperatures, Qingzang Plateau, China, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RSI-1%2F2%2F3-CR2-0020-V1.0",
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
-                "sun",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This is a Solar Conjunction measurement covering the time 2006-03-24T00:30:38.500 to 2006-03-24T07:44:20.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rsi-1-2-3-cr2-0020-v1.0_5dy7-exzc",
+            "issued": "2021-05-21",
+            "keyword": [
+                "sun",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RSI-1%2F2%2F3-CR2-0020-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rsi-1-2-3-cr2-0020-v1.0_5dy7-exzc",
-            "description": "This is a Solar Conjunction measurement covering the time 2006-03-24T00:30:38.500 to 2006-03-24T07:44:20.500.",
-            "title": "ROSETTA-ORBITER SUN RSI 1/2/3 CRUISE 2 0020 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER SUN RSI 1/2/3 CRUISE 2 0020 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-V-PLS-4-SUMM-VET-V1.0",
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
-                "venus"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Unknown",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-v-pls-4-summ-vet-v1.0_5e2v-3pns",
+            "issued": "2018-06-26",
+            "keyword": [
+                "galileo",
+                "venus"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-V-PLS-4-SUMM-VET-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-v-pls-4-summ-vet-v1.0_5e2v-3pns",
-            "description": "Unknown",
-            "title": "GO VEN PLS SUMM VENUS ET V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GO VEN PLS SUMM VENUS ET V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0518-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-01-02T00:01:20.000 to 2015-01-02T11:14:09.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0518-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0518-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0518-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-01-02T00:01:20.000 to 2015-01-02T11:14:09.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0518 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0518 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-A-SWAP-2-KEM1-V1.0",
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
-                "new horizons kuiper belt extended mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Raw data taken by the New Horizons Solar Wind Around Pluto instrument during the KEM1 ENCOUNTER mission phase. This is VERSION 1.0 of this data set. This data set contains data acquired by the spacecraft between 08/14/2018 and 12/31/2018. It only includes data downlinked before 01/01/2019. Future datasets may include more data acquired by the spacecraft after 08/13/2018 but downlinked after 12/31/2018.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-a-swap-2-kem1-v1.0_5e4s-4eqq",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons kuiper belt extended mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-A-SWAP-2-KEM1-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-a-swap-2-kem1-v1.0_5e4s-4eqq",
-            "description": "This data set contains Raw data taken by the New Horizons Solar Wind Around Pluto instrument during the KEM1 ENCOUNTER mission phase. This is VERSION 1.0 of this data set. This data set contains data acquired by the spacecraft between 08/14/2018 and 12/31/2018. It only includes data downlinked before 01/01/2019. Future datasets may include more data acquired by the spacecraft after 08/13/2018 but downlinked after 12/31/2018.",
-            "title": "NEW HORIZONS\n      SWAP KEM1\n      RAW V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS\n      SWAP KEM1\n      RAW V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/KIEBER_PHOTOCHEMISTRY/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/KIEBER_PHOTOCHEMISTRY/DATA001.",
-            "issued": "2002-06-24",
-            "temporal": "2002-06-24T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "earth science",
-                "salinity/density",
-                "ocean chemistry",
-                "oceans",
-                "ocean optics",
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
-            "identifier": "C1633360394-OB_DAAC",
             "description": "Measurements made along the mid-Atlantic and New England coastal regions.",
-            "title": "Photochemistry measurements made along the mid-Atlantic and New England coastal regions",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FKIEBER_PHOTOCHEMISTRY%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FKIEBER_PHOTOCHEMISTRY%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Kieber_Photochemistry/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Kieber_Photochemistry/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360394-OB_DAAC",
+            "issued": "2002-06-24",
+            "keyword": [
+                "earth science",
+                "salinity/density",
+                "ocean chemistry",
+                "oceans",
+                "ocean optics",
+                "ocean temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/KIEBER_PHOTOCHEMISTRY/DATA001",
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
+            "temporal": "2002-06-24T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Photochemistry measurements made along the mid-Atlantic and New England coastal regions"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L2_05kmAPro-Standard-V4-51",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L2_05kmAPro-Standard-V4-51. https://www.doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L2_05kmAPro-Standard-V4-51.",
-            "issued": "2006-06-12",
-            "temporal": "2006-06-11T00:00:00Z/2023-06-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-29",
-            "keyword": [
-                "earth science",
-                "aerosols",
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
-            "identifier": "C2667982873-LARC_ASDC",
             "description": "CAL_LID_L2_05kmAPro-Standard-V4-51 is the Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) Lidar Level 2 Aerosol Profile, Version 4-51 data product. Data for this product was collected using the CALIPSO Cloud-Aerosol Lidar with Orthogonal Polarization (CALIOP) instrument. \r\n\r\nThe CALIPSO satellite comprises three instruments: CALIOP, Imaging Infrared Radiometer (IIR), and Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency CNES (Centre National d'Etudes Spatiales).\r\n\r\nCALIPSO was launched on April 28, 2006, to study the impact of clouds and aerosols on the Earth's radiation budget and climate. From June 13, 2006, to September 13, 2018, CALIPSO was part of the A-Train constellation for coincident Earth Observations. After September 13, 2018, the satellite was lowered from 705 to 688 km to resume flying in formation with CloudSat, heretofore called the C-Train.",
-            "title": "CALIPSO Lidar Level 2 Aerosol Profile, V4-51",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCALIOP%2FCALIPSO%2FCAL_LID_L2_05kmAPro-Standard-V4-51",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCALIOP%2FCALIPSO%2FCAL_LID_L2_05kmAPro-Standard-V4-51",
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
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/products/CALIPSO_DPC_Rev4x95.pdf",
-                    "description": "CALIPSO - Data Management System - Data Products Catalog - Release 4.95",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO - Data Management System - Data Products Catalog - Release 4.95",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/products/CALIPSO_DPC_Rev4x95.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/qs/cal_lid_l2_all_v4-51.php",
-                    "description": "CALIPSO V4.51 Lidar Level 2 Data Quality Summary",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO V4.51 Lidar Level 2 Data Quality Summary",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/qs/cal_lid_l2_all_v4-51.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data quality document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/data_desc/cal_lid_l2_profile_v4-51_desc.php",
-                    "description": "CALIPSO V4.51 Lidar Level 2 Data Description Summary",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO V4.51 Lidar Level 2 Data Description Summary",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/data_desc/cal_lid_l2_profile_v4-51_desc.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L2_05kmAPro-Standard-V4-51",
-                    "description": "DOI data set landing page for CAL_LID_L2_05kmAPro-Standard-V4-51_V4-51",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CAL_LID_L2_05kmAPro-Standard-V4-51_V4-51",
+                    "downloadURL": "https://www.doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L2_05kmAPro-Standard-V4-51",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2667982873-LARC_ASDC",
-                    "description": "Earthdata Search for CAL_LID_L2_05kmAPro-Standard-V4-51_V4-51 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data).",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CAL_LID_L2_05kmAPro-Standard-V4-51_V4-51 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data).",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2667982873-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/products/lidar/browse_images/std_v451_index.php",
-                    "description": "CALIPSO - Browse Images",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO - Browse Images",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/products/lidar/browse_images/std_v451_index.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/browse/index.php",
-                    "description": "CALIPSO - Browse Image Tutorial",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO - Browse Image Tutorial",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/browse/index.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product usage"
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
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/bibliographies.php",
-                    "description": "CALIPSO \u2013 List of Publications",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO \u2013 List of Publications",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/bibliographies.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/tools/data_avail/",
-                    "description": "CALIPSO \u2013 Data Availability Site",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO \u2013 Data Availability Site",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/tools/data_avail/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's processing history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/products/inventory.php",
-                    "description": "CALIPSO \u2013 Data Inventory",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO \u2013 Data Inventory",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/products/inventory.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's processing history"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CALIPSO/LID_L2_05kmAPro-Standard-V4-51/",
-                    "description": "ASDC Direct Data Download for CAL_LID_L2_05kmAPro-Standard-V4-51_V4-51",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CAL_LID_L2_05kmAPro-Standard-V4-51_V4-51",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CALIPSO/LID_L2_05kmAPro-Standard-V4-51/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CALIPSO/LID_L2_05kmAPro-Standard-V4-51/contents.html",
-                    "description": "OPeNDAP data access for CAL_LID_L2_05kmAPro-Standard-V4-51_V4-51",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CAL_LID_L2_05kmAPro-Standard-V4-51_V4-51",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CALIPSO/LID_L2_05kmAPro-Standard-V4-51/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2667982873-LARC_ASDC",
+            "issued": "2006-06-12",
+            "keyword": [
+                "earth science",
+                "aerosols",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L2_05kmAPro-Standard-V4-51",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-06-29",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2006-06-11T00:00:00Z/2023-06-30T23:59:59.999Z",
             "theme": [
                 "CALIPSO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CALIPSO Lidar Level 2 Aerosol Profile, V4-51"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-ACCEL-5-PROFILE-V1.0",
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
-                "mars global surveyor"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "TBD",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-accel-5-profile-v1.0_5e5a-77iv",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars global surveyor"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-ACCEL-5-PROFILE-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-accel-5-profile-v1.0_5e5a-77iv",
-            "description": "TBD",
-            "title": "MGS MARS ACCELEROMETER ORBIT PROFILES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MGS MARS ACCELEROMETER ORBIT PROFILES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1356506694-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Tropical Rainfall Measuring Mission (TRMM). 2007-01-01. TRMM_2A55UW. TRMM Ground Validation Radar Site 3D Reflectivity L2 1 hour V7. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/TRMM_2A55UW_7.html.",
-            "issued": "2011-07-01",
-            "temporal": "1999-01-09T00:00:00Z/2003-12-31T23:59:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-05-09",
-            "keyword": [
-                "precipitation",
-                "atmosphere",
-                "earth science",
-                "spectral/engineering",
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
-            "identifier": "C1356506694-GES_DISC",
-            "description": "This dataset is part of the University of Washington TRMM Ground Validation products.\n\nMultiple-level cartesian grid containing output of NCAR SPRINT interpolation of CZ and VR fields of 1C51UW. Horizontal extent is 150x150km and resolution is 2km. Vertical range is 2-15km and resolution is 1km. Unlike other products, 2A55UW is not created for every volume but only for volumes of interest. These are defined as volumes within +/-15 minutes of overpass times and volumes with significant rainfall (areal rainfall rate greater or equal  0.15mm/hr).\n\nA key component of the TRMM project is the Ground Validation (GV) effort which consists of collecting data from ground-based radar, rain gauges and disdrometers. The data is quality-controlled, and then validation products are produced for comparison with TRMM satellite products.\n\nThe four primary GV sites are:\n\n+ Darwin, Australia; \n+ Houston, Texas; \n+ Kwajalein, Republic of the Marshall Islands;\n+ Melbourne, Florida. \n\nA significant effort is also being supported at NASA Wallops Flight Facility (WFF) and vicinity to provide high quality, long-term measurements of rain rates (via a network of rain gauges collocated with National Weather Service gauges), as well as drop size distributions (DSD) using a variety of instruments, including impact-type Joss Waldvogel, laser-optical Parsivel, as well as two-dimensional video disdrometers.  DSD measurements are also being collected at Melbourne and Kwajalein using Joss-Waldvogel disdrometers.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "TRMM_2A55UW",
             "creator": "Tropical Rainfall Measuring Mission (TRMM)",
-            "title": "TRMM Ground Validation Radar Site 3D Reflectivity L2 1 hour V7 (TRMM_2A55UW) at GES DISC",
-            "graphic-preview-file": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_GV_L2/TRMM_2A55.7/2008/033/2A55_BR.080202.12.KWAJ.7.PNG",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset is part of the University of Washington TRMM Ground Validation products.\n\nMultiple-level cartesian grid containing output of NCAR SPRINT interpolation of CZ and VR fields of 1C51UW. Horizontal extent is 150x150km and resolution is 2km. Vertical range is 2-15km and resolution is 1km. Unlike other products, 2A55UW is not created for every volume but only for volumes of interest. These are defined as volumes within +/-15 minutes of overpass times and volumes with significant rainfall (areal rainfall rate greater or equal  0.15mm/hr).\n\nA key component of the TRMM project is the Ground Validation (GV) effort which consists of collecting data from ground-based radar, rain gauges and disdrometers. The data is quality-controlled, and then validation products are produced for comparison with TRMM satellite products.\n\nThe four primary GV sites are:\n\n+ Darwin, Australia; \n+ Houston, Texas; \n+ Kwajalein, Republic of the Marshall Islands;\n+ Melbourne, Florida. \n\nA significant effort is also being supported at NASA Wallops Flight Facility (WFF) and vicinity to provide high quality, long-term measurements of rain rates (via a network of rain gauges collocated with National Weather Service gauges), as well as drop size distributions (DSD) using a variety of instruments, including impact-type Joss Waldvogel, laser-optical Parsivel, as well as two-dimensional video disdrometers.  DSD measurements are also being collected at Melbourne and Kwajalein using Joss-Waldvogel disdrometers.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -186786,500 +186762,533 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRMM_2A55UW_7.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRMM_2A55UW_7.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_GV_L2/TRMM_2A55UW.7",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_GV_L2/TRMM_2A55UW.7",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRMM_2A55UW",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRMM_2A55UW",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://pmm.nasa.gov",
-                    "description": "PMM Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "PMM Project Home Page",
+                    "downloadURL": "https://pmm.nasa.gov",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://atmos.washington.edu/gcg/MG/KWAJ/UWproductsOnDAAC.html",
-                    "description": "File specification document",
                     "@type": "dcat:Distribution",
+                    "description": "File specification document",
+                    "downloadURL": "https://atmos.washington.edu/gcg/MG/KWAJ/UWproductsOnDAAC.html",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://atmos.washington.edu/gcg/MG/KWAJ/GV.html",
-                    "description": "TRMM Field Campaign Project Page",
                     "@type": "dcat:Distribution",
+                    "description": "TRMM Field Campaign Project Page",
+                    "downloadURL": "https://atmos.washington.edu/gcg/MG/KWAJ/GV.html",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://atmos.washington.edu/gcg/MG/KWAJ/NewProductDocumentation010919.pdf",
-                    "description": "ALGORITHM THEORETICAL BASIS DOCUMENT (ATBD)",
                     "@type": "dcat:Distribution",
+                    "description": "ALGORITHM THEORETICAL BASIS DOCUMENT (ATBD)",
+                    "downloadURL": "https://atmos.washington.edu/gcg/MG/KWAJ/NewProductDocumentation010919.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
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
+            "graphic-preview-file": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_GV_L2/TRMM_2A55.7/2008/033/2A55_BR.080202.12.KWAJ.7.PNG",
+            "identifier": "C1356506694-GES_DISC",
+            "issued": "2011-07-01",
+            "keyword": [
+                "precipitation",
+                "atmosphere",
+                "earth science",
+                "spectral/engineering",
+                "radar"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1356506694-GES_DISC.html",
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
+            "series-name": "TRMM_2A55UW",
             "spatial": "-180.0 -40.0 180.0 40.0",
+            "temporal": "1999-01-09T00:00:00Z/2003-12-31T23:59:00Z",
             "theme": [
                 "TRMM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TRMM Ground Validation Radar Site 3D Reflectivity L2 1 hour V7 (TRMM_2A55UW) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4KK98PS",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "China in Time and Space - CITAS - University of Washington, Chinese Academy of Surveying and Mapping - CASM, and Center for International Earth Science Information Network - CIESIN. 1997-02-28. China Dimensions Data Collection: GuoBiao (GB) Codes for the Administrative Divisions of the Peoples Republic of China. Version 1.00. Saginaw, MI. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H4KK98PS. https://doi.org/10.7927/H4KK98PS.",
-            "issued": "1997-02-28",
-            "temporal": "1982-01-01T00:00:00Z/1992-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "1997-02-28",
-            "references": [
-                "https://doi.org/10.7927/H4RB72JW",
-                "https://doi.org/10.7927/H4QC01D2",
-                "https://doi.org/10.7927/H4C24TCF",
-                "https://doi.org/10.7927/H4GT5K3V",
-                "https://doi.org/10.7927/H4MK69T5",
-                "https://doi.org/10.7927/H4ZW1HVD",
-                "https://doi.org/10.7927/H47D2S2F",
-                "https://doi.org/10.7927/H43N21B3",
-                "https://doi.org/10.7927/H4V40S4D",
-                "https://doi.org/10.7927/H4FT8HZ2"
-            ],
-            "keyword": [
-                "earth science",
-                "human dimensions",
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
-            "identifier": "C179001909-SEDAC",
-            "description": "The GuoBiao (GB) Codes for the Administrative Divisions of the People's Republic of China consists of geographic codes for the administrative divisions of China. The data includes provinces (autonomous regions, municipalities directly under the Central Government), prefectures (prefecture-level cities, autonomous prefectures, leagues), and counties (districts, county-level cities, autonomous counties, banners) for 1 January 1982 to 31 December 1992.\n\nThis data set is produced in collaboration with the Chinese Academy of Surveying and Mapping (CASM), University of Washington as part of the China in Time and Space (CITAS) project, and the Columbia University Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "Saginaw, MI",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "China in Time and Space - CITAS - University of Washington, Chinese Academy of Surveying and Mapping - CASM, and Center for International Earth Science Information Network - CIESIN",
-            "title": "China Dimensions Data Collection: GuoBiao (GB) Codes for the Administrative Divisions of the Peoples Republic of China",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/cddc/cddc-china-guobiao-codes-admin-divisions/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The GuoBiao (GB) Codes for the Administrative Divisions of the People's Republic of China consists of geographic codes for the administrative divisions of China. The data includes provinces (autonomous regions, municipalities directly under the Central Government), prefectures (prefecture-level cities, autonomous prefectures, leagues), and counties (districts, county-level cities, autonomous counties, banners) for 1 January 1982 to 31 December 1992.\n\nThis data set is produced in collaboration with the Chinese Academy of Surveying and Mapping (CASM), University of Washington as part of the China in Time and Space (CITAS) project, and the Columbia University Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4KK98PS",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4KK98PS",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/cddc/cddc-china-guobiao-codes-admin-divisions/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/cddc/cddc-china-guobiao-codes-admin-divisions/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/cddc-china-guobiao-codes-admin-divisions/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/cddc-china-guobiao-codes-admin-divisions/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/cddc-china-guobiao-codes-admin-divisions/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/cddc-china-guobiao-codes-admin-divisions/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/cddc-china-guobiao-codes-admin-divisions",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/cddc-china-guobiao-codes-admin-divisions",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/cddc/cddc-china-guobiao-codes-admin-divisions/sedac-logo.jpg",
+            "identifier": "C179001909-SEDAC",
+            "issued": "1997-02-28",
+            "keyword": [
+                "earth science",
+                "human dimensions",
+                "boundaries"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4KK98PS",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1997-02-28",
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
+                "https://doi.org/10.7927/H4MK69T5",
+                "https://doi.org/10.7927/H4ZW1HVD",
+                "https://doi.org/10.7927/H47D2S2F",
+                "https://doi.org/10.7927/H43N21B3",
+                "https://doi.org/10.7927/H4V40S4D",
+                "https://doi.org/10.7927/H4FT8HZ2"
+            ],
+            "release-place": "Saginaw, MI",
             "spatial": "73.0 18.0 135.0 54.0",
+            "temporal": "1982-01-01T00:00:00Z/1992-12-31T00:00:00Z",
             "theme": [
                 "CDDC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "China Dimensions Data Collection: GuoBiao (GB) Codes for the Administrative Divisions of the Peoples Republic of China"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/19",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Fritschen, L. J. 1994. Bowen Ratio Surf[ace]. Flux: Fritschen (FIFE). Data set. Available on-line [http://www.daac.ornl.gov] from Oak Ridge National Laboratory Distributed Active Archive Center, Oak Ridge, Tennessee, U.S.A. Also published in D. E. Strebel, D. R. Landis, K. F. Huemmrich, and B. W. Meeson (eds.), Collected Data of the First ISLSCP Field Experiment, Vol. 1: Surface Observations and Non-Image Data Sets. CD-ROM. National Aeronautics and Space Administration, Goddard Space Flight Center, Greenbelt, Maryland, U.S.A. (available from http://www.daac.ornl.gov). doi:10.3334/ORNLDAAC/19",
-            "issued": "2024-05-05",
-            "temporal": "1987-05-26T00:00:00Z/1989-08-14T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-07",
-            "keyword": [
-                "land surface",
-                "soils",
-                "earth science",
-                "atmospheric winds",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "atmospheric radiation",
-                "atmosphere",
-                "agriculture"
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
-            "identifier": "C2979977869-ORNL_CLOUD",
             "description": "Evaluation of surface radiation and energy budget stations for FIFE",
-            "graphic-preview-description": "Browse Image",
-            "title": "Bowen Ratio Surf. Flux: Fritschen (FIFE)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/fife_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F19",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F19",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_sur_flux_30_min_brl/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_sur_flux_30_min_brl/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/Bowen_Ratio_Fritschen.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/Bowen_Ratio_Fritschen.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/19",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/19",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_flux_30_min_brl/comp/Bowen_Ratio_Fritschen.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_flux_30_min_brl/comp/Bowen_Ratio_Fritschen.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_flux_30_min_brl/comp/sflux_bl.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_flux_30_min_brl/comp/sflux_bl.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_flux_30_min_brl/comp/sf_30min.tdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_flux_30_min_brl/comp/sf_30min.tdf",
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
+            "identifier": "C2979977869-ORNL_CLOUD",
+            "issued": "2024-05-05",
+            "keyword": [
+                "land surface",
+                "soils",
+                "earth science",
+                "atmospheric winds",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "atmospheric radiation",
+                "atmosphere",
+                "agriculture"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/19",
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
             "spatial": "-96.61 38.98 -96.45 39.11",
+            "temporal": "1987-05-26T00:00:00Z/1989-08-14T23:59:59Z",
             "theme": [
                 "FIFE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Bowen Ratio Surf. Flux: Fritschen (FIFE)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/402",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Trumbore, S.E., J.W. Harden, E. Sundquist, and G.C. Winston. 1998. BOREAS TGB-12 Soil Carbon Data: NSA. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/402",
-            "issued": "2023-11-22",
-            "temporal": "1993-08-01T00:00:00Z/1996-07-21T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-28",
-            "keyword": [
-                "earth science",
-                "soils",
-                "land surface",
-                "atmosphere",
-                "atmospheric temperature",
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
-            "identifier": "C2808089794-ORNL_CLOUD",
             "description": "Contains the soil carbon data collected by TGB-12 in the northern study area.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS TGB-12 Soil Carbon Data: NSA",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F402",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F402",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TGB/tgb12scd/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TGB/tgb12scd/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TGB12_Soil_Carbon.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TGB12_Soil_Carbon.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/402",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/402",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb12scd/comp/tgb12scd.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb12scd/comp/tgb12scd.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb12scd/comp/TGB12_Soil_Carbon.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb12scd/comp/TGB12_Soil_Carbon.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb12scd/comp/TGB12_Soil_Carbon.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb12scd/comp/TGB12_Soil_Carbon.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb12scd/comp/TGB12_Soil_Carbon.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb12scd/comp/TGB12_Soil_Carbon.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
-                    "title": "Get a related visualization"
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
+                    "mediaType": "image/png",
+                    "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
+            "identifier": "C2808089794-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "earth science",
+                "soils",
+                "land surface",
+                "atmosphere",
+                "atmospheric temperature",
+                "land use/land cover"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/402",
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
             "spatial": "-98.95 55.07 -97.7 55.93",
+            "temporal": "1993-08-01T00:00:00Z/1996-07-21T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS TGB-12 Soil Carbon Data: NSA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ICESAT/GLAS/DATA212",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "GLAS/ICESat L2 Ocean Altimetry Data (HDF5) V034. Version 034. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/ICESAT/GLAS/DATA212.",
-            "issued": "2003-02-20",
-            "temporal": "2003-02-20T00:00:00Z/2009-10-11T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2009-10-11",
-            "keyword": [
-                "cryosphere",
-                "oceans",
-                "sea surface topography",
-                "earth science",
-                "sea ice"
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
-            "identifier": "C2153552369-NSIDC_CPRD",
             "description": "GLAH06 is used in conjunction with GLAH05 to create the Level-2 altimetry products. Level-2 altimetry data provide surface elevations for ice sheets (GLAH12), sea ice (GLAH13), land (GLAH14), and oceans (GLAH15). Data also include the laser footprint geolocation and reflectance, as well as geodetic, instrument, and atmospheric corrections for range measurements. The Level-2 elevation products, are regional products archived at 14 orbits per granule, starting and stopping at the same demarcation (\u00b1 50\u00b0 latitude) as GLAH05 and GLAH06. Each regional product is processed with algorithms specific to that surface type. Surface type masks define which data are written to each of the products. If any data within a given record fall within a specific mask, the entire record is written to the product. Masks can overlap: for example, non-land data in the sea ice region may be written to the sea ice and ocean products. This means that an algorithm may write the same data to more than one Level-2 product. In this case, different algorithms calculate the elevations in their respective products. The surface type masks are versioned and archived at NSIDC, so users can tell which data to expect in each product.  Each data granule has an associated browse product.",
-            "title": "GLAS/ICESat L2 Ocean Altimetry Data (HDF5) V034",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FICESAT%2FGLAS%2FDATA212",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FICESAT%2FGLAS%2FDATA212",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GLAH15+V034",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GLAH15+V034",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ICESAT/GLAS/DATA212",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/ICESAT/GLAS/DATA212",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ICESAT/GLAS/DATA212",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ICESAT/GLAS/DATA212",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2153552369-NSIDC_CPRD",
+            "issued": "2003-02-20",
+            "keyword": [
+                "cryosphere",
+                "oceans",
+                "sea surface topography",
+                "earth science",
+                "sea ice"
+            ],
+            "landingPage": "https://doi.org/10.5067/ICESAT/GLAS/DATA212",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2009-10-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -86.0 180.0 86.0",
+            "temporal": "2003-02-20T00:00:00Z/2009-10-11T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GLAS/ICESat L2 Ocean Altimetry Data (HDF5) V034"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=P12-V-ORAD-4-ALT%2FRAD-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set consists of groups of measurements made by the Radar Mapper experiment on the Pioneer Venus Orbiter spacecraft. The measurements were made during each approximately 12-second spacecraft rotation period for a period of 32 minutes on either side of periapsis, when the range to the surface was less than about 4500 kilometers. During those 12 seconds, up to 8 measurements were made: (a) cold-sky received calibration when the antenna pointed to the zenith, (b) 'early' imaging, when the antenna pointer at an angle of between 10 and 40 degrees from nadir, (c) planetary thermal noise temperature when the antenna pointed to the nadir (d) one altimetry measurement, or (d-g) four altimetry measurements, and (h) 'late' imaging, when the antenna again pointed at an angle of between 10 and 40 degrees from nadir, but on the other side from 'early' imaging.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.p12-v-orad-4-alt-rad-v1.0_5ebt-mssg",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "venus",
                 "pre-magellan",
                 "pioneer"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=P12-V-ORAD-4-ALT%2FRAD-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.p12-v-orad-4-alt-rad-v1.0_5ebt-mssg",
-            "description": "This data set consists of groups of measurements made by the Radar Mapper experiment on the Pioneer Venus Orbiter spacecraft. The measurements were made during each approximately 12-second spacecraft rotation period for a period of 32 minutes on either side of periapsis, when the range to the surface was less than about 4500 kilometers. During those 12 seconds, up to 8 measurements were made: (a) cold-sky received calibration when the antenna pointed to the zenith, (b) 'early' imaging, when the antenna pointer at an angle of between 10 and 40 degrees from nadir, (c) planetary thermal noise temperature when the antenna pointed to the nadir (d) one altimetry measurement, or (d-g) four altimetry measurements, and (h) 'late' imaging, when the antenna again pointed at an angle of between 10 and 40 degrees from nadir, but on the other side from 'early' imaging.",
-            "title": "P12 V ORBITING RADAR RESAMPLED ALTIMETER/RADIOMETER V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "P12 V ORBITING RADAR RESAMPLED ALTIMETER/RADIOMETER V1.0"
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
+            "description": "Exp: FAITH Hill 3-D Separated Flow. This web page provides data from experiments that may be useful for the validation of turbulence models. This resource is expected to grow gradually over time. All data herein arepublicly available.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://turbmodels.larc.nasa.gov/Other_exp_Data/FAITH_Hill/Cobra_data_vel.tar.gz",
+                    "mediaType": "application/x-gzip"
+                }
             ],
+            "identifier": "NASA-853__1",
+            "issued": "2018-06-25",
             "keyword": [
                 "validation",
                 "separation",
@@ -187290,388 +187299,381 @@
                 "turbulence",
                 "hill"
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
-            "identifier": "NASA-853__1",
-            "description": "Exp: FAITH Hill 3-D Separated Flow. This web page provides data from experiments that may be useful for the validation of turbulence models. This resource is expected to grow gradually over time. All data herein arepublicly available.",
-            "title": "Turbulence Models: Data from Other Experiments: FAITH Hill 3-D Separated Flow",
-            "programCode": [
-                "026:023"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://turbmodels.larc.nasa.gov/Other_exp_Data/FAITH_Hill/Cobra_data_vel.tar.gz",
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
+            "title": "Turbulence Models: Data from Other Experiments: FAITH Hill 3-D Separated Flow"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL-MIDAS-3-GRND-REF-2015-V1.0",
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
+            "description": "The Micro-Imaging Dust Analysis System (MIDAS) is an instrument on the\nROSETTA Orbiter that will provide 3D images and statistical parameters\nof pristine cometary particles, collected in the vicinity of comet\n67P/Churyumov-Gerasimenko. This data set includes reference\nmeasurement\ndata acquired with the flight spare unit (FS) on ground, which was\nused\nfor improving the accuracy of the images gathered by the actual flight\nunit and to develop adequate measuement procedures for flight. The\ntest\ndata was collected during several years and spawns several data sets,\nin order to keep the individual data set size on a reasonable level.\nThe current dataset contains data from 2015.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-midas-3-grnd-ref-2015-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "calibration",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL-MIDAS-3-GRND-REF-2015-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-midas-3-grnd-ref-2015-v1.0",
-            "description": "The Micro-Imaging Dust Analysis System (MIDAS) is an instrument on the\nROSETTA Orbiter that will provide 3D images and statistical parameters\nof pristine cometary particles, collected in the vicinity of comet\n67P/Churyumov-Gerasimenko. This data set includes reference\nmeasurement\ndata acquired with the flight spare unit (FS) on ground, which was\nused\nfor improving the accuracy of the images gathered by the actual flight\nunit and to develop adequate measuement procedures for flight. The\ntest\ndata was collected during several years and spawns several data sets,\nin order to keep the individual data set size on a reasonable level.\nThe current dataset contains data from 2015.",
-            "title": "ROSETTA-ORBITER CAL MIDAS 3 GRND REFERENCE 2015 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CAL MIDAS 3 GRND REFERENCE 2015 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4V69GJ5",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for International Earth Science Information Network - CIESIN - Columbia University. 2018-02-23. Global Fire Emissions Indicators, Country-Level Tabular Data: 1997-2015. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H4V69GJ5. https://doi.org/10.7927/H4V69GJ5.",
-            "issued": "2018-02-23",
-            "temporal": "1997-01-01T00:00:00Z/2015-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-02-23",
-            "references": [
-                "https://doi.org/10.7927/H400002V",
-                "https://doi.org/10.7927/H4KP803H",
-                "https://doi.org/10.1002/jgrg.20042"
-            ],
-            "keyword": [
-                "atmosphere",
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
-            "identifier": "C1457414586-SEDAC",
-            "description": "The Global Fire Emissions Indicators, Country-Level Tabular Data: 1997-2015 contains country tabulations from 1997 to 2015 for the total area burned (hectares) and total carbon content (tons). The annual total area burned is for all fire types per country. There are two groups of total carbon content (TCC), annual totals for all six fire types per country and annual totals for each of six fire types per country which include Agricultural, Boreal, Tropical Deforestation, Peat, Savanna, and Temperate forest fires.",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Center for International Earth Science Information Network - CIESIN - Columbia University",
-            "title": "Global Fire Emissions Indicators, Country-Level Tabular Data: 1997-2015",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/sdei/sdei-global-fire-emissions-indicators-country-level-1997-2015/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Global Fire Emissions Indicators, Country-Level Tabular Data: 1997-2015 contains country tabulations from 1997 to 2015 for the total area burned (hectares) and total carbon content (tons). The annual total area burned is for all fire types per country. There are two groups of total carbon content (TCC), annual totals for all six fire types per country and annual totals for each of six fire types per country which include Agricultural, Boreal, Tropical Deforestation, Peat, Savanna, and Temperate forest fires.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4V69GJ5",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4V69GJ5",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/sdei/sdei-global-fire-emissions-indicators-country-level-1997-2015/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/sdei/sdei-global-fire-emissions-indicators-country-level-1997-2015/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdei-global-fire-emissions-indicators-country-level-1997-2015/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdei-global-fire-emissions-indicators-country-level-1997-2015/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/sdei-global-fire-emissions-indicators-country-level-1997-2015/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/sdei-global-fire-emissions-indicators-country-level-1997-2015/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdei-global-fire-emissions-indicators-country-level-1997-2015",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdei-global-fire-emissions-indicators-country-level-1997-2015",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/sdei/sdei-global-fire-emissions-indicators-country-level-1997-2015/sedac-logo.jpg",
+            "identifier": "C1457414586-SEDAC",
+            "issued": "2018-02-23",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "air quality"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4V69GJ5",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-02-23",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H400002V",
+                "https://doi.org/10.7927/H4KP803H",
+                "https://doi.org/10.1002/jgrg.20042"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1997-01-01T00:00:00Z/2015-12-31T00:00:00Z",
             "theme": [
                 "SDEI",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Fire Emissions Indicators, Country-Level Tabular Data: 1997-2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3336-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-07-05T00:13:12 to 2012-07-05T02:18:09.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3336-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars express"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3336-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3336-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-07-05T00:13:12 to 2012-07-05T02:18:09.000.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3336 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3336 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-APXS-4%2F5-RDR-V1.0",
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
+            "description": "The MSL APXS RDR data set contains calibrated spectra and oxide weight percent data derived from observations of the APXS instrument aboard the Mars Science Laboratory rover. Two types of products are included: summed X-ray spectra in counts as a function of energy, and abundance data for a set of standard elements and oxides, derived from the summed spectra. Both product types are given as ASCII text files in comma-separated-value (CSV) format, suitable for reading with spreadsheet software.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-apxs-4-5-rdr-v1.0_5ehp-fx5s",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars science laboratory",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-APXS-4%2F5-RDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-apxs-4-5-rdr-v1.0_5ehp-fx5s",
-            "description": "The MSL APXS RDR data set contains calibrated spectra and oxide weight percent data derived from observations of the APXS instrument aboard the Mars Science Laboratory rover. Two types of products are included: summed X-ray spectra in counts as a function of energy, and abundance data for a set of standard elements and oxides, derived from the summed spectra. Both product types are given as ASCII text files in comma-separated-value (CSV) format, suitable for reading with spreadsheet software.",
-            "title": "MSL MARS ALPHA PARTICLE X-RAY SPECTROMETER 4/5 RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MSL MARS ALPHA PARTICLE X-RAY SPECTROMETER 4/5 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-ASTNAMES-DISCOVERY-V3.0",
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
+            "description": "This data set includes names, designations, and discovery circumstances for the numbered asteroids, sorted in order of catalog number.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-astnames-discovery-v3.0_5ejb-xe6g",
+            "issued": "2021-05-21",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-ASTNAMES-DISCOVERY-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-astnames-discovery-v3.0_5ejb-xe6g",
-            "description": "This data set includes names, designations, and discovery circumstances for the numbered asteroids, sorted in order of catalog number.",
-            "title": "ASTEROID NAMES AND DISCOVERY V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ASTEROID NAMES AND DISCOVERY V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amer2_mi_sci_calibrated&version=1.0",
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
-                "mars exploration rover"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This bundle contains calibrated data from the Microscopic Imager (MI) on Mars Exploration Rover 2 (Spirit). These data were produced by the science team.",
+            "identifier": "urn:nasa:pds:mer2_mi_sci_calibrated",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amer2_mi_sci_calibrated&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:mer2_mi_sci_calibrated",
-            "description": "This bundle contains calibrated data from the Microscopic Imager (MI) on Mars Exploration Rover 2 (Spirit). These data were produced by the science team.",
-            "title": "MER2 Microscopic Imager Science Calibrated Data Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MER2 Microscopic Imager Science Calibrated Data Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=M10-H-POS-6-M3-FLYBY-TRAJ-42SEC-V1.0",
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
-                "mercury",
-                "mariner 10"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.m10-h-pos-6-m3-flyby-traj-42sec-v1.0_5epc-drgx",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mercury",
+                "mariner 10"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=M10-H-POS-6-M3-FLYBY-TRAJ-42SEC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.m10-h-pos-6-m3-flyby-traj-42sec-v1.0_5epc-drgx",
-            "description": "not applicable",
-            "title": "MARINER 10 MERC POS M3 FLYBY TRAJ 42SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MARINER 10 MERC POS M3 FLYBY TRAJ 42SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Ago-pls-jup-fitted-parameters&version=1.0",
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
+            "description": "This bundle  consists of all of the fitted parameters (both good and bad) for fitting an  ion species to the Galileo Plasma Science Experiment (PLS) that were found during a grant  from NASA's Jupiter Data Analysis Program (NNX09AE03G). The 'good' results were used to  publish: Bagenal, F., R. J. Wilson, S. Siler, W. R. Paterson, and W. S. Kurth (2016),  Survey of Galileo plasma observations in Jupiter's plasma sheet,              J. Geophys. Res. Planets, 121, 871-894, doi:10.1002/2016JE005009.             Please cite this paper and this PDS bundle if you use this data. Please note: The data in this bundle have been reviewed by the coauthors of Bagenal, et al.  2016 and their method and figures passed the journal's peer review. These data have not yet completed PDS peer review, and are uncertified.",
+            "identifier": "urn:nasa:pds:go-pls-jup-fitted-parameters",
+            "issued": "2021-05-21",
+            "keyword": [
+                "pds"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Ago-pls-jup-fitted-parameters&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:go-pls-jup-fitted-parameters",
-            "description": "This bundle  consists of all of the fitted parameters (both good and bad) for fitting an  ion species to the Galileo Plasma Science Experiment (PLS) that were found during a grant  from NASA's Jupiter Data Analysis Program (NNX09AE03G). The 'good' results were used to  publish: Bagenal, F., R. J. Wilson, S. Siler, W. R. Paterson, and W. S. Kurth (2016),  Survey of Galileo plasma observations in Jupiter's plasma sheet,              J. Geophys. Res. Planets, 121, 871-894, doi:10.1002/2016JE005009.             Please cite this paper and this PDS bundle if you use this data. Please note: The data in this bundle have been reviewed by the coauthors of Bagenal, et al.  2016 and their method and figures passed the journal's peer review. These data have not yet completed PDS peer review, and are uncertified.",
-            "title": "Galileo Orbiter Plasma Science Experiment Jupiter Fitted Parameters Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Galileo Orbiter Plasma Science Experiment Jupiter Fitted Parameters Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-X-HRIV-2-EPOXI-EXOPLANETS-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set set contains raw images of eight known transiting extrasolar planetary systems (hot Jupiters) acquired by the Deep Impact High Resolution Visible CCD during the EPOCh phase of the EPOXI mission. From 22 January through 31 August 2008 the HRIV CCD collected over 172,000 usable, photometric-quality visible light images of these transiting planet systems: HAT-P-4, HAT-P-7, GJ 436, TrES-2, TrES-3, XO-2, XO-3, and WASP-3. Time series of continuous 50-second integrations were used with the clear filter (#6) to observe each system for about three weeks, typically covering five or more transits as well as secondary eclipses. An exception was XO-3 which was only observed briefly due to the spacecraft entering safe mode. The transiting planet systems were observed in the integrated light of the planet and star; no spatially resolved image of the planet was possible.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-x-hriv-2-epoxi-exoplanets-v1.0_5euy-w54f",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "xo-3",
                 "epoxi",
@@ -187683,1568 +187685,1548 @@
                 "wasp-3",
                 "xo-2"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-X-HRIV-2-EPOXI-EXOPLANETS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-x-hriv-2-epoxi-exoplanets-v1.0_5euy-w54f",
-            "description": "This data set set contains raw images of eight known transiting extrasolar planetary systems (hot Jupiters) acquired by the Deep Impact High Resolution Visible CCD during the EPOCh phase of the EPOXI mission. From 22 January through 31 August 2008 the HRIV CCD collected over 172,000 usable, photometric-quality visible light images of these transiting planet systems: HAT-P-4, HAT-P-7, GJ 436, TrES-2, TrES-3, XO-2, XO-3, and WASP-3. Time series of continuous 50-second integrations were used with the clear filter (#6) to observe each system for about three weeks, typically covering five or more transits as well as secondary eclipses. An exception was XO-3 which was only observed briefly due to the spacecraft entering safe mode. The transiting planet systems were observed in the integrated light of the planet and star; no spatially resolved image of the planet was possible.",
-            "title": "EPOXI EXOPLANET TRANSIT OBS - HRIV RAW IMAGES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "EPOXI EXOPLANET TRANSIT OBS - HRIV RAW IMAGES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0035-5-SDSSTAX-V1.1",
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
+            "description": "The Sloan Digital Sky Survey Moving Object Catalog (SDSS-MOC) is a large data set that provides five-filter magnitudes and astrometric information for all moving objects identified in the SDSS images (Izevic et al., 2010). The photometric observations were classified by Carvano et al. (2010) into nine taxonomic classes: Vp, Op, Qp, Sp, Ap, Lp, Dp, Xp and Cp, which are related to the classes and complexes of Bus Taxonomy (Bus & Binzel, 2002b). This data set is contains the taxonomic classification of each SDSS detections and its compilation for each observed asteroid.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0035-5-sdsstax-v1.1_5ew8-z3nb",
+            "issued": "2018-06-26",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0035-5-SDSSTAX-V1.1",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0035-5-sdsstax-v1.1_5ew8-z3nb",
-            "description": "The Sloan Digital Sky Survey Moving Object Catalog (SDSS-MOC) is a large data set that provides five-filter magnitudes and astrometric information for all moving objects identified in the SDSS images (Izevic et al., 2010). The photometric observations were classified by Carvano et al. (2010) into nine taxonomic classes: Vp, Op, Qp, Sp, Ap, Lp, Dp, Xp and Cp, which are related to the classes and complexes of Bus Taxonomy (Bus & Binzel, 2002b). This data set is contains the taxonomic classification of each SDSS detections and its compilation for each observed asteroid.",
-            "title": "SDSS-BASED ASTEROID TAXONOMY V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "SDSS-BASED ASTEROID TAXONOMY V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1181",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Saatchi, S.S. 2013. LBA-ECO LC-15 SRTM30 Digital Elevation Model Data, Amazon Basin: 2000. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1181",
-            "issued": "2020-12-03",
-            "temporal": "2000-02-11T00:00:00Z/2000-02-22T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-18",
-            "keyword": [
-                "earth science",
-                "topography",
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
-            "identifier": "C2768953357-ORNL_CLOUD",
             "description": "This dataset provides a subset of the SRTM30 Digital Elevation Model (DEM) elevation and standard deviation data for the Amazon Basin. SRTM30 is a near-global digital elevation model (DEM) comprising a combination of data from the Shuttle Radar Topography Mission (SRTM), flown in February, 2000, and the earlier U.S. Geological Survey's GTOPO30 data set. The SRTM30 resolution is 30 arc-sec or about 1 km. In processing the SRTM data, to combine with GTOPO30, the data were resampled from 3 arc-sec to 30 arc-sec. Provided here are the mean elevation and the standard deviation (STD) of the data points used in the averaging. The STD is thus an indication of topographic roughness useful in some applications.",
-            "graphic-preview-description": "This figure depicts the data in the file SA_srtm_mosaic_30arcsec_reg_hgt.tif.",
-            "title": "LBA-ECO LC-15 SRTM30 Digital Elevation Model Data, Amazon Basin: 2000",
-            "graphic-preview-file": "https://daac.ornl.gov/LBA/guides/LC15_SRTM_Topography_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1181",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1181",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC15_SRTM_Topography/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC15_SRTM_Topography/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC15_SRTM_Topography.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC15_SRTM_Topography.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1181",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1181",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC15_SRTM_Topography/comp/LC15_SRTM_Topography.pdf",
-                    "description": "LBA-ECO LC-15 SRTM30 Digital Elevation Model Data, Amazon Basin: 2000: LC15_SRTM_Topography.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "LBA-ECO LC-15 SRTM30 Digital Elevation Model Data, Amazon Basin: 2000: LC15_SRTM_Topography.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC15_SRTM_Topography/comp/LC15_SRTM_Topography.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC15_SRTM_Topography_Fig1.png",
-                    "description": "This figure depicts the data in the file SA_srtm_mosaic_30arcsec_reg_hgt.tif.",
                     "@type": "dcat:Distribution",
+                    "description": "This figure depicts the data in the file SA_srtm_mosaic_30arcsec_reg_hgt.tif.",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC15_SRTM_Topography_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "This figure depicts the data in the file SA_srtm_mosaic_30arcsec_reg_hgt.tif.",
+            "graphic-preview-file": "https://daac.ornl.gov/LBA/guides/LC15_SRTM_Topography_Fig1.png",
+            "identifier": "C2768953357-ORNL_CLOUD",
+            "issued": "2020-12-03",
+            "keyword": [
+                "earth science",
+                "topography",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1181",
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
             "spatial": "-82.72 -21.13 -33.57 13.86",
+            "temporal": "2000-02-11T00:00:00Z/2000-02-22T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO LC-15 SRTM30 Digital Elevation Model Data, Amazon Basin: 2000"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-ALICE-3-PLUTOCRUISE-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Calibrated data taken by the New Horizons         Alice Ultraviolet Imaging Spectrograph                                 instrument during the                                                    pluto cruise                                                           mission phase.  This is VERSION 2.0 of this data set.                    ALICE Activities Overview at Annual CheckOuts (ACOs) during the          Pluto Cruise mission phase started with the standard WakeUp              sequence (memory/code checks, aperture door performance test,            pixelhack issue verification, 24 hours of decontamination and            three one hour dark observations) and finished with the standard         Button-Up sequence (code and parameter refresh).  Other activities       (with targets as noted) were calibrations for flux (Spica,               rho-Leo, gamma-Grus, HD93521, Sun in Solar OCcultation Channel,          SOCC), flatfield (rho-Leo), airglow scattered light and SOCC             pointing calibrations (Spica, zeta-Pup), SOCC flat (Sun), dark sky       stares, spinning dark observations (in some cases the Sun strobes        through the slit), pointing and short wavelength calibration             (HD93521), InterPlanetary Medium (IPM) histograms and pixellist          observations, dual target tests (HD214680 = 8 Lac, HD214168 = 10         Lac), MEV Solar Wind (HEET) baseine observation, Pluto encounter         rehearsals, and instrument interference tests.                           The changes in Version 2.0 were re-running of the ancillary data         in the data product, updated geometry from newer SPICE kernels,          minor editing of the documentation, catalogs, etc., and resolution       of liens from the December, 2014 review, plus those from the May,        2016 review of the Pluto Encounter data sets.                            New observations added with this version (V2.0) include IPM              histogram scans in December, 2014, which failed.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-alice-3-plutocruise-v2.0_5eym-q2ab",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "new horizons",
                 "sun",
                 "calibration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-ALICE-3-PLUTOCRUISE-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-alice-3-plutocruise-v2.0_5eym-q2ab",
-            "description": "This data set contains Calibrated data taken by the New Horizons         Alice Ultraviolet Imaging Spectrograph                                 instrument during the                                                    pluto cruise                                                           mission phase.  This is VERSION 2.0 of this data set.                    ALICE Activities Overview at Annual CheckOuts (ACOs) during the          Pluto Cruise mission phase started with the standard WakeUp              sequence (memory/code checks, aperture door performance test,            pixelhack issue verification, 24 hours of decontamination and            three one hour dark observations) and finished with the standard         Button-Up sequence (code and parameter refresh).  Other activities       (with targets as noted) were calibrations for flux (Spica,               rho-Leo, gamma-Grus, HD93521, Sun in Solar OCcultation Channel,          SOCC), flatfield (rho-Leo), airglow scattered light and SOCC             pointing calibrations (Spica, zeta-Pup), SOCC flat (Sun), dark sky       stares, spinning dark observations (in some cases the Sun strobes        through the slit), pointing and short wavelength calibration             (HD93521), InterPlanetary Medium (IPM) histograms and pixellist          observations, dual target tests (HD214680 = 8 Lac, HD214168 = 10         Lac), MEV Solar Wind (HEET) baseine observation, Pluto encounter         rehearsals, and instrument interference tests.                           The changes in Version 2.0 were re-running of the ancillary data         in the data product, updated geometry from newer SPICE kernels,          minor editing of the documentation, catalogs, etc., and resolution       of liens from the December, 2014 review, plus those from the May,        2016 review of the Pluto Encounter data sets.                            New observations added with this version (V2.0) include IPM              histogram scans in December, 2014, which failed.",
-            "title": "NEW HORIZONS                            \n      ALICE PLUTO CRUISE                                                      \n      CALIBRATED V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS                            \n      ALICE PLUTO CRUISE                                                      \n      CALIBRATED V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/EPHBHKBQEJ09",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMEX02 Airborne Synthetic Aperture Radar (AIRSAR) Data, Iowa, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/EPHBHKBQEJ09.",
-            "issued": "2002-07-01",
-            "temporal": "2002-07-01T00:00:00Z/2002-07-09T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2002-07-09",
-            "keyword": [
-                "earth science",
-                "spectral/engineering",
-                "radar"
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
-            "identifier": "C1386204146-NSIDCV0",
             "description": "This data set contains radar backscatter measurments taken over the Soil Moisture Experiments 2002 (SMEX02) Walnut Creek Watershed area in Iowa, USA.",
-            "title": "SMEX02 Airborne Synthetic Aperture Radar (AIRSAR) Data, Iowa, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FEPHBHKBQEJ09",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FEPHBHKBQEJ09",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX02/aircraft_remote_sensing/AIRSAR/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX02/aircraft_remote_sensing/AIRSAR/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX02/aircraft_remote_sensing/AIRSAR/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX02/aircraft_remote_sensing/AIRSAR/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX02/aircraft_remote_sensing/AIRSAR/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX02/aircraft_remote_sensing/AIRSAR/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX02/aircraft_remote_sensing/AIRSAR/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX02/aircraft_remote_sensing/AIRSAR/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/EPHBHKBQEJ09",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/EPHBHKBQEJ09",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/EPHBHKBQEJ09",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/EPHBHKBQEJ09",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386204146-NSIDCV0",
+            "issued": "2002-07-01",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "radar"
+            ],
+            "landingPage": "https://doi.org/10.5067/EPHBHKBQEJ09",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2002-07-09",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-93.913 41.308 -93.017 42.389",
+            "temporal": "2002-07-01T00:00:00Z/2002-07-09T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMEX02 Airborne Synthetic Aperture Radar (AIRSAR) Data, Iowa, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0909-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-07-21T07:28:05.000 to 2015-07-21T09:41:55.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0909-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0909-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0909-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-07-21T07:28:05.000 to 2015-07-21T09:41:55.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0909 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0909 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/3AKYF8OS8DHK",
             "citation": "Kevin W. Bowman. 2023-08-09. TRPSDL2ALLCRSMGKAR. Version 1. TROPESS CrIS-SNPP L2 for Karachi Megacity, Standard Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/3AKYF8OS8DHK. https://disc.gsfc.nasa.gov/datacollection/TRPSDL2ALLCRSMGKAR_1.html. Digital Science Data.",
-            "issued": "2023-08-09",
-            "temporal": "2016-01-02T00:00:00Z/2023-09-04T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-09",
-            "references": [
-                "https://doi.org/10.1126/sciadv.abf7460"
-            ],
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric water vapor",
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
-            "identifier": "C2747542330-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS CrIS-SNPP L2 for Karachi Megacity, Standard Product contains the vertical distribution of seven retrieved atmospheric gases (CH4, CO, H2O, HDO, NH3, O3 and PAN) and temperature, along with formal uncertainties measured by the CrIS instrument on the Suomi-NPP satellite. This standard product is one of the TROPESS Special Collections, centered on a 2x2 degree region over Karachi for the time period from 2016-01-02 to 2021-05-21. The NASA TRopospheric Ozone and Precursors from Earth System Sounding (TROPESS) project, uses an optimal estimation algorithm, known as the MUlti-SpEctra, MUlti-SpEcies, Multi-SEnsors (MUSES).\n\nThe data files are written in the netCDF version 4 file format, and each file contains one day of data. The data have a spatial resolution of 14 km (CrIS nadir FOV), and are reported at 17 vertical levels from the surface to 0.1 hPa. The principal investigator for the TROPESS project is Kevin W. Bowman.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSDL2ALLCRSMGKAR",
-            "creator": "Kevin W. Bowman",
-            "graphic-preview-description": "TROPESS CrIS-SNPP Karachi Megacity (Forward Stream, Standard Product) at 681 hPa on 01 April 2021.",
-            "title": "TROPESS CrIS-SNPP L2 for Karachi Megacity, Standard Product V1 (TRPSDL2ALLCRSMGKAR) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2ALLCRSMGKAR_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F3AKYF8OS8DHK",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F3AKYF8OS8DHK",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2ALLCRSMGKAR_Sample.png",
-                    "description": "TROPESS CrIS-SNPP Karachi Megacity (Forward Stream, Standard Product) at 681 hPa on 01 April 2021.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS CrIS-SNPP Karachi Megacity (Forward Stream, Standard Product) at 681 hPa on 01 April 2021.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2ALLCRSMGKAR_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2ALLCRSMGKAR_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2ALLCRSMGKAR_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2ALLCRSMGKAR.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2ALLCRSMGKAR.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2ALLCRSMGKAR_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2ALLCRSMGKAR_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Standard/TRPSDL2ALLCRSMGKAR.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Standard/TRPSDL2ALLCRSMGKAR.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2ALLCRSMGKAR.1/doc/TROPESS_Forward_Stream_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2ALLCRSMGKAR.1/doc/TROPESS_Forward_Stream_README.pdf",
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
+            "graphic-preview-description": "TROPESS CrIS-SNPP Karachi Megacity (Forward Stream, Standard Product) at 681 hPa on 01 April 2021.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2ALLCRSMGKAR_Sample.png",
+            "identifier": "C2747542330-GES_DISC",
+            "issued": "2023-08-09",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric water vapor",
+                "atmospheric chemistry",
+                "atmospheric temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/3AKYF8OS8DHK",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-08-09",
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
+            "series-name": "TRPSDL2ALLCRSMGKAR",
             "spatial": "66.0 24.0 68.0 26.0",
+            "temporal": "2016-01-02T00:00:00Z/2023-09-04T00:00:00Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS CrIS-SNPP L2 for Karachi Megacity, Standard Product V1 (TRPSDL2ALLCRSMGKAR) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MOD09.NRT.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "LANCEMODIS. 2021-02-07. MODIS/Terra L2 Surface Reflectance, 5-Min Swath 250m, 500m, and 1km NRT. Version 6.1NRT. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, The Land, Atmosphere Near real-time Capability for EOS (LANCE). https://doi.org/10.5067/MODIS/MOD09.NRT.061.",
-            "issued": "2021-02-07",
-            "temporal": "2021-02-07T00:00:00Z/2023-07-24T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-20",
-            "keyword": [
-                "land surface",
-                "earth science",
-                "national geospatial data asset",
-                "ngda",
-                "surface radiative properties"
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
-            "identifier": "C2007657580-LANCEMODIS",
-            "description": "The MODIS/Terra Near Real Time (NRT) L2 Surface Reflectance, 5-Min Swath 250m, 500m, and 1km (MOD09) product is computed from the MODIS Level 1B land bands 1, 2, 3, 4, 5, 6, and 7 (centered at 648 nm, 858 nm, 470 nm, 555 nm, 1240 nm, 1640 nm, and 2130 nm, respectively). This product is an estimate of the surface spectral reflectance for each band as it would have been measured at ground level if there were no atmospheric scattering or absorption. The surface-reflectance product is the input for product generation for several land products: vegetation Indices (VIs), BRDF, thermal anomaly, snow/ice, and Fraction of Photosynthetically Active Radiation/Leaf Area Index (FPAR/LAI).",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "LANCEMODIS",
-            "title": "MODIS/Terra Atmospherically Corrected Surface Reflectance 5-Min L2 Swath 250m, 500m, 1km NRT",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MODIS/Terra Near Real Time (NRT) L2 Surface Reflectance, 5-Min Swath 250m, 500m, and 1km (MOD09) product is computed from the MODIS Level 1B land bands 1, 2, 3, 4, 5, 6, and 7 (centered at 648 nm, 858 nm, 470 nm, 555 nm, 1240 nm, 1640 nm, and 2130 nm, respectively). This product is an estimate of the surface spectral reflectance for each band as it would have been measured at ground level if there were no atmospheric scattering or absorption. The surface-reflectance product is the input for product generation for several land products: vegetation Indices (VIs), BRDF, thermal anomaly, snow/ice, and Fraction of Photosynthetically Active Radiation/Leaf Area Index (FPAR/LAI).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD09.NRT.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD09.NRT.061",
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
-                    "description": "Access Collection 61 data set from the MODAPS LANCE-MODIS page(download server).",
                     "@type": "dcat:Distribution",
+                    "description": "Access Collection 61 data set from the MODAPS LANCE-MODIS page(download server).",
+                    "downloadURL": "http://lance3.modaps.eosdis.nasa.gov/data_products/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through MODAPS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/61/MOD09",
-                    "description": "Direct access to the download site and directory hosting the MOD09 6.1 NRT data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to the download site and directory hosting the MOD09 6.1 NRT data set.",
+                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/61/MOD09",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2007657580-LANCEMODIS",
+            "issued": "2021-02-07",
+            "keyword": [
+                "land surface",
+                "earth science",
+                "national geospatial data asset",
+                "ngda",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MOD09.NRT.061",
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
                 "Terra",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Terra Atmospherically Corrected Surface Reflectance 5-Min L2 Swath 250m, 500m, 1km NRT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/60/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2010-09-10",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "ames",
-                "nasa",
-                "dashlink"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Elizabeth Foughty",
                 "hasEmail": "mailto:elizabeth.a.foughty@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_60",
             "description": "**Abstract**\r\n\r\nPrognostics solutions for mission critical systems require a comprehensive methodology for proactively detecting and isolating failures, recommending and guiding condition-based maintenance actions, and estimating in real time the remaining useful life of critical components and associated subsystems.\r\n\r\nA major challenge has been to extend the benefits of prognostics to include computer servers and other electronic components. The key enabler for prognostics capabilities is monitoring time series signals relating to the health of executing components and subsystems. Time series signals are processed in real time using pattern recognition for proactive anomaly detection and for remaining useful life estimation. Examples will be presented of the use of pattern recognition techniques for early detection of a number of mechanisms that are known to cause failures in electronic systems, including: environmental issues; software aging; degraded or failed sensors; degradation of hardware components; degradation of mechanical, electronic, and optical interconnects. Prognostics pattern classification is helping to substantially increase component reliability margins and system availability goals while reducing costly sources of \"no trouble found\"\r\n\r\nevents that have become a significant warranty-cost issue.\r\n\r\n \r\n\r\n**Bios**\r\n\r\nAleksey Urmanov is a research scientist at Sun Microsystems. He earned his doctoral degree in Nuclear Engineering at the University of Tennessee in 2002. Dr. Urmanov's research activities are centered around his interest in pattern recognition, statistical learning theory and ill-posed problems in engineering. His most recent activities at Sun focus on developing health monitoring and prognostics methods for EP-enabled computer servers. He is a founder and an Editor of the Journal of Pattern Recognition Research.\r\n\r\n \r\n\r\nAnton Bougaev holds a M.S. and a Ph.D. degrees in Nuclear Engineering from Purdue University. Before joining Sun Microsystems Inc. in 2007, he was a lecturer in Nuclear Engineering Department and a member of Applied Intelligent Systems Laboratory (AISL), of Purdue University, West Lafayette, USA. Dr. Bougaev is a founder and the Editor-in-Chief of the Journal of Pattern Recognition Research. His current focus is in reliability physics with emphasis on complex system analysis and the physics of failures which are based on the data driven pattern recognition techniques.",
-            "title": "Health Monitoring and Prognostics for Computer Servers",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Lecture7Urmanov.pdf",
-                    "description": "Lecture7Urmanov.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Lecture7Urmanov.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Lecture7Urmanov.pdf",
+                    "mediaType": "application/pdf",
                     "title": "Lecture7Urmanov.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_60",
+            "issued": "2010-09-10",
+            "keyword": [
+                "ames",
+                "nasa",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/60/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Health Monitoring and Prognostics for Computer Servers"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-M-HRIV-3%2F4-EPOXI-MARS-V1.0",
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
-                "epoxi"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains calibrated narrow band filter images (350-950 nm) images of Mars acquired by the Deep Impact High Resolution Visible CCD (HRIV) for the EPOCh project during the second cruise phase of the EPOXI mission. One set of observations was acquired on 20-21 November 2009 to characterize Mars as an analog for extrasolar planets. The observing period lasted approximately 24 hours. HRIV images were acquired once per hour with the filters centered on 350, 750 and 950 nm, whereas the 450-, 550-, 650-, and 850-nm data were taken every 15 minutes.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-m-hriv-3-4-epoxi-mars-v1.0_5f7w-wggg",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "epoxi"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-M-HRIV-3%2F4-EPOXI-MARS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-m-hriv-3-4-epoxi-mars-v1.0_5f7w-wggg",
-            "description": "This data set contains calibrated narrow band filter images (350-950 nm) images of Mars acquired by the Deep Impact High Resolution Visible CCD (HRIV) for the EPOCh project during the second cruise phase of the EPOXI mission. One set of observations was acquired on 20-21 November 2009 to characterize Mars as an analog for extrasolar planets. The observing period lasted approximately 24 hours. HRIV images were acquired once per hour with the filters centered on 350, 750 and 950 nm, whereas the 450-, 550-, 650-, and 850-nm data were taken every 15 minutes.",
-            "title": "EPOXI MARS OBS - HRIV CALIBRATED IMAGES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "EPOXI MARS OBS - HRIV CALIBRATED IMAGES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H46M34XX",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for International Earth Science Information Network - CIESIN - Columbia University. 2018-12-31. Gridded Population of the World, Version 4 (GPWv4): Basic Demographic Characteristics, Revision 11. Version 4.11. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H46M34XX. https://doi.org/10.7927/H46M34XX.",
-            "issued": "2018-12-31",
-            "temporal": "2010-07-01T00:00:00Z/2010-07-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-12-31",
-            "references": [
-                "https://doi.org/10.1080/23754931.2015.1014272",
-                "https://doi.org/10.7927/H45H7D7F",
-                "https://doi.org/10.7927/H4BC3WMT",
-                "https://doi.org/10.7927/H42Z13KG",
-                "https://doi.org/10.7927/H4Z60M4Z",
-                "https://doi.org/10.7927/H4TD9VDP",
-                "https://doi.org/10.7927/H4JW8BX5",
-                "https://doi.org/10.7927/H49C6VHW",
-                "https://doi.org/10.7927/H45Q4T5F",
-                "https://doi.org/10.7927/H4PN93PB",
-                "https://doi.org/10.7927/H4F47M65"
-            ],
-            "keyword": [
-                "population",
-                "human dimensions",
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
-            "identifier": "C1597149465-SEDAC",
-            "description": "The Gridded Population of the World, Version 4 (GPWv4): Basic Demographic Characteristics, Revision 11 consists of estimates of human population by age and sex as counts (number of persons per pixel) and densities (number of persons per square kilometer), consistent with national censuses and population registers, for the year 2010. To estimate the male and female populations by age in 2010, the proportions of males and females in each 5-year age group from ages 0-4 to ages 85+ for the given census year were calculated. These proportions were then applied to the 2010 estimates of the total population to obtain 2010 estimates of male and female populations by age. In some cases, the spatial resolution of the age and sex proportions was coarser than the resolution of the total population estimates to which they were applied. The population density rasters were created by dividing the population count rasters by the land area raster. The data files were produced as global rasters at 30 arc-second (~1 km at the equator) resolution. To enable faster global processing, and in support of research commUnities, the 30 arc-second data were aggregated to 2.5 arc-minute, 15 arc-minute, 30 arc-minute and 1 degree resolutions.",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Center for International Earth Science Information Network - CIESIN - Columbia University",
-            "title": "Gridded Population of the World, Version 4 (GPWv4): Basic Demographic Characteristics, Revision 11",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/gpw-v4-basic-demographic-characteristics-rev11/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Gridded Population of the World, Version 4 (GPWv4): Basic Demographic Characteristics, Revision 11 consists of estimates of human population by age and sex as counts (number of persons per pixel) and densities (number of persons per square kilometer), consistent with national censuses and population registers, for the year 2010. To estimate the male and female populations by age in 2010, the proportions of males and females in each 5-year age group from ages 0-4 to ages 85+ for the given census year were calculated. These proportions were then applied to the 2010 estimates of the total population to obtain 2010 estimates of male and female populations by age. In some cases, the spatial resolution of the age and sex proportions was coarser than the resolution of the total population estimates to which they were applied. The population density rasters were created by dividing the population count rasters by the land area raster. The data files were produced as global rasters at 30 arc-second (~1 km at the equator) resolution. To enable faster global processing, and in support of research commUnities, the 30 arc-second data were aggregated to 2.5 arc-minute, 15 arc-minute, 30 arc-minute and 1 degree resolutions.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH46M34XX",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH46M34XX",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/gpw-v4/gpw-v4-basic-demographic-characteristics-rev11/gpw-v4-basic-demographic-characteristics-rev11-young-aging-2010-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/gpw-v4/gpw-v4-basic-demographic-characteristics-rev11/gpw-v4-basic-demographic-characteristics-rev11-young-aging-2010-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/gpw-v4-basic-demographic-characteristics-rev11/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/gpw-v4-basic-demographic-characteristics-rev11/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/gpw-v4-basic-demographic-characteristics-rev11/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/gpw-v4-basic-demographic-characteristics-rev11/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/gpw-v4-basic-demographic-characteristics-rev11/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/gpw-v4-basic-demographic-characteristics-rev11/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/gpw-v4-basic-demographic-characteristics-rev11/maps/services",
-                    "description": "Web Map Service Page",
                     "@type": "dcat:Distribution",
+                    "description": "Web Map Service Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/gpw-v4-basic-demographic-characteristics-rev11/maps/services",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/gpw-v4-basic-demographic-characteristics-rev11",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/gpw-v4-basic-demographic-characteristics-rev11",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/gpw-v4-basic-demographic-characteristics-rev11/maps",
+            "identifier": "C1597149465-SEDAC",
+            "issued": "2018-12-31",
+            "keyword": [
+                "population",
+                "human dimensions",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.7927/H46M34XX",
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
+                "https://doi.org/10.7927/H45H7D7F",
+                "https://doi.org/10.7927/H4BC3WMT",
+                "https://doi.org/10.7927/H42Z13KG",
+                "https://doi.org/10.7927/H4Z60M4Z",
+                "https://doi.org/10.7927/H4TD9VDP",
+                "https://doi.org/10.7927/H4JW8BX5",
+                "https://doi.org/10.7927/H49C6VHW",
+                "https://doi.org/10.7927/H45Q4T5F",
+                "https://doi.org/10.7927/H4PN93PB",
+                "https://doi.org/10.7927/H4F47M65"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2010-07-01T00:00:00Z/2010-07-01T00:00:00Z",
             "theme": [
                 "GPW",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Gridded Population of the World, Version 4 (GPWv4): Basic Demographic Characteristics, Revision 11"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3304-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-06-08T12:13:42.000 to 2012-06-08T13:58:01.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3304-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars express"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3304-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3304-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-06-08T12:13:42.000 to 2012-06-08T13:58:01.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3304 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3304 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-PPOL-3-RDR-CROMMELIN-V1.0",
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
-                "international halley watch"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "In preparation for the concerted international study of Comet Halley, the IHW conducted a trial run with observations of Comet Crommelin, largely during February and March of 1984.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-ppol-3-rdr-crommelin-v1.0_5fez-ewuc",
+            "issued": "2021-05-21",
+            "keyword": [
+                "halley",
+                "international halley watch"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-PPOL-3-RDR-CROMMELIN-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-ppol-3-rdr-crommelin-v1.0_5fez-ewuc",
-            "description": "In preparation for the concerted international study of Comet Halley, the IHW conducted a trial run with observations of Comet Crommelin, largely during February and March of 1984.",
-            "title": "IHW COMET PPOL CALIBRATED REDUCED DATA RECORD CROMMELIN V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "IHW COMET PPOL CALIBRATED REDUCED DATA RECORD CROMMELIN V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aquarius/AQ3_SSS.005",
             "bureauCode": [
```

