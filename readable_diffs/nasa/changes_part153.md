# Change History for nasa.json (Part 153)

### Changes from 31606f9 to dd2190f (Part 142/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO3_logo.jpg",
+            "identifier": "C3277752333-GES_DISC",
+            "issued": "2024-07-01",
+            "keyword": [
+                "infrared wavelengths",
+                "atmospheric chemistry",
+                "spectral/engineering",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C3277752333-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-07-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "OCO3_L1aIn_Pixel",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2019-11-30T00:00:00Z/2024-11-11T00:00:00Z",
             "theme": [
                 "OCO-3",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OCO-3 Level 1A collated, parsed, calibration data V11 (OCO3_L1aIn_Pixel) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MEASURES/AMDBLWV",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Luis Millan, Matt Lebsock, Evan Fishbein, Peter Kalmus,  & Joao Teixeria. 2017-04-11. AMDBLWV. Version 1. AMSR-MODIS Boundary Layer Water Vapor L3 Daily 1 degree x 1 degree V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/MEASURES/AMDBLWV. https://disc.gsfc.nasa.gov/datacollection/AMDBLWV_1.html.",
-            "issued": "2002-07-04",
-            "temporal": "2002-07-04T00:00:00Z/2016-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-12-31",
-            "references": [
-                "https://doi.org/10.1175/JAMC-D-15-0143.1"
-            ],
-            "keyword": [
-                "national geospatial data asset",
-                "ngda",
-                "atmosphere",
-                "earth science",
-                "atmospheric water vapor"
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
-            "identifier": "C1382049816-GES_DISC",
-            "description": "This data set provides an estimate the marine boundary layer water vapor beneath uniform cloud fields. Microwave radiometry from AMSR-E and AMSR-2 provides the total column water vapor, while the near-infrared imagery from MODIS provides the water vapor above the cloud layers. The difference between the two gives the vapor between the surface and the cloud top, which may be interpreted as the boundary layer water vapor.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "AMDBLWV",
             "creator": "Luis Millan, Matt Lebsock, Evan Fishbein, Peter Kalmus,  & Joao Teixeria",
-            "title": "AMSR-MODIS Boundary Layer Water Vapor L3 Daily 1 degree x 1 degree V1 (AMDBLWV) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AMDBLWV_1.png",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This data set provides an estimate the marine boundary layer water vapor beneath uniform cloud fields. Microwave radiometry from AMSR-E and AMSR-2 provides the total column water vapor, while the near-infrared imagery from MODIS provides the water vapor above the cloud layers. The difference between the two gives the vapor between the surface and the cloud top, which may be interpreted as the boundary layer water vapor.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FAMDBLWV",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FAMDBLWV",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1493368,17 +1493341,17 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AMDBLWV_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AMDBLWV_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gsfc.nasa.gov/data/BLWV/AMDBLWV.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://measures.gsfc.nasa.gov/data/BLWV/AMDBLWV.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
@@ -1493388,10 +1493361,10 @@
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/BLWV/AMDBLWV.1/doc/README.AMSR-MODIS_BoundaryLayerWaterVapor_V1.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/BLWV/AMDBLWV.1/doc/README.AMSR-MODIS_BoundaryLayerWaterVapor_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
@@ -1493401,64 +1493374,93 @@
                     "title": "View this dataset's algorithm theoretical basis document"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AMDBLWV_1.png",
+            "identifier": "C1382049816-GES_DISC",
+            "issued": "2002-07-04",
+            "keyword": [
+                "national geospatial data asset",
+                "ngda",
+                "atmosphere",
+                "earth science",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/AMDBLWV",
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
+            "references": [
+                "https://doi.org/10.1175/JAMC-D-15-0143.1"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "AMDBLWV",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-07-04T00:00:00Z/2016-12-31T23:59:59Z",
             "theme": [
                 "MEaSUREs",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AMSR-MODIS Boundary Layer Water Vapor L3 Daily 1 degree x 1 degree V1 (AMDBLWV) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-MIRO-2-EAR1-EARTH1-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Spectroscopic, Continuum and Engineering data, in the form of table files, taken during the first Earth swing-by phase of the Rosetta mission by the MIRO instrument.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-miro-2-ear1-earth1-v1.0_uxmx-uaew",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "earth",
                 "moon"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-MIRO-2-EAR1-EARTH1-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-miro-2-ear1-earth1-v1.0_uxmx-uaew",
-            "description": "This data set contains Spectroscopic, Continuum and Engineering data, in the form of table files, taken during the first Earth swing-by phase of the Rosetta mission by the MIRO instrument.",
-            "title": "ROSETTA-ORBITER EARTH MIRO 2 EAR1 EARTH1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER EARTH MIRO 2 EAR1 EARTH1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LCROSS-E%2FL-NIR2-3-CAL-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Calibrated image data from the Near Infrared Camera 2 (NIR2) aboard the Lunar Crater Observation and Sensing Satellite (LCROSS).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lcross-e-l-nir2-3-cal-v1.0_uxqc-wg6z",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "lunar crater observation and sensing satellite",
                 "test image",
@@ -1493466,74 +1493468,37 @@
                 "moon",
                 "earth"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LCROSS-E%2FL-NIR2-3-CAL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lcross-e-l-nir2-3-cal-v1.0_uxqc-wg6z",
-            "description": "Calibrated image data from the Near Infrared Camera 2 (NIR2) aboard the Lunar Crater Observation and Sensing Satellite (LCROSS).",
-            "title": "LCROSS EARTH/MOON 2ND NEAR IR CAMERA 3 CAL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "LCROSS EARTH/MOON 2ND NEAR IR CAMERA 3 CAL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.nasa.gov/centers/kennedy/launchingrockets/archives/2006.html",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2006-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://www.nasa.gov/centers/kennedy/launchingrockets/archives/elv_archive-index.html"
-            ],
-            "keyword": [
-                "expedition",
-                "mission",
-                "vehicle",
-                "history",
-                "new horizons",
-                "stereo",
-                "earth's bridge to space",
-                "landing",
-                "atlas",
-                "calypso",
-                "delta",
-                "cloudsat",
-                "space technology",
-                "time",
-                "schedule",
-                "launch",
-                "pegasus",
-                "support"
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
-            "identifier": "NASA-928",
             "description": "A list of launch vehicles launched for NASA missions in 2006.",
-            "title": "NASA Expendable Launch Vehicle Launch Archive 2006",
-            "programCode": [
-                "026:046"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1493576,53 +1493541,66 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-928",
+            "issued": "2006-01-01",
+            "keyword": [
+                "expedition",
+                "mission",
+                "vehicle",
+                "history",
+                "new horizons",
+                "stereo",
+                "earth's bridge to space",
+                "landing",
+                "atlas",
+                "calypso",
+                "delta",
+                "cloudsat",
+                "space technology",
+                "time",
+                "schedule",
+                "launch",
+                "pegasus",
+                "support"
+            ],
+            "landingPage": "http://www.nasa.gov/centers/kennedy/launchingrockets/archives/2006.html",
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
+            "title": "NASA Expendable Launch Vehicle Launch Archive 2006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/UZBU0ANMH4ES",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Martin Snow. 2021-01-06. SOR3SOLD_MGII_018. Version 018. SORCE SOLSTICE Level 3 MgII Core-to-Wing Ratio 24 Hour Means V018. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/UZBU0ANMH4ES. https://disc.gsfc.nasa.gov/datacollection/SOR3SOLD_MGII_018.html. Digital Science Data.",
-            "issued": "2020-12-29",
-            "temporal": "2003-03-05T00:00:00Z/2020-02-25T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-29",
-            "keyword": [
-                "sun-earth interactions",
-                "solar activity",
-                "earth science"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "MARTIN SNOW",
                 "hasEmail": "mailto:martin.snow@lasp.colorado.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1993479667-GES_DISC",
-            "description": "The SORCE SOLSTICE Level 3 MgII Core to Wing Ratio 24 Hour Means product consists of daily averages of the magnesium II core-to-wing index from the SOLSTICE instrument. The SOLSTICE instrument makes measurements during each daytime orbit portion, 15 orbits per day. This product has solar spectra averaged for a day. The spectral resolution of SOLSTICE is 0.1 nm, allowing the Mg-II doublet to be fully resolved and modeled with Gaussians. The Mg-II core-to-wing ratio is used as a measurement of solar activity.\n\nThe Mg-II data are arranged in a single file in a tabular ASCII text file which can be easily read into a spreadsheet application. The columns contain the date (calendar and Julian Day), the core/wing ratio, and the absolute uncertainty. The rows are arranged with one daily average measurment, repeating for each day for the length of the measurement period.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "SOR3SOLD_MGII_018",
             "creator": "Martin Snow",
-            "title": "SORCE SOLSTICE Level 3 MgII Core-to-Wing Ratio 24 Hour Means V018 (SOR3SOLD_MGII_018) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SOR3SOLD_MGII_018.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The SORCE SOLSTICE Level 3 MgII Core to Wing Ratio 24 Hour Means product consists of daily averages of the magnesium II core-to-wing index from the SOLSTICE instrument. The SOLSTICE instrument makes measurements during each daytime orbit portion, 15 orbits per day. This product has solar spectra averaged for a day. The spectral resolution of SOLSTICE is 0.1 nm, allowing the Mg-II doublet to be fully resolved and modeled with Gaussians. The Mg-II core-to-wing ratio is used as a measurement of solar activity.\n\nThe Mg-II data are arranged in a single file in a tabular ASCII text file which can be easily read into a spreadsheet application. The columns contain the date (calendar and Julian Day), the core/wing ratio, and the absolute uncertainty. The rows are arranged with one daily average measurment, repeating for each day for the length of the measurement period.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FUZBU0ANMH4ES",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FUZBU0ANMH4ES",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1493632,736 +1493610,732 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/SORCE_Level3/SOR3SOLD_MGII.018/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/SORCE_Level3/SOR3SOLD_MGII.018/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SOR3SOLD_MGII_018",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SOR3SOLD_MGII_018",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://lasp.colorado.edu/data/sorce/file_readers/read_lasp_ascii_file.pro",
-                    "description": "IDL-based read software.",
                     "@type": "dcat:Distribution",
+                    "description": "IDL-based read software.",
+                    "downloadURL": "http://lasp.colorado.edu/data/sorce/file_readers/read_lasp_ascii_file.pro",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://lasp.colorado.edu/home/sorce/",
-                    "description": "SORCE Project Home Page.",
                     "@type": "dcat:Distribution",
+                    "description": "SORCE Project Home Page.",
+                    "downloadURL": "http://lasp.colorado.edu/home/sorce/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://lasp.colorado.edu/home/sorce/instruments/solstice/solstice-data-product-release-notes/",
-                    "description": "SOLSTICE Release Notes",
                     "@type": "dcat:Distribution",
+                    "description": "SOLSTICE Release Notes",
+                    "downloadURL": "http://lasp.colorado.edu/home/sorce/instruments/solstice/solstice-data-product-release-notes/",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://eospso.nasa.gov/sites/default/files/atbd/ATBD-SOR-01.pdf",
-                    "description": "SORCE ATBD",
                     "@type": "dcat:Distribution",
+                    "description": "SORCE ATBD",
+                    "downloadURL": "https://eospso.nasa.gov/sites/default/files/atbd/ATBD-SOR-01.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://lasp.colorado.edu/home/sorce/reference/publications/",
-                    "description": "List of publications.",
                     "@type": "dcat:Distribution",
+                    "description": "List of publications.",
+                    "downloadURL": "http://lasp.colorado.edu/home/sorce/reference/publications/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SOR3SOLD_MGII_018.png",
+            "identifier": "C1993479667-GES_DISC",
+            "issued": "2020-12-29",
+            "keyword": [
+                "sun-earth interactions",
+                "solar activity",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/UZBU0ANMH4ES",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-12-29",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "SOR3SOLD_MGII_018",
+            "temporal": "2003-03-05T00:00:00Z/2020-02-25T23:59:59.999Z",
             "theme": [
                 "SORCE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SORCE SOLSTICE Level 3 MgII Core-to-Wing Ratio 24 Hour Means V018 (SOR3SOLD_MGII_018) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1502",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Bloom, A.A., K. Bowman, M. Lee, A.J. Turner, R. Schroeder, J.R. Worden, R.J. Weidner, K.C. McDonald, and D.J. Jacob. 2017. CMS: Global 0.5-deg Wetland Methane Emissions and Uncertainty (WetCHARTs v1.0). ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1502",
-            "issued": "2017-06-05",
-            "temporal": "2001-01-01T00:00:00Z/2015-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-17",
-            "keyword": [
-                "earth science",
-                "biosphere",
-                "atmosphere",
-                "ecosystems",
-                "atmospheric chemistry",
-                "air quality"
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
-            "identifier": "C2389102945-ORNL_CLOUD",
             "description": "This data set provides global monthly wetland methane (CH4) emissions and uncertainty data products derived from an ensemble of multiple terrestrial biosphere models, wetland extent scenarios, and CH4:C temperature dependencies. The data are at 0.5 by 0.5-degree resolution. Two model output data products are included in WetCHARTs v1.0: an output from the full ensemble for 2009-2010 and an output from a limited subset for 2001-2015. The intended use of the products is as a process-informed wetland CH4 emission and uncertainty data set for atmospheric chemistry and transport modelling (WetCHARTs).",
-            "graphic-preview-description": "Browse Image",
-            "title": "CMS: Global 0.5-deg Wetland Methane Emissions and Uncertainty (WetCHARTs v1.0)",
-            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/CMS_Global_Monthly_Wetland_CH4_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1502",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1502",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/cms/CMS_Global_Monthly_Wetland_CH4/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/cms/CMS_Global_Monthly_Wetland_CH4/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_Global_Monthly_Wetland_CH4.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_Global_Monthly_Wetland_CH4.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1502",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1502",
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
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/CMS_Global_Monthly_Wetland_CH4/comp/CMS_Global_Monthly_Wetland_CH4.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/CMS_Global_Monthly_Wetland_CH4/comp/CMS_Global_Monthly_Wetland_CH4.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_Global_Monthly_Wetland_CH4_Fig1.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_Global_Monthly_Wetland_CH4_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1502/catalog.html",
-                    "description": "The THREDDS location for this Collection.",
                     "@type": "dcat:Distribution",
+                    "description": "The THREDDS location for this Collection.",
+                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1502/catalog.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/CMS_Global_Monthly_Wetland_CH4_Fig1.png",
+            "identifier": "C2389102945-ORNL_CLOUD",
+            "issued": "2017-06-05",
+            "keyword": [
+                "earth science",
+                "biosphere",
+                "atmosphere",
+                "ecosystems",
+                "atmospheric chemistry",
+                "air quality"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1502",
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
+            "temporal": "2001-01-01T00:00:00Z/2015-12-31T23:59:59Z",
             "theme": [
                 "CMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CMS: Global 0.5-deg Wetland Methane Emissions and Uncertainty (WetCHARTs v1.0)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-SS-POS-6-SUMM-CRUISE-RTN-V1.0",
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
+            "description": "This dataset contains the Galileo spacecraft trajectory during the interplanetary cruise. The data have been derived from SPICE kernels at a 1 minute sample rate. The data are provided in RTN coordinates.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-ss-pos-6-summ-cruise-rtn-v1.0_uxs8-h8ny",
+            "issued": "2021-05-21",
+            "keyword": [
+                "galileo"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-SS-POS-6-SUMM-CRUISE-RTN-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-ss-pos-6-summ-cruise-rtn-v1.0_uxs8-h8ny",
-            "description": "This dataset contains the Galileo spacecraft trajectory during the interplanetary cruise. The data have been derived from SPICE kernels at a 1 minute sample rate. The data are provided in RTN coordinates.",
-            "title": "GALILEO CRUISE POSITION DATA (RTN COORDINATES)",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GALILEO CRUISE POSITION DATA (RTN COORDINATES)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/706",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Holben, B.N., and T.F. Eck. 2000. SAFARI 2000 AERONET Ground-based Aerosol Data, Dry Season 2000. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/706",
-            "issued": "2023-10-18",
-            "temporal": "1999-01-01T00:00:00Z/2001-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-24",
-            "keyword": [
-                "atmospheric water vapor",
-                "aerosols",
-                "earth science",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
-                "hasEmail": "mailto:uso@daac.ornl.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "ORNL_DAAC"
-            },
-            "identifier": "C2788355135-ORNL_CLOUD",
-            "description": "AERONET (AErosol RObotic NETwork) is an optical ground-based aerosol monitoring network and data archive system. AERONET measurements of the column-integrated aerosol optical properties in the southern Africa region were made by sun-sky radiometers at several sites in August-September 2000 as a part of the SAFARI 2000 dry season aircraft campaign. AERONET is supported by NASA's Earth Observing System and expanded by federation with many non-NASA institutions. The network hardware consists of identical automatic sun-sky scanning spectral radiometers owned by national agencies and universities. Data from this collaboration provides globally-distributed near-real-time observations of aerosol spectral optical depths, aerosol size distributions, and precipitable water in diverse aerosol regimes.",
-            "graphic-preview-description": "Browse Image",
-            "title": "SAFARI 2000 AERONET Ground-based Aerosol Data, Dry Season 2000",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/safari_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
+                "hasEmail": "mailto:uso@daac.ornl.gov"
+            },
+            "description": "AERONET (AErosol RObotic NETwork) is an optical ground-based aerosol monitoring network and data archive system. AERONET measurements of the column-integrated aerosol optical properties in the southern Africa region were made by sun-sky radiometers at several sites in August-September 2000 as a part of the SAFARI 2000 dry season aircraft campaign. AERONET is supported by NASA's Earth Observing System and expanded by federation with many non-NASA institutions. The network hardware consists of identical automatic sun-sky scanning spectral radiometers owned by national agencies and universities. Data from this collaboration provides globally-distributed near-real-time observations of aerosol spectral optical depths, aerosol size distributions, and precipitable water in diverse aerosol regimes.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F706",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F706",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/atmospheric/AERONET_aerosol/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/atmospheric/AERONET_aerosol/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/S2K/guides/s2k_aeronet.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/S2K/guides/s2k_aeronet.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/706",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/706",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/atmospheric/AERONET_aerosol/comp/aeronet_doc.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/atmospheric/AERONET_aerosol/comp/aeronet_doc.pdf",
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
+            "identifier": "C2788355135-ORNL_CLOUD",
+            "issued": "2023-10-18",
+            "keyword": [
+                "atmospheric water vapor",
+                "aerosols",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/706",
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
             "spatial": "-26.19 28.03",
+            "temporal": "1999-01-01T00:00:00Z/2001-12-31T23:59:59Z",
             "theme": [
                 "SAFARI 2000",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAFARI 2000 AERONET Ground-based Aerosol Data, Dry Season 2000"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1274625654-GES_DISC.html",
             "citation": "Laboratory for Atmospheres at NASA/GSFC. 1995-01-01. TOVSA5TN. Version 01. TOVS GLA 5 DAY GRIDS from TIROSN V01. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/TOVSA5TN_01.html. Digital Science Data.",
-            "issued": "1978-12-01",
-            "temporal": "1978-12-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "1979-06-30",
-            "keyword": [
-                "ocean temperature",
-                "precipitation",
-                "oceans",
-                "atmospheric pressure",
-                "atmospheric radiation",
-                "atmospheric temperature",
-                "earth science",
-                "atmospheric chemistry",
-                "ocean pressure",
-                "atmosphere",
-                "atmospheric water vapor",
-                "clouds",
-                "land surface",
-                "surface thermal properties"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JOEL SUSSKIND",
                 "hasEmail": "mailto:joel.susskind-1@nasa.gov"
             },
+            "creator": "Laboratory for Atmospheres at NASA/GSFC",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1274625654-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "This dataset (TOVSA5TN) contains the TIROS Operational Vertical Sounder (TOVS) level 3 geophysical parameters derived using data from TIROS-N and the physical retrieval method of Susskind et al. (1984) and processed by the Satellite Data Utilization Office of the Goddard Laboratory for Atmospheres at NASA/GSFC. This method, which is hydrodynamic model- and a priori data-dependent, is designated as the so-called Path A scheme by the TOVS Pathfinder Science Working Group. The 20 channel High resolution Infrared Radiation Sounder 2 (HIRS2) and the 4 channel Microwave Sounding Unit (MSU) aboard the NOAA-xx series of Polar Orbiting Satellites are used to produce global fields of the 3-dimensional temperature-moisture structure of the atmosphere. In addition to profiles of temperature and moisture, the HIRS2/MSU data are used to derive important quantities such as land and sea surface temperature, outgoing longwave radiation, cloud fraction, cloudtop height, total ozone overburden and precipitation estimates.\n\nThe Path A system steps through an interactive forecast-retrieval-analysis cycle. In each 6 hour synoptic period, a 2nd order General Circulation Model (Takacs et al., 1994) is used to generate the 6 hour forecast fields of temperature and humidity. These global fields are used as the first guess for all soundings occuring within a 6 hour time window centered upon the forecast time. These retrievals are then assimilated with all available insitu measurements (such as radiosonde and ship reports) in the 6 hour interval using an Optimal Interpolation (OI) analysis scheme developed by the Data Assimilation Office of the Goddard Laboratory for Atmospheres. This analysis is then used to specify the initial conditions for the next 6 hour forecast, thus completing the cycle.\n\nThe retrieval algorithm itself is a physical method based on the iterative relaxation technique originally proposed by Chahine (1968). The basic approach consists of modifying the temperature profile from the previous iteration by an amount proportional to the difference between the observed brightness temperatures and the brightness temperatures computed from the trial parameters using the full radiative transfer equation applied at the observed satellite zenith angle. For the case of the temperature profile, the updated layer mean temperatures are given as a linear combination of multichannel brightness temperature differences with the coefficients given by the channel weighting functions. Constraints are imposed upon the solution in order to ensure stability and convergence of the iterative process. For more details see Susskind et al (1984).\n\nThere are level 3 data product files for five TOVS satellites, each of which is in the HDF format and each representative of a different averaging time period.  All files contain the same number of geophysical parameter arrays stored as HDF Scientific Data Sets (SDSs). The time periods include daily, 5 day (pentad) and monthly, with the AM and PM portions of the orbits treated separately.  All data are mapped to a 1 degree longitude by 1 degree latitude global grid. This collection contains 5-day averages.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TOVSA5TN",
-            "creator": "Laboratory for Atmospheres at NASA/GSFC",
-            "title": "TOVS GLA 5 DAY GRIDS from TIROSN V01 (TOVSA5TN ) at GES DISC",
-            "graphic-preview-description": "TOVSA5TN image",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOVSA5TN_01.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOVSA5TN_01.png",
-                    "description": "TOVSA5TN image",
                     "@type": "dcat:Distribution",
+                    "description": "TOVSA5TN image",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOVSA5TN_01.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TOVSA5TN_01.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TOVSA5TN_01.html",
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
-                    "downloadURL": "https://disc1.gesdisc.eosdis.nasa.gov/data/tovs/TOVSA5TN",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://disc1.gesdisc.eosdis.nasa.gov/data/tovs/TOVSA5TN",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TOVSA5TN+001",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TOVSA5TN+001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc1.gesdisc.eosdis.nasa.gov/data/tovs/TOVSA5TN/doc/README.TOVSPentad.txt",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://disc1.gesdisc.eosdis.nasa.gov/data/tovs/TOVSA5TN/doc/README.TOVSPentad.txt",
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
+            "graphic-preview-description": "TOVSA5TN image",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOVSA5TN_01.png",
+            "identifier": "C1274625654-GES_DISC",
+            "issued": "1978-12-01",
+            "keyword": [
+                "ocean temperature",
+                "precipitation",
+                "oceans",
+                "atmospheric pressure",
+                "atmospheric radiation",
+                "atmospheric temperature",
+                "earth science",
+                "atmospheric chemistry",
+                "ocean pressure",
+                "atmosphere",
+                "atmospheric water vapor",
+                "clouds",
+                "land surface",
+                "surface thermal properties"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1274625654-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1979-06-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "TOVSA5TN",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1978-12-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "TOVS Pathfinder",
                 "CWIC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TOVS GLA 5 DAY GRIDS from TIROSN V01 (TOVSA5TN ) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE1_Satellite_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2023-07-19. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE1_Satellite_Data_1.",
-            "issued": "2022-08-26",
-            "temporal": "1999-10-24T00:00:00Z/2000-03-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-08-26",
-            "keyword": [
-                "atmospheric water vapor",
-                "atmospheric pressure",
-                "atmospheric winds",
-                "atmospheric temperature",
-                "earth science",
-                "aerosols",
-                "atmosphere",
-                "atmospheric chemistry"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "James Russell III",
                 "hasEmail": "mailto:james.russell@hamptonu.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2569836885-LARC_ASDC",
             "description": "SOLVE1_Satellite_Data is the supplementary satellite data for the SAGE III Ozone Loss and Validation Experiment (SOLVE). Data were collected by instruments such as the Halogen Occultation Experiment (HALOE), the Polar Ozone and Aerosol Measurement III (POAM III) satellite, and the Global Ozone Monitoring Experiment (GOME). Data collection for this product is complete.\r\n\r\nThe SOLVE campaign was a NASA multi-program effort of the Upper Atmosphere Research Program (UARP), Atmospheric Effects of Aviation Project (AEAP), Atmospheric Chemistry Modeling and Analysis Program (ACMAP) and Earth Observing System (EOS) of NASA\u2019s Earth Science Enterprise (ESE). SOLVE\u2019s primary objective was for calibrating and validating the Stratospheric Aerosol and Gas Experiment (SAGE) III satellite measurements, while examining the processes that controlled ozone levels at a mid- to high-latitude range. The major goal of SAGE III was to quantitatively assess ozone loss at high latitudes. SOLVE was a two-phase experiment, the first phase, SOLVE, occurred during the fall of 1999 through the spring of 2000. The second phase, SOLVE II, occurred during the winter of 2003.\r\n\r\nSOLVE took place in the Arctic high-latitude region during the winter. The polar ozone depletion processes cause by human-produced chlorine and bromine are most active in mid-to-late winter and early spring in the high Arctic. In order to conduct this validation experiment, NASA deployed the NASA ER-2 aircraft and NASA DC-8 aircraft. The ER-2 measured a variety of atmospheric data, including ozone (O3), H2O, CO2, ClONO2, HCl, ClO/BrO, and Cl2O2. The DC-8 aircraft measured ozone, ClO/BrO, and aerosol, among other atmospheric data. SOLVE also utilized balloon platforms, ground-based instruments, and collaborations with the German Aerospace Center\u2019s (DLR) FALCON aircraft equipped with the OLEX Lidar to achieve the mission objectives. Overall, the campaign had 28 flights, with SOLVE featuring 17 total flights among the different aircrafts and SOLVE II featuring 11 flights.",
-            "title": "SOLVE I Supplementary Satellite Data Products",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSOLVE1_Satellite_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSOLVE1_Satellite_Data_1",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2569836885-LARC_ASDC",
-                    "description": "Earthdata Search client for SOLVE1_Satellite_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search client for SOLVE1_Satellite_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2569836885-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE1_Satellite_Data_1",
-                    "description": "DOI for SOLVE1_Satellite_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for SOLVE1_Satellite_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE1_Satellite_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/SOLVE/Satellite_Data_1/",
-                    "description": "ASDC Direct Data Download for SOLVE1_Satellite_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for SOLVE1_Satellite_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/SOLVE/Satellite_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2569836885-LARC_ASDC",
+            "issued": "2022-08-26",
+            "keyword": [
+                "atmospheric water vapor",
+                "atmospheric pressure",
+                "atmospheric winds",
+                "atmospheric temperature",
+                "earth science",
+                "aerosols",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE1_Satellite_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-08-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-73.9 -180.0 -73.9 180.0 69.1 180.0 69.1 -180.0 -73.9 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1999-10-24T00:00:00Z/2000-03-31T23:59:59.999Z",
             "theme": [
                 "SOLVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SOLVE I Supplementary Satellite Data Products"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/S6AP4-1BLNTR-F08",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Ocean Surface Topography Science Team. 2023-07-31. Sentinel-6A MF Jason-CS L1B P4 Altimeter Low Resolution (LR) NTC Geolocated Waveforms F08. Version F08. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/S6AP4-1BLNTR-F08.",
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
-            "identifier": "C2619443901-POCLOUD",
-            "description": "Provides reprocessed L1B low resolution (LR) non-time critical (NTC; 60-day latency) altimetry data from the Poseidon-4 SAR altimeter on the Sentinel-6A Michael Freilich spacecraft which include the geolocated, fully-calibrated pulse-limited LR power echoes. The S6A NTC product is analogous to the Jason-3 GDR product.",
-            "release-place": "PO.DAAC",
-            "graphic-preview-description": "Thumbnail image for Website",
             "creator": "Ocean Surface Topography Science Team",
-            "title": "Sentinel-6A MF Jason-CS L1B P4 Altimeter Low Resolution (LR) NTC Geolocated Waveforms F08",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L1B_ALT_LR_NTC_F.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Provides reprocessed L1B low resolution (LR) non-time critical (NTC; 60-day latency) altimetry data from the Poseidon-4 SAR altimeter on the Sentinel-6A Michael Freilich spacecraft which include the geolocated, fully-calibrated pulse-limited LR power echoes. The S6A NTC product is analogous to the Jason-3 GDR product.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FS6AP4-1BLNTR-F08",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FS6AP4-1BLNTR-F08",
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
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/dataset/JASON_CS_S6A_L1B_ALT_LR_NTC_F08",
-                    "description": "Data Set Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Landing Page",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/dataset/JASON_CS_S6A_L1B_ALT_LR_NTC_F08",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L1B_ALT_LR_NTC_F.jpg",
-                    "description": "Thumbnail image for Website",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail image for Website",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L1B_ALT_LR_NTC_F.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2619443901-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2619443901-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2619443901-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2619443901-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail image for Website",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L1B_ALT_LR_NTC_F.jpg",
+            "identifier": "C2619443901-POCLOUD",
+            "issued": "2020-12-17",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "sea surface topography",
+                "ocean waves"
+            ],
+            "landingPage": "https://doi.org/10.5067/S6AP4-1BLNTR-F08",
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
+            "title": "Sentinel-6A MF Jason-CS L1B P4 Altimeter Low Resolution (LR) NTC Geolocated Waveforms F08"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GQEKE2O8RJMY",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Charles Gatebe; Michael King; Rajesh Poudyal. 2019-03-06. CAR_SNOWEX17_BRDF. Version 2. CAR SnowEx17 BRDF Measurements L1 V2. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GQEKE2O8RJMY. https://disc.gsfc.nasa.gov/datacollection/CAR_SNOWEX17_BRDF_2.html.",
-            "issued": "2019-01-27",
-            "temporal": "2017-02-16T00:00:00Z/2017-02-22T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-01-27",
-            "keyword": [
-                "earth science",
-                "surface radiative properties",
-                "atmosphere",
-                "land surface",
-                "atmospheric radiation",
-                "oceans",
-                "ocean optics"
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
-            "identifier": "C1617621734-GES_DISC",
-            "description": "SnowEx is a multi-year airborne project to help advance capabilities, and plan for a near-future space mission to monitor global seasonal snow water equivalent - currently an inconsistently collected and difficult-to-obtain data point that scientists say is critical to understanding the world's water resources.\n\nThis data set consists of observations made with the CAR instrument and includes values for bidirectional reflectance factor at varying spectral bands.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "CAR_SNOWEX17_BRDF",
             "creator": "Charles Gatebe; Michael King; Rajesh Poudyal",
-            "title": "CAR SnowEx17 BRDF Measurements L1 V2 (CAR_SNOWEX17_BRDF) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/CAR_SNOWEX17_L1C_1.png",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "SnowEx is a multi-year airborne project to help advance capabilities, and plan for a near-future space mission to monitor global seasonal snow water equivalent - currently an inconsistently collected and difficult-to-obtain data point that scientists say is critical to understanding the world's water resources.\n\nThis data set consists of observations made with the CAR instrument and includes values for bidirectional reflectance factor at varying spectral bands.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGQEKE2O8RJMY",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGQEKE2O8RJMY",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1494371,430 +1494345,434 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CAR_SNOWEX17_BRDF_2.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CAR_SNOWEX17_BRDF_2.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/CAR/CAR_SNOWEX17_BRDF.2/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/CAR/CAR_SNOWEX17_BRDF.2/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/CAR/CAR_SNOWEX17_BRDF.2/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/CAR/CAR_SNOWEX17_BRDF.2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=CAR_SNOWEX17_BRDF",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=CAR_SNOWEX17_BRDF",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/CAR_SNOWEX17_L1C_1.png",
+            "identifier": "C1617621734-GES_DISC",
+            "issued": "2019-01-27",
+            "keyword": [
+                "earth science",
+                "surface radiative properties",
+                "atmosphere",
+                "land surface",
+                "atmospheric radiation",
+                "oceans",
+                "ocean optics"
+            ],
+            "landingPage": "https://doi.org/10.5067/GQEKE2O8RJMY",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-01-27",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "CAR_SNOWEX17_BRDF",
             "spatial": "-108.24156 37.85813 -105.7035 39.3067",
+            "temporal": "2017-02-16T00:00:00Z/2017-02-22T23:59:59.999Z",
             "theme": [
                 "CAR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CAR SnowEx17 BRDF Measurements L1 V2 (CAR_SNOWEX17_BRDF) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/239/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2010-10-13",
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
-            "identifier": "DASHLINK_239",
             "description": "UNDERSTANDING SEVERE WEATHER PROCESSES THROUGH\r\nSPATIOTEMPORAL RELATIONAL RANDOM FORESTS\r\n\r\nAMY MCGOVERN, TIMOTHY SUPINIE, DAVID JOHN GAGNE II, NATHANIEL TROUTMAN,\r\nMATTHEW COLLIER, RODGER A. BROWN, JEFFREY BASARA, AND JOHN K. WILLIAMS\r\n\r\nAbstract. Major severe weather events can cause a significant loss of life and property. We\r\nseek to revolutionize our understanding of and ability to predict such events through the mining\r\nof severe weather data. Because weather is inherently a spatiotemporal phenomenon, mining\r\nsuch data requires a model capable of representing and reasoning about complex spatiotemporal\r\ndynamics, including temporally and spatially varying attributes and relationships. We introduce\r\nan augmented version of the Spatiotemporal Relational Random Forest, which is a Random Forest\r\nthat learns with spatiotemporally varying relational data. Our algorithm maintains the strength\r\nand performance of Random Forests but extends their applicability, including the estimation of\r\nvariable importance, to complex spatiotemporal relational domains. We apply the augmented\r\nSpatiotemporal Relational Random Forest to three severe weather data sets. These are: predicting\r\natmospheric turbulence across the continental United States, examining the formation of tornadoes\r\nnear strong frontal boundaries, and understanding the translation of drought across the southern\r\nplains of the United States. The results on such a wide variety of real-world domains demonstrate\r\nthe extensive applicability of the Spatiotemporal Relational Random Forest. Our long-term goal\r\nis to significantly improve the ability to predict and warn about severe weather events.",
-            "title": "UNDERSTANDING SEVERE WEATHER PROCESSES THROUGH SPATIOTEMPORAL RELATIONAL RANDOM FORESTS",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/Paper_17_.pdf",
-                    "description": "UNDERSTANDING SEVERE WEATHER PROCESSES THROUGH SPATIOTEMPORAL RELATIONAL RANDOM FORESTS",
                     "@type": "dcat:Distribution",
+                    "description": "UNDERSTANDING SEVERE WEATHER PROCESSES THROUGH SPATIOTEMPORAL RELATIONAL RANDOM FORESTS",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/Paper_17_.pdf",
+                    "mediaType": "application/pdf",
                     "title": "Paper 17 .pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_239",
+            "issued": "2010-10-13",
+            "keyword": [
+                "ames",
+                "nasa",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/239/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "UNDERSTANDING SEVERE WEATHER PROCESSES THROUGH SPATIOTEMPORAL RELATIONAL RANDOM FORESTS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/LWTYSMP3VM5Z",
             "citation": "Beaudoing, H. and M. Rodell, NASA/GSFC/HSL. 2020-01-30. GLDAS_NOAH10_M. Version 2.1. GLDAS Noah Land Surface Model L4 monthly 1.0 x 1.0 degree V2.1. Greenbelt, Maryland, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/LWTYSMP3VM5Z. https://disc.gsfc.nasa.gov/datacollection/GLDAS_NOAH10_M_2.1.html. Digital Science Data.",
-            "issued": "2020-01-30",
-            "temporal": "2000-01-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-30",
-            "references": [
-                "https://doi.org/10.1175/BAMS-85-3-381"
-            ],
-            "keyword": [
-                "atmospheric water vapor",
-                "atmospheric pressure",
-                "atmosphere",
-                "atmospheric radiation",
-                "atmospheric temperature",
-                "terrestrial hydrosphere",
-                "surface water",
-                "surface thermal properties",
-                "soils",
-                "snow/ice",
-                "precipitation",
-                "land surface",
-                "earth science",
-                "atmospheric winds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "HUALAN RUI",
                 "hasEmail": "mailto:Hualan.Rui@nasa.gov"
             },
+            "creator": "Beaudoing, H. and M. Rodell, NASA/GSFC/HSL",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1288937542-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "NASA Global Land Data Assimilation System Version 2 (GLDAS-2) has three components: GLDAS-2.0, GLDAS-2.1, and GLDAS-2.2.  GLDAS-2.0 is forced entirely with the Princeton meteorological forcing input data and provides a temporally consistent series from 1948 through 2014.  GLDAS-2.1 is forced with a combination of model and observation data from 2000 to present.  GLDAS-2.2 product suites use data assimilation (DA), whereas the GLDAS-2.0 and GLDAS-2.1 products are \"open-loop\" (i.e., no data assimilation).  The choice of forcing data, as well as DA observation source, variable, and scheme, vary for different GLDAS-2.2 products. \n\nGLDAS-2.1 data products are now available in two production streams: one stream is forced with combined forcing data including GPCP version 1.3 (the main production stream), and the other stream is processed without this forcing data (the early production stream). Since the GPCP Version 1.3 data have a 3-4 month latency, the GLDAS-2.1 data products are first created without it, and are designated as Early Products (EPs), with about 1.5 month latency. Once the GPCP Version 1.3 data become available, the GLDAS-2.1 data products are processed in the main production stream and are removed from the Early Products archive. \n\nThis data product, reprocessed in January 2020, is for GLDAS-2.1 Noah monthly 1.0 degree data from the main production stream and it is a replacement to its previous version.\n\nThe monthly data product was generated through temporal averaging of GLDAS-2.1 Noah 3-hourly data simulated with the Noah Model 3.6 in Land Information System (LIS) Version 7.  The data product contains 36 land surface fields from January 2000 to present. The GLDAS-2.1 data are archived and distributed in NetCDF format. The GLDAS-2.1 products supersede their corresponding GLDAS-1 products.\n\nThe GLDAS-2.1 simulation started on January 1, 2000 using the conditions from the GLDAS-2.0 simulation. This simulation was forced with National Oceanic and Atmospheric Administration (NOAA)/Global Data Assimilation System (GDAS) atmospheric analysis fields (Derber et al., 1991), the disaggregated Global Precipitation Climatology Project (GPCP) V1.3 Daily Analysis precipitation fields (Adler et al., 2003; Huffman et al., 2001), and the Air Force Weather Agency's AGRicultural METeorological modeling system (AGRMET) radiation fields.  The simulation used with GDAS and GPCP only from 2000 to February 2001, followed by addition of AGRMET for March 1, 2001 onwards.\n\nIn October 2020, all 3-hourly and monthly GLDAS-2 data were post-processed with the MOD44W MODIS land mask.  Previously, some grid boxes over inland water were considered as over land and, thus, had non-missing values.  The post-processing corrected this issue and masked out all model output data over inland water; the post-processing did not affect the meteorological forcing variables. More information can be found in the GLDAS-2 README.  The MOD44W MODIS land mask is available on the GLDAS Project site.\n\nIf you had downloaded the GLDAS data prior to November 2020, please download the data again to receive the post-processed data.",
-            "release-place": "Greenbelt, Maryland, USA",
-            "series-name": "GLDAS_NOAH10_M",
-            "creator": "Beaudoing, H. and M. Rodell, NASA/GSFC/HSL",
-            "graphic-preview-description": "GLDAS-2.1 Noah 3-ourly 1.0 Degree 0-10 cm Soil Moisture [kg m-2] for 00Z March 01, 2001.",
-            "title": "GLDAS Noah Land Surface Model L4 monthly 1.0 x 1.0 degree V2.1 (GLDAS_NOAH10_M) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GLDAS_NOAH10_M_2.1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FLWTYSMP3VM5Z",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FLWTYSMP3VM5Z",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GLDAS_NOAH10_M_2.1.png",
-                    "description": "GLDAS-2.1 Noah 3-ourly 1.0 Degree 0-10 cm Soil Moisture [kg m-2] for 00Z March 01, 2001.",
                     "@type": "dcat:Distribution",
+                    "description": "GLDAS-2.1 Noah 3-ourly 1.0 Degree 0-10 cm Soil Moisture [kg m-2] for 00Z March 01, 2001.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GLDAS_NOAH10_M_2.1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GLDAS_NOAH10_M_2.1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GLDAS_NOAH10_M_2.1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/GLDAS/GLDAS_NOAH10_M.2.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/GLDAS/GLDAS_NOAH10_M.2.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GLDAS_NOAH10_M_2.1",
-                    "description": "Use the Earthdata Search Client (EDSC) to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client (EDSC) to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GLDAS_NOAH10_M_2.1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/opendap/GLDAS/GLDAS_NOAH10_M.2.1/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/opendap/GLDAS/GLDAS_NOAH10_M.2.1/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/dods/GLDAS_NOAH10_M.2.1/",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/dods/GLDAS_NOAH10_M.2.1/",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/GLDAS/GLDAS_NOAH10_M.2.1/doc/README_GLDAS2.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/GLDAS/GLDAS_NOAH10_M.2.1/doc/README_GLDAS2.pdf",
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
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/thredds/catalog/GLDAS_aggregation/GLDAS_NOAH10_M.2.1/catalog.html",
-                    "description": "Time aggregated THREDDS Data Server (TDS)",
                     "@type": "dcat:Distribution",
+                    "description": "Time aggregated THREDDS Data Server (TDS)",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/thredds/catalog/GLDAS_aggregation/GLDAS_NOAH10_M.2.1/catalog.html",
+                    "mediaType": "text/html",
                     "title": "Use THREDDS DATA to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "GLDAS-2.1 Noah 3-ourly 1.0 Degree 0-10 cm Soil Moisture [kg m-2] for 00Z March 01, 2001.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GLDAS_NOAH10_M_2.1.png",
+            "identifier": "C1288937542-GES_DISC",
+            "issued": "2020-01-30",
+            "keyword": [
+                "atmospheric water vapor",
+                "atmospheric pressure",
+                "atmosphere",
+                "atmospheric radiation",
+                "atmospheric temperature",
+                "terrestrial hydrosphere",
+                "surface water",
+                "surface thermal properties",
+                "soils",
+                "snow/ice",
+                "precipitation",
+                "land surface",
+                "earth science",
+                "atmospheric winds"
+            ],
+            "landingPage": "https://doi.org/10.5067/LWTYSMP3VM5Z",
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
+            "series-name": "GLDAS_NOAH10_M",
             "spatial": "-180.0 -60.0 180.0 90.0",
+            "temporal": "2000-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "GLDAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GLDAS Noah Land Surface Model L4 monthly 1.0 x 1.0 degree V2.1 (GLDAS_NOAH10_M) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Texas_Ground_MoodyTower_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2022-08-22. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Texas_Ground_MoodyTower_Data_1.",
-            "issued": "2021-08-26",
-            "temporal": "2013-08-30T00:00:00Z/2013-10-02T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-08-22",
-            "keyword": [
-                "atmospheric chemistry",
-                "precipitation",
-                "aerosols",
-                "atmosphere",
-                "atmospheric pressure",
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "earth science"
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
-            "identifier": "C2417019933-LARC_ASDC",
             "description": "DISCOVERAQ_Texas_Ground_MoodyTower_Data contains data collected at the Moody Tower ground site during the Texas (Houston) deployment of NASA's DISCOVER-AQ field study. This data product contains data for only the Texas deployment and data collection is complete.\r\n\r\nUnderstanding the factors that contribute to near surface pollution is difficult using only satellite-based observations. The incorporation of surface-level measurements from aircraft and ground-based platforms provides the crucial information necessary to validate and expand upon the use of satellites in understanding near surface pollution. Deriving Information on Surface conditions from Column and Vertically Resolved Observations Relevant to Air Quality (DISCOVER-AQ) was a four-year campaign conducted in collaboration between NASA Langley Research Center, NASA Goddard Space Flight Center, NASA Ames Research Center, and multiple universities to improve the use of satellites to monitor air quality for public health and environmental benefit. Through targeted airborne and ground-based observations, DISCOVER-AQ enabled more effective use of current and future satellites to diagnose ground level conditions influencing air quality.\r\n\r\nDISCOVER-AQ employed two NASA aircraft, the P-3B and King Air, with the P-3B completing in-situ spiral profiling of the atmosphere (aerosol properties, meteorological variables, and trace gas species). The King Air conducted both passive and active remote sensing of the atmospheric column extending below the aircraft to the surface. Data from an existing network of surface air quality monitors, AERONET sun photometers, Pandora UV/vis spectrometers and model simulations were also collected. Further, DISCOVER-AQ employed many surface monitoring sites, with measurements being made on the ground, in conjunction with the aircraft. The B200 and P-3B conducted flights in Baltimore-Washington, D.C. in 2011, Houston, TX in 2013, San Joaquin Valley, CA in 2013, and Denver, CO in 2014. These regions were targeted due to being in violation of the National Ambient Air Quality Standards (NAAQS).\r\n\r\nThe first objective of DISCOVER-AQ was to determine and investigate correlations between surface measurements and satellite column observations for the trace gases ozone (O3), nitrogen dioxide (NO2), and formaldehyde (CH2O) to understand how satellite column observations can diagnose surface conditions. DISCOVER-AQ also had the objective of using surface-level measurements to understand how satellites measure diurnal variability and to understand what factors control diurnal variability. Lastly, DISCOVER-AQ aimed to explore horizontal scales of variability, such as regions with steep gradients and urban plumes.",
-            "title": "DISCOVER-AQ Texas Deployment Moody Tower Ground Site Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDISCOVERAQ_Texas_Ground_MoodyTower_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDISCOVERAQ_Texas_Ground_MoodyTower_Data_1",
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
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Texas_Ground_MoodyTower_Data_1",
-                    "description": "DOI for DISCOVERAQ_Texas_Ground_MoodyTower_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for DISCOVERAQ_Texas_Ground_MoodyTower_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Texas_Ground_MoodyTower_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2417019933-LARC_ASDC",
-                    "description": "Earthdata Search client for DISCOVERAQ_Texas_Ground_MoodyTower_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search client for DISCOVERAQ_Texas_Ground_MoodyTower_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2417019933-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/DISCOVER-AQ/Texas_Ground_MoodyTower_Data_1/",
-                    "description": "ASDC Direct Data Download for DISCOVERAQ_Texas_Ground_MoodyTower_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for DISCOVERAQ_Texas_Ground_MoodyTower_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/DISCOVER-AQ/Texas_Ground_MoodyTower_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/DISCOVER-AQ/Texas_Ground_MoodyTower_Data_1/contents.html",
-                    "description": "OPeNDAP data access for DISCOVERAQ_Texas_Ground_MoodyTower_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for DISCOVERAQ_Texas_Ground_MoodyTower_Data_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/DISCOVER-AQ/Texas_Ground_MoodyTower_Data_1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2417019933-LARC_ASDC",
+            "issued": "2021-08-26",
+            "keyword": [
+                "atmospheric chemistry",
+                "precipitation",
+                "aerosols",
+                "atmosphere",
+                "atmospheric pressure",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Texas_Ground_MoodyTower_Data_1",
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
+            "temporal": "2013-08-30T00:00:00Z/2013-10-02T23:59:59.999Z",
             "theme": [
                 "DISCOVER-AQ",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "DISCOVER-AQ Texas Deployment Moody Tower Ground Site Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA2008",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Schwartz, M., Livesey, N. and Read, W.. 2015-02-19. ML2GPH. Version 004. MLS/Aura Level 2 Geopotential Height V004. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA2008. https://disc.gsfc.nasa.gov/datacollection/ML2GPH_004.html. Digital Science Data.",
-            "issued": "2015-02-19",
-            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-02-19",
-            "keyword": [
-                "altitude",
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
-            "identifier": "C1251101402-GES_DISC",
-            "description": "ML2GPH is the EOS Aura Microwave Limb Sounder (MLS) standard product for geopotential height derived from radiances measured by the 118 and 240 GHz radiometers. The data version is 4.2. Data coverage is from August 8, 2004 to current. Spatial coverage is near-global (-82 degrees to +82 degrees latitude), with each profile spaced 1.5 degrees or ~165 km along the orbit track (roughly 15 orbits per day). The recommended useful vertical range is between 261 and 0.001 hPa, and the vertical resolution varies between ~3.6 and 6 km. Users of the ML2GPH data product should read section 3.8 of the EOS MLS Level 2 Version 4 Quality Document for more information.\n\nThe data are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5), which is based on the version 5 Hierarchical Data Format, or HDF-5. Each file contains two swath objects (profile and column data), each with a set of data and geolocation fields, swath attributes, and metadata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML2GPH",
             "creator": "Schwartz, M., Livesey, N. and Read, W.",
-            "title": "MLS/Aura Level 2 Geopotential Height V004 (ML2GPH) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2GPH_004.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "ML2GPH is the EOS Aura Microwave Limb Sounder (MLS) standard product for geopotential height derived from radiances measured by the 118 and 240 GHz radiometers. The data version is 4.2. Data coverage is from August 8, 2004 to current. Spatial coverage is near-global (-82 degrees to +82 degrees latitude), with each profile spaced 1.5 degrees or ~165 km along the orbit track (roughly 15 orbits per day). The recommended useful vertical range is between 261 and 0.001 hPa, and the vertical resolution varies between ~3.6 and 6 km. Users of the ML2GPH data product should read section 3.8 of the EOS MLS Level 2 Version 4 Quality Document for more information.\n\nThe data are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5), which is based on the version 5 Hierarchical Data Format, or HDF-5. Each file contains two swath objects (profile and column data), each with a set of data and geolocation fields, swath attributes, and metadata.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA2008",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA2008",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1494804,115 +1494782,113 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML2GPH_004.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML2GPH_004.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level2/ML2GPH.004/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level2/ML2GPH.004/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level2/ML2GPH.004/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level2/ML2GPH.004/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML2GPH_004",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML2GPH_004",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2GPH_004.png",
+            "identifier": "C1251101402-GES_DISC",
+            "issued": "2015-02-19",
+            "keyword": [
+                "altitude",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA2008",
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
+            "series-name": "ML2GPH",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MLS/Aura Level 2 Geopotential Height V004 (ML2GPH) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-08-31",
-            "temporal": "2021-08-31T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "iss",
-                "trajectory",
-                "topo",
-                "station",
-                "space",
-                "coordinates",
-                "coords",
-                "ephemeris",
-                "international",
-                "location"
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
-            "identifier": "nasa-iss-data_2021-08-31_uyd9-bu96",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2021-08-31",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1495035,474 +1495011,469 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2021-08-31_uyd9-bu96",
+            "issued": "2021-08-31",
+            "keyword": [
+                "iss",
+                "trajectory",
+                "topo",
+                "station",
+                "space",
+                "coordinates",
+                "coords",
+                "ephemeris",
+                "international",
+                "location"
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
+            "temporal": "2021-08-31T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2021-08-31"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43MA1N.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "LANCEMODIS. 2023-11-20. VIIRS/NPP BRDF/Albedo Model Parameters Daily L3 Global 1 km SIN Grid NRT. Version 2. NASA GSFC LANCE. Archived by National Aeronautics and Space Administration, U.S. Government, LANCEMODIS. https://doi.org/10.5067/VIIRS/VNP43MA1N.002. http://doi.org/10.5067/VIIRS/VNP43MA1N.002.",
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
-            "identifier": "C2807604939-LANCEMODIS",
-            "description": "The VIIRS/NPP BRDF/Albedo Model Parameters Daily L3 Global 1 km SIN Grid Near Real Time (NRT), short-name VNP43MA1N product provides BRDF/Albedo model parameters at 1 km resolution. The VNP43MA1N product is produced daily using 16-day VIIRS data (i.e., the current day and the previous 15 days). \r\n\r\nThe VNP43 algorithm uses the RossThick/Li-Sparse-Reciprocal (RTLSR) semi-empirical kernel-driven BRDF model, with the three kernel weights from VNP43MA1N to reconstruct surface anisotropic effects, correcting the directional reflectance to a common view geometry (VNP43MA4N), while also computing integrated black-sky albedo (BSA) at local solar noon and white-sky albedo (WSA) (VNP43MA3N). Researchers can use the BRDF model parameters with a simple polynomial, to obtain black-sky albedo at any solar illumination angle. Likewise, both the BSA and WSA Science Dataset (SDS) layers can be used with a simple polynomial, to manually estimate instantaneous actual albedo (blue-sky albedo). Additional details regarding the methodology are available in the Algorithm Theoretical Basis Document (ATBD) at https://www.umb.edu/editor_uploads/images/school_for_the_environment_cs/Viirs/VIIRS_ATBD_Apr_Jul2017.pdf\r\n\r\nThe VNP43MA1N data product provides a total of 24 SDS layers including: mandatory quality bands and three multi-dimensional model parameter bands representing fiso, fvol, and fgeo for VIIRS moderate resolution bands: M1-M5, M7-M8, and M10-M11.",
-            "release-place": "NASA GSFC LANCE",
             "creator": "LANCEMODIS",
-            "title": "VIIRS/NPP BRDF/Albedo Model Parameters Daily L3 Global 1km SIN Grid NRT",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The VIIRS/NPP BRDF/Albedo Model Parameters Daily L3 Global 1 km SIN Grid Near Real Time (NRT), short-name VNP43MA1N product provides BRDF/Albedo model parameters at 1 km resolution. The VNP43MA1N product is produced daily using 16-day VIIRS data (i.e., the current day and the previous 15 days). \r\n\r\nThe VNP43 algorithm uses the RossThick/Li-Sparse-Reciprocal (RTLSR) semi-empirical kernel-driven BRDF model, with the three kernel weights from VNP43MA1N to reconstruct surface anisotropic effects, correcting the directional reflectance to a common view geometry (VNP43MA4N), while also computing integrated black-sky albedo (BSA) at local solar noon and white-sky albedo (WSA) (VNP43MA3N). Researchers can use the BRDF model parameters with a simple polynomial, to obtain black-sky albedo at any solar illumination angle. Likewise, both the BSA and WSA Science Dataset (SDS) layers can be used with a simple polynomial, to manually estimate instantaneous actual albedo (blue-sky albedo). Additional details regarding the methodology are available in the Algorithm Theoretical Basis Document (ATBD) at https://www.umb.edu/editor_uploads/images/school_for_the_environment_cs/Viirs/VIIRS_ATBD_Apr_Jul2017.pdf\r\n\r\nThe VNP43MA1N data product provides a total of 24 SDS layers including: mandatory quality bands and three multi-dimensional model parameter bands representing fiso, fvol, and fgeo for VIIRS moderate resolution bands: M1-M5, M7-M8, and M10-M11.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43MA1N.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43MA1N.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/5200/VNP43MA1N/",
-                    "description": "Access VIIRS data set from the MODAPS/NRT server.",
                     "@type": "dcat:Distribution",
+                    "description": "Access VIIRS data set from the MODAPS/NRT server.",
+                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/5200/VNP43MA1N/",
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
+            "identifier": "C2807604939-LANCEMODIS",
+            "issued": "2023-11-20",
+            "keyword": [
+                "earth science",
+                "land surface",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43MA1N.002",
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
+            "title": "VIIRS/NPP BRDF/Albedo Model Parameters Daily L3 Global 1km SIN Grid NRT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RSI-1%2F2%2F3-CR2-0043-V1.0",
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
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This is a Solar Conjunction measurement covering the time 2006-04-26T00:04:09.500 to 2006-04-26T03:15:06.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rsi-1-2-3-cr2-0043-v1.0_uyhk-xuf9",
+            "issued": "2018-06-26",
+            "keyword": [
+                "sun",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RSI-1%2F2%2F3-CR2-0043-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rsi-1-2-3-cr2-0043-v1.0_uyhk-xuf9",
-            "description": "This is a Solar Conjunction measurement covering the time 2006-04-26T00:04:09.500 to 2006-04-26T03:15:06.500.",
-            "title": "ROSETTA-ORBITER SUN RSI 1/2/3 CRUISE 2 0043 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER SUN RSI 1/2/3 CRUISE 2 0043 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Suborbital/OWLETS-1/SherpaAircraft_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2021-01-27. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/Suborbital/OWLETS-1/SherpaAircraft_Data_1.",
-            "issued": "2020-11-18",
-            "temporal": "2017-07-07T00:00:00Z/2017-09-12T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-19",
-            "keyword": [
-                "atmospheric temperature",
-                "atmospheric chemistry",
-                "earth science",
-                "atmosphere",
-                "atmospheric winds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Timothy Berkoff",
                 "hasEmail": "mailto:timothy.a.berkoff@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1997466300-LARC_ASDC",
             "description": "OWLETS1_SherpaAircraft_Data_1 is the Ozone Water-Land Environmental Transition Study (OWLETS-1) data collected on board the Sherpa Aircraft. OWLETS was supported by the NASA Science Innovation Fund (SIF). Data include trace gas measurements, greenhouse gases, and aircraft navigational and housekeeping data collected via remote sensing and in-situ instrumentation. This collection features data from the GeoTASO instrument, a pre-cursor to the TEMPO satellite. Data collection is complete.\r\n\r\nCoastal regions have typically posed a challenge for air quality researchers due to a lack of measurements available over water and water-land boundary transitions. Supported by NASA\u2019s Science Innovation Fund (SIF), the Ozone Water-Land Environmental Transition Study (OWLETS) field campaign examined ozone concentrations and gradients over the Chesapeake Bay from July 5, 2017 \u2013 August 3, 2017, with twelve intensive measurement days occurring during this time period. OWLETS utilized a unique combination of instrumentation, including aircraft, TOLNet ozone lidars (NASA Goddard Space Flight Center Tropospheric Ozone Differential Absorption Lidar and NASA Langley Research Center Mobile Ozone Lidar), UAV/drones, ozonesondes, AERONET sun photometers, and mobile and ship-based measurements, to characterize the land-water differences in ozone and other pollutants. Two main research sites were established as part of the campaign: an over-land site at NASA LaRC, and an over-water site at the Chesapeake Bay Bridge Tunnel. These two research sites were established to provide synchronous vertical measurements of meteorology and pollutants over water and over land. In combination with mobile observations between the two sites, pollutant gradients were able to be observed and used to better understand the fundamental processes occurring at the land-water interface. OWLETS-2 was completed from June 6, 2018 \u2013 July 6, 2018 in the upper Chesapeake Bay region. Research sites were established at the University of Maryland, Baltimore County (UMBC), Hart Miller Island (HMI), and Howard University Beltsville (HUBV), with HMI representing the over-water location and UMBC and HUBV representing the over-land sites. Similar measurements were carried out to further characterize water-land gradients in the upper Chesapeake Bay. The measurements completed during OWLETS are of importance in enhancing air quality models, and improving future satellite retrievals, particularly, NASA\u2019s Tropospheric Emissions: Monitoring of Pollution, which is scheduled to launch in 2022.",
-            "title": "OWLETS-1 Sherpa Aircraft Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSuborbital%2FOWLETS-1%2FSherpaAircraft_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSuborbital%2FOWLETS-1%2FSherpaAircraft_Data_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://journals.ametsoc.org/bams/article/100/2/291/69189/The-Ozone-Water-Land-Environmental-Transition",
-                    "description": "The Ozone Water\u2013Land Environmental Transition Study: An Innovative Strategy for Understanding Chesapeake Bay Pollution Events",
                     "@type": "dcat:Distribution",
+                    "description": "The Ozone Water\u2013Land Environmental Transition Study: An Innovative Strategy for Understanding Chesapeake Bay Pollution Events",
+                    "downloadURL": "https://journals.ametsoc.org/bams/article/100/2/291/69189/The-Ozone-Water-Land-Environmental-Transition",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/feature/langley/nasa-chesapeake-bay-study-to-help-improve-air-quality-forecasts",
-                    "description": "NASA Chesapeake Bay Study To Help Improve Air-Quality Forecasts",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Chesapeake Bay Study To Help Improve Air-Quality Forecasts",
+                    "downloadURL": "https://www.nasa.gov/feature/langley/nasa-chesapeake-bay-study-to-help-improve-air-quality-forecasts",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
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
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/owlets/docs/OwletsSlides.pdf",
-                    "description": "Ozone Water-Land Environmental Transition Study (OWLETS) Introduction Presentation Slides",
                     "@type": "dcat:Distribution",
+                    "description": "Ozone Water-Land Environmental Transition Study (OWLETS) Introduction Presentation Slides",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/owlets/docs/OwletsSlides.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/Suborbital/OWLETS-1/SherpaAircraft_Data_1",
-                    "description": "DOI data set landing page for OWLETS1_SherpaAircraft_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for OWLETS1_SherpaAircraft_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/Suborbital/OWLETS-1/SherpaAircraft_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1997466300-LARC_ASDC",
-                    "description": "Earthdata Search for OWLETS1_SherpaAircraft_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for OWLETS1_SherpaAircraft_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1997466300-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/OWLETS/1_SherpaAircraft_Data_1/",
-                    "description": "ASDC Direct Data Download for OWLETS1_SherpaAircraft_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for OWLETS1_SherpaAircraft_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/OWLETS/1_SherpaAircraft_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/OWLETS/1_SherpaAircraft_Data_1/contents.html",
-                    "description": "OPeNDAP data access for OWLETS1_SherpaAircraft_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for OWLETS1_SherpaAircraft_Data_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/OWLETS/1_SherpaAircraft_Data_1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1997466300-LARC_ASDC",
+            "issued": "2020-11-18",
+            "keyword": [
+                "atmospheric temperature",
+                "atmospheric chemistry",
+                "earth science",
+                "atmosphere",
+                "atmospheric winds"
+            ],
+            "landingPage": "https://doi.org/10.5067/Suborbital/OWLETS-1/SherpaAircraft_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-04-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>35.0 -78.0 35.0 -74.0 40.0 -74.0 40.0 -78.0 35.0 -78.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2017-07-07T00:00:00Z/2017-09-12T23:59:59.999Z",
             "theme": [
                 "OWLETS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OWLETS-1 Sherpa Aircraft Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/HORN_ISLAND/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/HORN_ISLAND/DATA001.",
-            "issued": "2003-09-17",
-            "temporal": "2003-09-17T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "oceans",
-                "ocean optics",
-                "ocean chemistry",
-                "earth science",
-                "ocean temperature",
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
-            "identifier": "C1633360369-OB_DAAC",
             "description": "Measurements made in the northern part of the Gulf of Mexico near Horn Island in 2003.",
-            "title": "Optical measurements from  Horn Island, Mississippi in 2003",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FHORN_ISLAND%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FHORN_ISLAND%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Horn_Island/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Horn_Island/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360369-OB_DAAC",
+            "issued": "2003-09-17",
+            "keyword": [
+                "oceans",
+                "ocean optics",
+                "ocean chemistry",
+                "earth science",
+                "ocean temperature",
+                "salinity/density"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/HORN_ISLAND/DATA001",
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
+            "temporal": "2003-09-17T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Optical measurements from  Horn Island, Mississippi in 2003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/312",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Anderson, Darwin. 1998. BOREAS TE-01 Soils Data over the SSA Tower Sites in Raster Format. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/312",
-            "issued": "2023-11-22",
-            "temporal": "1994-01-01T00:00:00Z/1994-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-10",
-            "keyword": [
-                "earth science",
-                "soils",
-                "geomorphic landforms/processes",
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
-            "identifier": "C2927721796-ORNL_CLOUD",
             "description": "Gridded from vector layers of soil maps that were received from Dr. Darwin Anderson TE-01, who did the original soil mapping in the field during 1994. The vector layers were gridded into raster files that cover approximately 1 square kilometer over each of the SSA tower sites.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS TE-01 Soils Data over the SSA Tower Sites in Raster Format",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F312",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F312",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TE/soilte1r/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TE/soilte1r/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TE01_SSA_Soils_AEAC.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TE01_SSA_Soils_AEAC.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/312",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/312",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/soilte1r/comp/0_readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/soilte1r/comp/0_readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/soilte1r/comp/TE01_SSA_Soils_AEAC.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/soilte1r/comp/TE01_SSA_Soils_AEAC.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/soilte1r/comp/TE01_SSA_Soils_AEAC.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/soilte1r/comp/TE01_SSA_Soils_AEAC.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/soilte1r/comp/TE01_SSA_Soils_AEAC.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/soilte1r/comp/TE01_SSA_Soils_AEAC.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/soilte1r/comp/te01_ssa_soil_hdr.asc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/soilte1r/comp/te01_ssa_soil_hdr.asc",
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
+            "identifier": "C2927721796-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "earth science",
+                "soils",
+                "geomorphic landforms/processes",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/312",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-04-10",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-106.21 53.62 -104.61 54.0",
+            "temporal": "1994-01-01T00:00:00Z/1994-12-31T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS TE-01 Soils Data over the SSA Tower Sites in Raster Format"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-2-ESC4-MTP024-V1.0",
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
+            "description": "This data set contains count rates (1/s) as measured by the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, along with their standard deviations.  The primary target is comet 67P/Churyumov-Gerasimenko. These are CODMAC Level 2 Experiment Data Record data, and provide a measure of the radiation in the spacecraft environment during the Medium Term Plan 24 period of the ESCORT 4 mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-2-esc4-mtp024-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-2-ESC4-MTP024-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-2-esc4-mtp024-v1.0",
-            "description": "This data set contains count rates (1/s) as measured by the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, along with their standard deviations.  The primary target is comet 67P/Churyumov-Gerasimenko. These are CODMAC Level 2 Experiment Data Record data, and provide a measure of the radiation in the spacecraft environment during the Medium Term Plan 24 period of the ESCORT 4 mission phase.",
-            "title": "ROSETTA-ORBITER 67P SREM 2 ESCORT 4\n    MTP024 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P SREM 2 ESCORT 4\n    MTP024 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://techport.nasa.gov/view/10479",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2012-05-01",
-            "temporal": "2012-05-01T00:00:00Z/2015-05-01T00:00:00Z",
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
-                "project",
-                "nasa headquarters"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "George Komar",
                 "hasEmail": "mailto:george.komar@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Science Mission Directorate"
-            },
-            "identifier": "TECHPORT_10479",
             "description": "&lt;p&gt;\r\n\tDesign and fabricate a space-qualifiable, fully conductively cooled, 2-micron pulsed laser breadboard meeting the projected 3-D Winds mission requirements.&lt;br /&gt;\r\n\tUtilize improvements in key technologies including high-power, long life space proven 804 nm pump diodes; derated diode operation, and heat pipe conductive cooling.&lt;/p&gt;",
-            "title": "Design and Fabrication of a Breadboard, Fully Conductively Cooled, 2-Micron, Pulsed Laser for the 3-D Winds Decadal Survey Mission Project",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1495510,171 +1495481,179 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "TECHPORT_10479",
+            "issued": "2012-05-01",
+            "keyword": [
+                "active",
+                "project",
+                "nasa headquarters"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/10479",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:005"
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
+            "temporal": "2012-05-01T00:00:00Z/2015-05-01T00:00:00Z",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Design and Fabrication of a Breadboard, Fully Conductively Cooled, 2-Micron, Pulsed Laser for the 3-D Winds Decadal Survey Mission Project"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0708-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-13T21:25:50.000 to 2015-04-14T08:07:06.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0708-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0708-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0708-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-13T21:25:50.000 to 2015-04-14T08:07:06.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0708 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0708 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567576-USGS_LTA.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "USGS and NASA. USGS. GLS. Global Land Survey. USGS EROS. Archived by National Aeronautics and Space Administration, U.S. Government, USGS. Download.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EROS CENTER",
+                "hasEmail": "mailto:lta@usgs.gov"
+            },
+            "creator": "USGS and NASA",
+            "data-presentation-form": "Download",
+            "description": "The U.S. Geological Survey (USGS) and the National Aeronautics and Space Administration (NASA) collaborated on the creation of the global land datasets using Landsat data from 1972 through 2008. NASA and the USGS have again partnered to develop the Global Land Survey 2010 (GLS2010), a new global land data set with core acquisition dates of 2008-2011. This dataset consists of both Landsat TM and ETM+ images that meet quality and cloud cover standards established by the earlier GLS collections. Data acquired in 2011 were used to fill areas of low image quality or excessive cloud cover.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "\n         EarthExplorer\n      ",
+                    "downloadURL": "http://earthexplorer.usgs.gov",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                }
+            ],
+            "editor": "USGS",
+            "identifier": "C1220567576-USGS_LTA",
             "issued": "2019-09-20",
-            "temporal": "1970-01-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-03-25",
             "keyword": [
                 "land surface",
                 "earth science",
                 "topography",
                 "surface radiative properties"
             ],
-            "data-presentation-form": "Download",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EROS CENTER",
-                "hasEmail": "mailto:lta@usgs.gov"
-            },
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567576-USGS_LTA.html",
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
-            "identifier": "C1220567576-USGS_LTA",
-            "description": "The U.S. Geological Survey (USGS) and the National Aeronautics and Space Administration (NASA) collaborated on the creation of the global land datasets using Landsat data from 1972 through 2008. NASA and the USGS have again partnered to develop the Global Land Survey 2010 (GLS2010), a new global land data set with core acquisition dates of 2008-2011. This dataset consists of both Landsat TM and ETM+ images that meet quality and cloud cover standards established by the earlier GLS collections. Data acquired in 2011 were used to fill areas of low image quality or excessive cloud cover.",
-            "editor": "USGS",
             "release-place": "USGS EROS",
             "series-name": "GLS",
-            "creator": "USGS and NASA",
-            "title": "Global Land Survey",
-            "programCode": [
-                "026:001"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://earthexplorer.usgs.gov",
-                    "description": "\n         EarthExplorer\n      ",
-                    "@type": "dcat:Distribution",
-                    "title": "Download this dataset"
-                }
-            ],
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1970-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Land Survey"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-MAG-4-SUMM-S3COORDS-48.0SEC-V1.1",
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
-                "jupiter"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains calibrated magnetic field data acquired by the Voyager 1 Low Field Magnetometer (LFM) during the Jupiter encounter. Coverage begins in the solar wind inbound to Jupiter and continues past the last outbound bowshock crossing. The data are in System III (1965) (SYS3) coordinates and have been averaged from the 9.6 second summary data to a 48 second sample rate.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-mag-4-summ-s3coords-48.0sec-v1.1_uyvm-g8p6",
+            "issued": "2021-05-21",
+            "keyword": [
+                "voyager",
+                "jupiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-MAG-4-SUMM-S3COORDS-48.0SEC-V1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-mag-4-summ-s3coords-48.0sec-v1.1_uyvm-g8p6",
-            "description": "This data set contains calibrated magnetic field data acquired by the Voyager 1 Low Field Magnetometer (LFM) during the Jupiter encounter. Coverage begins in the solar wind inbound to Jupiter and continues past the last outbound bowshock crossing. The data are in System III (1965) (SYS3) coordinates and have been averaged from the 9.6 second summary data to a 48 second sample rate.",
-            "title": "VG1 JUP MAG RESAMPLED SYSTEM III (1965)\n                                        COORDS 48.0SEC V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG1 JUP MAG RESAMPLED SYSTEM III (1965)\n                                        COORDS 48.0SEC V1.1"
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
-                "annual report",
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
-            "identifier": "NASA-861__5",
             "description": "Academy of Program/Project & Engineering Leadership's Annual Report highlights the Academy's efforts to serve the NASA workforce's needs in adapting to the challenges of today and the future.",
-            "title": "Academy of Program/Project & Engineering Leadership Annual Publications",
-            "programCode": [
-                "026:045"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1495682,424 +1495661,425 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/P2Y",
+            "identifier": "NASA-861__5",
+            "issued": "2018-06-25",
+            "keyword": [
+                "annual report",
+                "appel",
+                "sharing",
+                "knowledge"
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-ESC2-67PCHURYUMOV-M16-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera during the COMET ESCORT 2 phase of the Rosetta mission at the comet 67P, covering the period from 2015-05-05T23:25:00.000 to 2015-06-02T23:24:59.000. This version V2.0 supersedes previous deliveries of the same dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-esc2-67pchuryumov-m16-v2.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "bias",
                 "dark",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-ESC2-67PCHURYUMOV-M16-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-esc2-67pchuryumov-m16-v2.0",
-            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera during the COMET ESCORT 2 phase of the Rosetta mission at the comet 67P, covering the period from 2015-05-05T23:25:00.000 to 2015-06-02T23:24:59.000. This version V2.0 supersedes previous deliveries of the same dataset.",
-            "title": "ROSETTA-ORBITER COMET ESCORT 2 OSINAC 2 EDR MTP016 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMET ESCORT 2 OSINAC 2 EDR MTP016 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1274625681-GES_DISC.html",
             "citation": "Goddard Laboratory for Atmospheres at NASA GSFC. 1995-01-01. TOVSAMNF. Version 01. TOVS GLA MONTHLY GRIDS from NOAA-9 V01. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/TOVSAMNF_01.html. Digital Science Data.",
-            "issued": "1984-12-31",
-            "temporal": "1984-12-31T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "1987-01-01",
-            "keyword": [
-                "atmospheric water vapor",
-                "clouds",
-                "earth science",
-                "oceans",
-                "atmospheric chemistry",
-                "ocean temperature",
-                "precipitation",
-                "atmosphere",
-                "atmospheric pressure",
-                "atmospheric radiation",
-                "atmospheric temperature"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JOEL SUSSKIND",
                 "hasEmail": "mailto:joel.susskind-1@nasa.gov"
             },
+            "creator": "Goddard Laboratory for Atmospheres at NASA GSFC",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1274625681-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "This dataset (TOVSAMNF) contains the TIROS Operational Vertical Sounder (TOVS) level 3 geophysical parameters derived using data from NOAA-9 and the physical retrieval method of Susskind et al. (1984) and processed by the Satellite Data Utilization Office of the Goddard Laboratory for Atmospheres at NASA/GSFC. This method, which is hydrodynamic model- and a priori data-dependent, is designated as the so-called Path A scheme by the TOVS Pathfinder Science Working Group. The 20 channel High resolution Infrared Radiation Sounder 2 (HIRS2) and the 4 channel Microwave Sounding Unit (MSU) aboard the NOAA-xx series of Polar Orbiting Satellites are used to produce global fields of the 3-dimensional temperature-moisture structure of the atmosphere. In addition to profiles of temperature and moisture, the HIRS2/MSU data are used to derive important quantities such as land and sea surface temperature, outgoing longwave radiation, cloud fraction, cloudtop height, total ozone overburden and precipitation estimates.\n\nThe Path A system steps through an interactive forecast-retrieval-analysis cycle. In each 6 hour synoptic period, a 2nd order General Circulation Model (Takacs et al., 1994) is used to generate the 6 hour forecast fields of temperature and humidity. These global fields are used as the first guess for all soundings occuring within a 6 hour time window centered upon the forecast time. These retrievals are then assimilated with all available insitu measurements (such as radiosonde and ship reports) in the 6 hour interval using an Optimal Interpolation (OI) analysis scheme developed by the Data Assimilation Office of the Goddard Laboratory for Atmospheres. This analysis is then used to specify the initial conditions for the next 6 hour forecast, thus completing the cycle.\n\nThe retrieval algorithm itself is a physical method based on the iterative relaxation technique originally proposed by Chahine (1968). The basic approach consists of modifying the temperature profile from the previous iteration by an amount proportional to the difference between the observed brightness temperatures and the brightness temperatures computed from the trial parameters using the full radiative transfer equation applied at the observed satellite zenith angle. For the case of the temperature profile, the updated layer mean temperatures are given as a linear combination of multichannel brightness temperature differences with the coefficients given by the channel weighting functions. Constraints are imposed upon the solution in order to ensure stability and convergence of the iterative process. For more details see Susskind et al (1984).\n\nThere are level 3 data product files for five TOVS satellites, each of which is in the HDF format and each representative of a different averaging time period. All files contain the same number of geophysical parameter arrays stored as HDF Scientific Data Sets (SDSs). The time periods include daily, 5 day (pentad) and monthly, with the AM and PM portions of the orbits treated separately.  All data are mapped to a 1 degree longitude by 1 degree latitude global grid.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TOVSAMNF",
-            "creator": "Goddard Laboratory for Atmospheres at NASA GSFC",
-            "title": "TOVS GLA MONTHLY GRIDS from NOAA-9 V01 (TOVSAMNF) at GES DISC",
-            "graphic-preview-description": "TOVSAMNF image",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOVSAMNF_01.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOVSAMNF_01.png",
-                    "description": "TOVSAMNF image",
                     "@type": "dcat:Distribution",
+                    "description": "TOVSAMNF image",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOVSAMNF_01.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TOVSAMNF_01.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TOVSAMNF_01.html",
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
-                    "downloadURL": "https://disc1.gesdisc.eosdis.nasa.gov/data/tovs/TOVSAMNF",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://disc1.gesdisc.eosdis.nasa.gov/data/tovs/TOVSAMNF",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TOVSAMNF+001",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TOVSAMNF+001",
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
-                    "description": "This document is a TOVS legacy data guide.  Some information may be obsolete.",
                     "@type": "dcat:Distribution",
+                    "description": "This document is a TOVS legacy data guide.  Some information may be obsolete.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TOVS/TOVS_PATHFINDER_PATH_A_DATASET_GUIDE.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "TOVSAMNF image",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOVSAMNF_01.png",
+            "identifier": "C1274625681-GES_DISC",
+            "issued": "1984-12-31",
+            "keyword": [
+                "atmospheric water vapor",
+                "clouds",
+                "earth science",
+                "oceans",
+                "atmospheric chemistry",
+                "ocean temperature",
+                "precipitation",
+                "atmosphere",
+                "atmospheric pressure",
+                "atmospheric radiation",
+                "atmospheric temperature"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1274625681-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1987-01-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "TOVSAMNF",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1984-12-31T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "TOVS Pathfinder",
                 "CWIC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TOVS GLA MONTHLY GRIDS from NOAA-9 V01 (TOVSAMNF) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/0X6PTK8V19M8",
             "citation": "Chris Barnet. 2019-12-15. SNDRJ1IML3SMCCP. Version 2. Sounder SIPS: JPSS-1 CrIS Level 3 Specific Quality Control Gridded Monthly CLIMCAPS V2. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/0X6PTK8V19M8. https://disc.gsfc.nasa.gov/datacollection/SNDRJ1IML3SMCCP_2.html. Digital Science Data.",
-            "issued": "2018-02-01",
-            "temporal": "2018-02-01T00:00:00Z/2024-12-30T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-01",
-            "references": [
-                "https://doi.org/10.3390/rs11101227",
-                "https://doi.org/10.1109/TGRS.2012.2220369",
-                "https://doi.org/10.1016/S0022-4073(97)00169-6",
-                "https://doi.org/10.1109/TGRS.2002.808236",
-                "https://doi.org/10.1029/2005/JD007020",
-                "https://doi.org/10.5194/amt-13-4437-2020"
-            ],
-            "keyword": [
-                "earth science",
-                "clouds",
-                "air quality",
-                "atmosphere",
-                "atmospheric chemistry",
-                "atmospheric pressure",
-                "ocean temperature",
-                "precipitation",
-                "surface radiative properties",
-                "atmospheric radiation",
-                "surface thermal properties",
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "oceans",
-                "land surface",
-                "altitude"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Lena Iredell",
                 "hasEmail": "mailto:lena.iredell@nasa.gov"
             },
+            "creator": "Chris Barnet",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1692982099-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
             "description": "WARNING: To users of the derived product \u201cco_mmr_midtrop\u201d (carbon monoxide mass mixing ratio to dry air [kg/kg] at ~500 hPa). This variable has a significant bias due to a conversion error: the molecular weight of carbon dioxide (CO2, 44.01 g/mol) was used instead of carbon monoxide (CO, 28.01 g/mol). To correct, simply multiply \u201cco_mmr_midtrop\u201d by 28.01/44.01. Alternatively, derive a profile of mass mixing ratio from scratch using the retrieved column density values (\u201cmol_lay/co_mol_lay\u201d) in the Level 2 files. For further questions or concerns please contact the Sounder SIPS at: sounder.sips@jpl.nasa.gov\n\nThe CLIMCAPS (Community Long-term Infrared Microwave Coupled Product System) algorithm is used to analyze data from the Cross-track Infrared Sounder/Advanced Technology Microwave Sounder (CrIS/ATMS) instruments, also known as CrIMSS (Cross-track Infrared and Microwave Sounding Suite). The CrIS/ATMS instruments used for this product are on board the NOAA-20 platform, also known as JPSS-1. The CrIS instrument is a Fourier transform spectrometer with a total of 2211 FSR (Full Spectral Resolution) infrared sounding channels covering the longwave (645-1095 cm-1), midwave (1210-1750 cm-1), and shortwave (2100-2550 cm-1) spectral regions. The ATMS instrument  is a cross-track scanner with 22 channels in spectral bands from 23 GHz through 183 GHz.\n \nThe CLIMCAPS algorithm uses an Optimal Estimation methodology and uses an a-priori first guess to start the process. A CLIMCAPS sounding is comprised of a set of parameters that characterizes the full atmospheric state and includes a variety of geophysical parameters derived from the CrIMSS data. These include surface temperature and infrared emissivity; full atmosphere profiles of temperature, water vapor and ozone; infrared effective cloud top characteristics; carbon monoxide, methane, carbon dioxide, sulfur dioxide, nitrous oxide, and nitric acid.\n \nThis monthly one degree latitude by one degree longitude level-3 product starts with level-2 retrieval products with QC values of 0 (best), 1 (good), and 2 (don't use) which are provided for each variable. Specific QC accepts profile level from the top of the atmosphere down to the level where the QC determines that it is still good. Below this level, the data is rejected.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "SNDRJ1IML3SMCCP",
-            "creator": "Chris Barnet",
-            "graphic-preview-description": "Sample plot of CrIS/ATMS Level 3 monthly surface skin temperature (K).",
-            "title": "Sounder SIPS: JPSS-1 CrIS Level 3 Specific Quality Control Gridded Monthly CLIMCAPS V2 (SNDRJ1IML3SMCCP) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRJ1IML3SMCCP_2.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F0X6PTK8V19M8",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F0X6PTK8V19M8",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRJ1IML3SMCCP_2.png",
-                    "description": "Sample plot of CrIS/ATMS Level 3 monthly surface skin temperature (K).",
                     "@type": "dcat:Distribution",
+                    "description": "Sample plot of CrIS/ATMS Level 3 monthly surface skin temperature (K).",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRJ1IML3SMCCP_2.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRJ1IML3SMCCP_2.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRJ1IML3SMCCP_2.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/JPSS1_Sounder_Level3/SNDRJ1IML3SMCCP.2/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/JPSS1_Sounder_Level3/SNDRJ1IML3SMCCP.2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/JPSS1_Sounder_Level3/SNDRJ1IML3SMCCP.2/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/JPSS1_Sounder_Level3/SNDRJ1IML3SMCCP.2/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRJ1IML3SMCCP+2",
-                    "description": "Search the Earthdata website",
                     "@type": "dcat:Distribution",
+                    "description": "Search the Earthdata website",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRJ1IML3SMCCP+2",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRJ1IML3SMCCP_2.png",
+            "identifier": "C1692982099-GES_DISC",
+            "issued": "2018-02-01",
+            "keyword": [
+                "earth science",
+                "clouds",
+                "air quality",
+                "atmosphere",
+                "atmospheric chemistry",
+                "atmospheric pressure",
+                "ocean temperature",
+                "precipitation",
+                "surface radiative properties",
+                "atmospheric radiation",
+                "surface thermal properties",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "oceans",
+                "land surface",
+                "altitude"
+            ],
+            "landingPage": "https://doi.org/10.5067/0X6PTK8V19M8",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-11-01",
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
+            "series-name": "SNDRJ1IML3SMCCP",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-02-01T00:00:00Z/2024-12-30T00:00:00Z",
             "theme": [
                 "JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sounder SIPS: JPSS-1 CrIS Level 3 Specific Quality Control Gridded Monthly CLIMCAPS V2 (SNDRJ1IML3SMCCP) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-REMS-6-ADR-V1.0",
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
+            "description": "Ancillary data used in the processing of the data taken by the sensors of the Rover Environmental Monitoring Station (REMS) aboard the  Mars Science Laboratory.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-rems-6-adr-v1.0_uz5s-cnie",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars science laboratory",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-REMS-6-ADR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-rems-6-adr-v1.0_uz5s-cnie",
-            "description": "Ancillary data used in the processing of the data taken by the sensors of the Rover Environmental Monitoring Station (REMS) aboard the  Mars Science Laboratory.",
-            "title": "MSL MARS ROVER ENV MONITORING STATION \n                                      6 ADR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MSL MARS ROVER ENV MONITORING STATION \n                                      6 ADR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMAG-3-ESC1-CALIBRATED-V6.0",
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
+            "description": "This dataset contains CALIBRATED (CODMAC LEVEL 3) DATA of the COMET\nESCORT 1 Phase from November 22, 2014 until March 10, 2015 of the\nROSETTA orbiter magnetometer RPCMAG. Observations are done in the\nvicinity of comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1).\nThe current version of the dataset is V6.0, the first one\nbeing archived.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmag-3-esc1-calibrated-v6.0_uz6v-9nrc",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMAG-3-ESC1-CALIBRATED-V6.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmag-3-esc1-calibrated-v6.0_uz6v-9nrc",
-            "description": "This dataset contains CALIBRATED (CODMAC LEVEL 3) DATA of the COMET\nESCORT 1 Phase from November 22, 2014 until March 10, 2015 of the\nROSETTA orbiter magnetometer RPCMAG. Observations are done in the\nvicinity of comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1).\nThe current version of the dataset is V6.0, the first one\nbeing archived.",
-            "title": "ROSETTA-ORBITER 67P RPCMAG 3 ESC1 CALIBRATED V6.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCMAG 3 ESC1 CALIBRATED V6.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-LECP-3-RDR-STEP-48SEC-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This far encounter step data set consists of the counting rate and flux data for electrons and ions from the Low Energy Charged Particle (LECP) experiment on Voyager 2 while the spacecraft was within the vicinity of Jupiter. This instrument measures the intensities of in-situ charged particles ( >13 keV electrons and >24 keV ions) with various levels of discrimination based on energy range and mass species. A subset of almost 100 LECP channels are included in this data set. The LECP data are globally calibrated to the extent possible.  Particles include electrons, protons, alpha particles, and light, medium, and heavy nuclei particles.  The far encounter data are 48.0 second rate and flux measurements within 1/8 of the LECP instrumental motor rotation period (the angular scanning periods, or step period).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-lecp-3-rdr-step-48sec-v1.0_uz7k-qkht",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "jupiter",
                 "voyager"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-LECP-3-RDR-STEP-48SEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-lecp-3-rdr-step-48sec-v1.0_uz7k-qkht",
-            "description": "This far encounter step data set consists of the counting rate and flux data for electrons and ions from the Low Energy Charged Particle (LECP) experiment on Voyager 2 while the spacecraft was within the vicinity of Jupiter. This instrument measures the intensities of in-situ charged particles ( >13 keV electrons and >24 keV ions) with various levels of discrimination based on energy range and mass species. A subset of almost 100 LECP channels are included in this data set. The LECP data are globally calibrated to the extent possible.  Particles include electrons, protons, alpha particles, and light, medium, and heavy nuclei particles.  The far encounter data are 48.0 second rate and flux measurements within 1/8 of the LECP instrumental motor rotation period (the angular scanning periods, or step period).",
-            "title": "VG2 LECP 48.0 SECOND JUPITER FAR ENCOUNTER STEP DATA",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG2 LECP 48.0 SECOND JUPITER FAR ENCOUNTER STEP DATA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/uz9e-thad",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "apps",
-                "planets",
-                "global mosaic",
-                "nga",
-                "reflectance",
-                "space science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Joshua Rodriguez",
                 "hasEmail": "mailto:joshua.rodriguez@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-0000103",
             "description": "Planet Counter: Keep track of the latest planet discoveries on your desktop. New and updates about quest to discover exoplanets.",
-            "title": "Planet Quest",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1496107,822 +1496087,824 @@
                     "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "NASA-0000103",
+            "issued": "2018-06-25",
+            "keyword": [
+                "apps",
+                "planets",
+                "global mosaic",
+                "nga",
+                "reflectance",
+                "space science"
+            ],
+            "landingPage": "https://data.nasa.gov/d/uz9e-thad",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "title": "Planet Quest"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=SDU-C-DYNSCI-2-WILD2-V1.0",
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
+            "description": "This data set contains data from the Dynamic Science Experiment conducted during the Stardust encounter with comet Wild 2 on January 2, 2004. The data in this archive are organized into two tables in standard PDS format. The first of these tables provides high rate attitude control system (ACS) data spanning 40 minutes around closest approach while the second table provides attitude control thruster firing information (aka ``small forces'') spanning 3 hours around closest approach.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.sdu-c-dynsci-2-wild2-v1.0_uz9h-4j8t",
+            "issued": "2021-05-21",
+            "keyword": [
+                "81p/wild 2 (1978 a2)",
+                "stardust"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=SDU-C-DYNSCI-2-WILD2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.sdu-c-dynsci-2-wild2-v1.0_uz9h-4j8t",
-            "description": "This data set contains data from the Dynamic Science Experiment conducted during the Stardust encounter with comet Wild 2 on January 2, 2004. The data in this archive are organized into two tables in standard PDS format. The first of these tables provides high rate attitude control system (ACS) data spanning 40 minutes around closest approach while the second table provides attitude control thruster firing information (aka ``small forces'') spanning 3 hours around closest approach.",
-            "title": "STARDUST WILD 2 ENCOUNTER DYNAMIC SCIENCE EXPERIMENT DATA",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "STARDUST WILD 2 ENCOUNTER DYNAMIC SCIENCE EXPERIMENT DATA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/CYGNS-L1F30",
             "citation": "CYGNSS. 2020-11-30. CYGNSS Level 1 Full Delay Doppler Map Data Record. Version 3.0. CYGNSS Level 1 Full Delay Doppler Map Data Record Version 3.0. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/CYGNS-L1F30. https://cygnss.engin.umich.edu/. CYGNSS, PO.DAAC, 2020-11-30, CYGNSS Level 1 Full Delay Doppler Map Data Record Version 3.0, https://cygnss.engin.umich.edu/.",
-            "issued": "2020-11-13",
-            "temporal": "2018-08-06T00:00:01Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-13",
-            "references": [
-                "https://doi.org/10.1109/JSTARS.2018.2832981"
-            ],
-            "keyword": [
-                "radar",
-                "earth science",
-                "spectral/engineering"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
             },
-            "identifier": "C2205121474-POCLOUD",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "description": "This Level 1 (L1) dataset contains the Version 3.0 (v3.0) Full Delay Doppler Map (DDM) sensor data from the Delay Doppler Mapping Instrument aboard the CYGNSS satellite constellation. The primary CYGNSS instrument, also known as the Delay-Doppler Mapping Instrument (DDMI), measures the incoming radio frequency (RF) streams from three input antenna channels (2 nadir oriented science antennas and one zenith oriented navigation antenna) and processes them in real time into DDMs, which are two-dimensional maps of the signal scattered from the Earth surface as a function of propagation time delay and Doppler frequency shift. DDMs are normally sampled over a restricted range of delay and Doppler values centered on the values at the specular point of reflection. The bit resolution of scattered signal strength is also truncated by a lossy data compression algorithm. Full DDMs are sampled over a wider range of delay and Doppler values and retain their full (lossless) bit resolution. Full DDM data records are typically 10-15 min in duration and are initiated by ground commands to coincide with an overpass by one of the spacecraft of a target area of interest. This version supersedes the Full DDM Version 1.0 (https://doi.org/10.5067/CYGNS-L1FDD) for data retrieved during or after August 2018. For data retrieved prior to August 2018, users will need to continue using the Full DDM Version 1.0. This version links the Full DDMs to the CYGNSS v3.0 L1 files (https://doi.org/10.5067/CYGNS-L1X30) whereas the version 1.0 Full DDM linked the Full DDMs to the CYGNSS v2.1 L1 files (https://doi.org/10.5067/CYGNS-L1X21). The calibration of the Full DDMs has not been modified for this release.",
-            "release-place": "PO.DAAC",
-            "series-name": "CYGNSS Level 1 Full Delay Doppler Map Data Record",
             "creator": "CYGNSS",
-            "title": "CYGNSS Level 1 Full Delay Doppler Map Data Record Version 3.0",
-            "graphic-preview-description": "Thumbnail",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_L1_FULL_DDM_V3.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This Level 1 (L1) dataset contains the Version 3.0 (v3.0) Full Delay Doppler Map (DDM) sensor data from the Delay Doppler Mapping Instrument aboard the CYGNSS satellite constellation. The primary CYGNSS instrument, also known as the Delay-Doppler Mapping Instrument (DDMI), measures the incoming radio frequency (RF) streams from three input antenna channels (2 nadir oriented science antennas and one zenith oriented navigation antenna) and processes them in real time into DDMs, which are two-dimensional maps of the signal scattered from the Earth surface as a function of propagation time delay and Doppler frequency shift. DDMs are normally sampled over a restricted range of delay and Doppler values centered on the values at the specular point of reflection. The bit resolution of scattered signal strength is also truncated by a lossy data compression algorithm. Full DDMs are sampled over a wider range of delay and Doppler values and retain their full (lossless) bit resolution. Full DDM data records are typically 10-15 min in duration and are initiated by ground commands to coincide with an overpass by one of the spacecraft of a target area of interest. This version supersedes the Full DDM Version 1.0 (https://doi.org/10.5067/CYGNS-L1FDD) for data retrieved during or after August 2018. For data retrieved prior to August 2018, users will need to continue using the Full DDM Version 1.0. This version links the Full DDMs to the CYGNSS v3.0 L1 files (https://doi.org/10.5067/CYGNS-L1X30) whereas the version 1.0 Full DDM linked the Full DDMs to the CYGNSS v2.1 L1 files (https://doi.org/10.5067/CYGNS-L1X21). The calibration of the Full DDMs has not been modified for this release.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCYGNS-L1F30",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCYGNS-L1F30",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/148-0397-1_ATBD_L1_RawIF_FullDDM.pdf",
-                    "description": "Algorithm Theoretical Basis Document (ATBD) for the CYGNSS Level 1 Full DDM and Raw IF Datasets, S. Gleason, S. Musko, CYGNSS Project Document 148-0397-01, Rev 1, 22 June 2020",
                     "@type": "dcat:Distribution",
+                    "description": "Algorithm Theoretical Basis Document (ATBD) for the CYGNSS Level 1 Full DDM and Raw IF Datasets, S. Gleason, S. Musko, CYGNSS Project Document 148-0397-01, Rev 1, 22 June 2020",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/148-0397-1_ATBD_L1_RawIF_FullDDM.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/148-0137_ATBD_L1B_DDMCalibration_Rev2_Aug2018_release.pdf",
-                    "description": "Level 1B DDM Calibration Algorithm Theoretical Basis Document, S. Gleason, CYGNSS Project Document 148-0137, Rev 2, 20 Aug. 2018.",
                     "@type": "dcat:Distribution",
+                    "description": "Level 1B DDM Calibration Algorithm Theoretical Basis Document, S. Gleason, CYGNSS Project Document 148-0137, Rev 2, 20 Aug. 2018.",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/148-0137_ATBD_L1B_DDMCalibration_Rev2_Aug2018_release.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/forum/viewtopic.php?f=16&t=1261",
-                    "description": "Forum Post Capturing Changes to CYGNSS Sampling Rate",
                     "@type": "dcat:Distribution",
+                    "description": "Forum Post Capturing Changes to CYGNSS Sampling Rate",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/forum/viewtopic.php?f=16&t=1261",
+                    "mediaType": "text/html",
                     "title": "View this dataset's documented anomalies"
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
-                    "downloadURL": "https://docs.google.com/spreadsheets/d/1OZ5OlQU5mnIL0_cmZhdub8dz6x4JTOTGAWqndkBptO4/edit?usp=sharing",
-                    "description": "CYGNSS Targeting Information for Full DDM Data",
                     "@type": "dcat:Distribution",
+                    "description": "CYGNSS Targeting Information for Full DDM Data",
+                    "downloadURL": "https://docs.google.com/spreadsheets/d/1OZ5OlQU5mnIL0_cmZhdub8dz6x4JTOTGAWqndkBptO4/edit?usp=sharing",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/148-0373_Full_DDM_netCDF_Data_Dictionary.xlsx",
-                    "description": "Level 1 Full DDM netCDF Data Dictionary",
                     "@type": "dcat:Distribution",
+                    "description": "Level 1 Full DDM netCDF Data Dictionary",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/148-0373_Full_DDM_netCDF_Data_Dictionary.xlsx",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/148-0136_ATBD_L1A_DDMCalibration_Rev2_Aug2018_release.pdf",
-                    "description": "Level 1A DDM Calibration Algorithm Theoretical Basis Document, S. Gleason, CYGNSS Project Document 148-0136, Rev 2, 20 Aug. 2018.",
                     "@type": "dcat:Distribution",
+                    "description": "Level 1A DDM Calibration Algorithm Theoretical Basis Document, S. Gleason, CYGNSS Project Document 148-0136, Rev 2, 20 Aug. 2018.",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/148-0136_ATBD_L1A_DDMCalibration_Rev2_Aug2018_release.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://cygnss.engin.umich.edu/wp-content/uploads/sites/534/2021/06/CYGNSS_Handbook_April2016.pdf",
-                    "description": "Deriving Surface Winds from Tropical Cyclones",
                     "@type": "dcat:Distribution",
+                    "description": "Deriving Surface Winds from Tropical Cyclones",
+                    "downloadURL": "https://cygnss.engin.umich.edu/wp-content/uploads/sites/534/2021/06/CYGNSS_Handbook_April2016.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/sw/makefile_build_c/.gitkeep",
-                    "description": "C Source code for Makefile build to process Full DDMs",
                     "@type": "dcat:Distribution",
+                    "description": "C Source code for Makefile build to process Full DDMs",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/sw/makefile_build_c/.gitkeep",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1109/TGRS.2015.2502245",
-                    "description": "Gleason, S., C. Ruf, M. P. Clarizia, A. O'Brien, 'Calibration and Unwrapping of the Normalized Scattering Cross Section for the Cyclone Global Navigation Satellite System (CYGNSS)', IEEE Trans. Geosci. Remote Sens., doi:10.1109/TGRS.2015.2502245, 2016.",
                     "@type": "dcat:Distribution",
+                    "description": "Gleason, S., C. Ruf, M. P. Clarizia, A. O'Brien, 'Calibration and Unwrapping of the Normalized Scattering Cross Section for the Cyclone Global Navigation Satellite System (CYGNSS)', IEEE Trans. Geosci. Remote Sens., doi:10.1109/TGRS.2015.2502245, 2016.",
+                    "downloadURL": "https://doi.org/10.1109/TGRS.2015.2502245",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/sw/CYGNSS_DDM_Processor_MakefileBuild.pdf",
-                    "description": "Describes the software workflow in processing the Full DDMs",
                     "@type": "dcat:Distribution",
+                    "description": "Describes the software workflow in processing the Full DDMs",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/sw/CYGNSS_DDM_Processor_MakefileBuild.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://journals.ametsoc.org/doi/10.1175/BAMS-D-14-00218.1",
-                    "description": "Ruf, C., R. Atlas, P. Chang, M. Clarizia, J. Garrison, S. Gleason, S. Katzberg, Z. Jelenak, J. Johnson, S. Majumdar, A. O'Brien, D. Posselt, A. Ridley, R. Rose, V. Zavorotny (2015). New Ocean Winds Satellite Mission to Probe Hurricanes and Tropical Convection. Bull. Amer. Meteor. Soc., doi:10.1175/BAMS-D-14-00218.1.",
                     "@type": "dcat:Distribution",
+                    "description": "Ruf, C., R. Atlas, P. Chang, M. Clarizia, J. Garrison, S. Gleason, S. Katzberg, Z. Jelenak, J. Johnson, S. Majumdar, A. O'Brien, D. Posselt, A. Ridley, R. Rose, V. Zavorotny (2015). New Ocean Winds Satellite Mission to Probe Hurricanes and Tropical Convection. Bull. Amer. Meteor. Soc., doi:10.1175/BAMS-D-14-00218.1.",
+                    "downloadURL": "https://journals.ametsoc.org/doi/10.1175/BAMS-D-14-00218.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_L1_FULL_DDM_V3.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_L1_FULL_DDM_V3.0.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2205121474-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2205121474-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2205121474-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2205121474-POCLOUD",
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
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_L1_FULL_DDM_V3.0.jpg",
+            "identifier": "C2205121474-POCLOUD",
+            "issued": "2020-11-13",
+            "keyword": [
+                "radar",
+                "earth science",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/CYGNS-L1F30",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-11-13",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.1109/JSTARS.2018.2832981"
+            ],
+            "release-place": "PO.DAAC",
+            "series-name": "CYGNSS Level 1 Full Delay Doppler Map Data Record",
             "spatial": "-180.0 -40.0 180.0 40.0",
+            "temporal": "2018-08-06T00:00:01Z/2023-02-28T00:00:00Z",
             "theme": [
                 "CYGNSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CYGNSS Level 1 Full Delay Doppler Map Data Record Version 3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/7FILV218JZA2",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "CALFIN Subseasonal Greenland Glacial Terminus Positions V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA NSIDC DAAC. https://doi.org/10.5067/7FILV218JZA2.",
-            "issued": "1972-09-06",
-            "temporal": "1972-09-06T00:00:00Z/2019-06-25T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-25",
-            "keyword": [
-                "glaciers/ice sheets",
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
-            "identifier": "C2116307977-NSIDC_ECS",
             "description": "This data set contains shapefiles of Greenland\u2019s glacial termini and basins for the years 1972 to 2019. These vector data were created from Landsat 1-8 satellite imagery using the Calving Front Machine (CALFIN) an automated processing workflow utilizing neural networks for extracting calving fronts from satellite images of marine-terminating glaciers.",
-            "title": "CALFIN Subseasonal Greenland Glacial Terminus Positions V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F7FILV218JZA2",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F7FILV218JZA2",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/OTHR/NSIDC-0764.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/OTHR/NSIDC-0764.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0764/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0764/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=NSIDC-0764+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=NSIDC-0764+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/7FILV218JZA2",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/7FILV218JZA2",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/7FILV218JZA2",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/7FILV218JZA2",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2116307977-NSIDC_ECS",
+            "issued": "1972-09-06",
+            "keyword": [
+                "glaciers/ice sheets",
+                "cryosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/7FILV218JZA2",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-06-25",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-75.0 60.0 -15.0 80.0",
+            "temporal": "1972-09-06T00:00:00Z/2019-06-25T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CALFIN Subseasonal Greenland Glacial Terminus Positions V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-VARGBDET-5-WISAST-V1.0",
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
+            "description": "Photometric observations of 125 asteroids, including absolute magnitudes, reported in Wisniewski et al. 1997.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-vargbdet-5-wisast-v1.0_uzec-9qtk",
+            "issued": "2021-05-21",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-VARGBDET-5-WISAST-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-vargbdet-5-wisast-v1.0_uzec-9qtk",
-            "description": "Photometric observations of 125 asteroids, including absolute magnitudes, reported in Wisniewski et al. 1997.",
-            "title": "WISNIEWSKI ASTEROID ABSOLUTE MAGNITUDES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "WISNIEWSKI ASTEROID ABSOLUTE MAGNITUDES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/FIREXAQ_Analysis_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2021-03-09. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/FIREXAQ_Analysis_Data_1.",
-            "issued": "2020-11-03",
-            "temporal": "2019-07-24T00:00:00Z/2019-09-03T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-15",
-            "keyword": [
-                "atmospheric chemistry",
-                "earth science",
-                "air quality",
-                "atmosphere"
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
-            "identifier": "C2040520694-LARC_ASDC",
             "description": "FIREXAQ_Analysis_Data are supplementary analysis and ancillary data collected during FIREX-AQ. This product includes plume ratios, and supplementary datasets regarding the wildfires sampled during the campaign. Data collection for this product is complete.\r\n\r\nCompleted during summer 2019, FIREX-AQ utilized a combination of instrumented airplanes, satellites, and ground-based instrumentation. Detailed fire plume sampling was carried out by the NASA DC-8 aircraft, which had a comprehensive instrument payload capable of measuring over 200 trace gas species, as well as aerosol microphysical, optical, and chemical properties. The DC-8 aircraft completed 23 science flights, including 15 flights from Boise, Idaho and 8 flights from Salina, Kansas. NASA\u2019s ER-2 completed 11 flights, partially in support of the FIREX-AQ effort. The ER-2 payload was made up of 8 satellite analog instruments and provided critical fire information, including fire temperature, fire plume heights, and vegetation/soil albedo information. NOAA provided the NOAA-CHEM Twin Otter and the NOAA-MET Twin Otter aircraft to measure chemical processing in the lofted plumes of Western wildfires. The NOAA-CHEM Twin Otter focused on nighttime plume chemistry, from which data is archived at the NASA Atmospheric Science Data Center (ASDC). The NOAA-MET Twin Otter collected measurements of air movements at fire boundaries with the goal of understanding the local weather impacts of fires and the movement patterns of fires. NOAA-MET Twin Otter data will be archived at the ASDC in the future. Additionally, a ground-based station in McCall, Idaho and several mobile laboratories provided in-situ measurements of aerosol microphysical and optical properties, aerosol chemical compositions, and trace gas species. \r\n\r\nThe Fire Influence on Regional to Global Environments and Air Quality (FIREX-AQ) campaign was a NOAA/NASA interagency intensive study of North American fires to gain an understanding on the integrated impact of the fire emissions on the tropospheric chemistry and composition and to assess the satellite\u2019s capability for detecting fires and estimating fire emissions. The overarching goal of FIREX-AQ was to provide measurements of trace gas and aerosol emissions for wildfires and prescribed fires in great detail, relate them to fuel and fire conditions at the point of emission, characterize the conditions relating to plume rise, and follow plumes downwind to understand chemical transformation and air quality impacts. Data collection is complete.",
-            "title": "FIREX-AQ Analysis and Supplementary Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FFIREXAQ_Analysis_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FFIREXAQ_Analysis_Data_1",
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
-                    "downloadURL": "https://doi.org/10.5067/ASDC/FIREXAQ_Analysis_Data_1",
-                    "description": "DOI data set landing page for FIREXAQ_Analysis_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIREXAQ_Analysis_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/FIREXAQ_Analysis_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2040520694-LARC_ASDC",
-                    "description": "FIREXAQ_Analysis_Data_1 on Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "FIREXAQ_Analysis_Data_1 on Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2040520694-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIREX-AQ/Analysis_Data_1/",
-                    "description": "ASDC Direct Data Download for FIREXAQ_Analysis_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIREXAQ_Analysis_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIREX-AQ/Analysis_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2040520694-LARC_ASDC",
+            "issued": "2020-11-03",
+            "keyword": [
+                "atmospheric chemistry",
+                "earth science",
+                "air quality",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/FIREXAQ_Analysis_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-04-15",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>15.0 -135.0 15.0 -75.0 60.0 -75.0 60.0 -135.0 15.0 -135.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2019-07-24T00:00:00Z/2019-09-03T23:59:59.999Z",
             "theme": [
                 "FIREX-AQ",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FIREX-AQ Analysis and Supplementary Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-PRL-MTP006-V2.0",
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
+            "description": "This data set contains\nEDITED data from Rosetta RPC-LAP, acquired during the PRELANDING\nMTP006 mission phase. Comet C-G/67P was the primary target.\nThis data set supersedes RO-C-RPCLAP-2-PRL-EDITED-V1.0 and is only\nMTP006 part of it.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-prl-mtp006-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-PRL-MTP006-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-prl-mtp006-v2.0",
-            "description": "This data set contains\nEDITED data from Rosetta RPC-LAP, acquired during the PRELANDING\nMTP006 mission phase. Comet C-G/67P was the primary target.\nThis data set supersedes RO-C-RPCLAP-2-PRL-EDITED-V1.0 and is only\nMTP006 part of it.",
-            "title": "ROSETTA-ORBITER 67P RPCLAP 2\nPRL MTP006 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCLAP 2\nPRL MTP006 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GNSS/GNSS_HIGHRATE_F_001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "International GNSS Service, High-rate Beidou broadcast ephemeris data, Greenbelt, MD, USA: NASA Crustal Dynamics Data Information System (CDDIS), Accessed [[enter user data access date]] at doi:10.5067/GNSS/gnss_highrate_f_001",
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
-            "identifier": "C1422097980-CDDIS",
             "description": "This dataset consists of ground-based Global Navigation Satellite System (GNSS) Beidou Broadcast Ephemeris Data (sub-hourly files) from the NASA Crustal Dynamics Data Information System (CDDIS). GNSS provide autonomous geo-spatial positioning with global coverage. GNSS data sets from ground receivers at the CDDIS consist primarily of the data from the U.S. Global Positioning System (GPS) and the Russian GLONASS. Since 2011, the CDDIS GNSS archive includes data from other GNSS (Europe\u2019s Galileo, China\u2019s Beidou, Japan\u2019s Quasi-Zenith Satellite System/QZSS, the Indian Regional Navigation Satellite System/IRNSS, and worldwide Satellite Based Augmentation Systems/SBASs), which are similar to the U.S. GPS in terms of the satellite constellation, orbits, and signal structure. The high-rate (1-second) Beidou broadcast ephemeris files contain 15 minutes of Beidou broadcast navigation data in RINEX format from a global permanent network of ground-based receivers, one file per 15 minutes per site. More information about these data is available on the CDDIS website at https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/high-rate_data.html.",
-            "title": "Ground-Based Global Navigation Satellite System (GNSS) Beidou Broadcast Ephemeris Data (sub-hourly files) from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGNSS_HIGHRATE_F_001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGNSS_HIGHRATE_F_001",
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
-                    "description": "URL for more information about GNSS sub-hourly Beidou broadcast navigation data",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about GNSS sub-hourly Beidou broadcast navigation data",
+                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/broadcast_ephemeris_data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/GNSS/GNSS_HIGHRATE_F_001",
-                    "description": "URL for more information about GNSS sub-hourly Beidou broadcast navigation data",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about GNSS sub-hourly Beidou broadcast navigation data",
+                    "downloadURL": "https://doi.org/10.5067/GNSS/GNSS_HIGHRATE_F_001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1422097980-CDDIS",
+            "issued": "1992-01-01",
+            "keyword": [
+                "earth science",
+                "solid earth",
+                "geodetics",
+                "gravity/gravitational field",
+                "tectonics"
+            ],
+            "landingPage": "https://doi.org/10.5067/GNSS/GNSS_HIGHRATE_F_001",
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
+            "title": "Ground-Based Global Navigation Satellite System (GNSS) Beidou Broadcast Ephemeris Data (sub-hourly files) from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-MASTCAM-4-RDR-VID-V1.0",
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
+            "description": "NULL",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-mastcam-4-rdr-vid-v1.0_uzj4-bfn9",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars science laboratory"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-MASTCAM-4-RDR-VID-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-mastcam-4-rdr-vid-v1.0_uzj4-bfn9",
-            "description": "NULL",
-            "title": "MSL MARS MAST CAMERA 4 RDR\n                                      VIDEO V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MSL MARS MAST CAMERA 4 RDR\n                                      VIDEO V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/C1FCK9A0317Y",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMAPVEX08 PALS Brightness Temperature Data V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/C1FCK9A0317Y.",
-            "issued": "2008-09-29",
-            "temporal": "2008-09-29T00:00:00Z/2008-10-13T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2008-10-13",
-            "keyword": [
-                "surface thermal properties",
-                "microwave",
-                "land surface",
-                "spectral/engineering",
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
-            "identifier": "C1000001401-NSIDC_ECS",
             "description": "This data set contains brightness temperatures obtained by the Passive Active L-band System (PALS) microwave aircraft radiometer instrument as part of the Soil Moisture Active Passive Validation Experiment 2008 (SMAPVEX08).",
-            "title": "SMAPVEX08 PALS Brightness Temperature Data V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FC1FCK9A0317Y",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FC1FCK9A0317Y",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_VAL/SV08PLTB.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_VAL/SV08PLTB.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001421-NSIDC_ECS&m=29.109375%21-77.818359375%214%211%210%210%2C2&q=SMAPVEX08&ok=SMAPVEX08",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001421-NSIDC_ECS&m=29.109375%21-77.818359375%214%211%210%210%2C2&q=SMAPVEX08&ok=SMAPVEX08",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SV08PLTB/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SV08PLTB/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/C1FCK9A0317Y",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/C1FCK9A0317Y",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/C1FCK9A0317Y",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/C1FCK9A0317Y",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1000001401-NSIDC_ECS",
+            "issued": "2008-09-29",
+            "keyword": [
+                "surface thermal properties",
+                "microwave",
+                "land surface",
+                "spectral/engineering",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/C1FCK9A0317Y",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2008-10-13",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-76.25 38.93 -75.55 39.09",
+            "temporal": "2008-09-29T00:00:00Z/2008-10-13T23:59:59.999Z",
             "theme": [
                 "SMAPVEX08",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMAPVEX08 PALS Brightness Temperature Data V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/uzmv-qgys",
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
-                "geography",
-                "nen"
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
-            "identifier": "NASA-0000038__20",
+            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
             "description": "Planetary nomenclature, like terrestrial nomenclature, is used to uniquely identify a feature on the surface of a planet or satellite so that the feature can be easily located, described, and discussed. This gazetteer contains detailed information about all names of topographic and albedo features on planets and satellites (and some planetary ring and ring-gap systems) that the International Astronomical Union (IAU) has named and approved from its founding in 1919 through the present time.",
-            "title": "Gazetteer of Planetary Nomenclature",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1496930,276 +1496912,272 @@
                     "mediaType": "application/vnd.google-earth.kmz"
                 }
             ],
-            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
-            "accrualPeriodicity": "irregular"
+            "identifier": "NASA-0000038__20",
+            "issued": "2018-06-25",
+            "keyword": [
+                "wise",
+                "space science",
+                "geography",
+                "nen"
+            ],
+            "landingPage": "https://data.nasa.gov/d/uzmv-qgys",
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aphx_tt_bundle&version=1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The original PHX TT dataset was submitted in 2009",
+            "identifier": "urn:nasa:pds:phx_tt_bundle_uznz-2rma",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "mars",
                 "phoenix",
                 "phoenix telltale tt mars"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aphx_tt_bundle&version=1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:phx_tt_bundle_uznz-2rma",
-            "description": "The original PHX TT dataset was submitted in 2009",
-            "title": "Phoenix TELLTALE Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "Phoenix TELLTALE Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-HAZCAM-5-DISPARITY-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-hazcam-5-disparity-ops-v1.0_uzr5-rt6p",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars exploration rover",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-HAZCAM-5-DISPARITY-OPS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-hazcam-5-disparity-ops-v1.0_uzr5-rt6p",
-            "description": "not applicable",
-            "title": "MER 1 MARS HAZARD AVOID CAMERA DISPARITY RDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MER 1 MARS HAZARD AVOID CAMERA DISPARITY RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/SEA2SPACE/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/SEA2SPACE/DATA001.",
-            "issued": "2017-01-26",
-            "temporal": "2017-01-26T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean optics",
-                "salinity/density",
-                "ocean temperature",
-                "ocean chemistry",
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
-            "identifier": "C1647028412-OB_DAAC",
             "description": "Measurements from the Sea2Space (Sea to Space Particle Investigation) project aboard the RV Falkor, supported by the Schmidt Ocean Institute, in the central and northeast Pacific.",
-            "title": "Sea to Space expedition",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FSEA2SPACE%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FSEA2SPACE%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Sea2Space/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Sea2Space/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1647028412-OB_DAAC",
+            "issued": "2017-01-26",
+            "keyword": [
+                "ocean optics",
+                "salinity/density",
+                "ocean temperature",
+                "ocean chemistry",
+                "oceans",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/SEA2SPACE/DATA001",
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
+            "temporal": "2017-01-26T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sea to Space expedition"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1153",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Soares-Filho, B.S., D.C. Nepstad, L.M. Curran, E. Voll, R.A. Garcia, C.A. Ramos, A.J. McDonald, P.A. Lefebvre, and P. Schlesinger. 2013. LBA-ECO LC-14 Modeled Deforestation Scenarios,  Amazon Basin: 2002-2050. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1153",
-            "issued": "2023-10-03",
-            "temporal": "2002-01-01T00:00:00Z/2050-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-12",
-            "keyword": [
-                "land use/land cover",
-                "human dimensions",
-                "habitat conversion/fragmentation",
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
-            "identifier": "C2781400209-ORNL_CLOUD",
             "description": "This data set provides the results of the two modeled scenarios for future patterns of deforestation across the Amazon Basin from 2002 to 2050. This larger defined Amazon Basin (PanAmazon area) includes the Amazon River watershed, the Legal Amazon in Brazil, and the Guiana region. The model SimAmazonia was used to simulate monthly deforestation in the Amazon Basin from 2002 to 2050 for two scenarios: (1) a \"Business-as-Usual\" scenario, which considered the deforestation trends across the basin and projected the rates by using historical images and their variations from 1997 to 2002 and then added to that the effect of paving a set of major roads, and (2) a \"Governance\" scenario, that also considered the current deforestation trends, but assumed a 50% limit  imposed for deforested land within each basin's subregion, and that existing and proposed Protected Areas (PAs), play a decisive role in limiting deforestation as well (Soares et al., 2006).The provided data products include one GeoTiff (*.tif) for each year (2002 to 2050) for both model scenarios for a total of 98 files. The files have been compressed in two *.zip files, one for each model scenario. There is also one comma-delimited file that contains the model input data derived from satellite deforestation maps.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO LC-14 Modeled Deforestation Scenarios,  Amazon Basin: 2002-2050",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1153_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1153",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1153",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC14_Amazon_Scenarios/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC14_Amazon_Scenarios/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC14_Amazon_Scenarios.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC14_Amazon_Scenarios.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1153",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1153",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC14_Amazon_Scenarios/comp/Amazon_Scenarios_Supplemental_Info.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC14_Amazon_Scenarios/comp/Amazon_Scenarios_Supplemental_Info.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC14_Amazon_Scenarios/comp/LC14_Amazon_Scenarios.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC14_Amazon_Scenarios/comp/LC14_Amazon_Scenarios.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1153_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1153_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1153",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1153",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1153_1_fit.png",
+            "identifier": "C2781400209-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "land use/land cover",
+                "human dimensions",
+                "habitat conversion/fragmentation",
+                "land surface",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1153",
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
             "spatial": "-81.86 -55.77 -34.29 12.98",
+            "temporal": "2002-01-01T00:00:00Z/2050-12-31T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO LC-14 Modeled Deforestation Scenarios,  Amazon Basin: 2002-2050"
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
-                "incompressible",
-                "flow",
-                "cases",
-                "turbulence",
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
-            "identifier": "NASA-842__17",
             "description": "This grouping contains the incompressible-flow cases from the 1980-81 Data Library.",
-            "title": "Collaborative Testing of Turbulence Models: Incompressible Flow Cases from 1980-81 Data Library",
-            "programCode": [
-                "026:023"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1497207,60 +1497185,84 @@
                     "mediaType": "application/txt"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-842__17",
+            "issued": "2018-06-25",
+            "keyword": [
+                "incompressible",
+                "flow",
+                "cases",
+                "turbulence",
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MARSIS-2-EDR-EXT3-V1.0",
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
+            "description": "This dataset contains the scientific telemetry produced by the MARSIS instrument after editing for duplicated and corrupted packets, together with geometric information computed on ground to locate observations in space and time. Both subsurface and ionosphere sounding data are included in the dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-marsis-2-edr-ext3-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars express",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MARSIS-2-EDR-EXT3-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-marsis-2-edr-ext3-v1.0",
-            "description": "This dataset contains the scientific telemetry produced by the MARSIS instrument after editing for duplicated and corrupted packets, together with geometric information computed on ground to locate observations in space and time. Both subsurface and ionosphere sounding data are included in the dataset.",
-            "title": "MARS EXPRESS MARS MARSIS EXPERIMENT DATA RECORD EXT 3 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS MARSIS EXPERIMENT DATA RECORD EXT 3 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-L-MMTO_CCD47-2-EDR-LCROSS-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This archive contains raw observations of the 2009-10-09 impact of the LCROSS spacecraft on the moon by the CCD47 camera on the MMT Observatory 6.5m telescope. The archive consists of uncalibrated FITS images of the event. This is one of several data sets of Earth-based observations of the impact.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-l-mmto_ccd47-2-edr-lcross-v1.0_uzum-stnn",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "hd 43607",
                 "sky",
@@ -1497271,898 +1497273,905 @@
                 "flat field",
                 "bias"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-L-MMTO_CCD47-2-EDR-LCROSS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-l-mmto_ccd47-2-edr-lcross-v1.0_uzum-stnn",
-            "description": "This archive contains raw observations of the 2009-10-09 impact of the LCROSS spacecraft on the moon by the CCD47 camera on the MMT Observatory 6.5m telescope. The archive consists of uncalibrated FITS images of the event. This is one of several data sets of Earth-based observations of the impact.",
-            "title": "MMT OBSERVATORY 6.5M CCD47 RAW DATA OBSERVATIONS OF LCROSS",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MMT OBSERVATORY 6.5M CCD47 RAW DATA OBSERVATIONS OF LCROSS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MIDAS-3-EXT1-SAMPLES-V3.0",
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
+            "description": "The Micro-Imaging Dust Analysis System (MIDAS) is an instrument on the\nROSETTA Orbiter that will provide 3D images and statistical parameters\nof pristine cometary particles, collected in the vicinity of comet\n67P/Churyumov-Gerasimenko. This data set includes all data from the\nROSETTA EXTENSION 1 mission phase. This release supersedes version 2.0.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-midas-3-ext1-samples-v3.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MIDAS-3-EXT1-SAMPLES-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-midas-3-ext1-samples-v3.0",
-            "description": "The Micro-Imaging Dust Analysis System (MIDAS) is an instrument on the\nROSETTA Orbiter that will provide 3D images and statistical parameters\nof pristine cometary particles, collected in the vicinity of comet\n67P/Churyumov-Gerasimenko. This data set includes all data from the\nROSETTA EXTENSION 1 mission phase. This release supersedes version 2.0.",
-            "title": "ROSETTA-ORBITER 67P MIDAS 3 EXT1 SAMPLES V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P MIDAS 3 EXT1 SAMPLES V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VO1%2FVO2-M-IRTM-5-BINNED%2FCLOUDS-V1.0",
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
-                "viking"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set, derived from the Viking Orbiter Infrared Thermal Mapper (IRTM) data set, has been binned in both space and time. It consists of two complementary portions, water ice cloud observations and surface observations. For details on the IRTM instrument and data set, refer to [KIEFFER_ETAL_1977].",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vo1-vo2-m-irtm-5-binned-clouds-v1.0_uzxy-6f8d",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "viking"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VO1%2FVO2-M-IRTM-5-BINNED%2FCLOUDS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vo1-vo2-m-irtm-5-binned-clouds-v1.0_uzxy-6f8d",
-            "description": "This data set, derived from the Viking Orbiter Infrared Thermal Mapper (IRTM) data set, has been binned in both space and time. It consists of two complementary portions, water ice cloud observations and surface observations. For details on the IRTM instrument and data set, refer to [KIEFFER_ETAL_1977].",
-            "title": "VO1/VO2 MARS IRTM BINNED DATA AND DERIVED CLOUDS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VO1/VO2 MARS IRTM BINNED DATA AND DERIVED CLOUDS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1587",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Sulla-Menashe, D., M.A. Friedl, C. Woodcock, and E.K. Melaas. 2018. ABoVE: Peak Greenness for Canadian Boreal Forest from Landsat 5 TM Imagery, 1984-2011. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1587",
-            "issued": "2018-05-15",
-            "temporal": "1970-01-01T00:00:00Z/2014-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "natural hazards",
-                "human dimensions",
-                "vegetation",
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
-            "identifier": "C2162140027-ORNL_CLOUD",
             "description": "This dataset provides a 28-year time series of peak greenness (NDVI) data derived from Landsat 5 TM imagery over the boreal forest region of Canada. Landsat 5 TM scenes were collected for 46 selected sidelap sites along gradients in climate, tree cover, and disturbance history from 1984 to 2011. Peak-greenness reflectance was computed for 30-m Landsat pixels using the maximum normalized difference vegetation index (NDVI) along with the normalized burn ratio (NBR) during the period between days of the year (DOY) 180 and 204. To facilitate trend analysis at each site, the NDVI and NBR data of the 30-m Landsat pixels were regridded to the coarser MODIS 500-m (463.3-m) spatial scale to reduce the effects of missing data and to enhance the significance of the trend. The regridded NDVI and NBR 28-year time series data at 500-m resolution are provided for each of the 46 sites. Two trend analyses were run on the 500-m resolution data and are reported for each site. Supplemental site metadata are also provided, including the number of valid Landsat pixels, land cover composition, and disturbance history, for each 500-m pixel.",
-            "graphic-preview-description": "The Canadian boreal forest study area and the 46 sites used in the analyses (identified by red boxes) mapped on top of: (A) ecozones (from http://canadianbiodiversity.mcgill.ca/english/ecozones/index.htm), (B) AVHRR NDVI trends (Beck and Goetz 2011), (C) tree cover from the MODIS VCF product (Hansen et al. 2003), and (D) fire disturbance from the Canadian Large Fire Database (Stocks et al. 2002). The sites were numbered in alphabetical order and site names are listed below the map.",
-            "title": "ABoVE: Peak Greenness for Canadian Boreal Forest from Landsat 5 TM Imagery, 1984-2011",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Canada_Boreal_Forest_Greenness_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1587",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1587",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/Canada_Boreal_Forest_Greenness/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/Canada_Boreal_Forest_Greenness/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Canada_Boreal_Forest_Greenness.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Canada_Boreal_Forest_Greenness.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1587",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1587",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Canada_Boreal_Forest_Greenness/comp/Canada_Boreal_Forest_Greenness.pdf",
-                    "description": "ABoVE: Satellite Observations of Peak Greenness for Canadian Boreal Forest, 1984-2013: Canada_Boreal_Forest_Greenness.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Satellite Observations of Peak Greenness for Canadian Boreal Forest, 1984-2013: Canada_Boreal_Forest_Greenness.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Canada_Boreal_Forest_Greenness/comp/Canada_Boreal_Forest_Greenness.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Canada_Boreal_Forest_Greenness_Fig1.png",
-                    "description": "The Canadian boreal forest study area and the 46 sites used in the analyses (identified by red boxes) mapped on top of: (A) ecozones (from http://canadianbiodiversity.mcgill.ca/english/ecozones/index.htm), (B) AVHRR NDVI trends (Beck and Goetz 2011), (C) tree cover from the MODIS VCF product (Hansen et al. 2003), and (D) fire disturbance from the Canadian Large Fire Database (Stocks et al. 2002). The sites were numbered in alphabetical order and site names are listed below the map.",
                     "@type": "dcat:Distribution",
+                    "description": "The Canadian boreal forest study area and the 46 sites used in the analyses (identified by red boxes) mapped on top of: (A) ecozones (from http://canadianbiodiversity.mcgill.ca/english/ecozones/index.htm), (B) AVHRR NDVI trends (Beck and Goetz 2011), (C) tree cover from the MODIS VCF product (Hansen et al. 2003), and (D) fire disturbance from the Canadian Large Fire Database (Stocks et al. 2002). The sites were numbered in alphabetical order and site names are listed below the map.",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Canada_Boreal_Forest_Greenness_Fig1.png",
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
+            "graphic-preview-description": "The Canadian boreal forest study area and the 46 sites used in the analyses (identified by red boxes) mapped on top of: (A) ecozones (from http://canadianbiodiversity.mcgill.ca/english/ecozones/index.htm), (B) AVHRR NDVI trends (Beck and Goetz 2011), (C) tree cover from the MODIS VCF product (Hansen et al. 2003), and (D) fire disturbance from the Canadian Large Fire Database (Stocks et al. 2002). The sites were numbered in alphabetical order and site names are listed below the map.",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Canada_Boreal_Forest_Greenness_Fig1.png",
+            "identifier": "C2162140027-ORNL_CLOUD",
+            "issued": "2018-05-15",
+            "keyword": [
+                "natural hazards",
+                "human dimensions",
+                "vegetation",
+                "land surface",
+                "earth science",
+                "land use/land cover",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1587",
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
             "spatial": "-124.47 45.32 -53.91 63.44",
+            "temporal": "1970-01-01T00:00:00Z/2014-12-31T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE: Peak Greenness for Canadian Boreal Forest from Landsat 5 TM Imagery, 1984-2011"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/ICEPOP/SEAFLUX/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Roberts, Jason Brent .2020. GPM Ground Validation SEA FLUX ICE POP [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/ICEPOP/SEAFLUX/DATA101",
-            "issued": "2020-05-07",
-            "temporal": "2017-09-01T00:30:00Z/2018-04-30T23:30:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-31",
-            "keyword": [
-                "atmosphere",
-                "precipitation",
-                "ocean temperature",
-                "oceans",
-                "earth science",
-                "atmospheric water vapor",
-                "atmospheric winds",
-                "atmospheric radiation"
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
-            "identifier": "C1995570197-GHRC_DAAC",
             "description": "The GPM Ground Validation SEA FLUX ICE POP dataset includes estimates of ocean surface latent and sensible heat fluxes, 10m wind speed, 10m air temperature, 10m air humidity, and skin sea surface temperature in support of the International Collaborative Experiments for Pyeongchang 2018 Olympic and Paralympic Winter Games (ICE-POP) field campaign in South Korea. The two major objectives of ICE-POP were to study severe winter weather events in regions of complex terrain and improve the short-term forecasting of such events. These data contributed to the Global Precipitation Measurement mission Ground Validation (GPM GV) campaign efforts to improve satellite estimates of orographic winter precipitation. This data file is available in netCDF-4 format from September 1, 2017 through April 30, 2018.",
-            "title": "GPM Ground Validation SEA FLUX ICE POP V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FICEPOP%2FSEAFLUX%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FICEPOP%2FSEAFLUX%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmseafluxicepop%2Fdata%2F",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmseafluxicepop%2Fdata%2F",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.5067/GPMGV/ICEPOP/DATA101",
-                    "description": "ICE-POP Field Campaign Collection DOI",
                     "@type": "dcat:Distribution",
+                    "description": "ICE-POP Field Campaign Collection DOI",
+                    "downloadURL": "http://dx.doi.org/10.5067/GPMGV/ICEPOP/DATA101",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/icepop/SEAFLUX/doc/gpmseafluxicepop_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/icepop/SEAFLUX/doc/gpmseafluxicepop_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3390/rs10081306",
-                    "description": "Fundamental Climate Data Records of Microwave Brightness Temperatures",
                     "@type": "dcat:Distribution",
+                    "description": "Fundamental Climate Data Records of Microwave Brightness Temperatures",
+                    "downloadURL": "https://doi.org/10.3390/rs10081306",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/JPO-D-13-0225.1",
-                    "description": "On the Exchange of Momentum over the Open Ocean",
                     "@type": "dcat:Distribution",
+                    "description": "On the Exchange of Momentum over the Open Ocean",
+                    "downloadURL": "https://doi.org/10.1175/JPO-D-13-0225.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/2007JCLI1824.1",
-                    "description": "Daily high-resolution-blended analyses for sea surface temperature",
                     "@type": "dcat:Distribution",
+                    "description": "Daily high-resolution-blended analyses for sea surface temperature",
+                    "downloadURL": "https://doi.org/10.1175/2007JCLI1824.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/2018EA000436",
-                    "description": "Improving Near\u2010Surface Retrievals of Surface Humidity Over the Global Open Oceans From Passive Microwave Observations",
                     "@type": "dcat:Distribution",
+                    "description": "Improving Near\u2010Surface Retrievals of Surface Humidity Over the Global Open Oceans From Passive Microwave Observations",
+                    "downloadURL": "https://doi.org/10.1029/2018EA000436",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/2007JD009322",
-                    "description": "Predicting near-surface atmospheric variables from Special Sensor Microwave/Imager using neural networks with a first-guess approach",
                     "@type": "dcat:Distribution",
+                    "description": "Predicting near-surface atmospheric variables from Special Sensor Microwave/Imager using neural networks with a first-guess approach",
+                    "downloadURL": "https://doi.org/10.1029/2007JD009322",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/ice-pop",
-                    "description": "ICE-POP Field Campaign Project Homepage",
                     "@type": "dcat:Distribution",
+                    "description": "ICE-POP Field Campaign Project Homepage",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/ice-pop",
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
+            "identifier": "C1995570197-GHRC_DAAC",
+            "issued": "2020-05-07",
+            "keyword": [
+                "atmosphere",
+                "precipitation",
+                "ocean temperature",
+                "oceans",
+                "earth science",
+                "atmospheric water vapor",
+                "atmospheric winds",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/ICEPOP/SEAFLUX/DATA101",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-05-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/MSFC/GHRC"
+            },
             "spatial": "98.5 8.5 177.5 54.25",
+            "temporal": "2017-09-01T00:30:00Z/2018-04-30T23:30:00Z",
             "theme": [
                 "ICE POP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM Ground Validation SEA FLUX ICE POP V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SONEX_Miscellaneous_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2023-08-21. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/SONEX_Miscellaneous_Data_1.",
-            "issued": "1997-10-07",
-            "temporal": "1997-10-07T00:00:00Z/1997-11-13T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1997-11-12",
-            "keyword": [
-                "atmosphere",
-                "platform characteristics",
-                "spectral/engineering",
-                "weather events",
-                "atmospheric winds",
-                "earth science",
-                "atmospheric electricity"
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
-            "identifier": "C2662376578-LARC_ASDC",
             "description": "SONEX_Miscellaneous_Data_1 is the ancillary datasets from the SASS (Subsonics Assessment) Ozone and NOx Experiment (SONEX). This dataset contains gif and postscript files of datasets to support DC-8 aircraft measurements. Data collection for this product is complete.\r\nThe SASS (Subsonics Assessment) Ozone and NOx Experiment (SONEX) was an international, multi-organizational mission that took place in October-November 1997. NASA was the US sponsor of SONEX that partnered with POLINAT-2 (Pollution from Aircraft Emissions in the North Atlantic Flight Corridor) funded by the German DLR (Deutsches Zentrum f\u00fcr Luft- und Raumfahrt) or German Aerospace Agency. NASA flew the DC-8 aircraft out of NASA/Ames Research Center. DLR operated an instrumented Falcon 20 aircraft. The staging locations for NAFC sampling were primarily Bangor, Maine (US), and Shannon, Ireland. Subsonic aircraft emissions impact several aspects of atmospheric composition: nitrogen oxides (NOx), CO, and hydrocarbons from emissions can perturb upper tropospheric/lower stratospheric (UT/LS) ozone; water vapor, soot, and sulfur oxides (SOx) emitted by aircraft may perturb clouds and aerosols, changing UT/LS radiative forcing and global temperature.\r\nIn SONEX and POLINAT, flights were conducted in the vicinity of the North Atlantic Flight Coordinator (NAFC) to observe the impact of aircraft emissions on NOx and ozone (O3). The DC-8 aircraft payload (Singh et al., 1999) primarily measured in-situ CO, CO2, hydrocarbons/halocarbons, O3, aerosols (Dibb et al., 2000), OH/HO2, water vapor, nitric acid (Talbot et al., 1999), photolysis rates, temperature, pressure, winds, NOx, and NOy.\r\nThree sampling approaches were implemented during SONEX. First, special meteorological (Fuelberg et al., 2000) were developed to allow targeted sampling for air parcels affected by aircraft emissions and various meteorological events, e.g., convection, lightning (Jeker et al., 2000), stratospheric intrusions (Cho et al., 2000). Second, because the NAFC had not been extensively sampled in the past, it was important for SONEX to characterize the climatology of trace species like CN (Wang et al., 2000), NOx and NOy (Koike et al., 2000). Third, tracers (Simpson et al., 2000; Thompson et al., 1999) and model sensitivity studies (Meijer et al., 2000) were employed for Air Mass Identification. This sampling strategy answered the following questions: Where and when are air masses found with the greatest aircraft influence? When and where was stratospheric air sampled? SONEX showed a substantial impact of aircraft emissions on UT/LS NOx and CN in the vicinity of fresh aircraft emissions. However, during October-November 1997 over the NAFC, UT/LS NOx was dominated by surface emissions redistributed by convection and augmented by lightning.",
-            "title": "SASS (Subsonics Assessment) Ozone and NOx Experiment (SONEX) Ancillary Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSONEX_Miscellaneous_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSONEX_Miscellaneous_Data_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
-                    "description": "ASDC Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Home Page",
+                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data citation policy"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/1999GL900588",
-                    "description": "SONEX airborne mission and coordinated POLINAT-2 activity: Overview and accomplishments",
                     "@type": "dcat:Distribution",
+                    "description": "SONEX airborne mission and coordinated POLINAT-2 activity: Overview and accomplishments",
+                    "downloadURL": "https://doi.org/10.1029/1999GL900588",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/1999JD900424",
-                    "description": "https://doi.org/10.1029/1999GL900588",
                     "@type": "dcat:Distribution",
+                    "description": "https://doi.org/10.1029/1999GL900588",
+                    "downloadURL": "https://doi.org/10.1029/1999JD900424",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/1999GL900589",
-                    "description": "Reactive nitrogen budget during the NASA SONEX Mission",
                     "@type": "dcat:Distribution",
+                    "description": "Reactive nitrogen budget during the NASA SONEX Mission",
+                    "downloadURL": "https://doi.org/10.1029/1999GL900589",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/1999JD900917",
-                    "description": "A meteorological overview of the Subsonic Assessment Ozone and Nitrogen Oxide Experiment (SONEX) period",
                     "@type": "dcat:Distribution",
+                    "description": "A meteorological overview of the Subsonic Assessment Ozone and Nitrogen Oxide Experiment (SONEX) period",
+                    "downloadURL": "https://doi.org/10.1029/1999JD900917",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/1999JD901053",
-                    "description": "Measurements of nitrogen oxides at the tropopause: Attribution to convection and correlation with lightning",
                     "@type": "dcat:Distribution",
+                    "description": "Measurements of nitrogen oxides at the tropopause: Attribution to convection and correlation with lightning",
+                    "downloadURL": "https://doi.org/10.1029/1999JD901053",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/1999JD900430",
-                    "description": "Observations of convective and dynamical instabilities in tropopause folds and their contribution to stratosphere-troposphere exchange",
                     "@type": "dcat:Distribution",
+                    "description": "Observations of convective and dynamical instabilities in tropopause folds and their contribution to stratosphere-troposphere exchange",
+                    "downloadURL": "https://doi.org/10.1029/1999JD900430",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/1999GL010930",
-                    "description": "Evidence of convection as a major source of condensation nuclei in the northern midlatitude upper troposphere",
                     "@type": "dcat:Distribution",
+                    "description": "Evidence of convection as a major source of condensation nuclei in the northern midlatitude upper troposphere",
+                    "downloadURL": "https://doi.org/10.1029/1999GL010930",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/1999JD901013",
-                    "description": "Impact of aircraft emissions on reactive nitrogen over the North Atlantic Flight Corridor region",
                     "@type": "dcat:Distribution",
+                    "description": "Impact of aircraft emissions on reactive nitrogen over the North Atlantic Flight Corridor region",
+                    "downloadURL": "https://doi.org/10.1029/1999JD901013",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/1999JD900750",
-                    "description": "Nonmethane hydrocarbon measurements in the North Atlantic Flight Corridor during the Subsonic Assessment Ozone and Nitrogen Oxide Experiment",
                     "@type": "dcat:Distribution",
+                    "description": "Nonmethane hydrocarbon measurements in the North Atlantic Flight Corridor during the Subsonic Assessment Ozone and Nitrogen Oxide Experiment",
+                    "downloadURL": "https://doi.org/10.1029/1999JD900750",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/1999GL900581",
-                    "description": "Perspectives on NO, NOy, and fine aerosol sources and variability during SONEX",
                     "@type": "dcat:Distribution",
+                    "description": "Perspectives on NO, NOy, and fine aerosol sources and variability during SONEX",
+                    "downloadURL": "https://doi.org/10.1029/1999GL900581",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/1999JD901052",
-                    "description": "Model calculations of the impact of NOx from air traffic, lightning, and surface emissions, compared with measurements",
                     "@type": "dcat:Distribution",
+                    "description": "Model calculations of the impact of NOx from air traffic, lightning, and surface emissions, compared with measurements",
+                    "downloadURL": "https://doi.org/10.1029/1999JD901052",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/content/Ames_Format_Overview",
-                    "description": "Ames File Format Overview",
                     "@type": "dcat:Distribution",
+                    "description": "Ames File Format Overview",
+                    "downloadURL": "https://espo.nasa.gov/content/Ames_Format_Overview",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/SONEX/SONEX_Miscellaneous_DC8_Data_1/",
-                    "description": "ASDC Direct Data Download for SONEX_Miscellaneous_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for SONEX_Miscellaneous_DC8_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/SONEX/SONEX_Miscellaneous_DC8_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2662376578-LARC_ASDC",
+            "issued": "1997-10-07",
+            "keyword": [
+                "atmosphere",
+                "platform characteristics",
+                "spectral/engineering",
+                "weather events",
+                "atmospheric winds",
+                "earth science",
+                "atmospheric electricity"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SONEX_Miscellaneous_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1997-11-12",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>19.89 -129.402 19.89 13.023 69.127 13.023 69.127 -129.402 19.89 -129.402</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1997-10-07T00:00:00Z/1997-11-13T23:59:59.999Z",
             "theme": [
                 "SONEX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SASS (Subsonics Assessment) Ozone and NOx Experiment (SONEX) Ancillary Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0268-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-09-03T11:27:05.000 to 2014-09-03T17:39:21.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0268-v1.0_v2cz-gijp",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0268-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0268-v1.0_v2cz-gijp",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-09-03T11:27:05.000 to 2014-09-03T17:39:21.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0268 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0268 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1596",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Nehrkorn, T., M. Sargent, S.C. Wofsy, and M. Mountain. 2018. WRF-STILT Particle Trajectories for Boston, MA, USA, 2013-2014. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1596",
-            "issued": "2018-05-25",
-            "temporal": "2013-07-01T00:00:00Z/2014-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "earth science",
-                "atmospheric chemistry",
-                "atmospheric winds",
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
-            "identifier": "C2517667717-ORNL_CLOUD",
             "description": "This dataset provides Weather Research and Forecasting (WRF) Stochastic Time-Inverted Lagrangian Transport (STILT) particle trajectory data and footprint products for two receptors located in Boston, Massachusetts, USA, for July 2013 - December 2014. Meteorological fields from version 3.6.1 of the Weather Research and Forecasting model are used to drive STILT. STILT applies a Lagrangian particle dispersion model backwards in time from a measurement location (the \"receptor\" location), to create the adjoint of the transport model in the form of a \"footprint\" field. The footprint, with units of mixing ratio (ppm) per surface flux (umol m-2 s-1), quantifies the influence of upwind surface fluxes on CO2 and CH4 concentrations measured at the receptor and is computed by counting the number of particles in a surface-influenced volume and the time spent in that volume. Footprints are provided for the two receptors at two temporal and spatial scales: three days of surface influence over the whole North American coverage area at 1-degree resolution and 24 hours of surface influence within a smaller region close to the measurement locations ('near field') at 0.1-degree resolution.",
-            "graphic-preview-description": "Data from the WRF-STILT model representing the response of a receptor in Boston, Massachusetts to a unit surface emission of CO2 (ppm/umol m-2 s-1).",
-            "title": "WRF-STILT Particle Trajectories for Boston, MA, USA, 2013-2014",
-            "graphic-preview-file": "https://daac.ornl.gov/NACP/guides/WRF_STILT_Particles_Boston_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1596",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1596",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/nacp/WRF_STILT_Particles_Boston/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/nacp/WRF_STILT_Particles_Boston/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/NACP/guides/WRF_STILT_Particles_Boston.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/NACP/guides/WRF_STILT_Particles_Boston.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1596",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1596",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/WRF_STILT_Particles_Boston/comp/WRF_STILT_Particles_Boston.pdf",
-                    "description": "NACP: WRF-STILT Particles for Boston, 2013-2014: WRF_STILT_Particles_Boston.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "NACP: WRF-STILT Particles for Boston, 2013-2014: WRF_STILT_Particles_Boston.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/WRF_STILT_Particles_Boston/comp/WRF_STILT_Particles_Boston.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/NACP/guides/WRF_STILT_Particles_Boston_Fig1.png",
-                    "description": "Data from the WRF-STILT model representing the response of a receptor in Boston, Massachusetts to a unit surface emission of CO2 (ppm/umol m-2 s-1).",
                     "@type": "dcat:Distribution",
+                    "description": "Data from the WRF-STILT model representing the response of a receptor in Boston, Massachusetts to a unit surface emission of CO2 (ppm/umol m-2 s-1).",
+                    "downloadURL": "https://daac.ornl.gov/NACP/guides/WRF_STILT_Particles_Boston_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Data from the WRF-STILT model representing the response of a receptor in Boston, Massachusetts to a unit surface emission of CO2 (ppm/umol m-2 s-1).",
+            "graphic-preview-file": "https://daac.ornl.gov/NACP/guides/WRF_STILT_Particles_Boston_Fig1.png",
+            "identifier": "C2517667717-ORNL_CLOUD",
+            "issued": "2018-05-25",
+            "keyword": [
+                "earth science",
+                "atmospheric chemistry",
+                "atmospheric winds",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1596",
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
             "spatial": "-81.78 34.51 -65.93 49.19",
+            "temporal": "2013-07-01T00:00:00Z/2014-12-31T23:59:59Z",
             "theme": [
                 "NACP",
                 "CMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "WRF-STILT Particle Trajectories for Boston, MA, USA, 2013-2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C3166805761-OB_DAAC.html",
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
-                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
-            },
-            "identifier": "C3166805761-OB_DAAC",
             "description": "The Visible and Infrared Imager/Radiometer Suite (VIIRS) is a multi-disciplinary instrument that is being flown on the Joint Polar Satellite System (JPSS) series of spacecraft, including the Suomi National Polar-orbiting Partnership (S-NPP) that launched in October 2011.  JPSS is a multi-platform, multi-agency program that consolidates the polar orbiting spacecraft of NASA and the National Oceanic and Atmospheric Administration (NOAA).  S-NPP is the initial spacecraft in this series, and VIIRS is the successor to MODIS for Earth science data product generation.  VIIRS has 22 spectral bands ranging from 412 nm to 12 nm.  There are 16 moderate-resolution bands (750m at nadir), 5 image-resolution bands (375m), and one day-night band (DNB).",
-            "title": "NOAA-20 VIIRS Level-2 Regional Triple-window Sea Surface Temperature (SST3) Data, version 2024.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-2/NOAA20-VIIRS/",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-2/NOAA20-VIIRS/",
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
+            "identifier": "C3166805761-OB_DAAC",
+            "issued": "2024-07-19",
+            "keyword": [
+                "earth science",
+                "ocean temperature",
+                "oceans"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C3166805761-OB_DAAC.html",
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
+            "title": "NOAA-20 VIIRS Level-2 Regional Triple-window Sea Surface Temperature (SST3) Data, version 2024.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1196-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-20T07:45:00.000 to 2015-11-20T16:45:07.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1196-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1196-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1196-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-20T07:45:00.000 to 2015-11-20T16:45:07.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1196 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1196 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0021",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2003-04-29. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDCDAAC/NARSTO/0021.",
-            "issued": "2003-11-26",
-            "temporal": "2001-09-20T00:00:00Z/2001-12-27T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-08-07",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "air quality"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANTHONY WEXLER",
                 "hasEmail": "mailto:aswexler@ucdavis.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2350096067-LARC_ASDC",
             "description": "NARSTO_EPA_SS_PITTSBURGH_RAPID_SPMS_DATA is the North American Research Strategy for Tropospheric Ozone (NARSTO) Environmental Protection Agency (EPA) Supersite (SS) Pittsburgh Rapid Single-Particle Mass Spectrometer Data product. It was obtained between September 20 and December 27, 2001 during the Pittsburgh Air Quality Study (PAQS). During 12 months, starting September 2001, individual aerosol particles were sized and analyzed using a Rapid Single-particle Mass Spectrometer (RSMS) in Pittsburgh. RSMS aerodynamically focuses one particle size at a time to the source region of a mass spectrometer and employs a 193 nm excimer laser to desorb and ionize the particle components. The ions are analyzed in a dual time-of-flight mass spectrometer and the spectrum is digitally recorded. Spectra are only saved if the ion peak in the spectrum is above a threshold level. Background spectra were determined and flagged. Particle size scans were initiated periodically, and each size was sampled until 30 particle hits were obtained, unless the sampling time became excessive. Aerodynamic particle sizes ranged from about 40 to 1300 nm and were partitioned into nine discrete size classes logarithmically spaced, roughly, over the range. Single particle data were valuable because a) they were collected and analyzed real time so have excellent temporal resolution, b) the particle-to-particle composition variations (external mixing properties) could be assessed, and c) key particle sources were easily identified since the particles retain source characteristics. The data resulting from these measurements consist of an aerodynamic particle size and a positive and negative mass spectrum of the components for each particle, along with the date and time of measurement and other incidental measurement parameters such as the laser pulse energy.\r\n\r\nThe U.S. EPA Particulate Matter (PM) Supersites Program was an ambient air monitoring research program designed to provide information of value to the atmospheric sciences, and human health and exposure research communities. Eight geographically diverse projects were chosen to specifically address these EPA research priorities: (1) to characterize PM, its constituents, precursors, co-pollutants, atmospheric transport, and its source categories that affect the PM in any region; (2) to address the research questions and scientific uncertainties about PM source-receptor and exposure-health effects relationships; and (3) to compare and evaluate different methods of characterizing PM including testing new and emerging measurement methods.\r\n\r\nNARSTO, which has since disbanded, was a public/private partnership, whose membership spanned across government, utilities, industry, and academe throughout Mexico, the United States, and Canada. The primary mission was to coordinate and enhance policy-relevant scientific research and assessment of tropospheric pollution behavior; activities provide input for science-based decision-making and determination of workable, efficient, and effective strategies for local and regional air-pollution management. Data products from local, regional, and international monitoring and research programs are still available.",
-            "title": "NARSTO EPA Supersite (SS) Pittsburgh Rapid Single-Particle Mass Spectrometer Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDCDAAC%2FNARSTO%2F0021",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDCDAAC%2FNARSTO%2F0021",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2350096067-LARC_ASDC",
-                    "description": "Earthdata Search for NARSTO_EPA_SS_PITTSBURGH_RAPID_SPMS_DATA_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for NARSTO_EPA_SS_PITTSBURGH_RAPID_SPMS_DATA_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2350096067-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/guide/narsto_epa_ss_pittsburgh_rapid_spms_data.pdf",
-                    "description": "Guide for NARSTO EPA_SS_PITTSBURGH Rapid Single-Particle Mass Spectrometer Data",
                     "@type": "dcat:Distribution",
+                    "description": "Guide for NARSTO EPA_SS_PITTSBURGH Rapid Single-Particle Mass Spectrometer Data",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/guide/narsto_epa_ss_pittsburgh_rapid_spms_data.pdf",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/EPA_SS_Pittsburgh_Project_Plan.pdf",
-                    "description": "Quality Assurance Project Plan for the Pittsburgh Air Quality Study (PAQS)",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Assurance Project Plan for the Pittsburgh Air Quality Study (PAQS)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/EPA_SS_Pittsburgh_Project_Plan.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0021",
-                    "description": "DOI data set landing page for NARSTO_EPA_SS_PITTSBURGH_RAPID_SPMS_DATA_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for NARSTO_EPA_SS_PITTSBURGH_RAPID_SPMS_DATA_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0021",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/NARSTO/EPA_SS_PITTSBURGH_RAPID_SPMS_DATA_1/",
-                    "description": "ASDC Direct Data Download for NARSTO_EPA_SS_PITTSBURGH_RAPID_SPMS_DATA_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for NARSTO_EPA_SS_PITTSBURGH_RAPID_SPMS_DATA_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/NARSTO/EPA_SS_PITTSBURGH_RAPID_SPMS_DATA_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2350096067-LARC_ASDC",
+            "issued": "2003-11-26",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "air quality"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0021",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-08-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "40.43 -79.94",
+            "temporal": "2001-09-20T00:00:00Z/2001-12-27T23:59:59.999Z",
             "theme": [
                 "NARSTO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NARSTO EPA Supersite (SS) Pittsburgh Rapid Single-Particle Mass Spectrometer Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0768-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-05-11T22:03:05.000 to 2015-05-12T07:07:13.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0768-v1.0_v2p2-fdn6",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0768-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0768-v1.0_v2p2-fdn6",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-05-11T22:03:05.000 to 2015-05-12T07:07:13.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0768 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0768 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://lsp.ksc.nasa.gov/launchhistory/f/default.aspx",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "1998-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-13",
-            "references": [
-                "http://www.lsp.ksc.nasa.gov/"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brian Dunbar",
+                "hasEmail": "mailto:brian.dunbar@nasa.gov"
+            },
+            "description": "The NASA LSP website features a history of past spacecraft launches, from 1999 to present.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.nasa.gov/centers/kennedy/launchingrockets/archives/elv_archive-index.html",
+                    "mediaType": "text/html"
+                }
             ],
+            "identifier": "NASA-918",
+            "issued": "1998-01-01",
             "keyword": [
                 "landing",
                 "schedule",
@@ -1498173,334 +1498182,301 @@
                 "support",
                 "launch"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brian Dunbar",
-                "hasEmail": "mailto:brian.dunbar@nasa.gov"
-            },
+            "landingPage": "https://lsp.ksc.nasa.gov/launchhistory/f/default.aspx",
+            "modified": "2021-05-13",
+            "programCode": [
+                "026:046"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-918",
-            "description": "The NASA LSP website features a history of past spacecraft launches, from 1999 to present.",
-            "title": "NASA Launch Services Program (LSP) Launch History",
-            "programCode": [
-                "026:046"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.nasa.gov/centers/kennedy/launchingrockets/archives/elv_archive-index.html",
-                    "mediaType": "text/html"
-                }
+            "references": [
+                "http://www.lsp.ksc.nasa.gov/"
             ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "NASA Launch Services Program (LSP) Launch History"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TERRA/MOPITT/MOP02N_L2.008",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2018-11-15. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/TERRA/MOPITT/MOP02N_L2.008. https://asdc.larc.nasa.gov/project/MOPITT.",
-            "issued": "2018-10-26",
-            "temporal": "2000-03-03T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "atmospheric water vapor",
-                "atmosphere",
-                "atmospheric temperature",
-                "atmospheric chemistry",
-                "earth science",
-                "atmospheric pressure"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Helen Worden",
                 "hasEmail": "mailto:hmw@ucar.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1575974134-LARC",
             "description": "MOP02N_8 is the Measurements Of Pollution In The Troposphere (MOPITT) Derived carbon monoxide (CO) (Near Infrared Radiances) version 8 dataset. It consists of geo-located, retrieved CO profiles and total column amounts for CO. Ancillary data concerning surface properties and cloud conditions at the locations of the retrieved parameters are also included. Each retrieval is accompanied by an estimated error. MOPITT was successfully launched into sun-synchronous polar orbit aboard Terra, NASA's first Earth Observing System spacecraft, on December 18, 1999. The MOPITT instrument was constructed by a consortium of Canadian companies and funded by the Space Science Division of the Canadian Space Agency. Data collection for this product was completed in March of 2020. Data collection for this product was completed in March of 2020.",
-            "graphic-preview-description": "MOPITT Visualizations",
-            "title": "MOPITT Derived CO (Near Infrared Radiances) V008",
-            "graphic-preview-file": "https://www2.acom.ucar.edu/mopitt/visualization",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMOPITT%2FMOP02N_L2.008",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMOPITT%2FMOP02N_L2.008",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1575974134-LARC",
-                    "description": "Earthdata Search for MOP02N_8 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for MOP02N_8 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1575974134-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MOPITT/MOP02N.008/contents.html",
-                    "description": "OPeNDAP data access for MOP02N_8",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for MOP02N_8",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MOPITT/MOP02N.008/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/TERRA/MOPITT/MOP02N_L2.008",
-                    "description": "DOI data set landing page for MOP02N_8",
+                {
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for MOP02N_8",
+                    "downloadURL": "https://doi.org/10.5067/TERRA/MOPITT/MOP02N_L2.008",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
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
-                    "downloadURL": "https://subset.larc.nasa.gov/mopitt/",
-                    "description": "MOPITT Search and Subsetting Web Application",
                     "@type": "dcat:Distribution",
+                    "description": "MOPITT Search and Subsetting Web Application",
+                    "downloadURL": "https://subset.larc.nasa.gov/mopitt/",
+                    "mediaType": "text/html",
                     "title": "Subset this dataset using a web based subsetter"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/MOPITT/MOP02N.008/",
-                    "description": "ASDC Direct Data Download for MOP02N_8",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for MOP02N_8",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/MOPITT/MOP02N.008/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/mopitt/tools/README_MOPITT_L2Viewer.txt",
-                    "description": "MOPITT Level 2 Viewer Software Readme File",
                     "@type": "dcat:Distribution",
+                    "description": "MOPITT Level 2 Viewer Software Readme File",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/mopitt/tools/README_MOPITT_L2Viewer.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/mopitt/quality_summaries/MOPV8_L2_DQ_statement.pdf",
-                    "description": "Quality Summary: MOPITT Level 2, Version 8 (V8; L2V18.0.x), first released December, 2018",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Summary: MOPITT Level 2, Version 8 (V8; L2V18.0.x), first released December, 2018",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/mopitt/quality_summaries/MOPV8_L2_DQ_statement.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's data quality document"
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
                 }
             ],
+            "graphic-preview-description": "MOPITT Visualizations",
+            "graphic-preview-file": "https://www2.acom.ucar.edu/mopitt/visualization",
+            "identifier": "C1575974134-LARC",
+            "issued": "2018-10-26",
+            "keyword": [
+                "atmospheric water vapor",
+                "atmosphere",
+                "atmospheric temperature",
+                "atmospheric chemistry",
+                "earth science",
+                "atmospheric pressure"
+            ],
+            "landingPage": "https://doi.org/10.5067/TERRA/MOPITT/MOP02N_L2.008",
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
+            "temporal": "2000-03-03T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "MOPITT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MOPITT Derived CO (Near Infrared Radiances) V008"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-04-10",
-            "temporal": "2021-04-10T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "location",
-                "space",
-                "ephemeris",
-                "topo",
-                "coordinates",
-                "coords",
-                "international",
-                "iss",
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
-            "identifier": "nasa-iss-data_2021-04-10",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2021-04-10",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1498623,431 +1498599,434 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2021-04-10",
+            "issued": "2021-04-10",
+            "keyword": [
+                "location",
+                "space",
+                "ephemeris",
+                "topo",
+                "coordinates",
+                "coords",
+                "international",
+                "iss",
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
+            "temporal": "2021-04-10T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2021-04-10"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-RSS-1-SROC8-V1.0",
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
+            "description": "The Cassini Radio Science Saturn Atmosphere and Ring Occultation Experiment (SROC8) Raw Data Archive is a time-ordered collection of radio science raw data acquired on July 7, August 4, 19, 26, and September 10, 2008, during the Cassini Extended Mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-rss-1-sroc8-v1.0_v2z4-ragy",
+            "issued": "2018-06-26",
+            "keyword": [
+                "cassini-huygens",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-RSS-1-SROC8-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-rss-1-sroc8-v1.0_v2z4-ragy",
-            "description": "The Cassini Radio Science Saturn Atmosphere and Ring Occultation Experiment (SROC8) Raw Data Archive is a time-ordered collection of radio science raw data acquired on July 7, August 4, 19, 26, and September 10, 2008, during the Cassini Extended Mission.",
-            "title": "CASSINI RSS RAW DATA SET - SROC8 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI RSS RAW DATA SET - SROC8 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-RPCLAP-2-AST2-EDITED-V1.0",
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
-                "21 lutetia",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains EDITED raw data from    Rosetta RPC-LAP, acquired during the flyby of asteroid 21 Lutetia.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-rpclap-2-ast2-edited-v1.0_v33t-4vje",
+            "issued": "2021-05-21",
+            "keyword": [
+                "21 lutetia",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-RPCLAP-2-AST2-EDITED-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-rpclap-2-ast2-edited-v1.0_v33t-4vje",
-            "description": "This dataset contains EDITED raw data from    Rosetta RPC-LAP, acquired during the flyby of asteroid 21 Lutetia.",
-            "title": "ROSETTA-ORBITER LUTETIA RPCLAP 2 AST2 EDITED V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER LUTETIA RPCLAP 2 AST2 EDITED V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4DN434S",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wang, P., C. Huang, E. C. Brown de Colstoun, J. C. Tilton, and B. Tan. 2017-12-06. Global Human Built-up And Settlement Extent (HBASE) Dataset From Landsat. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H4DN434S. https://doi.org/10.7927/H4DN434S.",
-            "issued": "2017-12-06",
-            "temporal": "2010-01-01T00:00:00Z/2010-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-06",
-            "references": [
-                "https://doi.org/10.7927/H4P55KKF",
-                "https://doi.org/10.7927/H48W3BCM"
-            ],
-            "keyword": [
-                "habitat conversion/fragmentation",
-                "earth science",
-                "human dimensions",
-                "human settlements"
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
-            "identifier": "C1517101319-SEDAC",
-            "description": "The Global Human Built-up And Settlement Extent (HBASE) Dataset from Landsat is a global map of HBASE derived from the Global Land Survey (GLS) Landsat dataset for the target year 2010. The HBASE dataset consists of two layers: 1) the HBASE mask; and 2) the pixel-wise probability of HBASE. These layers are co-registered to the same spatial extent at a common 30m spatial resolution. The spatial extent covers the entire globe except Antarctica and some small islands. This dataset is one of the first global, 30m datasets of urban extent to be derived from the GLS data for 2010 and is a companion dataset to the Global Man-made Impervious Surface (GMIS) dataset. The HBASE mask was created for post-processing of the GMIS dataset, but can also be utilized by users needing a binary map. The dataset is expected to have a rather broad spectrum of users, from those wishing to examine/study the fine details of urban land cover over the globe at full 30m resolution to global modelers trying to understand the climate/environmental impacts of man-made surfaces at continental to global scales. For example, the data are applicable to local modeling studies of urban impacts on the energy, water, and carbon cycles, as well as analyses at the individual country level.",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Wang, P., C. Huang, E. C. Brown de Colstoun, J. C. Tilton, and B. Tan",
-            "title": "Global Human Built-up And Settlement Extent (HBASE) Dataset From Landsat",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/ulandsat-hbase-v1/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Global Human Built-up And Settlement Extent (HBASE) Dataset from Landsat is a global map of HBASE derived from the Global Land Survey (GLS) Landsat dataset for the target year 2010. The HBASE dataset consists of two layers: 1) the HBASE mask; and 2) the pixel-wise probability of HBASE. These layers are co-registered to the same spatial extent at a common 30m spatial resolution. The spatial extent covers the entire globe except Antarctica and some small islands. This dataset is one of the first global, 30m datasets of urban extent to be derived from the GLS data for 2010 and is a companion dataset to the Global Man-made Impervious Surface (GMIS) dataset. The HBASE mask was created for post-processing of the GMIS dataset, but can also be utilized by users needing a binary map. The dataset is expected to have a rather broad spectrum of users, from those wishing to examine/study the fine details of urban land cover over the globe at full 30m resolution to global modelers trying to understand the climate/environmental impacts of man-made surfaces at continental to global scales. For example, the data are applicable to local modeling studies of urban impacts on the energy, water, and carbon cycles, as well as analyses at the individual country level.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4DN434S",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4DN434S",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/ulandsat/ulandsat-hbase-v1/ulandsat-hbase-v1-hbase-extent-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/ulandsat/ulandsat-hbase-v1/ulandsat-hbase-v1-hbase-extent-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ulandsat-hbase-v1/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ulandsat-hbase-v1/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ulandsat-hbase-v1/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ulandsat-hbase-v1/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/ulandsat-hbase-v1/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/ulandsat-hbase-v1/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ulandsat-hbase-v1/maps/services",
-                    "description": "Web Map Service Page",
                     "@type": "dcat:Distribution",
+                    "description": "Web Map Service Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ulandsat-hbase-v1/maps/services",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ulandsat-hbase-v1",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ulandsat-hbase-v1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/ulandsat-hbase-v1/maps",
+            "identifier": "C1517101319-SEDAC",
+            "issued": "2017-12-06",
+            "keyword": [
+                "habitat conversion/fragmentation",
+                "earth science",
+                "human dimensions",
+                "human settlements"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4DN434S",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-12-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H4P55KKF",
+                "https://doi.org/10.7927/H48W3BCM"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -58.349606 180.0 82.788372",
+            "temporal": "2010-01-01T00:00:00Z/2010-12-31T00:00:00Z",
             "theme": [
                 "ULANDSAT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Human Built-up And Settlement Extent (HBASE) Dataset From Landsat"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-A-PWS-4-SUMM-ISA60S-V1.0",
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
-                "ida"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Unknown",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-a-pws-4-summ-isa60s-v1.0_v37i-d2nq",
+            "issued": "2018-06-26",
+            "keyword": [
+                "galileo",
+                "ida"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-A-PWS-4-SUMM-ISA60S-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-a-pws-4-summ-isa60s-v1.0_v37i-d2nq",
-            "description": "Unknown",
-            "title": "GO A PWS RESAMP SUMMARY IDA SPECTRUM ANALYZER 60S V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GO A PWS RESAMP SUMMARY IDA SPECTRUM ANALYZER 60S V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ORBVIEW-2/SeaWiFS/L3M/POC/2022",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/ORBVIEW-2/SeaWiFS/L3M/POC/2022.",
-            "issued": "2022-09-14",
-            "temporal": "1997-09-04T00:00:00Z/2010-12-11T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-14",
-            "keyword": [
-                "oceans",
-                "earth science",
-                "ocean chemistry"
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
-            "identifier": "C1449645607-OB_DAAC",
             "description": "The SeaWiFS instrument was launched by Orbital Sciences Corporation on the OrbView-2 (a.k.a. SeaStar) satellite in August 1997, and collected data from September 1997 until the end of mission in December 2010. SeaWiFS had 8 spectral bands from 412 to 865 nm. It collected global data at 4 km resolution, and local data (limited onboard storage and direct broadcast) at 1 km. The mission and sensor were optimized for ocean color measurements, with a local noon (descending) equator crossing time orbit, fore-and-aft tilt capability, full dynamic range, and low polarization sensitivity.",
-            "title": "OrbView-2 SeaWiFS Global Mapped Particulate Organic Carbon (POC) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FORBVIEW-2%2FSeaWiFS%2FL3M%2FPOC%2F2022",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FORBVIEW-2%2FSeaWiFS%2FL3M%2FPOC%2F2022",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/ORBVIEW-2/SeaWiFS/L3M/POC/2022",
-                    "description": "SeaWiFS L3M Particulate Organic Carbon (POC) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "SeaWiFS L3M Particulate Organic Carbon (POC) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/ORBVIEW-2/SeaWiFS/L3M/POC/2022",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/SeaWiFS/L3SMI/",
-                    "description": "OB.DAAC OPeNDAP Site for OrbView-2 SeaWiFS Standard Mapped Image (SMI) Product",
                     "@type": "dcat:Distribution",
+                    "description": "OB.DAAC OPeNDAP Site for OrbView-2 SeaWiFS Standard Mapped Image (SMI) Product",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/SeaWiFS/L3SMI/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1449645607-OB_DAAC",
+            "issued": "2022-09-14",
+            "keyword": [
+                "oceans",
+                "earth science",
+                "ocean chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/ORBVIEW-2/SeaWiFS/L3M/POC/2022",
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
+            "temporal": "1997-09-04T00:00:00Z/2010-12-11T23:59:59Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OrbView-2 SeaWiFS Global Mapped Particulate Organic Carbon (POC) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1121",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Bustamante, M.M.C., and L.A. Martinelli. 2012. LBA-ECO ND-07 Carbon and Nitrogen in Cerrado Plants and Soils, Brasilia: 1999-2000. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1121",
-            "issued": "2023-10-03",
-            "temporal": "1999-12-01T00:00:00Z/2000-09-30T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-11",
-            "keyword": [
-                "land surface",
-                "vegetation",
-                "solid earth",
-                "soils",
-                "geochemistry",
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
-            "identifier": "C2780940083-ORNL_CLOUD",
             "description": "This data set provides (1) delta 15N ratios and nitrogen concentrations for foliar samples and (2) delta 13C and delta 15N ratios as well as carbon and nitrogen concentrations for soil samples collected from cerrado sites within the Ecological Reserve of the Brazilian Institute of Geography and Statistic (IBGE), Brasilia, Brazil. Foliar samples, collected from 320 individuals representing 45 woody tree and shrub species, and soil samples were collected from 5 cerrado locations (2 in campo sujo, 2 in cerrado denso and 1 in cerrado). Soil samples were collected to 450 cm depth in the campo sujo and 800 cm depth elsewhere. Samples were collected during the period December 1999 to September 2000.  Eiten (1972) described campo sujo as an open savanna with scattered trees and shrubs, cerrado sensu stricto as a savanna woodland with abundant evergreen and deciduous trees and shrubs and an herbaceous understory, and cerrado denso as medium to tall woodlands with closed or semiclosed canopies (Bustamante et al., 2004).There are two comma-delimited data files with this data set.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO ND-07 Carbon and Nitrogen in Cerrado Plants and Soils, Brasilia: 1999-2000",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1121",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1121",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/nutrient_dynamics/ND07_15N_Leaves_Soils/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/nutrient_dynamics/ND07_15N_Leaves_Soils/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/ND07_15N_Leaves_Soil.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/ND07_15N_Leaves_Soil.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1121",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1121",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/nutrient_dynamics/ND07_15N_Leaves_Soils/comp/ND07_15N_Leaves_Soil.PDF",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/nutrient_dynamics/ND07_15N_Leaves_Soils/comp/ND07_15N_Leaves_Soil.PDF",
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
+            "identifier": "C2780940083-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "land surface",
+                "vegetation",
+                "solid earth",
+                "soils",
+                "geochemistry",
+                "earth science",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1121",
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
+            "temporal": "1999-12-01T00:00:00Z/2000-09-30T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO ND-07 Carbon and Nitrogen in Cerrado Plants and Soils, Brasilia: 1999-2000"
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
-                "appel",
-                "knowledge",
-                "sharing",
-                "ask magazine"
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
-            "identifier": "NASA-860__29",
             "description": "Academy of Program/Project & Engineering Leadership's ASK Magazine archive.",
-            "title": "Academy of Program/Project & Engineering Leadership ASK Magazine Past Issues",
-            "programCode": [
-                "026:045"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1499055,45 +1499034,44 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/P3M",
+            "identifier": "NASA-860__29",
+            "issued": "2018-06-25",
+            "keyword": [
+                "appel",
+                "knowledge",
+                "sharing",
+                "ask magazine"
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
-                "cases",
-                "flow",
-                "compressible"
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
-            "identifier": "NASA-843__14",
             "description": "This grouping contains the compressible-flow cases from the 1980-81 Data Library.",
-            "title": "Collaborative Testing of Turbulence Models: Compressible Flow Cases from 1980-81 Data Library",
-            "programCode": [
-                "026:023"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1499101,101 +1499079,125 @@
                     "mediaType": "application/txt"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-843__14",
+            "issued": "2018-06-25",
+            "keyword": [
+                "turbulence",
+                "models",
+                "cases",
+                "flow",
+                "compressible"
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
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/914/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2014-07-02",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "nasa",
-                "dashlink",
-                "ames"
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
-            "identifier": "DASHLINK_914",
             "description": "Jam fault scenarios with tensile (-40 lbs) load (diagnostic and prognostic).",
-            "title": "2010_09_10_jam_-40 Lab",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/x-zip-compressed",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/2010_09_10_jam_-40.zip",
-                    "description": "2010_09_10_jam_-40.zip",
                     "@type": "dcat:Distribution",
+                    "description": "2010_09_10_jam_-40.zip",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/2010_09_10_jam_-40.zip",
+                    "mediaType": "application/x-zip-compressed",
                     "title": "2010_09_10_jam_-40.zip"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_914",
+            "issued": "2014-07-02",
+            "keyword": [
+                "nasa",
+                "dashlink",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/914/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "2010_09_10_jam_-40 Lab"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Acocirs_c2h4abund&version=1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Mole fractions during the 2010 Saturn Storm",
+            "identifier": "urn:nasa:pds:cocirs_c2h4abund",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "abundances",
                 "cassini",
                 "saturn"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Acocirs_c2h4abund&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:cocirs_c2h4abund",
-            "description": "Mole fractions during the 2010 Saturn Storm",
-            "title": "C2H4 mole fraction and temperature profiles after the 2010 Saturn Storm",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "C2H4 mole fraction and temperature profiles after the 2010 Saturn Storm"
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lcross-e-l-vis-2-raw-v1.0_v3q6-an8z",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "test image",
                 "earth",
@@ -1499203,216 +1499205,192 @@
                 "calibration",
                 "moon"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LCROSS-E%2FL-VIS-2-RAW-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lcross-e-l-vis-2-raw-v1.0_v3q6-an8z",
-            "description": "Raw, uncalibrated image data from the Visible Camera (VIS) aboard the Lunar Crater Observation and Sensing Satellite (LCROSS).",
-            "title": "LCROSS EARTH/MOON VISIBLE CAMERA 2 RAW DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "LCROSS EARTH/MOON VISIBLE CAMERA 2 RAW DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RPCMAG-4-CR5-RESAMPLED-V3.0",
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
-                "checkout"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains RESAMPLED Data of the CRUISE 5 phase (CR5).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rpcmag-4-cr5-resampled-v3.0_v3qt-qa2s",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "checkout"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RPCMAG-4-CR5-RESAMPLED-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rpcmag-4-cr5-resampled-v3.0_v3qt-qa2s",
-            "description": "This dataset contains RESAMPLED Data of the CRUISE 5 phase (CR5).",
-            "title": "ROSETTA-ORBITER CHECK RPCMAG 4 CR5 RESAMPLED V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECK RPCMAG 4 CR5 RESAMPLED V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-REX-2-PLUTOCRUISE-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Raw data taken by the New Horizons                Radio Science Experiment                                               instrument during the                                                    pluto cruise                                                           mission phase.  This is VERSION 1.0 of this data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-rex-2-plutocruise-v1.0_v3qu-uncw",
             "issued": "2018-09-05",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "calibration",
                 "sun",
                 "new horizons",
                 "earth"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-REX-2-PLUTOCRUISE-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-rex-2-plutocruise-v1.0_v3qu-uncw",
-            "description": "This data set contains Raw data taken by the New Horizons                Radio Science Experiment                                               instrument during the                                                    pluto cruise                                                           mission phase.  This is VERSION 1.0 of this data set.",
-            "title": "NEW HORIZONS                            \n      REX PLUTO CRUISE                                                        \n      RAW V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS                            \n      REX PLUTO CRUISE                                                        \n      RAW V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GNSS/GNSS_IGSRSUM_001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GGL/CDDIS. https://doi.org/10.5067/GNSS/GNSS_IGSRSUM_001.",
-            "issued": "1992-01-01",
-            "temporal": "1992-01-01T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-10-28",
-            "keyword": [
-                "gravity/gravitational field",
-                "solid earth",
-                "geodetics",
-                "earth science",
-                "tectonics"
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
-            "identifier": "C1427032847-CDDIS",
             "description": "This derived product set consists of Global Navigation Satellite System Rapid Orbit/Reference Frame Product Summary from the NASA Crustal Dynamics Data Information System (CDDIS). GNSS provide autonomous geo-spatial positioning with global coverage. GNSS data sets from ground receivers at the CDDIS consist primarily of the data from the U.S. Global Positioning System (GPS) and the Russian GLObal NAvigation Satellite System (GLONASS). Since 2011, the CDDIS GNSS archive includes data from other GNSS (Europe\u2019s Galileo, China\u2019s Beidou, Japan\u2019s Quasi-Zenith Satellite System/QZSS, the Indian Regional Navigation Satellite System/IRNSS, and worldwide Satellite Based Augmentation Systems/SBASs), which are similar to the U.S. GPS in terms of the satellite constellation, orbits, and signal structure.  Analysis Centers (ACs) of the International GNSS Service (IGS) retrieve GNSS data on regular schedules to produce GNSS satellite and ground receiver clock values. The IGS Analysis Center Coordinator (ACC) uses these individual AC solutions to generate the official IGS rapid combined orbit, satellite and receiver clock, and ERP products. The rapid combination is a daily solution available approximately 17 hours after the end of the previous UTC day. All satellite and receiver clock solution files utilize the clock RINEX format and span 24 hours from 00:00 to 23:45 UTC. The solution summary file details information about the generation of the daily rapid products.",
-            "title": "Global Navigation Satellite System (GNSS) Rapid Orbit/Clock/ERP Product Summary from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGNSS_IGSRSUM_001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGNSS_IGSRSUM_001",
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
-                    "downloadURL": "http://dx.doi.org/10.5067/GNSS/GNSS_IGSRSUM_001",
-                    "description": "URL for more information about GNSS derived products",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about GNSS derived products",
+                    "downloadURL": "http://dx.doi.org/10.5067/GNSS/GNSS_IGSRSUM_001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1427032847-CDDIS",
+            "issued": "1992-01-01",
+            "keyword": [
+                "gravity/gravitational field",
+                "solid earth",
+                "geodetics",
+                "earth science",
+                "tectonics"
+            ],
+            "landingPage": "https://doi.org/10.5067/GNSS/GNSS_IGSRSUM_001",
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
+            "temporal": "1992-01-01T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "IGS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Navigation Satellite System (GNSS) Rapid Orbit/Clock/ERP Product Summary from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA2502",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Santee, M., Livesey, N. and Read, W.. 2020-06-11. ML2CH3CL. Version 005. MLS/Aura Level 2 Methyl Chloride (CH3CL) Mixing Ratio V005. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA2502. https://disc.gsfc.nasa.gov/datacollection/ML2CH3CL_005.html. Digital Science Data.",
-            "issued": "2020-02-04",
-            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-02-04",
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
-            "identifier": "C1729925099-GES_DISC",
-            "description": "ML2CH3CL is the EOS Aura Microwave Limb Sounder (MLS) standard product for methyl chloride derived from radiances measured by the 640 GHz radiometer. The data version is 5.0. Data coverage is from August 8, 2004 to current. Spatial coverage is near-global (-82 degrees to +82 degrees latitude), with each profile spaced 1.5 degrees or ~165 km along the orbit track (roughly 15 orbits per day). The recommended useful vertical range is between 147 and 4.64 hPa, and the vertical resolution ranges between 4-6 km in the lower stratosphere and 8-10 km above 14 hPa. Users of the ML2CH3CL data product should read section 3.3 of the EOS MLS Level 2 Version 5 Quality Document for more information.\n\nThe data are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5), which is based on the version 5 Hierarchical Data Format, or HDF-5. Each file contains one swath object (profile data), with a set of data and geolocation fields, swath attributes, and metadata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML2CH3CL",
             "creator": "Santee, M., Livesey, N. and Read, W.",
-            "title": "MLS/Aura Level 2 Methyl Chloride (CH3CL) Mixing Ratio V005 (ML2CH3CL) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2CH3CL_005.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "ML2CH3CL is the EOS Aura Microwave Limb Sounder (MLS) standard product for methyl chloride derived from radiances measured by the 640 GHz radiometer. The data version is 5.0. Data coverage is from August 8, 2004 to current. Spatial coverage is near-global (-82 degrees to +82 degrees latitude), with each profile spaced 1.5 degrees or ~165 km along the orbit track (roughly 15 orbits per day). The recommended useful vertical range is between 147 and 4.64 hPa, and the vertical resolution ranges between 4-6 km in the lower stratosphere and 8-10 km above 14 hPa. Users of the ML2CH3CL data product should read section 3.3 of the EOS MLS Level 2 Version 5 Quality Document for more information.\n\nThe data are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5), which is based on the version 5 Hierarchical Data Format, or HDF-5. Each file contains one swath object (profile data), with a set of data and geolocation fields, swath attributes, and metadata.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA2502",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA2502",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1499422,484 +1499400,482 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML2CH3CL_005.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML2CH3CL_005.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level2/ML2CH3CL.005/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level2/ML2CH3CL.005/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level2/ML2CH3CL.005/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level2/ML2CH3CL.005/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML2CH3CL_005",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML2CH3CL_005",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2CH3CL_005.png",
+            "identifier": "C1729925099-GES_DISC",
+            "issued": "2020-02-04",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA2502",
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
+            "series-name": "ML2CH3CL",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MLS/Aura Level 2 Methyl Chloride (CH3CL) Mixing Ratio V005 (ML2CH3CL) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/PAL-LTER/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/PAL-LTER/DATA001.",
-            "issued": "1991-12-03",
-            "temporal": "1991-12-03T00:00:00Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "salinity/density",
-                "ocean chemistry",
-                "earth science",
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
-            "identifier": "C1633360585-OB_DAAC",
             "description": "Measurements made under the Long Term Ecological Research Network (LTER) Palmer Station Antarctica (PAL) program.",
-            "title": "Palmer Station Antarctica (PAL) Long Term Ecological Research Network (LTER)",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FPAL-LTER%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FPAL-LTER%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/PAL-LTER/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/PAL-LTER/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360585-OB_DAAC",
+            "issued": "1991-12-03",
+            "keyword": [
+                "salinity/density",
+                "ocean chemistry",
+                "earth science",
+                "oceans",
+                "ocean optics",
+                "ocean temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/PAL-LTER/DATA001",
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
+            "temporal": "1991-12-03T00:00:00Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Palmer Station Antarctica (PAL) Long Term Ecological Research Network (LTER)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-X-PPR-2-EDR-CHECKOUT-V1.0",
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
+            "description": "added ARCHIVE_STATUS, ,This data set contains the R_EDR data for the Galileo Orbiter PPR instrument for the period corresponding to the initial turn-on and checkout of the PPR in December 1989.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-x-ppr-2-edr-checkout-v1.0_v3vr-wbrg",
+            "issued": "2018-06-26",
+            "keyword": [
+                "galileo"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-X-PPR-2-EDR-CHECKOUT-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-x-ppr-2-edr-checkout-v1.0_v3vr-wbrg",
-            "description": "added ARCHIVE_STATUS, ,This data set contains the R_EDR data for the Galileo Orbiter PPR instrument for the period corresponding to the initial turn-on and checkout of the PPR in December 1989.",
-            "title": "GLL PPR INITIAL CHECKOUT R_EDR",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GLL PPR INITIAL CHECKOUT R_EDR"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AVHRR/N14_AVH13C1.006",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The Long-Term Data Record (LTDR) project. 2023-07-25. NOAA-14 AVHRR Atmospherically Corrected Normalized Difference Vegetation Index Daily L3 Global 0.05 Deg. CMG. Version 6. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/AVHRR/N14_AVH13C1.006.",
-            "issued": "2022-07-21",
-            "temporal": "1995-01-01T00:00:00Z/2000-11-01T23:59:59.900Z",
-            "@type": "dcat:Dataset",
-            "modified": "2000-11-01",
-            "keyword": [
-                "earth science",
-                "land use/land cover",
-                "vegetation",
-                "land surface",
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
-            "identifier": "C2738316689-LAADS",
-            "description": "The Long-Term Data Record (LTDR) produces, validates, and distributes a global land surface climate data record (CDR) that uses both mature and well-tested algorithms in concert with the best-available polar-orbiting satellite data from past to the present.   The CDR is critically important to studying global climate change.  The LTDR project is unique in that it serves as a bridge that connects data derived from the NOAA Advanced Very High Resolution Radiometer (AVHRR), the EOS Moderate resolution Imaging Spectroradiometer (MODIS), the Suomi National Polar-orbiting Partnership (SNPP) Visible Infrared Imaging Radiometer Suite (VIIRS), and Joint Polar Satellite System (JPSS) VIIRS missions.  The LTDR draws from the following eight AVHRR missions: \r\nNOAA-7, NOAA-9, NOAA-11, NOAA-14, NOAA-16, NOAA-18, NOAA-19, and MetOp-B.\r\nCurrently, the project generates a daily surface reflectance product as the fundamental climate data record (FCDR) and derives daily Normalized Differential Vegetation Index (NDVI) and Leaf-Area Index/fraction of absorbed Photosynthetically Active Radiation (LAI/fPAR) as two thematic CDRs (TCDR).  LAI/fPAR was developed as an experimental product.\r\n\r\nThe NOAA-14 AVHRR Atmospherically Corrected Normalized Difference Vegetation Index (NDVI) Daily L3 Global 0.05 Deg CMG, short-name N14_AVH13C1 is generated from GIMMS Advanced Processing System (GAPS) BRDF-corrected Surface Reflectance product (N14_AVH01C1). The N14_AVH13C1 product is available in HDF4 file format.",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "The Long-Term Data Record (LTDR) project",
-            "title": "NOAA-14 AVHRR Atmospherically Corrected Normalized Difference Vegetation Index Daily L3 Global 0.05 Deg. CMG",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Long-Term Data Record (LTDR) produces, validates, and distributes a global land surface climate data record (CDR) that uses both mature and well-tested algorithms in concert with the best-available polar-orbiting satellite data from past to the present.   The CDR is critically important to studying global climate change.  The LTDR project is unique in that it serves as a bridge that connects data derived from the NOAA Advanced Very High Resolution Radiometer (AVHRR), the EOS Moderate resolution Imaging Spectroradiometer (MODIS), the Suomi National Polar-orbiting Partnership (SNPP) Visible Infrared Imaging Radiometer Suite (VIIRS), and Joint Polar Satellite System (JPSS) VIIRS missions.  The LTDR draws from the following eight AVHRR missions: \r\nNOAA-7, NOAA-9, NOAA-11, NOAA-14, NOAA-16, NOAA-18, NOAA-19, and MetOp-B.\r\nCurrently, the project generates a daily surface reflectance product as the fundamental climate data record (FCDR) and derives daily Normalized Differential Vegetation Index (NDVI) and Leaf-Area Index/fraction of absorbed Photosynthetically Active Radiation (LAI/fPAR) as two thematic CDRs (TCDR).  LAI/fPAR was developed as an experimental product.\r\n\r\nThe NOAA-14 AVHRR Atmospherically Corrected Normalized Difference Vegetation Index (NDVI) Daily L3 Global 0.05 Deg CMG, short-name N14_AVH13C1 is generated from GIMMS Advanced Processing System (GAPS) BRDF-corrected Surface Reflectance product (N14_AVH01C1). The N14_AVH13C1 product is available in HDF4 file format.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAVHRR%2FN14_AVH13C1.006",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAVHRR%2FN14_AVH13C1.006",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ltdr.modaps.eosdis.nasa.gov/cgi-bin/ltdr/ltdrPage.cgi?fileName=docs",
-                    "description": "Overview of LTDR Products documents",
                     "@type": "dcat:Distribution",
+                    "description": "Overview of LTDR Products documents",
+                    "downloadURL": "https://ltdr.modaps.eosdis.nasa.gov/cgi-bin/ltdr/ltdrPage.cgi?fileName=docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/1/N14_AVH13C1--466",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/1/N14_AVH13C1--466",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/466/N14_AVH13C1/",
-                    "description": "Direct access to C6 N14_AVH13C1 data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to C6 N14_AVH13C1 data set.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/466/N14_AVH13C1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/QA_WWW/forPage/user_guide/avhrr/LTDR_Ver5_Products_UserGuide_v1.0.pdf",
-                    "description": "A combined User's Guides for all L3 LTDR products",
                     "@type": "dcat:Distribution",
+                    "description": "A combined User's Guides for all L3 LTDR products",
+                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/QA_WWW/forPage/user_guide/avhrr/LTDR_Ver5_Products_UserGuide_v1.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "identifier": "C2738316689-LAADS",
+            "issued": "2022-07-21",
+            "keyword": [
+                "earth science",
+                "land use/land cover",
+                "vegetation",
+                "land surface",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/AVHRR/N14_AVH13C1.006",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2000-11-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1995-01-01T00:00:00Z/2000-11-01T23:59:59.900Z",
             "theme": [
                 "NOAA - SPACE WEATHER PROGRAM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NOAA-14 AVHRR Atmospherically Corrected Normalized Difference Vegetation Index Daily L3 Global 0.05 Deg. CMG"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-SWAP-3-JUPITER-V3.0",
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
+            "description": "This data set contains Calibrated data taken by the New Horizons         Solar Wind Around Pluto                                                instrument during the                                                    Jupiter encounter                                                      mission phase.  This is VERSION 3.0 of this data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-swap-3-jupiter-v3.0_v3xx-nwaz",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-SWAP-3-JUPITER-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-swap-3-jupiter-v3.0_v3xx-nwaz",
-            "description": "This data set contains Calibrated data taken by the New Horizons         Solar Wind Around Pluto                                                instrument during the                                                    Jupiter encounter                                                      mission phase.  This is VERSION 3.0 of this data set.",
-            "title": "NEW HORIZONS                            \n      SWAP JUPITER ENCOUNTER                                                  \n      CALIBRATED V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS                            \n      SWAP JUPITER ENCOUNTER                                                  \n      CALIBRATED V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SASSIE-SNK2",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Schanze, Julian. 2023-05-25. SASSIE Arctic Field Campaign Shipboard Salinity Snake Data Fall 2022. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, SASSIE Project Data Manager, Frederick Bingham. https://doi.org/10.5067/SASSIE-SNK2. http://doi.org/10.5067/SASSIE-SNK2.",
-            "issued": "2022-09-09",
-            "temporal": "2022-09-09T00:00:00Z/2022-10-03T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-10-02",
-            "keyword": [
-                "oceans",
-                "earth science",
-                "salinity/density",
-                "ocean temperature"
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
-            "identifier": "C2684906861-POCLOUD",
-            "description": "The Salinity and Stratification at the Sea Ice Edge (SASSIE) project is a NASA experiment that aims to understand how salinity anomalies in the upper ocean generated by melting sea ice affect sea surface temperature (SST), stratification, and subsequent sea-ice growth. SASSIE involved a field campaign that sampled the transition from summer melt to autumn ice advance in the Beaufort Sea during August-October 2022, making intensive in situ and remote sensing observations within ~200km of the sea ice edge. This dataset contains salinity and temperature measurements collected by a shipboard salinity snake. The salinity snake system consisted of a ship-mounted boom with a length of 10m to provide sampling of undisturbed water at a depth of 1-2cm. Salinity data are delayed by 40s, which is the average residence time in the hose, pump, and shipboard system before being analyzed. Data are available in netCDF format.",
             "creator": "Schanze, Julian",
-            "title": "SASSIE Arctic Field Campaign Shipboard Salinity Snake Data Fall 2022",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Salinity and Stratification at the Sea Ice Edge (SASSIE) project is a NASA experiment that aims to understand how salinity anomalies in the upper ocean generated by melting sea ice affect sea surface temperature (SST), stratification, and subsequent sea-ice growth. SASSIE involved a field campaign that sampled the transition from summer melt to autumn ice advance in the Beaufort Sea during August-October 2022, making intensive in situ and remote sensing observations within ~200km of the sea ice edge. This dataset contains salinity and temperature measurements collected by a shipboard salinity snake. The salinity snake system consisted of a ship-mounted boom with a length of 10m to provide sampling of undisturbed water at a depth of 1-2cm. Salinity data are delayed by 40s, which is the average residence time in the hose, pump, and shipboard system before being analyzed. Data are available in netCDF format.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSASSIE-SNK2",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSASSIE-SNK2",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://salinity.oceansciences.org/sassie.htm",
-                    "description": "SASSIE Project Website",
                     "@type": "dcat:Distribution",
+                    "description": "SASSIE Project Website",
+                    "downloadURL": "https://salinity.oceansciences.org/sassie.htm",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://podaac.jpl.nasa.gov/sassie",
-                    "description": "Field Campaign and Instrument Overview",
                     "@type": "dcat:Distribution",
+                    "description": "Field Campaign and Instrument Overview",
+                    "downloadURL": "http://podaac.jpl.nasa.gov/sassie",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://salinity.oceansciences.org/docs/SASSIE_overview.pdf",
-                    "description": "SASSIE Overview Document",
                     "@type": "dcat:Distribution",
+                    "description": "SASSIE Overview Document",
+                    "downloadURL": "https://salinity.oceansciences.org/docs/SASSIE_overview.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2684906861-POCLOUD",
-                    "description": "Browse and download granules over HTTPS using the virtual directories",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2684906861-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2684906861-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2684906861-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/SASSIE-SNK2",
-                    "description": "Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "Dataset Landing Page",
+                    "downloadURL": "https://doi.org/10.5067/SASSIE-SNK2",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2684906861-POCLOUD",
+            "issued": "2022-09-09",
+            "keyword": [
+                "oceans",
+                "earth science",
+                "salinity/density",
+                "ocean temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/SASSIE-SNK2",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-10-02",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
             "spatial": "-168.1 66.0 -144.8 73.6",
+            "temporal": "2022-09-09T00:00:00Z/2022-10-03T23:59:59Z",
             "theme": [
                 "SASSIE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SASSIE Arctic Field Campaign Shipboard Salinity Snake Data Fall 2022"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/DFO_CANADA_TIME_SERIES/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/DFO_CANADA_TIME_SERIES/DATA001.",
-            "issued": "2000-04-06",
-            "temporal": "2000-04-06T12:44:46Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean temperature",
-                "salinity/density",
-                "ocean optics",
-                "ocean chemistry",
-                "earth science",
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
-            "identifier": "C1633360201-OB_DAAC",
             "description": "This time series of chl data was obtained from the BioChem archive run by the Department of Fisheries and Oceans, Canada. Water sampling and chlorophyll analysis methods are described in the Mitchell et al. (2002) protocol document accompanying the data.DFO (2014). BioChem: database of biological and chemical oceanographic data. Department of Fisheries and Oceans, Canada.http://isdm.gc.ca/biochem/biochem-eng.htm",
-            "title": "Chlorophyll time series, Department of Fisheries and Oceans (DFO), Canada",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FDFO_CANADA_TIME_SERIES%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FDFO_CANADA_TIME_SERIES%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/DFO_Canada_Time_Series/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/DFO_Canada_Time_Series/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360201-OB_DAAC",
+            "issued": "2000-04-06",
+            "keyword": [
+                "ocean temperature",
+                "salinity/density",
+                "ocean optics",
+                "ocean chemistry",
+                "earth science",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/DFO_CANADA_TIME_SERIES/DATA001",
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
+            "temporal": "2000-04-06T12:44:46Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Chlorophyll time series, Department of Fisheries and Oceans (DFO), Canada"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2082387275-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "OCO Science Team/Michael Gunson, Annmarie Eldering. 2021-06-10. OCO3_L1B_Science. Version 10. OCO-3 Level 1B calibrated, geolocated science spectra, Forward Processing V10. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/OCO3_L1B_Science_10.html. Digital Science Data.",
-            "issued": "2021-05-31",
-            "temporal": "2019-08-06T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-31",
-            "keyword": [
-                "atmospheric chemistry",
-                "earth science",
-                "spectral/engineering",
-                "atmosphere",
-                "infrared wavelengths"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANDREY SAVTCHENKO",
                 "hasEmail": "mailto:andrey.savtchenko@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C2082387275-GES_DISC",
-            "description": "Version 10 is the current version of the data set. Older versions will no longer be available and are superseded by Version 10.\n\nThe Orbiting Carbon Observatory -3 (OCO-3) was deployed to the International Space Station in May, 2019. It is technically a single instrument, almost identical to OCO-2.\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere.\n\nOCO-3 incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers. The three spectrometers have different characteristics and are calibrated independently. \n\nOxygen-A Band cloud screening algorithm is one of the primary cloud screening tools implemented in the operational OCO processing pipeline. The algorithm was introduced and applied to early GOSAT data  with further analysis performed on OCO-2 simulations.\n\nThe OCO ABO2 algorithm employs a fast Bayesian retrieval to estimate surface pressure and surface albedo from high resolution spectra of the molecular oxygen (O2) A-band, near 0.765 \u00b5m. The radiative transfer forward model (FM) assumes a clear-sky condition, i.e. Rayleigh scattering only, such that differences between the modeled and measured radiances are apparent when the measurement scene contains cloud or aerosol.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OCO3_L1B_Science",
             "creator": "OCO Science Team/Michael Gunson, Annmarie Eldering",
-            "title": "OCO-3 Level 1B calibrated, geolocated science spectra, Forward Processing V10 (OCO3_L1B_Science) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO3_logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Version 10 is the current version of the data set. Older versions will no longer be available and are superseded by Version 10.\n\nThe Orbiting Carbon Observatory -3 (OCO-3) was deployed to the International Space Station in May, 2019. It is technically a single instrument, almost identical to OCO-2.\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere.\n\nOCO-3 incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers. The three spectrometers have different characteristics and are calibrated independently. \n\nOxygen-A Band cloud screening algorithm is one of the primary cloud screening tools implemented in the operational OCO processing pipeline. The algorithm was introduced and applied to early GOSAT data  with further analysis performed on OCO-2 simulations.\n\nThe OCO ABO2 algorithm employs a fast Bayesian retrieval to estimate surface pressure and surface albedo from high resolution spectra of the molecular oxygen (O2) A-band, near 0.765 \u00b5m. The radiative transfer forward model (FM) assumes a clear-sky condition, i.e. Rayleigh scattering only, such that differences between the modeled and measured radiances are apparent when the measurement scene contains cloud or aerosol.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1499908,300 +1499884,326 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO3_L1B_Science_10.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO3_L1B_Science_10.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO3_L2_DQ_Statement_v10.pdf",
-                    "description": "OCO-3 Data Quality Statement",
                     "@type": "dcat:Distribution",
+                    "description": "OCO-3 Data Quality Statement",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO3_L2_DQ_Statement_v10.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO3_L1B_Science",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO3_L1B_Science",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO3_L1B_Science.10/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO3_L1B_Science.10/contents.html",
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
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO3_DATA/OCO3_L1B_Science.10/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO3_DATA/OCO3_L1B_Science.10/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO_L1B_ATBD.pdf",
-                    "description": "Level  1B Algorithm Theoretical Basis (ATBD)",
                     "@type": "dcat:Distribution",
+                    "description": "Level  1B Algorithm Theoretical Basis (ATBD)",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO_L1B_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/SDOS_SIS_L1b.V7.pdf",
-                    "description": "Level 1B Software Interface Specification containing description of all data objects in data files",
                     "@type": "dcat:Distribution",
+                    "description": "Level 1B Software Interface Specification containing description of all data objects in data files",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/SDOS_SIS_L1b.V7.pdf",
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
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=OCO-2+Documents",
-                    "description": "OCO Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "OCO Documentation",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=OCO-2+Documents",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=OCO-3+Known+Data+Issues",
-                    "description": "OCO-3 Data Gaps",
                     "@type": "dcat:Distribution",
+                    "description": "OCO-3 Data Gaps",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=OCO-3+Known+Data+Issues",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO3_logo.jpg",
+            "identifier": "C2082387275-GES_DISC",
+            "issued": "2021-05-31",
+            "keyword": [
+                "atmospheric chemistry",
+                "earth science",
+                "spectral/engineering",
+                "atmosphere",
+                "infrared wavelengths"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2082387275-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-05-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "OCO3_L1B_Science",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2019-08-06T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "OCO-3",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OCO-3 Level 1B calibrated, geolocated science spectra, Forward Processing V10 (OCO3_L1B_Science) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/IMPACTS/NEXRAD/DATA123",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Brodzik, Stacy .2022. KLWX NEXRAD IMPACTS [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/IMPACTS/NEXRAD/DATA123",
-            "issued": "2022-03-23",
-            "temporal": "2020-01-01T00:05:11Z/2020-03-01T00:01:45Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
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
-            "identifier": "C2012931540-GHRC_DAAC",
             "description": "The KLWX NEXRAD IMPACTS dataset consists of Next Generation Weather Radar (NEXRAD) Level II surveillance data that were collected at 31 NEXRAD sites from January 1 to March 1, 2020 during the Investigation of Microphysics and Precipitation for Atlantic Coast-Threatening Snowstorms  (IMPACTS) field campaign. IMPACTS was a three-year sequence of winter season deployments conducted to study snowstorms over the U.S Atlantic Coast. The campaign aimed to (1) Provide observations critical to understanding the mechanisms of snowband formation, organization, and evolution; (2) Examine how the microphysical characteristics and likely growth mechanisms of snow particles vary across snowbands; and (3) Improve snowfall remote sensing interpretation and modeling to significantly advance prediction capabilities. There are currently 160 Weather Surveillance Radar-1988 Doppler (WSR-88D) or NEXRAD sites throughout the United States and abroad. This Level II dataset contains meteorological and dual-polarization base data quantities including: radar reflectivity, radial velocity, spectrum width, differential reflectivity, differential phase, and cross correlation ratio. The IMPACTS NEXRAD Level II data files are available in netCDF-4 format. It should be noted that this dataset will be updated in subsequent years of the IMPACTS campaign.",
-            "title": "KLWX NEXRAD IMPACTS V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FNEXRAD%2FDATA123",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FNEXRAD%2FDATA123",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=klwximpacts",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=klwximpacts",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.ofcm.gov/publications/fmh/FMH11/fmh-11B-2005.pdf",
-                    "description": "Federal Meteorological Handbook No. 11 Part B: Doppler Radar Theory and Meteorology",
                     "@type": "dcat:Distribution",
+                    "description": "Federal Meteorological Handbook No. 11 Part B: Doppler Radar Theory and Meteorology",
+                    "downloadURL": "http://www.ofcm.gov/publications/fmh/FMH11/fmh-11B-2005.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.ofcm.gov/publications/fmh/FMH11/FMH11D-2006.pdf",
-                    "description": "Federal Meteorological Handbook No. 11 Part D: WSR-88D Unit Description and Operational Applications",
                     "@type": "dcat:Distribution",
+                    "description": "Federal Meteorological Handbook No. 11 Part D: WSR-88D Unit Description and Operational Applications",
+                    "downloadURL": "http://www.ofcm.gov/publications/fmh/FMH11/FMH11D-2006.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.ofcm.gov/publications/fmh/FMH11/2016FMH11PTA.pdf",
-                    "description": "Federal Meteorological Handbook No. 11 Part A: System Concepts, Responsibilities, and Procedures",
                     "@type": "dcat:Distribution",
+                    "description": "Federal Meteorological Handbook No. 11 Part A: System Concepts, Responsibilities, and Procedures",
+                    "downloadURL": "http://www.ofcm.gov/publications/fmh/FMH11/2016FMH11PTA.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.ofcm.gov/publications/fmh/FMH11/fmh11partC.pdf",
-                    "description": "Federal Meteorological Handbook No. 11 Part C: WSR-88D Products and Algorithms",
                     "@type": "dcat:Distribution",
+                    "description": "Federal Meteorological Handbook No. 11 Part C: WSR-88D Products and Algorithms",
+                    "downloadURL": "http://www.ofcm.gov/publications/fmh/FMH11/fmh11partC.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.5067/IMPACTS/DATA101",
-                    "description": "IMPACTS Field Campaign Collection DOI",
                     "@type": "dcat:Distribution",
+                    "description": "IMPACTS Field Campaign Collection DOI",
+                    "downloadURL": "http://dx.doi.org/10.5067/IMPACTS/DATA101",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/impacts",
-                    "description": "IMPACTS Field Campaign Information",
                     "@type": "dcat:Distribution",
+                    "description": "IMPACTS Field Campaign Information",
+                    "downloadURL": "https://espo.nasa.gov/impacts",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncdc.noaa.gov/data-access/radar-data/nexrad",
-                    "description": "NEXRAD Information",
                     "@type": "dcat:Distribution",
+                    "description": "NEXRAD Information",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/NEXRAD/KLWX/doc/nexrad_datasets.pdf",
-                    "description": "NEXRAD IMPACTS User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "NEXRAD IMPACTS User Guide",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/NEXRAD/KLWX/doc/nexrad_datasets.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://go.gale.com/ps/anonymous?id=GALE%7CA9215749&sid=googleScholar&v=2.1&it=r&linkaccess=abs&issn=01926225&p=AONE&sw=w",
-                    "description": "Nexrad: next generation weather radar (WSR-88D)",
                     "@type": "dcat:Distribution",
+                    "description": "Nexrad: next generation weather radar (WSR-88D)",
+                    "downloadURL": "https://go.gale.com/ps/anonymous?id=GALE%7CA9215749&sid=googleScholar&v=2.1&it=r&linkaccess=abs&issn=01926225&p=AONE&sw=w",
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
-                    "downloadURL": "https://doi.org/10.1175/BAMS-D-20-0246.1",
-                    "description": "Chasing Snowstorms: The Investigation of Microphysics and Precipitation for Atlantic Coast-Threatening Snowstorms (IMPACTS) Campaign",
                     "@type": "dcat:Distribution",
+                    "description": "Chasing Snowstorms: The Investigation of Microphysics and Precipitation for Atlantic Coast-Threatening Snowstorms (IMPACTS) Campaign",
+                    "downloadURL": "https://doi.org/10.1175/BAMS-D-20-0246.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1109/IGARSS46834.2022.9883693",
-                    "description": "Investigation of Microphysics and Precipitation for Atlantic Coast Threatening Snowstorms (Impacts): The 2022 Deployment",
                     "@type": "dcat:Distribution",
+                    "description": "Investigation of Microphysics and Precipitation for Atlantic Coast Threatening Snowstorms (Impacts): The 2022 Deployment",
+                    "downloadURL": "https://doi.org/10.1109/IGARSS46834.2022.9883693",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/impacts",
-                    "description": "IMPACTS Field Campaign Project Homepage",
                     "@type": "dcat:Distribution",
+                    "description": "IMPACTS Field Campaign Project Homepage",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/impacts",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/micro-articles/investigation-microphysics-and-precipitation-atlantic-coast-threatening-snowstorms",
-                    "description": "IMPACTS Field Campaign Micro Article",
                     "@type": "dcat:Distribution",
+                    "description": "IMPACTS Field Campaign Micro Article",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/micro-articles/investigation-microphysics-and-precipitation-atlantic-coast-threatening-snowstorms",
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
+            "identifier": "C2012931540-GHRC_DAAC",
+            "issued": "2022-03-23",
+            "keyword": [
+                "spectral/engineering",
+                "radar",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/IMPACTS/NEXRAD/DATA123",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-01-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/MSFC/GHRC"
+            },
             "spatial": "-82.803 34.846 -72.172 43.106",
+            "temporal": "2020-01-01T00:05:11Z/2020-03-01T00:01:45Z",
             "theme": [
                 "IMPACTS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "KLWX NEXRAD IMPACTS V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-E%2FV%2FH-MASCS-2-UVVS-EDR-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Abstract ======== This data set consists of the MESSENGER MASCS UVVS uncalibrated observations, also known as EDRs. The MASCS UVVS experiment is a scanning grating monochromator equipped with three photomultiplier tubes. There are three UUVS EDR data products, one for each detector, which cover the wavelength ranges of the far ultraviolet (FUV), middle ultraviolet (MUV), and visible (VIS).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-e-v-h-mascs-2-uvvs-edr-v1.0_v47v-r8cv",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "messenger",
                 "calibration",
@@ -1500209,39 +1500211,39 @@
                 "earth",
                 "venus"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-E%2FV%2FH-MASCS-2-UVVS-EDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-e-v-h-mascs-2-uvvs-edr-v1.0_v47v-r8cv",
-            "description": "Abstract ======== This data set consists of the MESSENGER MASCS UVVS uncalibrated observations, also known as EDRs. The MASCS UVVS experiment is a scanning grating monochromator equipped with three photomultiplier tubes. There are three UUVS EDR data products, one for each detector, which cover the wavelength ranges of the far ultraviolet (FUV), middle ultraviolet (MUV), and visible (VIS).",
-            "title": "MESSENGER E/V/H MASCS 2 UVVS UNCALIBRATED DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MESSENGER E/V/H MASCS 2 UVVS UNCALIBRATED DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-REX-3-PLUTO-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Calibrated data taken by the New Horizons         Radio Science Experiment                                               instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 1.0 of this data set.                    This data set contains REX observations taken during the                 the Approach (Jan-Jul, 2015), Encounter, Departure, and                  Transition mission sub-phases, including flyby observations              taken on 14 July, 2015, and departure and calibration data               through late October, 2016.  This data set completes the                 Pluto mission phase deliveries for REX.                                  The REX datasets over the mission include calibrations using known radio sources, Jupiter, and cold sky measurements; operational readiness       tests (ORTs); internal test pattern calibration; and prime science       radiometry and occultation observations during the Pluto Encounter.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-rex-3-pluto-v1.0_v48d-gcjf",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "m 1",
                 "pluto",
@@ -1500251,159 +1500253,133 @@
                 "charon",
                 "earth"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-REX-3-PLUTO-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-rex-3-pluto-v1.0_v48d-gcjf",
-            "description": "This data set contains Calibrated data taken by the New Horizons         Radio Science Experiment                                               instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 1.0 of this data set.                    This data set contains REX observations taken during the                 the Approach (Jan-Jul, 2015), Encounter, Departure, and                  Transition mission sub-phases, including flyby observations              taken on 14 July, 2015, and departure and calibration data               through late October, 2016.  This data set completes the                 Pluto mission phase deliveries for REX.                                  The REX datasets over the mission include calibrations using known radio sources, Jupiter, and cold sky measurements; operational readiness       tests (ORTs); internal test pattern calibration; and prime science       radiometry and occultation observations during the Pluto Encounter.",
-            "title": "NEW HORIZONS                            \n      REX PLUTO ENCOUNTER                                                     \n      CALIBRATED V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS                            \n      REX PLUTO ENCOUNTER                                                     \n      CALIBRATED V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J%2FS%2FSS-PWS-2-RDR-SAFULL-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set includes nearly all measurements collected from the spectrum analyzer component of the Plasma Wave Spectrometer (PWS) onboard Voyager 1 for the entire mission.  Some noise lines during the planetary encounters have been edited from the data set.  Each sweep of the PWS spectrum analyzer records spectral densities in 16 frequency channels from 50 Hz to 10 kHz.  The values in this data set are given as instrument data numbers.  Instructions for producing calibrated values are provided.  An example C-language program which reads this data set and produces calibrated values is also provided.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-s-ss-pws-2-rdr-safull-v1.0_v49t-b3n3",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "saturn",
                 "jupiter",
                 "voyager",
                 "solar system"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J%2FS%2FSS-PWS-2-RDR-SAFULL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-s-ss-pws-2-rdr-safull-v1.0_v49t-b3n3",
-            "description": "This data set includes nearly all measurements collected from the spectrum analyzer component of the Plasma Wave Spectrometer (PWS) onboard Voyager 1 for the entire mission.  Some noise lines during the planetary encounters have been edited from the data set.  Each sweep of the PWS spectrum analyzer records spectral densities in 16 frequency channels from 50 Hz to 10 kHz.  The values in this data set are given as instrument data numbers.  Instructions for producing calibrated values are provided.  An example C-language program which reads this data set and produces calibrated values is also provided.",
-            "title": "VG1 J/S/SS PWS EDITED SPECTRUM ANALYZER FULL RES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG1 J/S/SS PWS EDITED SPECTRUM ANALYZER FULL RES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GPM/SSMI/F08/GPROFCLIM/3A-DAY/07",
             "citation": "GPM Science Team. 2022-05-09. GPM_3GPROFF08SSMI_DAY_CLIM. Version 07. GPM SSMI on F08 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/SSMI/F08/GPROFCLIM/3A-DAY/07. https://disc.gsfc.nasa.gov/datacollection/GPM_3GPROFF08SSMI_DAY_CLIM_07.html. Digital Science Data.",
-            "issued": "2022-05-09",
-            "temporal": "1987-07-09T00:00:00Z/1991-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-01",
-            "keyword": [
-                "atmospheric water vapor",
-                "earth science",
-                "atmosphere",
-                "precipitation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "GEORGE HUFFMAN",
                 "hasEmail": "mailto:George.J.Huffman@nasa.gov"
             },
+            "creator": "GPM Science Team",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2264135026-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Version 7 is the current version of the data set. Older versions will no longer be available and have been superseded by the current version. \n\nThe \"CLIM\"  products differ from their \"regular\" counterparts (without the \"CLIM\" in the name) by the ancillary data they use. They are Climate-Reference products, which requires homogeneous ancillary data over the climate time series.  Hence, the ECMWF-Interim (European Centre for Medium-Range Weather Forecasts, 2-3 months lag behind the regular production) reanalysis is used as ancillary data to derive surface and atmospheric conditions required by the GPROF algorithm for the \"CLIM\" output. The GPROF databases are also adjusted accordingly for these climate-referenced retrievals.\n\n3GPROF products provide global gridded monthly/daily precipitation averages from multiple satellites that can be used for climate studies. The 3GPROF products are based on retrievals from high-quality microwave sensors, which are sensitive to liquid and ice-phase precipitation hydrometeors in the atmosphere.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "GPM_3GPROFF08SSMI_DAY_CLIM",
-            "creator": "GPM Science Team",
-            "title": "GPM SSMI on F08 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFF08SSMI_DAY_CLIM) at GES DISC",
-            "graphic-preview-description": "GPM SSMI on F08 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree (GPM_3GPROFF08SSMI_DAY_CLIM)",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFF08SSMI_DAY_CLIM_07.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FSSMI%2FF08%2FGPROFCLIM%2F3A-DAY%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FSSMI%2FF08%2FGPROFCLIM%2F3A-DAY%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFF08SSMI_DAY_CLIM_07.png",
-                    "description": "GPM SSMI on F08 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree (GPM_3GPROFF08SSMI_DAY_CLIM)",
                     "@type": "dcat:Distribution",
+                    "description": "GPM SSMI on F08 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree (GPM_3GPROFF08SSMI_DAY_CLIM)",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFF08SSMI_DAY_CLIM_07.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3GPROFF08SSMI_DAY_CLIM_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3GPROFF08SSMI_DAY_CLIM_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3GPROFF08SSMI_DAY_CLIM.07/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3GPROFF08SSMI_DAY_CLIM.07/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L3/GPM_3GPROFF08SSMI_DAY_CLIM.07/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L3/GPM_3GPROFF08SSMI_DAY_CLIM.07/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3GPROFF08SSMI_DAY_CLIM_07",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3GPROFF08SSMI_DAY_CLIM_07",
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
@@ -1500413,196 +1500389,222 @@
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
+            "graphic-preview-description": "GPM SSMI on F08 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree (GPM_3GPROFF08SSMI_DAY_CLIM)",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFF08SSMI_DAY_CLIM_07.png",
+            "identifier": "C2264135026-GES_DISC",
+            "issued": "2022-05-09",
+            "keyword": [
+                "atmospheric water vapor",
+                "earth science",
+                "atmosphere",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/SSMI/F08/GPROFCLIM/3A-DAY/07",
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
+            "series-name": "GPM_3GPROFF08SSMI_DAY_CLIM",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1987-07-09T00:00:00Z/1991-12-31T23:59:59.999Z",
             "theme": [
                 "GPM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM SSMI on F08 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFF08SSMI_DAY_CLIM) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/447",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hodges, G.B., and E.A. Smith. 1999. BOREAS RSS-14 Level-3 Gridded Radiometer and Satellite Surface Radiation Images. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/447",
-            "issued": "2023-11-22",
-            "temporal": "1994-05-16T00:00:00Z/1994-09-20T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-11",
-            "keyword": [
-                "surface radiative properties",
-                "land surface",
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
-            "identifier": "C2929125100-ORNL_CLOUD",
             "description": "The BOREAS RSS-14 team collected and processed GOES-7 and -8 images of the BOREAS region as part of their effort to characterize the incoming, reflected and emitted radiation at regional scales. This data set contains surface radiation parameters, such as net radiation and net solar radiation, that have been interpolated from GOES-7 images and AMS data onto the standard BOREAS mapping grid at a resolution of 5 km N-S and E-W.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS RSS-14 Level-3 Gridded Radiometer and Satellite Surface Radiation Images",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F447",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F447",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/RSS/rss14srb/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/RSS/rss14srb/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/RSS14_L3_Gridded_SRB.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/RSS14_L3_Gridded_SRB.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/447",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/447",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rss14srb/comp/README",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rss14srb/comp/README",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rss14srb/comp/RSS14_L3_Gridded_SRB.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rss14srb/comp/RSS14_L3_Gridded_SRB.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rss14srb/comp/RSS14_L3_Gridded_SRB.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rss14srb/comp/RSS14_L3_Gridded_SRB.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rss14srb/comp/RSS14_L3_Gridded_SRB.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rss14srb/comp/RSS14_L3_Gridded_SRB.txt",
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
+            "identifier": "C2929125100-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "surface radiative properties",
+                "land surface",
+                "earth science",
+                "atmospheric radiation",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/447",
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
             "spatial": "-108.14 53.15 -95.48 56.58",
+            "temporal": "1994-05-16T00:00:00Z/1994-09-20T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS RSS-14 Level-3 Gridded Radiometer and Satellite Surface Radiation Images"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amess_ns_raw&version=1.0",
-            "bureauCode": [
-                "026:00"
-            ],
-            "issued": "2021-05-21",
             "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The MESSENGER NS uncalibrated observations consist of science and instrument data collected by the Neutron Spectrometer sensor.",
+            "identifier": "urn:nasa:pds:mess_ns_raw",
+            "issued": "2021-05-21",
             "keyword": [
                 "messenger",
                 "earth",
                 "venus",
                 "mercury"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amess_ns_raw&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:mess_ns_raw",
-            "description": "The MESSENGER NS uncalibrated observations consist of science and instrument data collected by the Neutron Spectrometer sensor.",
-            "title": "MESSENGER NS Raw (EDR) Data Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MESSENGER NS Raw (EDR) Data Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-PLS-2-EDR-RAW-TELEM-PACKETS-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains instrument packet files (IPFs) from the Plasma Science experiment (PLS) onboard the Galileo spacecraft during the Jupiter orbital operations phase. This data set is a very raw, binary form. It is archived for completeness only. There is another PDS data set (GO-J-PLS-3-RDR-FULLRES-V1.0) that contains all of the plasma detector counts in a form that is much easier to work with. The primary advantage of this data set is that it contains instrument housekeeping and engineering data in addition to the counts.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-pls-2-edr-raw-telem-packets-v1.0_v4ds-j693",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "europa",
                 "amalthea",
@@ -1500612,467 +1500614,467 @@
                 "galileo",
                 "callisto"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-PLS-2-EDR-RAW-TELEM-PACKETS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-pls-2-edr-raw-telem-packets-v1.0_v4ds-j693",
-            "description": "This data set contains instrument packet files (IPFs) from the Plasma Science experiment (PLS) onboard the Galileo spacecraft during the Jupiter orbital operations phase. This data set is a very raw, binary form. It is archived for completeness only. There is another PDS data set (GO-J-PLS-3-RDR-FULLRES-V1.0) that contains all of the plasma detector counts in a form that is much easier to work with. The primary advantage of this data set is that it contains instrument housekeeping and engineering data in addition to the counts.",
-            "title": "GALILEO JUPITER PLASMA RAW PACKETIZED TELEMETRY V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GALILEO JUPITER PLASMA RAW PACKETIZED TELEMETRY V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-SPICE-6-V1.0",
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
+            "description": "This data set includes the MSL SPICE data files (``kernel files''), which can be accessed using SPICE software. The SPICE data contain geometric and other ancillary information needed to recover the full value of science instrument data. In particular SPICE kernels provide rover and planetary ephemerides, instrument mounting alignments, rover orientation, and data needed for relevant time conversions.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-spice-6-v1.0_v4h2-s6n6",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars science laboratory"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-SPICE-6-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-spice-6-v1.0_v4h2-s6n6",
-            "description": "This data set includes the MSL SPICE data files (``kernel files''), which can be accessed using SPICE software. The SPICE data contain geometric and other ancillary information needed to recover the full value of science instrument data. In particular SPICE kernels provide rover and planetary ephemerides, instrument mounting alignments, rover orientation, and data needed for relevant time conversions.",
-            "title": "MSL SPICE KERNELS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MSL SPICE KERNELS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-PRL-MTP005-V2.0",
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
+            "description": "This data set contains\nEDITED data from Rosetta RPC-LAP, acquired during the PRELANDING\nMTP005 mission phase. Comet C-G/67p was the primary target.\nThis data set supersedes RO-C-RPCLAP-2-PRL-EDITED-V1.0 and is only\nthe MTP005 part of it.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-prl-mtp005-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-PRL-MTP005-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-prl-mtp005-v2.0",
-            "description": "This data set contains\nEDITED data from Rosetta RPC-LAP, acquired during the PRELANDING\nMTP005 mission phase. Comet C-G/67p was the primary target.\nThis data set supersedes RO-C-RPCLAP-2-PRL-EDITED-V1.0 and is only\nthe MTP005 part of it.",
-            "title": "ROSETTA-ORBITER 67P RPCLAP 2\nPRL MTP005 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCLAP 2\nPRL MTP005 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-A-NIMS-4-GASPRACUBE-V1.0",
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
-                "gaspra",
-                "galileo"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data volume contains a 17 channel spectral image cube of asteroid 951 Gaspra ranging from 0.7 to 5.2 micrometers in wavelength in cgs units of radiance. The spatial resolution of this data is 1.28 km/pixel. This data set was obtained by the Galileo spacecraft Near Infrared Mapping Spectrometer on October 29, 1991. It was radiometrically calibrated using calibration measurements obtained by the Near Infrared Mapping Spectrometer during its observations of Earth on December 9, 1990.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-a-nims-4-gaspracube-v1.0_v4jc-sqzj",
+            "issued": "2018-06-26",
+            "keyword": [
+                "gaspra",
+                "galileo"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-A-NIMS-4-GASPRACUBE-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-a-nims-4-gaspracube-v1.0_v4jc-sqzj",
-            "description": "This data volume contains a 17 channel spectral image cube of asteroid 951 Gaspra ranging from 0.7 to 5.2 micrometers in wavelength in cgs units of radiance. The spatial resolution of this data is 1.28 km/pixel. This data set was obtained by the Galileo spacecraft Near Infrared Mapping Spectrometer on October 29, 1991. It was radiometrically calibrated using calibration measurements obtained by the Near Infrared Mapping Spectrometer during its observations of Earth on December 9, 1990.",
-            "title": "HIRES NIMS GASPRA SPECTRAL IMAGE CUBE",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "HIRES NIMS GASPRA SPECTRAL IMAGE CUBE"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP22C2.001",
             "citation": "Xiaoyang Zhang, Mark Friedl, Geoffrey Henebry\r\n. 2020-07-08. VNP22C2. Version 001. VIIRS/NPP Land Cover Dynamics Yearly L3 Global 0.05 Deg CMG V001\r\n. Sioux Falls, SD, USA\r\n. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes DAAC\r\n. https://doi.org/10.5067/VIIRS/VNP22C2.001. https://doi.org/10.5067/VIIRS/VNP22C2.001. Digital Science Data. This data set was provided by the NASA/NOAA NPP Project. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
-            "issued": "2013-01-01",
-            "temporal": "2013-01-01T00:00:00Z/2023-10-23T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-12-31",
-            "keyword": [
-                "surface radiative properties",
-                "land surface",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:lpdaac@usgs.gov"
             },
+            "creator": "Xiaoyang Zhang, Mark Friedl, Geoffrey Henebry",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1712040022-LPDAAC_ECS",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
             "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Land Cover Dynamics data product provides global land surface phenology (GLSP) metrics at yearly intervals. The VNP22C2 data product is derived from time series of the two-band Enhanced Vegetation Index-2 (EVI2) calculated from VIIRS Nadir Bidirectional Reflectance Distribution Function (BRDF)-Adjusted Reflectance (NBAR). Vegetation phenology metrics at 0.05 degree (~5,600 meters) spatial resolution are identified for up to two detected growing cycles per year.\r\n \r\nProvided in each VNP22C2 product are 19 Science Dataset (SDS) layers. The product contains six phenological transition dates: onset of greenness increase, onset of greenness maximum, onset of greenness decrease, onset of greenness minimum, dates of mid-greenup, and senescence phases. The product also includes the growing season length. The greenness related metrics consist of EVI2 onset of greenness increase, EVI2 onset of greenness maximum, EVI2 growing season, rate of greenness increase and rate of greenness decrease. The confidence of phenology detection is provided as greenness agreement growing season, proportion of good quality (PGQ) growing season, PGQ onset greenness increase, PGQ onset greenness maximum, PGQ onset greenness decrease, and PGQ onset greenness minimum. The final layer is quality control specifying the overall quality of the product. A low-resolution browse image showing greenup is also available when viewing each VNP22C2 granule.",
-            "release-place": "Sioux Falls, SD, USA",
-            "series-name": "VNP22C2",
-            "creator": "Xiaoyang Zhang, Mark Friedl, Geoffrey Henebry",
-            "title": "VIIRS/NPP Land Cover Dynamics Yearly L3 Global 0.05 Deg CMG V001",
-            "graphic-preview-description": "Browse image for Earthdata Search",
-            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov//WORKING/BRWS/Browse.001/2020.05.22/BROWSE.VNP22C2.A2016001.001.2020134164310.1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP22C2.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP22C2.001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/NPP_QA/",
-                    "description": "Quality Assessment provides information regarding the usability and usefulness of the data product.",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Assessment provides information regarding the usability and usefulness of the data product.",
+                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/NPP_QA/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP22C2.001",
-                    "description": "Data set landing page at the LP DAAC",
                     "@type": "dcat:Distribution",
+                    "description": "Data set landing page at the LP DAAC",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP22C2.001",
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
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP22C2.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP22C2.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1712040022-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1712040022-LPDAAC_ECS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/637/VNP22_User_Guide_V1.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/637/VNP22_User_Guide_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/636/VNP22_ATBD.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/636/VNP22_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov//WORKING/BRWS/Browse.001/2020.05.22/BROWSE.VNP22C2.A2016001.001.2020134164310.1.jpg",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov//WORKING/BRWS/Browse.001/2020.05.22/BROWSE.VNP22C2.A2016001.001.2020134164310.1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://viirsland.gsfc.nasa.gov/Val/Pheno_Val.html",
-                    "description": "Validation at stage 1 has been achieved for the VIIRS land cover dynamic product suite.",
                     "@type": "dcat:Distribution",
+                    "description": "Validation at stage 1 has been achieved for the VIIRS land cover dynamic product suite.",
+                    "downloadURL": "https://viirsland.gsfc.nasa.gov/Val/Pheno_Val.html",
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
+            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov//WORKING/BRWS/Browse.001/2020.05.22/BROWSE.VNP22C2.A2016001.001.2020134164310.1.jpg",
+            "identifier": "C1712040022-LPDAAC_ECS",
+            "issued": "2013-01-01",
+            "keyword": [
+                "surface radiative properties",
+                "land surface",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP22C2.001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, SD, USA",
+            "series-name": "VNP22C2",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2013-01-01T00:00:00Z/2023-10-23T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP Land Cover Dynamics Yearly L3 Global 0.05 Deg CMG V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/R5LI5YA9X8LV",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMEX04 Landsat Thematic Mapper Imagery, Arizona, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/R5LI5YA9X8LV.",
-            "issued": "2004-06-11",
-            "temporal": "2004-06-11T00:00:00Z/2004-08-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2004-08-30",
-            "keyword": [
-                "spectral/engineering",
-                "infrared wavelengths",
-                "earth science",
-                "visible wavelengths"
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
-            "identifier": "C1386204372-NSIDCV0",
             "description": "This data set provides imagery developed from Landsat 5 Thematic Mapper (TM) data for use in studying land cover features during the Soil Moisture Experiment 2004 (SMEX04).",
-            "title": "SMEX04 Landsat Thematic Mapper Imagery, Arizona, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FR5LI5YA9X8LV",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FR5LI5YA9X8LV",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX04/Arizona/satellite/TM_GEOTIFF/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX04/Arizona/satellite/TM_GEOTIFF/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX04/Arizona/satellite/TM_GEOTIFF/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX04/Arizona/satellite/TM_GEOTIFF/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/R5LI5YA9X8LV",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/R5LI5YA9X8LV",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/R5LI5YA9X8LV",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/R5LI5YA9X8LV",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386204372-NSIDCV0",
+            "issued": "2004-06-11",
+            "keyword": [
+                "spectral/engineering",
+                "infrared wavelengths",
+                "earth science",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/R5LI5YA9X8LV",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2004-08-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-111.4 29.33 -108.56 32.69",
+            "temporal": "2004-06-11T00:00:00Z/2004-08-30T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMEX04 Landsat Thematic Mapper Imagery, Arizona, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VJ143MA3.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang, Angela Erb, Ian Paynter\r\n. 2024-10-31. VIIRS/JPSS1 BRDF/Albedo Albedo Daily L3 Global 1km SIN Grid V002. Version 002. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VJ143MA3.002. https://doi.org/10.5067/VIIRS/VJ143MA3.002. This data set was provided by the NASA/NOAA NPP Project. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
-            "issued": "2024-10-31",
-            "temporal": "2018-01-01T00:00:00Z/2024-11-04T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-31",
-            "keyword": [
-                "earth science",
-                "surface radiative properties",
-                "land surface"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Zhuosen Wang",
                 "hasEmail": "mailto:zhuosen.wang@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
-            "identifier": "C2545310938-LPCLOUD",
-            "description": "The NOAA-20 Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo (VJ143MA3) Version 2 product provides albedo values at 1 kilometer (km) resolution for the bihemispherical reflectance white-sky albedo (WSA) and directional hemispherical reflectance black-sky albedo (BSA) at local solar noon. The VJ143MA3 product is produced daily using 16 days of VIIRS data and is weighted temporally to the ninth day, which is reflected in the file name. The VJ143 data products are designed to promote the continuity of NASA\u2019s Moderate Resolution Imaging Spectroradiometer (MODIS) BRDF/Albedo data product suite. \r\n\r\nThe VJ143 algorithm uses the RossThick/Li-Sparse-Reciprocal (RTLSR) semi-empirical kernel-driven BRDF model, with the three kernel weights from (VJ143MA1) to reconstruct surface anisotropic effects, correcting the directional reflectance to a common view geometry (VJ143MA4), while also computing integrated black-sky albedo (BSA) at local solar noon and white-sky albedo (WSA) (VJ143MA3). Researchers can use the BRDF model parameters with a simple polynomial, to obtain black-sky albedo at any solar illumination angle. Likewise, both the BSA and WSA Science Dataset (SDS) layers can be used with a simple polynomial, to manually estimate instantaneous actual albedo (blue-sky albedo). Additional details regarding the methodology are available in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nThe VJ143MA3 product provides a total of 36 SDS layers including: BSA; WSA; and mandatory quality layers for nine VIIRS moderate bands M1-M5, M7-M8, and M10-M11; as well as near-infrared (NIR); shortwave; and visible broadbands. A low-resolution image is also available showing retrievals of WSA for band M1 in JPEG format.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "Crystal Schaaf, Zhuosen Wang, Angela Erb, Ian Paynter",
-            "title": "VIIRS/JPSS1 BRDF/Albedo Albedo Daily L3 Global 1km SIN Grid V002",
-            "graphic-preview-file": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/VJ143MA3.002/VJ143MA3.A2024294.h19v11.002.2024302064612/BROWSE.VJ143MA3.A2024294.h19v11.002.2024302064612.1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The NOAA-20 Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo (VJ143MA3) Version 2 product provides albedo values at 1 kilometer (km) resolution for the bihemispherical reflectance white-sky albedo (WSA) and directional hemispherical reflectance black-sky albedo (BSA) at local solar noon. The VJ143MA3 product is produced daily using 16 days of VIIRS data and is weighted temporally to the ninth day, which is reflected in the file name. The VJ143 data products are designed to promote the continuity of NASA\u2019s Moderate Resolution Imaging Spectroradiometer (MODIS) BRDF/Albedo data product suite. \r\n\r\nThe VJ143 algorithm uses the RossThick/Li-Sparse-Reciprocal (RTLSR) semi-empirical kernel-driven BRDF model, with the three kernel weights from (VJ143MA1) to reconstruct surface anisotropic effects, correcting the directional reflectance to a common view geometry (VJ143MA4), while also computing integrated black-sky albedo (BSA) at local solar noon and white-sky albedo (WSA) (VJ143MA3). Researchers can use the BRDF model parameters with a simple polynomial, to obtain black-sky albedo at any solar illumination angle. Likewise, both the BSA and WSA Science Dataset (SDS) layers can be used with a simple polynomial, to manually estimate instantaneous actual albedo (blue-sky albedo). Additional details regarding the methodology are available in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nThe VJ143MA3 product provides a total of 36 SDS layers including: BSA; WSA; and mandatory quality layers for nine VIIRS moderate bands M1-M5, M7-M8, and M10-M11; as well as near-infrared (NIR); shortwave; and visible broadbands. A low-resolution image is also available showing retrievals of WSA for band M1 in JPEG format.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ143MA3.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ143MA3.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf5",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2545310938-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2545310938-LPCLOUD",
+                    "mediaType": "application/x-hdf5",
                     "title": "Download this dataset through Earthdata Search"
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
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VJ143MA3.002",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VJ143MA3.002",
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
-                    "downloadURL": "https://www.umb.edu/spectralmass/viirs-user-guides-c1-and-c2/vnp43ia3-and-vnp43ma3-albedo-products/",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://www.umb.edu/spectralmass/viirs-user-guides-c1-and-c2/vnp43ia3-and-vnp43ma3-albedo-products/",
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
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/VJ143MA3.002/VJ143MA3.A2024294.h19v11.002.2024302064612/BROWSE.VJ143MA3.A2024294.h19v11.002.2024302064612.1.jpg",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/VJ143MA3.002/VJ143MA3.A2024294.h19v11.002.2024302064612/BROWSE.VJ143MA3.A2024294.h19v11.002.2024302064612.1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://viirsland.gsfc.nasa.gov/Val/Albedo_Val.html",
-                    "description": "Validation at stage 3 has been achieved for the VIIRS BRDF/Albedo product suite.",
                     "@type": "dcat:Distribution",
+                    "description": "Validation at stage 3 has been achieved for the VIIRS BRDF/Albedo product suite.",
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
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/VJ143MA3.002/VJ143MA3.A2024294.h19v11.002.2024302064612/BROWSE.VJ143MA3.A2024294.h19v11.002.2024302064612.1.jpg",
+            "identifier": "C2545310938-LPCLOUD",
+            "issued": "2024-10-31",
+            "keyword": [
+                "earth science",
+                "surface radiative properties",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VJ143MA3.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-10-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-01-01T00:00:00Z/2024-11-04T00:00:00Z",
             "theme": [
                 "JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/JPSS1 BRDF/Albedo Albedo Daily L3 Global 1km SIN Grid V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-LEISA-3-JUPITER-V1.1",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Calibrated data taken by the New Horizons Linear Etalon Imaging Spectral Array instrument during the Jupiter encounter mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-leisa-3-jupiter-v1.1_v4ww-sf6q",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "new horizons",
                 "jupiter",
@@ -1501083,213 +1501085,225 @@
                 "callisto",
                 "ganymede"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-LEISA-3-JUPITER-V1.1",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-leisa-3-jupiter-v1.1_v4ww-sf6q",
-            "description": "This data set contains Calibrated data taken by the New Horizons Linear Etalon Imaging Spectral Array instrument during the Jupiter encounter mission phase.",
-            "title": "NEW HORIZONS LEISA JUPITER ENCOUNTER V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS LEISA JUPITER ENCOUNTER V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/262",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hardy, J.P., and R.E. Davis. 1998. BOREAS HYD-03 Snow Water Equivalent Data. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/262",
-            "issued": "2023-11-22",
-            "temporal": "1994-02-05T00:00:00Z/1994-04-27T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-27",
-            "keyword": [
-                "earth science",
-                "snow/ice",
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
-            "identifier": "C2807625013-ORNL_CLOUD",
             "description": "Contains the snow water equivalent that was calculated from measurements of snow pack density and snow depth.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS HYD-03 Snow Water Equivalent Data",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F262",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F262",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/HYD/h03swed/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/HYD/h03swed/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/HYD03_Snow_Meas.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/HYD03_Snow_Meas.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/262",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/262",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h03swed/comp/h03swed.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h03swed/comp/h03swed.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h03swed/comp/HYD03_Snow_Meas.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h03swed/comp/HYD03_Snow_Meas.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h03swed/comp/HYD03_Snow_Meas.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h03swed/comp/HYD03_Snow_Meas.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h03swed/comp/HYD03_Snow_Meas.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h03swed/comp/HYD03_Snow_Meas.txt",
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
+            "identifier": "C2807625013-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "earth science",
+                "snow/ice",
+                "terrestrial hydrosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/262",
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
             "spatial": "-106.2 53.56 -97.82 55.93",
+            "temporal": "1994-02-05T00:00:00Z/1994-04-27T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS HYD-03 Snow Water Equivalent Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206762-NSIDCV0.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Upper soil temperatures in the Kolyma Highland, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center.",
-            "issued": "1977-10-01",
-            "temporal": "1977-10-01T00:00:00Z/1995-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1995-12-31",
-            "keyword": [
-                "atmosphere",
-                "atmospheric temperature",
-                "biosphere",
-                "cryosphere",
-                "earth science",
-                "frozen ground",
-                "terrestrial hydrosphere",
-                "soils",
-                "snow/ice",
-                "land surface",
-                "precipitation",
-                "vegetation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "G.G. Mazhitova",
                 "hasEmail": "mailto:biol@omkomi.intec.ru"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NSIDC"
-            },
-            "identifier": "C1386206762-NSIDCV0",
             "description": "This data set contains soil temperature and meteorological data for various sampling locations near the Aborigen research station in the Kolyma Highland, Northeastern Russia. Data are averaged from 1977 to 1995. A tab-delimited ASCII text file and Excel spreadsheet provide the following data: soil degree days, annual maximum temperature, and annual minimum temperature at 1 cm, 5 cm, 10 cm, and 20 cm depth; maximum annual snow depth, vegetation type and percent coverage, thaw depth, mean soil water content, soil classification, soil field capacity, soil bulk density, slope gradient/aspect, elevation, latitude, and longitude. Data are available via FTP.",
-            "title": "Upper soil temperatures in the Kolyma Highland, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/GGD31_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/GGD31_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD31/versions/1",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://nsidc.org/data/GGD31/versions/1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD31/versions/1",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://nsidc.org/data/GGD31/versions/1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386206762-NSIDCV0",
+            "issued": "1977-10-01",
+            "keyword": [
+                "atmosphere",
+                "atmospheric temperature",
+                "biosphere",
+                "cryosphere",
+                "earth science",
+                "frozen ground",
+                "terrestrial hydrosphere",
+                "soils",
+                "snow/ice",
+                "land surface",
+                "precipitation",
+                "vegetation"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206762-NSIDCV0.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1995-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "149.5 61.867 149.667 62.033",
+            "temporal": "1977-10-01T00:00:00Z/1995-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Upper soil temperatures in the Kolyma Highland, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/v554-yj97",
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
+            "identifier": "nasa_genelab_GLDS-98_v554-yj97",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "dna sequencing library construction",
                 "mass spectrometry",
@@ -1501308,361 +1501322,325 @@
                 "library construction",
                 "animal and tissue sampling"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/v554-yj97",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-98_v554-yj97",
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
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
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
-            "landingPage": "https://doi.org/10.5067/NOAA-20/VIIRS/L3M/PAR/2022",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/NOAA-20/VIIRS/L3M/PAR/2022.",
-            "issued": "2022-09-14",
-            "temporal": "2017-11-29T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-14",
-            "keyword": [
-                "oceans",
-                "earth science",
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
-            "identifier": "C2340494601-OB_DAAC",
             "description": "The Visible and Infrared Imager/Radiometer Suite (VIIRS) is a multi-disciplinary instrument that is being flown on the Joint Polar Satellite System (JPSS) series of spacecraft, including the Suomi National Polar-orbiting Partnership (S-NPP) that launched in October 2011.  JPSS is a multi-platform, multi-agency program that consolidates the polar orbiting spacecraft of NASA and the National Oceanic and Atmospheric Administration (NOAA).  S-NPP is the initial spacecraft in this series, and VIIRS is the successor to MODIS for Earth science data product generation.  VIIRS has 22 spectral bands ranging from 412 nm to 12 nm.  There are 16 moderate-resolution bands (750m at nadir), 5 image-resolution bands (375m), and one day-night band (DNB).",
-            "title": "NOAA-20 VIIRS Global Mapped Photosynthetically Active Radiation (PAR) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNOAA-20%2FVIIRS%2FL3M%2FPAR%2F2022",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNOAA-20%2FVIIRS%2FL3M%2FPAR%2F2022",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NOAA-20/VIIRS/L3M/PAR/2022",
-                    "description": "VIIRS-NOAA-20 L3M Photosynthetically Active Radiation (PAR) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS-NOAA-20 L3M Photosynthetically Active Radiation (PAR) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NOAA-20/VIIRS/L3M/PAR/2022",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
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
+            "identifier": "C2340494601-OB_DAAC",
+            "issued": "2022-09-14",
+            "keyword": [
+                "oceans",
+                "earth science",
+                "ocean optics"
+            ],
+            "landingPage": "https://doi.org/10.5067/NOAA-20/VIIRS/L3M/PAR/2022",
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
+            "temporal": "2017-11-29T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NOAA-20 VIIRS Global Mapped Photosynthetically Active Radiation (PAR) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3330-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-06-29T04:58:58.000 to 2012-06-29T06:24:05.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3330-v1.0_v572-38cj",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars express"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3330-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3330-v1.0_v572-38cj",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-06-29T04:58:58.000 to 2012-06-29T06:24:05.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3330 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3330 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2347",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Iraci, L., J.M. St.Clair, and T.P. Bui. 2024. COMEX: Flight Information for AJAX Airborne In Situ CO2 and CH4, 2014-2015, USA. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2347",
-            "issued": "2024-06-14",
-            "temporal": "2014-05-19T20:15:00Z/2015-08-19T22:07:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-17",
-            "keyword": [
-                "earth science",
-                "platform characteristics",
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
-            "identifier": "C3104478810-ORNL_CLOUD",
             "description": "This dataset provides information to access NASA Earthdata published flight data and flight information collected by the Alpha Jet Atmospheric eXperiment (AJAX) and associated with the COMEX project in 2014-2015. The file lists information for COMEX-related datasets that has been subsetted from AJAX collections archived through NASA's Atmospheric Science Data Center.  AJAX data are not otherwise replicated in this dataset. AJAX is a partnership between NASA's Ames Research Center and H211, L.L.C., which conducted in-situ measurements over California, Nevada, and the coastal Pacific in support of satellite validation. During COMEX data collection, a Picarro greenhouse gas (GHG) sensor was mounted on an Alpha Jet, a tactical strike fighter developed by Dassault-Breguet and Dornier through a German-French NATO collaboration. The GHG sensor made repeat measurements in California and Nevada. In situ data included measurements of CO2, CH4, and H2O at 2 Hz or CH4 and H2O at 10 Hz with a strategy of characterizing atmospheric structure over ocean and land, and vertical profiles to at least 5000 m.  Ancillary data, including O3, formaldehyde, and meteorological profiles, were also collected. This dataset provides filenames, spatiotemporal bounds, and download URLs for accessing these in situ data. This information is provided in comma separated values (CSV) format.",
-            "graphic-preview-description": "Methane concentrations from the Alpha Jet over Kern River oil field and environs in California on 10 June 2014. Source: Krautwurst et al. (2016).",
-            "title": "COMEX: Flight Information for AJAX Airborne In Situ CO2 and CH4, 2014-2015, USA",
-            "graphic-preview-file": "https://daac.ornl.gov/COMEX/guides/COMEX_AJAX_CO2_CH4_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2347",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2347",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/comex/COMEX_AJAX_CO2_CH4/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/comex/COMEX_AJAX_CO2_CH4/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/COMEX/guides/COMEX_AJAX_CO2_CH4.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/COMEX/guides/COMEX_AJAX_CO2_CH4.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2347",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2347",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/comex/COMEX_AJAX_CO2_CH4/comp/COMEX_AJAX_CO2_CH4.pdf",
-                    "description": "COMEX: Flight Information for AJAX Airborne In Situ CO2 and CH4, 2014-2015, USA: COMEX_AJAX_CO2_CH4.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "COMEX: Flight Information for AJAX Airborne In Situ CO2 and CH4, 2014-2015, USA: COMEX_AJAX_CO2_CH4.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/comex/COMEX_AJAX_CO2_CH4/comp/COMEX_AJAX_CO2_CH4.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/COMEX/guides/COMEX_AJAX_CO2_CH4_Fig1.jpg",
-                    "description": "Methane concentrations from the Alpha Jet over Kern River oil field and environs in California on 10 June 2014. Source: Krautwurst et al. (2016).",
                     "@type": "dcat:Distribution",
+                    "description": "Methane concentrations from the Alpha Jet over Kern River oil field and environs in California on 10 June 2014. Source: Krautwurst et al. (2016).",
+                    "downloadURL": "https://daac.ornl.gov/COMEX/guides/COMEX_AJAX_CO2_CH4_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5270/esa-k85rkdq",
-                    "description": "ESA COMEX Campaign Page",
                     "@type": "dcat:Distribution",
+                    "description": "ESA COMEX Campaign Page",
+                    "downloadURL": "https://doi.org/10.5270/esa-k85rkdq",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "graphic-preview-description": "Methane concentrations from the Alpha Jet over Kern River oil field and environs in California on 10 June 2014. Source: Krautwurst et al. (2016).",
+            "graphic-preview-file": "https://daac.ornl.gov/COMEX/guides/COMEX_AJAX_CO2_CH4_Fig1.jpg",
+            "identifier": "C3104478810-ORNL_CLOUD",
+            "issued": "2024-06-14",
+            "keyword": [
+                "earth science",
+                "platform characteristics",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2347",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-06-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-122.06 34.13 -116.26 38.89",
+            "temporal": "2014-05-19T20:15:00Z/2015-08-19T22:07:59Z",
             "theme": [
                 "COMEX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "COMEX: Flight Information for AJAX Airborne In Situ CO2 and CH4, 2014-2015, USA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQUA/MODIS/L3B/PIC/2022",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/AQUA/MODIS/L3B/PIC/2022.",
-            "issued": "2019-06-23",
-            "temporal": "2002-07-04T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-10-01",
-            "keyword": [
-                "national geospatial data asset",
-                "ocean chemistry",
-                "earth science",
-                "oceans",
-                "ngda"
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
-            "identifier": "C2330511790-OB_DAAC",
             "description": "MODIS (or Moderate-Resolution Imaging Spectroradiometer) is a key instrument aboard the Terra (EOS AM) and Aqua (EOS PM) satellites. Terra's orbit around the Earth is timed so that it passes from north to south across the equator in the morning, while Aqua passes south to north over the equator in the afternoon. Terra MODIS and Aqua MODIS are viewing the entire Earth's surface every 1 to 2 days, acquiring data in 36 spectral bands, or groups of wavelengths (see MODIS Technical Specifications). These data will improve our understanding of global dynamics and processes occurring on the land, in the oceans, and in the lower atmosphere. MODIS is playing a vital role in the development of validated, global, interactive Earth system models able to predict global change accurately enough to assist policy makers in making sound decisions concerning the protection of our environment.",
-            "title": "Aqua MODIS Global Binned Particulate Inorganic Carbon (PIC) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQUA%2FMODIS%2FL3B%2FPIC%2F2022",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQUA%2FMODIS%2FL3B%2FPIC%2F2022",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/AQUA/MODIS/L3B/PIC/2022",
-                    "description": "MODIS-Aqua L3B Particulate Inorganic Carbon (PIC) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS-Aqua L3B Particulate Inorganic Carbon (PIC) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/AQUA/MODIS/L3B/PIC/2022",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2330511790-OB_DAAC",
+            "issued": "2019-06-23",
+            "keyword": [
+                "national geospatial data asset",
+                "ocean chemistry",
+                "earth science",
+                "oceans",
+                "ngda"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQUA/MODIS/L3B/PIC/2022",
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
+            "title": "Aqua MODIS Global Binned Particulate Inorganic Carbon (PIC) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://nasa3d.arc.nasa.gov/detail/gemini-suit",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://www.nasa.gov/mission_pages/gemini/index.html"
-            ],
-            "keyword": [
-                "spacecraft",
-                "spacesuit",
-                "3d model",
-                "gemini"
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
-            "identifier": "NASA-351__1",
             "description": "The Gemini spacesuit had a combination of a pressure bladder and a link-net restraint layer that made the whole suit flexible when pressurized. Polygons: 57594 Vertices: 57638",
-            "title": "NASA 3D Models: Gemini Spacesuit",
-            "programCode": [
-                "026:045",
-                "026:046"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1501670,146 +1501648,151 @@
                     "mediaType": "application/octet-stream"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-351__1",
+            "issued": "2018-06-25",
+            "keyword": [
+                "spacecraft",
+                "spacesuit",
+                "3d model",
+                "gemini"
+            ],
+            "landingPage": "http://nasa3d.arc.nasa.gov/detail/gemini-suit",
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
+                "http://www.nasa.gov/mission_pages/gemini/index.html"
+            ],
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "NASA 3D Models: Gemini Spacesuit"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1328028152-LARC_ASDC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1999-09-29. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC.",
-            "issued": "1999-09-28",
-            "temporal": "1979-05-01T00:00:00Z/1980-05-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-08-06",
-            "keyword": [
-                "earth science",
-                "clouds",
-                "atmospheric radiation",
-                "atmosphere"
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
-            "identifier": "C1328028152-LARC_ASDC",
             "description": "NIMBUS7_NFOV_MLCE data are Nimbus 7 Narrow Field of View (NFOV) Maximum Likelihood Cloud Estimation (MLCE) Data in Native Format.The NIMBUS7_NFOV_MLCE data set uses the Nimbus-7 measurements and the MLCE algorithm for better regional and temporal resolution. The Earth Radiation Budget (ERB) parameters, derived from the Nimbus-7 scanner measurements, were rederived in 1990 using a Maximum Likelihood Cloud Estimation (MLCE) algorithm similar, but not identical, to the Earth Radiation Budget Experiment (ERBE) algorithm. Daily and monthly means are presented on two commensurate equal area world grids: (167 km by 167 km) and (500 km by 500 km). The MLCE procedure also yielded a rough estimate of the regional cloud cover.The scanner took measurements from November 16, 1978 through June 20, 1980; however, only 13 months (May 1979 through May 1980) of data sampling were reprocessed using the Sorting into Angular Bins and MLCE algorithms. There was poorer temporal sampling during the first five months of the experiment.The Nimbus 7 research-and-development satellite served as a stabilized, earth-oriented platform for the testing of advanced systems for sensing and collecting data in the pollution, oceanographic and meteorological disciplines. The polar-orbiting spacecraft consisted of three major structures: (1) a hollow torus-shaped sensor mount, (2) solar paddles, and (3) a control housing unit that was connected to the sensor mount by a tripod truss structure.",
-            "title": "Nimbus-7 Narrow Field of View (NFOV) Maximum Likelihood Cloud Estimation (MLCE) Data in Native Format",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/NIMBUS7",
-                    "description": "ASDC Data and Information for Nimbus-7 ERB",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for Nimbus-7 ERB",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/NIMBUS7",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1328028152-LARC_ASDC",
-                    "description": "Earthdata Search for NIMBUS7_NFOV_MLCE_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for NIMBUS7_NFOV_MLCE_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1328028152-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/nimbus7/guide/abstract_NIMBUS7_NFOV_MLCE.pdf",
-                    "description": "Temporary abstract provided as an interim guide for Nimbus-7 NFOV MLCE Data in Native Format",
                     "@type": "dcat:Distribution",
+                    "description": "Temporary abstract provided as an interim guide for Nimbus-7 NFOV MLCE Data in Native Format",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/nimbus7/guide/abstract_NIMBUS7_NFOV_MLCE.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/postscript",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/nimbus7/readme/readme_nimbus7_nfov_mlce.ps",
-                    "description": "Nimbus 7 NFOV MLCE Direct File Download (.pdf) Readme",
                     "@type": "dcat:Distribution",
+                    "description": "Nimbus 7 NFOV MLCE Direct File Download (.pdf) Readme",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/nimbus7/readme/readme_nimbus7_nfov_mlce.ps",
+                    "mediaType": "application/postscript",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/nimbus7/read_software/Makefile_nimbus7_nfov_mlce.txt",
-                    "description": "Read Software - nimbus7",
                     "@type": "dcat:Distribution",
+                    "description": "Read Software - nimbus7",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/nimbus7/read_software/Makefile_nimbus7_nfov_mlce.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/nimbus7/read_software/nimbus7_mlce.c",
-                    "description": "Readme to receive output files for Nimbus 7_MLCE Data - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "Readme to receive output files for Nimbus 7_MLCE Data - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/nimbus7/read_software/nimbus7_mlce.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/nimbus7/guide/nimbus7_project.pdf",
-                    "description": "Nimbus-7 Earth Radiation Budget (ERB) Langley DAAC Project/Campaign Document",
                     "@type": "dcat:Distribution",
+                    "description": "Nimbus-7 Earth Radiation Budget (ERB) Langley DAAC Project/Campaign Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/nimbus7/guide/nimbus7_project.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/NIMBUS-7/NFOV_MLCE/",
-                    "description": "ASDC Direct Data Download for NIMBUS7_NFOV_MLCE_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for NIMBUS7_NFOV_MLCE_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/NIMBUS-7/NFOV_MLCE/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/NIMBUS-7/NFOV_MLCE/contents.html",
-                    "description": "OPeNDAP data access for NIMBUS7_NFOV_MLCE_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for NIMBUS7_NFOV_MLCE_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/NIMBUS-7/NFOV_MLCE/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1328028152-LARC_ASDC",
+            "issued": "1999-09-28",
+            "keyword": [
+                "earth science",
+                "clouds",
+                "atmospheric radiation",
+                "atmosphere"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1328028152-LARC_ASDC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-08-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1979-05-01T00:00:00Z/1980-05-31T23:59:59.999Z",
             "theme": [
                 "NIMBUS-7",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Nimbus-7 Narrow Field of View (NFOV) Maximum Likelihood Cloud Estimation (MLCE) Data in Native Format"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2042454001-CDDIS.html",
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
-            "identifier": "C2042454001-CDDIS",
             "description": "Making Earth System Data Records for Use in Research Environments (MEaSUREs) empowers the research community to participate in developing and generating data products that complement and augment NASA produced and distributed Earth science data products. NASA\u2019s Enhanced Solid Earth Science Earth Science Data Record (ESDR) System (ESESES) continues and extends mature geodetic data product generation and archival as part of the MEaSUREs SESES project providing new, multi-decade, calibrated and validated geodetic-derived ESDRs obtained by the Scripps Institution of Oceanography (SIO) and NASA's Jet Propulsion Laboratory (JPL). These data-derived products include continuous multi-year high-rate GNSS, seismogeodetic, and meteorological time series, a catalog of transient deformation in tectonically active areas known for aseismic motion such as ETS with focus in Cascadia, and continuous estimation and cataloging of total near-surface water content derived from continuous GNSS time series over the continental U.S. These data products are high-rate seismogeodetic displacement and velocity records for historical earthquakes (M>6); broadband displacement and seismic velocity time series combining 1 Hz GPS displacements and 100 Hz accelerometer data for select large earthquakes and collocated CGPS and seismic instruments from regional networks.",
-            "title": "CDDIS SESES MEaSUREs products seismodetic for M>6 earthquakes",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1501818,111 +1501801,142 @@
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2042454001-CDDIS",
+            "issued": "2012-07-01",
+            "keyword": [
+                "nasa"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2042454001-CDDIS.html",
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
+            "title": "CDDIS SESES MEaSUREs products seismodetic for M>6 earthquakes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CPSA0M496MGB",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMAP L3 Radar Northern Hemisphere Daily 3 km EASE-Grid Freeze/Thaw State V003. Version 003. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/CPSA0M496MGB.",
-            "issued": "2015-04-13",
-            "temporal": "2015-04-13T00:00:00Z/2015-07-07T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-07-07",
-            "keyword": [
-                "spectral/engineering",
-                "cryosphere",
-                "earth science",
-                "radar",
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
-            "identifier": "C2872766057-NSIDC_CPRD",
             "description": "This Level-3 (L3) product provides a daily composite of Northern Hemisphere landscape freeze/thaw conditions retrieved by the Soil Moisture Active Passive (SMAP) radar from 6:00 a.m. descending and 6:00 p.m. ascending half-orbit passes. SMAP L-band backscatter data are used to derive freeze/thaw data, which are then resampled to an Earth-fixed, Northern Hemisphere azimuthal 3 km Equal-Area Scalable Earth Grid, Version 2.0 (EASE-Grid 2.0).",
-            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
-            "title": "SMAP L3 Radar Northern Hemisphere Daily 3 km EASE-Grid Freeze/Thaw State V003",
-            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?v=-4063232,-3477504,4063232,3477504&p=arctic&l=Coastlines_15m,SMAP_L3_Active_Day_Freeze_Thaw,MODIS_Terra_CorrectedReflectance_TrueColor&t=2015-04-14",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCPSA0M496MGB",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCPSA0M496MGB",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SPL3FTA+V003",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SPL3FTA+V003",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2872766057-NSIDC_CPRD",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2872766057-NSIDC_CPRD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://worldview.earthdata.nasa.gov/?v=-4063232%2C-3477504%2C4063232%2C3477504&p=arctic&l=Coastlines_15m%2CSMAP_L3_Active_Day_Freeze_Thaw%2CMODIS_Terra_CorrectedReflectance_TrueColor&t=2015-04-14",
-                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
                     "@type": "dcat:Distribution",
+                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+                    "downloadURL": "https://worldview.earthdata.nasa.gov/?v=-4063232%2C-3477504%2C4063232%2C3477504&p=arctic&l=Coastlines_15m%2CSMAP_L3_Active_Day_Freeze_Thaw%2CMODIS_Terra_CorrectedReflectance_TrueColor&t=2015-04-14",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through WORLDVIEW"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/CPSA0M496MGB",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/CPSA0M496MGB",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/CPSA0M496MGB",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/CPSA0M496MGB",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?v=-4063232,-3477504,4063232,3477504&p=arctic&l=Coastlines_15m,SMAP_L3_Active_Day_Freeze_Thaw,MODIS_Terra_CorrectedReflectance_TrueColor&t=2015-04-14",
+            "identifier": "C2872766057-NSIDC_CPRD",
+            "issued": "2015-04-13",
+            "keyword": [
+                "spectral/engineering",
+                "cryosphere",
+                "earth science",
+                "radar",
+                "snow/ice"
+            ],
+            "landingPage": "https://doi.org/10.5067/CPSA0M496MGB",
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
             "spatial": "-180.0 45.0 180.0 85.044",
+            "temporal": "2015-04-13T00:00:00Z/2015-07-07T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMAP L3 Radar Northern Hemisphere Daily 3 km EASE-Grid Freeze/Thaw State V003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/v5nq-hfkp",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Microgravity or an altered gravity environment from the static 1g has been shown to influence global gene expression patterns and protein levels in cultured cells or animals but it is unclear how these changes in gene and protein expressions are related to each other or are related to other factors regulating such changes. Recent advancement in the field of molecular biology revealed that a different class of RNA the small non-coding microRNA (miRNA) can have a broad effect on gene expression networks by mainly inhibiting the translational process. In this experiment conducted on the International Space Station we propose to test the hypotheses that miRNA profiles will be altered in the space environment and that cellular responses to DNA damage in space are different from those on the ground.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-118",
+                    "mediaType": "text/html",
+                    "title": "Transient gene expression profile changes of confluent human fibroblast cells in spaceflight"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-118_v5nq-hfkp",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "labeling",
                 "time",
@@ -1501942,85 +1501956,73 @@
                 "data transformation",
                 "data collection"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/v5nq-hfkp",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-118_v5nq-hfkp",
-            "description": "Microgravity or an altered gravity environment from the static 1g has been shown to influence global gene expression patterns and protein levels in cultured cells or animals but it is unclear how these changes in gene and protein expressions are related to each other or are related to other factors regulating such changes. Recent advancement in the field of molecular biology revealed that a different class of RNA the small non-coding microRNA (miRNA) can have a broad effect on gene expression networks by mainly inhibiting the translational process. In this experiment conducted on the International Space Station we propose to test the hypotheses that miRNA profiles will be altered in the space environment and that cellular responses to DNA damage in space are different from those on the ground.",
-            "title": "Transient gene expression profile changes of confluent human fibroblast cells in spaceflight",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-118",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Transient gene expression profile changes of confluent human fibroblast cells in spaceflight"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Transient gene expression profile changes of confluent human fibroblast cells in spaceflight"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMIP-3-ESC4-V2.0",
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
+            "description": "This archive contains data from the RPC-MIP instrument onboard ROSETTA Orbiter acquired during the COMET ESCORT 4 mission phase. The primary target was comet 67P/C-G. It also contains documentation which describes the RPC-MIP experiment. The data archived in this data set conform to the Planetary Data System Standards, Version 3.6. This is V2.0 updated after Science Review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmip-3-esc4-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMIP-3-ESC4-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmip-3-esc4-v2.0",
-            "description": "This archive contains data from the RPC-MIP instrument onboard ROSETTA Orbiter acquired during the COMET ESCORT 4 mission phase. The primary target was comet 67P/C-G. It also contains documentation which describes the RPC-MIP experiment. The data archived in this data set conform to the Planetary Data System Standards, Version 3.6. This is V2.0 updated after Science Review.",
-            "title": "ROSETTA-ORBITER 67P RPCMIP 3 ESC4 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCMIP 3 ESC4 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-UVIS-2-SSB-V1.3",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Photometric observations of stellar occultations by Saturnian rings, satellites, atmospheres, and Jovian atmosphere.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-uvis-2-ssb-v1.3_v5uk-nmn5",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "helene",
                 "epimetheus",
@@ -1502055,38 +1502057,45 @@
                 "tarqeq",
                 "tarvos"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-UVIS-2-SSB-V1.3",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-uvis-2-ssb-v1.3_v5uk-nmn5",
-            "description": "Photometric observations of stellar occultations by Saturnian rings, satellites, atmospheres, and Jovian atmosphere.",
-            "title": "CASSINI ORBITER SATURN UVIS SOLAR STELLAR BRIGHTNESS V1.3",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI ORBITER SATURN UVIS SOLAR STELLAR BRIGHTNESS V1.3"
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
+            "description": "CRAT, DLRE, LAMP, LEND, LOLA, LROC, MRFLRO",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20100615.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-572",
+            "issued": "2018-06-25",
             "keyword": [
                 "pds",
                 "lroc",
@@ -1502097,339 +1502106,339 @@
                 "crat",
                 "lamp"
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
-            "identifier": "NASA-572",
-            "description": "CRAT, DLRE, LAMP, LEND, LOLA, LROC, MRFLRO",
-            "title": "PDS Lunar Reconnaissance Orbiter Data 2",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20100615.shtml",
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
+            "title": "PDS Lunar Reconnaissance Orbiter Data 2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0437-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-11-16T14:32:20.000 to 2014-11-17T02:48:31.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0437-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0437-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0437-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-11-16T14:32:20.000 to 2014-11-17T02:48:31.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0437 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0437 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0878-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-07-05T21:57:05.000 to 2015-07-06T00:09:27.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0878-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0878-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0878-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-07-05T21:57:05.000 to 2015-07-06T00:09:27.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0878 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0878 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-E-MRI-3%2F4-EPOXI-EARTH-V2.0",
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
-                "epoxi"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains calibrated, 750-nm filter images of Earth acquired by the Deep Impact Medium Resolution Visible CCD (MRI) during the EPOCh and Cruise 2 phases of the EPOXI mission. The MRI instrument was only used during the first Earth observing period on 18-19 March 2008 and the last two on 27-28 March and 04-05 October 2009. Each observing period lasted approximately 24 hours, and one MRI image was taken simultaneously with the first north/south scan of the HRI IR spectrometer at half-hour intervals to serve as context spectra. On 27-28 September 2009 during the first attempt at Earth south polar observations, a full set of MRI context images was acquired although the HRII and HRIV instruments were turned off by fault protection shortly after the sequence started. Version 2.0 includes the application of a horizontal destriping process, new absolute calibration constants for filters, and revised electronic crosstalk calibration files.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-e-mri-3-4-epoxi-earth-v2.0_v5yt-sd99",
+            "issued": "2021-05-21",
+            "keyword": [
+                "earth",
+                "epoxi"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-E-MRI-3%2F4-EPOXI-EARTH-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-e-mri-3-4-epoxi-earth-v2.0_v5yt-sd99",
-            "description": "This dataset contains calibrated, 750-nm filter images of Earth acquired by the Deep Impact Medium Resolution Visible CCD (MRI) during the EPOCh and Cruise 2 phases of the EPOXI mission. The MRI instrument was only used during the first Earth observing period on 18-19 March 2008 and the last two on 27-28 March and 04-05 October 2009. Each observing period lasted approximately 24 hours, and one MRI image was taken simultaneously with the first north/south scan of the HRI IR spectrometer at half-hour intervals to serve as context spectra. On 27-28 September 2009 during the first attempt at Earth south polar observations, a full set of MRI context images was acquired although the HRII and HRIV instruments were turned off by fault protection shortly after the sequence started. Version 2.0 includes the application of a horizontal destriping process, new absolute calibration constants for filters, and revised electronic crosstalk calibration files.",
-            "title": "EPOXI EARTH OBS - MRI CALIBRATED IMAGES V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "EPOXI EARTH OBS - MRI CALIBRATED IMAGES V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0490-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-12-16T00:36:45.000 to 2014-12-16T12:31:06.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0490-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0490-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0490-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-12-16T00:36:45.000 to 2014-12-16T12:31:06.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0490 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0490 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ESO22M-SR-APPH-4-OCC-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.eso22m-sr-apph-4-occ-v1.0_v63h-u7f5",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "saturn occultation of 28 sagittarius 1989",
                 "saturn",
                 "s rings"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ESO22M-SR-APPH-4-OCC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.eso22m-sr-apph-4-occ-v1.0_v63h-u7f5",
-            "description": "not applicable",
-            "title": "ESO22M SR AP-PHOTOMETER RESAMPLED RING OCCULTATION V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ESO22M SR AP-PHOTOMETER RESAMPLED RING OCCULTATION V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/9",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MacPherson, J. I. 1994. Aircraft Flux - Raw: NRCC (FIFE). Data set. Available on -line [http://www.daac.ornl.gov] from Oak Ridge National Laboratory Distributed Active Archive Center, Oak Ridge, Tennessee, U.S.A. Also published in D. E. Strebel, D. R. Landis, K. F. Huemmrich, and B. W. Meeson (eds.), Collected Data of the First ISLSCP Field Experiment, Vol. 1: Surface Observations and Non-Image Data Sets. CD-ROM. National Aeronautics and Space Administration, Goddard Space Flight Center, Greenbelt, Maryland, U.S.A. (available from http://www.daac.ornl.gov. doi:10.3334/ORNLDAAC/9",
-            "issued": "2024-05-02",
-            "temporal": "1987-06-26T00:00:00Z/1989-10-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-03",
-            "keyword": [
-                "atmospheric temperature",
-                "atmospheric chemistry",
-                "vegetation",
-                "atmospheric radiation",
-                "atmosphere",
-                "atmospheric water vapor",
-                "earth science",
-                "atmospheric pressure",
-                "biosphere",
-                "atmospheric winds",
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
-            "identifier": "C2968531540-ORNL_CLOUD",
             "description": "Raw (unmodified) boundary layer fluxes recorded on aircraft flights over Konza",
-            "graphic-preview-description": "Browse Image",
-            "title": "Aircraft Flux-Raw: NRCC (FIFE)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/fife_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F9",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F9",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_AF_raw_nae/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_AF_raw_nae/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/air_flux_raw_nrcc.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/air_flux_raw_nrcc.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/9",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/9",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_AF_raw_nae/comp/aflux_mc.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_AF_raw_nae/comp/aflux_mc.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_AF_raw_nae/comp/af_raw.tdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_AF_raw_nae/comp/af_raw.tdf",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_AF_raw_nae/comp/air_flux_raw_nrcc.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_AF_raw_nae/comp/air_flux_raw_nrcc.pdf",
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
+            "identifier": "C2968531540-ORNL_CLOUD",
+            "issued": "2024-05-02",
+            "keyword": [
+                "atmospheric temperature",
+                "atmospheric chemistry",
+                "vegetation",
+                "atmospheric radiation",
+                "atmosphere",
+                "atmospheric water vapor",
+                "earth science",
+                "atmospheric pressure",
+                "biosphere",
+                "atmospheric winds",
+                "altitude"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/9",
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
             "spatial": "-102.0 37.0 -95.0 40.0",
+            "temporal": "1987-06-26T00:00:00Z/1989-10-31T23:59:59Z",
             "theme": [
                 "FIFE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aircraft Flux-Raw: NRCC (FIFE)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://appel.nasa.gov/knowledge-sharing/case-studies/appel-case-studies/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://km.nasa.gov/knowledge-map/"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Ed Hoffman",
+                "hasEmail": "mailto:ehoffman@nasa.gov"
+            },
+            "description": "Case studies illustrate the kinds of decisions and dilemmas managers face every day, and as such provide an effective learning tool for project management. Due to the dynamic and complex environment of projects, a great deal of project management knowledge is tacit and hard to formalize. A case study captures the complex nature of a project and identifies key decision points, allowing the reader an inside look at the project from a practitioner\u2019s point of view.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.nasa.gov/externalflash/irkm-aixll/",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-867",
+            "issued": "2018-06-25",
             "keyword": [
                 "appel",
                 "training",
@@ -1502439,140 +1502448,109 @@
                 "knowledge",
                 "case studies"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Ed Hoffman",
-                "hasEmail": "mailto:ehoffman@nasa.gov"
-            },
+            "landingPage": "http://appel.nasa.gov/knowledge-sharing/case-studies/appel-case-studies/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:045"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-867",
-            "description": "Case studies illustrate the kinds of decisions and dilemmas managers face every day, and as such provide an effective learning tool for project management. Due to the dynamic and complex environment of projects, a great deal of project management knowledge is tacit and hard to formalize. A case study captures the complex nature of a project and identifies key decision points, allowing the reader an inside look at the project from a practitioner\u2019s point of view.",
-            "title": "Academy of Program/Project & Engineering Leadership: Interactive Case Studies",
-            "programCode": [
-                "026:045"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.nasa.gov/externalflash/irkm-aixll/",
-                    "mediaType": "application/html"
-                }
+            "references": [
+                "http://km.nasa.gov/knowledge-map/"
             ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "Academy of Program/Project & Engineering Leadership: Interactive Case Studies"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-SWAP-3-LAUNCH-V2.0",
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
-                "solar wind",
-                "new horizons"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Calibrated data taken by the New Horizons Solar Wind Around Pluto instrument during the post-launch checkout mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-swap-3-launch-v2.0_v6b6-7qev",
+            "issued": "2018-06-26",
+            "keyword": [
+                "solar wind",
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-SWAP-3-LAUNCH-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-swap-3-launch-v2.0_v6b6-7qev",
-            "description": "This data set contains Calibrated data taken by the New Horizons Solar Wind Around Pluto instrument during the post-launch checkout mission phase.",
-            "title": "NEW HORIZONS SWAP POST-LAUNCH CHECKOUT V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS SWAP POST-LAUNCH CHECKOUT V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0729-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-24T21:15:55.000 to 2015-04-25T01:53:30.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0729-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0729-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0729-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-24T21:15:55.000 to 2015-04-25T01:53:30.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0729 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0729 V1.0"
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
-                "incompressible",
-                "flow",
-                "cases",
-                "turbulence",
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
-            "identifier": "NASA-842__16",
             "description": "This grouping contains the incompressible-flow cases from the 1980-81 Data Library.",
-            "title": "Collaborative Testing of Turbulence Models: Incompressible Flow Cases from 1980-81 Data Library",
-            "programCode": [
-                "026:023"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1502580,316 +1502558,315 @@
                     "mediaType": "application/txt"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-842__16",
+            "issued": "2018-06-25",
+            "keyword": [
+                "incompressible",
+                "flow",
+                "cases",
+                "turbulence",
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
-            "landingPage": "https://doi.org/10.5067/GPMGV/IFLOODS/GAUGES/DATA301",
             "bureauCode": [
                 "026:00"
             ],
             "citation": ".2017. GPM Ground Validation USGS Stream Flow IFloodS [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/IFLOODS/GAUGES/DATA301",
-            "issued": "2017-12-21",
-            "temporal": "2008-07-24T23:40:00Z/2013-07-01T11:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-09",
-            "keyword": [
-                "terrestrial hydrosphere",
-                "surface water",
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
-            "identifier": "C1979723016-GHRC_DAAC",
             "description": "The GPM Ground Validation USGS Stream Flow IFloodS dataset was obtained from USGS during the Iowa Flood Studies (IFloodS) field campaign that extended from March 30, 2013 through June 30, 2013. The main goal of IFloodS was to evaluate how well the GPM satellite rainfall data can be used for flood forecasting. The USGS monitors streamflow using gauges on streams and rivers throughout the U.S.  For the IFloodS field campaign, streamflow data from about 200 gauges in the Iowa IFloodS study area were downloaded from the USGS web site as support data for the campaign.  The USGS streamflow data were collected in real-time and provide measurements at 15-60 minute intervals. These USGS Stream Flow data are available in XML format.",
-            "title": "GPM Ground Validation USGS Stream Flow IFloodS V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FIFLOODS%2FGAUGES%2FDATA301",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FIFLOODS%2FGAUGES%2FDATA301",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmsgusgsifld",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmsgusgsifld",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://pubs.usgs.gov/fs/FS-006-97/FS-006-97.pdf",
-                    "description": "Streamflow Information for the Nation",
                     "@type": "dcat:Distribution",
+                    "description": "Streamflow Information for the Nation",
+                    "downloadURL": "https://pubs.usgs.gov/fs/FS-006-97/FS-006-97.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://water.usgs.gov/edu/measureflow.html",
-                    "description": "How Streamflow is Measured",
                     "@type": "dcat:Distribution",
+                    "description": "How Streamflow is Measured",
+                    "downloadURL": "https://water.usgs.gov/edu/measureflow.html",
+                    "mediaType": "text/html",
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
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.5066/F7P55KJN",
-                    "description": "USGS Water Data for the Nation",
                     "@type": "dcat:Distribution",
+                    "description": "USGS Water Data for the Nation",
+                    "downloadURL": "http://dx.doi.org/10.5066/F7P55KJN",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/stream_flow_USGS/doc/gpmsgusgsifld_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/stream_flow_USGS/doc/gpmsgusgsifld_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/ifloods",
-                    "description": "IFloodS project home page",
                     "@type": "dcat:Distribution",
+                    "description": "IFloodS project home page",
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
+            "identifier": "C1979723016-GHRC_DAAC",
+            "issued": "2017-12-21",
+            "keyword": [
+                "terrestrial hydrosphere",
+                "surface water",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/IFLOODS/GAUGES/DATA301",
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
             "spatial": "-96.5619 40.6017 -90.1904 43.4697",
+            "temporal": "2008-07-24T23:40:00Z/2013-07-01T11:00:00Z",
             "theme": [
                 "IFloodS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM Ground Validation USGS Stream Flow IFloodS V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1957",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hook, S.J., J.S. Myers, K.J. Thome, M. Fitzgerald, A.B. Kahle,  Airborne Sensor Facility NASA Ames Research Center, and R.O. Green. 2022. MASTER: HyspIRI Airborne Campaign, California, Spring 2015. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1957",
-            "issued": "2023-06-29",
-            "temporal": "2015-04-16T17:02:01Z/2015-05-05T22:50:45Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-13",
-            "keyword": [
-                "land surface",
-                "earth science",
-                "visible wavelengths",
-                "surface thermal properties",
-                "infrared wavelengths",
-                "spectral/engineering",
-                "surface radiative properties"
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
-            "identifier": "C2731672247-ORNL_CLOUD",
             "description": "This dataset includes Level 1B (L1B) and Level 2 (L2) data products from the MODIS/ASTER Airborne Simulator (MASTER) instrument. The spectral data were collected as part of the Hyperspectral Infrared Imager (HyspIRI) mission's preparatory airborne campaign during six flights aboard a NASA ER-2 aircraft over California and Nevada, U.S., from 2015-04-16 to 2015-05-05. Data products include L1B georeferenced multispectral imagery of calibrated radiance in 50 bands covering wavelengths of 0.460 to 12.879 micrometers at approximately 50-meter spatial resolution. Derived L2 data products are emissivity in 5 bands in thermal infrared range (8.58 to 12.13 micrometers) and land surface temperature. The L1B file format is HDF-4, and L2 products are provided in ENVI and KMZ formats. In addition, the dataset includes flight paths, spectral band information, instrument configuration, ancillary notes, and summary information for each flight, and browse images derived from each L1B data file.",
-            "graphic-preview-description": "Single band images and an RGB composite image from flight track 11 acquired on 05 May 2015 over the Sierra National Forest near Sumitt Lake and Hot Springs Pass, northeast of Fresno, California. Source: MASTERL1B_1593800_11_20150505_2039_2052_V01.jpg",
-            "title": "MASTER: HyspIRI Airborne Campaign, California, Spring 2015",
-            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_HyspIRI_Spring_2015_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1957",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1957",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/master/MASTER_HyspIRI_Spring_2015/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/master/MASTER_HyspIRI_Spring_2015/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_HyspIRI_Spring_2015.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_HyspIRI_Spring_2015.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1957",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1957",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_HyspIRI_Spring_2015/comp/MASTER_HyspIRI_Spring_2015.pdf",
-                    "description": "MASTER: HyspIRI Airborne Campaign, California, Spring 2015: MASTER_HyspIRI_Spring_2015.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "MASTER: HyspIRI Airborne Campaign, California, Spring 2015: MASTER_HyspIRI_Spring_2015.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_HyspIRI_Spring_2015/comp/MASTER_HyspIRI_Spring_2015.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_HyspIRI_Spring_2015_Fig1.jpg",
-                    "description": "Single band images and an RGB composite image from flight track 11 acquired on 05 May 2015 over the Sierra National Forest near Sumitt Lake and Hot Springs Pass, northeast of Fresno, California. Source: MASTERL1B_1593800_11_20150505_2039_2052_V01.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Single band images and an RGB composite image from flight track 11 acquired on 05 May 2015 over the Sierra National Forest near Sumitt Lake and Hot Springs Pass, northeast of Fresno, California. Source: MASTERL1B_1593800_11_20150505_2039_2052_V01.jpg",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_HyspIRI_Spring_2015_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Single band images and an RGB composite image from flight track 11 acquired on 05 May 2015 over the Sierra National Forest near Sumitt Lake and Hot Springs Pass, northeast of Fresno, California. Source: MASTERL1B_1593800_11_20150505_2039_2052_V01.jpg",
+            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_HyspIRI_Spring_2015_Fig1.jpg",
+            "identifier": "C2731672247-ORNL_CLOUD",
+            "issued": "2023-06-29",
+            "keyword": [
+                "land surface",
+                "earth science",
+                "visible wavelengths",
+                "surface thermal properties",
+                "infrared wavelengths",
+                "spectral/engineering",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1957",
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
             "spatial": "-123.77 31.95 -112.5 40.98",
+            "temporal": "2015-04-16T17:02:01Z/2015-05-05T22:50:45Z",
             "theme": [
                 "MASTER",
                 "HyspIRI Airborne",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MASTER: HyspIRI Airborne Campaign, California, Spring 2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206869-NSIDCV0.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Borehole permafrost data, Kumtor and Taragai Valleys, Tienshan, Kazakhstan, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center.",
-            "issued": "1974-02-23",
-            "temporal": "1974-02-23T00:00:00Z/1995-03-29T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1995-03-29",
-            "keyword": [
-                "atmosphere",
-                "atmospheric temperature",
-                "cryosphere",
-                "atmospheric winds",
-                "soils",
-                "land surface",
-                "frozen ground",
-                "agriculture",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Aldar Gorbunov",
                 "hasEmail": "mailto:ingeo@kazmail.asdc.kz"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NSIDC"
-            },
-            "identifier": "C1386206869-NSIDCV0",
             "description": "This dataset includes observations of the permafrost temperatures in the Inner Tien Shan were started in 1986 by Kazakhstan Alpine Permafrost Laboratory. Observations are carried out on more than 40 boreholes, at altitudes between 3300-4200 m. The depths of the boreholes vary from 30 to 600 m. The boreholes are located in both loose (moraines) sediments and bedrock. Several boreholes are situated in the territory of the 'Kumtor' goldmine. The geocryological conditions of goldmine 'Kumtor' and nearby territory have been discussed in scientific reports 1988, 1989 and articles (see references). Two boreholes were drilled in body of glacier 'Davydov' and located in the central and lateral parts of the glacier (depth - 30 m). A third borehole passed through the glacier, moraine and bedrock to a depth of 600 m. In the Kumtor and Taragai valleys, permafrost temperature in 14 boreholes from 25 to 50 m depth, between 3300-3750 m ASL were observed. The distance between outermost boreholes is about 40 km.\n\nTemperature measurements in 9 geological prospecting adits [tunnels] (lengthwise 1500-1900 m) located in the four neighboring valleys (altitudes from 3920 to 4010 m) were carried out. At the same sites, but in natural conditions, the thermal conductivity of the bedrock was determined by the cylindrical sounding method. Grain size, soil moisture content, cryogenic structure and depth of seasonal thaw were also obtained from 15 pits located in differing altitudinal levels and exposures. At two further sites, ground temperatures measurements at depths of 0, 2, 5, 10, 15, 20 and 40 cm were taken every hour during daylight hours every 5 days over a two year period. Air temperature, wind velocity and duration of daylight were measured at the same time as the ground temperature measurements. These data are presented on the CAPS Version 1.0 CD-ROM, June 1998.",
-            "title": "Borehole permafrost data, Kumtor and Taragai Valleys, Tienshan, Kazakhstan, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/GGD499_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/GGD499_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD499/versions/1",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://nsidc.org/data/GGD499/versions/1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD499/versions/1",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://nsidc.org/data/GGD499/versions/1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386206869-NSIDCV0",
+            "issued": "1974-02-23",
+            "keyword": [
+                "atmosphere",
+                "atmospheric temperature",
+                "cryosphere",
+                "atmospheric winds",
+                "soils",
+                "land surface",
+                "frozen ground",
+                "agriculture",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206869-NSIDCV0.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1995-03-29",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "77.817 41.65 78.233 41.933",
+            "temporal": "1974-02-23T00:00:00Z/1995-03-29T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Borehole permafrost data, Kumtor and Taragai Valleys, Tienshan, Kazakhstan, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/SCAR_A/0001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1999-09-02. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/SCAR_A/0001. http://eosweb.larc.nasa.gov/project/scara/scara_table.",
-            "issued": "1999-09-02",
-            "temporal": "1993-07-12T00:00:00Z/1993-07-29T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-03",
-            "keyword": [
-                "atmosphere",
-                "visible wavelengths",
-                "aerosols",
-                "clouds",
-                "spectral/engineering",
-                "infrared wavelengths",
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
-            "identifier": "C1337195082-LARC_ASDC",
             "description": "SCAR_A_ER2_MAS data are Sulfates, Clouds and Radiation America (SCARA) NASA ER2 Moderate Resolution Imaging Spectrometer (MODIS) Airborne Simulator (MAS) Data in Hierarchical Data Format (HDF).Smoke/Sulfates, Clouds and Radiation - America (SCAR-A) data include physical and chemical components of the Earth's surface, the atmosphere and the radiation field collected in the eastern part of the United States with an emphasis in air pollution.The primary objective of the SCAR-A experiment was to help scientists characterize the the relationship between sulfate particles and clouds' reflective properties. Sulfate aerosols are believed to provide condensation nuclei, resulting in smaller, more numerous droplets within a cloud. SCAR-A was the first in a series of experiments. It was was followed by the SCAR-C experiment conducted over California in 1994. A third experiment, SCAR-B was conducted in Brazil during August and September 1995. The MODIS Airbourne Simulator (MAS) is a modified Daedalus Wildfire scanning spectrometer which flies on a NASA ER-2 and provides spectral information similar to that provided by the Moderate Resolution Imaging Spectroradiometer (MODIS), launched on Terra (EOS AM-1) in 1999 and Aqua (EOS PM-1) in 2002. The MAS spectrometer acquires high spatial resolution imagery in the wavelength range of 0.55 to 14.3 microns. A total of 50 spectral bands are available in this range, and the digitizer can be configured to collect data from any 12 of these bands. The digitizer was configured with four 10-bit channels and seven 8-bit channels. The MAS spectrometer was mated to a scanner subassembly which collected image data with an IFOV of 2.5 mrad, giving a ground resolution of 50 meters from 20000 meters altitude, and a cross track scan width of 85.92 degrees. The data granules were written using the self documenting file storage format provided through the netCDF interface routines included in the HDF libraries.",
-            "title": "Sulfates, Clouds and Radiation America NASA ER-2 Moderate Resolution Imaging Spectrometer (MODIS) Airborne Simulator (MAS) Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FSCAR_A%2F0001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FSCAR_A%2F0001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1502965,1502 +1502942,1537 @@
                     "title": "View this dataset's data citation policy"
                 }
             ],
+            "identifier": "C1337195082-LARC_ASDC",
+            "issued": "1999-09-02",
+            "keyword": [
+                "atmosphere",
+                "visible wavelengths",
+                "aerosols",
+                "clouds",
+                "spectral/engineering",
+                "infrared wavelengths",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/SCAR_A/0001",
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
             "spatial": "-99.97 35.02 -79.75 44.54",
+            "temporal": "1993-07-12T00:00:00Z/1993-07-29T23:59:59Z",
             "theme": [
                 "SCAR_A",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sulfates, Clouds and Radiation America NASA ER-2 Moderate Resolution Imaging Spectrometer (MODIS) Airborne Simulator (MAS) Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/459/",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Ashok Srivastava",
+                "hasEmail": "mailto:ashok.n.srivastava@gmail.com"
+            },
+            "description": "## Confirmed Speakers from the United States\r\n\r\n<ul>\r\n<li>  Ashok N. Srivastava, NASA Ames Research Center \r\n<li>  Robert Mah, NASA Ames Research Center\r\n<li>  Gary Hunter, NASA Glenn Research Center\r\n<li>  Nagi Gabraeel, Georgia Tech\r\n<li>  Vitali Volovoi, Georgia Tech\r\n<li>  Eric Feron, Georgia Tech\r\n<li>  Pradeep Lall, Auburn University\r\n<li>  Fu-Kuo Chang, Stanford University\r\n<li>  Tim Wilmering, Boeing\r\n<li>  Natarajan Shankar, SRI\r\n<li>  George Vachtesvanos, Impact Technologies\r\n</ul>",
+            "identifier": "DASHLINK_459",
             "issued": "2011-09-03",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "ames",
                 "nasa",
                 "dashlink"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Ashok Srivastava",
-                "hasEmail": "mailto:ashok.n.srivastava@gmail.com"
-            },
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/459/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Dashlink"
             },
-            "identifier": "DASHLINK_459",
-            "description": "## Confirmed Speakers from the United States\r\n\r\n<ul>\r\n<li>  Ashok N. Srivastava, NASA Ames Research Center \r\n<li>  Robert Mah, NASA Ames Research Center\r\n<li>  Gary Hunter, NASA Glenn Research Center\r\n<li>  Nagi Gabraeel, Georgia Tech\r\n<li>  Vitali Volovoi, Georgia Tech\r\n<li>  Eric Feron, Georgia Tech\r\n<li>  Pradeep Lall, Auburn University\r\n<li>  Fu-Kuo Chang, Stanford University\r\n<li>  Tim Wilmering, Boeing\r\n<li>  Natarajan Shankar, SRI\r\n<li>  George Vachtesvanos, Impact Technologies\r\n</ul>",
-            "title": "Workshop on IVHM and Aviation Safety:  Invited Speakers",
-            "programCode": [
-                "026:029"
-            ],
-            "accrualPeriodicity": "irregular"
+            "title": "Workshop on IVHM and Aviation Safety:  Invited Speakers"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GRGSM-20C06",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "GRACE. 2018-05-10. GRACE Monthly Geopotential Spherical Harmonic Coefficients CSR (GSM). Version 6.0. GRACE_GSM_L2_GRAV_CSR_RL06. JPL. Archived by National Aeronautics and Space Administration, U.S. Government, CSR. https://doi.org/10.5067/GRGSM-20C06. https://podaac-tools.jpl.nasa.gov/drive/files/allData/grace/docs/. GRACE, CSR, 2018-05-10, GRACE FIELD GEOPOTENTIAL COEFFICIENTS CSR RELEASE 6.0, https://podaac-tools.jpl.nasa.gov/drive/files/allData/grace/docs/.",
-            "issued": "2018-04-26",
-            "temporal": "2002-04-05T00:00:00Z/2017-06-30T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-04-26",
-            "keyword": [
-                "oceans",
-                "earth science",
-                "gravity/gravitational field",
-                "ocean pressure",
-                "solid earth"
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
-            "identifier": "C2491772131-POCLOUD",
-            "description": "FOR EXPERT USE ONLY.  This dataset contains estimates of static field geopotential of the Earth, derived from the Gravity Recovery and Climate Experiment (GRACE) mission measurements, produced by the Center for Space Research (CSR) at University of Texas at Austin.  The data are in spherical harmonics averaged over approximately a month.  The primary objective of the GRACE mission is to obtain accurate estimates of the mean and time-variable components of the gravity field variations.  This objective is achieved by making continuous measurements of the change in distance between twin spacecraft, co-orbiting in about 500 km altitude, near circular, polar orbit, spaced approximately 200 km apart, using a microwave ranging system.  In addition to these range change, the non-gravitional forces are measured on each satellite using a high accuracy electrostatic, room-temperature accelerometer.  The satellite orientation and position (and timing) are precisely measured using twin star cameras and a GPS receiver, respectively.  Spatial and temporal variations in the gravity field affect the orbits (or trajectories) of the twin spacecraft differently.  These differences are manifested as changes in the distance between the spacecraft, as they orbit the Earth.  This change in distance is reflected in the time-of-flight of microwave signals transmitted and received nearly simultaneously between the two spacecraft.  The change in this time of fight is continuously measured by tracking the phase of the microwave carrier signals.  The so called dual-one-way range change measurements can be reconstructed from these phase measurements.  This range change (or its numerically derived derivatives), along with other mission and ancillary data, is subsequently analyzed to extract the parameters of an Earth gravity field model.",
-            "release-place": "JPL",
-            "series-name": "GRACE Monthly Geopotential Spherical Harmonic Coefficients CSR (GSM)",
-            "graphic-preview-description": "Thumbnail",
             "creator": "GRACE",
-            "title": "GRACE FIELD GEOPOTENTIAL COEFFICIENTS CSR RELEASE 6.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GRACE_GSM_L2_GRAV_CSR_RL06.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "FOR EXPERT USE ONLY.  This dataset contains estimates of static field geopotential of the Earth, derived from the Gravity Recovery and Climate Experiment (GRACE) mission measurements, produced by the Center for Space Research (CSR) at University of Texas at Austin.  The data are in spherical harmonics averaged over approximately a month.  The primary objective of the GRACE mission is to obtain accurate estimates of the mean and time-variable components of the gravity field variations.  This objective is achieved by making continuous measurements of the change in distance between twin spacecraft, co-orbiting in about 500 km altitude, near circular, polar orbit, spaced approximately 200 km apart, using a microwave ranging system.  In addition to these range change, the non-gravitional forces are measured on each satellite using a high accuracy electrostatic, room-temperature accelerometer.  The satellite orientation and position (and timing) are precisely measured using twin star cameras and a GPS receiver, respectively.  Spatial and temporal variations in the gravity field affect the orbits (or trajectories) of the twin spacecraft differently.  These differences are manifested as changes in the distance between the spacecraft, as they orbit the Earth.  This change in distance is reflected in the time-of-flight of microwave signals transmitted and received nearly simultaneously between the two spacecraft.  The change in this time of fight is continuously measured by tracking the phase of the microwave carrier signals.  The so called dual-one-way range change measurements can be reconstructed from these phase measurements.  This range change (or its numerically derived derivatives), along with other mission and ancillary data, is subsequently analyzed to extract the parameters of an Earth gravity field model.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGRGSM-20C06",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGRGSM-20C06",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/grace/open/L1B/GFZ/AOD1B/RL04/docs/ReleaseNotes_csr_RL06.txt",
-                    "description": "Release Notes for GRACE L-2 products - version UTCSR RL-06",
                     "@type": "dcat:Distribution",
+                    "description": "Release Notes for GRACE L-2 products - version UTCSR RL-06",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/grace/open/L1B/GFZ/AOD1B/RL04/docs/ReleaseNotes_csr_RL06.txt",
+                    "mediaType": "text/html",
                     "title": "View an important notice for this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/grace/open/L1B/GFZ/AOD1B/RL04/docs/L2-CSR006_ProcStd_v5.0.pdf",
-                    "description": "UTCSR Level-2 Processing Standards Document For Level-2 Product Release 06",
                     "@type": "dcat:Distribution",
+                    "description": "UTCSR Level-2 Processing Standards Document For Level-2 Product Release 06",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/grace/open/L1B/GFZ/AOD1B/RL04/docs/L2-CSR006_ProcStd_v5.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GRACE_GSM_L2_GRAV_CSR_RL06.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GRACE_GSM_L2_GRAV_CSR_RL06.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
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
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/grace/open/L1B/GFZ/AOD1B/RL04/docs/L2-UserHandbook_v4.0.pdf",
-                    "description": "Level-2 Gravity Field Product User Handbook",
                     "@type": "dcat:Distribution",
+                    "description": "Level-2 Gravity Field Product User Handbook",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/grace/open/L1B/GFZ/AOD1B/RL04/docs/L2-UserHandbook_v4.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/gracefo/open/L2/CSR/RL06/README.txt",
-                    "description": "README file",
                     "@type": "dcat:Distribution",
+                    "description": "README file",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/gracefo/open/L2/CSR/RL06/README.txt",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772131-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772131-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772131-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772131-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GRACE_GSM_L2_GRAV_CSR_RL06.jpg",
+            "identifier": "C2491772131-POCLOUD",
+            "issued": "2018-04-26",
+            "keyword": [
+                "oceans",
+                "earth science",
+                "gravity/gravitational field",
+                "ocean pressure",
+                "solid earth"
+            ],
+            "landingPage": "https://doi.org/10.5067/GRGSM-20C06",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-04-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "JPL",
+            "series-name": "GRACE Monthly Geopotential Spherical Harmonic Coefficients CSR (GSM)",
             "spatial": "-180.0 -88.0 180.0 88.0",
+            "temporal": "2002-04-05T00:00:00Z/2017-06-30T00:00:00Z",
             "theme": [
                 "GRACE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GRACE FIELD GEOPOTENTIAL COEFFICIENTS CSR RELEASE 6.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/770",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Myneni, R.B., Y. Tian, and Y. Wang. 2005. SAFARI 2000 LAI Measurements at Kalahari Transect Sites, Wet Season 2000. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/770",
-            "issued": "2023-10-18",
-            "temporal": "2000-03-04T00:00:00Z/2000-03-16T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-24",
-            "keyword": [
-                "biosphere",
-                "earth science",
-                "ecosystems",
-                "vegetation",
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
-            "identifier": "C2789085993-ORNL_CLOUD",
             "description": "The Boston University team collected several data sets along the Kalahari Transect during the SAFARI 2000 wet season field campaign from March 3rd to March 18th, 2000, to support the validation of the MODIS LAI/FPAR algorithm. Ground measurements of LAI, FPAR, leaf hemispherical reflectance, leaf hemispherical transmittance, and canopy transmittance were made using a LAI-2000 plant canopy analyzer, an AccuPAR ceptometer, a LiCor 1800-12S External Integrating Sphere (LI-1800) portable spectroradiometer, and an ASD handheld spectroradiometer. LAI data are provided in this data set. LAI was intensively measured at 4 different sites in Botswana -- Pandamatenga, Maun, Okwa River, and Tshane (from north to south) -- where vegetation types range from moist closed woodlands to arid sparsely-shrub-covered grasslands.",
-            "graphic-preview-description": "Browse Image",
-            "title": "SAFARI 2000 LAI Measurements at Kalahari Transect Sites, Wet Season 2000",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/safari_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F770",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F770",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/field_campaign/kt_lai/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/field_campaign/kt_lai/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/S2K/guides/kt_lai.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/S2K/guides/kt_lai.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/770",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/770",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/field_campaign/kt_lai/comp/GPS_Coords_transect_endpts.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/field_campaign/kt_lai/comp/GPS_Coords_transect_endpts.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/field_campaign/kt_lai/comp/kt_lai.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/field_campaign/kt_lai/comp/kt_lai.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/field_campaign/kt_lai/comp/kt_lai_readme.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/field_campaign/kt_lai/comp/kt_lai_readme.pdf",
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
+            "identifier": "C2789085993-ORNL_CLOUD",
+            "issued": "2023-10-18",
+            "keyword": [
+                "biosphere",
+                "earth science",
+                "ecosystems",
+                "vegetation",
+                "atmospheric radiation",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/770",
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
             "spatial": "21.71 -24.13 25.49 -18.66",
+            "temporal": "2000-03-04T00:00:00Z/2000-03-16T23:59:59Z",
             "theme": [
                 "SAFARI 2000",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAFARI 2000 LAI Measurements at Kalahari Transect Sites, Wet Season 2000"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MODCSR_B.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MODIS Science Team. 2017-10-01. MODIS/Terra 8-Day Clear Sky Radiance Bias Daily L3 Global 1Deg Zonal Bands. Version 6.1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/MODIS/MODCSR_B.061. https://doi.org/10.5067/MODIS/MODCSR_B.061.",
-            "issued": "2017-10-01",
-            "temporal": "2000-02-24T00:00:00Z/2025-01-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-17",
-            "keyword": [
-                "earth science",
-                "spectral/engineering",
-                "infrared wavelengths",
-                "microwave",
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
-            "identifier": "C1444171490-LAADS",
-            "description": "The MODIS/Terra 8-Day Clear Sky Radiance Bias Daily L3 Global 1Deg Zonal Bands (MODCSR_B) product consists of 1-degree zonal mean clear-sky biases (observed minus calculated radiance differences) and associated statistics for bands 31 and 33-36 for each calendar day from the previous eight-day period. Zonal means (5-zone moving averages) are created from the eight-day, 25-km radiance differences for daytime land, nighttime land, and ocean data separately. Day and night land data are combined south of -60 degrees latitude due to poor clear-sky sampling and the difficulty of discriminating between clear and cloudy conditions in this region. The zonal mean biases are utilized to correct clear-sky radiance calculations in the cloud top pressure (CO2 slicing) algorithm. The files are in Hierarchical Data Format (HDF).",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "MODIS Science Team",
-            "title": "MODIS/Terra 8-Day Clear Sky Radiance Bias Daily L3 Global 1Deg Zonal Bands",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MODIS/Terra 8-Day Clear Sky Radiance Bias Daily L3 Global 1Deg Zonal Bands (MODCSR_B) product consists of 1-degree zonal mean clear-sky biases (observed minus calculated radiance differences) and associated statistics for bands 31 and 33-36 for each calendar day from the previous eight-day period. Zonal means (5-zone moving averages) are created from the eight-day, 25-km radiance differences for daytime land, nighttime land, and ocean data separately. Day and night land data are combined south of -60 degrees latitude due to poor clear-sky sampling and the difficulty of discriminating between clear and cloudy conditions in this region. The zonal mean biases are utilized to correct clear-sky radiance calculations in the cloud top pressure (CO2 slicing) algorithm. The files are in Hierarchical Data Format (HDF).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMODCSR_B.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMODCSR_B.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MODCSR_B.061",
-                    "description": "The product landing page",
                     "@type": "dcat:Distribution",
+                    "description": "The product landing page",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MODCSR_B.061",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/MODCSR_B--61",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/MODCSR_B--61",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MODCSR_B/",
-                    "description": "Direct access to MODCSR_B C6.1 data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to MODCSR_B C6.1 data set.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MODCSR_B/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/61/MODCSR_B/contents.html",
-                    "description": "Direct access to product's OPeNDAP directory",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to product's OPeNDAP directory",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/61/MODCSR_B/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1444171490-LAADS",
+            "issued": "2017-10-01",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "infrared wavelengths",
+                "microwave",
+                "ngda",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MODCSR_B.061",
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
+            "temporal": "2000-02-24T00:00:00Z/2025-01-27T00:00:00Z",
             "theme": [
                 "Terra",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Terra 8-Day Clear Sky Radiance Bias Daily L3 Global 1Deg Zonal Bands"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-PRL-67PCHURYUMOV-M07B-V1.0",
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
+            "description": "This data set contains calibrated images acquired by the OSIRIS Narrow Angle\nCamera during the prelanding phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-09-16 to 2014-09-23.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-prl-67pchuryumov-m07b-v1.0_v77h-pb92",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-PRL-67PCHURYUMOV-M07B-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-prl-67pchuryumov-m07b-v1.0_v77h-pb92",
-            "description": "This data set contains calibrated images acquired by the OSIRIS Narrow Angle\nCamera during the prelanding phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-09-16 to 2014-09-23.",
-            "title": "ROSETTA-ORBITER COMET PRELANDING OSINAC 3 RDR MTP 007B V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER COMET PRELANDING OSINAC 3 RDR MTP 007B V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-SPICE-6-EARTH-V1.0",
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
+            "description": "This data set includes the complete set of SPICE data for one NEAR mission phase in the form of SPICE kernels, which can be accessed using SPICE software available to read these files.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-spice-6-earth-v1.0_v794-f2vc",
+            "issued": "2021-05-21",
+            "keyword": [
+                "eros",
+                "near earth asteroid rendezvous"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-SPICE-6-EARTH-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-spice-6-earth-v1.0_v794-f2vc",
-            "description": "This data set includes the complete set of SPICE data for one NEAR mission phase in the form of SPICE kernels, which can be accessed using SPICE software available to read these files.",
-            "title": "NEAR SPICE KERNELS EARTH",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEAR SPICE KERNELS EARTH"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-5-EXT3-67P-M35-GEO-V1.0",
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
+            "description": "This CODMAC level 5 data set contains derived data products that include pixel-precise georeferencing information, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 3 mission phase, covering the period from 2016-09-26T06:40:00.000 to 2016-10-01T00:00:00.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-5-ext3-67p-m35-geo-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-5-EXT3-67P-M35-GEO-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-5-ext3-67p-m35-geo-v1.0",
-            "description": "This CODMAC level 5 data set contains derived data products that include pixel-precise georeferencing information, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 3 mission phase, covering the period from 2016-09-26T06:40:00.000 to 2016-10-01T00:00:00.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 5 EXT3-MTP035 DDR-GEO V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 5 EXT3-MTP035 DDR-GEO V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQR50-3DCCE",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA Aquarius project. 2017-12-07. Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Mission Cumulative Data. Version 5.0. Aquarius Sea Surface Salinity Products. Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC OBPG. https://doi.org/10.5067/AQR50-3DCCE. http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius. NASA Aquarius project, NASA/GSFC OBPG, 2017-12-07, Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Mission Cumulative Data V5.0, http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius.",
-            "issued": "2017-10-21",
-            "temporal": "2011-08-25T01:45:23Z/2015-06-07T12:45:21Z",
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
-            "identifier": "C2491755842-POCLOUD",
-            "description": "Aquarius Level 3 sea surface density standard mapped image data contains gridded 1 degree spatial resolution derived density averaged over daily, 7 day, monthly, and seasonal time scales. This particular data set is the mission\nseries mean or cumulative, sea surface density product for version 5.0 of the Aquarius data set.  Surface density estimates are based on TEOS-10 and derived using retrieved salinity from Aquarius and collocated ancillary SST (Reynolds OI 0.25 degree product). The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
-            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA",
-            "series-name": "Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Mission Cumulative Data",
-            "graphic-preview-description": "Thumbnail",
             "creator": "NASA Aquarius project",
-            "title": "Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Mission Cumulative Data V5.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_DENSITY_SMI_CUMULATIVE_V5.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Aquarius Level 3 sea surface density standard mapped image data contains gridded 1 degree spatial resolution derived density averaged over daily, 7 day, monthly, and seasonal time scales. This particular data set is the mission\nseries mean or cumulative, sea surface density product for version 5.0 of the Aquarius data set.  Surface density estimates are based on TEOS-10 and derived using retrieved salinity from Aquarius and collocated ancillary SST (Reynolds OI 0.25 degree product). The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3DCCE",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3DCCE",
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_DENSITY_SMI_CUMULATIVE_V5.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_DENSITY_SMI_CUMULATIVE_V5.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491755842-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491755842-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491755842-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491755842-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_DENSITY_SMI_CUMULATIVE_V5.jpg",
+            "identifier": "C2491755842-POCLOUD",
+            "issued": "2017-10-21",
+            "keyword": [
+                "oceans",
+                "earth science",
+                "salinity/density"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQR50-3DCCE",
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
+            "series-name": "Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Mission Cumulative Data",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T01:45:23Z/2015-06-07T12:45:21Z",
             "theme": [
                 "AQUARIUS SAC-D",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Mission Cumulative Data V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSIWAC-4-RVM1-CHKOUT-REFLECT-V1.0",
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
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled)  image data in reflectance units (normalized and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the RENDEZVOUS MANOEUVRE 1 mission phase, covering the period  from 2010-09-04T00:00:00.000 to 2011-07-13T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. This version V1.0 is the first version of this dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osiwac-4-rvm1-chkout-reflect-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSIWAC-4-RVM1-CHKOUT-REFLECT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osiwac-4-rvm1-chkout-reflect-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled)  image data in reflectance units (normalized and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the RENDEZVOUS MANOEUVRE 1 mission phase, covering the period  from 2010-09-04T00:00:00.000 to 2011-07-13T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. This version V1.0 is the first version of this dataset.",
-            "title": "ROSETTA-ORBITER CHECKOUT OSIWAC 4 RVM1 RDR-REFLECT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECKOUT OSIWAC 4 RVM1 RDR-REFLECT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-PANCAM-3-RADCAL-RDR-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-pancam-3-radcal-rdr-v1.0_v7cj-6r4a",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-PANCAM-3-RADCAL-RDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-pancam-3-radcal-rdr-v1.0_v7cj-6r4a",
-            "description": "not applicable",
-            "title": "MER 2 MARS PANCAM RADIOMETRICALLY CALIBRATED RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MER 2 MARS PANCAM RADIOMETRICALLY CALIBRATED RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-RSS-1-SAGR7-V1.0",
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
+            "description": "The Cassini Radio Science Saturn Gravity Science Experiment (SAGR7) Raw Data Archive is a time-ordered collection of radio science raw data acquired on April 2, May 17, June 8, 9, 14, 16, 21 and 29, 2008, during the Tour subphase of the Cassini mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-rss-1-sagr7-v1.0_v7cu-e9ee",
+            "issued": "2018-06-26",
+            "keyword": [
+                "cassini-huygens",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-RSS-1-SAGR7-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-rss-1-sagr7-v1.0_v7cu-e9ee",
-            "description": "The Cassini Radio Science Saturn Gravity Science Experiment (SAGR7) Raw Data Archive is a time-ordered collection of radio science raw data acquired on April 2, May 17, June 8, 9, 14, 16, 21 and 29, 2008, during the Tour subphase of the Cassini mission.",
-            "title": "CASSINI RSS RAW DATA SET - SAGR7 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI RSS RAW DATA SET - SAGR7 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LRO-L-LOLA-2-EDR-V1.0",
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
-                "lunar reconnaissance orbiter",
-                "moon"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains archival raw experiment data from the Lunar Orbiter Laser Altimeter instrument (LOLA).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lro-l-lola-2-edr-v1.0_v7d3-ij7c",
+            "issued": "2021-05-21",
+            "keyword": [
+                "lunar reconnaissance orbiter",
+                "moon"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LRO-L-LOLA-2-EDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lro-l-lola-2-edr-v1.0_v7d3-ij7c",
-            "description": "This data set contains archival raw experiment data from the Lunar Orbiter Laser Altimeter instrument (LOLA).",
-            "title": "LRO MOON LASER ALTIMETER 2 EDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "LRO MOON LASER ALTIMETER 2 EDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1125-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-24T10:22:10.000 to 2015-10-24T17:19:43.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1125-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1125-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1125-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-24T10:22:10.000 to 2015-10-24T17:19:43.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1125 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1125 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-NAVCAM-5-MOSAIC-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-navcam-5-mosaic-ops-v1.0_v7h4-wyzf",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars exploration rover",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-NAVCAM-5-MOSAIC-OPS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-navcam-5-mosaic-ops-v1.0_v7h4-wyzf",
-            "description": "not applicable",
-            "title": "MER 1 MARS NAVIGATION CAMERA MOSAICS RDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MER 1 MARS NAVIGATION CAMERA MOSAICS RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/340/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2011-04-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "nasa",
-                "dashlink",
-                "ames"
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
-            "identifier": "DASHLINK_340",
             "description": "This will contain publications used by the AePW",
-            "title": "AePW publications",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/AePW_Status_AIAA_SDTC_April_2011-JH.pptx.pdf",
-                    "description": "Presentation to SDTC at SDM2011",
                     "@type": "dcat:Distribution",
+                    "description": "Presentation to SDTC at SDM2011",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/AePW_Status_AIAA_SDTC_April_2011-JH.pptx.pdf",
+                    "mediaType": "application/pdf",
                     "title": "AePW_Status_AIAA_SDTC_April_2011-JH.pptx.pdf"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/sampleabstract.doc",
-                    "description": "Sample Abstract for Data Submittal",
                     "@type": "dcat:Distribution",
+                    "description": "Sample Abstract for Data Submittal",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/sampleabstract.doc",
+                    "mediaType": "application/msword",
                     "title": "sampleabstract.doc"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_340",
+            "issued": "2011-04-01",
+            "keyword": [
+                "nasa",
+                "dashlink",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/340/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "AePW publications"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-OSIWAC-3-AST1-STEINSFLYBY-V1.4",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera during the STEINS_FLY-BY mission phase",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-osiwac-3-ast1-steinsflyby-v1.4_v7ie-wb9v",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "2867 steins",
                 "vega",
                 "international rosetta mission",
                 "16 cyg b"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-OSIWAC-3-AST1-STEINSFLYBY-V1.4",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-osiwac-3-ast1-steinsflyby-v1.4_v7ie-wb9v",
-            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera during the STEINS_FLY-BY mission phase",
-            "title": "ROSETTA-ORBITER STEINS_FLY-BY OSIWAC 3 RDR V1.4",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER STEINS_FLY-BY OSIWAC 3 RDR V1.4"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-PWS-5-DDR-PLASMA-DENSITY-1S-V1.0",
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
+            "description": "Electron plasma density data set for Jupiter's outer magnetosphere derived from high-resolution wideband measurements of low-frequency radio and plasma waves obtained by Voyagers 1 and 2 during their 1979 flybys.  Density data were measured at 1-second intervals.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-pws-5-ddr-plasma-density-1s-v1.0_v7ij-7nmn",
+            "issued": "2018-06-26",
+            "keyword": [
+                "voyager",
+                "jupiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-PWS-5-DDR-PLASMA-DENSITY-1S-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-pws-5-ddr-plasma-density-1s-v1.0_v7ij-7nmn",
-            "description": "Electron plasma density data set for Jupiter's outer magnetosphere derived from high-resolution wideband measurements of low-frequency radio and plasma waves obtained by Voyagers 1 and 2 during their 1979 flybys.  Density data were measured at 1-second intervals.",
-            "title": "VG2 J PLASMA WAVE SPECTROMETER DENSITY 1S V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG2 J PLASMA WAVE SPECTROMETER DENSITY 1S V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0249-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-27T19:18:10.000 to 2014-08-27T23:29:29.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0249-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0249-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0249-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-27T19:18:10.000 to 2014-08-27T23:29:29.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0249 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0249 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQR50-3D1AE",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA Aquarius project. 2017-12-07. Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Ascending Daily Data. Version 5.0. Aquarius Sea Surface Salinity Products. Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC OBPG. https://doi.org/10.5067/AQR50-3D1AE. http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius. NASA Aquarius project, NASA/GSFC OBPG, 2017-12-07, Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Ascending Daily Data V5.0, http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius.",
-            "issued": "2017-10-21",
-            "temporal": "2011-08-25T01:45:23Z/2015-06-07T11:41:38Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-07",
-            "keyword": [
-                "earth science",
-                "oceans",
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
-            "identifier": "C2491755993-POCLOUD",
-            "description": "Aquarius Level 3 sea surface density standard mapped image data contains gridded 1 degree spatial resolution density data averaged over daily, 7 day, monthly, and seasonal time scales. This particular data set is the Daily, Ascending sea surface density product\nfor version 5.0 of the Aquarius data set. Only retrieved values for Ascending passes have been used to create this product.  Surface density estimates are based on TEOS-10 and derived using retrieved salinity from Aquarius and collocated ancillary SST (Reynolds OI 0.25 degree product). The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
-            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA",
-            "series-name": "Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Ascending Daily Data",
-            "graphic-preview-description": "Thumbnail",
             "creator": "NASA Aquarius project",
-            "title": "Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Ascending Daily Data V5.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_DENSITY_SMIA_DAILY_V5.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Aquarius Level 3 sea surface density standard mapped image data contains gridded 1 degree spatial resolution density data averaged over daily, 7 day, monthly, and seasonal time scales. This particular data set is the Daily, Ascending sea surface density product\nfor version 5.0 of the Aquarius data set. Only retrieved values for Ascending passes have been used to create this product.  Surface density estimates are based on TEOS-10 and derived using retrieved salinity from Aquarius and collocated ancillary SST (Reynolds OI 0.25 degree product). The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3D1AE",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3D1AE",
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
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_DENSITY_SMIA_DAILY_V5.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_DENSITY_SMIA_DAILY_V5.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491755993-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491755993-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491755993-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491755993-POCLOUD",
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
```

