# Change History for nasa.json (Part 122)

### Changes from 31606f9 to dd2190f (Part 111/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset is intended to include information on observation conditions of IR and VNIR data cubes from the CRISM instrument on MRO, where the data cubes are pointed at the planet limb. For surface-pointed data cubes, Derived data records are the functional counterpart. The information in LDRs is mapped to the sensor space of non-map-projected data, EDRs and TRDRs.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mro-m-crism-6-ldr-v1.0_nw2f-ja74",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars reconnaissance orbiter",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MRO-M-CRISM-6-LDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mro-m-crism-6-ldr-v1.0_nw2f-ja74",
-            "description": "This dataset is intended to include information on observation conditions of IR and VNIR data cubes from the CRISM instrument on MRO, where the data cubes are pointed at the planet limb. For surface-pointed data cubes, Derived data records are the functional counterpart. The information in LDRs is mapped to the sensor space of non-map-projected data, EDRs and TRDRs.",
-            "title": "MRO CRISM LIMB DATA RECORD V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MRO CRISM LIMB DATA RECORD V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/789",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Pinheiro, A.C., and J.L. Privette. 2005. SAFARI 2000 Soil Properties, Moisture, and Temp., Skukuza and Mongu, 1999-2001. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/789",
-            "issued": "2023-10-18",
-            "temporal": "1999-08-19T00:00:00Z/2001-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-25",
-            "keyword": [
-                "land surface",
-                "earth science",
-                "surface thermal properties",
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
-            "identifier": "C2789728240-ORNL_CLOUD",
             "description": "Soil moisture and temperature profile sensors were deployed at flux tower sites in Mongu, Zambia and Skukuza, South Africa. In addition, thermal infrared sensors were deployed to monitor surface temperature at the sites, and soil samples were collected for physical property analysis. A heat-flux plate was also installed at 10 cm depth at the Mongu site. The data cover the period variously from August, 1999 to December, 2001.At the Mongu site, three profiles of soil moisture and temperature were obtained to a maximum depth of 125 cm. These profiles were located approximately 30 meters north of the Mongu flux tower, within the Kataba Local Forest. Surface radiometric temperature was measured by thermal infrared sensors deployed on top of the 30-meter tower and on a tree.  At the Skukuza site, two profiles of soil moisture and temperature were obtained to a maximum depth of 40 cm in a Combretum stand. The radiometric temperature of the tree crown and the background surface were monitored by infrared thermocouple sensors deployed on a pole at 2.5 m and 5 m heights. Soil samples were collected at different depths in the vicinity of the soil profiles at each site and were analyzed at CSIR in Pretoria to determine bulk density, texture, and particle size distribution. The data files are stored as ASCII text files, in comma-separated-value (.csv) format. Associated with each data file is a metadata (.txt ) file. Among other information, the metadata files indicate periods of missing data.",
-            "graphic-preview-description": "Browse Image",
-            "title": "SAFARI 2000 Soil Properties, Moisture, and Temp., Skukuza and Mongu, 1999-2001",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/safari_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F789",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F789",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/field_campaign/mongu_skukuza_soil_prop/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/field_campaign/mongu_skukuza_soil_prop/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/S2K/guides/mongu_skukuza_soil_prop.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/S2K/guides/mongu_skukuza_soil_prop.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/789",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/789",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/field_campaign/mongu_skukuza_soil_prop/comp/mongu_skukuza_soil_prop_readme.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/field_campaign/mongu_skukuza_soil_prop/comp/mongu_skukuza_soil_prop_readme.pdf",
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
+            "identifier": "C2789728240-ORNL_CLOUD",
+            "issued": "2023-10-18",
+            "keyword": [
+                "land surface",
+                "earth science",
+                "surface thermal properties",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/789",
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
             "spatial": "23.25 -25.02 31.47 -15.44",
+            "temporal": "1999-08-19T00:00:00Z/2001-12-31T23:59:59Z",
             "theme": [
                 "SAFARI 2000",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAFARI 2000 Soil Properties, Moisture, and Temp., Skukuza and Mongu, 1999-2001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/885",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Diner, D.J. 2007. SAFARI 2000 MISR Level 2 Data, Southern Africa, Dry Season 2000. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/885",
-            "issued": "2023-10-18",
-            "temporal": "2000-08-12T00:00:00Z/2000-09-28T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-24",
-            "keyword": [
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
-            "identifier": "C2788357139-ORNL_CLOUD",
             "description": "MISR (Multi-angle Imaging SpectroRadiometer) views the sunlit Earth simultaneously at nine widely spaced and collects global images with high spatial detail in four colors at every angle. These images are carefully calibrated to provide accurate measures of the brightness, contrast, and color of reflected sunlight. The change in reflection at different view angles affords the means to distinguish different types of atmospheric particles (aerosols), cloud forms, and land surface covers. Combined with stereoscopic techniques, this enables construction of 3-dimensional models and more accurate estimates of the total amount of sunlight reflected by Earth's diverse environments.MISR was built for NASA by the Jet Propulsion Laboratory. It is part of NASA's Terra spacecraft, launched into a polar orbit around the Earth on December 18, 1999.The Southern African Fire Atmosphere Research Initiative (SAFARI) 2000 field campaign focused on the smoke and gases released into the environment of southern Africa by industrial, biological, and man-made sources such as biomass burning. The area of study and MISR path numbers include Botswana, Lesotho, Malawi, Mozambique, Namibia, South Africa, Swaziland, Zambia, and Zimbabwe. These MISR data cover the period August 12 through September 28, 2000.",
-            "graphic-preview-description": "Browse Image",
-            "title": "SAFARI 2000 MISR Level 2 Data, Southern Africa, Dry Season 2000",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/safari_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F885",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F885",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/remote_sensing/MISR/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/remote_sensing/MISR/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/S2K/guides/S2K_MISR_guide.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/S2K/guides/S2K_MISR_guide.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/885",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/885",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MISR/comp/DPS_RevE.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MISR/comp/DPS_RevE.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MISR/comp/DPS_v214.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MISR/comp/DPS_v214.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MISR/comp/DPS_v32_RevL.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MISR/comp/DPS_v32_RevL.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MISR/comp/DPS_v40_RevN.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MISR/comp/DPS_v40_RevN.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MISR/comp/MISR_Quality_Summaries_Reformatted_Products.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MISR/comp/MISR_Quality_Summaries_Reformatted_Products.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MISR/comp/S2K_MISR_guide.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MISR/comp/S2K_MISR_guide.pdf",
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
+            "identifier": "C2788357139-ORNL_CLOUD",
+            "issued": "2023-10-18",
+            "keyword": [
+                "surface radiative properties",
+                "land surface",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/885",
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
             "spatial": "9.08 -35.0 31.49 -15.0",
+            "temporal": "2000-08-12T00:00:00Z/2000-09-28T23:59:59Z",
             "theme": [
                 "SAFARI 2000",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAFARI 2000 MISR Level 2 Data, Southern Africa, Dry Season 2000"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2340494419-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC.",
-            "issued": "2022-09-14",
-            "temporal": "2012-01-02T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-14",
-            "keyword": [
-                "ocean chemistry",
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
-            "identifier": "C2340494419-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "Suomi-NPP VIIRS Global Mapped Particulate Organic Carbon (POC) - Near Real Time (NRT) Data, version R2022.0",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/SNPP/VIIRS/L3M/POC/2022",
-                    "description": "VIIRS-Suomi-NPP L3M Particulate Organic Carbon (POC) - Near Real Time (NRT) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS-Suomi-NPP L3M Particulate Organic Carbon (POC) - Near Real Time (NRT) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/SNPP/VIIRS/L3M/POC/2022",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/VIIRS/L3SMI/",
-                    "description": "OB.DAAC OPeNDAP Site for Suomi-NPP VIIRS Standard Mapped Image (SMI) Product",
                     "@type": "dcat:Distribution",
+                    "description": "OB.DAAC OPeNDAP Site for Suomi-NPP VIIRS Standard Mapped Image (SMI) Product",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/VIIRS/L3SMI/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2340494419-OB_DAAC",
+            "issued": "2022-09-14",
+            "keyword": [
+                "ocean chemistry",
+                "oceans",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2340494419-OB_DAAC.html",
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
+            "title": "Suomi-NPP VIIRS Global Mapped Particulate Organic Carbon (POC) - Near Real Time (NRT) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.nasa.gov/news/budget/index.html",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brian Dunbar",
+                "hasEmail": "mailto:brian.dunbar@nasa.gov"
+            },
+            "description": "NASA Financial Budget Documents, Strategic Plans and Performance Reports for fiscal year 2016.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "FY16 Agency Fact Sheet PDF",
+                    "downloadURL": "http://www.nasa.gov/sites/default/files/files/Agency_Fact_Sheet_FY_2016.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "NASA Agency Fact Sheet 2016"
+                }
+            ],
+            "identifier": "OCIO-Fitara-56",
             "issued": "2014-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "financial",
                 "budget",
@@ -1163539,206 +1163553,170 @@
                 "plan",
                 "strategic"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brian Dunbar",
-                "hasEmail": "mailto:brian.dunbar@nasa.gov"
-            },
+            "landingPage": "http://www.nasa.gov/news/budget/index.html",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:046"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "NASA HQ"
             },
-            "identifier": "OCIO-Fitara-56",
-            "description": "NASA Financial Budget Documents, Strategic Plans and Performance Reports for fiscal year 2016.",
-            "title": "NASA Financial Budget Documents, Strategic Plans and Performance Reports 2016: NASA Budget Fact Sheet",
-            "programCode": [
-                "026:046"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.nasa.gov/sites/default/files/files/Agency_Fact_Sheet_FY_2016.pdf",
-                    "description": "FY16 Agency Fact Sheet PDF",
-                    "@type": "dcat:Distribution",
-                    "title": "NASA Agency Fact Sheet 2016"
-                }
-            ],
-            "accrualPeriodicity": "R/P1Y",
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "NASA Financial Budget Documents, Strategic Plans and Performance Reports 2016: NASA Budget Fact Sheet"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TIGR14-V1.0",
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
+            "description": "The Cassini Radio Science Titan Gravity Science Experiment (TIGR14) Raw Data Archive is a time-ordered collection of radio science raw data acquired on April 3, 5, June 21 and 23, 2009, during he Cassini Extended Mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tigr14-v1.0_nwek-x22i",
+            "issued": "2021-05-21",
+            "keyword": [
+                "cassini-huygens",
+                "titan"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TIGR14-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tigr14-v1.0_nwek-x22i",
-            "description": "The Cassini Radio Science Titan Gravity Science Experiment (TIGR14) Raw Data Archive is a time-ordered collection of radio science raw data acquired on April 3, 5, June 21 and 23, 2009, during he Cassini Extended Mission.",
-            "title": "CASSINI RSS RAW DATA SET - TIGR14 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI RSS RAW DATA SET - TIGR14 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2057",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Jones, C., T. Oliver-Cabrera, M. Simard, and Y. Lou. 2022. Delta-X: UAVSAR L2 Interferometric Products, MRD, Louisiana, 2021. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2057",
-            "issued": "2024-07-23",
-            "temporal": "2021-03-27T13:28:00Z/2021-09-13T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-24",
-            "keyword": [
-                "ecosystems",
-                "geomorphic landforms/processes",
-                "land surface",
-                "surface water",
-                "terrestrial hydrosphere",
-                "topography",
-                "oceans",
-                "coastal processes",
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
-            "identifier": "C2428388674-ORNL_CLOUD",
             "description": "This dataset contains georeferenced UAVSAR Level 2 (L2) interferometric products for Delta-X flight lines acquired during the spring (2021-03-27 to 2021-04-18) and fall (2021-09-03 to 2021-09-13) deployments. This dataset provides water-level change observations throughout wetlands of the Atchafalaya and Terrebonne Basins, in Southern Louisiana, USA, within the Mississippi River Delta (MRD), and it may be used to generate time series analysis. The data were collected by Uninhabited Aerial Vehicle Synthetic Aperture Radar (UAVSAR), a polarimetric L-band synthetic aperture radar flown on the NASA Gulfstream-III (C20) aircraft as part of the Delta-X campaign. Water surface elevations were measured on multiple flights at 30-minute intervals. Data quality was assessed by comparing water elevation estimates with data from in situ water level gauges throughout the study area. The data include interferogram phase, interferogram amplitude, unwrapped interferogram phase, and coherence products. A series of quality assurance masks of troposphere-induced phase delay regions were generated for all SAR acquisition dates using a weather feature matching algorithm. Geometry files for each flight line per field campaign with latitude, longitude, height and incidence angle information are also included. The data are provided in ENVI format.",
-            "graphic-preview-description": "UAVSAR interferometric product example. From left to right: Interferometric amplitude (displayed in decibel scale), wrapped interferometric phase, interferometric coherence and unwrapped interferometric phase, generated using acquisitions from flight-line wterre_34202 on 2021-04-06 at 20:32 and 21:02 (UTC) times.",
-            "title": "Delta-X: UAVSAR L2 Interferometric Products, MRD, Louisiana, 2021",
-            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L2_UAVSAR_WaterLevels_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2057",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2057",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/deltax/DeltaX_L2_UAVSAR_WaterLevels/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/deltax/DeltaX_L2_UAVSAR_WaterLevels/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L2_UAVSAR_WaterLevels.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L2_UAVSAR_WaterLevels.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2057",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2057",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/DeltaX_L2_UAVSAR_WaterLevels/comp/DeltaX_L2_UAVSAR_WaterLevels.pdf",
-                    "description": "Delta-X: UAVSAR L2 Interferometric Products, MRD, Louisiana, 2021: DeltaX_L2_UAVSAR_WaterLevels.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Delta-X: UAVSAR L2 Interferometric Products, MRD, Louisiana, 2021: DeltaX_L2_UAVSAR_WaterLevels.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/DeltaX_L2_UAVSAR_WaterLevels/comp/DeltaX_L2_UAVSAR_WaterLevels.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L2_UAVSAR_WaterLevels_Fig1.jpg",
-                    "description": "UAVSAR interferometric product example. From left to right: Interferometric amplitude (displayed in decibel scale), wrapped interferometric phase, interferometric coherence and unwrapped interferometric phase, generated using acquisitions from flight-line wterre_34202 on 2021-04-06 at 20:32 and 21:02 (UTC) times.",
                     "@type": "dcat:Distribution",
+                    "description": "UAVSAR interferometric product example. From left to right: Interferometric amplitude (displayed in decibel scale), wrapped interferometric phase, interferometric coherence and unwrapped interferometric phase, generated using acquisitions from flight-line wterre_34202 on 2021-04-06 at 20:32 and 21:02 (UTC) times.",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L2_UAVSAR_WaterLevels_Fig1.jpg",
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
+            "graphic-preview-description": "UAVSAR interferometric product example. From left to right: Interferometric amplitude (displayed in decibel scale), wrapped interferometric phase, interferometric coherence and unwrapped interferometric phase, generated using acquisitions from flight-line wterre_34202 on 2021-04-06 at 20:32 and 21:02 (UTC) times.",
+            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L2_UAVSAR_WaterLevels_Fig1.jpg",
+            "identifier": "C2428388674-ORNL_CLOUD",
+            "issued": "2024-07-23",
+            "keyword": [
+                "ecosystems",
+                "geomorphic landforms/processes",
+                "land surface",
+                "surface water",
+                "terrestrial hydrosphere",
+                "topography",
+                "oceans",
+                "coastal processes",
+                "biosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2057",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-07-24",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-91.59 29.01 -90.13 29.78",
+            "temporal": "2021-03-27T13:28:00Z/2021-09-13T23:59:59Z",
             "theme": [
                 "Delta-X",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Delta-X: UAVSAR L2 Interferometric Products, MRD, Louisiana, 2021"
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
-                "safety",
-                "aviation",
-                "collision",
-                "midair",
-                "incident"
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
-            "identifier": "NASA-817",
             "description": "Reports concerning near midair collision events.",
-            "title": "Aviation Safety Reporting System: Near Midair Collision Incidents",
-            "programCode": [
-                "026:021"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1163746,113 +1163724,109 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-817",
+            "issued": "2018-06-25",
+            "keyword": [
+                "safety",
+                "aviation",
+                "collision",
+                "midair",
+                "incident"
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
+            "title": "Aviation Safety Reporting System: Near Midair Collision Incidents"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GPM/IMERG/3B-HH-L/07",
             "citation": "Huffman, G.J., E.F. Stocker, D.T. Bolvin, E.J. Nelkin, Jackson Tan. 2024-06-07. GPM_3IMERGHHL. Version 07. GPM IMERG Late Precipitation L3 Half Hourly 0.1 degree x 0.1 degree V07. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/IMERG/3B-HH-L/07. https://disc.gsfc.nasa.gov/datacollection/GPM_3IMERGHHL_07.html. Digital Science Data.",
-            "issued": "2024-06-01",
-            "temporal": "2000-06-01T00:00:00Z/2024-06-10T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-01",
-            "references": [
-                "https://doi.org/10.1175/JHM-D-11-022.1"
-            ],
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
+            "creator": "Huffman, G.J., E.F. Stocker, D.T. Bolvin, E.J. Nelkin, Jackson Tan",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2723754845-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Version 07 is the current version of the data set. Older versions will no longer be available and have been superseded by Version 07.\n\nThe Integrated Multi-satellitE Retrievals for GPM (IMERG) IMERG is a NASA product estimating global surface precipitation rates at a high resolution of 0.1\u00b0 every half-hour beginning 2000.  It is part of the joint NASA-JAXA Global Precipitation Measurement (GPM) mission, using the GPM Core Observatory satellite as the standard to combine precipitation observations from an international constellation of satellites using advanced techniques.  IMERG can be used for global-scale applications as well as over regions with sparse or no reliable surface observations.  The fine spatial and temporal resolution of IMERG data allows them to be accumulated to the scale of the application for increased skill.  IMERG has three Runs with varying latencies in response to a range of application needs: rapid-response applications (Early Run, 4-h latency), same/next-day applications (Late Run, 14-h latency), and post-real-time research (Final Run, 3.5-month latency).  While IMERG strives for consistency and accuracy, satellite estimates of precipitation are expected to have lower skill over frozen surfaces, complex terrain, and coastal zones.  As well, the changing GPM satellite constellation over time may introduce artifacts that affect studies focusing on multi-year changes.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "GPM_3IMERGHHL",
-            "creator": "Huffman, G.J., E.F. Stocker, D.T. Bolvin, E.J. Nelkin, Jackson Tan",
-            "graphic-preview-description": "Online visualization and analysis",
-            "title": "GPM IMERG Late Precipitation L3 Half Hourly 0.1 degree x 0.1 degree V07 (GPM_3IMERGHHL) at GES DISC",
-            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/#dataKeyword=IMERGHHL",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FIMERG%2F3B-HH-L%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FIMERG%2F3B-HH-L%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3IMERGHHL_07.png",
-                    "description": "Surface Precipitation  (Late) from GPM IMERG (0.1 degree x 0.1 degree)  (GPM_3IMERGHHL)",
                     "@type": "dcat:Distribution",
+                    "description": "Surface Precipitation  (Late) from GPM IMERG (0.1 degree x 0.1 degree)  (GPM_3IMERGHHL)",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3IMERGHHL_07.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3IMERGHHL_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3IMERGHHL_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHL.07/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHL.07/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://giovanni.gsfc.nasa.gov/#dataKeyword=IMERGHHL",
-                    "description": "Online visualization and analysis",
                     "@type": "dcat:Distribution",
+                    "description": "Online visualization and analysis",
+                    "downloadURL": "https://giovanni.gsfc.nasa.gov/#dataKeyword=IMERGHHL",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through GIOVANNI"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/hyrax/GPM_L3/GPM_3IMERGHHL.07/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/hyrax/GPM_L3/GPM_3IMERGHHL.07/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/dods/GPM_3IMERGHHL_07.info",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/dods/GPM_3IMERGHHL_07.info",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/thredds/catalog/aggregation/GPM_3IMERGHHL.07/catalog.html",
-                    "description": "Access the data via the THREDDS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the THREDDS.",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/thredds/catalog/aggregation/GPM_3IMERGHHL.07/catalog.html",
+                    "mediaType": "text/html",
                     "title": "Use THREDDS DATA to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3IMERGHHL_07",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3IMERGHHL_07",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
@@ -1163862,75 +1163836,114 @@
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/MorphingInV06IMERG.pdf",
-                    "description": "Release notes; New Morphing algorithm",
                     "@type": "dcat:Distribution",
+                    "description": "Release notes; New Morphing algorithm",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/MorphingInV06IMERG.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm.nasa.gov/resources/documents/imerg-v07-release-notes",
-                    "description": "IMERG Release Notes",
                     "@type": "dcat:Distribution",
+                    "description": "IMERG Release Notes",
+                    "downloadURL": "https://gpm.nasa.gov/resources/documents/imerg-v07-release-notes",
+                    "mediaType": "text/html",
                     "title": "View an important notice for this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/IMERG_doc.06.pdf",
-                    "description": "IMERG Technical Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "IMERG Technical Documentation",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/IMERG_doc.06.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/IMERGV06_QI.pdf",
-                    "description": "IMERG Quality Index",
                     "@type": "dcat:Distribution",
+                    "description": "IMERG Quality Index",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/IMERGV06_QI.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
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
-                    "downloadURL": "https://gpm.nasa.gov",
-                    "description": "GPM Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "GPM Project Home Page",
+                    "downloadURL": "https://gpm.nasa.gov",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "graphic-preview-description": "Online visualization and analysis",
+            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/#dataKeyword=IMERGHHL",
+            "identifier": "C2723754845-GES_DISC",
+            "issued": "2024-06-01",
+            "keyword": [
+                "atmosphere",
+                "precipitation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/IMERG/3B-HH-L/07",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-06-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1175/JHM-D-11-022.1"
+            ],
+            "release-place": "Greenbelt, MD",
+            "series-name": "GPM_3IMERGHHL",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-06-01T00:00:00Z/2024-06-10T00:00:00Z",
             "theme": [
                 "GPM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM IMERG Late Precipitation L3 Half Hourly 0.1 degree x 0.1 degree V07 (GPM_3IMERGHHL) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567190-USGS_LTA.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "U.S. Geological Survey. 2010-01-01. USGS Global Forest Observations Initiative (GFOI) Brazil. Archived by National Aeronautics and Space Administration, U.S. Government, U.S. Geological Survey. http://lsiexplorer.cr.usgs.gov.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EUGENE FOSNIGHT",
+                "hasEmail": "mailto:fosnight@usgs.gov"
+            },
+            "creator": "U.S. Geological Survey",
+            "description": "The Global Forest Observations Initiative (GFOI) is an initiative of the inter-governmental Group on Earth Observations (GEO) that aims to:\n\nfoster the sustained availability of observations for national forest monitoring systems; support governments that are establishing national systems by providing a platform for coordinating observations, providing assistance and guidance on utilizing observations, developing accepted methods and protocols, and promoting ongoing research and development; and work with national governments that report into international forest assessments (such as the global Forest Resources Assessment (FRA) of the Food and Agriculture Organization, FAO) and the national greenhouse gas inventories reported to the UN Framework Convention on Climate Change (UNFCCC) using methods of the Intergovernmental Panel on Climate Change (IPCC).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "\n         Group on Earth Observations (GEO) Global Forest Observations Initiative (GFOI)\n      ",
+                    "downloadURL": "http://www.gfoi.org/",
+                    "mediaType": "text/html",
+                    "title": "The dataset's project home page"
+                }
+            ],
+            "identifier": "C1220567190-USGS_LTA",
             "issued": "1972-07-28",
-            "temporal": "1972-07-28T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-03-25",
             "keyword": [
                 "terrestrial ecosystems",
                 "earth science",
@@ -1163941,119 +1163954,84 @@
                 "biosphere",
                 "agriculture"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EUGENE FOSNIGHT",
-                "hasEmail": "mailto:fosnight@usgs.gov"
-            },
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567190-USGS_LTA.html",
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
-            "identifier": "C1220567190-USGS_LTA",
-            "description": "The Global Forest Observations Initiative (GFOI) is an initiative of the inter-governmental Group on Earth Observations (GEO) that aims to:\n\nfoster the sustained availability of observations for national forest monitoring systems; support governments that are establishing national systems by providing a platform for coordinating observations, providing assistance and guidance on utilizing observations, developing accepted methods and protocols, and promoting ongoing research and development; and work with national governments that report into international forest assessments (such as the global Forest Resources Assessment (FRA) of the Food and Agriculture Organization, FAO) and the national greenhouse gas inventories reported to the UN Framework Convention on Climate Change (UNFCCC) using methods of the Intergovernmental Panel on Climate Change (IPCC).",
-            "creator": "U.S. Geological Survey",
-            "title": "USGS Global Forest Observations Initiative (GFOI) Brazil",
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
             "spatial": "-75.25 -35.5 -33.9 6.7",
+            "temporal": "1972-07-28T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "CWIC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "USGS Global Forest Observations Initiative (GFOI) Brazil"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3381-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-08-30T03:37:38.000 to 2012-08-30T06:15:09.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3381-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars express",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3381-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3381-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-08-30T03:37:38.000 to 2012-08-30T06:15:09.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3381 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3381 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA/3111",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Pumphrey, H., Livesey, N., Read, W., and Fuller, R.. 2020-04-20. ML3DBHCN. Version 004. MLS/Aura Level 3 Daily Binned Hydrogen Cyanide (HCN) Mixing Ratio on Assorted Grids V004. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA/3111. https://disc.gsfc.nasa.gov/datacollection/ML3DBHCN_004.html. Digital Science Data.",
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
-            "identifier": "C1725331558-GES_DISC",
-            "description": "ML3DBHCN is the EOS Aura Microwave Limb Sounder (MLS) daily binned on various vertical grids product for hydrogen cyanide (HCN) derived from radiances measured primarily by the 190 GHz radiometer. The data version is 4.2. Spatial coverage is near-global (-82 to +82 degrees latitude) at a spatial resolution of 4 degrees latitude by 5 degrees longitude. The recommended useful vertical range is from 21.5 to 0.1 hPa, and the vertical resolution is between 8 and 12 km. Users of the ML3DBHCN data product should read chapter 4 and section 3.11 of the EOS MLS Level 2 Version 4 Quality Document for more information.\n\nThe data files are archived in the netCDF4 format, which is also compatible with HDF5 readers and tools. Each file contains six group objects: lat-lon map vs pressure, lat vs pressure zonal mean, lat-lon map vs \"potential temperature\", lat vs \"potential temperature\" zonal mean, \"equivalent latitude\" vs \"potential temperature\" zonal mean, and vortex average vs \"potential temperature\". Each group has a set of data (average, min, max, std dev, rms) and geolocation fields, grid attributes, and metadata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML3DBHCN",
             "creator": "Pumphrey, H., Livesey, N., Read, W., and Fuller, R.",
-            "title": "MLS/Aura Level 3 Daily Binned Hydrogen Cyanide (HCN) Mixing Ratio on Assorted Grids V004 (ML3DBHCN) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML3DBHCN_004.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "ML3DBHCN is the EOS Aura Microwave Limb Sounder (MLS) daily binned on various vertical grids product for hydrogen cyanide (HCN) derived from radiances measured primarily by the 190 GHz radiometer. The data version is 4.2. Spatial coverage is near-global (-82 to +82 degrees latitude) at a spatial resolution of 4 degrees latitude by 5 degrees longitude. The recommended useful vertical range is from 21.5 to 0.1 hPa, and the vertical resolution is between 8 and 12 km. Users of the ML3DBHCN data product should read chapter 4 and section 3.11 of the EOS MLS Level 2 Version 4 Quality Document for more information.\n\nThe data files are archived in the netCDF4 format, which is also compatible with HDF5 readers and tools. Each file contains six group objects: lat-lon map vs pressure, lat vs pressure zonal mean, lat-lon map vs \"potential temperature\", lat vs \"potential temperature\" zonal mean, \"equivalent latitude\" vs \"potential temperature\" zonal mean, and vortex average vs \"potential temperature\". Each group has a set of data (average, min, max, std dev, rms) and geolocation fields, grid attributes, and metadata.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA%2F3111",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA%2F3111",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1164063,370 +1164041,394 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML3DBHCN_004.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML3DBHCN_004.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level3/ML3DBHCN.004/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level3/ML3DBHCN.004/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level3/ML3DBHCN.004/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level3/ML3DBHCN.004/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML3DBHCN_004",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML3DBHCN_004",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML3DBHCN_004.png",
+            "identifier": "C1725331558-GES_DISC",
+            "issued": "2020-03-06",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA/3111",
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
+            "series-name": "ML3DBHCN",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MLS/Aura Level 3 Daily Binned Hydrogen Cyanide (HCN) Mixing Ratio on Assorted Grids V004 (ML3DBHCN) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-J-KECK-3-EDR-SL9-V1.0",
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
-                "pds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "TBD",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-j-keck-3-edr-sl9-v1.0_nwyp-p3y2",
+            "issued": "2018-06-26",
+            "keyword": [
+                "pds"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-J-KECK-3-EDR-SL9-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-j-keck-3-edr-sl9-v1.0_nwyp-p3y2",
-            "description": "TBD",
-            "title": "KECK OBSERVATORY IMAGE DATA FROM SL9 IMPACTS WITH JUPITER",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "KECK OBSERVATORY IMAGE DATA FROM SL9 IMPACTS WITH JUPITER"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-MOLA-5-MEGDR-L3-V1.0",
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
+            "description": "The Mars Global Surveyor spacecraft includes a laser altimeter instrument. The primary objective of the Mars Orbiter Laser Altimeter (MOLA) is to determine globally the topography of Mars at a level suitable for addressing problems in geology and geophysics. The MOLA Experiment Gridded Data Record (EGDR) is a topographic map of Mars based on altimetry data acquired by the MOLA instrument and accumulated over the course of the mission. The Mission Experiment Gridded Data Record (MEGDR), consists of data accumulated over the whole primary mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-mola-5-megdr-l3-v1.0_nx3s-sqbg",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars global surveyor"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-MOLA-5-MEGDR-L3-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-mola-5-megdr-l3-v1.0_nx3s-sqbg",
-            "description": "The Mars Global Surveyor spacecraft includes a laser altimeter instrument. The primary objective of the Mars Orbiter Laser Altimeter (MOLA) is to determine globally the topography of Mars at a level suitable for addressing problems in geology and geophysics. The MOLA Experiment Gridded Data Record (EGDR) is a topographic map of Mars based on altimetry data acquired by the MOLA instrument and accumulated over the course of the mission. The Mission Experiment Gridded Data Record (MEGDR), consists of data accumulated over the whole primary mission.",
-            "title": "MOLA MISSION EXPERIMENT GRIDDED DATA RECORD",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MOLA MISSION EXPERIMENT GRIDDED DATA RECORD"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220566821-USGS_LTA.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, DOI/USGS/EROS.",
-            "issued": "1972-12-06",
-            "temporal": "1972-12-06T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-12-27",
-            "keyword": [
-                "earth science",
-                "surface thermal properties",
-                "surface radiative properties",
-                "spectral/engineering",
-                "sensor characteristics",
-                "ngda",
-                "national geospatial data asset",
-                "land use/land cover",
-                "land surface"
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
-            "identifier": "C1220566821-USGS_LTA",
             "description": "On the background of these requirements for sensor calibration, intercalibration and product validation, the subgroup on Calibration and Validation of the Committee on Earth Observing System (CEOS) formulated the following recommendation during the plenary session held in China at the end of 2004, with the goal of setting-up and operating an internet based system to provide sensor data, protocols and guidelines for these purposes:\r\n\r\nBackground:\r\n\r\nReference Datasets are required to support the understanding of climate change and quality assure operational services by Earth Observing satellites. The data from different sensors and the resulting synergistic data products require a high level of accuracy that can only be obtained through continuous traceable calibration and validation activities.\r\nRequirement:\r\n\r\nInitiate an activity to document a reference methodology to predict Top of Atmosphere (TOA) radiance for which currently flying and planned wide swath sensors can be intercompared, i.e. define a standard for traceability. Also create and maintain a fully accessible web page containing, on an instrument basis, links to all instrument characteristics needed for intercomparisons as specified above, ideally in a common format. In addition, create and maintain a database (e.g. SADE) of instrument data for specific vicarious calibration sites, including site characteristics, in a common format. Each agency is responsible for providing data for their instruments in this common format. Recommendation : The required activities described above should be supported for an implementation period of two years and a maintenance period over two subsequent years. The CEOS should encourage a member agency to accept the lead role in supporting this activity. CEOS should request all member agencies to support this activity by providing appropriate information and data in a timely manner.\r\n\r\nInstrumented Sites:\r\nDome C, Antarctica is one of eight instrumented sites that are CEOS Reference Test Sites. The CEOS instrumented sites are provisionally being called LANDNET. These instrumented sites are primarily used for field campaigns to obtain radiometric gain, and these sites can serve as a focus for international efforts, facilitating traceability and inter-comparison to evaluate biases of in-flight and future instruments in a harmonized manner.\u00a0 In the longer-term it is anticipated that these sites will all be fully automated and provide surface and atmospheric measurements to the WWW in an autonomous manner reducing some of the cost of a manned campaign, at present three can operate in this manner.",
-            "title": "CEOS Cal Val Test Site - Dome C, Antarctica - Instrumented Site",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/opensearch/granules/descriptor_document.xml?collectionConceptId=C1220566821-USGS_LTA",
-                    "description": "Collection-specific granule Open Search Descriptor Document",
                     "@type": "dcat:Distribution",
+                    "description": "Collection-specific granule Open Search Descriptor Document",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/opensearch/granules/descriptor_document.xml?collectionConceptId=C1220566821-USGS_LTA",
+                    "mediaType": "application/opensearchdescription+xml",
                     "title": "Retrieve the OpenSearch Get Capabilities document"
                 }
             ],
+            "identifier": "C1220566821-USGS_LTA",
+            "issued": "1972-12-06",
+            "keyword": [
+                "earth science",
+                "surface thermal properties",
+                "surface radiative properties",
+                "spectral/engineering",
+                "sensor characteristics",
+                "ngda",
+                "national geospatial data asset",
+                "land use/land cover",
+                "land surface"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220566821-USGS_LTA.html",
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
             "spatial": "123.0 -76.6 131.18 -74.5",
+            "temporal": "1972-12-06T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "CWIC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CEOS Cal Val Test Site - Dome C, Antarctica - Instrumented Site"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-PANCAM-5-NORMAL-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-pancam-5-normal-ops-v1.0_nx57-udcu",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-PANCAM-5-NORMAL-OPS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-pancam-5-normal-ops-v1.0_nx57-udcu",
-            "description": "not applicable",
-            "title": "MER 1 MARS PANORAMIC CAMERA SURFACE NORMAL RDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MER 1 MARS PANORAMIC CAMERA SURFACE NORMAL RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGN-V-RSS-5-LOSAPDR-L2-V1.0",
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
-                "magellan",
-                "venus"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Line of Sight Acceleration Profile Data Records (LOSAPDR) consist of data from Doppler tracking of the orbiting spacecraft. The relative motion of the spacecraft and the earth-based radio receiver is measured very precisely, and known motions are removed a priori (i.e. earth rotation, planetary motions, spacecraft orbital motion, solar pressure, drag), leaving small velocity changes caused by variations in the mass distribution of the planet. The residual Doppler frequency shifts are linearly proportional to the component of velocity in the Earth direction. Numerical differentiation of these velocity residuals with respect to time produces line-of-sight (LOS) gravity. These measures are accelerations at spacecraft altitude which can be modeled for geophysical interpretation.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgn-v-rss-5-losapdr-l2-v1.0_nx78-ijg3",
+            "issued": "2018-06-26",
+            "keyword": [
+                "magellan",
+                "venus"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGN-V-RSS-5-LOSAPDR-L2-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgn-v-rss-5-losapdr-l2-v1.0_nx78-ijg3",
-            "description": "Line of Sight Acceleration Profile Data Records (LOSAPDR) consist of data from Doppler tracking of the orbiting spacecraft. The relative motion of the spacecraft and the earth-based radio receiver is measured very precisely, and known motions are removed a priori (i.e. earth rotation, planetary motions, spacecraft orbital motion, solar pressure, drag), leaving small velocity changes caused by variations in the mass distribution of the planet. The residual Doppler frequency shifts are linearly proportional to the component of velocity in the Earth direction. Numerical differentiation of these velocity residuals with respect to time produces line-of-sight (LOS) gravity. These measures are accelerations at spacecraft altitude which can be modeled for geophysical interpretation.",
-            "title": "MGN V RSS LINE OF SIGHT ACCELERATION PROFILES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MGN V RSS LINE OF SIGHT ACCELERATION PROFILES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-2CP-3-RDR-ECAS-V2.0",
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
+            "description": "The eight color asteroid survey provides reflectance spectra for minor planets using eight filter passbands. This dataset includes the primary data obtained for 589 minor planets, the mean values for each minor planet included in the survey, the principal component scores derived from the primary data, the response curves, effective wavelengths, and bandpasses for the filters, and the coordinates and values determined for standard stars defining the system.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-2cp-3-rdr-ecas-v2.0_nx7r-hh3n",
+            "issued": "2021-05-21",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-2CP-3-RDR-ECAS-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-2cp-3-rdr-ecas-v2.0_nx7r-hh3n",
-            "description": "The eight color asteroid survey provides reflectance spectra for minor planets using eight filter passbands. This dataset includes the primary data obtained for 589 minor planets, the mean values for each minor planet included in the survey, the principal component scores derived from the primary data, the response curves, effective wavelengths, and bandpasses for the filters, and the coordinates and values determined for standard stars defining the system.",
-            "title": "EIGHT COLOR ASTEROID SURVEY V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "EIGHT COLOR ASTEROID SURVEY V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-NIS-2-EDR-CRUISE4-V1.0",
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
-                "solar system",
-                "near earth asteroid rendezvous"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains the NEAR infrared spectrometer (NIS) data for the CRUISE4 phase. The data set begins on 1998-12-24T00:00:00.000 and ends 2000-01-10T23:59:59.999 . The data are raw telemetry data, provided in engineering units, that have been reformatted into FITS file format (NASA Office of Science and Technology (NOST), 100-1.0). In addition to the raw spectrometer data, a calibration file and algorithm are available. This data set is archived as a set of CDROM images as a part of the NEAR EDR volume set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-nis-2-edr-cruise4-v1.0_nx8b-67sh",
+            "issued": "2021-05-21",
+            "keyword": [
+                "solar system",
+                "near earth asteroid rendezvous"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-NIS-2-EDR-CRUISE4-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-nis-2-edr-cruise4-v1.0_nx8b-67sh",
-            "description": "This data set contains the NEAR infrared spectrometer (NIS) data for the CRUISE4 phase. The data set begins on 1998-12-24T00:00:00.000 and ends 2000-01-10T23:59:59.999 . The data are raw telemetry data, provided in engineering units, that have been reformatted into FITS file format (NASA Office of Science and Technology (NOST), 100-1.0). In addition to the raw spectrometer data, a calibration file and algorithm are available. This data set is archived as a set of CDROM images as a part of the NEAR EDR volume set.",
-            "title": "NEAR NIS SPECTRA FOR CRUISE4",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEAR NIS SPECTRA FOR CRUISE4"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-STOOKEMAPS-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The Stooke Small Bodies Map collection contains maps of small solar system bodies in various projections, with and without latitude/longiude grids. The maps are based on the best available mission data for each object. The collection includes four asteroids: 243 Ida, 253 Mathilde, 433 Eros (pre-NEAR encounter) and 951 Gaspra; and five moons: J5 Amalthea, M1 Phobos, M2 Deimos, S7 Hyperion and S11 Epimetheus. The maps are in JPEG format and are presented as a document collection. The science data directory contains only a map list.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-stookemaps-v1.0_nx8h-qian",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "amalthea",
                 "epimetheus",
@@ -1164439,58 +1164441,37 @@
                 "deimos",
                 "hyperion"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-STOOKEMAPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-stookemaps-v1.0_nx8h-qian",
-            "description": "The Stooke Small Bodies Map collection contains maps of small solar system bodies in various projections, with and without latitude/longiude grids. The maps are based on the best available mission data for each object. The collection includes four asteroids: 243 Ida, 253 Mathilde, 433 Eros (pre-NEAR encounter) and 951 Gaspra; and five moons: J5 Amalthea, M1 Phobos, M2 Deimos, S7 Hyperion and S11 Epimetheus. The maps are in JPEG format and are presented as a document collection. The science data directory contains only a map list.",
-            "title": "STOOKE SMALL BODIES MAPS",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "STOOKE SMALL BODIES MAPS"
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
-            "identifier": "NASA-567",
             "description": "RSS",
-            "title": "PDS Odyssey Radio Science Data (97)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1164498,225 +1164479,219 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-567",
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
+            "title": "PDS Odyssey Radio Science Data (97)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-ESC3-67PCHURYUMOV-M20-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-08-25T23:25:00.000 to 2015-09-22T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-esc3-67pchuryumov-m20-v3.0_nxbx-3ayz",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "bias",
                 "dark"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-ESC3-67PCHURYUMOV-M20-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-esc3-67pchuryumov-m20-v3.0_nxbx-3ayz",
-            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-08-25T23:25:00.000 to 2015-09-22T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 2 ESC3-MTP020 EDR V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 2 ESC3-MTP020 EDR V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D30.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler\r\n. 2019-11-07. VNP43D30. Version 001. VIIRS/NPP BRDF/Albedo Parameter 3 VIS Daily L3 Global 30 ArcSec CMG V001\r\n. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VNP43D30.001. https://doi.org/10.5067/VIIRS/VNP43D30.001. Digital Science Data. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
-            "issued": "2019-11-07",
-            "temporal": "2012-01-19T00:00:00Z/2024-05-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-11-07",
-            "keyword": [
-                "surface radiative properties",
-                "land surface",
-                "earth science"
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
-            "identifier": "C1607326974-LPDAAC_ECS",
-            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Model Parameter 3 VIS product (VNP43D30) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. Each of the three model parameters (isotropic, volumetric, and geometric) for each of the nine VIIRS moderate resolution bands along with the visible (VIS), near-infrared (NIR), and shortwave bands included in the VNP43MA1 (https://doi.org/10.5067/VIIRS/VNP43MA1.001) product is stored in a separate file as VNP43D01 through VNP43D36. In addition to the bands included in VNP43MA1, this product suite includes model parameters for the VIIRS Day/Night Band (DNB) as VNP43D37 through VNP43D39. Details regarding methodology are available on the VNP43MA1 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D30 is the BRDF geometric parameter for the VIIRS visible broadband (0.64 \u03bcm). The geometric parameter, in conjunction with the isotropic and volumetric parameters, is used to derive the BRDF/Albedo values for the VIIRS visible broadband.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "VNP43D30",
             "creator": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler",
-            "title": "VIIRS/NPP BRDF/Albedo Parameter 3 VIS Daily L3 Global 30 ArcSec CMG V001",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Model Parameter 3 VIS product (VNP43D30) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. Each of the three model parameters (isotropic, volumetric, and geometric) for each of the nine VIIRS moderate resolution bands along with the visible (VIS), near-infrared (NIR), and shortwave bands included in the VNP43MA1 (https://doi.org/10.5067/VIIRS/VNP43MA1.001) product is stored in a separate file as VNP43D01 through VNP43D36. In addition to the bands included in VNP43MA1, this product suite includes model parameters for the VIIRS Day/Night Band (DNB) as VNP43D37 through VNP43D39. Details regarding methodology are available on the VNP43MA1 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D30 is the BRDF geometric parameter for the VIIRS visible broadband (0.64 \u03bcm). The geometric parameter, in conjunction with the isotropic and volumetric parameters, is used to derive the BRDF/Albedo values for the VIIRS visible broadband.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D30.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D30.001",
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
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D30.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D30.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/xhdf5",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D30.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D30.001/",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607326974-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607326974-LPDAAC_ECS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D30.001/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D30.001/contents.html",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D30",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D30",
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
+            "identifier": "C1607326974-LPDAAC_ECS",
+            "issued": "2019-11-07",
+            "keyword": [
+                "surface radiative properties",
+                "land surface",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D30.001",
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
+            "series-name": "VNP43D30",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-19T00:00:00Z/2024-05-20T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP BRDF/Albedo Parameter 3 VIS Daily L3 Global 30 ArcSec CMG V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/239QXXSBUD41",
             "citation": "William J. Blackwell, MIT Lincoln Laboratory. 2023-03-01. TROPICS01BRTTL1B. Version 1.0. TROPICS01\u00a0Pathfinder\u00a0L1B Orbital Geolocated Native-Resolution Brightness Temperatures V1.0. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/239QXXSBUD41. https://disc.gsfc.nasa.gov/datacollection/TROPICS01BRTTL1B_1.0.html. Digital Science Data.",
-            "issued": "2021-07-19",
-            "temporal": "2021-07-19T00:00:00Z/2024-02-12T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-07-19",
-            "references": [
-                "https://doi.org/10.5067/239QXXSBUD41"
-            ],
-            "keyword": [
-                "spectral/engineering",
-                "microwave",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kristan Morgan",
                 "hasEmail": "mailto:kristan.l.morgan@nasa.gov"
             },
+            "creator": "William J. Blackwell, MIT Lincoln Laboratory",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2622841366-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The \"Time-Resolved Observations of Precipitation structure and storm Intensity with a Constellation of Smallsats\" (TROPICS) mission has a goal of providing nearly all-weather observations of three-dimensional temperature and humidity, as well as cloud ice and precipitation horizontal structure, at high temporal resolution to conduct high-value science investigations of tropical cyclones.  The mission comprises a constellation of six identical Space Vehicles (SVs) conforming to the 3U form factor and hosting a passive microwave spectrometer payload.  This dataset is produced from the Pathfinder satellite, a single 3U small satellite, which has launched previous to the constellation, on a sun-synchronous orbital plane.\n\nEach SV hosts an identical high-performance spectrometer named the TROPICS Millimeter-wave Sounder (TMS) that will provide temperature profiles using seven channels near the 118.75-GHz oxygen absorption line, water vapor profiles using three channels near the 183-GHz water vapor absorption line, imagery in a single channel near 90 GHz for precipitation measurements (when combined with higher resolution water vapor channels), and a single channel near 205 GHz that is more sensitive to cloud-sized ice particles.\n\nEach TROPICS netCDF file contains a granule of data with 81 spots and approximately 2880 scans, where a granule is defined as an orbit's worth of data.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "TROPICS01BRTTL1B",
-            "creator": "William J. Blackwell, MIT Lincoln Laboratory",
-            "title": "TROPICS01\u00a0Pathfinder\u00a0L1B Orbital Geolocated Native-Resolution Brightness Temperatures V1.0",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TROPICS01ANTTL1A_01.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F239QXXSBUD41",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F239QXXSBUD41",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1164726,350 +1164701,384 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TROPICS01BRTTL1B_1.0.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TROPICS01BRTTL1B_1.0.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/.Twp5FGhb5T/TROPICS_L1B/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/.Twp5FGhb5T/TROPICS_L1B/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/opendap/.Twp5FGhb5T/TROPICS_L1B/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/opendap/.Twp5FGhb5T/TROPICS_L1B/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TROPICSBRTTL1B_1.0",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TROPICSBRTTL1B_1.0",
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
+            "identifier": "C2622841366-GES_DISC",
+            "issued": "2021-07-19",
+            "keyword": [
+                "spectral/engineering",
+                "microwave",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/239QXXSBUD41",
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
+                "https://doi.org/10.5067/239QXXSBUD41"
+            ],
+            "release-place": "Greenbelt, MD",
+            "series-name": "TROPICS01BRTTL1B",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2021-07-19T00:00:00Z/2024-02-12T00:00:00Z",
             "theme": [
                 "TROPICS (EVI-3)",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPICS01\u00a0Pathfinder\u00a0L1B Orbital Geolocated Native-Resolution Brightness Temperatures V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GNSS/GNSS_HOURLY_N_001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "International GNSS Service, Hourly 30-second GPS broadcast ephemeris data, Greenbelt, MD, USA:NASA Crustal Dynamics Data Information System (CDDIS), Accessed [[enter user data access date]] at doi:10.5067/GNSS/gnss_hourly_n_001",
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
-            "identifier": "C1419774535-CDDIS",
             "description": "This dataset consists of ground-based Global Navigation Satellite System (GNSS) GPS Broadcast Ephemeris Data (hourly files) from the NASA Crustal Dynamics Data Information System (CDDIS). GNSS provide autonomous geo-spatial positioning with global coverage. GNSS data sets from ground receivers at the CDDIS consist primarily of the data from the U.S. Global Positioning System (GPS) and the Russian GLObal NAvigation Satellite System (GLONASS). Since 2011, the CDDIS GNSS archive includes data from other GNSS (Europe\u2019s Galileo, China\u2019s Beidou, Japan\u2019s Quasi-Zenith Satellite System/QZSS, the Indian Regional Navigation Satellite System/IRNSS, and worldwide Satellite Based Augmentation Systems/SBASs), which are similar to the U.S. GPS in terms of the satellite constellation, orbits, and signal structure. The hourly GPS broadcast ephemeris files contain one day of GPS broadcast navigation data in RINEX format from a global permanent network of ground-based receivers, one file per site. More information about these data is available on the CDDIS website at https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/hourly_30second_data.html.",
-            "title": "Ground-Based Global Navigation Satellite System (GNSS) GPS Broadcast Ephemeris Data (hourly files) from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGNSS_HOURLY_N_001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGNSS_HOURLY_N_001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/archive/gnss/data/hourly",
-                    "description": "URL for retrieval of GNSS hourly data through https",
                     "@type": "dcat:Distribution",
+                    "description": "URL for retrieval of GNSS hourly data through https",
+                    "downloadURL": "https://cddis.nasa.gov/archive/gnss/data/hourly",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/broadcast_ephemeris_data.html",
-                    "description": "URL for more information about GNSS hourly GPS broadcast navigation data",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about GNSS hourly GPS broadcast navigation data",
+                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/broadcast_ephemeris_data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/GNSS/GNSS_HOURLY_N_001",
-                    "description": "URL for more information about GNSS hourly GPS broadcast navigation data",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about GNSS hourly GPS broadcast navigation data",
+                    "downloadURL": "https://doi.org/10.5067/GNSS/GNSS_HOURLY_N_001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1419774535-CDDIS",
+            "issued": "1992-01-01",
+            "keyword": [
+                "earth science",
+                "solid earth",
+                "geodetics",
+                "gravity/gravitational field",
+                "tectonics"
+            ],
+            "landingPage": "https://doi.org/10.5067/GNSS/GNSS_HOURLY_N_001",
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
+            "title": "Ground-Based Global Navigation Satellite System (GNSS) GPS Broadcast Ephemeris Data (hourly files) from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/302",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Way, J., K. McDonald, and R. Zimmermann. 1998. BOREAS RSS-17 Stem, Soil, and Air Temperature Data. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/302",
-            "issued": "2023-11-22",
-            "temporal": "1993-10-25T00:00:00Z/1995-04-26T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-27",
-            "keyword": [
-                "earth science",
-                "vegetation",
-                "biosphere",
-                "soils",
-                "land surface",
-                "atmospheric temperature",
-                "atmosphere",
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
-            "identifier": "C2807645356-ORNL_CLOUD",
             "description": "Contains the soil and stem temperature measurements collected by RSS17 at various flux sites:  (1) Southern Study Area (SSA) at the Old Black Spruce (OBS), Old Jack Pine (OJP), Old Aspen (OA), and Young Jack Pine (YJP); and (2) Northern Study Area (NSA) O",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS RSS-17 Stem, Soil, and Air Temperature Data",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F302",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F302",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/RSS/rs7ssatd/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/RSS/rs7ssatd/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/RSS17_Stem_Temp.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/RSS17_Stem_Temp.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/302",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/302",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rs7ssatd/comp/rs7ssatd.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rs7ssatd/comp/rs7ssatd.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rs7ssatd/comp/RSS17_Stem_Temp.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rs7ssatd/comp/RSS17_Stem_Temp.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rs7ssatd/comp/RSS17_Stem_Temp.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rs7ssatd/comp/RSS17_Stem_Temp.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rs7ssatd/comp/RSS17_Stem_Temp.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rs7ssatd/comp/RSS17_Stem_Temp.txt",
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
+            "identifier": "C2807645356-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "earth science",
+                "vegetation",
+                "biosphere",
+                "soils",
+                "land surface",
+                "atmospheric temperature",
+                "atmosphere",
+                "ecosystems"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/302",
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
             "spatial": "-106.2 53.63 -98.48 55.88",
+            "temporal": "1993-10-25T00:00:00Z/1995-04-26T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS RSS-17 Stem, Soil, and Air Temperature Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://podaac.jpl.nasa.gov/ws/metadata/granule/index.html",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2015-11-30",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "https://data.nasa.gov/developer"
-            ],
-            "keyword": [
-                "api",
-                "earth science research",
-                "oceanography",
-                "granule"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jason Duley",
                 "hasEmail": "mailto:jason.duley@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "API-27",
             "description": "PO.DAAC provides several ways to discover and access physical oceanography data, from the PO.DAAC Web Portal to FTP access to front-end user interfaces (see http://podaac.jpl.nasa.gov).  That same data can also be discovered and accessed through PO.DAAC Web Services, enabling efficient machine-to-machine communication and data transfers. Granule metadata service Retrieves the metadata of a granule(s) in PO.DAAC's catalog.",
-            "title": "JPL Physical Oceanography Distributed Active Archive Center (PODAAC) Granules Metadata API",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://podaac.jpl.nasa.gov/ws/metadata/granule/index.html",
-                    "description": "PO.DAAC provides several ways to discover and access physical oceanography data, from the PO.DAAC Web Portal to FTP access to front-end user interfaces (see http://podaac.jpl.nasa.gov).  That same data can also be discovered and accessed through PO.DAAC Web Services, enabling efficient machine-to-machine communication and data transfers. Granule metadata service Retrieves the metadata of a granule(s) in PO.DAAC's catalog.",
                     "@type": "dcat:Distribution",
+                    "description": "PO.DAAC provides several ways to discover and access physical oceanography data, from the PO.DAAC Web Portal to FTP access to front-end user interfaces (see http://podaac.jpl.nasa.gov).  That same data can also be discovered and accessed through PO.DAAC Web Services, enabling efficient machine-to-machine communication and data transfers. Granule metadata service Retrieves the metadata of a granule(s) in PO.DAAC's catalog.",
+                    "downloadURL": "http://podaac.jpl.nasa.gov/ws/metadata/granule/index.html",
+                    "mediaType": "text/html",
                     "title": "JPL Physical Oceanography Distributed Active Archive Center (PODAAC) Granules Metadata API"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "API-27",
+            "issued": "2015-11-30",
+            "keyword": [
+                "api",
+                "earth science research",
+                "oceanography",
+                "granule"
+            ],
+            "landingPage": "http://podaac.jpl.nasa.gov/ws/metadata/granule/index.html",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "references": [
+                "https://data.nasa.gov/developer"
+            ],
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "JPL Physical Oceanography Distributed Active Archive Center (PODAAC) Granules Metadata API"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-PEPSSI-4-PLASMA-V1.0",
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
-                "new horizons"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains higher level products derived from data taken by the New Horizons Pluto Energetic Particle Spectrometer Science Investigation (PEPSSI) instrument during the Pluto encounter mission phase.  The data products contain proton and ion fluxes at five second, five minute, and three hour averages, with the corresponding attitude and ephemeris data. This is VERSION 1.0 of this data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-pepssi-4-plasma-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-PEPSSI-4-PLASMA-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-pepssi-4-plasma-v1.0",
-            "description": "This data set contains higher level products derived from data taken by the New Horizons Pluto Energetic Particle Spectrometer Science Investigation (PEPSSI) instrument during the Pluto encounter mission phase.  The data products contain proton and ion fluxes at five second, five minute, and three hour averages, with the corresponding attitude and ephemeris data. This is VERSION 1.0 of this data set.",
-            "title": "NEW HORIZONS PEPSSI PLUTO ENCOUNTER\n                                      PLASMA FLUXES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS PEPSSI PLUTO ENCOUNTER\n                                      PLASMA FLUXES V1.0"
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
+            "description": "Exp: Round Synthetic Jets for Separation Control on 2-D Ramp This web page provides data from experiments that may be useful for the validation of turbulence models. This resource is expected to grow gradually over time. All data herein arepublicly available.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://turbmodels.larc.nasa.gov/Other_exp_Data/Roundjet/F40Hz.tar.gz",
+                    "mediaType": "application/x-gzip"
+                }
             ],
+            "identifier": "NASA-852__1",
+            "issued": "2018-06-25",
             "keyword": [
                 "jets",
                 "validation",
@@ -1165081,495 +1165090,488 @@
                 "ramp",
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
-            "identifier": "NASA-852__1",
-            "description": "Exp: Round Synthetic Jets for Separation Control on 2-D Ramp This web page provides data from experiments that may be useful for the validation of turbulence models. This resource is expected to grow gradually over time. All data herein arepublicly available.",
-            "title": "Turbulence Models: Data from Other Experiments: Round Synthetic Jets for Separation Control on 2-D Ramp",
-            "programCode": [
-                "026:023"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://turbmodels.larc.nasa.gov/Other_exp_Data/Roundjet/F40Hz.tar.gz",
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
+            "title": "Turbulence Models: Data from Other Experiments: Round Synthetic Jets for Separation Control on 2-D Ramp"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1439296101-OMINRT.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, OMI SIPS.",
-            "issued": "2017-11-14",
-            "temporal": "2011-10-28T11:50:43Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-11-14",
-            "keyword": [
-                "nasa"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:support@earthdata.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "OMI SIPS"
-            },
-            "identifier": "C1439296101-OMINRT",
             "description": "The OMPS-NPP L2 NP Ozone (O3) Total Column swath orbital product provides ozone profile retrievals from the Ozone Mapping and Profiling Suite (OMPS) Nadir-Profiler (NP) instrument on the Suomi-NPP satellite in Near Real Time. The V8 ozone profile algorithm relies on nadir profiler measurements made in the 250 to 310 nm range, as well as from measurements from the nadir mapper in the 300 to 380 nm range. Ozone mixing ratios are reported at 15 pressure levels between 50 and 0.5 hPa. Additionally, this data product contains measurements of total ozone, UV aerosol index and reflectivities at 331 and 380 nm. Each granule contains data from the daylight portion of each orbit measured for a full day. Spatial coverage is global (-82 to +82 degrees latitude), and there are about 14.5 orbits per day, each has typically 80 profiles. The NP footprint size is 250 km x 250 km. The L2 NP Ozone data are written using the Hierarchical Data Format Version 5 or HDF5.",
-            "title": "OMPS-NPP L2 NP Ozone (O3) Vertical Profile swath orbital NRT",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1439296101-OMINRT.html",
-                    "description": "View this dataset on the CMR (Common Metadata Repository)",
                     "@type": "dcat:Distribution",
+                    "description": "View this dataset on the CMR (Common Metadata Repository)",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1439296101-OMINRT.html",
+                    "mediaType": "text/html",
                     "title": "CMR"
                 }
             ],
-            "theme": [
-                "geospatial"
+            "identifier": "C1439296101-OMINRT",
+            "issued": "2017-11-14",
+            "keyword": [
+                "nasa"
             ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1439296101-OMINRT.html",
             "language": [
                 "en-US"
-            ]
+            ],
+            "modified": "2017-11-14",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "OMI SIPS"
+            },
+            "temporal": "2011-10-28T11:50:43Z/2022-01-17T00:00:00Z",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "OMPS-NPP L2 NP Ozone (O3) Vertical Profile swath orbital NRT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMAG-4-ESC2-RESAMPLED-V9.0",
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
+            "description": "This dataset contains RESAMPLED DATA (CODMAC LEVEL 4) of the\nCOMET ESCORT 2 Phase from March 11, 2015 until June 30, 2015\nof the ROSETTA orbiter magnetometer RPCMAG. Data are averaged to 1s means and\n60s means. Observations are done in the vicinity of comet\n67P/CHURYUMOV-GERASIMENKO 1 (1969 R1).\nThe current version of the dataset is V9.0.\nThe difference to the datasets of earlier versions is mainly a significantly\nimproved sensor temperature model, more detailed documentation about magnetic\ndisturbance sources, more data handling information for the user and\nalso an improved quality flagging system.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmag-4-esc2-resampled-v9.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMAG-4-ESC2-RESAMPLED-V9.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmag-4-esc2-resampled-v9.0",
-            "description": "This dataset contains RESAMPLED DATA (CODMAC LEVEL 4) of the\nCOMET ESCORT 2 Phase from March 11, 2015 until June 30, 2015\nof the ROSETTA orbiter magnetometer RPCMAG. Data are averaged to 1s means and\n60s means. Observations are done in the vicinity of comet\n67P/CHURYUMOV-GERASIMENKO 1 (1969 R1).\nThe current version of the dataset is V9.0.\nThe difference to the datasets of earlier versions is mainly a significantly\nimproved sensor temperature model, more detailed documentation about magnetic\ndisturbance sources, more data handling information for the user and\nalso an improved quality flagging system.",
-            "title": "ROSETTA-ORBITER 67P RPCMAG 4 ESC2 RESAMPLED V9.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCMAG 4 ESC2 RESAMPLED V9.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL-MIDAS-3-GRND-REF-2013-V1.0",
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
+            "description": "The Micro-Imaging Dust Analysis System (MIDAS) is an instrument on the\nROSETTA Orbiter that will provide 3D images and statistical parameters\nof pristine cometary particles, collected in the vicinity of comet\n67P/Churyumov-Gerasimenko. This data set includes reference\nmeasurement\ndata acquired with the flight spare unit (FS) on ground, which was\nused\nfor improving the accuracy of the images gathered by the actual flight\nunit and to develop adequate measuement procedures for flight. The\ntest\ndata was collected during several years and spawns several data sets,\nin order to keep the individual data set size on a reasonable level.\nThe current dataset contains data from 2013.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-midas-3-grnd-ref-2013-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "calibration",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL-MIDAS-3-GRND-REF-2013-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-midas-3-grnd-ref-2013-v1.0",
-            "description": "The Micro-Imaging Dust Analysis System (MIDAS) is an instrument on the\nROSETTA Orbiter that will provide 3D images and statistical parameters\nof pristine cometary particles, collected in the vicinity of comet\n67P/Churyumov-Gerasimenko. This data set includes reference\nmeasurement\ndata acquired with the flight spare unit (FS) on ground, which was\nused\nfor improving the accuracy of the images gathered by the actual flight\nunit and to develop adequate measuement procedures for flight. The\ntest\ndata was collected during several years and spawns several data sets,\nin order to keep the individual data set size on a reasonable level.\nThe current dataset contains data from 2013.",
-            "title": "ROSETTA-ORBITER CAL MIDAS 3 GRND REFERENCE 2013 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CAL MIDAS 3 GRND REFERENCE 2013 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-A-UVS-3-RDR-V1.0",
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
+            "description": "TBD",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-a-uvs-3-rdr-v1.0_nxud-hk2g",
+            "issued": "2018-06-26",
+            "keyword": [
+                "galileo"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-A-UVS-3-RDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-a-uvs-3-rdr-v1.0_nxud-hk2g",
-            "description": "TBD",
-            "title": "GLL IDA UVS IDA ENCOUNTER RDR",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GLL IDA UVS IDA ENCOUNTER RDR"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/QFJ13GEGDI99",
             "citation": "Global Modeling and Assimilation Office (GMAO). 2020-11-15. M2SMNXEDI. Version 1. MERRA-2 statM_2d_edi_Nx: 2d, Single-Level, Monthly Extremes Detection Indices V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/QFJ13GEGDI99. https://disc.gsfc.nasa.gov/datacollection/M2SMNXEDI_1.html. Digital Science Data.",
-            "issued": "2020-10-19",
-            "temporal": "1980-01-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-10-19",
-            "references": [
-                "https://doi.org/10.1175/JCLI-D-16-0758.1"
-            ],
-            "keyword": [
-                "precipitation",
-                "earth science",
-                "climate indicators",
-                "atmosphere",
-                "atmospheric/ocean indicators",
-                "atmospheric temperature"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Suhung Shen",
                 "hasEmail": "mailto:suhung.shen-1@nasa.gov"
             },
+            "creator": "Global Modeling and Assimilation Office (GMAO)",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1949649168-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The Modern Era Retrospective analysis for Research and Applications, Version 2 (MERRA-2) contains a wealth of information that can be used for weather and climate studies. By combining the assimilation of observations with a frozen version of the Goddard Earth Observing System (GEOS), a global analysis is produced at an hourly temporal resolution spanning from January 1980 through present (Gelaro et al., 2017). It can be difficult to parse through a multidecadal dataset such as MERRA-2 to evaluate the interannual variability of weather that occurs on a daily timescale, let alone determine the occurrence of an extreme weather event. This data collection provides climate statistics compute using MERRA-2 to assist in the analysis of extreme temperature and precipitation events and the accompanying the large scale meteorological patterns across a time period of over four decades. \n\nFind the product File Specific, Readme, References, and data tools under \"Documentation\" tab.\n\nSign up for the MERRA-2 mailing list to receive announcements on the latest data information, tools and services that become available, data announcements from GMAO MERRA-2 project and more! Contact the GES DISC User Services (gsfc-dl-help-disc@mail.nasa.gov) to be added to the list.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "M2SMNXEDI",
-            "creator": "Global Modeling and Assimilation Office (GMAO)",
-            "graphic-preview-description": "M2SMNXEDI sample image: Total monthly precipitation from days > 95th percentile for Jan 1980 , unit=mm/day.",
-            "title": "MERRA-2 statM_2d_edi_Nx: 2d, Single-Level, Monthly Extremes Detection Indices V1 (M2SMNXEDI) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2SMNXEDI_1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FQFJ13GEGDI99",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FQFJ13GEGDI99",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2SMNXEDI_1.png",
-                    "description": "M2SMNXEDI sample image: Total monthly precipitation from days > 95th percentile for Jan 1980 , unit=mm/day. ",
                     "@type": "dcat:Distribution",
+                    "description": "M2SMNXEDI sample image: Total monthly precipitation from days > 95th percentile for Jan 1980 , unit=mm/day. ",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2SMNXEDI_1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/howto?tags=MERRA",
-                    "description": "Documents with exmaple on how to read and plot MERRA-2 data.",
                     "@type": "dcat:Distribution",
+                    "description": "Documents with exmaple on how to read and plot MERRA-2 data.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/howto?tags=MERRA",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://gmao.gsfc.nasa.gov/pubs/docs/Collow1341.pdf",
-                    "description": "File Specification Document",
                     "@type": "dcat:Distribution",
+                    "description": "File Specification Document",
+                    "downloadURL": "https://gmao.gsfc.nasa.gov/pubs/docs/Collow1341.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2SMNXEDI_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2SMNXEDI_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_CLIM/M2SMNXEDI.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_CLIM/M2SMNXEDI.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2SMNXEDI",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2SMNXEDI",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2_CLIM/M2SMNXEDI.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2_CLIM/M2SMNXEDI.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gmao.gsfc.nasa.gov/reanalysis/MERRA-2/docs/",
-                    "description": "The NASA GMAO MERRA-2 Data Documentation and FAQs",
                     "@type": "dcat:Distribution",
+                    "description": "The NASA GMAO MERRA-2 Data Documentation and FAQs",
+                    "downloadURL": "https://gmao.gsfc.nasa.gov/reanalysis/MERRA-2/docs/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_CLIM/M2SMNXEDI.1/doc/README_MERRA2_CLIMSTAT.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_CLIM/M2SMNXEDI.1/doc/README_MERRA2_CLIMSTAT.pdf",
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
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/dods/M2SMNXEDI.info",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/dods/M2SMNXEDI.info",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 }
             ],
+            "graphic-preview-description": "M2SMNXEDI sample image: Total monthly precipitation from days > 95th percentile for Jan 1980 , unit=mm/day.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2SMNXEDI_1.png",
+            "identifier": "C1949649168-GES_DISC",
+            "issued": "2020-10-19",
+            "keyword": [
+                "precipitation",
+                "earth science",
+                "climate indicators",
+                "atmosphere",
+                "atmospheric/ocean indicators",
+                "atmospheric temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/QFJ13GEGDI99",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-10-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1175/JCLI-D-16-0758.1"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "M2SMNXEDI",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1980-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "MERRA-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MERRA-2 statM_2d_edi_Nx: 2d, Single-Level, Monthly Extremes Detection Indices V1 (M2SMNXEDI) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/178",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hall, F. G., K. F. Huemmrich, D. E. Strebel, S. J. Goetz, J. E. Nickeson, and K. D. Woods. 1996. NWS Monthly Climatology Summary (SNF). [National Weather Service Monthly Climatology Summary (Superior National Forest)]. Data set. Available on-line [http://www.daac.ornl.gov] from Oak Ridge National Laboratory Distributed Active Archive Center, Oak Ridge, Tennessee, U.S.A. Based on F. G. Hall, K. F. Huemmrich, D. E. Strebel, S. J. Goetz, J. E. Nickeson, and K. D. Woods, Biophysical, Morphological, Canopy Optical Property, and Productivity Data from the Superior National Forest, NASA Technical Memorandum 104568, National Aeronautics and Space Administration, Goddard Space Flight Center, Greenbelt, Maryland, U.S.A., 1992. doi:10.3334/ORNLDAAC/178",
-            "issued": "2024-03-02",
-            "temporal": "1976-01-01T00:00:00Z/1986-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-04",
-            "keyword": [
-                "atmospheric radiation",
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
-            "identifier": "C2884978709-ORNL_CLOUD",
             "description": "Monthly averages of daily temperature, precipitation and insolation data collected by the NWS for region including the Superior National Forest",
-            "graphic-preview-description": "Browse Image",
-            "title": "NWS Monthly Climatology Summary (SNF)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/snf_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F178",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F178",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/snf/SNF_MET_SUMM/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/snf/SNF_MET_SUMM/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/SNF/guides/nws_monthly_climate_sum.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/SNF/guides/nws_monthly_climate_sum.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/178",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/178",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_SUMM/comp/met_summ.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_SUMM/comp/met_summ.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_SUMM/comp/met_summ.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_SUMM/comp/met_summ.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_SUMM/comp/nws_monthly_climate_sum.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_SUMM/comp/nws_monthly_climate_sum.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_SUMM/comp/nws_monthly_climate_sum.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_SUMM/comp/nws_monthly_climate_sum.txt",
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
+            "identifier": "C2884978709-ORNL_CLOUD",
+            "issued": "2024-03-02",
+            "keyword": [
+                "atmospheric radiation",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/178",
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
+            "title": "NWS Monthly Climatology Summary (SNF)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3349-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-09-17T06:49:48.000 to 2012-09-17T09:08:01.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3349-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars express"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3349-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3349-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-09-17T06:49:48.000 to 2012-09-17T09:08:01.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3349 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3349 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSINAC-2-CR2-CHECKOUT-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit,  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the CRUISE 2 mission phase, covering the period  from 2005-04-05T00:00:00.000 to 2006-07-28T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Reprocessed dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osinac-2-cr2-checkout-v2.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "2867 steins",
                 "9p/tempel 1 (1867 g1)",
@@ -1165579,272 +1165581,248 @@
                 "bias",
                 "starfield"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSINAC-2-CR2-CHECKOUT-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osinac-2-cr2-checkout-v2.0",
-            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit,  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the CRUISE 2 mission phase, covering the period  from 2005-04-05T00:00:00.000 to 2006-07-28T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Reprocessed dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER CHECKOUT OSINAC 2 CR2 EDR V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECKOUT OSINAC 2 CR2 EDR V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-PLS-5-SUMM-ION-L-MODE-96S-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-pls-5-summ-ion-l-mode-96s-v1.0_ny5q-9dhq",
+            "issued": "2018-06-26",
+            "keyword": [
+                "voyager",
+                "jupiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-PLS-5-SUMM-ION-L-MODE-96S-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-pls-5-summ-ion-l-mode-96s-v1.0_ny5q-9dhq",
-            "description": "not applicable",
-            "title": "VG1 JUP PLS DERIVED ION IN/OUTBND MAGSHTH L-MODE 96SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG1 JUP PLS DERIVED ION IN/OUTBND MAGSHTH L-MODE 96SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3252-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-07-23T07:18:06.000 to 2012-07-23T10:01:34.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3252-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars express"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3252-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3252-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-07-23T07:18:06.000 to 2012-07-23T10:01:34.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3252 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3252 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-DERIVED-LIGHTCURVE-V12.0",
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
+            "description": "This is a compilation of published rotational parameters derived from lightcurve data for asteroids, based on the Warner et al. (2009) Asteroid Lightcurve Database. This is the version released on Mar. 2, 2011. In addition to reported rotational parameters by individual paper, there is a summary file with the values adopted by Harris, Warner, and Pravec as the most likely correct values for each asteroid. The data set also contains files listing known binary asteroids and 'tumbling' asteroids.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-derived-lightcurve-v12.0_nybg-da4p",
+            "issued": "2018-06-26",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-DERIVED-LIGHTCURVE-V12.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-derived-lightcurve-v12.0_nybg-da4p",
-            "description": "This is a compilation of published rotational parameters derived from lightcurve data for asteroids, based on the Warner et al. (2009) Asteroid Lightcurve Database. This is the version released on Mar. 2, 2011. In addition to reported rotational parameters by individual paper, there is a summary file with the values adopted by Harris, Warner, and Pravec as the most likely correct values for each asteroid. The data set also contains files listing known binary asteroids and 'tumbling' asteroids.",
-            "title": "ASTEROID LIGHTCURVE DERIVED DATA V12.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ASTEROID LIGHTCURVE DERIVED DATA V12.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO_L4G_WUE.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Simon Hook, Gregory Halverson, Margaret Johnson, Kerry Cawse-Nicholson. 2024-05-09. ECOSTRESS Gridded Water Use Efficiency Instantaneous L4 Global 70 m v002. Version 002. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/ECOSTRESS/ECO_L4G_WUE.002. https://doi.org/10.5067/ECOSTRESS/ECO_L4G_WUE.002. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2024-05-09",
-            "temporal": "2018-07-09T00:00:00Z/2024-06-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-09",
-            "keyword": [
-                "earth science",
-                "land surface",
-                "surface thermal properties"
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
-            "identifier": "C2076109886-LPCLOUD",
-            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found on the ECOSTRESS website.\r\n\r\nThe ECOSTRESS Gridded Water Use Efficiency Instantaneous L4 Global 70 m (ECO_L4G_WUE) Version 2 data product provides Water Use Efficiency (WUE) data generated by dividing the Breathing Earth System Simulator (BESS) Gross Primary Production (GPP) by the Priestley-Taylor Jet Propulsion Laboratory Soil Moisture (PT-JPL-SM) transpiration to estimate WUE, the ratio of grams of carbon that plants absorb to kilograms of water that plants release. The product provides a BESS GPP estimate that represents the amount of carbon surrounding the plants. \r\n\r\nThe ECO_L4G_WUE Version 2 data product is available globally and projected to a globally snapped 0.0006\u00b0 grid with a 70 meter spatial resolution and is distributed in HDF5.  Each granule contains layers of Water Use Efficiency (WUE), Water Gross Primary Production (GPP), cloud mask, and water mask. A low-resolution browse is also available showing daily WUE as a stretched image with a color ramp in JPEG format.\r\n\r\nKnown Issues: *Data acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU, and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly, temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented, and science acquisitions resumed. To optimize the new acquisition approach, only Thermal Infrared (TIR) bands 2, 4, and 5 are being downloaded. The data products are the same as before, but the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023. *Data acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected. *Data acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "Simon Hook, Gregory Halverson, Margaret Johnson, Kerry Cawse-Nicholson",
-            "title": "ECOSTRESS Gridded Water Use Efficiency Instantaneous L4 Global 70 m V002",
-            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2797166445-LPCLOUD?h=85&w=85",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found on the ECOSTRESS website.\r\n\r\nThe ECOSTRESS Gridded Water Use Efficiency Instantaneous L4 Global 70 m (ECO_L4G_WUE) Version 2 data product provides Water Use Efficiency (WUE) data generated by dividing the Breathing Earth System Simulator (BESS) Gross Primary Production (GPP) by the Priestley-Taylor Jet Propulsion Laboratory Soil Moisture (PT-JPL-SM) transpiration to estimate WUE, the ratio of grams of carbon that plants absorb to kilograms of water that plants release. The product provides a BESS GPP estimate that represents the amount of carbon surrounding the plants. \r\n\r\nThe ECO_L4G_WUE Version 2 data product is available globally and projected to a globally snapped 0.0006\u00b0 grid with a 70 meter spatial resolution and is distributed in HDF5.  Each granule contains layers of Water Use Efficiency (WUE), Water Gross Primary Production (GPP), cloud mask, and water mask. A low-resolution browse is also available showing daily WUE as a stretched image with a color ramp in JPEG format.\r\n\r\nKnown Issues: *Data acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU, and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly, temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented, and science acquisitions resumed. To optimize the new acquisition approach, only Thermal Infrared (TIR) bands 2, 4, and 5 are being downloaded. The data products are the same as before, but the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023. *Data acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected. *Data acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECOSTRESS%2FECO_L4G_WUE.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECOSTRESS%2FECO_L4G_WUE.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/xhdf5",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2076109886-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2076109886-LPCLOUD",
+                    "mediaType": "application/xhdf5",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO_L4G_WUE.002",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO_L4G_WUE.002",
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
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1004/ECO4ESIALEXI_ATBD_V1.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1004/ECO4ESIALEXI_ATBD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2797166445-LPCLOUD?h=85&w=85",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2797166445-LPCLOUD?h=85&w=85",
+                    "mediaType": "text/html",
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
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2797166445-LPCLOUD?h=85&w=85",
+            "identifier": "C2076109886-LPCLOUD",
+            "issued": "2024-05-09",
+            "keyword": [
+                "earth science",
+                "land surface",
+                "surface thermal properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO_L4G_WUE.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-05-09",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-07-09T00:00:00Z/2024-06-03T00:00:00Z",
             "theme": [
                 "ECOSTRESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ECOSTRESS Gridded Water Use Efficiency Instantaneous L4 Global 70 m V002"
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
-                "turbulence",
-                "cases",
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
-            "identifier": "NASA-842__7",
             "description": "This grouping contains the incompressible-flow cases from the 1980-81 Data Library.",
-            "title": "Collaborative Testing of Turbulence Models: Incompressible Flow Cases from 1980-81 Data Library",
-            "programCode": [
-                "026:023"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1165852,1122 +1165830,1122 @@
                     "mediaType": "application/txt"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-842__7",
+            "issued": "2018-06-25",
+            "keyword": [
+                "flow",
+                "turbulence",
+                "cases",
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
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1777",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hanan, N.P., L. Prihodko, C.W. Ross, G. Bucini, and A.T. Tredennick. 2020. Gridded Estimates of Woody Cover and Biomass across Sub-Saharan Africa, 2000-2004. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1777",
-            "issued": "2020-08-10",
-            "temporal": "2000-01-01T00:00:00Z/2005-01-01T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-06",
-            "keyword": [
-                "vegetation",
-                "ecosystems",
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
-            "identifier": "C2762262652-ORNL_CLOUD",
             "description": "This dataset provides maps of woody (tree and shrub) cover and biomass across Sub-Saharan Africa at a resolution of 1 km for the period 2000-2004. Canopy cover observations and remote-sensing data related to woody vegetation were used to predict woody cover across Africa. Predicted woody cover, canopy height, and tree allometry were used to estimate woody biomass for Sub-Saharan Africa. Canopy cover observations were assembled from field measurements and Google Earth imagery collected from 2000-2004. Remote-sensing data related to the structural attributes of woody vegetation were derived from MODIS optical data and Q-SCAT (Quick Scatterometer) microwave measurements. Canopy height estimates were derived from spaceborne lidar and tree allometry equations were retrieved from GlobAllomeTree.",
-            "graphic-preview-description": "Estimates of woody biomass (tree and shrubs) at 1-km resolution in megagrams per hectare (Mg ha-1). Biomass was estimated from canopy cover, canopy height, and tree allometry.  Source: C.W. Ross",
-            "title": "Gridded Estimates of Woody Cover and Biomass across Sub-Saharan Africa, 2000-2004",
-            "graphic-preview-file": "https://daac.ornl.gov/VEGETATION/guides/Gridded_Biomass_Africa_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1777",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1777",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/Gridded_Biomass_Africa/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/Gridded_Biomass_Africa/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/Gridded_Biomass_Africa.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/Gridded_Biomass_Africa.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1777",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1777",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/Gridded_Biomass_Africa/comp/Gridded_Biomass_Africa.pdf",
-                    "description": "Gridded Estimates of Woody Cover and Biomass across Sub-Saharan Africa, 2000-2004: Gridded_Biomass_Africa.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Gridded Estimates of Woody Cover and Biomass across Sub-Saharan Africa, 2000-2004: Gridded_Biomass_Africa.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/Gridded_Biomass_Africa/comp/Gridded_Biomass_Africa.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/Gridded_Biomass_Africa_Fig1.png",
-                    "description": "Estimates of woody biomass (tree and shrubs) at 1-km resolution in megagrams per hectare (Mg ha-1). Biomass was estimated from canopy cover, canopy height, and tree allometry.  Source: C.W. Ross",
                     "@type": "dcat:Distribution",
+                    "description": "Estimates of woody biomass (tree and shrubs) at 1-km resolution in megagrams per hectare (Mg ha-1). Biomass was estimated from canopy cover, canopy height, and tree allometry.  Source: C.W. Ross",
+                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/Gridded_Biomass_Africa_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Estimates of woody biomass (tree and shrubs) at 1-km resolution in megagrams per hectare (Mg ha-1). Biomass was estimated from canopy cover, canopy height, and tree allometry.  Source: C.W. Ross",
+            "graphic-preview-file": "https://daac.ornl.gov/VEGETATION/guides/Gridded_Biomass_Africa_Fig1.png",
+            "identifier": "C2762262652-ORNL_CLOUD",
+            "issued": "2020-08-10",
+            "keyword": [
+                "vegetation",
+                "ecosystems",
+                "earth science",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1777",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-09-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-20.61 -34.81 61.53 22.01",
+            "temporal": "2000-01-01T00:00:00Z/2005-01-01T23:59:59Z",
             "theme": [
                 "Vegetation",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Gridded Estimates of Woody Cover and Biomass across Sub-Saharan Africa, 2000-2004"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1987",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Thompson, D.R., D.J. Jensen, J. Chapman, E. Greenberg, and M. Simard. 2022. Delta-X: AVIRIS-NG L1B Spectral Radiance Products, MRD, Louisiana, 2021. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1987",
-            "issued": "2022-05-02",
-            "temporal": "2021-03-27T09:58:10Z/2021-09-25T15:38:27Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "water quality/water chemistry",
-                "spectral/engineering",
-                "sensor characteristics",
-                "infrared wavelengths",
-                "ecosystems",
-                "terrestrial hydrosphere",
-                "vegetation",
-                "geomorphic landforms/processes",
-                "land surface",
-                "biosphere",
-                "earth science",
-                "visible wavelengths"
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
-            "identifier": "C2256471725-ORNL_CLOUD",
             "description": "This dataset provides Level 1B (L1B) radiance products from NASA's Airborne Visible Infrared Imaging Spectrometer- Next Generation (AVIRIS-NG) instrument acquired over the Atchafalaya and Terrebonne basins of the Mississippi River Delta, Louisiana, USA during two deployments; spring and fall of 2021. All flights were flown on a Dynamic Aviation King Air B200. There are a combined 200 total flight lines for the spring and fall 2021 deployments; spring 2021 had 75 flight lines, fall 2021 had 175 flight lines.  AVIRIS-NG measures reflected radiance at 5-nanometer (nm) intervals in the visible to shortwave infrared spectral range between 380 and 2510 nm. Level 1B data are orthorectified calibrated radiance values in units of spectral radiance in which raw digital numbers (DNs) are translated to units of radiant intensity measured at the sensor. Measurements are radiometrically and geometrically calibrated and provided at approximately 5-meter spatial resolution, dependent on aircraft altitude. Additional flight line files include band information of observational geometry and illumination parameters, as well as geographic pixel locations and elevation. These L1B data are provided in ENVI file format.  AVIRIS-NG Cal/Val, Level 2 and Level 3 products for the Pre-Delta-X and Delta-X missions are provided in related datasets.",
-            "graphic-preview-description": "True-color image of the AVIRIS-NG data collected over the Atchafalaya Basin in Spring 2021.  Source: authors.",
-            "title": "Delta-X: AVIRIS-NG L1B Spectral Radiance Products, MRD, Louisiana, 2021",
-            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L1_AVIRIS_Radiance_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1987",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1987",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/deltax/DeltaX_L1_AVIRIS_Radiance/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/deltax/DeltaX_L1_AVIRIS_Radiance/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L1_AVIRIS_Radiance.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L1_AVIRIS_Radiance.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1987",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1987",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/DeltaX_L1_AVIRIS_Radiance/comp/DeltaX_L1_AVIRIS_Radiance.pdf",
-                    "description": "Delta-X: AVIRIS-NG L1B Spectral Radiance Products, MRD, Louisiana, 2021: DeltaX_L1_AVIRIS_Radiance.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Delta-X: AVIRIS-NG L1B Spectral Radiance Products, MRD, Louisiana, 2021: DeltaX_L1_AVIRIS_Radiance.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/DeltaX_L1_AVIRIS_Radiance/comp/DeltaX_L1_AVIRIS_Radiance.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L1_AVIRIS_Radiance_Fig1.png",
-                    "description": "True-color image of the AVIRIS-NG data collected over the Atchafalaya Basin in Spring 2021.  Source: authors.",
                     "@type": "dcat:Distribution",
+                    "description": "True-color image of the AVIRIS-NG data collected over the Atchafalaya Basin in Spring 2021.  Source: authors.",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L1_AVIRIS_Radiance_Fig1.png",
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
+            "graphic-preview-description": "True-color image of the AVIRIS-NG data collected over the Atchafalaya Basin in Spring 2021.  Source: authors.",
+            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L1_AVIRIS_Radiance_Fig1.png",
+            "identifier": "C2256471725-ORNL_CLOUD",
+            "issued": "2022-05-02",
+            "keyword": [
+                "water quality/water chemistry",
+                "spectral/engineering",
+                "sensor characteristics",
+                "infrared wavelengths",
+                "ecosystems",
+                "terrestrial hydrosphere",
+                "vegetation",
+                "geomorphic landforms/processes",
+                "land surface",
+                "biosphere",
+                "earth science",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1987",
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
             "spatial": "-91.59 29.06 -89.68 29.85",
+            "temporal": "2021-03-27T09:58:10Z/2021-09-25T15:38:27Z",
             "theme": [
                 "Delta-X",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Delta-X: AVIRIS-NG L1B Spectral Radiance Products, MRD, Louisiana, 2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/767/",
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
-            "identifier": "DASHLINK_767",
             "description": "Lightning induced damage is one of the major concerns in aircraft health monitoring. Such short-duration high voltages can cause significant damage to electronic devices. This paper presents a study on the effects of lightning injection on power metal-oxide semiconductor field effect transistors (MOSFETs). This approach consisted of pin- injecting lightning waveforms into the gate, drain and/or source of MOSFET devices while they were in the OFF-state. Analysis of the characteristic curves of the devices showed that for certain injection modes the devices can accumulate considerable damage rendering them inoperable. Early results demonstrate that a power MOSFET, even in its off-state, can incur considerable damage due to lightning pin injection, leading to significant deviation in its behavior and performance, and to possibly early device failures.",
-            "title": "Effects of Lightning Injection on Power-MOSFETs",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2009_PHM_Lightning.pdf",
-                    "description": "2009_PHM_Lightning.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "2009_PHM_Lightning.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2009_PHM_Lightning.pdf",
+                    "mediaType": "application/pdf",
                     "title": "2009_PHM_Lightning.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_767",
+            "issued": "2013-06-19",
+            "keyword": [
+                "nasa",
+                "dashlink",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/767/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Effects of Lightning Injection on Power-MOSFETs"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0974-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-08-20T15:27:50.000 to 2015-08-20T17:26:42.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0974-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0974-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0974-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-08-20T15:27:50.000 to 2015-08-20T17:26:42.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0974 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0974 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D52.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang. 2021-02-22. MODIS/Terra+Aqua BRDF/Albedo White Sky Albedo Band1 Daily L3 Global 30ArcSec CMG V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MCD43D52.061. https://doi.org/10.5067/MODIS/MCD43D52.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-02-22",
-            "temporal": "2000-02-16T00:00:00Z/2024-05-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-22",
-            "keyword": [
-                "national geospatial data asset",
-                "land surface",
-                "surface radiative properties",
-                "earth science",
-                "ngda"
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
-            "identifier": "C2540273061-LPCLOUD",
-            "description": "The MCD43D52 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) White-Sky Albedo dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter (m)) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. \r\n\r\nMCD43D42 through MCD43D61 are the albedo products of the MCD43D BRDF/Albedo product suite. There are 10 black-sky albedo and 10 white-sky albedo layers representing MODIS bands 1 through 7 and the visible, near infrared (NIR), and shortwave bands. The black-sky albedo (directional hemispherical reflectance) is defined as albedo in the absence of a diffuse component and is a function of solar zenith angle. White-sky albedo (bihemispherical reflectance) is defined as albedo in the absence of a direct component when the diffuse component is isotropic. \r\n\r\nMCD43D52 is the white-sky albedo for MODIS band 1. \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
-            "release-place": "Sioux Falls, South Dakota, USA",
             "creator": "Crystal Schaaf, Zhuosen Wang",
-            "title": "MODIS/Terra+Aqua BRDF/Albedo White Sky Albedo Band1 Daily L3 Global 30ArcSec CMG V061",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MCD43D52 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) White-Sky Albedo dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter (m)) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. \r\n\r\nMCD43D42 through MCD43D61 are the albedo products of the MCD43D BRDF/Albedo product suite. There are 10 black-sky albedo and 10 white-sky albedo layers representing MODIS bands 1 through 7 and the visible, near infrared (NIR), and shortwave bands. The black-sky albedo (directional hemispherical reflectance) is defined as albedo in the absence of a diffuse component and is a function of solar zenith angle. White-sky albedo (bihemispherical reflectance) is defined as albedo in the absence of a direct component when the diffuse component is isotropic. \r\n\r\nMCD43D52 is the white-sky albedo for MODIS band 1. \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D52.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D52.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D52.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D52.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2540273061-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2540273061-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D52.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D52.061",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MCD43D52",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MCD43D52",
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
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D52.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D52.061/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2540273061-LPCLOUD",
+            "issued": "2021-02-22",
+            "keyword": [
+                "national geospatial data asset",
+                "land surface",
+                "surface radiative properties",
+                "earth science",
+                "ngda"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D52.061",
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
+            "title": "MODIS/Terra+Aqua BRDF/Albedo White Sky Albedo Band1 Daily L3 Global 30ArcSec CMG V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/LPVEX/MET/DATA201",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Moisseev, Dmitri N, Matti  Leskinen and Sabine  Goeke.2019. GPM Ground Validation Physicum Building Mast Meteorological Data LPVEx [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/LPVEX/MET/DATA201",
-            "issued": "2019-09-21",
-            "temporal": "2010-09-16T22:00:00Z/2010-10-22T21:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-23",
-            "keyword": [
-                "biosphere",
-                "atmospheric radiation",
-                "earth science",
-                "atmospheric winds",
-                "vegetation",
-                "atmospheric pressure",
-                "atmospheric water vapor",
-                "atmosphere",
-                "atmospheric temperature"
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
-            "identifier": "C1979684512-GHRC_DAAC",
             "description": "The GPM Ground Validation Physicum Building Mast Meteorological Data LPVEx dataset consists of meteorological data (temperature, pressure, wind, precipitation, and radiation) collected from the Station for Measuring Ecosystem-Atmosphere Relations III (SMEAR III) at the University of Helsinki\u2019s Physicum building rooftop weather station in Helsinki, Finland. These data were collected during the Global Precipitation Measurement (GPM) mission Light Precipitation Validation Experiment (LPVEx) field campaign that took place around the Gulf of Finland, aiming to provide additional high-latitude, light rainfall measurements for the improvement of GPM satellite precipitation algorithms. These meteorological data files are available from September 16 through October 22, 2010 in ASCII-CSV and ASCII text formats.",
-            "title": "GPM Ground Validation Physicum Building Mast Meteorological Data LPVEx V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FLPVEX%2FMET%2FDATA201",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FLPVEX%2FMET%2FDATA201",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmpmastmetlpvex",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmpmastmetlpvex",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
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
-                    "downloadURL": "https://ntrs.nasa.gov/search.jsp?R=20110015768",
-                    "description": "The NASA CloudSat/GPM Light Precipitation Validation Experiment (LPVEx)",
                     "@type": "dcat:Distribution",
+                    "description": "The NASA CloudSat/GPM Light Precipitation Validation Experiment (LPVEx)",
+                    "downloadURL": "https://ntrs.nasa.gov/search.jsp?R=20110015768",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.kippzonen.com/Download/86/Instruction-Sheet-Net-Radiometers-CNR1?ShowInfo=true",
-                    "description": "Instruction Sheet - CNR1 Net Radiometer",
                     "@type": "dcat:Distribution",
+                    "description": "Instruction Sheet - CNR1 Net Radiometer",
+                    "downloadURL": "https://www.kippzonen.com/Download/86/Instruction-Sheet-Net-Radiometers-CNR1?ShowInfo=true",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.kippzonen.com/Download/116/PAR-Lite-Manual?ShowInfo=true",
-                    "description": "PAR lite Photosynthetic Active Radiometer Instruction Manual",
                     "@type": "dcat:Distribution",
+                    "description": "PAR lite Photosynthetic Active Radiometer Instruction Manual",
+                    "downloadURL": "https://www.kippzonen.com/Download/116/PAR-Lite-Manual?ShowInfo=true",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www.vaisala.com/sites/default/files/documents/WAA151_User_Guide_in_English.pdf",
-                    "description": "Anemometer WAA151 User\u2019s Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Anemometer WAA151 User\u2019s Guide",
+                    "downloadURL": "https://www.vaisala.com/sites/default/files/documents/WAA151_User_Guide_in_English.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www.vaisala.com/sites/default/files/documents/WAV151_User_Guide_in_English.pdf",
-                    "description": "Wind Vane WAV151 User\u2019s Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Wind Vane WAV151 User\u2019s Guide",
+                    "downloadURL": "https://www.vaisala.com/sites/default/files/documents/WAV151_User_Guide_in_English.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.atm.helsinki.fi/globalsmear/images/Smear-concept-locked-11sept18.pdf",
-                    "description": "Station for Measuring Earth Surface-Atmosphere Relations - SMEAR Concept",
                     "@type": "dcat:Distribution",
+                    "description": "Station for Measuring Earth Surface-Atmosphere Relations - SMEAR Concept",
+                    "downloadURL": "http://www.atm.helsinki.fi/globalsmear/images/Smear-concept-locked-11sept18.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.atm.helsinki.fi/SMEAR/index.php/smear-iii",
-                    "description": "SMEAR",
                     "@type": "dcat:Distribution",
+                    "description": "SMEAR",
+                    "downloadURL": "https://www.atm.helsinki.fi/SMEAR/index.php/smear-iii",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.campbellsci.com/cnr1",
-                    "description": "CNR1 Net Radiometer",
                     "@type": "dcat:Distribution",
+                    "description": "CNR1 Net Radiometer",
+                    "downloadURL": "https://www.campbellsci.com/cnr1",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ott.com/en-us/products/meteorological-sensors-26/ott-pluvio2-weighing-rain-gauge-963/",
-                    "description": "OTT Pluvio2 - Weighing Rain Gauge",
                     "@type": "dcat:Distribution",
+                    "description": "OTT Pluvio2 - Weighing Rain Gauge",
+                    "downloadURL": "https://www.ott.com/en-us/products/meteorological-sensors-26/ott-pluvio2-weighing-rain-gauge-963/",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.picotech.com/library/application-note/pt100-platinum-resistance-thermometers",
-                    "description": "PT100 platinum resistance thermometers",
                     "@type": "dcat:Distribution",
+                    "description": "PT100 platinum resistance thermometers",
+                    "downloadURL": "https://www.picotech.com/library/application-note/pt100-platinum-resistance-thermometers",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www.vaisala.com/sites/default/files/documents/HUMICAP-Technology-description-B210781EN-C.pdf",
-                    "description": "Vaisala HUMICAP Sensor for Measuring Relative Humidity",
                     "@type": "dcat:Distribution",
+                    "description": "Vaisala HUMICAP Sensor for Measuring Relative Humidity",
+                    "downloadURL": "https://www.vaisala.com/sites/default/files/documents/HUMICAP-Technology-description-B210781EN-C.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.vaisala.com/en/products/instruments-sensors-and-other-measurement-devices/weather-stations-and-sensors/pwd12",
-                    "description": "Present Weather Detector PWD12",
                     "@type": "dcat:Distribution",
+                    "description": "Present Weather Detector PWD12",
+                    "downloadURL": "https://www.vaisala.com/en/products/instruments-sensors-and-other-measurement-devices/weather-stations-and-sensors/pwd12",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/lpvex/Meteorological_data/Physicum/doc/gpmpmastmetlpvex_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/lpvex/Meteorological_data/Physicum/doc/gpmpmastmetlpvex_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/lpvex/Meteorological_data/Physicum/doc/README.txt",
-                    "description": "Physicum Dataset ReadMe File",
                     "@type": "dcat:Distribution",
+                    "description": "Physicum Dataset ReadMe File",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/lpvex/Meteorological_data/Physicum/doc/README.txt",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://helda.helsinki.fi/bitstream/handle/10138/233627/ber14A-086.pdf?sequence=1",
-                    "description": "The urban measurement station SMEAR III: Continuous monitoring of air pollution and surface-atmosphere interactions in Helsinki, Finland",
                     "@type": "dcat:Distribution",
+                    "description": "The urban measurement station SMEAR III: Continuous monitoring of air pollution and surface-atmosphere interactions in Helsinki, Finland",
+                    "downloadURL": "https://helda.helsinki.fi/bitstream/handle/10138/233627/ber14A-086.pdf?sequence=1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
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
+            "identifier": "C1979684512-GHRC_DAAC",
+            "issued": "2019-09-21",
+            "keyword": [
+                "biosphere",
+                "atmospheric radiation",
+                "earth science",
+                "atmospheric winds",
+                "vegetation",
+                "atmospheric pressure",
+                "atmospheric water vapor",
+                "atmosphere",
+                "atmospheric temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/LPVEX/MET/DATA201",
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
             "spatial": "24.9533 60.1947 24.9733 60.2147",
+            "temporal": "2010-09-16T22:00:00Z/2010-10-22T21:00:00Z",
             "theme": [
                 "LPVEX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM Ground Validation Physicum Building Mast Meteorological Data LPVEx V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/BSEP59ADC6XN",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SnowEx23 Laser Snow Microstructure Specific Surface Area Data V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/BSEP59ADC6XN.",
-            "issued": "2023-03-06",
-            "temporal": "2023-03-06T00:00:00Z/2023-03-16T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-03-16",
-            "keyword": [
-                "earth science",
-                "cryosphere",
-                "snow/ice"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Hans-Peter Marshall",
                 "hasEmail": "mailto:hpmarshall@boisestate.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C2735033831-NSIDC_ECS",
             "description": "Preliminary: This data set reports vertical profiles of snow reflectance and specific surface area (SSA) in Alaska, USA, in two regions, the Fairbanks region characterized by spruce taiga forest and the arctic coast region characterized by coastal tundra. Reflectance was measured in situ using a 1310 nm and a 945 nm integrating sphere laser device and converted to SSA.",
-            "title": "SnowEx23 Laser Snow Microstructure Specific Surface Area Data V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FBSEP59ADC6XN",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FBSEP59ADC6XN",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX23_SSA.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX23_SSA.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX23_SSA+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX23_SSA+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX23_SSA/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX23_SSA/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/BSEP59ADC6XN",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/BSEP59ADC6XN",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/BSEP59ADC6XN",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/BSEP59ADC6XN",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2735033831-NSIDC_ECS",
+            "issued": "2023-03-06",
+            "keyword": [
+                "earth science",
+                "cryosphere",
+                "snow/ice"
+            ],
+            "landingPage": "https://doi.org/10.5067/BSEP59ADC6XN",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-03-16",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-149.5964 68.5284 -148.6127 70.084",
+            "temporal": "2023-03-06T00:00:00Z/2023-03-16T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SnowEx23 Laser Snow Microstructure Specific Surface Area Data V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MARSIS-3-RDR-SS-EXT1-V1.0",
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
-                "mars express",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains subsurface sounding data from the MARS EXPRESS MARS MARSIS EXPERIMENT DATA RECORD V2.0 Data Set that have been uncompressed, corrected for Automated Gain Control, aligned to a reference altitude and, except for data acquired using the SS2 mode, range processed after correcting for the distortion of the transmitted signal caused by the ionosphere.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-marsis-3-rdr-ss-ext1-v1.0_nytm-q6t7",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars express",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MARSIS-3-RDR-SS-EXT1-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-marsis-3-rdr-ss-ext1-v1.0_nytm-q6t7",
-            "description": "This dataset contains subsurface sounding data from the MARS EXPRESS MARS MARSIS EXPERIMENT DATA RECORD V2.0 Data Set that have been uncompressed, corrected for Automated Gain Control, aligned to a reference altitude and, except for data acquired using the SS2 mode, range processed after correcting for the distortion of the transmitted signal caused by the ionosphere.",
-            "title": "MARS EXPRESS MARSIS REDUCED DATA SUBSURFACE EXT 1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARSIS REDUCED DATA SUBSURFACE EXT 1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/348",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Saugier, B., and J.Y. Pontailler. 1998. BOREAS TE-11 Leaf Gas Exchange Measurements. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/348",
-            "issued": "2023-11-22",
-            "temporal": "1993-08-27T00:00:00Z/1994-08-19T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-28",
-            "keyword": [
-                "atmosphere",
-                "vegetation",
-                "atmospheric water vapor",
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
-            "identifier": "C2808129876-ORNL_CLOUD",
             "description": "Contains data collected by BOREAS TE-11 team on CO2 assimilation and transpiration in the SSA.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS TE-11 Leaf Gas Exchange Measurements",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F348",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F348",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TE/te11lgxd/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TE/te11lgxd/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TE11_Leaf_Gas_Exchange.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TE11_Leaf_Gas_Exchange.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/348",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/348",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te11lgxd/comp/te11lgxd.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te11lgxd/comp/te11lgxd.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te11lgxd/comp/TE11_Leaf_Gas_Exchange.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te11lgxd/comp/TE11_Leaf_Gas_Exchange.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te11lgxd/comp/TE11_Leaf_Gas_Exchange.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te11lgxd/comp/TE11_Leaf_Gas_Exchange.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te11lgxd/comp/TE11_Leaf_Gas_Exchange.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te11lgxd/comp/TE11_Leaf_Gas_Exchange.txt",
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
+            "identifier": "C2808129876-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "atmosphere",
+                "vegetation",
+                "atmospheric water vapor",
+                "biosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/348",
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
             "spatial": "53.92 -104.69",
+            "temporal": "1993-08-27T00:00:00Z/1994-08-19T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS TE-11 Leaf Gas Exchange Measurements"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/CLDPROPCOSP_D3_VIIRS_NOAA20.011",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MODIS Atmosphere Science Team. 2024-05-10. MODIS/Aqua Cloud Properties COSP Level 3 daily, 1x1 degree grid. Version 1.1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/MODIS/CLDPROPCOSP_D3_VIIRS_NOAA20.011. https://doi.org/10.5067/MODIS/CLDPROPCOSP_D3_VIIRS_NOAA20.011.",
-            "issued": "2024-02-10",
-            "temporal": "2018-02-17T00:00:00Z/2025-01-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-20",
-            "keyword": [
-                "clouds",
-                "atmosphere",
-                "atmospheric radiation",
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
-            "identifier": "C2946990777-LAADS",
-            "description": "The VIIRS/NOAA20 Cloud Properties COSP Level 3 daily, 1x1 degree grid product is a new L3 CLDPROP COSP Cloud product with short-name CLDPROPCOSP_D3_VIIRS_NOAA20.  It contains VIIRS NOAA-20 cloud mask, cloud top, and cloud optical retrieval data over daily timeframe. It provides a set of custom cloud-related parameters for better comparison with climate model output. The \u201cCOSP\u201d acronym in the short-name stands for  Cloud Feedback Model Intercomparison Project (CFMIP) Observation Simulator Package. Provided in netCDF4 format, it contains 32 aggregated science data sets (SDS/parameters).\n\nConsult the CLDPROPCOSP User Guide for details regarding how the L3 daily statistics are computed, and to learn more about the gridding and sampling protocols specific to this product and a number of other topics germane to the user community.  The collection of this product starts from February 17, 2018 and includes 365 granules each calendar year.",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "MODIS Atmosphere Science Team",
-            "title": "VIIRS/NOAA20 Cloud Properties COSP Level 3 daily, 1x1 deg. grid",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The VIIRS/NOAA20 Cloud Properties COSP Level 3 daily, 1x1 degree grid product is a new L3 CLDPROP COSP Cloud product with short-name CLDPROPCOSP_D3_VIIRS_NOAA20.  It contains VIIRS NOAA-20 cloud mask, cloud top, and cloud optical retrieval data over daily timeframe. It provides a set of custom cloud-related parameters for better comparison with climate model output. The \u201cCOSP\u201d acronym in the short-name stands for  Cloud Feedback Model Intercomparison Project (CFMIP) Observation Simulator Package. Provided in netCDF4 format, it contains 32 aggregated science data sets (SDS/parameters).\n\nConsult the CLDPROPCOSP User Guide for details regarding how the L3 daily statistics are computed, and to learn more about the gridding and sampling protocols specific to this product and a number of other topics germane to the user community.  The collection of this product starts from February 17, 2018 and includes 365 granules each calendar year.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FCLDPROPCOSP_D3_VIIRS_NOAA20.011",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FCLDPROPCOSP_D3_VIIRS_NOAA20.011",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/CLDPROPCOSP_D3_VIIRS_NOAA20.011",
-                    "description": "The product landing page",
                     "@type": "dcat:Distribution",
+                    "description": "The product landing page",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/CLDPROPCOSP_D3_VIIRS_NOAA20.011",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://atmosphere-imager.gsfc.nasa.gov/sites/default/files/ModAtmo/documents/L3_MCD06COSP_UserGuide_v1.5.pdf",
-                    "description": "Daily MCD06COSP product User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Daily MCD06COSP product User Guide",
+                    "downloadURL": "https://atmosphere-imager.gsfc.nasa.gov/sites/default/files/ModAtmo/documents/L3_MCD06COSP_UserGuide_v1.5.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/CLDPROPCOSP_D3_VIIRS_NOAA20--5111",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/CLDPROPCOSP_D3_VIIRS_NOAA20--5111",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/5111/CLDPROPCOSP_D3_VIIRS_NOAA20/",
-                    "description": "Direct access to CLDPROPCOSP_D3_VIIRS_NOAA20 data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to CLDPROPCOSP_D3_VIIRS_NOAA20 data set.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/5111/CLDPROPCOSP_D3_VIIRS_NOAA20/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/5111/CLDPROPCOSP_D3_VIIRS_NOAA20/contents.html",
-                    "description": "Direct access to product's OPeNDAP directory",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to product's OPeNDAP directory",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/5111/CLDPROPCOSP_D3_VIIRS_NOAA20/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2946990777-LAADS",
+            "issued": "2024-02-10",
+            "keyword": [
+                "clouds",
+                "atmosphere",
+                "atmospheric radiation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/CLDPROPCOSP_D3_VIIRS_NOAA20.011",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-02-17T00:00:00Z/2025-01-27T00:00:00Z",
             "theme": [
                 "NOAA - SPACE WEATHER PROGRAM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NOAA20 Cloud Properties COSP Level 3 daily, 1x1 deg. grid"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ERBE/S10N_WFOV_NF_EDITION2_NAT_L3",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2001-11-01. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ERBE/S10N_WFOV_NF_EDITION2_NAT_L3.",
-            "issued": "2014-03-13",
-            "temporal": "1984-11-01T00:00:00Z/1999-09-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-04-23",
-            "keyword": [
-                "earth science",
-                "atmospheric radiation",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "BRUCE, DR. BARKSTROM",
                 "hasEmail": "mailto:b.r.barkstrom@larc.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1000000800-LARC_ASDC",
             "description": "ERBE_S10N_WFOV_NF_Edition2 is the Earth Radiation Budget Experiment (ERBE) S-10N (Nonscanner-only) Wide Field of View (WFOV) Numerical Filter (NF) Radiant Flux and Albedo Edition 2 in Native Format data product. Data collection for this product is complete.\r\n\r\nThe reprocessed ERBE S10N_WFOV ERBS Edition2 data product contains temporally and spatially averaged shortwave (SW) and longwave (LW) top-of-the-atmosphere (TOA) fluxes derived from one month of Earth Radiation Budget Experiment non-scanning wide field-of-view instruments aboard the Earth Radiation Budget Satellite. Instantaneous TOA fluxes from the ERBE/ERBS S7 product were spatially averaged on a 5\u00b0 and 10\u00b0 equal-angle grid using numerical filter and shape factor techniques, respectively. ERBE scanner-independent temporal interpolation algorithms were applied to produce daily, monthly-hourly, and monthly mean fluxes from the instantaneous gridded data. The S10N_WFOV files contain both temporally averaged and instantaneous gridded mean values of TOA total-sky LW flux, total-sky SW flux, and total-sky albedo for each 5\u00b0 and 10\u00b0 region observed during the month. The major differences between Edition2 and the original release are in the monthly mean fluxes with (1) the incorporation of stochastic quality assurance algorithms for filtering out monthly-mean data with excessive temporal sample errors and (2) a self-consistent usage of the WFOV data in selecting scene-dependent directional models for temporal interpolation of the ERBE WFOV instantaneous gridded data.",
-            "title": "Earth Radiation Budget Experiment (ERBE) S-10N (Nonscanner-only) Wide Field of View (WFOV) Numerical Filter (NF) Radiant Flux and Albedo Edition 2 in Native Format",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FERBE%2FS10N_WFOV_NF_EDITION2_NAT_L3",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FERBE%2FS10N_WFOV_NF_EDITION2_NAT_L3",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/ERBE",
-                    "description": "ASDC Data and Information for ERBE",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for ERBE",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/ERBE",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ERBE/S10N_WFOV_NF_EDITION2_NAT_L3",
-                    "description": "DOI data set landing page for ERBE_S10N_WFOV_NF_Edition2",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for ERBE_S10N_WFOV_NF_Edition2",
+                    "downloadURL": "https://doi.org/10.5067/ERBE/S10N_WFOV_NF_EDITION2_NAT_L3",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000800-LARC_ASDC",
-                    "description": "Earthdata Search for ERBE_S10N_WFOV_NF_Edition2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for ERBE_S10N_WFOV_NF_Edition2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000800-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/read_software/erbe_s10n_edition2_read.zip",
-                    "description": "Read Software Package - ERBE_S10N_Edition2_Read Document - Direct File Download (.zip)",
                     "@type": "dcat:Distribution",
+                    "description": "Read Software Package - ERBE_S10N_Edition2_Read Document - Direct File Download (.zip)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/read_software/erbe_s10n_edition2_read.zip",
+                    "mediaType": "application/zip",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/read_software/gbytes.c",
-                    "description": "Tools for storage/retrieval of arbitrary size bytes from 32 bit words - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "Tools for storage/retrieval of arbitrary size bytes from 32 bit words - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/read_software/gbytes.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/read_software/io.c",
-                    "description": "Readme to work with FORTRAN - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "Readme to work with FORTRAN - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/read_software/io.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/guide/erbe_project.pdf",
-                    "description": "ERBE Langley ASDC Project Document",
                     "@type": "dcat:Distribution",
+                    "description": "ERBE Langley ASDC Project Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/guide/erbe_project.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/guide/erbe_s10n.pdf",
-                    "description": "ERBE Earth Radiant Fluxes and Albedo for Month Nonscanner (S-10N) Langley ASDC Data Set Document",
                     "@type": "dcat:Distribution",
+                    "description": "ERBE Earth Radiant Fluxes and Albedo for Month Nonscanner (S-10N) Langley ASDC Data Set Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/guide/erbe_s10n.pdf",
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/readme/readme_erbe_s10n_wfov_nf_edition2.txt",
-                    "description": "ERBE S-10N WFOV Edition2 Readme",
                     "@type": "dcat:Distribution",
+                    "description": "ERBE S-10N WFOV Edition2 Readme",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/readme/readme_erbe_s10n_wfov_nf_edition2.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/readme/readme_erbe_s10n_wfv_nf_nat_dmonotice1.txt",
-                    "description": "Note for S-10N/S-4N/S-4GN Product",
                     "@type": "dcat:Distribution",
+                    "description": "Note for S-10N/S-4N/S-4GN Product",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/readme/readme_erbe_s10n_wfv_nf_nat_dmonotice1.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's documented anomalies"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/quality_summaries/s10n_wfov/erbe_s10n_wfov_nf_sf_erbs_edition2.pdf",
-                    "description": "Quality Summary: ERBE S10N_WFOV ERBS Edition 2",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Summary: ERBE S10N_WFOV ERBS Edition 2",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/quality_summaries/s10n_wfov/erbe_s10n_wfov_nf_sf_erbs_edition2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/GEWEX-RFA",
-                    "description": "ASDC Data and Information for GEWEX-RFA",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for GEWEX-RFA",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/GEWEX-RFA",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthdata.nasa.gov/learn/sensing-our-planet/a-burning-question",
-                    "description": "Earth Observing System Data and InformationSystem (EOSDIS) Article: \"A Burning Question\" By Annette Varani",
                     "@type": "dcat:Distribution",
+                    "description": "Earth Observing System Data and InformationSystem (EOSDIS) Article: \"A Burning Question\" By Annette Varani",
+                    "downloadURL": "https://earthdata.nasa.gov/learn/sensing-our-planet/a-burning-question",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthdata.nasa.gov/learn/sensing-our-planet/absorption-of-solar-radiation-by-clouds-observations-versus-models",
-                    "description": "Earth Observing System Data and InformationSystem (EOSDIS) Article: \"Absorption of Solar Radiation by Clouds: Observations versus Models\"",
                     "@type": "dcat:Distribution",
+                    "description": "Earth Observing System Data and InformationSystem (EOSDIS) Article: \"Absorption of Solar Radiation by Clouds: Observations versus Models\"",
+                    "downloadURL": "https://earthdata.nasa.gov/learn/sensing-our-planet/absorption-of-solar-radiation-by-clouds-observations-versus-models",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/features/QuestionConvection",
-                    "description": "NASA Earth Observatory Article: NASA Earth Observatory Article",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: NASA Earth Observatory Article",
+                    "downloadURL": "https://earthobservatory.nasa.gov/features/QuestionConvection",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/readme/erbe_overview.pdf",
-                    "description": "ERBE Overview Document",
                     "@type": "dcat:Distribution",
+                    "description": "ERBE Overview Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/readme/erbe_overview.pdf",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/ERBE/S10N/WFOV_NF_Edition2/",
-                    "description": "ASDC Direct Data Download for ERBE_S10N_WFOV_NF_Edition2",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for ERBE_S10N_WFOV_NF_Edition2",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/ERBE/S10N/WFOV_NF_Edition2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1000000800-LARC_ASDC",
+            "issued": "2014-03-13",
+            "keyword": [
+                "earth science",
+                "atmospheric radiation",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ERBE/S10N_WFOV_NF_EDITION2_NAT_L3",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-04-23",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1984-11-01T00:00:00Z/1999-09-30T23:59:59.999Z",
             "theme": [
                 "ERBE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Earth Radiation Budget Experiment (ERBE) S-10N (Nonscanner-only) Wide Field of View (WFOV) Numerical Filter (NF) Radiant Flux and Albedo Edition 2 in Native Format"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA2519",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Read, W. and Livesey, N.. 2020-06-11. ML2SO2. Version 005. MLS/Aura Level 2 Sulfur Dioxide (SO2) Mixing Ratio V005. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA2519. https://disc.gsfc.nasa.gov/datacollection/ML2SO2_005.html. Digital Science Data.",
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
-            "identifier": "C1729926699-GES_DISC",
-            "description": "ML2SO2 is the EOS Aura Microwave Limb Sounder (MLS) standard product for sulfur dioxide derived from radiances measured by the 240 GHz radiometer. The data version is 5.0. Spatial coverage is near-global (-82 degrees to +82 degrees latitude), with each profile spaced 1.5 degrees or ~165 km along the orbit track (roughly 15 orbits per day). The recommended useful vertical range is from 215 to 10 hPa, and the vertical resolution is about 3 km. Users of the ML2SO2 data product should read section 3.21 of the EOS MLS Level 2 Version 5 Quality Document for more information.\n\nThe data are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5), which is based on the version 5 Hierarchical Data Format, or HDF-5. Each file contains two swath objects (profile and column data), each with a set of data and geolocation fields, swath attributes, and metadata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML2SO2",
             "creator": "Read, W. and Livesey, N.",
-            "title": "MLS/Aura Level 2 Sulfur Dioxide (SO2) Mixing Ratio V005 (ML2SO2) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2SO2_005.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "ML2SO2 is the EOS Aura Microwave Limb Sounder (MLS) standard product for sulfur dioxide derived from radiances measured by the 240 GHz radiometer. The data version is 5.0. Spatial coverage is near-global (-82 degrees to +82 degrees latitude), with each profile spaced 1.5 degrees or ~165 km along the orbit track (roughly 15 orbits per day). The recommended useful vertical range is from 215 to 10 hPa, and the vertical resolution is about 3 km. Users of the ML2SO2 data product should read section 3.21 of the EOS MLS Level 2 Version 5 Quality Document for more information.\n\nThe data are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5), which is based on the version 5 Hierarchical Data Format, or HDF-5. Each file contains two swath objects (profile and column data), each with a set of data and geolocation fields, swath attributes, and metadata.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA2519",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA2519",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1166977,293 +1166955,324 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML2SO2_005.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML2SO2_005.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level2/ML2SO2.005/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level2/ML2SO2.005/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level2/ML2SO2.005/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level2/ML2SO2.005/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML2SO2_005",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML2SO2_005",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2SO2_005.png",
+            "identifier": "C1729926699-GES_DISC",
+            "issued": "2020-02-04",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA2519",
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
+            "series-name": "ML2SO2",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MLS/Aura Level 2 Sulfur Dioxide (SO2) Mixing Ratio V005 (ML2SO2) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43C2.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler\r\n. 2019-11-07. VNP43C2. Version 001. VIIRS/NPP BRDF/Albedo Snow-free Model Parameters Daily L3 Global 0.05Deg CMG V001\r\n. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VNP43C2.001. https://doi.org/10.5067/VIIRS/VNP43C2.001. Digital Science Data. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
-            "issued": "2019-11-07",
-            "temporal": "2012-01-19T00:00:00Z/2024-06-03T00:00:00Z",
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
-            "identifier": "C1629257065-LPDAAC_ECS",
-            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Snow-free Model Parameters Daily Global 0.05 Degree Climate Modeling Grid (CMG) Version 1 product (VNP43C2) is derived from the 30 arc second CMG VNP43D Version 1 product suite. VNP43C2 is generated daily from all available snow-free acquisitions over a 16-day moving window emphasizing the ninth day of the retrieval period, which is reflected in the Julian date in the filename. VNP43C2 supplies the weighting parameters associated with the RossThick/Li-Sparse-Reciprocal BRDF model, which is used to produce the VNP43C3 Albedo and VNP43C4 Nadir BRDF-Adjusted Reflectance (NBAR) products. The highest quality full inversion values are used for the temporal fitting effort and supplemented with lower quality pixels, spatial fitting, and spatial smoothing as needed. The status of each pixel can be found in the ancillary layers. Users are encouraged to assess the quality information before using the BRDF/Albedo data. This 0.05 degree (5,600 meters at the equator) CMG product covers the entire globe for use in climate simulation models. \r\n\r\nThe VNP43C2 product includes 39 layers containing the three parameters (fiso, fvol, and fgeo) for the VIIRS Day/Night band (DNB), moderate resolution bands M1 through M5, M7, M8, M10, and M11, as well as the shortwave band, visible band, and near-infrared (NIR) broadbands. Along with the parameter data for the 13 bands are four ancillary layers for uncertainty, quality, local solar noon, and percent finer resolution inputs.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "VNP43C2",
             "creator": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler",
-            "title": "VIIRS/NPP BRDF/Albedo Snow-free Model Parameters Daily L3 Global 0.05Deg CMG V001",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Snow-free Model Parameters Daily Global 0.05 Degree Climate Modeling Grid (CMG) Version 1 product (VNP43C2) is derived from the 30 arc second CMG VNP43D Version 1 product suite. VNP43C2 is generated daily from all available snow-free acquisitions over a 16-day moving window emphasizing the ninth day of the retrieval period, which is reflected in the Julian date in the filename. VNP43C2 supplies the weighting parameters associated with the RossThick/Li-Sparse-Reciprocal BRDF model, which is used to produce the VNP43C3 Albedo and VNP43C4 Nadir BRDF-Adjusted Reflectance (NBAR) products. The highest quality full inversion values are used for the temporal fitting effort and supplemented with lower quality pixels, spatial fitting, and spatial smoothing as needed. The status of each pixel can be found in the ancillary layers. Users are encouraged to assess the quality information before using the BRDF/Albedo data. This 0.05 degree (5,600 meters at the equator) CMG product covers the entire globe for use in climate simulation models. \r\n\r\nThe VNP43C2 product includes 39 layers containing the three parameters (fiso, fvol, and fgeo) for the VIIRS Day/Night band (DNB), moderate resolution bands M1 through M5, M7, M8, M10, and M11, as well as the shortwave band, visible band, and near-infrared (NIR) broadbands. Along with the parameter data for the 13 bands are four ancillary layers for uncertainty, quality, local solar noon, and percent finer resolution inputs.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43C2.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43C2.001",
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
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43C2.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43C2.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43C2.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43C2.001/",
+                    "mediaType": "application/x-hdf",
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
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1629257065-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1629257065-LPDAAC_ECS",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43C2.001/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43C2.001/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.umb.edu/spectralmass/viirs-user-guide/vnp43c2-cmg-brdf-albedo-model-snow-free-parameters/",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://www.umb.edu/spectralmass/viirs-user-guide/vnp43c2-cmg-brdf-albedo-model-snow-free-parameters/",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43C2",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43C2",
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
+            "identifier": "C1629257065-LPDAAC_ECS",
+            "issued": "2019-11-07",
+            "keyword": [
+                "surface radiative properties",
+                "earth science",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43C2.001",
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
+            "series-name": "VNP43C2",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-19T00:00:00Z/2024-06-03T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP BRDF/Albedo Snow-free Model Parameters Daily L3 Global 0.05Deg CMG V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-GRAND-5-CERES-TPE-COUNTS-V1.0",
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
+            "description": "A global map thermal+epithermal         neutron counting rates binned on twenty-degree quasi-equal-area         pixels is provided. The map was determined from a time series           of the rate of neutron capture by lithium in the lithium-loaded         glass scintillator, part of the +Z phoswich sensor on Dawn's Gamma      Ray and Neutron Detector (GRaND). Neutrons in the thermal and           epithermal energy range contribute to the reaction. The data were       acquired while in low altitude mapping orbit, about 385 km from         Ceres' surface (about 0.8 body radii altitude). Prior to mapping,       the time series counting data were subjected to corrections for         variations in the flux of galactic cosmic rays and measurement          geometry, as described by PRETTYMANETAL2017.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-grand-5-ceres-tpe-counts-v1.0_nyzy-znr5",
+            "issued": "2018-06-26",
+            "keyword": [
+                "1 ceres",
+                "dawn mission to vesta and ceres"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-GRAND-5-CERES-TPE-COUNTS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-grand-5-ceres-tpe-counts-v1.0_nyzy-znr5",
-            "description": "A global map thermal+epithermal         neutron counting rates binned on twenty-degree quasi-equal-area         pixels is provided. The map was determined from a time series           of the rate of neutron capture by lithium in the lithium-loaded         glass scintillator, part of the +Z phoswich sensor on Dawn's Gamma      Ray and Neutron Detector (GRaND). Neutrons in the thermal and           epithermal energy range contribute to the reaction. The data were       acquired while in low altitude mapping orbit, about 385 km from         Ceres' surface (about 0.8 body radii altitude). Prior to mapping,       the time series counting data were subjected to corrections for         variations in the flux of galactic cosmic rays and measurement          geometry, as described by PRETTYMANETAL2017.",
-            "title": "DAWN GRAND MAP CERES TPE                \n                                      NEUTRON COUNTS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "DAWN GRAND MAP CERES TPE                \n                                      NEUTRON COUNTS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-U-CRS-4-SUMM-D1-96SEC-V1.0",
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
-                "uranus",
-                "voyager"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set describes data of the\ncounting rate from the D1 detector in the Cosmic Ray System (CRS) electron\ntelescope (TET) on Voyager 2 during the Uranus encounter. The D1 detector\nnominally responds to electrons with kinetic energies above approximately\n1 MeV (see detector description for details). Note that the instrument is\nsaturated near the maximum of counting rate of approximately 50,000 counts/sec\nbetween approximately 1986-01-24T18:10:50Z and 1986-01-24T19:02:02Z.  When\nthey are near saturation, the counting rates should be corrected for deadtime\naccording to the formula in the DATA_SET_OR_INST_PARM_DESC:\n{corrected rate} = {uncorrected rate/(1+deadtime*{uncorrected rate}).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-u-crs-4-summ-d1-96sec-v1.0_nz2t-39dv",
+            "issued": "2021-05-21",
+            "keyword": [
+                "uranus",
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-U-CRS-4-SUMM-D1-96SEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-u-crs-4-summ-d1-96sec-v1.0_nz2t-39dv",
-            "description": "This data set describes data of the\ncounting rate from the D1 detector in the Cosmic Ray System (CRS) electron\ntelescope (TET) on Voyager 2 during the Uranus encounter. The D1 detector\nnominally responds to electrons with kinetic energies above approximately\n1 MeV (see detector description for details). Note that the instrument is\nsaturated near the maximum of counting rate of approximately 50,000 counts/sec\nbetween approximately 1986-01-24T18:10:50Z and 1986-01-24T19:02:02Z.  When\nthey are near saturation, the counting rates should be corrected for deadtime\naccording to the formula in the DATA_SET_OR_INST_PARM_DESC:\n{corrected rate} = {uncorrected rate/(1+deadtime*{uncorrected rate}).",
-            "title": "VG2 URA CRS RESAMPLED SUMMARY D1 RATE\n                                      ELEC 96SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG2 URA CRS RESAMPLED SUMMARY D1 RATE\n                                      ELEC 96SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://fermi.gsfc.nasa.gov/ssc/data/access/lat/2nd_PSR_catalog/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://arxiv.org/abs/1305.4385"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Phil Newman",
+                "hasEmail": "mailto:panewman@lheapop.gsfc.nasa.gov"
+            },
+            "description": "The LAT Second Pulsar Catalog is available as a .tgz (tarred and zipped) archive file. The archive includes a main catalog FITS file with the data from the paper tables, images of the light curve and spectral energy distributions (SEDs) for each pulsar, FITS files containing the data points used in those images, and the timing parameters used in the analysis. A full description of the online archive is given in Appendix B of the preprint. Upon final publication, this catalog will also be generated as a BROWSE table that will be linked to this page.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://fermi.gsfc.nasa.gov/ssc/data/access/lat/2nd_PSR_catalog/combined_2PC_lightcurves.pdf",
+                    "mediaType": "application/pdf"
+                }
             ],
+            "identifier": "NASA-0000223__4",
+            "issued": "2018-06-25",
             "keyword": [
                 "gamma",
                 "high-energy",
@@ -1167281,153 +1167290,158 @@
                 "balloon",
                 "acd"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Phil Newman",
-                "hasEmail": "mailto:panewman@lheapop.gsfc.nasa.gov"
-            },
+            "landingPage": "http://fermi.gsfc.nasa.gov/ssc/data/access/lat/2nd_PSR_catalog/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:014"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000223__4",
-            "description": "The LAT Second Pulsar Catalog is available as a .tgz (tarred and zipped) archive file. The archive includes a main catalog FITS file with the data from the paper tables, images of the light curve and spectral energy distributions (SEDs) for each pulsar, FITS files containing the data points used in those images, and the timing parameters used in the analysis. A full description of the online archive is given in Appendix B of the preprint. Upon final publication, this catalog will also be generated as a BROWSE table that will be linked to this page.",
-            "title": "LAT Second Catalog of Gamma-ray Pulsars",
-            "programCode": [
-                "026:014"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://fermi.gsfc.nasa.gov/ssc/data/access/lat/2nd_PSR_catalog/combined_2PC_lightcurves.pdf",
-                    "mediaType": "application/pdf"
-                }
+            "references": [
+                "http://arxiv.org/abs/1305.4385"
             ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "LAT Second Catalog of Gamma-ray Pulsars"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC2-67P-M14-STRLIGHT-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 2 mission phase, covering the period from 2015-03-10T23:25:00.000 to 2015-04-08T11:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc2-67p-m14-strlight-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC2-67P-M14-STRLIGHT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc2-67p-m14-strlight-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 2 mission phase, covering the period from 2015-03-10T23:25:00.000 to 2015-04-08T11:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC2-MTP014 RDR-STRLIGHT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC2-MTP014 RDR-STRLIGHT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0921-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-07-26T10:17:05.000 to 2015-07-26T14:10:09.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0921-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0921-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0921-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-07-26T10:17:05.000 to 2015-07-26T14:10:09.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0921 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0921 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-GIA-3-ESC1-COMET-ESCORT-1-V1.0",
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
+            "description": "Comet Escort 1 Phase covers the period of time from the 21st November 2014  until the 10th March 2015. It started after Rosetta successfully completed the  Prelanding Phase. The present DataSet collects the GIADA data of ESC1 phase. The GIADA Scientific phase started on 7th May 2014 and was devoted to the characterization of the 67P environment.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-gia-3-esc1-comet-escort-1-v1.0_nz7g-st33",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-GIA-3-ESC1-COMET-ESCORT-1-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-gia-3-esc1-comet-escort-1-v1.0_nz7g-st33",
-            "description": "Comet Escort 1 Phase covers the period of time from the 21st November 2014  until the 10th March 2015. It started after Rosetta successfully completed the  Prelanding Phase. The present DataSet collects the GIADA data of ESC1 phase. The GIADA Scientific phase started on 7th May 2014 and was devoted to the characterization of the 67P environment.",
-            "title": "ROSETTA-ORBITER 67P GIADA 3 ESC1 COMET ESCORT 1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P GIADA 3 ESC1 COMET ESCORT 1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.nasa.gov/news/budget/index.html",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brian Dunbar",
+                "hasEmail": "mailto:brian.dunbar@nasa.gov"
+            },
+            "description": "NASA Financial Budget Documents, Strategic Plans and Performance Reports for fiscal year 2011.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "FY11 NASA Budget Administrator Remarks",
+                    "downloadURL": "http://www.nasa.gov/pdf/420994main_2011_Budget_Administrator_Remarks.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "NASA FY11 Budget Administrator Remarks"
+                }
+            ],
+            "identifier": "OCIO-Fitara-74",
             "issued": "2010-02-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "performance",
                 "plan",
@@ -1167436,69 +1167450,33 @@
                 "finance",
                 "financial"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brian Dunbar",
-                "hasEmail": "mailto:brian.dunbar@nasa.gov"
-            },
+            "landingPage": "http://www.nasa.gov/news/budget/index.html",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:046"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "NASA HQ"
             },
-            "identifier": "OCIO-Fitara-74",
-            "description": "NASA Financial Budget Documents, Strategic Plans and Performance Reports for fiscal year 2011.",
-            "title": "NASA Financial Budget Documents, Strategic Plans and Performance Reports 2011: NASA Budget Administrator Remarks",
-            "programCode": [
-                "026:046"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.nasa.gov/pdf/420994main_2011_Budget_Administrator_Remarks.pdf",
-                    "description": "FY11 NASA Budget Administrator Remarks",
-                    "@type": "dcat:Distribution",
-                    "title": "NASA FY11 Budget Administrator Remarks"
-                }
-            ],
-            "accrualPeriodicity": "R/P1Y",
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "NASA Financial Budget Documents, Strategic Plans and Performance Reports 2011: NASA Budget Administrator Remarks"
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
-                "models",
-                "incompressible",
-                "flow",
-                "cases"
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
-            "identifier": "NASA-844__26",
             "description": "This grouping contains the incompressible-flow cases from the 1980-81 Data Library.",
-            "title": "Collaborative Testing of Turbulence Models: Incompressible Flow Cases from 1980-81 Data Library",
-            "programCode": [
-                "026:023"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1167506,119 +1167484,118 @@
                     "mediaType": "application/x-gzip"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-844__26",
+            "issued": "2018-06-25",
+            "keyword": [
+                "turbulence",
+                "models",
+                "incompressible",
+                "flow",
+                "cases"
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-MECA-2-NIEDR-V1.0",
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
-                "phoenix",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Microscopy, Electrochemistry, and Conductivity Analyzer (MECA) experiment on the Mars Phoenix Lander consists of four instrument components plus command electronics. This MECA Non-Imaging EDR data set contains data from three of the four MECA components, the Thermal and Electrical Conductivity Probe (TECP), the Atomic Force Microscope (AFM), and the Wet Chemistry Laboratory (WCL). Data from the fourth MECA component, the Optical Microscope (OM), is in a separate data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-meca-2-niedr-v1.0_nzb5-t9k4",
+            "issued": "2018-06-26",
+            "keyword": [
+                "phoenix",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-MECA-2-NIEDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-meca-2-niedr-v1.0_nzb5-t9k4",
-            "description": "The Microscopy, Electrochemistry, and Conductivity Analyzer (MECA) experiment on the Mars Phoenix Lander consists of four instrument components plus command electronics. This MECA Non-Imaging EDR data set contains data from three of the four MECA components, the Thermal and Electrical Conductivity Probe (TECP), the Atomic Force Microscope (AFM), and the Wet Chemistry Laboratory (WCL). Data from the fourth MECA component, the Optical Microscope (OM), is in a separate data set.",
-            "title": "PHOENIX MARS MECA NON-IMAGING EDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "PHOENIX MARS MECA NON-IMAGING EDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-ER-4-MAP1%2FANGULAR-FLUX-V1.0",
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
+            "description": "This data set consists of calibrated, time-ordered, angle-resolved\nelectron flux data from the Electron Reflectometer (ER) instrument on\nthe Mars Global Surveyor (MGS) spacecraft.  The primary data consist of\ntime-series tables with descriptive headers.  The data set also includes\nancillary data (including geometry), documentation, and browse plots.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-er-4-map1-angular-flux-v1.0_nzby-5hks",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars global surveyor",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-ER-4-MAP1%2FANGULAR-FLUX-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-er-4-map1-angular-flux-v1.0_nzby-5hks",
-            "description": "This data set consists of calibrated, time-ordered, angle-resolved\nelectron flux data from the Electron Reflectometer (ER) instrument on\nthe Mars Global Surveyor (MGS) spacecraft.  The primary data consist of\ntime-series tables with descriptive headers.  The data set also includes\nancillary data (including geometry), documentation, and browse plots.",
-            "title": "MGS MARS/MOONS MAG/ER MAPPING ER ANGULAR FLUX V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MGS MARS/MOONS MAG/ER MAPPING ER ANGULAR FLUX V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://nasa3d.arc.nasa.gov/detail/mercury-suit",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://www.nasa.gov/mission_pages/mercury/index.html"
-            ],
-            "keyword": [
-                "3d model",
-                "astronaut",
-                "spacesuit",
-                "suit",
-                "mercury"
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
-            "identifier": "NASA-385",
             "description": "Mercury spacesuit. Polygons: 55366 Vertices: 55460",
-            "title": "NASA 3D Models: Mercury Spacesuit",
-            "programCode": [
-                "026:045",
-                "026:046"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1167626,98 +1167603,135 @@
                     "mediaType": "image/x-3ds"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-385",
+            "issued": "2018-06-25",
+            "keyword": [
+                "3d model",
+                "astronaut",
+                "spacesuit",
+                "suit",
+                "mercury"
+            ],
+            "landingPage": "http://nasa3d.arc.nasa.gov/detail/mercury-suit",
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
+                "http://www.nasa.gov/mission_pages/mercury/index.html"
+            ],
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "NASA 3D Models: Mercury Spacesuit"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SENTINEL-3B/OLCI/L2/ERR/IOP/2022",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SENTINEL-3B/OLCI/L2/ERR/IOP/2022.",
-            "issued": "2022-09-13",
-            "temporal": "2018-04-25T00:00:00Z/2024-04-22T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-13",
-            "keyword": [
-                "atmospheric radiation",
-                "ocean optics",
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
-            "identifier": "C2250852706-OB_DAAC",
             "description": "The Ocean and Land Colour Instrument (OLCI) is the successor to ENVISAT's Medium Resolution Imaging Spectrometer (MERIS) having additional spectral channels, different camera arrangements and simplified on-board processing. The OLCI is a push-broom instrument with five camera modules sharing the field of view. The field of view of the five cameras is arranged in a fan-shaped configuration in the vertical plane, perpendicular to the platform velocity. Each camera has an individual field of view of 14.2\u00b0 and a 0.6\u00b0 overlap with its neighbors. The whole field of view is shifted across track by 12.6\u00b0 away from the sun to minimize the impact of sun glint. OLCI is equipped with on-board calibration hardware based on sun diffusers. There are three sun diffusers--two 'white' diffusers dedicated to radiometric calibration and one dedicated to spectral calibration, with spectral reflectance features. The native resolution is approximately 300m, refered to as Full Resolution (FR). A Reduced Resolution (RR) processing mode provides Level-1B data at sampling rates decreased by a factor of four in both spatial dimensions resulting to resolution of approximately 1.2 km.",
-            "title": "Sentinel-3B OLCI Level-2 Earth-observation Reduced-Resolution (ERR) Inherent Optical Properties (IOP) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSENTINEL-3B%2FOLCI%2FL2%2FERR%2FIOP%2F2022",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSENTINEL-3B%2FOLCI%2FL2%2FERR%2FIOP%2F2022",
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
+            "identifier": "C2250852706-OB_DAAC",
+            "issued": "2022-09-13",
+            "keyword": [
+                "atmospheric radiation",
+                "ocean optics",
+                "earth science",
+                "oceans",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/SENTINEL-3B/OLCI/L2/ERR/IOP/2022",
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
+            "title": "Sentinel-3B OLCI Level-2 Earth-observation Reduced-Resolution (ERR) Inherent Optical Properties (IOP) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/nzj6-ynsw",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "These data were generated from mice that were skeletally unloaded using antiorthostatic suspension (AOS). Mice were either subjected to AOS or tail restraint without unloading for two weeks before injection with saline xc2 xb1tetanus toxoid xc2 xb1Cpg. Mice were unloaded for an additional two weeks before being sacrificed.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-201",
+                    "mediaType": "text/html",
+                    "title": "Impact of Antiorthostatic Suspension on Mouse response to Tetanus Toxoid and CpG"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-201_nzj6-ynsw",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "hindlimb unloading",
                 "animal treatmet",
@@ -1167729,726 +1167743,714 @@
                 "nucleic acid extraction",
                 "nucleic acid sequencing"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/nzj6-ynsw",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-201_nzj6-ynsw",
-            "description": "These data were generated from mice that were skeletally unloaded using antiorthostatic suspension (AOS). Mice were either subjected to AOS or tail restraint without unloading for two weeks before injection with saline xc2 xb1tetanus toxoid xc2 xb1Cpg. Mice were unloaded for an additional two weeks before being sacrificed.",
-            "title": "Impact of Antiorthostatic Suspension on Mouse response to Tetanus Toxoid and CpG",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-201",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Impact of Antiorthostatic Suspension on Mouse response to Tetanus Toxoid and CpG"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Impact of Antiorthostatic Suspension on Mouse response to Tetanus Toxoid and CpG"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4TB14TN",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Seirup, L., G. Yetman, and L. Razafindrazay. 2013-05-17. U.S. Census Grids (Summary File 1), 1990. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H4TB14TN. https://doi.org/10.7927/H4TB14TN.",
-            "issued": "2013-05-17",
-            "temporal": "1990-04-01T00:00:00Z/1990-04-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2013-05-17",
-            "references": [
-                "https://doi.org/10.7927/H4B85623",
-                "https://doi.org/10.7927/H40Z716C"
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
-            "identifier": "C1000000180-SEDAC",
-            "description": "The U.S. Census Grids (Summary File 1), 1990 data set contains grids of demographic and socioeconomic data from the year 1990 U.S. census in ASCII and geotiff formats. The grids have a resolution of 30 arc-seconds (0.0083 decimal degrees), or approximately 1 square km. The gridded variables are based on census block geography from Census 1990 TIGER/Line Files and census variables (population, households, and housing variables). This data set is produced by the Columbia University Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Seirup, L., G. Yetman, and L. Razafindrazay",
-            "title": "U.S. Census Grids (Summary File 1), 1990",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/usgrid/usgrid-summary-file1-1990/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The U.S. Census Grids (Summary File 1), 1990 data set contains grids of demographic and socioeconomic data from the year 1990 U.S. census in ASCII and geotiff formats. The grids have a resolution of 30 arc-seconds (0.0083 decimal degrees), or approximately 1 square km. The gridded variables are based on census block geography from Census 1990 TIGER/Line Files and census variables (population, households, and housing variables). This data set is produced by the Columbia University Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4TB14TN",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4TB14TN",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/usgrid/usgrid-summary-file1-1990/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/usgrid/usgrid-summary-file1-1990/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file1-1990/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file1-1990/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file1-1990/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file1-1990/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file1-1990",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file1-1990",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/usgrid/usgrid-summary-file1-1990/sedac-logo.jpg",
+            "identifier": "C1000000180-SEDAC",
+            "issued": "2013-05-17",
+            "keyword": [
+                "population",
+                "earth science",
+                "human dimensions"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4TB14TN",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2013-05-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H4B85623",
+                "https://doi.org/10.7927/H40Z716C"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 17.0 -65.0 72.0",
+            "temporal": "1990-04-01T00:00:00Z/1990-04-01T00:00:00Z",
             "theme": [
                 "USCG",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "U.S. Census Grids (Summary File 1), 1990"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1625796321-LARC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MISR Science Team (2006), Terra/MISR Level 2, TOA/Cloud Aerosol Product subset for the GoMACCS region, version 2, Hampton, VA, USA: NASA Atmospheric Science Data Center (ASDC), Accessed <author citing data inserts date here> at doi: TBD",
-            "issued": "2019-07-22",
-            "temporal": "2006-07-30T17:00:40.686Z/2006-10-16T17:15:34.106Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-07-22",
-            "keyword": [
-                "aerosols",
-                "atmosphere",
-                "earth science",
-                "air quality"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Earl Hansen",
                 "hasEmail": "mailto:earl.g.hansen@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1625796321-LARC",
             "description": "Multi-angle Imaging SpectroRadiometer (MISR) is an instrument designed to view Earth with cameras pointed in 9 different directions. As the instrument flies overhead, each piece of Earth's surface below is successively imaged by all 9 cameras, in each of 4 wavelengths (blue, green, red, and near-infrared). The goal of MISR is to improve our understanding of the fate of sunlight in Earth environment, as well as distinguish different types of clouds, particles and surfaces. Specifically, MISR monitors the monthly, seasonal, and long-term trends in three areas: 1) amount and type of atmospheric particles (aerosols), including those formed by natural sources and by human activities; 2) amounts, types, and heights of clouds, and 3) distribution of land surface cover, including vegetation canopy structure. MISR Level 2 TOA/Cloud Aerosol Product subset for the GoMACCS region V002 contains Aerosol optical depth and particle type, with associated atmospheric data.",
-            "title": "MISR Level 2 TOA/Cloud Aerosol Product subset for the GoMACCS region V002",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1625796321-LARC.html",
-                    "description": "View this dataset on the CMR (Common Metadata Repository)",
                     "@type": "dcat:Distribution",
+                    "description": "View this dataset on the CMR (Common Metadata Repository)",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1625796321-LARC.html",
+                    "mediaType": "text/html",
                     "title": "CMR"
                 }
             ],
+            "identifier": "C1625796321-LARC",
+            "issued": "2019-07-22",
+            "keyword": [
+                "aerosols",
+                "atmosphere",
+                "earth science",
+                "air quality"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1625796321-LARC.html",
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
+            "temporal": "2006-07-30T17:00:40.686Z/2006-10-16T17:15:34.106Z",
             "theme": [
                 "GOMACCS_2006",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR Level 2 TOA/Cloud Aerosol Product subset for the GoMACCS region V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/OLYMPEX/AMPR/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Lang, Timothy  and Anthony R Guillory.2017. GPM Ground Validation Advanced Microwave Precipitation Radiometer (AMPR) OLYMPEX [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/OLYMPEX/AMPR/DATA101",
-            "issued": "2017-10-20",
-            "temporal": "2015-11-09T18:48:53Z/2015-12-15T20:03:37Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "spectral/engineering",
-                "earth science",
-                "microwave"
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
-            "identifier": "C1979126614-GHRC_DAAC",
             "description": "The GPM Ground Validation Advanced Microwave Precipitation Radiometer (AMPR) OLYMPEX dataset was collected by the AMPR instrument flown on the high altitude ER-2 research aircraft from November 9 - December 15, 2015, during the Olympic Mountains Experiment (OLYMPEX) field campaign conducted at Washington State\u2019s Olympic Peninsula.  AMPR is an airborne passive microwave radiometer from which cloud, precipitation, water vapor, wind speed and wind direction can be obtained using advanced algorithms with the 10.7, 19.35, 37.1, and 85.5 GHz microwave frequency brightness temperatures measured by AMPR.  The primary goal of OLYMPEX was to validate rain and snow measurements in midlatitude frontal systems moving from ocean to coast to mountains.  AMPR data at the Global Hydrology Resource Center (GHRC) DAAC include netCDF format data files of brightness temperature and PNG browse files of Quality Control Flags and Brightness Temperatures.",
-            "graphic-preview-description": "Sample Browse Image",
-            "title": "GPM Ground Validation Advanced Microwave Precipitation Radiometer (AMPR) OLYMPEX V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/AMPR/browse/olympex_ampr_20151124_145455_tb.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FOLYMPEX%2FAMPR%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FOLYMPEX%2FAMPR%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmamprolyx",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmamprolyx",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/AMPR/browse/olympex_ampr_20151124_145455_tb.png",
-                    "description": "Sample Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample Browse Image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/AMPR/browse/olympex_ampr_20151124_145455_tb.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20150022943.pdf",
-                    "description": "AMPR and radar observations from IPHEx: Data quality control and product generation",
                     "@type": "dcat:Distribution",
+                    "description": "AMPR and radar observations from IPHEx: Data quality control and product generation",
+                    "downloadURL": "https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20150022943.pdf",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/AMPR/doc/gpmamprolyx_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/AMPR/doc/gpmamprolyx_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/JAS3606.1",
-                    "description": "Classification of Tropical Oceanic Precipitation using High-Altitude Aircraft Microwave and Electric Field Measurements",
                     "@type": "dcat:Distribution",
+                    "description": "Classification of Tropical Oceanic Precipitation using High-Altitude Aircraft Microwave and Electric Field Measurements",
+                    "downloadURL": "https://doi.org/10.1175/JAS3606.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/JAMC-D-14-0145.1",
-                    "description": "Signatures of Hydrometeor Species from Airborne Passive Microwave Data for Frequencies 10\u2013183 GHz",
                     "@type": "dcat:Distribution",
+                    "description": "Signatures of Hydrometeor Species from Airborne Passive Microwave Data for Frequencies 10\u2013183 GHz",
+                    "downloadURL": "https://doi.org/10.1175/JAMC-D-14-0145.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1109/36.981360",
-                    "description": "Influence of microphysical cloud parameterizations on microwave brightness temperatures  View Document",
                     "@type": "dcat:Distribution",
+                    "description": "Influence of microphysical cloud parameterizations on microwave brightness temperatures  View Document",
+                    "downloadURL": "https://doi.org/10.1109/36.981360",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/1520-0426(1994)011%3C0849:HRIORS%3E2.0.CO;2",
-                    "description": "High-Resolution Imaging of Rain Systems with the Advanced Microwave Precipitation Radiometer",
                     "@type": "dcat:Distribution",
+                    "description": "High-Resolution Imaging of Rain Systems with the Advanced Microwave Precipitation Radiometer",
+                    "downloadURL": "https://doi.org/10.1175/1520-0426(1994)011%3C0849:HRIORS%3E2.0.CO;2",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1109/36.239909",
-                    "description": "Comparisons of precipitation measurements by the Advanced Microwave Precipitation Radiometer and multiparameter radar",
                     "@type": "dcat:Distribution",
+                    "description": "Comparisons of precipitation measurements by the Advanced Microwave Precipitation Radiometer and multiparameter radar",
+                    "downloadURL": "https://doi.org/10.1109/36.239909",
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
+            "graphic-preview-description": "Sample Browse Image",
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/AMPR/browse/olympex_ampr_20151124_145455_tb.png",
+            "identifier": "C1979126614-GHRC_DAAC",
+            "issued": "2017-10-20",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "microwave"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/OLYMPEX/AMPR/DATA101",
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
             "spatial": "-130.947 33.7591 -117.287 50.0166",
+            "temporal": "2015-11-09T18:48:53Z/2015-12-15T20:03:37Z",
             "theme": [
                 "OLYMPEX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM Ground Validation Advanced Microwave Precipitation Radiometer (AMPR) OLYMPEX V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CRN0E7YPPFGY",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "High Mountain Asia 1 km 6-hourly Downscaled Meteorological Data 2003 to 2018 V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/CRN0E7YPPFGY.",
-            "issued": "2003-01-01",
-            "temporal": "2003-01-01T00:00:00Z/2018-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-12-31",
-            "keyword": [
-                "atmospheric pressure",
-                "earth science",
-                "atmospheric winds",
-                "atmospheric temperature",
-                "atmospheric radiation",
-                "atmosphere",
-                "atmospheric water vapor",
-                "precipitation"
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
-            "identifier": "C2091757248-NSIDC_ECS",
             "description": "This data set provides downscaled six-hourly atmospheric forcings from European Centre for Medium-Range Weather Forecasts (ECMWF) and Climate Hazards Group InfraRed Precipitation with Station data (CHIRPS) precipitation from 2003 to 2019 at a spatial resolution of ~1km across High Mountain Asia.",
-            "title": "High Mountain Asia 1 km 6-hourly Downscaled Meteorological Data 2003 to 2018 V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCRN0E7YPPFGY",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCRN0E7YPPFGY",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/HMA_DM_6H/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/HMA_DM_6H/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/HMA/HMA_DM_6H.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/HMA/HMA_DM_6H.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=HMA_DM_6H+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=HMA_DM_6H+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/HMA_DM_6H/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/HMA_DM_6H/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/HMA/HMA_DM_6H.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/HMA/HMA_DM_6H.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=HMA_DM_6H+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=HMA_DM_6H+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/CRN0E7YPPFGY",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/CRN0E7YPPFGY",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/CRN0E7YPPFGY",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/CRN0E7YPPFGY",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2091757248-NSIDC_ECS",
+            "issued": "2003-01-01",
+            "keyword": [
+                "atmospheric pressure",
+                "earth science",
+                "atmospheric winds",
+                "atmospheric temperature",
+                "atmospheric radiation",
+                "atmosphere",
+                "atmospheric water vapor",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.5067/CRN0E7YPPFGY",
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
             "spatial": "56.94 12.95 102.59 48.5",
+            "temporal": "2003-01-01T00:00:00Z/2018-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "High Mountain Asia 1 km 6-hourly Downscaled Meteorological Data 2003 to 2018 V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amer1_mtes_derived_temperature&version=1.0",
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
+            "description": "This bundle contains derived brightness temperature data from the Mini-TES instrument on Mars Exploration Rover 1 (Opportunity).",
+            "identifier": "urn:nasa:pds:mer1_mtes_derived_temperature",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amer1_mtes_derived_temperature&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:mer1_mtes_derived_temperature",
-            "description": "This bundle contains derived brightness temperature data from the Mini-TES instrument on Mars Exploration Rover 1 (Opportunity).",
-            "title": "MER1 Mini-TES Derived Brightness Temperature Data Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MER1 Mini-TES Derived Brightness Temperature Data Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/303/",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Vlad Popescu",
+                "hasEmail": "mailto:vmpopescu@gmail.com"
+            },
+            "description": "not available",
+            "identifier": "DASHLINK_303",
             "issued": "2011-02-07",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "nasa",
                 "dashlink",
                 "ames"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Vlad Popescu",
-                "hasEmail": "mailto:vmpopescu@gmail.com"
-            },
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/303/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Dashlink"
             },
-            "identifier": "DASHLINK_303",
-            "description": "not available",
-            "title": "Predicting Controller Communication Time for Capacity Estimation",
-            "programCode": [
-                "026:029"
-            ],
-            "accrualPeriodicity": "irregular"
+            "title": "Predicting Controller Communication Time for Capacity Estimation"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/dv72-s254",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hauer, M., and Center for International Earth Science Information Network - CIESIN - Columbia University. 2021-03-16. Georeferenced U.S. County-Level Population Projections, Total and by Sex, Race and Age, Based on the SSPs, 2020-2100. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/dv72-s254. https://doi.org/10.7927/dv72-s254.",
-            "issued": "2021-03-16",
-            "temporal": "2020-01-01T00:00:00Z/2100-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-03-16",
-            "references": [
-                "https:/doi.org/10.7927/escf-qp41"
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
-            "identifier": "C2039248970-SEDAC",
-            "description": "The Georeferenced U.S. County-Level Population Projections, Total and by Sex, Race and Age, Based on the SSPs, 2020-2100 consists of county-level population projection scenarios of total population, and by age, sex, and race in five-year intervals for all U.S. counties for the period 2020 - 2100. These data have numerous potential uses and can serve as inputs for addressing questions involving sub-national demographic change in the United States in the near, middle- and long-term.",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Hauer, M., and Center for International Earth Science Information Network - CIESIN - Columbia University",
-            "title": "Georeferenced U.S. County-Level Population Projections, Total and by Sex, Race and Age, Based on the SSPs, 2020-2100",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/popdynamics/popdynamics-us-county-level-pop-projections-sex-race-age-ssp-2020-2100/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Georeferenced U.S. County-Level Population Projections, Total and by Sex, Race and Age, Based on the SSPs, 2020-2100 consists of county-level population projection scenarios of total population, and by age, sex, and race in five-year intervals for all U.S. counties for the period 2020 - 2100. These data have numerous potential uses and can serve as inputs for addressing questions involving sub-national demographic change in the United States in the near, middle- and long-term.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2Fdv72-s254",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2Fdv72-s254",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/popdynamics/popdynamics-us-county-level-pop-projections-sex-race-age-ssp-2020-2100/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/popdynamics/popdynamics-us-county-level-pop-projections-sex-race-age-ssp-2020-2100/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/popdynamics-us-county-level-pop-projections-sex-race-age-ssp-2020-2100/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/popdynamics-us-county-level-pop-projections-sex-race-age-ssp-2020-2100/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/popdynamics-us-county-level-pop-projections-sex-race-age-ssp-2020-2100/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/popdynamics-us-county-level-pop-projections-sex-race-age-ssp-2020-2100/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/popdynamics-us-county-level-pop-projections-sex-race-age-ssp-2020-2100",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/popdynamics-us-county-level-pop-projections-sex-race-age-ssp-2020-2100",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/popdynamics/popdynamics-us-county-level-pop-projections-sex-race-age-ssp-2020-2100/sedac-logo.jpg",
+            "identifier": "C2039248970-SEDAC",
+            "issued": "2021-03-16",
+            "keyword": [
+                "population",
+                "human dimensions",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.7927/dv72-s254",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-03-16",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https:/doi.org/10.7927/escf-qp41"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 17.0 -65.0 72.0",
+            "temporal": "2020-01-01T00:00:00Z/2100-12-31T00:00:00Z",
             "theme": [
                 "POPDYNAMICS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Georeferenced U.S. County-Level Population Projections, Total and by Sex, Race and Age, Based on the SSPs, 2020-2100"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/86",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "McCreight, R.W., and R.H. Waring. 1994. SE-590 Low Altitude Reflectances (OTTER). ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/86",
-            "issued": "2023-11-19",
-            "temporal": "1990-08-13T00:00:00Z/1991-07-03T23:59:59Z",
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
-            "identifier": "C2804788870-ORNL_CLOUD",
             "description": "Low altitude (Ultralight) spectral reflectances of OTTER research sites measured by Spectron SE590 spectrophotometer",
-            "graphic-preview-description": "Browse Image",
-            "title": "SE-590 Low Altitude Reflectances (OTTER)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/otter_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F86",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F86",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/otter/spectra_se590_altitude/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/otter/spectra_se590_altitude/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/OTTER/guides/SE590_Low_Altitude_Reflectance_Data.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/OTTER/guides/SE590_Low_Altitude_Reflectance_Data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/86",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/86",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/otter/spectra_se590_altitude/comp/mccreigh.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/otter/spectra_se590_altitude/comp/mccreigh.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/otter/spectra_se590_altitude/comp/se590.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/otter/spectra_se590_altitude/comp/se590.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/otter/spectra_se590_altitude/comp/SE590_Low_Altitude_Reflectance_Data.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/otter/spectra_se590_altitude/comp/SE590_Low_Altitude_Reflectance_Data.pdf",
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
+            "identifier": "C2804788870-ORNL_CLOUD",
+            "issued": "2023-11-19",
+            "keyword": [
+                "earth science",
+                "atmospheric radiation",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/86",
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
+            "temporal": "1990-08-13T00:00:00Z/1991-07-03T23:59:59Z",
             "theme": [
                 "OTTER",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SE-590 Low Altitude Reflectances (OTTER)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/851/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-12-12",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "nasa",
-                "ames",
-                "dashlink"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Abhinav Saxena",
                 "hasEmail": "mailto:abhinav.saxena@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_851",
             "description": "In this paper, a probabilistic delamination location and size detection framework is proposed. The delamination probability image using Lamb wave-based damage detection is constructed using the Bayesian updating technique. First, the algorithm for the probabilistic delamination detection framework using Bayesian updating (Bayesian Imaging Method - BIM) is proposed. Following this, the composite coupon fatigue testing setup is introduced and the corresponding lamb wave diagnosis signal is collected and interpreted. Next, the obtained signal features are incorporated in the Bayesian Imaging Method to detect delamination size and location, as well as their confidence bounds. The damage detection results using the proposed methodology are compared with X-ray images for verification and validation. Finally, some conclusions and future works are drawn based on the proposed study.",
-            "title": "Probabilistic Delamination Diagnosis of Composite Materials Using a Novel Bayesian Imaging Method",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/download",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/STI_9457_Probabilistic_delamination_diagnosis_of_composite_materials_using_a_novel_Bayesian_Imaging_Method_final.pdf",
-                    "description": "STI_9457_Probabilistic delamination diagnosis of composite materials using a novel Bayesian Imaging Method_final.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "STI_9457_Probabilistic delamination diagnosis of composite materials using a novel Bayesian Imaging Method_final.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/STI_9457_Probabilistic_delamination_diagnosis_of_composite_materials_using_a_novel_Bayesian_Imaging_Method_final.pdf",
+                    "mediaType": "application/download",
                     "title": "STI_9457_Probabilistic delamination diagnosis of composite materials using a novel Bayesian Imaging Method_final.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_851",
+            "issued": "2013-12-12",
+            "keyword": [
+                "nasa",
+                "ames",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/851/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Probabilistic Delamination Diagnosis of Composite Materials Using a Novel Bayesian Imaging Method"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-POS-6-SC-TRAJ-MOON-COORDS-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Galileo trajectory data in moon (Amalthea, Io, Europa, Ganymede, Callisto) centered coordinates for all of the near satellite encounters. Ephemeris data are provided every two seconds for approximately one hour about closest approach.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-pos-6-sc-traj-moon-coords-v1.0_nzup-t88i",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "ganymede",
                 "amalthea",
@@ -1168459,791 +1168461,767 @@
                 "io plasma torus",
                 "jupiter"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-POS-6-SC-TRAJ-MOON-COORDS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-pos-6-sc-traj-moon-coords-v1.0_nzup-t88i",
-            "description": "This data set contains Galileo trajectory data in moon (Amalthea, Io, Europa, Ganymede, Callisto) centered coordinates for all of the near satellite encounters. Ephemeris data are provided every two seconds for approximately one hour about closest approach.",
-            "title": "GO JUP POS GLL TRAJECTORY MOON CENTERED COORDS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GO JUP POS GLL TRAJECTORY MOON CENTERED COORDS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-RAC-5-MOSAIC-OPS-V1.0",
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
+            "description": "The Robotic Arm Camera (RAC)  experiment on the Mars Phoenix Lander consists of one instrument  component plus command electronics. This RAC Imaging Operations RDR  data set contains mosaic data from the Robotic Arm Camera (RAC).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-rac-5-mosaic-ops-v1.0_nzwq-5f3g",
+            "issued": "2021-05-21",
+            "keyword": [
+                "phoenix",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-RAC-5-MOSAIC-OPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-rac-5-mosaic-ops-v1.0_nzwq-5f3g",
-            "description": "The Robotic Arm Camera (RAC)  experiment on the Mars Phoenix Lander consists of one instrument  component plus command electronics. This RAC Imaging Operations RDR  data set contains mosaic data from the Robotic Arm Camera (RAC).",
-            "title": "PHOENIX MARS ROBOTIC ARM CAMERA  \n                                     5 MOSAIC OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "PHOENIX MARS ROBOTIC ARM CAMERA  \n                                     5 MOSAIC OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/385",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Bourbonniere, R.A. 1998. BOREAS TGB-05 Dissolved Organic Carbon Data from NSA Beaver Ponds. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/385",
-            "issued": "2023-11-22",
-            "temporal": "1994-04-22T00:00:00Z/1994-09-19T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-28",
-            "keyword": [
-                "earth science",
-                "water quality/water chemistry",
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
-            "identifier": "C2808131800-ORNL_CLOUD",
             "description": "Contains the TGB-05 dissolved organic carbon data for the Northern Study Area beaver pond site.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS TGB-05 Dissolved Organic Carbon Data from NSA Beaver Ponds",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F385",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F385",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TGB/tgb5docd/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TGB/tgb5docd/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TGB05_DissOrgC.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TGB05_DissOrgC.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/385",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/385",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb5docd/comp/TGB05_DissOrgC.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb5docd/comp/TGB05_DissOrgC.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb5docd/comp/TGB05_DissOrgC.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb5docd/comp/TGB05_DissOrgC.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb5docd/comp/TGB05_DissOrgC.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb5docd/comp/TGB05_DissOrgC.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb5docd/comp/tgb5docd.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb5docd/comp/tgb5docd.def",
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
+            "identifier": "C2808131800-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "earth science",
+                "water quality/water chemistry",
+                "terrestrial hydrosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/385",
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
+            "temporal": "1994-04-22T00:00:00Z/1994-09-19T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS TGB-05 Dissolved Organic Carbon Data from NSA Beaver Ponds"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/420",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Aber, J.D., M.E. Martin, and C. Wessman. 1999. Calculated Leaf Carbon and Nitrogen, 1992 (ACCP). ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/420",
-            "issued": "2023-10-02",
-            "temporal": "1992-06-18T00:00:00Z/1992-09-01T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-03",
-            "keyword": [
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
-            "identifier": "C2776829507-ORNL_CLOUD",
             "description": "Study plot canopy chemistry values were calculated from leaf chemistry and litterfall weight values. Average leaf concentrations of nitrogen and carbon were used to investigate how reflectance varies with chemistry.",
-            "graphic-preview-description": "Browse Image",
-            "title": "Calculated Leaf Carbon and Nitrogen, 1992 (ACCP)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/accp_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F420",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F420",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/accp/plotchem/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/accp/plotchem/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ACCP/guides/plotchem.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ACCP/guides/plotchem.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/420",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/420",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/accp/plotchem/comp/plotchem.pdf",
-                    "description": "guide.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "guide.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/accp/plotchem/comp/plotchem.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/accp_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/accp_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/accp_logo_square.png",
+            "identifier": "C2776829507-ORNL_CLOUD",
+            "issued": "2023-10-02",
+            "keyword": [
+                "biosphere",
+                "vegetation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/420",
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
             "spatial": "-89.76 42.49 -68.74 45.22",
+            "temporal": "1992-06-18T00:00:00Z/1992-09-01T23:59:59Z",
             "theme": [
                 "ACCP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Calculated Leaf Carbon and Nitrogen, 1992 (ACCP)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/2YCD3NSNDMRM",
             "citation": "GES DISC Northern Eurasian Earth Science Partnership Initiative Project. 2001-01-01. MYD11CM1D. Version 005. MODIS/Aqua Monthly mean Day-Time Land Surface Temperature at 1x1 degree V005. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/2YCD3NSNDMRM. https://disc.gsfc.nasa.gov/datacollection/MYD11CM1D_005.html. Digital Science Data.",
-            "issued": "2009-03-10",
-            "temporal": "2002-08-01T00:00:00Z/2015-06-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-06-30",
-            "keyword": [
-                "earth science",
-                "surface thermal properties",
-                "ngda",
-                "national geospatial data asset",
-                "land surface"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "PETER ROMANOV, PHD",
                 "hasEmail": "mailto:Peter.Romanov@noaa.gov"
             },
+            "creator": "GES DISC Northern Eurasian Earth Science Partnership Initiative Project",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1239898022-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The dataset contains global monthly day-time land surface temperature averaged within 1 by 1 degree grid cells. The source for the data is MODIS/Aqua MYD11C3 Collection 005 product (MODIS/Aqua Monthly mean land surface temperature at 0.05 degree spatial resolution). The dataset covers the time period from 2002-08-01 to 2015-06-30.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "MYD11CM1D",
-            "creator": "GES DISC Northern Eurasian Earth Science Partnership Initiative Project",
-            "title": "MODIS/Aqua Monthly mean Day-Time Land Surface Temperature at 1x1 degree V005 (MYD11CM1D) at GES DISC",
-            "graphic-preview-description": "Sample image of MODIS-Aqua global monthly daytime land surface temperature at 1x1 degree, July 2010",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/MYD11CM1D_005.gif",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F2YCD3NSNDMRM",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F2YCD3NSNDMRM",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/MYD11CM1D_005.gif",
-                    "description": "Sample image of MODIS-Aqua global monthly daytime land surface temperature at 1x1 degree, July 2010",
                     "@type": "dcat:Distribution",
+                    "description": "Sample image of MODIS-Aqua global monthly daytime land surface temperature at 1x1 degree, July 2010",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/MYD11CM1D_005.gif",
+                    "mediaType": "image/gif",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/MYD11CM1D_005.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/MYD11CM1D_005.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://reason.gesdisc.eosdis.nasa.gov/data/Land_Surface_Temperature/MYD11CM1D.005/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://reason.gesdisc.eosdis.nasa.gov/data/Land_Surface_Temperature/MYD11CM1D.005/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://reason.gesdisc.eosdis.nasa.gov/data/Land_Surface_Temperature/MYD11CM1D.005/doc/README.MODIS_LST_1deg.005.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://reason.gesdisc.eosdis.nasa.gov/data/Land_Surface_Temperature/MYD11CM1D.005/doc/README.MODIS_LST_1deg.005.pdf",
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
+            "graphic-preview-description": "Sample image of MODIS-Aqua global monthly daytime land surface temperature at 1x1 degree, July 2010",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/MYD11CM1D_005.gif",
+            "identifier": "C1239898022-GES_DISC",
+            "issued": "2009-03-10",
+            "keyword": [
+                "earth science",
+                "surface thermal properties",
+                "ngda",
+                "national geospatial data asset",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/2YCD3NSNDMRM",
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
+            "series-name": "MYD11CM1D",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-08-01T00:00:00Z/2015-06-30T23:59:59.999Z",
             "theme": [
                 "NEESPI NASA",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Aqua Monthly mean Day-Time Land Surface Temperature at 1x1 degree V005 (MYD11CM1D) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/DCODSYU2N0CW",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMEX04 Leaf Area Index Data: Arizona, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/DCODSYU2N0CW.",
-            "issued": "2004-07-29",
-            "temporal": "2004-07-29T00:00:00Z/2004-08-25T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2004-08-25",
-            "keyword": [
-                "vegetation",
-                "biosphere",
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
-            "identifier": "C1386205086-NSIDCV0",
             "description": "Notice to Data Users: The documentation for this data set was provided solely by the Principal Investigator(s) and was not further developed, thoroughly reviewed, or edited by NSIDC. Thus, support for this data set may be limited.\n\nThis data set is comprised of in situ Leaf Area Index (LAI) data collected as part of the Soil Moisture Experiment 2004 (SMEX04) in the SMEX04 North American study area of southern Arizona, USA.",
-            "title": "SMEX04 Leaf Area Index Data: Arizona, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FDCODSYU2N0CW",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FDCODSYU2N0CW",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX04/Arizona/vegetation/LAI/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX04/Arizona/vegetation/LAI/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX04/Arizona/vegetation/LAI/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX04/Arizona/vegetation/LAI/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/DCODSYU2N0CW",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/DCODSYU2N0CW",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/DCODSYU2N0CW",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/DCODSYU2N0CW",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386205086-NSIDCV0",
+            "issued": "2004-07-29",
+            "keyword": [
+                "vegetation",
+                "biosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/DCODSYU2N0CW",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2004-08-25",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-110.3 31.4 -109.7 32.0",
+            "temporal": "2004-07-29T00:00:00Z/2004-08-25T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMEX04 Leaf Area Index Data: Arizona, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/HIM08/CERES/GEO_ED4_NH_V01.2",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2018-07-19. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/HIM08/CERES/GEO_ED4_NH_V01.2.",
-            "issued": "2018-05-22",
-            "temporal": "2015-07-06T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-19",
-            "keyword": [
-                "clouds",
-                "earth science",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1584977037-LARC_ASDC",
             "description": "CER_GEO_Ed4_HIM08_NH_V01.2 is the Satellite ClOud and Radiation Property retrieval System (SatCORPS) Clouds and the Earth's Radiant Energy System (CERES) Geostationary Satellite (GEO) Edition 4 Himawari-8 over the Northern Hemisphere (NH) Version 1.2 data product. Data was collected using the Advanced Himawari Imager (AHI) Instrument on the Himawari-8 platform. Data collection for this product is in progress. \r\n\r\nNote : Version 1.2 is identical to version 1.0 . No changes have been made to the retrieval algorithm.\r\n\r\nThis data set is comprised of cloud micro-physical and radiation properties derived hourly from GOES-11 geostationary satellite imager data using the Langley Research Center (LaRC) SATCORPS algorithms in support of the CERES project. The cloud micro-physical and radiation properties from each active geostationary satellite are merged together to create hourly global cloud properties that are used to estimate fluxes between CERES instrument measurements to account for the changing diurnal cycle. The data set is arranged as files for each hour and in netCDF-4 format. The observations are at 4-km resolution (at nadir) and are sub-sampled to 8 km.\r\n\r\nCERES is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions are a follow-on to the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument, protoflight model (PFM), was launched on November 27, 1997 as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the Earth Observing System (EOS) flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board Earth Observing System (EOS) Aqua on May 4, 2002. The CERES FM5 instrument was launched on board the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The newest CERES instrument (FM6) was launched on board the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite, now called NOAA-20, on November 18, 2017.",
-            "title": "SatCORPS CERES GEO Edition 4 Himawari-8 Northern Hemisphere Version 1.2",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FHIM08%2FCERES%2FGEO_ED4_NH_V01.2",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FHIM08%2FCERES%2FGEO_ED4_NH_V01.2",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1584977037-LARC_ASDC",
-                    "description": "Earthdata Search for CER_GEO_Ed4_HIM08_NH_V01.2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CER_GEO_Ed4_HIM08_NH_V01.2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1584977037-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/HIM08/CERES/GEO_ED4_NH_V01.2",
-                    "description": "DOI data set landing page for CER_GEO_Ed4_HIM08_NH_V01.2",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CER_GEO_Ed4_HIM08_NH_V01.2",
+                    "downloadURL": "https://doi.org/10.5067/HIM08/CERES/GEO_ED4_NH_V01.2",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/GEO/Edition4/HIM08_NH_V01.2/",
-                    "description": "ASDC Direct Data Download for CER_GEO_Ed4_HIM08_NH_V01.2",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CER_GEO_Ed4_HIM08_NH_V01.2",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/GEO/Edition4/HIM08_NH_V01.2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/GEO/Edition4/HIM08_NH_V01.2/contents.html",
-                    "description": "OPeNDAP data access for CER_GEO_Ed4_HIM08_NH_V01.2",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CER_GEO_Ed4_HIM08_NH_V01.2",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/GEO/Edition4/HIM08_NH_V01.2/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1584977037-LARC_ASDC",
+            "issued": "2018-05-22",
+            "keyword": [
+                "clouds",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/HIM08/CERES/GEO_ED4_NH_V01.2",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-07-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>0.0 80.0 0.0 180.0 60.0 180.0 60.0 80.0 0.0 80.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2015-07-06T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "CERES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SatCORPS CERES GEO Edition 4 Himawari-8 Northern Hemisphere Version 1.2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SUOMI-NPP/VIIRS/L3B/PAR/2022",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SUOMI-NPP/VIIRS/L3B/PAR/2022.",
-            "issued": "2022-09-14",
-            "temporal": "2012-01-02T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-14",
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
-            "identifier": "C2340494035-OB_DAAC",
             "description": "The Visible and Infrared Imager/Radiometer Suite (VIIRS) is a multi-disciplinary instrument that is being flown on the Joint Polar Satellite System (JPSS) series of spacecraft, including the Suomi National Polar-orbiting Partnership (S-NPP) that launched in October 2011.  JPSS is a multi-platform, multi-agency program that consolidates the polar orbiting spacecraft of NASA and the National Oceanic and Atmospheric Administration (NOAA).  S-NPP is the initial spacecraft in this series, and VIIRS is the successor to MODIS for Earth science data product generation.  VIIRS has 22 spectral bands ranging from 412 nm to 12 nm.  There are 16 moderate-resolution bands (750m at nadir), 5 image-resolution bands (375m), and one day-night band (DNB).",
-            "title": "Suomi-NPP VIIRS Global Binned Photosynthetically Active Radiation (PAR) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSUOMI-NPP%2FVIIRS%2FL3B%2FPAR%2F2022",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSUOMI-NPP%2FVIIRS%2FL3B%2FPAR%2F2022",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/SUOMI-NPP/VIIRS/L3B/PAR/2022",
-                    "description": "VIIRS-Suomi-NPP L3B Photosynthetically Active Radiation (PAR) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS-Suomi-NPP L3B Photosynthetically Active Radiation (PAR) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/SUOMI-NPP/VIIRS/L3B/PAR/2022",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2340494035-OB_DAAC",
+            "issued": "2022-09-14",
+            "keyword": [
+                "ocean optics",
+                "earth science",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/SUOMI-NPP/VIIRS/L3B/PAR/2022",
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
+            "title": "Suomi-NPP VIIRS Global Binned Photosynthetically Active Radiation (PAR) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-2-ESC3-MTP019-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This dataset contains ROSETTA NAVCAM RAW DATA of the Escort Phase 3 from 28th July 2015 to 25th Aug 2015 when at the vicinity of target 67P/CG.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-2-esc3-mtp019-v1.0_p27j-k2uy",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "zeta cas",
                 "international rosetta mission",
                 "alpha lyr"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-2-ESC3-MTP019-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-2-esc3-mtp019-v1.0_p27j-k2uy",
-            "description": "This dataset contains ROSETTA NAVCAM RAW DATA of the Escort Phase 3 from 28th July 2015 to 25th Aug 2015 when at the vicinity of target 67P/CG.",
-            "title": "ROSETTA-ORBITER 67P NAVCAM 2 COMET ESCORT 3 MTP019 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P NAVCAM 2 COMET ESCORT 3 MTP019 V1.0"
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
-                "turbulence",
-                "flow",
-                "incompressible",
-                "cases"
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
-            "identifier": "NASA-842__24",
             "description": "This grouping contains the incompressible-flow cases from the 1980-81 Data Library.",
-            "title": "Collaborative Testing of Turbulence Models: Incompressible Flow Cases from 1980-81 Data Library",
-            "programCode": [
-                "026:023"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1169251,50 +1169229,51 @@
                     "mediaType": "application/txt"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-842__24",
+            "issued": "2018-06-25",
+            "keyword": [
+                "models",
+                "turbulence",
+                "flow",
+                "incompressible",
+                "cases"
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
-            "landingPage": "https://doi.org/10.5067/GNSS/GDGPS_daily_acc_POD_1sec_clk_corr_gal_001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, CDDIS. https://doi.org/10.5067/GNSS/GDGPS_daily_acc_POD_1sec_clk_corr_gal_001\r\n.",
-            "issued": "1992-01-01",
-            "temporal": "2023-10-01T00:00:00Z/2024-11-18T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-15",
-            "keyword": [
-                "earth science",
-                "geodetics",
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
-                "name": "CDDIS"
-            },
-            "identifier": "C2781531557-CDDIS",
             "description": "This product contains a time series of clock biases for healthy satellites in the Galileo constellation that are accumulated every minute throughout the day. In addition, formal 1-sigma uncertainties for the corrections are provided. The product is generated at JPL's Global Differential GPS Operations Centers in real-time. The data in this product can be concatenated with other daily products to provide larger coverage in time.",
-            "title": "Ground-Based Global Navigation Satellite System (GNSS) Guardian Galileo daily accumulated real-time POD Clock Corrections (1-second sampling, 24-hour files) from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGDGPS_daily_acc_POD_1sec_clk_corr_gal_001%0D%0A",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGDGPS_daily_acc_POD_1sec_clk_corr_gal_001%0D%0A",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1169310,64 +1169289,87 @@
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2781531557-CDDIS",
+            "issued": "1992-01-01",
+            "keyword": [
+                "earth science",
+                "geodetics",
+                "gravity/gravitational field",
+                "tectonics",
+                "solid earth"
+            ],
+            "landingPage": "https://doi.org/10.5067/GNSS/GDGPS_daily_acc_POD_1sec_clk_corr_gal_001",
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
+            "title": "Ground-Based Global Navigation Satellite System (GNSS) Guardian Galileo daily accumulated real-time POD Clock Corrections (1-second sampling, 24-hour files) from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-5-EDP1-V1.0",
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
+            "description": "This data set contains the complete collection of the published Cassini radio occultation electron density profiles of the Titan ionosphere as of September 2008.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-5-edp1-v1.0_p29t-9jgv",
+            "issued": "2021-05-21",
+            "keyword": [
+                "cassini-huygens",
+                "titan"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-5-EDP1-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-5-edp1-v1.0_p29t-9jgv",
-            "description": "This data set contains the complete collection of the published Cassini radio occultation electron density profiles of the Titan ionosphere as of September 2008.",
-            "title": "CASSINI RSS: IONOSPHERIC ELECTRON DENSITY PROFILES EDP1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI RSS: IONOSPHERIC ELECTRON DENSITY PROFILES EDP1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-EPD-2-REDR-RTS-SCAN-AVG-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains 11 min resolution RTS 16 sector rate, pitch, and phase data for all Jupiter orbits.  There are a total of 18 tabulated data files that contain A1, A2, A3, A4, A5, E1, F2, TP1, TP2, TA1, TO1, TO2, TO3, TS1, TS2, Start, Pitch, and Phase 16 sector data.  The rates reported are in units of (counts/sec), pitch and phase angles are in (radians).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-epd-2-redr-rts-scan-avg-v1.0_p2bn-gs6m",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "jupiter",
                 "amalthea",
@@ -1169378,270 +1169380,249 @@
                 "io",
                 "io plasma torus"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-EPD-2-REDR-RTS-SCAN-AVG-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-epd-2-redr-rts-scan-avg-v1.0_p2bn-gs6m",
-            "description": "This data set contains 11 min resolution RTS 16 sector rate, pitch, and phase data for all Jupiter orbits.  There are a total of 18 tabulated data files that contain A1, A2, A3, A4, A5, E1, F2, TP1, TP2, TA1, TO1, TO2, TO3, TS1, TS2, Start, Pitch, and Phase 16 sector data.  The rates reported are in units of (counts/sec), pitch and phase angles are in (radians).",
-            "title": "GO JUP EPD REFORMATTED REAL TIME SCAN AVERAGED V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GO JUP EPD REFORMATTED REAL TIME SCAN AVERAGED V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/XL382B4YZJP5",
             "citation": "Kevin W. Bowman. 2021-05-27. TRPSDL2TATMCRSFS. Version 1. TROPESS CrIS-SNPP L2 Atmospheric Temperature for Forward Stream, Standard Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/XL382B4YZJP5. https://disc.gsfc.nasa.gov/datacollection/TRPSDL2TATMCRSFS_1.html. Digital Science Data.",
-            "issued": "2021-04-29",
-            "temporal": "2021-02-01T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-04-29",
-            "references": [
-                "https://doi.org/10.1126/sciadv.abf7460",
-                "https://doi.org/10.1109/TGRS.2006.871234",
-                "https://doi.org/10.1029/2002JD002299",
-                "https://doi.org/10.1029/2004JD004522",
-                "https://doi.org/10.5194/amt-5-397-2012"
-            ],
-            "keyword": [
-                "earth science",
-                "atmospheric temperature",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "KEVIN BOWMAN",
                 "hasEmail": "mailto:kevin.w.bowman@jpl.nasa.gov"
             },
+            "creator": "Kevin W. Bowman",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2041968764-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS CrIS-SNPP L2 Atmospheric Temperature for Forward Stream, Standard Product contains the vertical distribution of the retrieved atmospheric state of atmospheric temperature (TATM), formal uncertainties, and diagnostic information measured by the CrIS instrument on the Suomi-NPP satellite. The forward stream standard product is global for the time period from 2021-02-01 to 2021-05-21, when the CrIS-SNPP processing was discontinued. The NASA TRopospheric Ozone and Precursors from Earth System Sounding (TROPESS) project, uses an optimal estimation algorithm, known as the MUlti-SpEctra, MUlti-SpEcies, Multi-SEnsors (MUSES).\n\nThe data files are written in the netCDF version 4 file format, and each file contains one day of data. The data have a spatial resolution of 14 km (CrIS nadir FOV), and are reported at 31 vertical levels from the surface to 0.1 hPa. The principal investigator for the TROPESS project is Kevin W. Bowman.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSDL2TATMCRSFS",
-            "creator": "Kevin W. Bowman",
-            "graphic-preview-description": "TROPESS CrIS-SNPP Atmospheric Temperature (Forward Stream, Standard Product) at 348 hPa on 01 April 2021.",
-            "title": "TROPESS CrIS-SNPP L2 Atmospheric Temperature for Forward Stream, Standard Product V1 (TRPSDL2TATMCRSFS) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2TATMCRSFS_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FXL382B4YZJP5",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FXL382B4YZJP5",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2TATMCRSFS_Sample.png",
-                    "description": "TROPESS CrIS-SNPP Atmospheric Temperature (Forward Stream, Standard Product) at 348 hPa on 01 April 2021.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS CrIS-SNPP Atmospheric Temperature (Forward Stream, Standard Product) at 348 hPa on 01 April 2021.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2TATMCRSFS_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2TATMCRSFS_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2TATMCRSFS_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2TATMCRSFS.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2TATMCRSFS.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2TATMCRSFS_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2TATMCRSFS_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Standard/TRPSDL2TATMCRSFS.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Standard/TRPSDL2TATMCRSFS.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2TATMCRSFS.1/doc/TROPESS_Forward_Stream_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2TATMCRSFS.1/doc/TROPESS_Forward_Stream_README.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/User_Guides/TROPESS-AIRS-CrIS_TATM_L2_Product_User_Guide_v1_20210202.pdf",
-                    "description": "User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "User's Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/User_Guides/TROPESS-AIRS-CrIS_TATM_L2_Product_User_Guide_v1_20210202.pdf",
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
+            "graphic-preview-description": "TROPESS CrIS-SNPP Atmospheric Temperature (Forward Stream, Standard Product) at 348 hPa on 01 April 2021.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2TATMCRSFS_Sample.png",
+            "identifier": "C2041968764-GES_DISC",
+            "issued": "2021-04-29",
+            "keyword": [
+                "earth science",
+                "atmospheric temperature",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/XL382B4YZJP5",
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
+            "references": [
+                "https://doi.org/10.1126/sciadv.abf7460",
+                "https://doi.org/10.1109/TGRS.2006.871234",
+                "https://doi.org/10.1029/2002JD002299",
+                "https://doi.org/10.1029/2004JD004522",
+                "https://doi.org/10.5194/amt-5-397-2012"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "TRPSDL2TATMCRSFS",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2021-02-01T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS CrIS-SNPP L2 Atmospheric Temperature for Forward Stream, Standard Product V1 (TRPSDL2TATMCRSFS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/907",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Lu, L., A.S. Denning, M.A. da Silva-Dias, P. Silva-Dias, S.R. Freitas, and S.S. Saatchi. 2008. LBA-ECO CD-01 Simulated Atmospheric Circulation, CO2 Variation, Tapajos: August 2001. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/907",
-            "issued": "2023-10-03",
-            "temporal": "2001-08-01T00:00:00Z/2001-08-16T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-03",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric chemistry",
-                "atmospheric winds"
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
-            "identifier": "C2776919988-ORNL_CLOUD",
             "description": "This data set consists of a single NetCDF file containing simulated three dimensional winds and CO2 concentrations centered on the Tapajos National Forest in Brazil in August 2001. Winds (u, v, and w  components) and CO2 concentrations were generated at 31 vertical levels at 1 km grid increment with the Brazilian version of Colorado State University (CSU) Regional Atmospheric Modeling System (RAMS). The simulation ran from the 1st through the 15th of August 2001, which was concurrent with the Santarem Mesoscale Campaign. The data file is in NetCDF format.Mesoscale circulations and atmospheric CO2 variations were investigated over a heterogeneous landscape of forests, pastures, and large rivers during the Santarem Mesoscale Campaign (SMC) of August 2001 (Silva Dias et al., 2004). The atmospheric CO2 concentration variations were simulated using the Colorado State University Regional Atmospheric Modeling System with four nested grids that included a 1-km finest grid centered on the Tapajos National Forest. Surface CO2 fluxes were prescribed using idealized diurnal cycles over forest and pasture that derived from flux tower observations; while surface water CO2 efflux was prescribed using a value suggested by in situ measurements in the Amazon region (Lu et al., 2005). Simulation ran from 1 August through 15 August 2001, which was concurrent with the SMC. Evaluation against flux tower observations and Belterra meteorological tower measurements showed that the model captured the observed 2-m temperatures and 10-m winds reasonably well. At 57 m the model reproduced the daytime CO2 concentration better than the nighttime concentration but missed the observed early morning CO2 maxima, in part because of the difficulties of simulating stable nocturnal boundary conditions and subgrid-scale intra-canopy processes. The results also suggested that the topography, the differences in roughness length between water and land, the shape juxtaposition of Amazon and Tapajos Rivers, and the resulting horizontal and vertical wind shears all facilitated the generation of local mesoscale circulations. Possible mechanisms producing a low-level convergence (LLC) line near the east bank of the Tapajos River were explored. Under strong trade wind conditions, mechanical forcing is more important than thermal forcing in LLC formation. Persistent clouds near the east side of the Tapajos River may have a significant impact on observed ecosystem carbon flux and should be taken into account if tower fluxes are to be generalized to a larger region.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO CD-01 Simulated Atmospheric Circulation, CO2 Variation, Tapajos: August 2001",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F907",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F907",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/carbon_dynamics/CD01_BRAMS/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/carbon_dynamics/CD01_BRAMS/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/CD01_BRAMS.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/CD01_BRAMS.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/907",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/907",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_BRAMS/comp/CD01_BRAMS.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_BRAMS/comp/CD01_BRAMS.pdf",
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
+            "identifier": "C2776919988-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry",
+                "atmospheric winds"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/907",
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
             "spatial": "-55.42 -3.07 -54.56 -2.2",
+            "temporal": "2001-08-01T00:00:00Z/2001-08-16T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO CD-01 Simulated Atmospheric Circulation, CO2 Variation, Tapajos: August 2001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://human-factors.arc.nasa.gov/SLAB/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2015-01-07",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "slab",
-                "spatial hearing",
-                "acoustic",
-                "api",
-                "render"
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
-            "identifier": "OCIO-Fitara-139",
             "description": "SLAB is a software-based, real-time virtual acoustic environment rendering system being developed as a tool for the study of spatial hearing. SLAB is designed to work in the personal computer environment to take advantage of the low-cost PC platform while providing a flexible, maintainable, and extensible architecture to enable the quick development of experiments. The software provides an API (Application Programming Interface) for specifying the acoustic scene as well as an extensible architecture for exploring multiple rendering strategies.",
-            "title": "ARC Code TI: SLAB Spatial Audio Renderer",
-            "programCode": [
-                "026:046"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1169649,130 +1169630,123 @@
                     "mediaType": "application/octet-stream"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "OCIO-Fitara-139",
+            "issued": "2015-01-07",
+            "keyword": [
+                "slab",
+                "spatial hearing",
+                "acoustic",
+                "api",
+                "render"
+            ],
+            "landingPage": "http://human-factors.arc.nasa.gov/SLAB/",
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
+            "title": "ARC Code TI: SLAB Spatial Audio Renderer"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-MOLA-5-IEGDR-L3-V2.0",
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
+            "description": "The Mars Global Surveyor spacecraft included a laser altimeter instrument. The primary objective of the Mars Orbiter Laser Altimeter (MOLA) is to determine globally the topography of Mars at a level suitable for addressing problems in geology and geophysics.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-mola-5-iegdr-l3-v2.0_p2if-dkkz",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "mars global surveyor"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-MOLA-5-IEGDR-L3-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-mola-5-iegdr-l3-v2.0_p2if-dkkz",
-            "description": "The Mars Global Surveyor spacecraft included a laser altimeter instrument. The primary objective of the Mars Orbiter Laser Altimeter (MOLA) is to determine globally the topography of Mars at a level suitable for addressing problems in geology and geophysics.",
-            "title": "MOLA INITIAL EXPERIMENT GRIDDED DATA RECORD",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MOLA INITIAL EXPERIMENT GRIDDED DATA RECORD"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0201-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-12T16:41:55.000 to 2014-08-12T19:15:19.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0201-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0201-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0201-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-12T16:41:55.000 to 2014-08-12T19:15:19.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0201 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0201 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SENTINEL5P/S5P_L1B_RA_BD4.1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Copernicus Sentinel data processed by ESA, Koninklijk Nederlands Meteorologisch Instituut (KNMI). 2018-08-23. S5P_L1B_RA_BD4. Version 1. Sentinel-5P TROPOMI L1B Radiance product band 4 (UVIS detector). Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/SENTINEL5P/S5P_L1B_RA_BD4.1. https://disc.gsfc.nasa.gov/datacollection/S5P_L1B_RA_BD4_1.html. Digital Science Data.",
-            "issued": "2014-12-09",
-            "temporal": "2018-04-30T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2014-12-09",
-            "keyword": [
-                "atmosphere",
-                "atmospheric radiation",
-                "earth science",
-                "platform characteristics",
-                "sensor characteristics",
-                "ultraviolet wavelengths",
-                "spectral/engineering"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Quintus Kleipool",
                 "hasEmail": "mailto:quintus.kleipool@knmi.nl"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1442068499-GES_DISC",
-            "description": "Starting from August 6th in 2019, Sentinel-5P TROPOMI along-track high spatial resolution (~5.5km at nadir) has been implemented.\nFor data after August 6th of 2019, please check S5P_L1B_RA_BD4 data collection.\n\nThe Copernicus Sentinel-5 Precursor (Sentinel-5P or S5P) satellite mission is one of the European Space Agency's (ESA) new mission family - Sentinels, and it is a joint initiative between the Kingdom of the Netherlands and the ESA. The sole payload on Sentinel-5P is the TROPOspheric Monitoring Instrument (TROPOMI), which is a nadir-viewing 108 degree Field-of-View push-broom grating hyperspectral spectrometer, covering the wavelength of ultraviolet-visible (UV-VIS, 270nm to 495nm), near infrared (NIR, 675nm to 775nm), and shortwave infrared (SWIR, 2305nm-2385nm).\nTROPOMI Level-1B (L1B) product is generated by the Koninklijk Nederlands Meteoroligisch Instituut (KNMI) TROPOMI L01B processor from Level-0 input data and auxiliary data products with the netCDF-4 enhanced model. It provides users with radiance, irradiance, calibration and engineering products.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "S5P_L1B_RA_BD4",
             "creator": "Copernicus Sentinel data processed by ESA, Koninklijk Nederlands Meteorologisch Instituut (KNMI)",
-            "title": "Sentinel-5P TROPOMI Radiance product band 4 (UVIS detector) L1B V1 (S5P_L1B_RA_BD4) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/S5P_OFFL_L1B_RA_BD4_1.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Starting from August 6th in 2019, Sentinel-5P TROPOMI along-track high spatial resolution (~5.5km at nadir) has been implemented.\nFor data after August 6th of 2019, please check S5P_L1B_RA_BD4 data collection.\n\nThe Copernicus Sentinel-5 Precursor (Sentinel-5P or S5P) satellite mission is one of the European Space Agency's (ESA) new mission family - Sentinels, and it is a joint initiative between the Kingdom of the Netherlands and the ESA. The sole payload on Sentinel-5P is the TROPOspheric Monitoring Instrument (TROPOMI), which is a nadir-viewing 108 degree Field-of-View push-broom grating hyperspectral spectrometer, covering the wavelength of ultraviolet-visible (UV-VIS, 270nm to 495nm), near infrared (NIR, 675nm to 775nm), and shortwave infrared (SWIR, 2305nm-2385nm).\nTROPOMI Level-1B (L1B) product is generated by the Koninklijk Nederlands Meteoroligisch Instituut (KNMI) TROPOMI L01B processor from Level-0 input data and auxiliary data products with the netCDF-4 enhanced model. It provides users with radiance, irradiance, calibration and engineering products.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSENTINEL5P%2FS5P_L1B_RA_BD4.1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSENTINEL5P%2FS5P_L1B_RA_BD4.1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1169782,127 +1169756,155 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/S5P_L1B_RA_BD4_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/S5P_L1B_RA_BD4_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/opendap/S5P_TROPOMI_Level1B/S5P_L1B_RA_BD4.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/opendap/S5P_TROPOMI_Level1B/S5P_L1B_RA_BD4.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/data/S5P_TROPOMI_Level1B/S5P_L1B_RA_BD4.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/data/S5P_TROPOMI_Level1B/S5P_L1B_RA_BD4.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sentinel.esa.int/documents/247904/2476257/Sentinel-5P-TROPOMI-Level-1B-ATBD",
-                    "description": "Algorithm Theoretical Basis Document",
                     "@type": "dcat:Distribution",
+                    "description": "Algorithm Theoretical Basis Document",
+                    "downloadURL": "https://sentinel.esa.int/documents/247904/2476257/Sentinel-5P-TROPOMI-Level-1B-ATBD",
+                    "mediaType": "text/html",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sentinel.esa.int/documents/247904/3119978/Sentinel-5P-Level-01B-input-output-data-specification",
-                    "description": "Data Specification Document",
                     "@type": "dcat:Distribution",
+                    "description": "Data Specification Document",
+                    "downloadURL": "https://sentinel.esa.int/documents/247904/3119978/Sentinel-5P-Level-01B-input-output-data-specification",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=S5P_L1B_RA_BD4_1",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=S5P_L1B_RA_BD4_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sentinel.esa.int/documents/247904/3541451/Sentinel-5P-Level-1b-Product-Readme-File",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://sentinel.esa.int/documents/247904/3541451/Sentinel-5P-Level-1b-Product-Readme-File",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/S5P_OFFL_L1B_RA_BD4_1.png",
+            "identifier": "C1442068499-GES_DISC",
+            "issued": "2014-12-09",
+            "keyword": [
+                "atmosphere",
+                "atmospheric radiation",
+                "earth science",
+                "platform characteristics",
+                "sensor characteristics",
+                "ultraviolet wavelengths",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/SENTINEL5P/S5P_L1B_RA_BD4.1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2014-12-09",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "S5P_L1B_RA_BD4",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-04-30T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Sentinel-5P",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sentinel-5P TROPOMI Radiance product band 4 (UVIS detector) L1B V1 (S5P_L1B_RA_BD4) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-SPICE-6-SPK-V2.0",
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
+            "description": "Version 2.0 ----------- This data set replaces the Voyager 1 Jupiter SPICE data set (DATA_SET_ID = VG1-J-6-SPK-V1.0).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-spice-6-spk-v2.0_p2tn-iv4y",
+            "issued": "2021-05-21",
+            "keyword": [
+                "jupiter",
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-SPICE-6-SPK-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-spice-6-spk-v2.0_p2tn-iv4y",
-            "description": "Version 2.0 ----------- This data set replaces the Voyager 1 Jupiter SPICE data set (DATA_SET_ID = VG1-J-6-SPK-V1.0).",
-            "title": "VG1 JUPITER SPICE SPK KERNEL V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG1 JUPITER SPICE SPK KERNEL V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-LORRI-2-PLUTOCRUISE-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Raw data taken by the New Horizons                Long Range Reconnaissance Imager                                       instrument during the                                                    pluto cruise                                                           mission phase.  This is VERSION 1.0 of this data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-lorri-2-plutocruise-v1.0_p2wm-s5xc",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "charon",
                 "styx",
@@ -1169920,158 +1169922,132 @@
                 "sun",
                 "136108 haumea"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-LORRI-2-PLUTOCRUISE-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-lorri-2-plutocruise-v1.0_p2wm-s5xc",
-            "description": "This data set contains Raw data taken by the New Horizons                Long Range Reconnaissance Imager                                       instrument during the                                                    pluto cruise                                                           mission phase.  This is VERSION 1.0 of this data set.",
-            "title": "NEW HORIZONS                            \n      LORRI PLUTO CRUISE                                                      \n      RAW V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS                            \n      LORRI PLUTO CRUISE                                                      \n      RAW V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amaven.anc&version=1.18",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This bundle contains products associated with the PDS MAVEN Ancillary data archive.",
+            "identifier": "urn:nasa:pds:maven.anc_p2xv-ibne",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "mars",
                 "drf",
                 "mars atmosphere and volatile evolution"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amaven.anc&version=1.18",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:maven.anc_p2xv-ibne",
-            "description": "This bundle contains products associated with the PDS MAVEN Ancillary data archive.",
-            "title": "MAVEN Ancillary Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MAVEN Ancillary Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GPM/AMSRE/AQUA/GPROFCLIM/3A-MONTH/07",
             "citation": "GPM Science Team. 2022-05-09. GPM_3GPROFAQUAAMSRE_CLIM. Version 07. GPM AMSR-E on Aqua (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/AMSRE/AQUA/GPROFCLIM/3A-MONTH/07. https://disc.gsfc.nasa.gov/datacollection/GPM_3GPROFAQUAAMSRE_CLIM_07.html. Digital Science Data.",
-            "issued": "2022-05-09",
-            "temporal": "2002-06-01T00:00:00Z/2011-10-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-01",
-            "keyword": [
-                "atmospheric water vapor",
-                "atmosphere",
-                "earth science",
-                "precipitation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "GEORGE HUFFMAN",
                 "hasEmail": "mailto:George.J.Huffman@nasa.gov"
             },
+            "creator": "GPM Science Team",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2264134954-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Version 07 is the current version of the data set. Older versions will no longer be available and have been superseded by Version 07. \n\nThe \"CLIM\"  products differ from their \"regular\" counterparts (without the \"CLIM\" in the name) by the ancillary data they use. They are Climate-Reference products, which requires homogeneous ancillary data over the climate time series.  Hence, the ECMWF-Interim (European Centre for Medium-Range Weather Forecasts, 2-3 months lag behind the regular production) reanalysis is used as ancillary data to derive surface and atmospheric conditions required by the GPROF algorithm for the \"CLIM\" output. The GPROF databases are also adjusted accordingly for these climate-referenced retrievals.\n\n3GPROF products provide global gridded monthly/daily precipitation averages from multiple satellites that can be used for climate studies. The 3GPROF products are based on retrievals from high-quality microwave sensors, which are sensitive to liquid and ice-phase precipitation hydrometeors in the atmosphere.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "GPM_3GPROFAQUAAMSRE_CLIM",
-            "creator": "GPM Science Team",
-            "title": "GPM AMSR-E on Aqua (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFAQUAAMSRE_CLIM) at GES DISC",
-            "graphic-preview-description": "GPM AMSR-E on Aqua (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree (GPM_3GPROFAQUAAMSRE_CLIM)",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFAQUAAMSRE_CLIM_07.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FAMSRE%2FAQUA%2FGPROFCLIM%2F3A-MONTH%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FAMSRE%2FAQUA%2FGPROFCLIM%2F3A-MONTH%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFAQUAAMSRE_CLIM_07.png",
-                    "description": "GPM AMSR-E on Aqua (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree (GPM_3GPROFAQUAAMSRE_CLIM)",
                     "@type": "dcat:Distribution",
+                    "description": "GPM AMSR-E on Aqua (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree (GPM_3GPROFAQUAAMSRE_CLIM)",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFAQUAAMSRE_CLIM_07.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3GPROFAQUAAMSRE_CLIM_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3GPROFAQUAAMSRE_CLIM_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3GPROFAQUAAMSRE_CLIM.07/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3GPROFAQUAAMSRE_CLIM.07/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L3/GPM_3GPROFAQUAAMSRE_CLIM.07/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L3/GPM_3GPROFAQUAAMSRE_CLIM.07/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3GPROFAQUAAMSRE_CLIM_07",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3GPROFAQUAAMSRE_CLIM_07",
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
@@ -1170081,81 +1170057,119 @@
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
-                    "downloadURL": "https://aqua.nasa.gov/amsr-e",
-                    "description": "Instrument Description",
                     "@type": "dcat:Distribution",
+                    "description": "Instrument Description",
+                    "downloadURL": "https://aqua.nasa.gov/amsr-e",
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
+            "graphic-preview-description": "GPM AMSR-E on Aqua (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree (GPM_3GPROFAQUAAMSRE_CLIM)",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFAQUAAMSRE_CLIM_07.png",
+            "identifier": "C2264134954-GES_DISC",
+            "issued": "2022-05-09",
+            "keyword": [
+                "atmospheric water vapor",
+                "atmosphere",
+                "earth science",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/AMSRE/AQUA/GPROFCLIM/3A-MONTH/07",
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
+            "series-name": "GPM_3GPROFAQUAAMSRE_CLIM",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-06-01T00:00:00Z/2011-10-31T23:59:59.999Z",
             "theme": [
                 "GPM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM AMSR-E on Aqua (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFAQUAAMSRE_CLIM) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SS-RSS-1-SCE1-V1.0",
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
-                "solar system"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ss-rss-1-sce1-v1.0_p32a-xrvq",
+            "issued": "2018-06-26",
+            "keyword": [
+                "cassini-huygens",
+                "solar system"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SS-RSS-1-SCE1-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ss-rss-1-sce1-v1.0_p32a-xrvq",
-            "description": "not applicable",
-            "title": "CASSINI RSS RAW DATA SET - SCE1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI RSS RAW DATA SET - SCE1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/p32p-ptxs",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "The Rodent Research-3 (RR-3) mission was sponsored by the pharmaceutical company Eli Lilly and Co. and the Center for the Advancement of Science in Space to study the effectiveness of a potential countermeasure for the loss of muscle and bone mass that occurs during spaceflight. Twenty BALB/c 18-weeks old female mice (ten controls and ten treated) were flown to the ISS and housed in the Rodent Habitat for 39-42 days. Twenty mice of similar age sex and strain were used for ground controls housed in identical hardware and matching ISS environmental conditions. Basal controls were housed in standard vivarium cages. Spaceflight ground controls and basal groups had blood collected then were euthanized had one hind limb removed and finally whole carcasses were stored at -80 C until dissection. All mice in this data set received only the control/sham injection.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-163",
+                    "mediaType": "text/html",
+                    "title": "Rodent Research-3-CASIS: Mouse kidney transcriptomic proteomic and epigenomic data"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-163_p32p-ptxs_p32p-ptxs",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "labeling",
                 "mass spectrometry",
@@ -1170174,1482 +1170188,1477 @@
                 "animal husbandry",
                 "library construction"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/p32p-ptxs",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-163_p32p-ptxs_p32p-ptxs",
-            "description": "The Rodent Research-3 (RR-3) mission was sponsored by the pharmaceutical company Eli Lilly and Co. and the Center for the Advancement of Science in Space to study the effectiveness of a potential countermeasure for the loss of muscle and bone mass that occurs during spaceflight. Twenty BALB/c 18-weeks old female mice (ten controls and ten treated) were flown to the ISS and housed in the Rodent Habitat for 39-42 days. Twenty mice of similar age sex and strain were used for ground controls housed in identical hardware and matching ISS environmental conditions. Basal controls were housed in standard vivarium cages. Spaceflight ground controls and basal groups had blood collected then were euthanized had one hind limb removed and finally whole carcasses were stored at -80 C until dissection. All mice in this data set received only the control/sham injection.",
-            "title": "Rodent Research-3-CASIS: Mouse kidney transcriptomic proteomic and epigenomic data",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-163",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Rodent Research-3-CASIS: Mouse kidney transcriptomic proteomic and epigenomic data"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Rodent Research-3-CASIS: Mouse kidney transcriptomic proteomic and epigenomic data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-PANCAM-5-ANAGLYPH-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-pancam-5-anaglyph-ops-v1.0_p383-u5hs",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-PANCAM-5-ANAGLYPH-OPS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-pancam-5-anaglyph-ops-v1.0_p383-u5hs",
-            "description": "not applicable",
-            "title": "MER 2 MARS PANORAMIC CAMERA ANAGLYPH RDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MER 2 MARS PANORAMIC CAMERA ANAGLYPH RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C156141692-LARC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 FIRSTLOOK Component Global Radiance Product for a day;See ProductionDateTime for Published date.",
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
-            "identifier": "C156141692-LARC",
             "description": "This file contains the MISR Level 3 FIRSTLOOK Component Global Radiance Product covering a day",
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "title": "MISR Level 3 FIRSTLOOK Component Global Radiance Product covering a day V002",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C156141692-LARC.html",
-                    "description": "View this dataset on the CMR (Common Metadata Repository)",
                     "@type": "dcat:Distribution",
+                    "description": "View this dataset on the CMR (Common Metadata Repository)",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C156141692-LARC.html",
+                    "mediaType": "text/html",
                     "title": "CMR"
                 }
             ],
+            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
+            "identifier": "C156141692-LARC",
+            "issued": "2007-07-30",
+            "keyword": [
+                "nasa"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C156141692-LARC.html",
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
+            "title": "MISR Level 3 FIRSTLOOK Component Global Radiance Product covering a day V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-RSSL-N-NDR-HALLEY-V1.0",
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
+            "description": "NASA's International Halley Watch (IHW) has created a Comet Halley Archive. The collection of data spans the full wavelength range as submitted by scientists to the IHW. The observations belong to one of the following Disciplines: Amateur, Astrometry, Infrared Studies, Large-Scale Phenomena, Meteor Studies, Near-Nucleus Studies, Photometry and Polarimetry, Radio Studies, and Spectroscopy and Spectrophotometry. The data collected by these nine disciplines were augmented by Spacecraft measurements. The data were submitted to IHW, but the evaluation and selection for the Archive has been the primary responsibility of the Discipline Specialist Teams for each network in cooperation with the Lead Center. The Radio Studies Spectral Line Subnetwork also recorded data as 'upper limits'. There are 82 files recording this information for dates from 1985 October 05 through 1986 May 06.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-rssl-n-ndr-halley-v1.0_p39x-zeck",
+            "issued": "2018-06-26",
+            "keyword": [
+                "halley",
+                "international halley watch"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-RSSL-N-NDR-HALLEY-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-rssl-n-ndr-halley-v1.0_p39x-zeck",
-            "description": "NASA's International Halley Watch (IHW) has created a Comet Halley Archive. The collection of data spans the full wavelength range as submitted by scientists to the IHW. The observations belong to one of the following Disciplines: Amateur, Astrometry, Infrared Studies, Large-Scale Phenomena, Meteor Studies, Near-Nucleus Studies, Photometry and Polarimetry, Radio Studies, and Spectroscopy and Spectrophotometry. The data collected by these nine disciplines were augmented by Spacecraft measurements. The data were submitted to IHW, but the evaluation and selection for the Archive has been the primary responsibility of the Discipline Specialist Teams for each network in cooperation with the Lead Center. The Radio Studies Spectral Line Subnetwork also recorded data as 'upper limits'. There are 82 files recording this information for dates from 1985 October 05 through 1986 May 06.",
-            "title": "IHW COMET HALLEY RADIO SPECTRAL MEASUREMENTS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "IHW COMET HALLEY RADIO SPECTRAL MEASUREMENTS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2652675337-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC.",
-            "issued": "2023-04-04",
-            "temporal": "2022-11-10T00:00:00Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-04",
-            "keyword": [
-                "earth science",
-                "oceans",
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
-            "identifier": "C2652675337-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "NOAA-21 VIIRS Global Mapped Chlorophyll (CHL) - NRT Data, version R2022.0",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NOAA21/VIIRS/L3M/CHL/2022",
-                    "description": "VIIRS-NOAA-21 L3M Chlorophyll (CHL) - NRT Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS-NOAA-21 L3M Chlorophyll (CHL) - NRT Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NOAA21/VIIRS/L3M/CHL/2022",
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
+            "identifier": "C2652675337-OB_DAAC",
+            "issued": "2023-04-04",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "ocean optics"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2652675337-OB_DAAC.html",
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
+            "title": "NOAA-21 VIIRS Global Mapped Chlorophyll (CHL) - NRT Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/17",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Eloranta, E. W. 1994. Boundary Layer Heights: LIDAR (FIFE). Data set. Available on-line [http://www.daac.ornl.gov] from Oak Ridge National Laboratory Distributed Active Archive Center, Oak Ridge, Tennessee, U.S.A. Also published in D. E. Strebel, D. R. Landis, K. F. Huemmrich, and B. W. Meeson (eds.), Collected Data of the First ISLSCP Field Experiment, Vol. 1: Surface Observations and Non-Image Data Sets. CD-ROM. National Aeronautics and Space Administration, Goddard Space Flight Center, Greenbelt, Maryland, U.S.A. (available from http://www.daac.ornl.gov). doi:10.3334/ORNLDAAC/17",
-            "issued": "2024-05-04",
-            "temporal": "1987-06-30T00:00:00Z/1989-10-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-07",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "altitude"
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
-            "identifier": "C2979931759-ORNL_CLOUD",
             "description": "Height of the mixed layer gas for each LIDAR shot in volume scan, then averaged",
-            "graphic-preview-description": "Browse Image",
-            "title": "Boundary Layer Heights: LIDAR (FIFE)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/fife_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F17",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F17",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_atmos_lidar_ht/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_atmos_lidar_ht/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/lidar_height_data.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/lidar_height_data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/17",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/17",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_atmos_lidar_ht/comp/lidar_height_data.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_atmos_lidar_ht/comp/lidar_height_data.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_atmos_lidar_ht/comp/lidar_ht.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_atmos_lidar_ht/comp/lidar_ht.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_atmos_lidar_ht/comp/lidar_ht.tdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_atmos_lidar_ht/comp/lidar_ht.tdf",
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
+            "identifier": "C2979931759-ORNL_CLOUD",
+            "issued": "2024-05-04",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "altitude"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/17",
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
             "spatial": "39.07 -96.54",
+            "temporal": "1987-06-30T00:00:00Z/1989-10-31T23:59:59Z",
             "theme": [
                 "FIFE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Boundary Layer Heights: LIDAR (FIFE)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NOAA-21/VIIRS/L3B/RRS/2022",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/NOAA-21/VIIRS/L3B/RRS/2022.",
-            "issued": "2023-04-04",
-            "temporal": "2022-11-10T00:00:00Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-04",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "aerosols",
-                "oceans",
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
-            "identifier": "C2652675335-OB_DAAC",
             "description": "The Visible and Infrared Imager/Radiometer Suite (VIIRS) is a multi-disciplinary instrument that is being flown on the Joint Polar Satellite System (JPSS) series of spacecraft, including the Suomi National Polar-orbiting Partnership (S-NPP) that launched in October 2011. JPSS is a multi-platform, multi-agency program that consolidates the polar orbiting spacecraft of NASA and the National Oceanic and Atmospheric Administration (NOAA). S-NPP is the initial spacecraft in this series, and VIIRS is the successor to MODIS for Earth science data product generation. VIIRS has 22 spectral bands ranging from 412 nm to 12 nm. There are 16 moderate-resolution bands (750m at nadir), 5 image-resolution bands (375m), and one day-night band (DNB).",
-            "title": "NOAA-21 VIIRS Global Binned Remote-Sensing Reflectance (RRS) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNOAA-21%2FVIIRS%2FL3B%2FRRS%2F2022",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNOAA-21%2FVIIRS%2FL3B%2FRRS%2F2022",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NOAA-21/VIIRS/L3B/RRS/2022",
-                    "description": "VIIRS-NOAA-21 L3B Remote-Sensing Reflectance (RRS) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS-NOAA-21 L3B Remote-Sensing Reflectance (RRS) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NOAA-21/VIIRS/L3B/RRS/2022",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2652675335-OB_DAAC",
+            "issued": "2023-04-04",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "aerosols",
+                "oceans",
+                "ocean optics"
+            ],
+            "landingPage": "https://doi.org/10.5067/NOAA-21/VIIRS/L3B/RRS/2022",
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
+            "title": "NOAA-21 VIIRS Global Binned Remote-Sensing Reflectance (RRS) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1708926764-CDDIS.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, CDDIS.",
-            "issued": "1992-01-01",
-            "temporal": "1992-01-01T00:00:00Z/2024-10-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-23",
-            "keyword": [
-                "solid earth",
-                "earth science",
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
-            "identifier": "C1708926764-CDDIS",
             "description": "This dataset consists of supporting information for use of ground-based Global Navigation Satellite System (GNSS) data and products from the NASA Crustal Dynamics Data Information System (CDDIS). GNSS provide autonomous geo-spatial positioning with global coverage. GNSS data sets from ground receivers at the CDDIS consist primarily of the data from the U.S. Global Positioning System (GPS) and the Russian GLObal NAvigation Satellite System (GLONASS). Since 2011, the CDDIS GNSS archive includes data from other GNSS (Europe\u2019s Galileo, China\u2019s Beidou, Japan\u2019s Quasi-Zenith Satellite System/QZSS, the Indian Regional Navigation Satellite System/IRNSS, and worldwide Satellite Based Augmentation Systems/SBASs), which are similar to the U.S. GPS in terms of the satellite constellation, orbits, and signal structure. More information about these data and products are available on the CDDIS website at https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/GNSS_data_and_product_archive.html.",
-            "title": "Supporting Information for Global Navigation Satellite System (GNSS) Data and Products from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/GNSS_data_and_product_archive.html",
-                    "description": "URL for more information about GNSS data and products",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about GNSS data and products",
+                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/GNSS_data_and_product_archive.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/archive/gnss",
-                    "description": "URL for retrieval of GNSS data, products, and information through https",
                     "@type": "dcat:Distribution",
+                    "description": "URL for retrieval of GNSS data, products, and information through https",
+                    "downloadURL": "https://cddis.nasa.gov/archive/gnss",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1708926764-CDDIS",
+            "issued": "1992-01-01",
+            "keyword": [
+                "solid earth",
+                "earth science",
+                "geodetics",
+                "gravity/gravitational field",
+                "tectonics"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1708926764-CDDIS.html",
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
+            "temporal": "1992-01-01T00:00:00Z/2024-10-28T00:00:00Z",
             "theme": [
                 "IGS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Supporting Information for Global Navigation Satellite System (GNSS) Data and Products from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ISS/CATS/L2O_N-M7.2-V3-01_05kmPro",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2018-10-31. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ISS/CATS/L2O_N-M7.2-V3-01_05kmPro. https://asdc.larc.nasa.gov/project/CATS-ISS.",
-            "issued": "2018-08-13",
-            "temporal": "2015-03-25T00:00:00Z/2017-10-29T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-08-13",
-            "keyword": [
-                "aerosols",
-                "atmosphere",
-                "clouds",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "MATTHEW MCGILL",
                 "hasEmail": "mailto:matthew.j.mcgill@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1599922074-LARC_ASDC",
             "description": "CATS-ISS_L2O_N-M7.1-V2-01_05kmPro is the Cloud-Aerosol Transport System (CATS) International Space Station (ISS) Level 2 Operational Night Mode 7.2 Version 3-01 5 km Profile data product. This collection spans from March 25, 2015 to October 29, 2017. CATS, which was launched on January 10, 2015, was a lidar remote sensing instrument that provided range-resolved profile measurements of atmospheric aerosols and clouds from the ISS. CATS was intended to operate on-orbit for up to three years. CATS provides vertical profiles at three wavelengths, orbiting between ~230 and ~270 miles above the Earth's surface at a 51-degree inclination with nearly a three-day repeat cycle. For the first time, scientists were able to study diurnal (day-to-night) changes in cloud and aerosol effects from space by observing the same spot on Earth at different times each day. CATS Level 2 Layer data products contain geophysical parameters and are derived from Level 1 data, at 60m vertical and 5km horizontal resolution.",
-            "graphic-preview-description": "CATS Browse and Granule Availability",
-            "title": "CATS-ISS Level 2 Operational Night Mode 7.2 Version 3-01 5 km Profile",
-            "graphic-preview-file": "https://cats.gsfc.nasa.gov/data/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FISS%2FCATS%2FL2O_N-M7.2-V3-01_05kmPro",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FISS%2FCATS%2FL2O_N-M7.2-V3-01_05kmPro",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/CATS-ISS",
-                    "description": "ASDC Data and Information for CATS",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for CATS",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/CATS-ISS",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/cats/quality_summaries/CATS_Release_Notes6_v2.pdf",
-                    "description": "CATS Data Release Notes, L1B Version 2.08, L2O Version 2.00, L2O Version 2.01",
                     "@type": "dcat:Distribution",
+                    "description": "CATS Data Release Notes, L1B Version 2.08, L2O Version 2.00, L2O Version 2.01",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/cats/quality_summaries/CATS_Release_Notes6_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://cats.gsfc.nasa.gov/media/docs/CATS_Data_Products_Catalog.pdf",
-                    "description": "CATS Data Management System Data Products Catalog",
                     "@type": "dcat:Distribution",
+                    "description": "CATS Data Management System Data Products Catalog",
+                    "downloadURL": "https://cats.gsfc.nasa.gov/media/docs/CATS_Data_Products_Catalog.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cats.gsfc.nasa.gov/data/browse/",
-                    "description": "CATS Browse and Granule Availability",
                     "@type": "dcat:Distribution",
+                    "description": "CATS Browse and Granule Availability",
+                    "downloadURL": "https://cats.gsfc.nasa.gov/data/browse/",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/cats/guide/CATS_ATBD.pdf",
-                    "description": "CATS Algorithm Theoretical Basis Document Level 1 and Level 2 Data Products - Release 1.0 - 12 June2015",
                     "@type": "dcat:Distribution",
+                    "description": "CATS Algorithm Theoretical Basis Document Level 1 and Level 2 Data Products - Release 1.0 - 12 June2015",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/cats/guide/CATS_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1599922074-LARC_ASDC",
-                    "description": "Earthdata Search for CATS-ISS_L2O_N-M7.2-V3-01_05kmPro_V3-01 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CATS-ISS_L2O_N-M7.2-V3-01_05kmPro_V3-01 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1599922074-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CATS/L2O_N-M7.2-V3-01_05kmPro/contents.html",
-                    "description": "OPeNDAP data access for CATS-ISS_L2O_N-M7.2-V3-01_05kmPro_V3-01",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CATS-ISS_L2O_N-M7.2-V3-01_05kmPro_V3-01",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CATS/L2O_N-M7.2-V3-01_05kmPro/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ISS/CATS/L2O_N-M7.2-V3-01_05kmPro",
-                    "description": "DOI data set landing page for CATS-ISS_L2O_N-M7.2-V3-01_05kmPro_V3-01",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CATS-ISS_L2O_N-M7.2-V3-01_05kmPro_V3-01",
+                    "downloadURL": "https://doi.org/10.5067/ISS/CATS/L2O_N-M7.2-V3-01_05kmPro",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/cats/guide/CATS_Data_Products_Catalog_R7.0.pdf",
-                    "description": "CATS Data Management System Data Products Catalog Release 7.0",
                     "@type": "dcat:Distribution",
+                    "description": "CATS Data Management System Data Products Catalog Release 7.0",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/cats/guide/CATS_Data_Products_Catalog_R7.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/cats/guide/CATS_Data_Products_Catalog_R6.0.pdf",
-                    "description": "CATS Data Management System Data Products Catalog, Release 6.0",
                     "@type": "dcat:Distribution",
+                    "description": "CATS Data Management System Data Products Catalog, Release 6.0",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/cats/guide/CATS_Data_Products_Catalog_R6.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CATS/L2O_N-M7.2-V3-01_05kmPro/",
-                    "description": "ASDC Direct Data Download for CATS-ISS_L2O_N-M7.2-V3-01_05kmPro_V3-01",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CATS-ISS_L2O_N-M7.2-V3-01_05kmPro_V3-01",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CATS/L2O_N-M7.2-V3-01_05kmPro/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/84400/dust-and-clouds-dance-over-the-sahara",
-                    "description": "NASA Earth Observatory Article: Dust and Clouds Dance Over the Sahara",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Dust and Clouds Dance Over the Sahara",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/84400/dust-and-clouds-dance-over-the-sahara",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/84214/blue-marble-eastern-hemisphere",
-                    "description": "NASA Earth Observatory Article: Blue Marble, Eastern Hemisphere",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Blue Marble, Eastern Hemisphere",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/84214/blue-marble-eastern-hemisphere",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/86286/nighttime-view-of-raung-volcanic-plume",
-                    "description": "NASA Earth Observatory Article: Nighttime View of Raung Volcanic Plume",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Nighttime View of Raung Volcanic Plume",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/86286/nighttime-view-of-raung-volcanic-plume",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/86218/a-slice-of-cirrus",
-                    "description": "NASA Earth Observatory Article: A Slice of Cirrus",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: A Slice of Cirrus",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/86218/a-slice-of-cirrus",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 }
             ],
+            "graphic-preview-description": "CATS Browse and Granule Availability",
+            "graphic-preview-file": "https://cats.gsfc.nasa.gov/data/browse/",
+            "identifier": "C1599922074-LARC_ASDC",
+            "issued": "2018-08-13",
+            "keyword": [
+                "aerosols",
+                "atmosphere",
+                "clouds",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ISS/CATS/L2O_N-M7.2-V3-01_05kmPro",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-08-13",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-180.0 -52.0 180.0 52.0",
+            "temporal": "2015-03-25T00:00:00Z/2017-10-29T23:59:59Z",
             "theme": [
                 "CATS-ISS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CATS-ISS Level 2 Operational Night Mode 7.2 Version 3-01 5 km Profile"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0182-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-06T08:45:05.000 to 2014-08-06T12:29:58.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0182-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0182-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0182-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-06T08:45:05.000 to 2014-08-06T12:29:58.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0182 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0182 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ATLAS/ATL20.004",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "ATLAS/ICESat-2 L3B Daily and Monthly Gridded Sea Ice Freeboard V004. Version 004. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/ATLAS/ATL20.004.",
-            "issued": "2018-10-14",
-            "temporal": "2018-10-14T00:00:00Z/2024-10-07T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-31",
-            "keyword": [
-                "earth science",
-                "sea ice",
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
-            "identifier": "C2666857908-NSIDC_ECS",
             "description": "ATL20 contains daily and monthly gridded estimates of sea ice freeboard, derived from along-track freeboard estimates in the ATLAS/ICESat-2 L3A Sea Ice Freeboard product (ATL10). Data are gridded at 25 km using the SSM/I Polar Stereographic Projection.",
-            "title": "ATLAS/ICESat-2 L3B Daily and Monthly Gridded Sea Ice Freeboard V004",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FATLAS%2FATL20.004",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FATLAS%2FATL20.004",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ATLAS/ATL20.004/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ATLAS/ATL20.004/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ATL20+V004",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ATL20+V004",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/ATL20/versions/4/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/ATL20/versions/4/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL20.004",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL20.004",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL20.004",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL20.004",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2666857908-NSIDC_ECS",
+            "issued": "2018-10-14",
+            "keyword": [
+                "earth science",
+                "sea ice",
+                "cryosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ATLAS/ATL20.004",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-07-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-10-14T00:00:00Z/2024-10-07T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ATLAS/ICESat-2 L3B Daily and Monthly Gridded Sea Ice Freeboard V004"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-SWAP-5-DERIVED-SOLARWIND-V1.0",
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
+            "description": "This data set presents characteristics of the solar wind derived from     the New Horizons Solar Wind Around Pluto (SWAP) experiment from           observations obtained during cruise, Pluto encounter (excluding the       period inside the Pluto system), and afterwards. The single data file     the time information for a given pair of sweeps, original level 2         data file reference, the solar wind speed proton density, proton          speed, proton temperature, proton dynamic pressure, proton thermal        pressure, spacecraft position and speed in Heliographic Inertial          (HGI), Heliocentric Aries ecliptic, and Heliographic (Carrington)         coordinates.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-swap-5-derived-solarwind-v1.0_p3sm-btsh",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-SWAP-5-DERIVED-SOLARWIND-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-swap-5-derived-solarwind-v1.0_p3sm-btsh",
-            "description": "This data set presents characteristics of the solar wind derived from     the New Horizons Solar Wind Around Pluto (SWAP) experiment from           observations obtained during cruise, Pluto encounter (excluding the       period inside the Pluto system), and afterwards. The single data file     the time information for a given pair of sweeps, original level 2         data file reference, the solar wind speed proton density, proton          speed, proton temperature, proton dynamic pressure, proton thermal        pressure, spacecraft position and speed in Heliographic Inertial          (HGI), Heliocentric Aries ecliptic, and Heliographic (Carrington)         coordinates.",
-            "title": "NEW HORIZONS SWAP SOLAR WIND DERIVED CHARACTERISTICS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS SWAP SOLAR WIND DERIVED CHARACTERISTICS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-C-MRI-3-NAV-9P-ENCOUNTER-V1.0",
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
-                "9p/tempel 1 (1867 g1)"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains calibrated images of comet 9P/Tempel 1 acquired by the Deep Impact Medium Resolution Instrument Visible CCD during the encounter phase of the mission. These observations were used for optical and autonomous navigation of the flyby spacecraft as well as for scientific investigations. These data were collected from 15 May to 4 July 2005.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-c-mri-3-nav-9p-encounter-v1.0_p3sq-rakh",
+            "issued": "2018-06-26",
+            "keyword": [
+                "deep impact",
+                "9p/tempel 1 (1867 g1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-C-MRI-3-NAV-9P-ENCOUNTER-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-c-mri-3-nav-9p-encounter-v1.0_p3sq-rakh",
-            "description": "This data set contains calibrated images of comet 9P/Tempel 1 acquired by the Deep Impact Medium Resolution Instrument Visible CCD during the encounter phase of the mission. These observations were used for optical and autonomous navigation of the flyby spacecraft as well as for scientific investigations. These data were collected from 15 May to 4 July 2005.",
-            "title": "DEEP IMPACT 9P/TEMPEL ENCOUNTER - REDUCED MRI NAV IMGS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "DEEP IMPACT 9P/TEMPEL ENCOUNTER - REDUCED MRI NAV IMGS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/ME5QX6Q5IGGU",
             "citation": "Global Modeling and Assimilation Office (GMAO). 2015-06-30. M2C0NXASM. Version 5.12.4. MERRA-2 const_2d_asm_Nx: 2d, constants V5.12.4. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/ME5QX6Q5IGGU. https://disc.gsfc.nasa.gov/datacollection/M2C0NXASM_5.12.4.html. Digital Science Data.",
-            "issued": "2007-06-14",
-            "temporal": "1980-01-01T00:00:00Z/2020-12-31T23:59:59.999Z",
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
-                "oceans",
-                "sea surface topography",
-                "altitude",
-                "earth science",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DANA OSTRENGA",
                 "hasEmail": "mailto:dana.ostrenga@nasa.gov"
             },
+            "creator": "Global Modeling and Assimilation Office (GMAO)",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1276812819-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "M2C0NXASM (or const_2d_asm_Nx) is a data collection in Modern-Era Retrospective analysis for Research and Applications version 2 (MERRA-2).  This collection consists of 2-dimensional constant model parameters, such as the fraction of lake, land, and ocean within a model grid cell. \n\nMERRA-2 is the latest version of global atmospheric reanalysis for the satellite era produced by NASA Global Modeling and Assimilation Office (GMAO) using the Goddard Earth Observing System Model (GEOS) version 5.12.4.  \n\nMERRA-2 Mailing List: Sign up to receive information on reprocessing of data, changing of tools and services, as well as data announcements from GMAO. Contact the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov) to be added to the list.\n\nQuestions: If you have a question, please read \"MERRA-2 File Specification Document\",  \u201cMERRA-2 Data Access \u2013 Quick Start Guide\u201d, and FAQs linked from the \u201dDocumentation\u201d tab on this page.  If that does not answer your question, you may email the question on data access to the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov), or the question on science to the MERRA-2 science team (merra-questions@lists.nasa.gov).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "M2C0NXASM",
-            "creator": "Global Modeling and Assimilation Office (GMAO)",
-            "graphic-preview-description": "M2C0NXASM variable",
-            "title": "MERRA-2 const_2d_asm_Nx: 2d, constants 0.625 x 0.5 degree V5.12.4 (M2C0NXASM) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2C0NXASM_5.12.4.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FME5QX6Q5IGGU",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FME5QX6Q5IGGU",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2C0NXASM_5.12.4.png",
-                    "description": "M2C0NXASM variable",
                     "@type": "dcat:Distribution",
+                    "description": "M2C0NXASM variable",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2C0NXASM_5.12.4.png",
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
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2C0NXASM_5.12.4.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2C0NXASM_5.12.4.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_MONTHLY/M2C0NXASM.5.12.4/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_MONTHLY/M2C0NXASM.5.12.4/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2C0NXASM",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2C0NXASM",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/dods/M2C0NXASM.info",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/dods/M2C0NXASM.info",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2_MONTHLY/M2C0NXASM.5.12.4/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2_MONTHLY/M2C0NXASM.5.12.4/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_constant/M2C0NXASM.5.12.4/catalog.html",
-                    "description": "Time aggregated THREDDS Data Server (TDS) ",
                     "@type": "dcat:Distribution",
+                    "description": "Time aggregated THREDDS Data Server (TDS) ",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_constant/M2C0NXASM.5.12.4/catalog.html",
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
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_MONTHLY/M2C0NXASM.5.12.4/doc/MERRA2.README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_MONTHLY/M2C0NXASM.5.12.4/doc/MERRA2.README.pdf",
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
+            "graphic-preview-description": "M2C0NXASM variable",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2C0NXASM_5.12.4.png",
+            "identifier": "C1276812819-GES_DISC",
+            "issued": "2007-06-14",
+            "keyword": [
+                "oceans",
+                "sea surface topography",
+                "altitude",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ME5QX6Q5IGGU",
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
+            "series-name": "M2C0NXASM",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1980-01-01T00:00:00Z/2020-12-31T23:59:59.999Z",
             "theme": [
                 "MERRA-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MERRA-2 const_2d_asm_Nx: 2d, constants 0.625 x 0.5 degree V5.12.4 (M2C0NXASM) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-A-SDC-3-KEM1-V2.0",
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
-                "dust",
-                "new horizons kuiper belt extended mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Calibrated data taken by the New Horizons Student Dust Counter instrument during the KEM1 ENCOUNTER mission phase. This is VERSION 2.0 of this data set. This data set contains data acquired by the spacecraft between 08/14/2018 and 01/31/2019. It only includes data downlinked before 02/01/2019. Future datasets may include more data acquired by the spacecraft after 08/13/2018 but downlinked after 01/31/2019.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-a-sdc-3-kem1-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "dust",
+                "new horizons kuiper belt extended mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-A-SDC-3-KEM1-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-a-sdc-3-kem1-v2.0",
-            "description": "This data set contains Calibrated data taken by the New Horizons Student Dust Counter instrument during the KEM1 ENCOUNTER mission phase. This is VERSION 2.0 of this data set. This data set contains data acquired by the spacecraft between 08/14/2018 and 01/31/2019. It only includes data downlinked before 02/01/2019. Future datasets may include more data acquired by the spacecraft after 08/13/2018 but downlinked after 01/31/2019.",
-            "title": "NEW HORIZONS\n      SDC KEM1\n      CALIBRATED V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS\n      SDC KEM1\n      CALIBRATED V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-HAZCAM-5-ANAGLYPH-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-hazcam-5-anaglyph-ops-v1.0_p3yh-uhy3",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars exploration rover",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-HAZCAM-5-ANAGLYPH-OPS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-hazcam-5-anaglyph-ops-v1.0_p3yh-uhy3",
-            "description": "not applicable",
-            "title": "MER 1 MARS HAZARD AVOID CAMERA ANAGLYPH RDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MER 1 MARS HAZARD AVOID CAMERA ANAGLYPH RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/STRAT_MetNav_AircraftInSitu_ER2_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2023-11-20. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/STRAT_MetNav_AircraftInSitu_ER2_Data_1.",
-            "issued": "1995-03-24",
-            "temporal": "1995-03-24T00:00:00Z/1996-12-21T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "1996-12-20",
-            "keyword": [
-                "spectral/engineering",
-                "atmospheric pressure",
-                "atmospheric winds",
-                "atmospheric temperature",
-                "platform characteristics",
-                "infrared wavelengths",
-                "earth science",
-                "altitude",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "T. Paul Bui",
                 "hasEmail": "mailto:thaopaul.v.bui@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2770076029-LARC_ASDC",
             "description": "STRAT_MetNav_AircraftInSitu_ER2_Data is the in-situ meteorological and navigational data collected during the Stratospheric Tracers of Atmospheric Transport (STRAT) campaign. Data from the Meteorological Measurement System (MMS), ER-2 Nav Recorder (NavRec), Microwave Temperature Profiler (MTP), and the Composition and Photo-Dissociative Flux Measurement (CPFM) are featured in this collection. Data collection for this product is complete.\r\n\r\nThe STRAT campaign was a field campaign conducted by NASA from May 1995 to February 1996. The primary goal of STRAT was to collect measurements of the change of long-lived tracers and functions of altitude, latitude, and season. These measurements were taken to aid with determining rates for global-scale transport and future distributions of high-speed civil transport (HSCT) exhaust that was emitted into the lower atmosphere. STRAT had four main objectives:  defining the rate of transport of trace gases from the stratosphere and troposphere (i.e., HSCT exhaust emissions), improving the understanding of dynamical coupling rates for transport of trace gases between tropical regions and higher latitudes and lower altitudes (between tropical regions, higher latitudes, and lower altitudes are where most ozone resides), improving understanding of chemistry in the upper troposphere and lower stratosphere, and finally, providing data sets for testing two-dimensional and three-dimensional models used in assessments of impacts from stratospheric aviation.  \r\n\r\nTo accomplish these objectives, the STRAT Science Team conducted various surface-based remote sensing and in-situ measurements. NASA flew the ER-2 aircraft along with balloons such as ozonesondes and radiosondes just below the tropopause in the Northern Hemisphere to collect data. Along with the ER-2 and balloons, NASA also utilized satellite imagery, theoretical models, and ground sites. The ER-2 collected data on HOx, NOy, CO2, ozone, water vapor, and temperature. The ER-2 also collected in-situ stratospheric measurements of N2O, CH4, CO, HCL, and NO using the Aircraft Laser Infrared Absorption Spectrometer (ALIAS). Ozonesondes and radiosondes were also deployed to collect data on CO2, NO/NOy, air temperature, pressure, and 3D wind. These balloons also took in-situ measurements of N2O, CFC-11, CH4, CO, HCL, and NO2 using the ALIAS. Ground stations were responsible for taking measurements of O3, ozone mixing ratio, pressure, and temperature. Satellites took infrared images of the atmosphere with the goal of aiding in completing STRAT objectives. Pressure and temperature models were created to help plan the mission.",
-            "title": "STRAT ER-2 Meteorological and Navigational Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSTRAT_MetNav_AircraftInSitu_ER2_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSTRAT_MetNav_AircraftInSitu_ER2_Data_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/strat",
-                    "description": "ESPO Home Page for STRAT",
                     "@type": "dcat:Distribution",
+                    "description": "ESPO Home Page for STRAT",
+                    "downloadURL": "https://espo.nasa.gov/strat",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/strat/content/STRAT_Science_Overview",
-                    "description": "STRAT Science Overview",
                     "@type": "dcat:Distribution",
+                    "description": "STRAT Science Overview",
+                    "downloadURL": "https://espo.nasa.gov/strat/content/STRAT_Science_Overview",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2770076029-LARC_ASDC",
-                    "description": "Earthdata Search for STRAT_MetNav_AircraftInSitu_ER2_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for STRAT_MetNav_AircraftInSitu_ER2_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2770076029-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/STRAT_MetNav_AircraftInSitu_ER2_Data_1",
-                    "description": "DOI for STRAT_MetNav_AircraftInSitu_ER2_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for STRAT_MetNav_AircraftInSitu_ER2_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/STRAT_MetNav_AircraftInSitu_ER2_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/STRAT/MetNav_AircraftInSitu_ER2_Data_1/",
-                    "description": "ASDC Direct Data Download for STRAT_MetNav_AircraftInSitu_ER2_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for STRAT_MetNav_AircraftInSitu_ER2_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/STRAT/MetNav_AircraftInSitu_ER2_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
-            "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-80.01 -180.0 -80.01 180.0 68.23 180.0 68.23 -180.0 -80.01 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
-            "theme": [
-                "STRAT",
-                "geospatial"
+            "identifier": "C2770076029-LARC_ASDC",
+            "issued": "1995-03-24",
+            "keyword": [
+                "spectral/engineering",
+                "atmospheric pressure",
+                "atmospheric winds",
+                "atmospheric temperature",
+                "platform characteristics",
+                "infrared wavelengths",
+                "earth science",
+                "altitude",
+                "atmosphere"
             ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/STRAT_MetNav_AircraftInSitu_ER2_Data_1",
             "language": [
                 "en-US"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0040",
-            "bureauCode": [
-                "026:00"
             ],
-            "citation": "2003-07-02. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDCDAAC/NARSTO/0040.",
-            "issued": "2003-09-09",
-            "temporal": "2000-08-19T00:00:00Z/2000-09-12T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-04-18",
-            "keyword": [
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "atmospheric radiation",
-                "atmospheric winds",
-                "atmospheric pressure",
-                "aerosols",
-                "atmosphere",
-                "atmospheric chemistry",
-                "earth science"
+            "modified": "1996-12-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
+            "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-80.01 -180.0 -80.01 180.0 68.23 180.0 68.23 -180.0 -80.01 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1995-03-24T00:00:00Z/1996-12-21T00:00:00Z",
+            "theme": [
+                "STRAT",
+                "geospatial"
+            ],
+            "title": "STRAT ER-2 Meteorological and Navigational Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
             ],
+            "citation": "2003-07-02. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDCDAAC/NARSTO/0040.",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "YIN-NAN LEE",
                 "hasEmail": "mailto:ynlee@bnl.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2338588309-LARC_ASDC",
             "description": "NARSTO_EPA_SS_HOUSTON_TEXAQS2000_DOE_G-1_DATA is North American Research Strategy for Tropospheric Ozone (NARSTO) Environmental Protection Agency (EPA) Supersite (SS) Houston, Texas Air Quality Study 2000 (TexAQS2000) Department of Energy (DOE) G-1 Air Chemistry, Aerosol, and Met Data. \r\n\r\nTwenty research flights were made from August 18 to September 12, 2000.The Houston Supersite is one of several Supersites that was established in urban areas within the United States by the U.S. Environmental Protection Agency (EPA) to better understand the measurement, sources, and health effects of suspended particulate matter (PM). The overall goals were to characterize the composition and identify the sources of particulate matter in Southeastern Texas, to develop and test new methods for characterizing fine particulate matter, and to collect data on the physical and chemical characterization of fine particulate matter that can be used to support exposure and health effects studies.\r\n\r\nNARSTO, which has since disbanded, was a public/private partnership, whose membership spanned across government, utilities, industry, and academe throughout Mexico, the United States, and Canada. The primary mission was to coordinate and enhance policy-relevant scientific research and assessment of tropospheric pollution behavior; activities provide input for science-based decision-making and determination of workable, efficient, and effective strategies for local and regional air-pollution management. Data products from local, regional, and international monitoring and research programs are still available.",
-            "title": "NARSTO EPA Supersite (SS) Houston, Texas Air Quality Study 2000 (TexAQS2000) Department of Energy (DOE) G-1 Air Chemistry, Aerosol, and Met Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDCDAAC%2FNARSTO%2F0040",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDCDAAC%2FNARSTO%2F0040",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2338588309-LARC_ASDC",
-                    "description": "Earthdata Search for NARSTO_EPA_SS_HOUSTON_TEXAQS2000_DOE_G-1_DATA_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for NARSTO_EPA_SS_HOUSTON_TEXAQS2000_DOE_G-1_DATA_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2338588309-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0040",
-                    "description": "DOI data set landing page for NARSTO_EPA_SS_HOUSTON_TEXAQS2000_DOE_G-1_DATA_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for NARSTO_EPA_SS_HOUSTON_TEXAQS2000_DOE_G-1_DATA_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0040",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/guide/narsto_epa_ss_houston_texaqs2000_doe_g-1_data.pdf",
-                    "description": "Guide for NARSTO EPA_SS_HOUSTONTEXAQS2000 DOE G-1 Air Chemistry, Aerosol, and Met Data",
                     "@type": "dcat:Distribution",
+                    "description": "Guide for NARSTO EPA_SS_HOUSTONTEXAQS2000 DOE G-1 Air Chemistry, Aerosol, and Met Data",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/guide/narsto_epa_ss_houston_texaqs2000_doe_g-1_data.pdf",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/EPA_SS_Houston_Project_Plan.pdf",
-                    "description": "Quality Assurance Project Plan for the Gulf Coast Aerosol Research and Characterization Program (GC-ARCH): Houston Supersite, June 2000",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Assurance Project Plan for the Gulf Coast Aerosol Research and Characterization Program (GC-ARCH): Houston Supersite, June 2000",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/EPA_SS_Houston_Project_Plan.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/readme_narsto_epa_ss_houston_texaqs2000_doe_g-1_data_hydrocarbons_v1.txt",
-                    "description": "HYDROCARBON_V1 ; Excerpt from Final Results BKHVN 2004.xls Readme (.xlx)",
                     "@type": "dcat:Distribution",
+                    "description": "HYDROCARBON_V1 ; Excerpt from Final Results BKHVN 2004.xls Readme (.xlx)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/readme_narsto_epa_ss_houston_texaqs2000_doe_g-1_data_hydrocarbons_v1.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/vnd.google-earth.kmz",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/EPA_Supersites.kmz",
-                    "description": "EPA Supersites - Direct File Download (.kmz)",
                     "@type": "dcat:Distribution",
+                    "description": "EPA Supersites - Direct File Download (.kmz)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/EPA_Supersites.kmz",
+                    "mediaType": "application/vnd.google-earth.kmz",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/NARSTO/EPA_SS_HOUSTON_TEXAQS2000_DOE_G-1_DATA_1/",
-                    "description": "ASDC Direct Data Download for NARSTO_EPA_SS_HOUSTON_TEXAQS2000_DOE_G-1_DATA_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for NARSTO_EPA_SS_HOUSTON_TEXAQS2000_DOE_G-1_DATA_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/NARSTO/EPA_SS_HOUSTON_TEXAQS2000_DOE_G-1_DATA_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2338588309-LARC_ASDC",
+            "issued": "2003-09-09",
+            "keyword": [
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "atmospheric radiation",
+                "atmospheric winds",
+                "atmospheric pressure",
+                "aerosols",
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0040",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>28.46 -97.45 28.46 -94.47 31.68 -94.47 31.68 -97.45 28.46 -97.45</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2000-08-19T00:00:00Z/2000-09-12T23:59:59.999Z",
             "theme": [
                 "NARSTO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NARSTO EPA Supersite (SS) Houston, Texas Air Quality Study 2000 (TexAQS2000) Department of Energy (DOE) G-1 Air Chemistry, Aerosol, and Met Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-CAL-ROMAP-3-CR5-SPM-V1.0",
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
+            "description": "This archive contains level 3 data from the ROMAP SPM instrument onboard ROSETTA Lander, acquired during the CR5 (cruise 5) phase. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-cal-romap-3-cr5-spm-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "calibration"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-CAL-ROMAP-3-CR5-SPM-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-cal-romap-3-cr5-spm-v1.0",
-            "description": "This archive contains level 3 data from the ROMAP SPM instrument onboard ROSETTA Lander, acquired during the CR5 (cruise 5) phase. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER CAL ROMAP 3 CR5 SPM V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-LANDER CAL ROMAP 3 CR5 SPM V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A%2FCAL-ALICE-4-AST2-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains CODMAC level 4 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the Lutetia flyby mission phase, which took place between 2010-06-07 and 2010-09-10.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-cal-alice-4-ast2-v1.0_p47s-srek",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "calibration",
                 "21 lutetia"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A%2FCAL-ALICE-4-AST2-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-cal-alice-4-ast2-v1.0_p47s-srek",
-            "description": "This data set contains CODMAC level 4 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the Lutetia flyby mission phase, which took place between 2010-06-07 and 2010-09-10.",
-            "title": "ROSETTA-ORBITER LUTETIA/CAL ALICE 4 AST2 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER LUTETIA/CAL ALICE 4 AST2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2566342407-LARC_ASDC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2023-05-31. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC.",
-            "issued": "2022-10-17",
-            "temporal": "2022-07-14T00:00:00Z/2022-09-14T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-11-22",
-            "keyword": [
-                "earth science",
-                "atmospheric chemistry",
-                "atmosphere",
-                "atmospheric water vapor"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Andrew Rollins",
                 "hasEmail": "mailto:andrew.rollins@noaa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2566342407-LARC_ASDC",
             "description": "ACCLIP_TraceGas_AircraftInSitu_WB57_Data is the in-situ trace gas data collection during the Asian Summer Monsoon Chemical & Climate Impact Project (ACCLIP). Data from the Airborne Carbon Oxide Sulfide Spectrometer (ACOS), Carbon monOxide Measurement from Ames (COMA), Laser Induced Fluorescence - Nitrogen Oxide (LIF-NO), In Situ Airborne Formaldehyde (ISAF), Carbon Oxide Laser Detector 2 (COLD 2), and the NOAA UAS O3 Photometer (UASO3) is featured in this collection. Data collection for this product is complete.\r\n\r\nACCLIP is an international, multi-organizational suborbital campaign that aims to study aerosols and chemical transport that is associated with the Asian Summer Monsoon (ASM) in the Western Pacific region from 15 July 2022 to 31 August 2022. The ASM is the largest meteorological pattern in the Northern Hemisphere (NH) during the summer and is associated with persistent convection and large anticyclonic flow patterns in the upper troposphere and lower stratosphere (UTLS). This leads to significant enhancements in the UTLS of trace species that originate from pollution or biomass burning. Convection connected to the ASM occurs over South, Southeast, and East Asia, a region with complex and rapidly changing emissions due to its high population density and economic growth. Pollution that reaches the UTLS from this region can have significant effects on the climate and chemistry of the atmosphere, making it important to have an accurate representation and understanding of ASM transport, chemical, and microphysical processes for chemistry-climate models to characterize these interactions and for predicting future impacts on climate.\r\n\r\nThe ACCLIP campaign is conducted by the National Aeronautics and Space Administration (NASA) and the National Center for Atmospheric Research (NCAR) with the primary goal of investigating the impacts of Asian gas and aerosol emissions on global chemistry and climate. The NASA WB-57 and NCAR G-V aircraft are outfitted with state-of-the-art sensors to accomplish this. ACCLIP seeks to address four scientific objectives related to its main goal. The first is to investigate the transport pathways of ASM uplifted air from inside of the anticyclone to the global UTLS. Another objective is to sample the chemical content of air processed in the ASM in order to quantify the role of the ASM in transporting chemically active species and short-lived climate forcing agents to the UTLS to determine their impact on stratospheric ozone chemistry and global climate. Third, information is obtained on aerosol size, mass, and chemical composition that is necessary for determining the radiative effects of the ASM to constrain models of aerosol formation and for contrasting the organic-rich ASM UTLS aerosol population with that of the background aerosols. Last, ACCLIP seeks to measure the water vapor distribution associated with the monsoon dynamical structure to evaluate transport across the tropopause and determine the role of the ASM in water vapor transport in the stratosphere.",
-            "title": "ACCLIP WB-57 Aircraft In-situ Trace Gas Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/acclip/index.html",
-                    "description": "ACCLIP Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "ACCLIP Project Home Page",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/acclip/index.html",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/acclip/content/ACCLIP",
-                    "description": "ACCLIP ESPO Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "ACCLIP ESPO Home Page",
+                    "downloadURL": "https://espo.nasa.gov/acclip/content/ACCLIP",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www2.acom.ucar.edu/acclip",
-                    "description": "ACCLIP NCAR Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "ACCLIP NCAR Home Page",
+                    "downloadURL": "https://www2.acom.ucar.edu/acclip",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/ACCLIP/TraceGas_AircraftInSitu_WB57_Data_1/",
-                    "description": "ASDC Direct Data Download for ACCLIP_TraceGas_AircraftInSitu_WB57_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for ACCLIP_TraceGas_AircraftInSitu_WB57_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/ACCLIP/TraceGas_AircraftInSitu_WB57_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2566342407-LARC_ASDC",
+            "issued": "2022-10-17",
+            "keyword": [
+                "earth science",
+                "atmospheric chemistry",
+                "atmosphere",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2566342407-LARC_ASDC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-11-22",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>16.6 -180.0 16.6 180.0 61.5 180.0 61.5 -180.0 16.6 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2022-07-14T00:00:00Z/2022-09-14T23:59:59.999Z",
             "theme": [
                 "ACCLIP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ACCLIP WB-57 Aircraft In-situ Trace Gas Data"
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
+            "description": "Shock Wave / Turbulent Boundary Layer Flows at High Mach Numbers. This web page provides data from experiments that may be useful for the validation of turbulence models. This resource is expected to grow gradually over time. All data herein arepublicly available.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.cubrc.org/_iassets/docs/LENS2-largeconeflare.xlsx",
+                    "mediaType": "application/xlsx"
+                }
             ],
+            "identifier": "NASA-850__3",
+            "issued": "2018-06-25",
             "keyword": [
                 "shockwave",
                 "layer",
@@ -1171660,300 +1171669,302 @@
                 "turbulence",
                 "mach"
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
-            "identifier": "NASA-850__3",
-            "description": "Shock Wave / Turbulent Boundary Layer Flows at High Mach Numbers. This web page provides data from experiments that may be useful for the validation of turbulence models. This resource is expected to grow gradually over time. All data herein arepublicly available.",
-            "title": "Turbulence Models: Data from Other Experiments:  Shock Wave / Turbulent Boundary Layer Flows at High Mach Numbers",
-            "programCode": [
-                "026:023"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.cubrc.org/_iassets/docs/LENS2-largeconeflare.xlsx",
-                    "mediaType": "application/xlsx"
-                }
+            "references": [
+                "http://turbmodels.larc.nasa.gov/index.html"
             ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Aerospace"
-            ]
+            ],
+            "title": "Turbulence Models: Data from Other Experiments:  Shock Wave / Turbulent Boundary Layer Flows at High Mach Numbers"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1654",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Numata, I., S.S. da Silva, and M.A. Cochrane. 2018. Forest Inventories and DBH at Burned and Unburned Forest Sites, Acre, Brazil, 2017. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1654",
-            "issued": "2018-12-28",
-            "temporal": "2017-10-07T00:00:00Z/2017-12-13T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-11",
-            "keyword": [
-                "natural hazards",
-                "vegetation",
-                "biosphere",
-                "human dimensions",
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
-            "identifier": "C2764878430-ORNL_CLOUD",
             "description": "This data set provides measurements of diameter at breast height (DBH) and species identification at four forest sites in the eastern side of Acre, Brazil including Bonal (A), Catuaba (B), Humaita (C) and Transacreana (D). The inventory locations include forests burned in 2005 and 2010 and nearby unburned areas. Inventory surveys were conducted in October and December 2017.",
-            "graphic-preview-description": "Photos taken in 2017 of Bonal measurement area (Area A, Transect 8, burned 2005) and Catuaba area (Area B, unburned). Photos courtesy of I. Numata.",
-            "title": "Forest Inventories and DBH at Burned and Unburned Forest Sites, Acre, Brazil, 2017",
-            "graphic-preview-file": "https://daac.ornl.gov/VEGETATION/guides/Forest_Inventory_Acre_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1654",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1654",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/Forest_Inventory_Acre_Brazil/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/Forest_Inventory_Acre_Brazil/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/Forest_Inventory_Acre_Brazil.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/Forest_Inventory_Acre_Brazil.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1654",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1654",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/vnd.google-earth.kmz",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/Forest_Inventory_Acre_Brazil/comp/acre_forest_inventory_plots_2017.kmz",
-                    "description": "Forest Inventories and DBH at Burned and Unburned Forest Sites, Acre, Brazil, 2017: acre_forest_inventory_plots_2017.kmz",
                     "@type": "dcat:Distribution",
+                    "description": "Forest Inventories and DBH at Burned and Unburned Forest Sites, Acre, Brazil, 2017: acre_forest_inventory_plots_2017.kmz",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/Forest_Inventory_Acre_Brazil/comp/acre_forest_inventory_plots_2017.kmz",
+                    "mediaType": "application/vnd.google-earth.kmz",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/Forest_Inventory_Acre_Brazil/comp/Bonal_unburned_area.JPG",
-                    "description": "Forest Inventories and DBH at Burned and Unburned Forest Sites, Acre, Brazil, 2017: Bonal_unburned_area.JPG",
                     "@type": "dcat:Distribution",
+                    "description": "Forest Inventories and DBH at Burned and Unburned Forest Sites, Acre, Brazil, 2017: Bonal_unburned_area.JPG",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/Forest_Inventory_Acre_Brazil/comp/Bonal_unburned_area.JPG",
+                    "mediaType": "image/jpeg",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/Forest_Inventory_Acre_Brazil/comp/Catuaba_unburned_area1.JPG",
-                    "description": "Forest Inventories and DBH at Burned and Unburned Forest Sites, Acre, Brazil, 2017: Catuaba_unburned_area1.JPG",
                     "@type": "dcat:Distribution",
+                    "description": "Forest Inventories and DBH at Burned and Unburned Forest Sites, Acre, Brazil, 2017: Catuaba_unburned_area1.JPG",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/Forest_Inventory_Acre_Brazil/comp/Catuaba_unburned_area1.JPG",
+                    "mediaType": "image/jpeg",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/Forest_Inventory_Acre_Brazil/comp/Forest_Inventory_Acre_Brazil.pdf",
-                    "description": "Forest Inventories and DBH at Burned and Unburned Forest Sites, Acre, Brazil, 2017: Forest_Inventory_Acre_Brazil.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Forest Inventories and DBH at Burned and Unburned Forest Sites, Acre, Brazil, 2017: Forest_Inventory_Acre_Brazil.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/Forest_Inventory_Acre_Brazil/comp/Forest_Inventory_Acre_Brazil.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/Forest_Inventory_Acre_Fig1.png",
-                    "description": "Photos taken in 2017 of Bonal measurement area (Area A, Transect 8, burned 2005) and Catuaba area (Area B, unburned). Photos courtesy of I. Numata.",
                     "@type": "dcat:Distribution",
+                    "description": "Photos taken in 2017 of Bonal measurement area (Area A, Transect 8, burned 2005) and Catuaba area (Area B, unburned). Photos courtesy of I. Numata.",
+                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/Forest_Inventory_Acre_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Photos taken in 2017 of Bonal measurement area (Area A, Transect 8, burned 2005) and Catuaba area (Area B, unburned). Photos courtesy of I. Numata.",
+            "graphic-preview-file": "https://daac.ornl.gov/VEGETATION/guides/Forest_Inventory_Acre_Fig1.png",
+            "identifier": "C2764878430-ORNL_CLOUD",
+            "issued": "2018-12-28",
+            "keyword": [
+                "natural hazards",
+                "vegetation",
+                "biosphere",
+                "human dimensions",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1654",
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
             "spatial": "-68.15 -10.08 -67.28 -9.75",
+            "temporal": "2017-10-07T00:00:00Z/2017-12-13T23:59:59Z",
             "theme": [
                 "Vegetation",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Forest Inventories and DBH at Burned and Unburned Forest Sites, Acre, Brazil, 2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/LPVEX/RADAR/DATA201",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Moisseev, Dmitri N.2020. GPM Ground Validation C-band Kerava (KER) Radar LPVEx [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/LPVEX/RADAR/DATA201",
-            "issued": "2020-04-29",
-            "temporal": "2010-09-01T00:00:00Z/2011-01-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-20",
-            "keyword": [
-                "earth science",
-                "spectral/engineering",
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
-            "identifier": "C1995569709-GHRC_DAAC",
             "description": "The GPM Ground Validation C-Band Radar LPVEx datasets include radar reflectivity data from the Kerava (KER) dual-polarimetric C-Band Doppler radar in Finland during the Global Precipitation Measurement (GPM) mission Light Precipitation Validation Experiment (LPVEx) field campaign. This radar, along with four others, provided reflectivity measurements for light precipitation systems during LPVEx. This field campaign took place around the Gulf of Finland, aiming to provide additional high-latitude, light rainfall measurements for the improvement of GPM satellite precipitation algorithms. The Kerava C-Band Radar data files are available in RAW and UF format from  September 21 through October 20, 2010.",
-            "title": "GPM Ground Validation C-band Kerava (KER) Radar LPVEx V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FLPVEX%2FRADAR%2FDATA201",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FLPVEX%2FRADAR%2FDATA201",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmkerlpvex",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmkerlpvex",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
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
-                    "downloadURL": "https://ntrs.nasa.gov/search.jsp?R=20110015768",
-                    "description": "The NASA CloudSat/GPM Light Precipitation Validation Experiment (LPVEx)",
                     "@type": "dcat:Distribution",
+                    "description": "The NASA CloudSat/GPM Light Precipitation Validation Experiment (LPVEx)",
+                    "downloadURL": "https://ntrs.nasa.gov/search.jsp?R=20110015768",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/GPMGV/LPVEX/DATA101",
-                    "description": "LPVEx Field Campaign Collection DOI",
                     "@type": "dcat:Distribution",
+                    "description": "LPVEx Field Campaign Collection DOI",
+                    "downloadURL": "https://doi.org/10.5067/GPMGV/LPVEX/DATA101",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.atm.helsinki.fi/UH_RADAR/sites.html",
-                    "description": "Instrument Information",
                     "@type": "dcat:Distribution",
+                    "description": "Instrument Information",
+                    "downloadURL": "https://www.atm.helsinki.fi/UH_RADAR/sites.html",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/lpvex/C-band_radar/doc/lpvexradar_datasets.pdf",
-                    "description": "GPM Ground Validation C-Band Radar LPVEx User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "GPM Ground Validation C-Band Radar LPVEx User Guide",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/lpvex/C-band_radar/doc/lpvexradar_datasets.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.researchgate.net/publication/280623315_Quality_Assurance_in_the_FMI_Doppler_Weather_Radar_Network",
-                    "description": "Quality Assurance in the FMI Doppler Weather Radar Network",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Assurance in the FMI Doppler Weather Radar Network",
+                    "downloadURL": "https://www.researchgate.net/publication/280623315_Quality_Assurance_in_the_FMI_Doppler_Weather_Radar_Network",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/lpvex",
-                    "description": "LPVEx Field Campaign Project Homepage",
                     "@type": "dcat:Distribution",
+                    "description": "LPVEx Field Campaign Project Homepage",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/lpvex",
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
+            "identifier": "C1995569709-GHRC_DAAC",
+            "issued": "2020-04-29",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "radar"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/LPVEX/RADAR/DATA201",
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
             "spatial": "20.565 58.142 29.663 62.634",
+            "temporal": "2010-09-01T00:00:00Z/2011-01-31T23:59:59Z",
             "theme": [
                 "LPVEX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM Ground Validation C-band Kerava (KER) Radar LPVEx V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-GRAND-5-CERES-IRON_MAP_V1.0",
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
-                "1 ceres"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "A global map of the                      concentration of iron within the regolith of asteroid 1 Ceres           on twenty-degree quasi-equal-area pixels is provided. Iron              concentrations were determined from gamma ray counting data acquired    by Dawn's Gamma Ray and Neutron Detector (GRaND) in a low altitude      mapping orbit, about 385 km from Ceres' surface (about 0.8 body radii   altitude). The concentrations are representative of Ceres's bulk        regolith to depths up to a few decimeters with a spatial resolution     of about 600-km full-width-at-half-maximum of arc length on the         surface. The methods used to determine iron concentration are           described by PRETTYMANETAL2017.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-grand-5-ceres-iron_map_v1.0_p4cg-bav2",
+            "issued": "2018-06-26",
+            "keyword": [
+                "dawn mission to vesta and ceres",
+                "1 ceres"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-GRAND-5-CERES-IRON_MAP_V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-grand-5-ceres-iron_map_v1.0_p4cg-bav2",
-            "description": "A global map of the                      concentration of iron within the regolith of asteroid 1 Ceres           on twenty-degree quasi-equal-area pixels is provided. Iron              concentrations were determined from gamma ray counting data acquired    by Dawn's Gamma Ray and Neutron Detector (GRaND) in a low altitude      mapping orbit, about 385 km from Ceres' surface (about 0.8 body radii   altitude). The concentrations are representative of Ceres's bulk        regolith to depths up to a few decimeters with a spatial resolution     of about 600-km full-width-at-half-maximum of arc length on the         surface. The methods used to determine iron concentration are           described by PRETTYMANETAL2017.",
-            "title": "DAWN GRAND MAP CERES IRON MAP V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "DAWN GRAND MAP CERES IRON MAP V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/p4d4-u4t3",
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
+                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_iir_l2_track-beta-v2-02_table",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000137",
             "issued": "2018-06-25",
-            "temporal": "2008-09-14/2011-01-17",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "aerosol",
                 "atmospheric science",
@@ -1171963,867 +1171974,833 @@
                 "radiation",
                 "satellite"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John M. Kusterer",
-                "hasEmail": "mailto:john.m.kusterer@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/p4d4-u4t3",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:004"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000137",
-            "description": "Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) was launched on April 28, 2006 to study the impact of clouds and aerosols on the Earth\u2019s radiation budget and climate. It flies in formation with five other satellites in the international \u201cA-Train\u201d (PDF) constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments, the Cloud-Aerosol LIdar with Orthogonal Polarization (CALIOP), the Imaging Infrared Radiometer (IIR), and the Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES. These data consist of half orbit (Night and Day) emissivity and cloud particle data related to pixels that have been co-located to the Lidar track.",
-            "title": "CALIPSO Imaging Infrared Radiometer L2 Data Track V2-02",
-            "programCode": [
-                "026:004"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_iir_l2_track-beta-v2-02_table",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
+            "temporal": "2008-09-14/2011-01-17",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CALIPSO Imaging Infrared Radiometer L2 Data Track V2-02"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MCD19A2.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Alexei Lyapustin, Yujie Wang. 2022-07-06. MODIS/Terra+Aqua Land Aerosol Optical Depth Daily L2G Global 1km SIN Grid V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MCD19A2.061. https://doi.org/10.5067/MODIS/MCD19A2.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2022-07-06",
-            "temporal": "2000-02-24T00:00:00Z/2024-06-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-07-06",
-            "keyword": [
-                "national geospatial data asset",
-                "earth science",
-                "ngda",
-                "atmosphere",
-                "aerosols"
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
-            "identifier": "C2324689816-LPCLOUD",
-            "description": "The MCD19A2 Version 6.1 data product is a Moderate Resolution Imaging Spectroradiometer (MODIS) Terra and Aqua combined Multi-angle Implementation of Atmospheric Correction (MAIAC) Land Aerosol Optical Depth (AOD) gridded Level 2 product produced daily at 1 kilometer (km) pixel resolution. The MCD19A2 product provides the atmospheric properties and view geometry used to calculate the MAIAC Land Surface Bidirectional Reflectance Factor (BRF) or surface reflectance, MCD19A1 product.\r\n\r\nThe MCD19A2 AOD data product contains the following Science Dataset (SDS) layers: blue band AOD at 0.47 \u00b5m, green band AOD at 0.55 \u00b5m, AOD uncertainty, fine mode fraction over water, column water vapor over land and clouds (in cm), smoke injection height (m above ground), AOD QA, AOD model at 1km, cosine of solar zenith angle, cosine of view zenith angle, relative azimuth angle, scattering angle, and glint angle at 5km. A low-resolution browse image is also included showing AOD of the blue band at 0.47 \u00b5m created using a composite of all available orbits.\r\n\r\nEach SDS layer within each MCD19A2 Hierarchical Data Format 4 (HDF4) file contains a third dimension that represents the number of orbit overpasses. This factor could affect the total number of bands for each SDS layer.\r\n\r\nValidation at stage 1 (https://landweb.modaps.eosdis.nasa.gov/cgi-bin/QA_WWW/newPage.cgi?fileName=maturity) has been achieved for the AOD SDS layers. Further details regarding MODIS land product validation for MCD19 data products are available from the MODIS Land Team Validation site (https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD19).\r\n\r\nImprovements/Changes from Previous Versions\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).\r\n* The MCD19 Version 6.1 products have added 250 m resolution bands.\r\n* The previous BRDF product (MCD19A3) was reported once every eight days and the new MCD19A3D is a daily product.\r\n* MCD19A3D introduces gap-filled NDVI and gap-filled 250 m NBAR. \r\n* Snow Fraction, Snow Fit, and Snow Grain size layers were moved from MCD19A1 to the MCD19A3D.\r\n* There are four additional Climate Modeling Grid (CMG) products: MCD19A1CMGL, MCD19A1GO, MCD19A2CMG, and MCD19A3CMG.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "graphic-preview-description": "Browse image for Earthdata Search.",
             "creator": "Alexei Lyapustin, Yujie Wang",
-            "title": "MODIS/Terra+Aqua Land Aerosol Optical Depth Daily L2G Global 1km SIN Grid V061",
-            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2336273307-LPCLOUD?h=500&w=500",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MCD19A2 Version 6.1 data product is a Moderate Resolution Imaging Spectroradiometer (MODIS) Terra and Aqua combined Multi-angle Implementation of Atmospheric Correction (MAIAC) Land Aerosol Optical Depth (AOD) gridded Level 2 product produced daily at 1 kilometer (km) pixel resolution. The MCD19A2 product provides the atmospheric properties and view geometry used to calculate the MAIAC Land Surface Bidirectional Reflectance Factor (BRF) or surface reflectance, MCD19A1 product.\r\n\r\nThe MCD19A2 AOD data product contains the following Science Dataset (SDS) layers: blue band AOD at 0.47 \u00b5m, green band AOD at 0.55 \u00b5m, AOD uncertainty, fine mode fraction over water, column water vapor over land and clouds (in cm), smoke injection height (m above ground), AOD QA, AOD model at 1km, cosine of solar zenith angle, cosine of view zenith angle, relative azimuth angle, scattering angle, and glint angle at 5km. A low-resolution browse image is also included showing AOD of the blue band at 0.47 \u00b5m created using a composite of all available orbits.\r\n\r\nEach SDS layer within each MCD19A2 Hierarchical Data Format 4 (HDF4) file contains a third dimension that represents the number of orbit overpasses. This factor could affect the total number of bands for each SDS layer.\r\n\r\nValidation at stage 1 (https://landweb.modaps.eosdis.nasa.gov/cgi-bin/QA_WWW/newPage.cgi?fileName=maturity) has been achieved for the AOD SDS layers. Further details regarding MODIS land product validation for MCD19 data products are available from the MODIS Land Team Validation site (https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD19).\r\n\r\nImprovements/Changes from Previous Versions\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).\r\n* The MCD19 Version 6.1 products have added 250 m resolution bands.\r\n* The previous BRDF product (MCD19A3) was reported once every eight days and the new MCD19A3D is a daily product.\r\n* MCD19A3D introduces gap-filled NDVI and gap-filled 250 m NBAR. \r\n* Snow Fraction, Snow Fit, and Snow Grain size layers were moved from MCD19A1 to the MCD19A3D.\r\n* There are four additional Climate Modeling Grid (CMG) products: MCD19A1CMGL, MCD19A1GO, MCD19A2CMG, and MCD19A3CMG.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD19A2.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD19A2.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD19A2.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD19A2.061",
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
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD19A2.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD19A2.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2324689816-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2324689816-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/MCD19A2.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/MCD19A2.061/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/111/MCD19_ATBD.pdf",
-                    "description": "The Algorithm Theoretical Basis Document (ATBD) describes the physical and mathematical algorithms for the product.",
                     "@type": "dcat:Distribution",
+                    "description": "The Algorithm Theoretical Basis Document (ATBD) describes the physical and mathematical algorithms for the product.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/111/MCD19_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1500/MCD19_User_Guide_V61.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1500/MCD19_User_Guide_V61.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MCD19A2",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MCD19A2",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MCD19",
-                    "description": "Further details regarding MODIS land product validation for the MCD19 data products are available from the MODIS Land Team Validation site.",
                     "@type": "dcat:Distribution",
+                    "description": "Further details regarding MODIS land product validation for the MCD19 data products are available from the MODIS Land Team Validation site.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MCD19",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/MODLAND_val.html",
-                    "description": "Validation at stage 1 has been achieved for the MODIS MAIAC products.",
                     "@type": "dcat:Distribution",
+                    "description": "Validation at stage 1 has been achieved for the MODIS MAIAC products.",
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
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2336273307-LPCLOUD?h=500&w=500",
-                    "description": "Browse image for Earthdata Search.",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2336273307-LPCLOUD?h=500&w=500",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search.",
+            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2336273307-LPCLOUD?h=500&w=500",
+            "identifier": "C2324689816-LPCLOUD",
+            "issued": "2022-07-06",
+            "keyword": [
+                "national geospatial data asset",
+                "earth science",
+                "ngda",
+                "atmosphere",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MCD19A2.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-07-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
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
+            "title": "MODIS/Terra+Aqua Land Aerosol Optical Depth Daily L2G Global 1km SIN Grid V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TIGR5-V1.0",
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
-                "titan"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Cassini Radio Science Titan Gravity Science Experiment (TIGR5) Raw Data Archive is a time-ordered collection of radio science raw data acquired on July 1 and 3, 2006 during the Tour subphase of the Cassini mission. DATA_SET_DESC =",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tigr5-v1.0_p4et-f9dv",
+            "issued": "2018-06-26",
+            "keyword": [
+                "cassini-huygens",
+                "titan"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TIGR5-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tigr5-v1.0_p4et-f9dv",
-            "description": "The Cassini Radio Science Titan Gravity Science Experiment (TIGR5) Raw Data Archive is a time-ordered collection of radio science raw data acquired on July 1 and 3, 2006 during the Tour subphase of the Cassini mission. DATA_SET_DESC =",
-            "title": "CASSINI RSS RAW DATA SET - TIGR5 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI RSS RAW DATA SET - TIGR5 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-APD-POLARIMETRY-V2.0",
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
+            "description": "The Asteroid Polarimetric Database (APD) is compiled by Dmitrij Lupishko of Kharkov University. This database tabulates the original data comprising degree of polarization as a function of phase angle of the asteroid, and additional parameters where available. This data set, together with 'polar.tab' containing the TRIAD polarimetry, includes most if not all existing asteroid polarimetry data published by 1996. The APD is an ongoing compilation and this data set will be updated yearly.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-apd-polarimetry-v2.0_p4fc-2xkz",
+            "issued": "2018-06-26",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-APD-POLARIMETRY-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-apd-polarimetry-v2.0_p4fc-2xkz",
-            "description": "The Asteroid Polarimetric Database (APD) is compiled by Dmitrij Lupishko of Kharkov University. This database tabulates the original data comprising degree of polarization as a function of phase angle of the asteroid, and additional parameters where available. This data set, together with 'polar.tab' containing the TRIAD polarimetry, includes most if not all existing asteroid polarimetry data published by 1996. The APD is an ongoing compilation and this data set will be updated yearly.",
-            "title": "ASTEROID POLARIMETRIC DATABASE V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ASTEROID POLARIMETRIC DATABASE V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4WH2MXH",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for International Earth Science Information Network - CIESIN - Columbia University. 2015-01-21. Population Exposure Estimates in Proximity to Nuclear Power Plants, Locations. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H4WH2MXH. https://doi.org/10.7927/H4WH2MXH.",
-            "issued": "2015-01-21",
-            "temporal": "1956-01-01T00:00:00Z/2012-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-01-21",
-            "references": [
-                "https://doi.org/10.7927/H41834D6"
-            ],
-            "keyword": [
-                "human dimensions",
-                "environmental impacts",
-                "earth science",
-                "public health",
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
-            "identifier": "C1000000480-SEDAC",
-            "description": "The Population Exposure Estimates in Proximity to Nuclear Power Plants, Locations data set combines information from a global data set developed by Declan Butler of Nature News and the Power Reactor Information System (PRIS), an up-to-date database of nuclear reactors maintained by the International Atomic Energy Agency (IAEA). The locations of nuclear reactors around the world are represented as point features associated with reactor specification and performance history attributes as of March 2012.",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Center for International Earth Science Information Network - CIESIN - Columbia University",
-            "title": "Population Exposure Estimates in Proximity to Nuclear Power Plants, Locations",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/energy/energy-pop-exposure-nuclear-plants-locations/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Population Exposure Estimates in Proximity to Nuclear Power Plants, Locations data set combines information from a global data set developed by Declan Butler of Nature News and the Power Reactor Information System (PRIS), an up-to-date database of nuclear reactors maintained by the International Atomic Energy Agency (IAEA). The locations of nuclear reactors around the world are represented as point features associated with reactor specification and performance history attributes as of March 2012.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4WH2MXH",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4WH2MXH",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/energy/energy-pop-exposure-nuclear-plants-locations/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/energy/energy-pop-exposure-nuclear-plants-locations/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/energy-pop-exposure-nuclear-plants-locations/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/energy-pop-exposure-nuclear-plants-locations/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/energy-pop-exposure-nuclear-plants-locations/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/energy-pop-exposure-nuclear-plants-locations/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/energy-pop-exposure-nuclear-plants-locations/maps/services",
-                    "description": "Web Map Service Page",
                     "@type": "dcat:Distribution",
+                    "description": "Web Map Service Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/energy-pop-exposure-nuclear-plants-locations/maps/services",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/energy-pop-exposure-nuclear-plants-locations",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/energy-pop-exposure-nuclear-plants-locations",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/energy/energy-pop-exposure-nuclear-plants-locations/sedac-logo.jpg",
+            "identifier": "C1000000480-SEDAC",
+            "issued": "2015-01-21",
+            "keyword": [
+                "human dimensions",
+                "environmental impacts",
+                "earth science",
+                "public health",
+                "population"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4WH2MXH",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-01-21",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H41834D6"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-124.21 -34.0 166.45 68.05",
+            "temporal": "1956-01-01T00:00:00Z/2012-12-31T00:00:00Z",
             "theme": [
                 "ENERGY",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Population Exposure Estimates in Proximity to Nuclear Power Plants, Locations"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT5-3704-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2015-01-01 to 2016-12-31. It is a Occultation measurement and covers the time 2015-03-03T02:33:01 to 2015-03-03T08:17:05.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext5-3704-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars express",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT5-3704-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext5-3704-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2015-01-01 to 2016-12-31. It is a Occultation measurement and covers the time 2015-03-03T02:33:01 to 2015-03-03T08:17:05.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 5 3704 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 5 3704 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-UVS-0--SL9-NULL-RESULTS-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "A preliminary examination of the Ultraviolet Spectrometer (UVS) data revealed no obvious detections of anything which might correspond with the impact phenomena. In order to investigate the possibility that more subtle impact-related events were present in the data and to establish a formal statistical upper limit for the non-detection of the impacts, we performed a statistical analysis as described in the DPS poster paper 'Voyager 2 UVS Observations of Jupiter During the Comet Shoemaker-Levy 9 Impact Events', by R. J. Vervack et al. [VERVACKETAL1995]",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-uvs-0--sl9-null-results-v1.0_p4iz-s3in",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "voyager",
                 "sl9",
                 "jupiter",
                 "comet sl9/jupiter collision"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-UVS-0--SL9-NULL-RESULTS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-uvs-0--sl9-null-results-v1.0_p4iz-s3in",
-            "description": "A preliminary examination of the Ultraviolet Spectrometer (UVS) data revealed no obvious detections of anything which might correspond with the impact phenomena. In order to investigate the possibility that more subtle impact-related events were present in the data and to establish a formal statistical upper limit for the non-detection of the impacts, we performed a statistical analysis as described in the DPS poster paper 'Voyager 2 UVS Observations of Jupiter During the Comet Shoemaker-Levy 9 Impact Events', by R. J. Vervack et al. [VERVACKETAL1995]",
-            "title": "VOYAGER 2 JUPITER/SHOEMAKER-LEVY 9 UVS NULL RESULTS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VOYAGER 2 JUPITER/SHOEMAKER-LEVY 9 UVS NULL RESULTS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/569",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Global Soil Data Task Group. 2000. Global Gridded Surfaces of Selected Soil Characteristics (IGBP-DIS) . ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/569",
-            "issued": "2022-02-14",
-            "temporal": "1950-01-01T00:00:00Z/1996-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "earth science",
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
-            "identifier": "C2216863098-ORNL_CLOUD",
             "description": "Global data-surfaces pre-generated by  SoilData, at a resolution of 5x5 arc-minutes, in ASCII GRID format for ARC INFO, and for the soil depth interval 0-100 cm.",
-            "graphic-preview-description": "Browse Image",
-            "title": "Global Gridded Surfaces of Selected Soil Characteristics (IGBP-DIS)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/567_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F569",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F569",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/global_soil/IGBP-SurfaceProducts/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/global_soil/IGBP-SurfaceProducts/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/SOILS/guides/IGBP-SurfaceProducts.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/SOILS/guides/IGBP-SurfaceProducts.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/569",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/569",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/IGBP-SurfaceProducts/comp/bk.jpg",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/IGBP-SurfaceProducts/comp/bk.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/IGBP-SurfaceProducts/comp/fc.jpg",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/IGBP-SurfaceProducts/comp/fc.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/IGBP-SurfaceProducts/comp/IGBP-SurfaceProducts.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/IGBP-SurfaceProducts/comp/IGBP-SurfaceProducts.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/IGBP-SurfaceProducts/comp/pawc.jpg",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/IGBP-SurfaceProducts/comp/pawc.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/IGBP-SurfaceProducts/comp/readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/IGBP-SurfaceProducts/comp/readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/IGBP-SurfaceProducts/comp/README_images",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/IGBP-SurfaceProducts/comp/README_images",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/IGBP-SurfaceProducts/comp/sc.jpg",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/IGBP-SurfaceProducts/comp/sc.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/IGBP-SurfaceProducts/comp/tc.jpg",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/IGBP-SurfaceProducts/comp/tc.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/IGBP-SurfaceProducts/comp/tn.jpg",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/IGBP-SurfaceProducts/comp/tn.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/IGBP-SurfaceProducts/comp/wp.jpg",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/IGBP-SurfaceProducts/comp/wp.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/567_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/567_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=569",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=569",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/567_1_fit.png",
+            "identifier": "C2216863098-ORNL_CLOUD",
+            "issued": "2022-02-14",
+            "keyword": [
+                "earth science",
+                "soils",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/569",
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
+            "title": "Global Gridded Surfaces of Selected Soil Characteristics (IGBP-DIS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/STRAT_Ground_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2023-11-20. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/STRAT_Ground_Data_1.",
-            "issued": "1995-05-04",
-            "temporal": "1995-05-04T00:00:00Z/1996-12-12T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "1996-12-11",
-            "keyword": [
-                "atmospheric chemistry",
-                "atmospheric pressure",
-                "atmosphere",
-                "earth science",
-                "lidar",
-                "spectral/engineering",
-                "atmospheric temperature"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "C. Thomas McElroy",
                 "hasEmail": "mailto:tmcelroy@yorku.ca"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2770059453-LARC_ASDC",
             "description": "STRAT_Ground_Data is the ground site data collected during the Stratospheric Tracers of Atmospheric Transport (STRAT) campaign. Data from the JPL ozone lidar at Mauna Loa and Table Mountain, the Composition and Photo-Dissociative Flux Measurement (CPFM), and the Airborne Raman Ozone, Temperature, and Aerosol Lidar (AROTAL) are featured in this collection. Data collection for this product is complete.\r\n\r\nThe STRAT campaign was a field campaign conducted by NASA from May 1995 to February 1996. The primary goal of STRAT was to collect measurements of the change of long-lived tracers and functions of altitude, latitude, and season. These measurements were taken to aid with determining rates for global-scale transport and future distributions of high-speed civil transport (HSCT) exhaust that was emitted into the lower atmosphere. STRAT had four main objectives:  defining the rate of transport of trace gases from the stratosphere and troposphere (i.e., HSCT exhaust emissions), improving the understanding of dynamical coupling rates for transport of trace gases between tropical regions and higher latitudes and lower altitudes (between tropical regions, higher latitudes, and lower altitudes are where most ozone resides), improving understanding of chemistry in the upper troposphere and lower stratosphere, and finally, providing data sets for testing two-dimensional and three-dimensional models used in assessments of impacts from stratospheric aviation.  \r\n\r\nTo accomplish these objectives, the STRAT Science Team conducted various surface-based remote sensing and in-situ measurements. NASA flew the ER-2 aircraft along with balloons such as ozonesondes and radiosondes just below the tropopause in the Northern Hemisphere to collect data. Along with the ER-2 and balloons, NASA also utilized satellite imagery, theoretical models, and ground sites. The ER-2 collected data on HOx, NOy, CO2, ozone, water vapor, and temperature. The ER-2 also collected in-situ stratospheric measurements of N2O, CH4, CO, HCL, and NO using the Aircraft Laser Infrared Absorption Spectrometer (ALIAS). Ozonesondes and radiosondes were also deployed to collect data on CO2, NO/NOy, air temperature, pressure, and 3D wind. These balloons also took in-situ measurements of N2O, CFC-11, CH4, CO, HCL, and NO2 using the ALIAS. Ground stations were responsible for taking measurements of O3, ozone mixing ratio, pressure, and temperature. Satellites took infrared images of the atmosphere with the goal of aiding in completing STRAT objectives. Pressure and temperature models were created to help plan the mission.",
-            "title": "STRAT Ground Site Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSTRAT_Ground_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSTRAT_Ground_Data_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/strat",
-                    "description": "ESPO Home Page for STRAT",
                     "@type": "dcat:Distribution",
+                    "description": "ESPO Home Page for STRAT",
+                    "downloadURL": "https://espo.nasa.gov/strat",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/strat/content/STRAT_Science_Overview",
-                    "description": "STRAT Science Overview",
                     "@type": "dcat:Distribution",
+                    "description": "STRAT Science Overview",
+                    "downloadURL": "https://espo.nasa.gov/strat/content/STRAT_Science_Overview",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2770059453-LARC_ASDC",
-                    "description": "Earthdata Search for STRAT_Ground_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for STRAT_Ground_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2770059453-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/STRAT_Ground_Data_1",
-                    "description": "DOI for STRAT_Ground_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for STRAT_Ground_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/STRAT_Ground_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/STRAT/Ground_Data_1/",
-                    "description": "ASDC Direct Data Download for STRAT_Ground_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for STRAT_Ground_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/STRAT/Ground_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2770059453-LARC_ASDC",
+            "issued": "1995-05-04",
+            "keyword": [
+                "atmospheric chemistry",
+                "atmospheric pressure",
+                "atmosphere",
+                "earth science",
+                "lidar",
+                "spectral/engineering",
+                "atmospheric temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/STRAT_Ground_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1996-12-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>19.4 -155.8 19.4 158.1 37.5 158.1 37.5 -155.8 19.4 -155.8</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1995-05-04T00:00:00Z/1996-12-12T00:00:00Z",
             "theme": [
                 "STRAT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "STRAT Ground Site Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/FZHPYHXJ4JGV",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Level-4 9ka Greenland Ice Sheet Balance Velocity V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/FZHPYHXJ4JGV.",
-            "issued": "1993-06-23",
-            "temporal": "1993-06-23T00:00:00Z/2013-04-26T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2013-04-26",
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
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1430937702-NSIDC_ECS",
             "description": "This data set contains calculated balance velocity of the Greenland Ice Sheet during the last three quarters of the Holocene epoch (9ka).",
-            "title": "Level-4 9ka Greenland Ice Sheet Balance Velocity V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FFZHPYHXJ4JGV",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FFZHPYHXJ4JGV",
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
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/RDGBV4.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/RDGBV4.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1430937702-NSIDC_ECS&m=58.42417023895163%21-26.755542538598352%210%210%210%210%2C2&q=RDGBV4",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1430937702-NSIDC_ECS&m=58.42417023895163%21-26.755542538598352%210%210%210%210%2C2&q=RDGBV4",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/RDGBV4/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/RDGBV4/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/FZHPYHXJ4JGV",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/FZHPYHXJ4JGV",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/FZHPYHXJ4JGV",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/FZHPYHXJ4JGV",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1430937702-NSIDC_ECS",
+            "issued": "1993-06-23",
+            "keyword": [
+                "cryosphere",
+                "earth science",
+                "snow/ice"
+            ],
+            "landingPage": "https://doi.org/10.5067/FZHPYHXJ4JGV",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2013-04-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-88.33 58.91 6.62 81.51",
+            "temporal": "1993-06-23T00:00:00Z/2013-04-26T23:59:59.999Z",
             "theme": [
                 "MULTI_NASA",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Level-4 9ka Greenland Ice Sheet Balance Velocity V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-APXS-2-EDR-V1.0",
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
-                "mars science laboratory"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Unprocessed experiment data copied from the memory buffer of the APXS instrument aboard the Mars Science Laboratory rover.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-apxs-2-edr-v1.0_p4r9-kpa7",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars science laboratory"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-APXS-2-EDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-apxs-2-edr-v1.0_p4r9-kpa7",
-            "description": "Unprocessed experiment data copied from the memory buffer of the APXS instrument aboard the Mars Science Laboratory rover.",
-            "title": "MSL MARS ALPHA PARTICLE X-RAY SPECTROMETER 2 EDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MSL MARS ALPHA PARTICLE X-RAY SPECTROMETER 2 EDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1288777498-LARC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, LaRC.",
-            "issued": "2016-06-15",
-            "temporal": "2000-03-03T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-07-05",
-            "keyword": [
-                "nasa"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:support@earthdata.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "identifier": "C1288777498-LARC",
             "description": "MOPITT Calibration History File",
-            "title": "MOPITT Calibration History File V007",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1288777498-LARC.html",
-                    "description": "View this dataset on the CMR (Common Metadata Repository)",
                     "@type": "dcat:Distribution",
+                    "description": "View this dataset on the CMR (Common Metadata Repository)",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1288777498-LARC.html",
+                    "mediaType": "text/html",
                     "title": "CMR"
                 }
             ],
-            "theme": [
-                "geospatial"
+            "identifier": "C1288777498-LARC",
+            "issued": "2016-06-15",
+            "keyword": [
+                "nasa"
             ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1288777498-LARC.html",
             "language": [
                 "en-US"
-            ]
+            ],
+            "modified": "2016-07-05",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LaRC"
+            },
+            "temporal": "2000-03-03T00:00:00Z/2022-01-17T00:00:00Z",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "MOPITT Calibration History File V007"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1236350982-GES_DISC.html",
             "citation": "OMI Science Team. GES DISC. 2012-07-01. OMTO3_CPR. Version 003. OMI/Aura Level 2 Ozone (O3) Total Column 1-Orbit Subset and Collocated Swath along CloudSat track 200-km wide. NASA Goddard Space Flight Center. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/OMTO3_CPR_003.html. Digital Science Data.",
-            "issued": "2006-06-01",
-            "temporal": "2006-06-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-03-02",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric chemistry"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANDREY SAVTCHENKO",
                 "hasEmail": "mailto:Andrey.Savtchenko@nasa.gov"
             },
+            "creator": "OMI Science Team",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1236350982-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "This is a CloudSat-collocated subset of the original product OMTO3, for the purposes of the A-Train mission. The goal of the subset is to select and return OMI data that are within +/-100 km across the CloudSat track. The resultant OMI subset swath is sought to be about 200 km cross-track of CloudSat. This product also contains many ancillary and derived parameters, terrain and geolocation information, solar and satellite viewing angles, and quality flags. Even though collocated with CloudSat, this subset can serve many other A-Train applications.\n                           \n(The shortname for this CloudSat-collocated OMI Level 2 Total Ozone Column subset is OMTO3_CPR_V003)",
-            "editor": "GES DISC",
-            "release-place": "NASA Goddard Space Flight Center",
-            "series-name": "OMTO3_CPR",
-            "creator": "OMI Science Team",
-            "title": "OMI/Aura Level 2 Ozone (O3) Total Column 1-Orbit Subset and Collocated Swath along CloudSat track 200-km wide at 13x24 km2 resolution",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMTO3_CPR_003.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1172832,784 +1172809,818 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMTO3_CPR_003.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMTO3_CPR_003.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://atrain.gesdisc.eosdis.nasa.gov/data/OMI/OMTO3_CPR.003/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://atrain.gesdisc.eosdis.nasa.gov/data/OMI/OMTO3_CPR.003/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithm/ATBD-OMI-02.pdf",
-                    "description": "OMI Algorithm Theoretical Basis Document",
                     "@type": "dcat:Distribution",
+                    "description": "OMI Algorithm Theoretical Basis Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithm/ATBD-OMI-02.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis.gsfc.nasa.gov/",
-                    "description": "MODIS Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS Project Home Page",
+                    "downloadURL": "https://modis.gsfc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://www.cloudsat.cira.colostate.edu/",
-                    "description": "CloudSat Data Processing Center",
                     "@type": "dcat:Distribution",
+                    "description": "CloudSat Data Processing Center",
+                    "downloadURL": "http://www.cloudsat.cira.colostate.edu/",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://projects.knmi.nl/omi/research/product/index.php",
-                    "description": "Quality Assurance for the original product.",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Assurance for the original product.",
+                    "downloadURL": "http://projects.knmi.nl/omi/research/product/index.php",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "editor": "GES DISC",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMTO3_CPR_003.png",
+            "identifier": "C1236350982-GES_DISC",
+            "issued": "2006-06-01",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1236350982-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-03-02",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "NASA Goddard Space Flight Center",
+            "series-name": "OMTO3_CPR",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2006-06-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "ATDD",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OMI/Aura Level 2 Ozone (O3) Total Column 1-Orbit Subset and Collocated Swath along CloudSat track 200-km wide at 13x24 km2 resolution"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CAMEX-3/NAV/DATA201",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Sorenson, Carl  and Gloria  Fields.1999. CAMEX-3 ER-2 NAVIGATION [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/CAMEX-3/NAV/DATA201",
-            "issued": "1999-05-17",
-            "temporal": "1998-08-08T16:00:00Z/1998-09-27T21:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-23",
-            "keyword": [
-                "earth science",
-                "atmospheric winds",
-                "atmosphere",
-                "atmospheric temperature"
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
-            "identifier": "C1979112721-GHRC_DAAC",
             "description": "The CAMEX-3 ER-2 Navigation data files contain information recorded by on board navigation and data collection systems. In addition to typical navigation data (e.g. date, time, lat/lon and altitude) it contains outside meteorological parameters such as wind speed, wind direction, and temperature. These data are available in ASCII text file format and Graphics Interchange Format, where each file contains data recorded at one second intervals for each flight.",
-            "graphic-preview-description": "N/A",
-            "title": "CAMEX-3 ER-2 NAVIGATION V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex3/er2nav/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAMEX-3%2FNAV%2FDATA201",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAMEX-3%2FNAV%2FDATA201",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=er2nav",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=er2nav",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex3/er2nav/browse/camex3_er2_98220.param_02.gif",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex3/er2nav/browse/camex3_er2_98220.param_02.gif",
+                    "mediaType": "image/gif",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/camex3/er2nav/er2nav_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/camex3/er2nav/er2nav_dataset.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/CAMEX3",
-                    "description": "The home page for the project or program which sponsored the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The home page for the project or program which sponsored the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/CAMEX3",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex3/er2nav/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex3/er2nav/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex3/er2nav/browse/",
+            "identifier": "C1979112721-GHRC_DAAC",
+            "issued": "1999-05-17",
+            "keyword": [
+                "earth science",
+                "atmospheric winds",
+                "atmosphere",
+                "atmospheric temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/CAMEX-3/NAV/DATA201",
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
             "spatial": "-89.971 13.976 -63.22 34.588",
+            "temporal": "1998-08-08T16:00:00Z/1998-09-27T21:00:00Z",
             "theme": [
                 "CAMEX-3",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CAMEX-3 ER-2 NAVIGATION V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D14.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler\r\n. 2019-11-07. VNP43D14. Version 001. VIIRS/NPP BRDF/Albedo Parameter 2 Band M5 Daily L3 Global 30 ArcSec CMG V001\r\n. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VNP43D14.001. https://doi.org/10.5067/VIIRS/VNP43D14.001. Digital Science Data. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
-            "issued": "2019-11-07",
-            "temporal": "2012-01-19T00:00:00Z/2024-05-20T00:00:00Z",
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
-            "identifier": "C1607316799-LPDAAC_ECS",
-            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Model Parameter 2 Band M5 product (VNP43D14) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. Each of the three model parameters (isotropic, volumetric, and geometric) for each of the nine VIIRS moderate resolution bands along with the visible, near-infrared (NIR), and shortwave bands included in the VNP43MA1 (https://doi.org/10.5067/VIIRS/VNP43MA1.001) product is stored in a separate file as VNP43D01 through VNP43D36. In addition to the bands included in VNP43MA1, this product suite includes model parameters for the VIIRS Day/Night Band (DNB) as VNP43D37 through VNP43D39. Details regarding methodology are available on the VNP43MA1 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D14 is the BRDF volumetric parameter for VIIRS band M5 (0.672 \u03bcm). The volumetric parameter, in conjunction with the isotropic and geometric parameters, is used to derive the BRDF/Albedo values for VIIRS band M5.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "VNP43D14",
             "creator": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler",
-            "title": "VIIRS/NPP BRDF/Albedo Parameter 2 Band M5 Daily L3 Global 30 ArcSec CMG V001",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Model Parameter 2 Band M5 product (VNP43D14) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. Each of the three model parameters (isotropic, volumetric, and geometric) for each of the nine VIIRS moderate resolution bands along with the visible, near-infrared (NIR), and shortwave bands included in the VNP43MA1 (https://doi.org/10.5067/VIIRS/VNP43MA1.001) product is stored in a separate file as VNP43D01 through VNP43D36. In addition to the bands included in VNP43MA1, this product suite includes model parameters for the VIIRS Day/Night Band (DNB) as VNP43D37 through VNP43D39. Details regarding methodology are available on the VNP43MA1 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D14 is the BRDF volumetric parameter for VIIRS band M5 (0.672 \u03bcm). The volumetric parameter, in conjunction with the isotropic and geometric parameters, is used to derive the BRDF/Albedo values for VIIRS band M5.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D14.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D14.001",
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
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D14.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D14.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/xhdf5",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D14.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D14.001/",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607316799-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607316799-LPDAAC_ECS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D14.001/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D14.001/contents.html",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D14",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D14",
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
+            "identifier": "C1607316799-LPDAAC_ECS",
+            "issued": "2019-11-07",
+            "keyword": [
+                "surface radiative properties",
+                "earth science",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D14.001",
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
+            "series-name": "VNP43D14",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-19T00:00:00Z/2024-05-20T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP BRDF/Albedo Parameter 2 Band M5 Daily L3 Global 30 ArcSec CMG V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/835/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-09-11",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "ames",
-                "nasa",
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
-            "identifier": "DASHLINK_835",
             "description": "The databases of computational and experimental data from the first Aeroelastic Prediction Workshop are located here.\r\n\r\nThe databases file names tell their contents by configuration, angle of attack, Mach number and Reynolds number where necessary.  The experimental data sets are in files with _X in the name.  Files without an _X are computational results.\r\n\r\nThese are the files updated to include data received as of Sept 11, 2013. (JH)",
-            "title": "Databases",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_HIRENASD_steady_mp7_re7.mat",
-                    "description": "DB_HIRENASD_steady_mp7_re7.mat",
                     "@type": "dcat:Distribution",
+                    "description": "DB_HIRENASD_steady_mp7_re7.mat",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_HIRENASD_steady_mp7_re7.mat",
+                    "mediaType": "application/octet-stream",
                     "title": "DB_HIRENASD_steady_mp7_re7.mat"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_HIRENASD_unsteady_mp7_re7.mat",
-                    "description": "DB_HIRENASD_unsteady_mp7_re7.mat",
                     "@type": "dcat:Distribution",
+                    "description": "DB_HIRENASD_unsteady_mp7_re7.mat",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_HIRENASD_unsteady_mp7_re7.mat",
+                    "mediaType": "application/octet-stream",
                     "title": "DB_HIRENASD_unsteady_mp7_re7.mat"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_HIRENASD_steady_mp8_re7.mat",
-                    "description": "DB_HIRENASD_steady_mp8_re7.mat",
                     "@type": "dcat:Distribution",
+                    "description": "DB_HIRENASD_steady_mp8_re7.mat",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_HIRENASD_steady_mp8_re7.mat",
+                    "mediaType": "application/octet-stream",
                     "title": "DB_HIRENASD_steady_mp8_re7.mat"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_HIRENASD_unsteady_mp8_re7.mat",
-                    "description": "DB_HIRENASD_unsteady_mp8_re7.mat",
                     "@type": "dcat:Distribution",
+                    "description": "DB_HIRENASD_unsteady_mp8_re7.mat",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_HIRENASD_unsteady_mp8_re7.mat",
+                    "mediaType": "application/octet-stream",
                     "title": "DB_HIRENASD_unsteady_mp8_re7.mat"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_HIRENASD_steady_mp8_re23.mat",
-                    "description": "DB_HIRENASD_steady_mp8_re23.mat",
                     "@type": "dcat:Distribution",
+                    "description": "DB_HIRENASD_steady_mp8_re23.mat",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_HIRENASD_steady_mp8_re23.mat",
+                    "mediaType": "application/octet-stream",
                     "title": "DB_HIRENASD_steady_mp8_re23.mat"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_HIRENASD_unsteady_mp8_re23.mat",
-                    "description": "DB_HIRENASD_unsteady_mp8_re23.mat",
                     "@type": "dcat:Distribution",
+                    "description": "DB_HIRENASD_unsteady_mp8_re23.mat",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_HIRENASD_unsteady_mp8_re23.mat",
+                    "mediaType": "application/octet-stream",
                     "title": "DB_HIRENASD_unsteady_mp8_re23.mat"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_BSCW_steady_aoa5.mat",
-                    "description": "DB_BSCW_steady_aoa5.mat",
                     "@type": "dcat:Distribution",
+                    "description": "DB_BSCW_steady_aoa5.mat",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_BSCW_steady_aoa5.mat",
+                    "mediaType": "application/octet-stream",
                     "title": "DB_BSCW_steady_aoa5.mat"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_BSCW_unsteady_aoa5_f1.mat",
-                    "description": "DB_BSCW_unsteady_aoa5_f1.mat",
                     "@type": "dcat:Distribution",
+                    "description": "DB_BSCW_unsteady_aoa5_f1.mat",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_BSCW_unsteady_aoa5_f1.mat",
+                    "mediaType": "application/octet-stream",
                     "title": "DB_BSCW_unsteady_aoa5_f1.mat"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_BSCW_unsteady_aoa5_f10.mat",
-                    "description": "DB_BSCW_unsteady_aoa5_f10.mat",
                     "@type": "dcat:Distribution",
+                    "description": "DB_BSCW_unsteady_aoa5_f10.mat",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_BSCW_unsteady_aoa5_f10.mat",
+                    "mediaType": "application/octet-stream",
                     "title": "DB_BSCW_unsteady_aoa5_f10.mat"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_RSW_steady_aoa2.mat",
-                    "description": "DB_RSW_steady_aoa2.mat",
                     "@type": "dcat:Distribution",
+                    "description": "DB_RSW_steady_aoa2.mat",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_RSW_steady_aoa2.mat",
+                    "mediaType": "application/octet-stream",
                     "title": "DB_RSW_steady_aoa2.mat"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_RSW_unsteady_aoa2_f10_modified.mat",
-                    "description": "DB_RSW_unsteady_aoa2_f10_modified.mat",
                     "@type": "dcat:Distribution",
+                    "description": "DB_RSW_unsteady_aoa2_f10_modified.mat",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_RSW_unsteady_aoa2_f10_modified.mat",
+                    "mediaType": "application/octet-stream",
                     "title": "DB_RSW_unsteady_aoa2_f10_modified.mat"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_RSW_unsteady_aoa2_f20_modified.mat",
-                    "description": "DB_RSW_unsteady_aoa2_f20_modified.mat",
                     "@type": "dcat:Distribution",
+                    "description": "DB_RSW_unsteady_aoa2_f20_modified.mat",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_RSW_unsteady_aoa2_f20_modified.mat",
+                    "mediaType": "application/octet-stream",
                     "title": "DB_RSW_unsteady_aoa2_f20_modified.mat"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_RSW_steady_aoa4.mat",
-                    "description": "DB_RSW_steady_aoa4.mat",
                     "@type": "dcat:Distribution",
+                    "description": "DB_RSW_steady_aoa4.mat",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_RSW_steady_aoa4.mat",
+                    "mediaType": "application/octet-stream",
                     "title": "DB_RSW_steady_aoa4.mat"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_X_HIRENASD_steady_mp7_re7.mat",
-                    "description": "Exp",
                     "@type": "dcat:Distribution",
+                    "description": "Exp",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_X_HIRENASD_steady_mp7_re7.mat",
+                    "mediaType": "application/octet-stream",
                     "title": "DB_X_HIRENASD_steady_mp7_re7.mat"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_X_HIRENASD_unsteady_mp7_re7.mat",
-                    "description": "Exp",
                     "@type": "dcat:Distribution",
+                    "description": "Exp",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_X_HIRENASD_unsteady_mp7_re7.mat",
+                    "mediaType": "application/octet-stream",
                     "title": "DB_X_HIRENASD_unsteady_mp7_re7.mat"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_X_HIRENASD_steady_mp8_re7.mat",
-                    "description": "Exp",
                     "@type": "dcat:Distribution",
+                    "description": "Exp",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_X_HIRENASD_steady_mp8_re7.mat",
+                    "mediaType": "application/octet-stream",
                     "title": "DB_X_HIRENASD_steady_mp8_re7.mat"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_X_HIRENASD_unsteady_mp8_re7.mat",
-                    "description": "Exp",
                     "@type": "dcat:Distribution",
+                    "description": "Exp",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_X_HIRENASD_unsteady_mp8_re7.mat",
+                    "mediaType": "application/octet-stream",
                     "title": "DB_X_HIRENASD_unsteady_mp8_re7.mat"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_X_HIRENASD_steady_mp8_re23.mat",
-                    "description": "Exp",
                     "@type": "dcat:Distribution",
+                    "description": "Exp",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_X_HIRENASD_steady_mp8_re23.mat",
+                    "mediaType": "application/octet-stream",
                     "title": "DB_X_HIRENASD_steady_mp8_re23.mat"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_X_HIRENASD_unsteady_mp8_re23.mat",
-                    "description": "Exp",
                     "@type": "dcat:Distribution",
+                    "description": "Exp",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_X_HIRENASD_unsteady_mp8_re23.mat",
+                    "mediaType": "application/octet-stream",
                     "title": "DB_X_HIRENASD_unsteady_mp8_re23.mat"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_X_BSCW_steady_aoa5.mat",
-                    "description": "Exp",
                     "@type": "dcat:Distribution",
+                    "description": "Exp",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_X_BSCW_steady_aoa5.mat",
+                    "mediaType": "application/octet-stream",
                     "title": "DB_X_BSCW_steady_aoa5.mat"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_X_BSCW_unsteady_aoa5_f1.mat",
-                    "description": "Exp",
                     "@type": "dcat:Distribution",
+                    "description": "Exp",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_X_BSCW_unsteady_aoa5_f1.mat",
+                    "mediaType": "application/octet-stream",
                     "title": "DB_X_BSCW_unsteady_aoa5_f1.mat"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_X_BSCW_unsteady_aoa5_f10.mat",
-                    "description": "Exp",
                     "@type": "dcat:Distribution",
+                    "description": "Exp",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_X_BSCW_unsteady_aoa5_f10.mat",
+                    "mediaType": "application/octet-stream",
                     "title": "DB_X_BSCW_unsteady_aoa5_f10.mat"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_X_RSW_steady_aoa2.mat",
-                    "description": "Exp",
                     "@type": "dcat:Distribution",
+                    "description": "Exp",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_X_RSW_steady_aoa2.mat",
+                    "mediaType": "application/octet-stream",
                     "title": "DB_X_RSW_steady_aoa2.mat"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_X_RSW_unsteady_aoa2_f10.mat",
-                    "description": "Exp",
                     "@type": "dcat:Distribution",
+                    "description": "Exp",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_X_RSW_unsteady_aoa2_f10.mat",
+                    "mediaType": "application/octet-stream",
                     "title": "DB_X_RSW_unsteady_aoa2_f10.mat"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_X_RSW_unsteady_aoa2_f20.mat",
-                    "description": "Exp",
                     "@type": "dcat:Distribution",
+                    "description": "Exp",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_X_RSW_unsteady_aoa2_f20.mat",
+                    "mediaType": "application/octet-stream",
                     "title": "DB_X_RSW_unsteady_aoa2_f20.mat"
                 },
                 {
-                    "mediaType": "application/x-zip-compressed",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/HIRENASD_ExpDatabases_April2012.ZIP",
-                    "description": "Exp_allHIRENASD_files",
                     "@type": "dcat:Distribution",
+                    "description": "Exp_allHIRENASD_files",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/HIRENASD_ExpDatabases_April2012.ZIP",
+                    "mediaType": "application/x-zip-compressed",
                     "title": "HIRENASD_ExpDatabases_April2012.ZIP"
                 },
                 {
-                    "mediaType": "application/x-zip-compressed",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/HIRENASD_databases_April19_2013.ZIP",
-                    "description": "Comp_allHirenasd_database",
                     "@type": "dcat:Distribution",
+                    "description": "Comp_allHirenasd_database",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/HIRENASD_databases_April19_2013.ZIP",
+                    "mediaType": "application/x-zip-compressed",
                     "title": "HIRENASD_databases_April19_2013.ZIP"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_X_RSW_steady_aoa4.mat",
-                    "description": "Exp",
                     "@type": "dcat:Distribution",
+                    "description": "Exp",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DB_X_RSW_steady_aoa4.mat",
+                    "mediaType": "application/octet-stream",
                     "title": "DB_X_RSW_steady_aoa4.mat"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_835",
+            "issued": "2013-09-11",
+            "keyword": [
+                "ames",
+                "nasa",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/835/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Databases"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQR50-3W7DS",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA Aquarius project. 2017-12-07. Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Descending 7-Day Data. Version 5.0. Aquarius Sea Surface Salinity Products. Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Ocean Color Group, Gene Feldman, Joel Gales. https://doi.org/10.5067/AQR50-3W7DS. http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius. NASA Aquarius project, Goddard Ocean Color Group, Gene Feldman, Joel Gales, 2017-12-07, Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Descending 7-Day Data V5.0, http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius.",
-            "issued": "2017-10-21",
-            "temporal": "2011-08-25T02:41:02Z/2015-06-07T12:45:21Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-07",
-            "keyword": [
-                "ocean winds",
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
-            "identifier": "C2491757205-POCLOUD",
-            "description": "Aquarius Level 3 ocean surface wind speed standard mapped image data contains gridded 1 degree spatial resolution wind speed data averaged over daily, 7 day, monthly, and seasonal time scales. This particular data set is the 7-Day,\nDescending wind speed product for version 5.0 of the Aquarius data set, which is the official end of mission public data release from the AQUARIUS/SAC-D mission. Only retrieved values for Descending passes have been used to create this product.  The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
-            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA",
-            "series-name": "Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Descending 7-Day Data",
-            "graphic-preview-description": "Thumbnail",
             "creator": "NASA Aquarius project",
-            "title": "Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Descending 7-Day Data V5.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_WIND_SPEED_SMID_7DAY_V5.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Aquarius Level 3 ocean surface wind speed standard mapped image data contains gridded 1 degree spatial resolution wind speed data averaged over daily, 7 day, monthly, and seasonal time scales. This particular data set is the 7-Day,\nDescending wind speed product for version 5.0 of the Aquarius data set, which is the official end of mission public data release from the AQUARIUS/SAC-D mission. Only retrieved values for Descending passes have been used to create this product.  The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3W7DS",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3W7DS",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_WIND_SPEED_SMID_7DAY_V5.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_WIND_SPEED_SMID_7DAY_V5.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491757205-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491757205-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491757205-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491757205-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_WIND_SPEED_SMID_7DAY_V5.jpg",
+            "identifier": "C2491757205-POCLOUD",
+            "issued": "2017-10-21",
+            "keyword": [
+                "ocean winds",
+                "earth science",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQR50-3W7DS",
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
+            "series-name": "Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Descending 7-Day Data",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T02:41:02Z/2015-06-07T12:45:21Z",
             "theme": [
                 "AQUARIUS SAC-D",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Descending 7-Day Data V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://fermi.gsfc.nasa.gov/ssc/data/access/lat/2yr_catalog/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Phil Newman",
+                "hasEmail": "mailto:panewman@lheapop.gsfc.nasa.gov"
+            },
+            "description": "The Fermi Gamma-ray Space Telescope (Fermi) Large Area Telescope (LAT) is a successor to EGRET, with greatly improved sensitivity, resolution, and energy range. This web page presents the second full catalog of LAT sources, based on the first 24 months of survey data. For a full explanation about the catalog and its construction see the LAT 2-year Catalog Paper (also available on arxiv).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://iopscience.iop.org/0067-0049/199/2/31/pdf/apjs_199_2_31.pdf",
+                    "mediaType": "application/pdf"
+                }
+            ],
+            "identifier": "NASA-0000217__3",
             "issued": "2018-06-25",
-            "temporal": "2008-08-04/2010-07-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "cgro",
                 "energy",
@@ -1173627,192 +1173638,183 @@
                 "high-energy",
                 "egret"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Phil Newman",
-                "hasEmail": "mailto:panewman@lheapop.gsfc.nasa.gov"
-            },
+            "landingPage": "http://fermi.gsfc.nasa.gov/ssc/data/access/lat/2yr_catalog/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:014"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000217__3",
-            "description": "The Fermi Gamma-ray Space Telescope (Fermi) Large Area Telescope (LAT) is a successor to EGRET, with greatly improved sensitivity, resolution, and energy range. This web page presents the second full catalog of LAT sources, based on the first 24 months of survey data. For a full explanation about the catalog and its construction see the LAT 2-year Catalog Paper (also available on arxiv).",
-            "title": "LAT 2-year Point Source Catalog",
-            "programCode": [
-                "026:014"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://iopscience.iop.org/0067-0049/199/2/31/pdf/apjs_199_2_31.pdf",
-                    "mediaType": "application/pdf"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
+            "temporal": "2008-08-04/2010-07-31",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "LAT 2-year Point Source Catalog"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TPSDR-BIN0A",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "TOPEX/Poseidon. 1993-08-07. TOPEX ALTIMETER SENSOR DATA RECORD. Version A. TOPEX_ALTSDR. JPL. Archived by National Aeronautics and Space Administration, U.S. Government, TOPEX/Poseidon. https://doi.org/10.5067/TPSDR-BIN0A. TOPEX/Poseidon, TOPEX/Poseidon, 1993-08-07, TOPEX ALTIMETER SENSOR DATA RECORD, N/A.",
-            "issued": "2009-06-15",
-            "temporal": "1992-09-25T00:00:00Z/2005-10-04T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2011-01-21",
-            "keyword": [
-                "oceans",
-                "ocean waves",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jessica Hausman",
                 "hasEmail": "mailto:Jessica.K.Hausman@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "identifier": "C2617176787-POCLOUD",
-            "description": "The Sensory Data Record (SDR) is similar to the GDR product except that it also contains waveforms, which are required for retracking.  This is an expert level product.  If you do not need the waveforms then the GDR should suit your needs.",
-            "release-place": "JPL",
-            "series-name": "TOPEX ALTIMETER SENSOR DATA RECORD",
-            "graphic-preview-description": "Thumbnail",
             "creator": "TOPEX/Poseidon",
-            "title": "TOPEX ALTIMETER SENSOR DATA RECORD",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TOPEX_ALTSDR.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Sensory Data Record (SDR) is similar to the GDR product except that it also contains waveforms, which are required for retracking.  This is an expert level product.  If you do not need the waveforms then the GDR should suit your needs.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTPSDR-BIN0A",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTPSDR-BIN0A",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TOPEX_ALTSDR.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TOPEX_ALTSDR.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/topex/open/L1B/altsdr/docs/D-8591_C_sdr.pdf",
-                    "description": "PO.DAAC Drive",
                     "@type": "dcat:Distribution",
+                    "description": "PO.DAAC Drive",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/topex/open/L1B/altsdr/docs/D-8591_C_sdr.pdf",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2617176787-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2617176787-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2617176787-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2617176787-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TOPEX_ALTSDR.jpg",
+            "identifier": "C2617176787-POCLOUD",
+            "issued": "2009-06-15",
+            "keyword": [
+                "oceans",
+                "ocean waves",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/TPSDR-BIN0A",
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
+            "release-place": "JPL",
+            "series-name": "TOPEX ALTIMETER SENSOR DATA RECORD",
             "spatial": "-180.0 -66.0 180.0 66.0",
+            "temporal": "1992-09-25T00:00:00Z/2005-10-04T23:59:59.999Z",
             "theme": [
                 "TOPEX/POSEIDON",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TOPEX ALTIMETER SENSOR DATA RECORD"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/LIDAR/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/LIDAR/DATA001.",
-            "issued": "1989-09-02",
-            "temporal": "1989-09-02T00:00:02Z/2023-04-10T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-03-29",
-            "keyword": [
-                "ocean chemistry",
-                "salinity/density",
-                "ocean optics",
-                "oceans",
-                "earth science",
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
-            "identifier": "C1633360430-OB_DAAC",
             "description": "Pigment measurements from 1989 and 1990 in the Gulf of St Lawrence.",
-            "title": "Pigment measurements from 1989 and 1990 in the Gulf of St Lawrence",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FLIDAR%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FLIDAR%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
```

