# Change History for nasa.json (Part 106)

### Changes from 31606f9 to dd2190f (Part 95/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
-            "title": "MODIS/Terra+Aqua BRDF/Albedo Parameter1 Band3 Daily L3 Global 30ArcSec CMG V061",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MCD43D07 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) Model Parameter dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. Each of the three model parameters (isotropic, volumetric, and geometric) for each of the MODIS bands 1 through 7 and the visible, near infrared (NIR), and shortwave bands included in MCD43C1 (https://doi.org/10.5067/MODIS/MCD43C1.061) are stored in a separate file as MCD43D01 through MCD43D30. \r\n\r\nMCD43D07 is the BRDF isotropic parameter for MODIS band 3. The isotropic parameter, in conjunction with the volumetric and geometric parameters, is used to derive the BRDF/Albedo values for MODIS band 3. \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D07.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D07.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D07.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D07.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2539207575-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2539207575-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D07.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D07.061",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MCD43D07",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MCD43D07",
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
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D07.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D07.061/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2539207575-LPCLOUD",
+            "issued": "2021-02-22",
+            "keyword": [
+                "surface radiative properties",
+                "earth science",
+                "land surface",
+                "national geospatial data asset",
+                "ngda"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D07.061",
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
+            "title": "MODIS/Terra+Aqua BRDF/Albedo Parameter1 Band3 Daily L3 Global 30ArcSec CMG V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-11-09",
-            "temporal": "2021-11-09T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "space",
-                "trajectory",
-                "topo",
-                "station",
-                "location",
-                "iss",
-                "international",
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
-            "identifier": "nasa-iss-data_2021-11-09_jswm-23pg",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2021-11-09",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -994936,186 +994912,212 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2021-11-09_jswm-23pg",
+            "issued": "2021-11-09",
+            "keyword": [
+                "space",
+                "trajectory",
+                "topo",
+                "station",
+                "location",
+                "iss",
+                "international",
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
+            "temporal": "2021-11-09T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2021-11-09"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7265/qt2b-y743",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Arctic Sea State 2015 Field Campaign, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center. https://doi.org/10.7265/qt2b-y743.",
-            "issued": "2015-10-01",
-            "temporal": "2015-10-01T00:00:00Z/2015-11-07T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-11-07",
-            "keyword": [
-                "salinity/density",
-                "sea ice",
-                "atmosphere",
-                "atmospheric pressure",
-                "ocean waves",
-                "earth science",
-                "atmospheric winds",
-                "cryosphere",
-                "atmospheric water vapor",
-                "ocean temperature",
-                "clouds",
-                "atmospheric temperature",
-                "oceans",
-                "snow/ice",
-                "ocean circulation",
-                "ocean heat budget"
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
-            "identifier": "C2109756241-NSIDCV0",
             "description": "The U.S. Office of Naval Research (ONR) Sea State Departmental Research Initiative (DRI) field campaign was conducted during autumn of 2015 in the Beaufort Sea in order to better understand how waves and ice interact as Arctic ice advances in late autumn. Data collection took place under four sampling modes: wave experiments, ice stations, flux stations, and ship surveys. This data set provides curated data from this field campaign in NetCDF data files.",
-            "title": "Arctic Sea State 2015 Field Campaign, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2Fqt2b-y743",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2Fqt2b-y743",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/G10030_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/G10030_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/qt2b-y743",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/qt2b-y743",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/qt2b-y743",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/qt2b-y743",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2109756241-NSIDCV0",
+            "issued": "2015-10-01",
+            "keyword": [
+                "salinity/density",
+                "sea ice",
+                "atmosphere",
+                "atmospheric pressure",
+                "ocean waves",
+                "earth science",
+                "atmospheric winds",
+                "cryosphere",
+                "atmospheric water vapor",
+                "ocean temperature",
+                "clouds",
+                "atmospheric temperature",
+                "oceans",
+                "snow/ice",
+                "ocean circulation",
+                "ocean heat budget"
+            ],
+            "landingPage": "https://doi.org/10.7265/qt2b-y743",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-11-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "-168.49 62.76 -148.53 75.48",
+            "temporal": "2015-10-01T00:00:00Z/2015-11-07T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Arctic Sea State 2015 Field Campaign, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/857/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-12-12",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "ames",
-                "nasa"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jose Celaya Galvan",
                 "hasEmail": "mailto:jose.r.celayagalvan@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_857",
             "description": "The prognostic technique for a power MOSFET presented\r\nin this paper is based on accelerated aging of MOSFET\r\nIRF520Npbf in a TO-220 package. The methodology utilizes\r\nthermal and power cycling to accelerate the life of the devices.\r\nThe major failure mechanism for the stress conditions is die attachment\r\ndegradation, typical for discrete devices with lead free\r\nsolder die attachment. It has been determined that die attach\r\ndegradation results in an increase in ON-state resistance\r\ndue to its dependence on junction temperature. Increasing\r\nresistance, thus, can be used as a precursor of failure for the\r\ndie-attach failure mechanism under thermal stress. A feature\r\nbased on normalized ON-resistance is computed from in-situ\r\nmeasurements of the electro-thermal response. An Extended\r\nKalman filter is used as a model-based prognostics techniques\r\nbased on the Bayesian tracking framework.",
-            "title": "Prognostics Approach For Power Mosfet Under Thermal-Stress Aging",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/RAMS-12_MOSFET_Final.pdf",
-                    "description": "Full paper PDF",
                     "@type": "dcat:Distribution",
+                    "description": "Full paper PDF",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/RAMS-12_MOSFET_Final.pdf",
+                    "mediaType": "application/pdf",
                     "title": "RAMS-12 MOSFET Final.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_857",
+            "issued": "2013-12-12",
+            "keyword": [
+                "dashlink",
+                "ames",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/857/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Prognostics Approach For Power Mosfet Under Thermal-Stress Aging"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-XGRS-2-EDR-CRUISE3-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-xgrs-2-edr-cruise3-v1.0_jsym-3dy7",
+            "issued": "2018-06-26",
+            "keyword": [
+                "solar system",
+                "near earth asteroid rendezvous"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-XGRS-2-EDR-CRUISE3-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-xgrs-2-edr-cruise3-v1.0_jsym-3dy7",
-            "description": "NEAR EDR volume sets contain a single data set, from one instrument and one mission phase (defined in the phase table in /AAREADME.TXT).",
-            "title": "NEAR XGRS SPECTRA FOR CRUISE3",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEAR XGRS SPECTRA FOR CRUISE3"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-PFS-2-EDR-EXT1-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The Mars Express PFS data set contains raw (CODMAC Level 2) measurements from the Planetary Fourier Spectrometer collected during the first extension Mars orbit phases.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-pfs-2-edr-ext1-v1.0_jsyt-9jue",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "deep space",
                 "internal source",
@@ -995124,438 +995126,447 @@
                 "phobos",
                 "responsivity"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-PFS-2-EDR-EXT1-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-pfs-2-edr-ext1-v1.0_jsyt-9jue",
-            "description": "The Mars Express PFS data set contains raw (CODMAC Level 2) measurements from the Planetary Fourier Spectrometer collected during the first extension Mars orbit phases.",
-            "title": "MARS EXPRESS MARS PFS EDR FIRST\n                                 EXTENSION MISSION DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS PFS EDR FIRST\n                                 EXTENSION MISSION DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0030",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2010-11-02. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDCDAAC/NARSTO/0030.",
-            "issued": "2011-08-25",
-            "temporal": "2000-10-03T00:00:00Z/2003-09-19T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-04-18",
-            "keyword": [
-                "atmospheric chemistry",
-                "aerosols",
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
-            "identifier": "C2338659983-LARC_ASDC",
             "description": "NARSTO_EPA_SS_LOS_ANGELES_PARTISOL_DATA is the North American Research Strategy for Tropospheric Ozone (NARSTO) Environmental Protection Agency (EPA) Supersite (SS) Los Angeles Particulate Matter (PM) 2.5-10 Composition and Mass Data product. Data was collected using Partisol Model 2025-D samplers between late 2000 and late 2003 from sites at Downey, Claremont, Riverside, Rubidoux, and the University of Southern California (USC). Samples were collected episodically, frequently for a 24-hour per period, but in some cases multiple samples were collected over the course of a day. Element/metals, nitrate/sulfate ion, and mass concentration data were obtained. The Partisol is a dichotomous sequential multi-filter air sampler. It uses a virtual impactor to divide the air stream to facilitate the collection of fine (0.0-2.5um) and coarse (2.5-10.0um) particles onto a filter media over a pre-programmed collection period. The coarse fraction was analyzed using X-ray fluorescence and mass concentration analysis. Ion chromatography and mass concentration analyses were performed on the fine fraction. The overall objective of the Southern California Supersite (SCS) was to conduct research and monitoring that contributed to a better understanding of the measurement, sources, size distribution, chemical composition, physical state, spatial and temporal variability, and health effects of suspended PM in the Los Angeles Basin (LAB). Intensive aerosol measurements, well beyond the traditional PM2.5 mass, sulfate and nitrate concentrations, were conducted in several areas of the LAB. These included particle number concentrations, size distributions, and detailed PM chemical composition as a function of particle size. Sampling locations were chosen to provide wide geographical and seasonal coverage, including urban source sites and downwind receptor sites. \r\n\r\nThe primary sampling facility, a mobile Particle Instrumentation Unit (PIU), was deployed to several locations to conduct a wide range of PM measurements. Sampling in each site lasted for 6-12 months. Intensive PM measurements were also conducted up and downwind of several freeways of the LAB, to characterize near-roadway exposure environments and to support several in vivo and in vitro health studies. The monitoring activities of the SCS were linked with toxicology studies in the LAB using a mobile PM Concentrator facility to investigate health effects associated with exposures to ultrafine, fine and coarse particles. Finally, the PIU facility was successfully used as a platform to develop, test, and evaluate numerous PM measurement instruments and sampling technologies, including several monitors for semi-continuous size fractionated mass and chemistry, personal PM exposure monitors, particle concentration technologies, and particle counting devices.\r\n\r\nNARSTO, which has since disbanded, was a public/private partnership, whose membership spanned across government, utilities, industry, and academe throughout Mexico, the United States, and Canada. The primary mission was to coordinate and enhance policy-relevant scientific research and assessment of tropospheric pollution behavior; activities provide input for science-based decision-making and determination of workable, efficient, and effective strategies for local and regional air-pollution management. Data products from local, regional, and international monitoring and research programs are still available.",
-            "title": "NARSTO EPA Supersite (SS) Los Angeles Particulate Matter (PM) 2.5-10 Composition and Mass Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDCDAAC%2FNARSTO%2F0030",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDCDAAC%2FNARSTO%2F0030",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2338659983-LARC_ASDC",
-                    "description": "Earthdata Search for NARSTO_EPA_SS_LOS_ANGELES_PARTISOL_DATA_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for NARSTO_EPA_SS_LOS_ANGELES_PARTISOL_DATA_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2338659983-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0030",
-                    "description": "DOI data set landing page for NARSTO_EPA_SS_LOS_ANGELES_PARTISOL_DATA_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for NARSTO_EPA_SS_LOS_ANGELES_PARTISOL_DATA_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0030",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/guide/narsto_epa_ss_los_angeles_partisol_data.pdf",
-                    "description": "Guide for NARSTO EPA_SS_LOS_ANGELES PM2.5-10 Composition and Mass Data (Partisol)",
                     "@type": "dcat:Distribution",
+                    "description": "Guide for NARSTO EPA_SS_LOS_ANGELES PM2.5-10 Composition and Mass Data (Partisol)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/guide/narsto_epa_ss_los_angeles_partisol_data.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/EPA_SS_Los_Angeles_Final_Report.pdf",
-                    "description": "Executive Summary for the Southern California Supersite (EPA: CR-82805901) Final Report \u2013 March 30, 2005",
                     "@type": "dcat:Distribution",
+                    "description": "Executive Summary for the Southern California Supersite (EPA: CR-82805901) Final Report \u2013 March 30, 2005",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/EPA_SS_Los_Angeles_Final_Report.pdf",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/NARSTO/EPA_SS_LOS_ANGELES_PARTISOL_DATA_1/",
-                    "description": "ASDC Direct Data Download for NARSTO_EPA_SS_LOS_ANGELES_PARTISOL_DATA_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for NARSTO_EPA_SS_LOS_ANGELES_PARTISOL_DATA_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/NARSTO/EPA_SS_LOS_ANGELES_PARTISOL_DATA_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2338659983-LARC_ASDC",
+            "issued": "2011-08-25",
+            "keyword": [
+                "atmospheric chemistry",
+                "aerosols",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0030",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>33.93 -118.16 33.93 -117.33 34.13 -117.33 34.13 -118.16 33.93 -118.16</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2000-10-03T00:00:00Z/2003-09-19T23:59:59.999Z",
             "theme": [
                 "NARSTO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NARSTO EPA Supersite (SS) Los Angeles Particulate Matter (PM) 2.5-10 Composition and Mass Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-MAG-4-48.0SEC",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set includes Voyager 2 Saturn encounter magnetometer data that have been resampled at a 48.0 second sample rate. The data set is composed of 6 columns: 1) ctime - this column contains the data acquisition time. The time is always output in the ISO standard spacecraft event time format (yyyy-mm-dd-Thh:mm:ss.sss) but is stored internally in Cline time which is measured in seconds after 00:00:00.000 Jan 01, 1966, 2) br - this column contains the radial component of the magnetic field, 3) bphi - this column contains the phi component of the magnetic field, 4) btheta - this column contains the theta component of the magnetic field, 5) bmag - this column contains the magnitude of the magnetic field, 6) flag - a flag value that indicates either software error or spacecraft hardware interference reduced confidence in this record (flag value of 1 is bad , 0 is good or unchecked). All magnetic field observations are measured in nanoTeslas. The coordinate system for this dataset is Minus Saturn Longitude System (-SLS). All of the magnetic field data are calibrated (see the instrument calibration description for more details). The SLS coordinate system is defined in Desch and Kaiser, 1981 and the reference documents for this dataset are: Ness et al, 1982 Acuna,Connerney,and Ness, 1983 Connerney,Acuna,and Ness, 1983 Behannon,Lepping,and Ness, 1983",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-mag-4-48.0sec_jt2x-yfw9",
             "issued": "2021-05-21",
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
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-MAG-4-48.0SEC",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-mag-4-48.0sec_jt2x-yfw9",
-            "description": "This data set includes Voyager 2 Saturn encounter magnetometer data that have been resampled at a 48.0 second sample rate. The data set is composed of 6 columns: 1) ctime - this column contains the data acquisition time. The time is always output in the ISO standard spacecraft event time format (yyyy-mm-dd-Thh:mm:ss.sss) but is stored internally in Cline time which is measured in seconds after 00:00:00.000 Jan 01, 1966, 2) br - this column contains the radial component of the magnetic field, 3) bphi - this column contains the phi component of the magnetic field, 4) btheta - this column contains the theta component of the magnetic field, 5) bmag - this column contains the magnitude of the magnetic field, 6) flag - a flag value that indicates either software error or spacecraft hardware interference reduced confidence in this record (flag value of 1 is bad , 0 is good or unchecked). All magnetic field observations are measured in nanoTeslas. The coordinate system for this dataset is Minus Saturn Longitude System (-SLS). All of the magnetic field data are calibrated (see the instrument calibration description for more details). The SLS coordinate system is defined in Desch and Kaiser, 1981 and the reference documents for this dataset are: Ness et al, 1982 Acuna,Connerney,and Ness, 1983 Connerney,Acuna,and Ness, 1983 Behannon,Lepping,and Ness, 1983",
-            "title": "VOYAGER 2 SATURN MAGNETOMETER RESAMPLED DATA 48.0 SEC",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VOYAGER 2 SATURN MAGNETOMETER RESAMPLED DATA 48.0 SEC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MRO-M-CRISM-5-RDR-MULTISPECTRAL-V1.0",
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
-                "mars reconnaissance orbiter"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains CRISM Multispectral Reduced Data Records (MRDRs). MRDRs are organized into 30 subdirectories named by the Mars Chart containing the MRDR, e.g. MC01. Latitude and longitude limits of Mars Charts are given below. An MRDR consists of several or more strips of multispectral survey data mosaicked into a map tile. Thus a map tile is constructed from a large number of TRDRs. The mosaic is uncontrolled (accepting existing pointing data often resulting in image mismatch at seams within a mosaic). The tile contains up to four images: radiance extracted from temporary TRDRs Lambert albedo summary products DDR data used to generate the first three images, augmented with additional positional information The MRDR also contains up to two text files, one listing the wavelengths present and ther other listing the SPICE metakernels used for map projection of each constituent observation on the tile. Each file has a separate label. For every latitude or longitude in an MRDR, there is a radiance and all the information providing traceability to through I/F to Lambert albedo corrected for atmospheric, photometric, and thermal emission effects, plus the information needed to reconstruct the map projection. A global pattern of 1964 such tiles is being used, forming the major data product for multispectral survey observations. Multiple MRDRs are in each of the 30 subdirectories.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mro-m-crism-5-rdr-multispectral-v1.0_jt3b-3x4g",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars reconnaissance orbiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MRO-M-CRISM-5-RDR-MULTISPECTRAL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mro-m-crism-5-rdr-multispectral-v1.0_jt3b-3x4g",
-            "description": "This dataset contains CRISM Multispectral Reduced Data Records (MRDRs). MRDRs are organized into 30 subdirectories named by the Mars Chart containing the MRDR, e.g. MC01. Latitude and longitude limits of Mars Charts are given below. An MRDR consists of several or more strips of multispectral survey data mosaicked into a map tile. Thus a map tile is constructed from a large number of TRDRs. The mosaic is uncontrolled (accepting existing pointing data often resulting in image mismatch at seams within a mosaic). The tile contains up to four images: radiance extracted from temporary TRDRs Lambert albedo summary products DDR data used to generate the first three images, augmented with additional positional information The MRDR also contains up to two text files, one listing the wavelengths present and ther other listing the SPICE metakernels used for map projection of each constituent observation on the tile. Each file has a separate label. For every latitude or longitude in an MRDR, there is a radiance and all the information providing traceability to through I/F to Lambert albedo corrected for atmospheric, photometric, and thermal emission effects, plus the information needed to reconstruct the map projection. A global pattern of 1964 such tiles is being used, forming the major data product for multispectral survey observations. Multiple MRDRs are in each of the 30 subdirectories.",
-            "title": "MRO CRISM MULTISPECTRAL REDUCED DATA\n                                     RECORD V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MRO CRISM MULTISPECTRAL REDUCED DATA\n                                     RECORD V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/IVM9SK5USQOS",
             "citation": "AIRS Science Team (Joel Susskind, NASA/GSFC). 2013-01-15. AIRG2SSD_IRonly. Version 006. AIRS/Aqua L2G Precipitation Estimate (AIRS-only) V006. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/IVM9SK5USQOS. https://disc.gsfc.nasa.gov/datacollection/AIRG2SSD_IRonly_006.html. Digital Science Data.",
-            "issued": "2002-08-30",
-            "temporal": "2002-08-30T00:00:00Z/2025-01-13T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-10",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "clouds",
-                "precipitation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ED ESFANDIARI",
                 "hasEmail": "mailto:asghar.e.esfandiari@nasa.gov"
             },
+            "creator": "AIRS Science Team (Joel Susskind, NASA/GSFC)",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1618076955-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The Atmospheric Infrared Sounder (AIRS) is a grating spectrometer (R = 1200) aboard the second Earth Observing System (EOS) polar-orbiting platform, EOS Aqua. This precipitation estimate from AIRS IR only is using a TOVS-like algorithm, and is intended for merging into the precipitation product of the Global Precipitation Climatology Project (GPCP). The precipitation estimate from AIRS Level 2 Support product, which are 6-min swath granules (240 per day) are combined here into one daily \"Level 2G\" global grid with dimensions (24x1440x720). Thus every hour is a \"layer\", and the resulting grid cell size is 0.25 degree (~25 km). Thus the grid size is made to fit TRMM products. Since AIRS precipitation is retrieved at AMSU footprint resolution, which is about 45 km at nadir, many grid cells in this 0.25-deg grid are \"empty\". The data are stored such that the first line is the South Pole. The geolocation information for every hour-layer is also provided in the file.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "AIRG2SSD_IRonly",
-            "creator": "AIRS Science Team (Joel Susskind, NASA/GSFC)",
-            "title": "AIRS/Aqua L2G Precipitation Estimate (AIRS-only) V006 (AIRG2SSD_IRonly) at GES DISC",
-            "graphic-preview-description": "Sample image for layer 19 of the precipitation estimate from AIRS Level 2 Support product combined into one daily \"Level 2G\" global grid with dimensions (24x1440x720).  Every hour is a \"layer\", and the resulting grid cell size is 0.25 degree (~25 km).",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRG2SSD_006.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIVM9SK5USQOS",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIVM9SK5USQOS",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRG2SSD_006.png",
-                    "description": "Sample image for layer 19 of the precipitation estimate from AIRS Level 2 Support product combined into one daily \"Level 2G\" global grid with dimensions (24x1440x720).  Every hour is a \"layer\", and the resulting grid cell size is 0.25 degree (~25 km).",
                     "@type": "dcat:Distribution",
+                    "description": "Sample image for layer 19 of the precipitation estimate from AIRS Level 2 Support product combined into one daily \"Level 2G\" global grid with dimensions (24x1440x720).  Every hour is a \"layer\", and the resulting grid cell size is 0.25 degree (~25 km).",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRG2SSD_006.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRG2SSD_IRonly_006.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRG2SSD_IRonly_006.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://airsl2.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level2/AIRG2SSD_IRonly.006/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://airsl2.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level2/AIRG2SSD_IRonly.006/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://airsl2.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level2/AIRG2SSD_IRonly.006/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://airsl2.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level2/AIRG2SSD_IRonly.006/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRG2SSD_IRonly+006",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRG2SSD_IRonly+006",
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
-                    "description": "ATBD",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD",
+                    "downloadURL": "https://eospso.gsfc.nasa.gov/sites/default/files/atbd/20070301_L2_ATBD_signed.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 }
             ],
+            "graphic-preview-description": "Sample image for layer 19 of the precipitation estimate from AIRS Level 2 Support product combined into one daily \"Level 2G\" global grid with dimensions (24x1440x720).  Every hour is a \"layer\", and the resulting grid cell size is 0.25 degree (~25 km).",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRG2SSD_006.png",
+            "identifier": "C1618076955-GES_DISC",
+            "issued": "2002-08-30",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "clouds",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.5067/IVM9SK5USQOS",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-10",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "AIRG2SSD_IRonly",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-08-30T00:00:00Z/2025-01-13T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AIRS/Aqua L2G Precipitation Estimate (AIRS-only) V006 (AIRG2SSD_IRonly) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TIGR19-V1.0",
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
-                "titan",
-                "cassini-huygens"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Cassini LGA Radio Science Titan Gravity Science Experiment (TIGR19) Raw Data Archive is a time-ordered collection of radio science raw data acquired on March 16, 2015, during the Cassini Extended Extended Mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tigr19-v1.0_jt5s-7fw9",
+            "issued": "2018-06-26",
+            "keyword": [
+                "titan",
+                "cassini-huygens"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TIGR19-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tigr19-v1.0_jt5s-7fw9",
-            "description": "The Cassini LGA Radio Science Titan Gravity Science Experiment (TIGR19) Raw Data Archive is a time-ordered collection of radio science raw data acquired on March 16, 2015, during the Cassini Extended Extended Mission.",
-            "title": "CASSINI RSS RAW DATA SET - TIGR19 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI RSS RAW DATA SET - TIGR19 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-ENG-6-RMC-OPS-V1.0",
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
-                "mars exploration rover",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This archive contains position and orientation information for various \ncoordinate systems indexed by the Rover Motion Counter (RMC).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-eng-6-rmc-ops-v1.0_jt8q-z9s2",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars exploration rover",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-ENG-6-RMC-OPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-eng-6-rmc-ops-v1.0_jt8q-z9s2",
-            "description": "This archive contains position and orientation information for various \ncoordinate systems indexed by the Rover Motion Counter (RMC).",
-            "title": "MER 2 MARS ENGINEERING ROVER MOTION\n                                      COUNTER OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MER 2 MARS ENGINEERING ROVER MOTION\n                                      COUNTER OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/jtb5-j87z",
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
+                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_lid_l2_05kmcpro-prov-v2-02_table",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000176",
             "issued": "2018-06-25",
-            "temporal": "2008-09-14/2010-03-28",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "radiation",
                 "aerosol",
@@ -995565,328 +995576,329 @@
                 "cloud",
                 "satellite"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John M. Kusterer",
-                "hasEmail": "mailto:john.m.kusterer@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/jtb5-j87z",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:004"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000176",
-            "description": "Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) was launched on April 28, 2006 to study the impact of clouds and aerosols on the Earth\u2019s radiation budget and climate. It flies in formation with five other satellites in the international \u201cA-Train\u201d (PDF) constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments, the Cloud-Aerosol LIdar with Orthogonal Polarization (CALIOP), the Imaging Infrared Radiometer (IIR), and the Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES. These data consist 5 km aerosol layer data.",
-            "title": "CALIPSO Lidar L2 5 km Cloud Profile Data V2-02",
-            "programCode": [
-                "026:004"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_lid_l2_05kmcpro-prov-v2-02_table",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
+            "temporal": "2008-09-14/2010-03-28",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CALIPSO Lidar L2 5 km Cloud Profile Data V2-02"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/OYF98UGSOUQY",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SnowEx Mores Creek Summit (MCS) Airborne LiDAR Survey Raw V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/OYF98UGSOUQY.",
-            "issued": "2022-02-17",
-            "temporal": "2021-03-10T00:00:00Z/2024-04-18T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-18",
-            "keyword": [
-                "earth science",
-                "spectral/engineering",
-                "lidar"
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
-            "identifier": "C3267588841-NSIDC_ECS",
             "description": "The data set described here provides raw lidar data collected as part of a multi-year effort to monitor monthly snow distribution over a 35 km\u00b2 region of the Mores Creek Headwaters in the Boise Mountains of central Idaho between 2021 and 2024. Data acquisition in 2021 overlapped temporally with the NASA SnowEx 2021 field campaign. \n\nDigital terrain models (DTM), digital surface models (DSM) snow depth models, and canopy height models (CHM) derived from these point cloud data are available as <a href=\"https://nsidc.org/data/SNEX_MCS_Lidar\">SnowEx Mores Creek Summit (MCS) Airborne LiDAR Survey, Version 1</a>.",
-            "title": "SnowEx Mores Creek Summit (MCS) Airborne LiDAR Survey Raw V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FOYF98UGSOUQY",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FOYF98UGSOUQY",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX_MCS_Lidar_Raw.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX_MCS_Lidar_Raw.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX_MCS_Lidar_Raw+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX_MCS_Lidar_Raw+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX_MCS_Lidar_Raw/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX_MCS_Lidar_Raw/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/OYF98UGSOUQY",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/OYF98UGSOUQY",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/OYF98UGSOUQY",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/OYF98UGSOUQY",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C3267588841-NSIDC_ECS",
+            "issued": "2022-02-17",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "lidar"
+            ],
+            "landingPage": "https://doi.org/10.5067/OYF98UGSOUQY",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-04-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-115.7304987 43.9136453 -115.6424377 43.9748021",
+            "temporal": "2021-03-10T00:00:00Z/2024-04-18T23:59:59.999Z",
             "theme": [
                 "SnowEx",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SnowEx Mores Creek Summit (MCS) Airborne LiDAR Survey Raw V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-E-PPR-2-EDR-EARTH2-V1.0",
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
-                "galileo"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains the R_EDR data for the Galileo Orbiter PPR instrument for the period corresponding to the Earth-2 encounter observations in November-December 1992.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-e-ppr-2-edr-earth2-v1.0_jte3-4it8",
+            "issued": "2021-05-21",
+            "keyword": [
+                "earth",
+                "galileo"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-E-PPR-2-EDR-EARTH2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-e-ppr-2-edr-earth2-v1.0_jte3-4it8",
-            "description": "This data set contains the R_EDR data for the Galileo Orbiter PPR instrument for the period corresponding to the Earth-2 encounter observations in November-December 1992.",
-            "title": "GLL PPR EARTH-2 ENCOUNTER EDR",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GLL PPR EARTH-2 ENCOUNTER EDR"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-SWAP-5-DERIVED-SOLARWIND-V1.0",
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
-                "new horizons"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set presents characteristics of the solar wind derived from     the New Horizons Solar Wind Around Pluto (SWAP) experiment from           observations obtained during cruise, Pluto encounter (excluding the       period inside the Pluto system), and afterwards. The single data file     the time information for a given pair of sweeps, original level 2         data file reference, the solar wind speed proton density, proton          speed, proton temperature, proton dynamic pressure, proton thermal        pressure, spacecraft position and speed in Heliographic Inertial          (HGI), Heliocentric Aries ecliptic, and Heliographic (Carrington)         coordinates.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-swap-5-derived-solarwind-v1.0_jtju-r7m5",
+            "issued": "2018-09-05",
+            "keyword": [
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-SWAP-5-DERIVED-SOLARWIND-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-swap-5-derived-solarwind-v1.0_jtju-r7m5",
-            "description": "This data set presents characteristics of the solar wind derived from     the New Horizons Solar Wind Around Pluto (SWAP) experiment from           observations obtained during cruise, Pluto encounter (excluding the       period inside the Pluto system), and afterwards. The single data file     the time information for a given pair of sweeps, original level 2         data file reference, the solar wind speed proton density, proton          speed, proton temperature, proton dynamic pressure, proton thermal        pressure, spacecraft position and speed in Heliographic Inertial          (HGI), Heliocentric Aries ecliptic, and Heliographic (Carrington)         coordinates.",
-            "title": "NEW HORIZONS SWAP SOLAR WIND DERIVED CHARACTERISTICS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS SWAP SOLAR WIND DERIVED CHARACTERISTICS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D73.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler\r\n. 2019-11-07. VNP43D73. Version 001. VIIRS/NPP BRDF/Albedo WSA at Solar Noon Band M8 Daily L3 Global 30ArcSec CMG V001\r\n. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VNP43D73.001. https://doi.org/10.5067/VIIRS/VNP43D73.001. Digital Science Data. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
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
-            "identifier": "C1607344635-LPDAAC_ECS",
-            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo white-sky albedo for band M8 (VNP43D73) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. \r\n\r\nVNP43D54 through VNP43D79 are the albedo products of the VNP43D BRDF/Albedo product suite. Black-sky albedo (BSA) and white-sky albedo (WSA) values are provided for the nine VIIRS moderate resolution bands (M1 through M5, M7, M8, M10, and M11) along with the visible, near-infrared (NIR), and shortwave bands included in the VNP43MA3 (https://doi.org/10.5067/VIIRS/VNP43MA3.001) product. In addition to the bands included in VNP43MA3, this product suite includes albedo values for the VIIRS Day/Night Band (DNB). The black-sky albedo (directional hemispherical reflectance) is defined as albedo in the absence of a diffuse component and is a function of solar zenith angle. White-sky albedo (bihemispherical reflectance) is defined as albedo in the absence of a direct component when the diffuse component is isotropic. Details regarding methodology are available on the VNP43MA3 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D73 is the WSA for VIIRS band M8 (1.240 \u03bcm).",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "VNP43D73",
             "creator": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler",
-            "title": "VIIRS/NPP BRDF/Albedo WSA at Solar Noon Band M8 Daily L3 Global 30ArcSec CMG V001",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo white-sky albedo for band M8 (VNP43D73) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. \r\n\r\nVNP43D54 through VNP43D79 are the albedo products of the VNP43D BRDF/Albedo product suite. Black-sky albedo (BSA) and white-sky albedo (WSA) values are provided for the nine VIIRS moderate resolution bands (M1 through M5, M7, M8, M10, and M11) along with the visible, near-infrared (NIR), and shortwave bands included in the VNP43MA3 (https://doi.org/10.5067/VIIRS/VNP43MA3.001) product. In addition to the bands included in VNP43MA3, this product suite includes albedo values for the VIIRS Day/Night Band (DNB). The black-sky albedo (directional hemispherical reflectance) is defined as albedo in the absence of a diffuse component and is a function of solar zenith angle. White-sky albedo (bihemispherical reflectance) is defined as albedo in the absence of a direct component when the diffuse component is isotropic. Details regarding methodology are available on the VNP43MA3 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D73 is the WSA for VIIRS band M8 (1.240 \u03bcm).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D73.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D73.001",
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
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D73.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D73.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/xhdf5",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D73.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D73.001/",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607344635-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607344635-LPDAAC_ECS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D73.001/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D73.001/contents.html",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D73",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D73",
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
+            "identifier": "C1607344635-LPDAAC_ECS",
+            "issued": "2019-11-07",
+            "keyword": [
+                "surface radiative properties",
+                "earth science",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D73.001",
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
+            "series-name": "VNP43D73",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-19T00:00:00Z/2024-05-27T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP BRDF/Albedo WSA at Solar Noon Band M8 Daily L3 Global 30ArcSec CMG V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/jtnt-s6ha",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Dan Irwin",
+                "hasEmail": "mailto:dan.irwin@nasa.gov"
+            },
+            "description": "SERVIR is a Spanish acronym for 'Regional Visualization and Monitoring System.' The&#160;SERVIR project enables the use of Earth observations and predictive models for timely decision making through regional platforms in Mesoamerica, East Africa, and the Hindu-Kush Himalayas. &#160;The SERVIR project was initially developed by NASA, the US Agency for International Development, the World Bank, the Central American Commission for Environment and Development (CCAD), and the Water Center for the Humid Tropics of Latin America and the Caribbean (CATHALAC) in 2005. &#160; In 2008, the Regional Center for Mapping of Resources for Development (RCMRD) in Nairobi, Kenya, joined the SERVIR project, and in 2010, SERVIR inaugurated its third hub at the International Centre for Integrated Mountain Development (ICIMOD) in Kathmandu, Nepal. &#160; SERVIR also stands for the Spanish verb 'to serve,' which is what the project aims to do in terms of providing improved access to data and knowledge for decision-making.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.servirglobal.net/Global/MapsData.aspx",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000107",
             "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "earth science",
                 "climate",
@@ -995902,435 +995914,404 @@
                 "panorama",
                 "mesoamerica"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Dan Irwin",
-                "hasEmail": "mailto:dan.irwin@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/jtnt-s6ha",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000107",
-            "description": "SERVIR is a Spanish acronym for 'Regional Visualization and Monitoring System.' The&#160;SERVIR project enables the use of Earth observations and predictive models for timely decision making through regional platforms in Mesoamerica, East Africa, and the Hindu-Kush Himalayas. &#160;The SERVIR project was initially developed by NASA, the US Agency for International Development, the World Bank, the Central American Commission for Environment and Development (CCAD), and the Water Center for the Humid Tropics of Latin America and the Caribbean (CATHALAC) in 2005. &#160; In 2008, the Regional Center for Mapping of Resources for Development (RCMRD) in Nairobi, Kenya, joined the SERVIR project, and in 2010, SERVIR inaugurated its third hub at the International Centre for Integrated Mountain Development (ICIMOD) in Kathmandu, Nepal. &#160; SERVIR also stands for the Spanish verb 'to serve,' which is what the project aims to do in terms of providing improved access to data and knowledge for decision-making.",
-            "title": "SERVIR Data Catalog",
-            "programCode": [
-                "026:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.servirglobal.net/Global/MapsData.aspx",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular"
+            "title": "SERVIR Data Catalog"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4CC0XMD",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for International Earth Science Information Network - CIESIN - Columbia University. 2013-11-14. Sea Level Rise Impacts on Ramsar Wetlands of International Importance. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H4CC0XMD. https://doi.org/10.7927/H4CC0XMD.",
-            "issued": "2013-11-14",
-            "temporal": "2000-01-01T00:00:00Z/2010-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2013-11-14",
-            "references": [
-                "https://doi.org/10.7927/H4TM782G",
-                "https://doi.org/10.7927/H4MW2F2J"
-            ],
-            "keyword": [
-                "biosphere",
-                "ecosystems",
-                "earth science",
-                "climate indicators",
-                "atmospheric/ocean indicators"
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
-            "identifier": "C1000000260-SEDAC",
-            "description": "The Sea Level Rise Impacts on Ramsar Wetlands of International Importance data set represents the results of an analysis using the boundaries for Ramsar sites designated under the Ramsar Convention on Wetlands and intersecting them with different elevation zones in the coastal zone to assess area and percent area that would become inundated under 1 and 2 meter sea level rise scenarios. This data set provides results for 613 sites with defined boundaries that were found to intersect with the 0-5m above mean sea level coastal zone, defined by NASA Shuttle Radar Topography Mission (SRTM) elevation data. In addition to assessing the degree of risk of inundation, the data set provides population density and percent of land that is urban within the site and within 1km and 5km buffers surrounding the site. The data set also reports on infant mortality rates within 1km and 5km buffers around the site, as a measure of poverty levels that may affect adaptive capacity.",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Center for International Earth Science Information Network - CIESIN - Columbia University",
-            "title": "Sea Level Rise Impacts on Ramsar Wetlands of International Importance",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/lecz/lecz-slr-impacts-ramsar-wetlands/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Sea Level Rise Impacts on Ramsar Wetlands of International Importance data set represents the results of an analysis using the boundaries for Ramsar sites designated under the Ramsar Convention on Wetlands and intersecting them with different elevation zones in the coastal zone to assess area and percent area that would become inundated under 1 and 2 meter sea level rise scenarios. This data set provides results for 613 sites with defined boundaries that were found to intersect with the 0-5m above mean sea level coastal zone, defined by NASA Shuttle Radar Topography Mission (SRTM) elevation data. In addition to assessing the degree of risk of inundation, the data set provides population density and percent of land that is urban within the site and within 1km and 5km buffers surrounding the site. The data set also reports on infant mortality rates within 1km and 5km buffers around the site, as a measure of poverty levels that may affect adaptive capacity.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4CC0XMD",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4CC0XMD",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/lecz/lecz-slr-impacts-ramsar-wetlands/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/lecz/lecz-slr-impacts-ramsar-wetlands/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/lecz-slr-impacts-ramsar-wetlands/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/lecz-slr-impacts-ramsar-wetlands/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/lecz-slr-impacts-ramsar-wetlands/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/lecz-slr-impacts-ramsar-wetlands/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/lecz-slr-impacts-ramsar-wetlands/maps/services",
-                    "description": "Web Map Service Page",
                     "@type": "dcat:Distribution",
+                    "description": "Web Map Service Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/lecz-slr-impacts-ramsar-wetlands/maps/services",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/lecz-slr-impacts-ramsar-wetlands",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/lecz-slr-impacts-ramsar-wetlands",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/lecz/lecz-slr-impacts-ramsar-wetlands/sedac-logo.jpg",
+            "identifier": "C1000000260-SEDAC",
+            "issued": "2013-11-14",
+            "keyword": [
+                "biosphere",
+                "ecosystems",
+                "earth science",
+                "climate indicators",
+                "atmospheric/ocean indicators"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4CC0XMD",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2013-11-14",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H4TM782G",
+                "https://doi.org/10.7927/H4MW2F2J"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -58.0 180.0 85.0",
+            "temporal": "2000-01-01T00:00:00Z/2010-12-31T00:00:00Z",
             "theme": [
                 "LECZ",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sea Level Rise Impacts on Ramsar Wetlands of International Importance"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-PLS-5-ION-FBR-96.0SEC",
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
+            "description": "THIS DATA SET CONTAINS THE ION DENSITIES, TEMPERATURES, AND VELOCITIES OBTAINED FROM VOYAGER 1 PLS DATA (VOLTAGE RANGE 10-5950 EV/Q) AT SATURN BY FITTING THE MEASURED SPECTRA WITH ISOTROPIC MAXWELLIAN DISTRIBUTIONS. IT IS A SUBSET OF THE DATA SET VG1-S-PLS-5-ION-FIT-96.0SEC WHICH SHOULD BE OBTAINED BEFORE THIS DATA IS USED. ONLY SPECTRA WHICH HAD DISTINCT CURRENT PEAKS WERE FIT. SPECTRA WERE FIT USING ONE OR TWO ION SPECIES, PROTONS AND/OR A HEAVY ION WHICH WAS TAKEN TO BE OXYGEN. OUTSIDE L=10-12 ION SPECTRA CHANGE RAPIDLY, SO THE VALUES IN THIS DATA SET DO NOT REPRESENT AVERAGE PLASMA CONDITIONS IN THE OUTER MAGNETOSPHERE. A COMPLETE DESCRIPTION OF THIS DATA SET IS GIVEN IN RICHARDSON (1986). DATA FORMAT: FIRST 5 COLUMNS ARE TIME TAG (YEAR, DAY, HOUR, MIN SEC.MSEC), FOLLOWED BY PROTON DENSITY (CM-3), PROTON TEMPERATURE (EV), HEAVY ION DENSITY (CM-3), HEAVY ION TEMPERATURE (EV), AND THREE VELOCITY COMPONENTS, (RHO, PHI,Z) IN KM/S. A CYLINDRICAL COORDINATE SYSTEM CENTERED ON THE PLANET IS USED, WITH RHO OUTWARDS FROM THE SPIN AXIS, PHI IN THE DIRECTION OF ROTATION, AND Z THE DISTANCE ABOVE THE EQUATOR. EACH ROW HAS THE FORMAT (2I4,2I3,F7.3,7E11.3). VALUES OF 1.E32 INDICATE THAT THE PARAMETER COULD NOT BE OBTAINED FROM THE DATA USING THE STANDARD ANALYSIS TECHNIQUE. ADDITIONAL INFORMATION ABOUT THIS DATASET AND THE INSTRUMENT WHICH PRODUCED IT CAN BE FOUND ELSEWHERE IN THIS CATALOG. AN OVERVIEW OF THE DATA IN THIS DATA SET CAN BE FOUND IN RICHARDSON (1986) AND A COMPLETE INSTRUMENT DESCRIPTION CAN BE FOUND IN BRIDGE (1977).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-pls-5-ion-fbr-96.0sec_jtq3-km7q",
+            "issued": "2021-05-21",
+            "keyword": [
+                "saturn",
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-PLS-5-ION-FBR-96.0SEC",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-pls-5-ion-fbr-96.0sec_jtq3-km7q",
-            "description": "THIS DATA SET CONTAINS THE ION DENSITIES, TEMPERATURES, AND VELOCITIES OBTAINED FROM VOYAGER 1 PLS DATA (VOLTAGE RANGE 10-5950 EV/Q) AT SATURN BY FITTING THE MEASURED SPECTRA WITH ISOTROPIC MAXWELLIAN DISTRIBUTIONS. IT IS A SUBSET OF THE DATA SET VG1-S-PLS-5-ION-FIT-96.0SEC WHICH SHOULD BE OBTAINED BEFORE THIS DATA IS USED. ONLY SPECTRA WHICH HAD DISTINCT CURRENT PEAKS WERE FIT. SPECTRA WERE FIT USING ONE OR TWO ION SPECIES, PROTONS AND/OR A HEAVY ION WHICH WAS TAKEN TO BE OXYGEN. OUTSIDE L=10-12 ION SPECTRA CHANGE RAPIDLY, SO THE VALUES IN THIS DATA SET DO NOT REPRESENT AVERAGE PLASMA CONDITIONS IN THE OUTER MAGNETOSPHERE. A COMPLETE DESCRIPTION OF THIS DATA SET IS GIVEN IN RICHARDSON (1986). DATA FORMAT: FIRST 5 COLUMNS ARE TIME TAG (YEAR, DAY, HOUR, MIN SEC.MSEC), FOLLOWED BY PROTON DENSITY (CM-3), PROTON TEMPERATURE (EV), HEAVY ION DENSITY (CM-3), HEAVY ION TEMPERATURE (EV), AND THREE VELOCITY COMPONENTS, (RHO, PHI,Z) IN KM/S. A CYLINDRICAL COORDINATE SYSTEM CENTERED ON THE PLANET IS USED, WITH RHO OUTWARDS FROM THE SPIN AXIS, PHI IN THE DIRECTION OF ROTATION, AND Z THE DISTANCE ABOVE THE EQUATOR. EACH ROW HAS THE FORMAT (2I4,2I3,F7.3,7E11.3). VALUES OF 1.E32 INDICATE THAT THE PARAMETER COULD NOT BE OBTAINED FROM THE DATA USING THE STANDARD ANALYSIS TECHNIQUE. ADDITIONAL INFORMATION ABOUT THIS DATASET AND THE INSTRUMENT WHICH PRODUCED IT CAN BE FOUND ELSEWHERE IN THIS CATALOG. AN OVERVIEW OF THE DATA IN THIS DATA SET CAN BE FOUND IN RICHARDSON (1986) AND A COMPLETE INSTRUMENT DESCRIPTION CAN BE FOUND IN BRIDGE (1977).",
-            "title": "VOYAGER 1 SATURN PLASMA DERIVED ION FITS BROWSE 96 SEC",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VOYAGER 1 SATURN PLASMA DERIVED ION FITS BROWSE 96 SEC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-RAC-5-ROUGHNESS-OPS-V1.0",
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
+            "description": "The Robotic Arm Camera (RAC)  experiment on the Mars Phoenix Lander consists of one instrument  component plus command electronics. This RAC Imaging Operations RDR  data set contains roughness data from the Robotic Arm Camera (RAC).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-rac-5-roughness-ops-v1.0_jtra-gut2",
+            "issued": "2021-05-21",
+            "keyword": [
+                "phoenix",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-RAC-5-ROUGHNESS-OPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-rac-5-roughness-ops-v1.0_jtra-gut2",
-            "description": "The Robotic Arm Camera (RAC)  experiment on the Mars Phoenix Lander consists of one instrument  component plus command electronics. This RAC Imaging Operations RDR  data set contains roughness data from the Robotic Arm Camera (RAC).",
-            "title": "PHOENIX MARS ROBOTIC ARM CAMERA \n                                      5 ROUGHNESS OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "PHOENIX MARS ROBOTIC ARM CAMERA \n                                      5 ROUGHNESS OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/IMPACTS/NEXRAD/DATA127",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Brodzik, Stacy .2022. KPBZ NEXRAD IMPACTS [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/IMPACTS/NEXRAD/DATA127",
-            "issued": "2022-03-23",
-            "temporal": "2020-01-01T00:01:03Z/2020-03-01T00:01:48Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "radar",
-                "earth science",
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
-            "identifier": "C2020261956-GHRC_DAAC",
             "description": "The KPBZ NEXRAD IMPACTS dataset consists of Next Generation Weather Radar (NEXRAD) Level II surveillance data that were collected at 31 NEXRAD sites from January 1 to March 1, 2020 during the Investigation of Microphysics and Precipitation for Atlantic Coast-Threatening Snowstorms  (IMPACTS) field campaign. IMPACTS was a three-year sequence of winter season deployments conducted to study snowstorms over the U.S Atlantic Coast. The campaign aimed to (1) Provide observations critical to understanding the mechanisms of snowband formation, organization, and evolution; (2) Examine how the microphysical characteristics and likely growth mechanisms of snow particles vary across snowbands; and (3) Improve snowfall remote sensing interpretation and modeling to significantly advance prediction capabilities. There are currently 160 Weather Surveillance Radar-1988 Doppler (WSR-88D) or NEXRAD sites throughout the United States and abroad. These Level II datasets contain meteorological and dual-polarization base data quantities including: radar reflectivity, radial velocity, spectrum width, differential reflectivity, differential phase, and cross correlation ratio. The IMPACTS NEXRAD Level II data files are available in netCDF-4 format. It should be noted that this dataset will be updated in subsequent years of the IMPACTS campaign.",
-            "title": "KPBZ NEXRAD IMPACTS V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FNEXRAD%2FDATA127",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FNEXRAD%2FDATA127",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=kpbzimpacts",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=kpbzimpacts",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/uso/ds_details/collections/impactsC.html",
-                    "description": "IMPACTS Field Campaign Collection DOI",
                     "@type": "dcat:Distribution",
+                    "description": "IMPACTS Field Campaign Collection DOI",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/uso/ds_details/collections/impactsC.html",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/NEXRAD/KPBZ/doc/nexrad_datasets.pdf",
-                    "description": "NEXRAD IMPACTS User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "NEXRAD IMPACTS User Guide",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/NEXRAD/KPBZ/doc/nexrad_datasets.pdf",
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
+            "identifier": "C2020261956-GHRC_DAAC",
+            "issued": "2022-03-23",
+            "keyword": [
+                "radar",
+                "earth science",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/IMPACTS/NEXRAD/DATA127",
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
             "spatial": "-85.6552 36.4018 -74.7808 44.6616",
+            "temporal": "2020-01-01T00:01:03Z/2020-03-01T00:01:48Z",
             "theme": [
                 "IMPACTS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "KPBZ NEXRAD IMPACTS V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-C-HRII-3%2F4-EPOXI-HARTLEY2-V2.0",
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
-                "103p/hartley 2 (1986 e2)",
-                "epoxi"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains calibrated, 1.05- to 4.8-micron spectral images of comet 103/P Hartley 2 acquired by the High Resolution Infrared Spectrometer from 01 October through 26 November 2010 during the Hartley 2 encounter phase of the EPOXI mission. Version 2.0 includes the application of new per-pixel linearity and calibration files such flats, darks, and absolute calibration curves that were derived using the new linearization.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-c-hrii-3-4-epoxi-hartley2-v2.0_jts8-at8v",
+            "issued": "2021-05-21",
+            "keyword": [
+                "103p/hartley 2 (1986 e2)",
+                "epoxi"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-C-HRII-3%2F4-EPOXI-HARTLEY2-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-c-hrii-3-4-epoxi-hartley2-v2.0_jts8-at8v",
-            "description": "This dataset contains calibrated, 1.05- to 4.8-micron spectral images of comet 103/P Hartley 2 acquired by the High Resolution Infrared Spectrometer from 01 October through 26 November 2010 during the Hartley 2 encounter phase of the EPOXI mission. Version 2.0 includes the application of new per-pixel linearity and calibration files such flats, darks, and absolute calibration curves that were derived using the new linearization.",
-            "title": "EPOXI 103P/HARTLEY2 ENCOUNTER - HRII CALIBRATED SPECTRA V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "EPOXI 103P/HARTLEY2 ENCOUNTER - HRII CALIBRATED SPECTRA V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://data.giss.nasa.gov/stormtracks/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "temporal": "1961-01-01/1998-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "geodata",
-                "climate",
-                "weather",
-                "charts",
-                "storm tracking"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Mark Chandler",
                 "hasEmail": "mailto:mark.a.chandler@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-0000025__1",
+            "describedBy": "http://data.giss.nasa.gov/stormtracks/",
             "description": "Plotted images and a dataset for getting underlying coordinate data of extratropical storms.",
-            "title": "Atlas of Extratropical Storm Tracks",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -996338,22 +996319,50 @@
                     "mediaType": "application/octet-stream"
                 }
             ],
+            "identifier": "NASA-0000025__1",
+            "issued": "2018-06-25",
+            "keyword": [
+                "geodata",
+                "climate",
+                "weather",
+                "charts",
+                "storm tracking"
+            ],
+            "landingPage": "http://data.giss.nasa.gov/stormtracks/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
             "spatial": "Global",
-            "describedBy": "http://data.giss.nasa.gov/stormtracks/",
-            "accrualPeriodicity": "irregular"
+            "temporal": "1961-01-01/1998-01-01",
+            "title": "Atlas of Extratropical Storm Tracks"
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
+                    "downloadURL": "http://appel.nasa.gov/wp-content/uploads/sites/2/2013/04/352126main_Ares_I-X_Case_Study.pdf",
+                    "mediaType": "application/pdf"
+                }
             ],
+            "identifier": "NASA-865__7",
+            "issued": "2018-06-25",
             "keyword": [
                 "training",
                 "appel",
@@ -996362,615 +996371,582 @@
                 "management",
                 "sharing"
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
-            "identifier": "NASA-865__7",
-            "description": "Case studies illustrate the kinds of decisions and dilemmas managers face every day, and as such provide an effective learning tool for project management. Due to the dynamic and complex environment of projects, a great deal of project management knowledge is tacit and hard to formalize. A case study captures the complex nature of a project and identifies key decision points, allowing the reader an inside look at the project from a practitioner\u2019s point of view.",
-            "title": "Academy of Program/Project & Engineering Leadership: APPEL Case Studies",
-            "programCode": [
-                "026:045"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://appel.nasa.gov/wp-content/uploads/sites/2/2013/04/352126main_Ares_I-X_Case_Study.pdf",
-                    "mediaType": "application/pdf"
-                }
+            "references": [
+                "http://km.nasa.gov/knowledge-map/"
             ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "Academy of Program/Project & Engineering Leadership: APPEL Case Studies"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQR50-3UMAE",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA Aquarius project. 2017-12-07. Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Smoothed Standard Mapped Image Ascending Monthly Data. Version 5.0. Aquarius Sea Surface Salinity Products. Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC OBPG. https://doi.org/10.5067/AQR50-3UMAE. http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius. NASA Aquarius project, NASA/GSFC OBPG, 2017-12-07, Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Smoothed Standard Mapped Image Ascending Monthly Data V5.0, http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius.",
-            "issued": "2017-10-21",
-            "temporal": "2011-08-25T00:18:37Z/2015-06-07T11:41:38Z",
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
-            "identifier": "C2491756764-POCLOUD",
-            "description": "Aquarius Level 3 sea surface salinity (SSS) standard mapped image data contains gridded 1 degree spatial resolution SSS averaged over daily, 7 day, monthly, and seasonal time scales.\nThis particular data set is the Monthly, Ascending rain-flagged sea surface salinity smoothed product for version 5.0 of the Aquarius data set. Only retrieved values for Ascending passes have been used to create this product.  The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
-            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA",
-            "series-name": "Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Smoothed Standard Mapped Image Ascending Monthly Data",
-            "graphic-preview-description": "Thumbnail",
             "creator": "NASA Aquarius project",
-            "title": "Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Smoothed Standard Mapped Image Ascending Monthly Data V5.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS-RainFlagged_SM_SMIA_MONTHLY_V5.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Aquarius Level 3 sea surface salinity (SSS) standard mapped image data contains gridded 1 degree spatial resolution SSS averaged over daily, 7 day, monthly, and seasonal time scales.\nThis particular data set is the Monthly, Ascending rain-flagged sea surface salinity smoothed product for version 5.0 of the Aquarius data set. Only retrieved values for Ascending passes have been used to create this product.  The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3UMAE",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3UMAE",
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS-RainFlagged_SM_SMIA_MONTHLY_V5.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS-RainFlagged_SM_SMIA_MONTHLY_V5.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491756764-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491756764-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491756764-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491756764-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS-RainFlagged_SM_SMIA_MONTHLY_V5.jpg",
+            "identifier": "C2491756764-POCLOUD",
+            "issued": "2017-10-21",
+            "keyword": [
+                "oceans",
+                "earth science",
+                "salinity/density"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQR50-3UMAE",
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
+            "series-name": "Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Smoothed Standard Mapped Image Ascending Monthly Data",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T00:18:37Z/2015-06-07T11:41:38Z",
             "theme": [
                 "AQUARIUS SAC-D",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Smoothed Standard Mapped Image Ascending Monthly Data V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VJ202IMG.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "VCST Team. 2024-01-18. VIIRS/JPSS2 Imagery Resolution 6-Min L1B Swath 375 m. Version 2. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/VIIRS/VJ202IMG.002. https://doi.org/10.5067/VIIRS/VJ202IMG.002.",
-            "issued": "2023-09-25",
-            "temporal": "2023-02-10T00:00:00Z/2024-06-10T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-05",
-            "keyword": [
-                "infrared wavelengths",
-                "visible wavelengths",
-                "spectral/engineering",
-                "earth science"
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
-            "identifier": "C2839119522-LAADS",
-            "description": "The VIIRS/JPSS2 Imagery Resolution 6-Min L1B Swath 375m, short-name VJ202IMG is the Joint Polar-orbiting Satellite System-2 (JPSS-2/NOAA-21; referred to hereafter as J2) platform-derived NASA Visible Infrared Imaging Radiometer Suite (VIIRS) L1B calibrated radiances product that comprise five image-resolution or I-bands, which have a 375-meter resolution at nadir.  These I-bands comprise three reflective solar bands (RSB) and two thermal emissive bands (TEB).  Each of the I-bands has 32 detectors in the along-track direction with 32 rows of pixels per scan that offer a resolution that is twice finer than that of the moderate (M) and Day-Night bands (DNB).  Ranging in wavelengths from 0.6 \u00b5m to 12.4 \u00b5m, the I-bands are sensitive to visible/reflective, near-, shortwave-, mediumwave-, and longwave-infrared wavelengths.  \r\n\r\nThe J2 VIIRS radiometric calibration Level-1B reprocessing includes a few calibration updates for the reflective solar bands (RSB), but no significant changes for the day-night band (DNB) or thermal emissive bands (TEB). For more information and documents, visit LAADS product page at:\r\n\r\nhttps://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/products/VJ202IMG",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "VCST Team",
-            "title": "VIIRS/JPSS2 Imagery Resolution 6-Min L1B Swath 375 m",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The VIIRS/JPSS2 Imagery Resolution 6-Min L1B Swath 375m, short-name VJ202IMG is the Joint Polar-orbiting Satellite System-2 (JPSS-2/NOAA-21; referred to hereafter as J2) platform-derived NASA Visible Infrared Imaging Radiometer Suite (VIIRS) L1B calibrated radiances product that comprise five image-resolution or I-bands, which have a 375-meter resolution at nadir.  These I-bands comprise three reflective solar bands (RSB) and two thermal emissive bands (TEB).  Each of the I-bands has 32 detectors in the along-track direction with 32 rows of pixels per scan that offer a resolution that is twice finer than that of the moderate (M) and Day-Night bands (DNB).  Ranging in wavelengths from 0.6 \u00b5m to 12.4 \u00b5m, the I-bands are sensitive to visible/reflective, near-, shortwave-, mediumwave-, and longwave-infrared wavelengths.  \r\n\r\nThe J2 VIIRS radiometric calibration Level-1B reprocessing includes a few calibration updates for the reflective solar bands (RSB), but no significant changes for the day-night band (DNB) or thermal emissive bands (TEB). For more information and documents, visit LAADS product page at:\r\n\r\nhttps://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/products/VJ202IMG",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ202IMG.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ202IMG.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VJ202IMG.002",
-                    "description": "The product landing page",
                     "@type": "dcat:Distribution",
+                    "description": "The product landing page",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VJ202IMG.002",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/VJ202IMG--5200",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/VJ202IMG--5200",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/5200/VJ202IMG/",
-                    "description": "Direct access to VJ202IMG C2 data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to VJ202IMG C2 data set.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/5200/VJ202IMG/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/hyrax/allData/5200/VJ202IMG/contents.html",
-                    "description": "Direct access to product's OPeNDAP directory",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to product's OPeNDAP directory",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/hyrax/allData/5200/VJ202IMG/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2839119522-LAADS",
+            "issued": "2023-09-25",
+            "keyword": [
+                "infrared wavelengths",
+                "visible wavelengths",
+                "spectral/engineering",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VJ202IMG.002",
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
+            "temporal": "2023-02-10T00:00:00Z/2024-06-10T00:00:00Z",
             "theme": [
                 "JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/JPSS2 Imagery Resolution 6-Min L1B Swath 375 m"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RPCLAP-2-CVP1-EDITED2-V1.0",
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
-                "checkout",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains EDITED\ndata from Rosetta RPC-LAP, acquired during the COMMISSIONING 1 mission\nphase where there was no primary target. It contains uncalibrated raw\ndata, i.e. the digital output of the instrument.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rpclap-2-cvp1-edited2-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "checkout",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RPCLAP-2-CVP1-EDITED2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rpclap-2-cvp1-edited2-v1.0",
-            "description": "This data set contains EDITED\ndata from Rosetta RPC-LAP, acquired during the COMMISSIONING 1 mission\nphase where there was no primary target. It contains uncalibrated raw\ndata, i.e. the digital output of the instrument.",
-            "title": "ROSETTA-ORBITER CHECK RPCLAP\n2 CVP1 EDITED2 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECK RPCLAP\n2 CVP1 EDITED2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1338-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-13T16:56:55.000 to 2016-01-14T00:48:38.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1338-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1338-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1338-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-13T16:56:55.000 to 2016-01-14T00:48:38.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1338 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1338 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-A-SSI-3-GASPRA-CALIMAGES-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set includes Galileo Orbiter SSI radiometrically calibrated images of the asteroid 951 Gaspra, created using ISIS software and assuming nadir pointing. This is an original delivery of radiometrically calibrated files, not an update to existing files. All images archived include the the asteroid within the image frame. Calibration was performed in 2013-2014.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-a-ssi-3-gaspra-calimages-v1.0_ju49-sj6j",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "gaspra",
                 "galileo",
                 "951 gaspra"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-A-SSI-3-GASPRA-CALIMAGES-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-a-ssi-3-gaspra-calimages-v1.0_ju49-sj6j",
-            "description": "This data set includes Galileo Orbiter SSI radiometrically calibrated images of the asteroid 951 Gaspra, created using ISIS software and assuming nadir pointing. This is an original delivery of radiometrically calibrated files, not an update to existing files. All images archived include the the asteroid within the image frame. Calibration was performed in 2013-2014.",
-            "title": "GALILEO SSI/GASPRA RADIOMETRICALLY\n        CALIBRATED IMAGES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GALILEO SSI/GASPRA RADIOMETRICALLY\n        CALIBRATED IMAGES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/423/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2011-07-05",
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
-            "identifier": "DASHLINK_423",
             "description": "Information that was shared at the meetings held in Paris is located in this resource page\r\n\r\n<a href=\"http://www.sciencedirect.com/science?_ob=MImg&_imagekey=B6VK2-4TC925R-1-1&_cdi=6110&_user=141910&_pii=S1270963808000783&_origin=search&_zone=rslt_list_item&_coverDate=03%2F31%2F2009&_sk=999869997&wchp=dGLzVlb-zSkzV&md5=be385b276b917ea4c7c982a90fff7586&ie=/sdarticle.pdf\">Paper that was published in magazine</a> is linked directly",
-            "title": "RTA & IFASD June-July 2011",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/vnd.ms-powerpoint",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/HEEG_IFASD_v4a_2_2.ppt",
-                    "description": "summary paper presented at IFASD",
                     "@type": "dcat:Distribution",
+                    "description": "summary paper presented at IFASD",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/HEEG_IFASD_v4a_2_2.ppt",
+                    "mediaType": "application/vnd.ms-powerpoint",
                     "title": "HEEG_IFASD_v4a_2.ppt"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/IFASD_Panel_Discussion_v3_2.pdf",
-                    "description": "Lots of slides and details",
                     "@type": "dcat:Distribution",
+                    "description": "Lots of slides and details",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/IFASD_Panel_Discussion_v3_2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "IFASD_Panel_Discussion_v3.pdf"
                 },
                 {
-                    "mediaType": "application/vnd.ms-powerpoint",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Structural_Dynamics_Model_Plan_of_Action_2.ppt",
-                    "description": "RTO meeting plan of action regarding the structural dynamics modeltion regarding the str",
                     "@type": "dcat:Distribution",
+                    "description": "RTO meeting plan of action regarding the structural dynamics modeltion regarding the str",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Structural_Dynamics_Model_Plan_of_Action_2.ppt",
+                    "mediaType": "application/vnd.ms-powerpoint",
                     "title": "Structural_Dynamics_Model_Plan_of_Action.ppt"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_423",
+            "issued": "2011-07-05",
+            "keyword": [
+                "dashlink",
+                "ames",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/423/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "RTA & IFASD June-July 2011"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-X-MRS-1%2F2%2F3-EXT3-2765-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Solar Conjunction measurement and covers the time 2011-02-09T14:00:15 to 2011-02-09T16:29:57.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-x-mrs-1-2-3-ext3-2765-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars express"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-X-MRS-1%2F2%2F3-EXT3-2765-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-x-mrs-1-2-3-ext3-2765-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Solar Conjunction measurement and covers the time 2011-02-09T14:00:15 to 2011-02-09T16:29:57.500.",
-            "title": "MARS EXPRESS SUN MRS 1/2/3\n                                     EXTENDED MISSION 3 2765 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS SUN MRS 1/2/3\n                                     EXTENDED MISSION 3 2765 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-10-04",
-            "temporal": "2021-10-04T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "topo",
-                "coordinates",
-                "coords",
-                "ephemeris",
-                "international",
-                "iss",
-                "location",
-                "space",
-                "station",
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
-            "identifier": "nasa-iss-data_2021-10-04_jufh-my5i",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2021-10-04",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -997093,47 +997069,53 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2021-10-04_jufh-my5i",
+            "issued": "2021-10-04",
+            "keyword": [
+                "topo",
+                "coordinates",
+                "coords",
+                "ephemeris",
+                "international",
+                "iss",
+                "location",
+                "space",
+                "station",
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
+            "temporal": "2021-10-04T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2021-10-04"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/juj5-m9v3",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "temporal": "1977-01-01/1996-01-01",
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
                 "fn": "William Stefanov",
                 "hasEmail": "mailto:jsc-earthweb@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-0000037__21",
+            "describedBy": "http://www.lpi.usra.edu/resources/gc/gcreadme.html",
             "description": "Planetary nomenclature, like terrestrial nomenclature, is used to uniquely identify a feature on the surface of a planet or satellite so that the feature can be easily located, described, and discussed. This gazetteer contains detailed information about all names of topographic and albedo features on planets and satellites (and some planetary ring and ring-gap systems) that the International Astronomical Union (IAU) has named and approved from its founding in 1919 through the present time.",
-            "title": "Gateway to Astronaut Photography of Earth",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -997141,250 +997123,243 @@
                     "mediaType": "text/html"
                 }
             ],
-            "describedBy": "http://www.lpi.usra.edu/resources/gc/gcreadme.html",
-            "accrualPeriodicity": "irregular"
+            "identifier": "NASA-0000037__21",
+            "issued": "2018-06-25",
+            "keyword": [
+                "wise",
+                "space science",
+                "nen",
+                "geography"
+            ],
+            "landingPage": "https://data.nasa.gov/d/juj5-m9v3",
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-NLR-6-EROS-MAPS-MODELS-V1.0",
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
+            "description": "NLR Level 3 Data Products includes spherical harmonic shape and gravity models, and gridded maps or images of those models.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-nlr-6-eros-maps-models-v1.0_jujw-ibqe",
+            "issued": "2018-06-26",
+            "keyword": [
+                "near earth asteroid rendezvous",
+                "eros"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-NLR-6-EROS-MAPS-MODELS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-nlr-6-eros-maps-models-v1.0_jujw-ibqe",
-            "description": "NLR Level 3 Data Products includes spherical harmonic shape and gravity models, and gridded maps or images of those models.",
-            "title": "NEAR NLR LEVEL 3 DATA PRODUCTS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEAR NLR LEVEL 3 DATA PRODUCTS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/914",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Folho Novaes, J.P., E.C. Selva, E.G. Couto, J. Lehmann, M.S. Johnson, and S.J. Riha. 2009. LBA-ECO ND-11 Soil Properties of Forested Headwater Catchments, Mato Grosso, Brazil. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/914",
-            "issued": "2023-10-03",
-            "temporal": "2004-05-01T00:00:00Z/2004-08-18T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-04",
-            "keyword": [
-                "land surface",
-                "earth science",
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
-            "identifier": "C2777411496-ORNL_CLOUD",
             "description": "The results of the analysis of soil chemical parameters, texture, and color are reported for 185 georeferenced soil profile sample points over four forested headwater catchments near Juruena, Mato Grosso, Brazil (Novaes Filho, et al., 2007a and Novaes Filho, et al., 2007b). Samples were collected from an approximately 20 x 20 m grid over each watershed from 2004/05/01 to 2004/08/18. By sampling each location at depths of 0-20 and 40-60 cm it was possible to distinguish and map the principle soil classes found in the study area to the 2nd category level of the Brazilian System of Soil Classification (Cooper et al., 2005) associated with the topographic relief. The data set contains one comma separated ASCII data file with spatially referenced soil nutrient and organic carbon data from 0-20 cm (A layer, topsoil) and 40-60 cm (B layer, subsoil)depths for the Juruena watersheds study area.A satisfactory relationship between the redness index of the diagnostic horizons and the soil class colors was also found. In spite of the apparent homogeneity of the visible landscape characteristics such as slope, soil color, and vegetation, the carbon and soil clay attributes were found to vary greatly. This variability over small distances demonstrates that extrapolation of soil characteristics and soil carbon stocks to larger areas could produce erroneous results if the spatial variability of the soil attributes is not taken into consideration.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO ND-11 Soil Properties of Forested Headwater Catchments, Mato Grosso, Brazil",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F914",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F914",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/nutrient_dynamics/ND11_Soil_Spatial_Variability/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/nutrient_dynamics/ND11_Soil_Spatial_Variability/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/ND11_Soil_Spatial_Variability.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/ND11_Soil_Spatial_Variability.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/914",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/914",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/nutrient_dynamics/ND11_Soil_Spatial_Variability/comp/ND11_Soil_Spatial_Variability.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/nutrient_dynamics/ND11_Soil_Spatial_Variability/comp/ND11_Soil_Spatial_Variability.pdf",
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
+            "identifier": "C2777411496-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "land surface",
+                "earth science",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/914",
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
             "spatial": "-10.42 -58.76",
+            "temporal": "2004-05-01T00:00:00Z/2004-08-18T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO ND-11 Soil Properties of Forested Headwater Catchments, Mato Grosso, Brazil"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-SDC-2-PLUTOCRUISE-V2.0",
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
-                "dust"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Raw data taken by the New Horizons                Student Dust Counter                                                   instrument during the                                                    pluto cruise                                                           mission phase.  This is VERSION 2.0 of this data set.                    SDC collected science data intermittently during the hibernation         years following the Jupiter encounter, designated as the PLUTOCRUISE     phase.  There were also Annual Checkouts (ACOs), STIM calibrations,      Noise calibrations, and an anomaly in November, 2007.                    SDC's main science data collection periods were during hibernation.      During ACOs, science data are taken intermittently but the user must     be careful in analyzing these data since there is usually more           activity on the spacecraft during hibernation.  STIM and Noise refer     to scheduled calibrations and are done with a regular cadence of one     per year after the Jupiter encounter; they occurred sporadically in      the early years of the mission.                                          Note that some SDC data files have the same stop and start time and      a zero exposure time.  The reason for this is that the start and         stop time for SDC data files are the event times for the first and       last events in the files, so for files that contain a single event,      these two values are the same.                                           The changes in Version 2.0 were re-running of the ancillary data         in the data product, updated geometry from newer SPICE kernels,          minor editing of the documentation, catalogs, etc., and resolution       of liens from the December, 2014 review, plus those from the May,        2016 review of the Pluto Encounter data sets.                            New observations added with this version (V2.0) include ongoing          cruise observations from August, 2014 through January, 2015.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-sdc-2-plutocruise-v2.0_jumw-c67y",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons",
+                "dust"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-SDC-2-PLUTOCRUISE-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-sdc-2-plutocruise-v2.0_jumw-c67y",
-            "description": "This data set contains Raw data taken by the New Horizons                Student Dust Counter                                                   instrument during the                                                    pluto cruise                                                           mission phase.  This is VERSION 2.0 of this data set.                    SDC collected science data intermittently during the hibernation         years following the Jupiter encounter, designated as the PLUTOCRUISE     phase.  There were also Annual Checkouts (ACOs), STIM calibrations,      Noise calibrations, and an anomaly in November, 2007.                    SDC's main science data collection periods were during hibernation.      During ACOs, science data are taken intermittently but the user must     be careful in analyzing these data since there is usually more           activity on the spacecraft during hibernation.  STIM and Noise refer     to scheduled calibrations and are done with a regular cadence of one     per year after the Jupiter encounter; they occurred sporadically in      the early years of the mission.                                          Note that some SDC data files have the same stop and start time and      a zero exposure time.  The reason for this is that the start and         stop time for SDC data files are the event times for the first and       last events in the files, so for files that contain a single event,      these two values are the same.                                           The changes in Version 2.0 were re-running of the ancillary data         in the data product, updated geometry from newer SPICE kernels,          minor editing of the documentation, catalogs, etc., and resolution       of liens from the December, 2014 review, plus those from the May,        2016 review of the Pluto Encounter data sets.                            New observations added with this version (V2.0) include ongoing          cruise observations from August, 2014 through January, 2015.",
-            "title": "NEW HORIZONS                            \n      SDC PLUTO CRUISE                                                        \n      RAW V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS                            \n      SDC PLUTO CRUISE                                                        \n      RAW V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-RSS-1-SAGR6-V1.0",
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
+            "description": "The Cassini Radio Science Saturn Gravity Science Experiment (SAGR6) Raw Data Archive is a time-ordered collection of radio science raw data acquired on January 14, February 7, 9, and March 31, 2008, during the Tour subphase of the Cassini mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-rss-1-sagr6-v1.0_juqt-n2k4",
+            "issued": "2021-05-21",
+            "keyword": [
+                "saturn",
+                "cassini-huygens"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-RSS-1-SAGR6-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-rss-1-sagr6-v1.0_juqt-n2k4",
-            "description": "The Cassini Radio Science Saturn Gravity Science Experiment (SAGR6) Raw Data Archive is a time-ordered collection of radio science raw data acquired on January 14, February 7, 9, and March 31, 2008, during the Tour subphase of the Cassini mission.",
-            "title": "CASSINI RSS RAW DATA SET - SAGR6 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI RSS RAW DATA SET - SAGR6 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/JAQQKCT6FZHX",
             "citation": "William J. Blackwell, MIT Lincoln Laboratory. 2024-08-01. TROPICS03URADL2A. Version 1.0. TROPICS03\u00a0L2A Unified Resolution Brightness Temperatures V1.0. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/JAQQKCT6FZHX. https://disc.gsfc.nasa.gov/datacollection/TROPICS03URADL2A_1.0.html. Digital Science Data.",
-            "issued": "2021-07-19",
-            "temporal": "2021-07-19T00:00:00Z/2024-08-26T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-07-19",
-            "references": [
-                "https://doi.org/10.1002/qj.3290"
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
-            "identifier": "C3179859133-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The \"Time-Resolved Observations of Precipitation structure and storm Intensity with a Constellation of Smallsats\" (TROPICS) mission has a goal of providing nearly all-weather observations of three-dimensional temperature and humidity, as well as cloud ice and precipitation horizontal structure, at high temporal resolution to conduct high-value science investigations of tropical cyclones. The mission comprises a constellation of five identical Space Vehicles (SVs) conforming to the 3U form factor and hosting a passive microwave spectrometer payload.\n\nEach SV hosts an identical high-performance spectrometer named the TROPICS Millimeter-wave Sounder (TMS) that will provide temperature profiles using seven channels near the 118.75-GHz oxygen absorption line, water vapor profiles using three channels near the 183-GHz water vapor absorption line, imagery in a single channel near 90 GHz for precipitation measurements (when combined with higher resolution water vapor channels), and a single channel near 205 GHz that is more sensitive to cloud-sized ice particles.\n\nThis dataset is from the TROPICS03 satellite, as the Validated Stage-1 version of the Level 2A geolocated brightness temperature with the water vapor sounding channels (Ch. 9 to 12) converted from their native G-band resolution to the temperature sounding channel (F-band) native resolution (i.e., all measurements at the same unified larger resolution). This product is used in the Atmospheric Vertical Temperature Profile (AVTP) retrievals to gain the benefit of averaging the G-band channels (i.e., noise reduction) while maintain the F-band (AVTP) spatial resolution. The conversion uses the Backus-Gilbert technique. Each TROPICS netCDF file contains a granule of data with 81 spots and approximately 2880 scans, where a granule is defined as an orbit's worth of data.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "TROPICS03URADL2A",
-            "creator": "William J. Blackwell, MIT Lincoln Laboratory",
-            "title": "TROPICS03\u00a0L2A Unified Resolution Brightness Temperatures V1.0",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TROPICS03URADL2A_0.2.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FJAQQKCT6FZHX",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FJAQQKCT6FZHX",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -997394,326 +997369,353 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TROPICS03URADL2A_1.0.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TROPICS03URADL2A_1.0.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TROPICS_L2A/TROPICS03URADL2A.1.0/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TROPICS_L2A/TROPICS03URADL2A.1.0/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/opendap/TROPICS_L2A/TROPICS03URADL2A.1.0/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/opendap/TROPICS_L2A/TROPICS03URADL2A.1.0/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TROPICS03URADL2A_1.0",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TROPICS03URADL2A_1.0",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPICS/TRPCS-ATBD-035_L2a_URRP_V2.1.pdf",
-                    "description": "TROPICS L2A Radiance ATBD",
                     "@type": "dcat:Distribution",
+                    "description": "TROPICS L2A Radiance ATBD",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPICS/TRPCS-ATBD-035_L2a_URRP_V2.1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPICS/TROPICS_UserGuide_base_Sept2023.pdf",
-                    "description": "TROPICS User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "TROPICS User Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPICS/TROPICS_UserGuide_base_Sept2023.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPICS/TROPICS-03_-06_-05_-07_L2a_Release_README_Aug2024.pdf",
-                    "description": "TROPICS L2A README",
                     "@type": "dcat:Distribution",
+                    "description": "TROPICS L2A README",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPICS/TROPICS-03_-06_-05_-07_L2a_Release_README_Aug2024.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
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
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TROPICS03URADL2A_0.2.png",
+            "identifier": "C3179859133-GES_DISC",
+            "issued": "2021-07-19",
+            "keyword": [
+                "spectral/engineering",
+                "microwave",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/JAQQKCT6FZHX",
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
+                "https://doi.org/10.1002/qj.3290"
+            ],
+            "release-place": "Greenbelt, MD",
+            "series-name": "TROPICS03URADL2A",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2021-07-19T00:00:00Z/2024-08-26T00:00:00Z",
             "theme": [
                 "TROPICS (EVI-3)",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPICS03\u00a0L2A Unified Resolution Brightness Temperatures V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/10.7927/5tht-jg22",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Requia, W. J., Y. Wei, A. Shtein, X. Xing, E. Castro, Q. Di, R. Silvern, J. T. Kelly, P. Koutrakis, L. J. Mickley, M. P. Sulprizio, H. Amini, C. Hultquist, L. Shi, Y. Daouk, and J. Schwartz. 2024-01-30. Daily 8-Hour Maximum and Annual O3 Concentrations for the Contiguous United States, 1-km Grids, Version 1.10 (2000-2016). Version 1.10. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/10.7927/5tht-jg22. https://doi.org/10.7927/5tht-jg22.",
-            "issued": "2024-01-30",
-            "temporal": "2000-01-01T00:00:00Z/2016-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-01-30",
-            "keyword": [
-                "atmospheric chemistry",
-                "earth science",
-                "atmosphere"
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
-            "identifier": "C2848642408-SEDAC",
-            "description": "The Daily 8-Hour Maximum and Annual O3 Concentrations for the Contiguous United States, 1-km Grids, Version 1.10 (2000-2016) data set contains estimates of ozone concentrations at a high resolution spatially (1-km grid cells) and temporally (daily) for the years 2000 to 2016. These predictions incorporated various predictor variables such as Ozone (O3) ground measurements from the U.S. Environmental Protection Agency (EPA) Air Quality System (AQS) monitoring data, land-use variables, meteorological variables, chemical transport models and remote sensing data, along with other data sources. After imputing missing data with machine learning algorithms, a geographically-weighted ensemble model was applied that combined estimates from three types of machine learners (neural network, random forest, and gradient boosting). The annual predictions were computed by averaging the daily 8-hour maximum predictions in each year for each grid cell. The results demonstrate high overall model performance with a cross-validated R-squared value against daily observations of 0.90 and 0.86 for annual averages. In version 1.10, we have enhanced the completeness of daily O3 predictions by employing linear interpolation to impute missing values. Specifically, for days with small spatial patches of missing data with less than 100 grid cells, we used inverse distance weighting interpolation to fill the missing grid cells. Other missing daily O3 predictions were interpolated from the nearest days with available data. Annual predictions were updated by averaging the imputed daily predictions for each year in each grid cell. These daily 8-hour maximum and annual O3 predictions allow public health researchers to respectively estimate the short- and long-term effects of O3 exposures on human health, supporting the U.S. EPA for the revision of the National Ambient Air Quality Standards for O3. The data are available in RDS and GeoTIFF formats for statistical research and geospatial analysis.",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Requia, W. J., Y. Wei, A. Shtein, X. Xing, E. Castro, Q. Di, R. Silvern, J. T. Kelly, P. Koutrakis, L. J. Mickley, M. P. Sulprizio, H. Amini, C. Hultquist, L. Shi, Y. Daouk, and J. Schwartz",
-            "title": "Daily 8-Hour Maximum and Annual O3 Concentrations for the Contiguous United States, 1-km Grids, Version 1.10 (2000-2016)",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/aqdh/aqdh-o3-concentrations-contiguous-us-1-km-v1-10-2000-2016/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Daily 8-Hour Maximum and Annual O3 Concentrations for the Contiguous United States, 1-km Grids, Version 1.10 (2000-2016) data set contains estimates of ozone concentrations at a high resolution spatially (1-km grid cells) and temporally (daily) for the years 2000 to 2016. These predictions incorporated various predictor variables such as Ozone (O3) ground measurements from the U.S. Environmental Protection Agency (EPA) Air Quality System (AQS) monitoring data, land-use variables, meteorological variables, chemical transport models and remote sensing data, along with other data sources. After imputing missing data with machine learning algorithms, a geographically-weighted ensemble model was applied that combined estimates from three types of machine learners (neural network, random forest, and gradient boosting). The annual predictions were computed by averaging the daily 8-hour maximum predictions in each year for each grid cell. The results demonstrate high overall model performance with a cross-validated R-squared value against daily observations of 0.90 and 0.86 for annual averages. In version 1.10, we have enhanced the completeness of daily O3 predictions by employing linear interpolation to impute missing values. Specifically, for days with small spatial patches of missing data with less than 100 grid cells, we used inverse distance weighting interpolation to fill the missing grid cells. Other missing daily O3 predictions were interpolated from the nearest days with available data. Annual predictions were updated by averaging the imputed daily predictions for each year in each grid cell. These daily 8-hour maximum and annual O3 predictions allow public health researchers to respectively estimate the short- and long-term effects of O3 exposures on human health, supporting the U.S. EPA for the revision of the National Ambient Air Quality Standards for O3. The data are available in RDS and GeoTIFF formats for statistical research and geospatial analysis.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2F10.7927%2F5tht-jg22",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2F10.7927%2F5tht-jg22",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/aqdh/aqdh-o3-concentrations-contiguous-us-1-km-v1-10-2000-2016/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/aqdh/aqdh-o3-concentrations-contiguous-us-1-km-v1-10-2000-2016/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/aqdh-o3-concentrations-contiguous-us-1-km-v1-10-2000-2016/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/aqdh-o3-concentrations-contiguous-us-1-km-v1-10-2000-2016/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/aqdh-o3-concentrations-contiguous-us-1-km-v1-10-2000-2016/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/aqdh-o3-concentrations-contiguous-us-1-km-v1-10-2000-2016/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/aqdh-o3-concentrations-contiguous-us-1-km-v1-10-2000-2016",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/aqdh-o3-concentrations-contiguous-us-1-km-v1-10-2000-2016",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/aqdh/aqdh-o3-concentrations-contiguous-us-1-km-v1-10-2000-2016/sedac-logo.jpg",
+            "identifier": "C2848642408-SEDAC",
+            "issued": "2024-01-30",
+            "keyword": [
+                "atmospheric chemistry",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.7927/10.7927/5tht-jg22",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-01-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 17.0 -65.0 72.0",
+            "temporal": "2000-01-01T00:00:00Z/2016-12-31T00:00:00Z",
             "theme": [
                 "AQDH",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Daily 8-Hour Maximum and Annual O3 Concentrations for the Contiguous United States, 1-km Grids, Version 1.10 (2000-2016)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1615929573-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, OB.DAAC.",
-            "issued": "2019-06-23",
-            "temporal": "2002-07-04T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-10-01",
-            "keyword": [
-                "ocean temperature",
-                "ngda",
-                "earth science",
-                "national geospatial data asset",
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
-            "identifier": "C1615929573-OB_DAAC",
             "description": "MODIS (or Moderate Resolution Imaging Spectroradiometer) is a key instrument aboard the Terra (EOS AM) and Aqua (EOS PM) satellites. Terra's orbit around the Earth is timed so that it passes from north to south across the equator in the morning, while Aqua passes south to north over the equator in the afternoon. Terra MODIS and Aqua MODIS are viewing the entire Earth's surface every 1 to 2 days, acquiring data in 36 spectral bands, or groups of wavelengths (see MODIS Technical Specifications). These data will improve our understanding of global dynamics and processes occurring on the land, in the oceans, and in the lower atmosphere. MODIS is playing a vital role in the development of validated, global, interactive Earth system models able to predict global change accurately enough to assist policy makers in making sound decisions concerning the protection of our environment.",
-            "title": "Aqua MODIS Global Mapped 11\u00b5m Nighttime Sea Surface Temperature (NSST) Data, version R2019.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directaccess/MODIS-Aqua/L3SMI/",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directaccess/MODIS-Aqua/L3SMI/",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/AQUA/MODIS/L3M/NSST/R2019.0",
-                    "description": "MODIS-Aqua L3M 11\u00b5m Nighttime Sea Surface Temperature (NSST) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS-Aqua L3M 11\u00b5m Nighttime Sea Surface Temperature (NSST) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/AQUA/MODIS/L3M/NSST/R2019.0",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/MODISA/L3SMI/",
-                    "description": "OB.DAAC OPeNDAP Site for Aqua MODIS Standard Mapped Image (SMI) Product",
                     "@type": "dcat:Distribution",
+                    "description": "OB.DAAC OPeNDAP Site for Aqua MODIS Standard Mapped Image (SMI) Product",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/MODISA/L3SMI/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1615929573-OB_DAAC",
+            "issued": "2019-06-23",
+            "keyword": [
+                "ocean temperature",
+                "ngda",
+                "earth science",
+                "national geospatial data asset",
+                "oceans"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1615929573-OB_DAAC.html",
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
+            "title": "Aqua MODIS Global Mapped 11\u00b5m Nighttime Sea Surface Temperature (NSST) Data, version R2019.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/942/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2016-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "ames",
-                "dashlink",
-                "nasa"
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
-            "identifier": "DASHLINK_942",
             "description": "The chapter describes the application of prognostic techniques to the domain of structural health and\r\ndemonstrates the efficacy of the methods using fatigue data from a graphite-epoxy composite coupon. Prognostics denotes the in-situ assessment of the health of a component and the repeated estimation of remaining life, conditional on anticipated future usage. The methods shown here use a physics-based modeling approach whereby the behavior of the damaged components is encapsulated via mathematical equations that describe the characteristics of the components as it experiences increasing degrees of degradation. Mathematical rigorous techniques are used to extrapolate the remaining life to a failure threshold. Additionally, mathematical tools are used to calculate the uncertainty associated with making predictions. The information stemming from the predictions can be used in an operational context for go/no go decisions, quantify risk of ability to complete a (set of) mission or operation, and when to schedule maintenance.",
-            "title": "Prognostics Design Solutions in Structural Health Monitoring Systems",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2015_PrognosticsDesign.pdf",
-                    "description": "chapter",
                     "@type": "dcat:Distribution",
+                    "description": "chapter",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2015_PrognosticsDesign.pdf",
+                    "mediaType": "application/pdf",
                     "title": "2015_PrognosticsDesign.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_942",
+            "issued": "2016-01-14",
+            "keyword": [
+                "ames",
+                "dashlink",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/942/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Prognostics Design Solutions in Structural Health Monitoring Systems"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0741-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-30T09:36:15.000 to 2015-04-30T15:24:09.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0741-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0741-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0741-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-30T09:36:15.000 to 2015-04-30T15:24:09.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0741 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0741 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-ESC1-67PCHURYUMOV-M12-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera during the COMET ESCORT 1 phase of the Rosetta mission at the comet 67P, covering the period from 2015-01-13T23:25:00.000 to 2015-02-10T23:24:59.000. This version V2.0 supersedes previous deliveries of the same dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-esc1-67pchuryumov-m12-v2.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "vega",
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
@@ -997721,277 +997723,257 @@
                 "dark",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-ESC1-67PCHURYUMOV-M12-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-esc1-67pchuryumov-m12-v2.0",
-            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera during the COMET ESCORT 1 phase of the Rosetta mission at the comet 67P, covering the period from 2015-01-13T23:25:00.000 to 2015-02-10T23:24:59.000. This version V2.0 supersedes previous deliveries of the same dataset.",
-            "title": "ROSETTA-ORBITER COMET ESCORT 1 OSINAC 2 EDR MTP012 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMET ESCORT 1 OSINAC 2 EDR MTP012 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0591-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-02-19T10:51:30.000 to 2015-02-19T20:14:12.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0591-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0591-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0591-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-02-19T10:51:30.000 to 2015-02-19T20:14:12.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0591 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0591 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2094",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hook, S.J., J.S. Myers, K.J. Thome, M. Fitzgerald, A.B. Kahle,  Airborne Sensor Facility NASA Ames Research Center, F.F. Sabins, L.J. Rothschild, C. Real, and J. Baxter. 2022. MASTER: Airborne Science, California-Nevada, March, 2000. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2094",
-            "issued": "2023-07-09",
-            "temporal": "2000-03-10T21:43:48Z/2000-03-14T10:55:41Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-13",
-            "keyword": [
-                "earth science",
-                "visible wavelengths",
-                "spectral/engineering",
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
-            "identifier": "C2731771950-ORNL_CLOUD",
             "description": "This dataset includes Level 1B (L1B) data products from the MODIS/ASTER Airborne Simulator (MASTER) instrument. The spectral data were collected during five flights aboard a DOE B-200 aircraft over California and Nevada, U.S., on 2000-03-10 to 2000-03-14. This deployment was coordinated by the U.S. Department of Energy's Remote Sensing Laboratory (RSL) located at Nellis Air Force Base near Las Vegas, Nevada. Data products include L1B georeferenced multispectral imagery of calibrated radiance in 50 bands covering wavelengths of 0.460 to 12.879 micrometers at approximately 20-meter spatial resolution. The L1B file format is HDF-4. In addition, the dataset includes flight paths, spectral band information, instrument configuration, ancillary notes, and summary information for each flight, and browse images derived from each L1B data file.",
-            "graphic-preview-description": "Single-band images and a RGB composite image from flight track 1 acquired on 13 March 2000 over Bair Island portion of San Francisco Bay north of Menlo Park, California, U.S. Source: MASTERL1B_0000105_01_20000313_2014_2018_V01.jpg",
-            "title": "MASTER: Airborne Science, California-Nevada, March, 2000",
-            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_March_2000_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2094",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2094",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/master/MASTER_RSL_March_2000/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/master/MASTER_RSL_March_2000/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_March_2000.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_March_2000.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2094",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2094",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_RSL_March_2000/comp/MASTER_RSL_March_2000.pdf",
-                    "description": "MASTER: Airborne Science, California-Nevada, March, 2000: MASTER_RSL_March_2000.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "MASTER: Airborne Science, California-Nevada, March, 2000: MASTER_RSL_March_2000.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_RSL_March_2000/comp/MASTER_RSL_March_2000.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_March_2000_Fig1.jpg",
-                    "description": "Single-band images and a RGB composite image from flight track 1 acquired on 13 March 2000 over Bair Island portion of San Francisco Bay north of Menlo Park, California, U.S. Source: MASTERL1B_0000105_01_20000313_2014_2018_V01.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Single-band images and a RGB composite image from flight track 1 acquired on 13 March 2000 over Bair Island portion of San Francisco Bay north of Menlo Park, California, U.S. Source: MASTERL1B_0000105_01_20000313_2014_2018_V01.jpg",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_March_2000_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Single-band images and a RGB composite image from flight track 1 acquired on 13 March 2000 over Bair Island portion of San Francisco Bay north of Menlo Park, California, U.S. Source: MASTERL1B_0000105_01_20000313_2014_2018_V01.jpg",
+            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_March_2000_Fig1.jpg",
+            "identifier": "C2731771950-ORNL_CLOUD",
+            "issued": "2023-07-09",
+            "keyword": [
+                "earth science",
+                "visible wavelengths",
+                "spectral/engineering",
+                "infrared wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2094",
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
             "spatial": "-122.31 34.01 -118.13 39.37",
+            "temporal": "2000-03-10T21:43:48Z/2000-03-14T10:55:41Z",
             "theme": [
                 "MASTER",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MASTER: Airborne Science, California-Nevada, March, 2000"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/806",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Thornton, P.E. 2005. Biome-BGC: Modeling Effects of Disturbance and Climate (Thornton et al. 2002). ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/806",
-            "issued": "2024-04-26",
-            "temporal": "2002-12-02T00:00:00Z/2002-12-02T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-28",
-            "keyword": [
-                "earth science",
-                "land surface",
-                "biosphere",
-                "ecological dynamics",
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
-            "identifier": "C2956538963-ORNL_CLOUD",
             "description": "This archived model product contains the directions, executables, and procedures for running Biome-BGC, Version 4.1.1, to recreate the results of the following article: Thornton, P. E., B. E. Law, H. L. Gholz, K. L. Clark, E. Falge, D. S. Ellsworth, A. H. Goldstein, R. K. Monson,  D. Hollinger, M. Falk, J. Chen, and J. P. Sparks. 2002. Modeling and measuring the effects of disturbance history and climate on carbon and water budgets in evergreen needleleaf forests. Agricultural and Forest Meteorology 113:185-222. Abstract: The effects of disturbance history, climate, and changes in atmospheric carbon dioxide (CO2) concentration and nitrogen deposition (Ndep) on carbon and water fluxes in seven North American evergreen forests are assessed using a coupled water, carbon, nitrogen model, canopy-scale flux observations, and descriptions of the vegetation type, management practices, and disturbance histories at each site. The effects of interannual climate variability, disturbance history, and vegetation ecophysiology on carbon and water fluxes and storage are integrated by the ecosystem process model Biome-BGC, with results compared to site biometric analyses and eddy covariance observations aggregated by month and year.  The model produced good estimates of between-site variation in leaf area index, with mixed performance for between- and within-site variation in evapotranspiration. There is a model bias toward smaller annual carbon sinks at five sites, with a seasonal model bias toward smaller warm-season sink strength at all sites.",
-            "graphic-preview-description": "Browse Image",
-            "title": "Biome-BGC: Modeling Effects of Disturbance and Climate (Thornton et al. 2002)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/model-archive_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F806",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F806",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/model_archive/BIOME_BGC_m_4_1_1/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/model_archive/BIOME_BGC_m_4_1_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/MODELS/guides/biome-bgc_manuscript.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/MODELS/guides/biome-bgc_manuscript.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/806",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/806",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/model_archive/BIOME_BGC_m_4_1_1/comp/biome-bgc_manuscript.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/model_archive/BIOME_BGC_m_4_1_1/comp/biome-bgc_manuscript.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/model_archive/BIOME_BGC_m_4_1_1/comp/thornton_2002_msarch_readme.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/model_archive/BIOME_BGC_m_4_1_1/comp/thornton_2002_msarch_readme.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/model-archive_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/model-archive_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/model-archive_logo_square.png",
+            "identifier": "C2956538963-ORNL_CLOUD",
+            "issued": "2024-04-26",
+            "keyword": [
+                "earth science",
+                "land surface",
+                "biosphere",
+                "ecological dynamics",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/806",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-04-28",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-12-02T00:00:00Z/2002-12-02T23:59:59Z",
             "theme": [
                 "Model Archive",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Biome-BGC: Modeling Effects of Disturbance and Climate (Thornton et al. 2002)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/jv6f-574k",
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
-                "geography",
-                "nen",
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
-            "identifier": "NASA-0000038__65",
+            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
             "description": "Planetary nomenclature, like terrestrial nomenclature, is used to uniquely identify a feature on the surface of a planet or satellite so that the feature can be easily located, described, and discussed. This gazetteer contains detailed information about all names of topographic and albedo features on planets and satellites (and some planetary ring and ring-gap systems) that the International Astronomical Union (IAU) has named and approved from its founding in 1919 through the present time.",
-            "title": "Gazetteer of Planetary Nomenclature",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -997999,49 +997981,39 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
-            "accrualPeriodicity": "irregular"
+            "identifier": "NASA-0000038__65",
+            "issued": "2018-06-25",
+            "keyword": [
+                "wise",
+                "geography",
+                "nen",
+                "space science"
+            ],
+            "landingPage": "https://data.nasa.gov/d/jv6f-574k",
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
-                "circulation",
-                "imagery",
-                "lunar science",
-                "modeling"
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
-            "identifier": "NASA-0000030__3",
             "description": "The Consolidated Lunar Atlas is a collection of the best photographic images of the moon, including low-oblique photography, full-moon photography, and tabular and positional plates.",
-            "title": "Consolidated Lunar Atlas",
-            "programCode": [
-                "026:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -998049,97 +998021,139 @@
                     "mediaType": "text/html"
                 }
             ],
+            "identifier": "NASA-0000030__3",
+            "issued": "2018-06-25",
+            "keyword": [
+                "space science",
+                "circulation",
+                "imagery",
+                "lunar science",
+                "modeling"
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0801-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-05-22T21:00:10.000 to 2015-05-22T23:09:07.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0801-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0801-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0801-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-05-22T21:00:10.000 to 2015-05-22T23:09:07.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0801 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0801 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-HRSC-5-REFDR-MAPPROJECTED-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "N/A",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-hrsc-5-refdr-mapprojected-v3.0_jvbr-q2wi",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "deimos",
                 "mars",
                 "phobos",
                 "mars express"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-HRSC-5-REFDR-MAPPROJECTED-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-hrsc-5-refdr-mapprojected-v3.0_jvbr-q2wi",
-            "description": "N/A",
-            "title": "MARS EXPRESS HRSC MAP PROJECTED REFDR V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS HRSC MAP PROJECTED REFDR V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/jvc7-p5f4",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Cell cycle and cell proliferation are decoupled under altered gravity conditions. We have previously shown that semisolid cell cultures of Arabidopsis suffer overall genome changes in response to altered gravity and also that cell cycle stages duration is altered. By using synchronized cell cultures we will demonstrate the precise alterations in cell cycle duration and also the transcriptional signature in any of them. Experiments consists on exposures of Arabidopsis cell cultures to 1g control/simulated microgravity (RPM) conditions. Asynchronous cells exposed for 14 h + Syncronous populations choosen to have an enrichment of cell cycle phases were used (being T7/T10 samples on G2 phase T14/T16 samples on G1 phase). 6 dye-swap - time course treated vs untreated comparison.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-144",
+                    "mediaType": "text/html",
+                    "title": "Gravitational signature of synchronized cell cultures in particular cell cycle stages"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-144_jvc7-p5f4",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "cell cycle phase",
                 "sample treatment protocol",
@@ -998158,70 +998172,34 @@
                 "growth protocol",
                 "array scanning protocol"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/jvc7-p5f4",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-144_jvc7-p5f4",
-            "description": "Cell cycle and cell proliferation are decoupled under altered gravity conditions. We have previously shown that semisolid cell cultures of Arabidopsis suffer overall genome changes in response to altered gravity and also that cell cycle stages duration is altered. By using synchronized cell cultures we will demonstrate the precise alterations in cell cycle duration and also the transcriptional signature in any of them. Experiments consists on exposures of Arabidopsis cell cultures to 1g control/simulated microgravity (RPM) conditions. Asynchronous cells exposed for 14 h + Syncronous populations choosen to have an enrichment of cell cycle phases were used (being T7/T10 samples on G2 phase T14/T16 samples on G1 phase). 6 dye-swap - time course treated vs untreated comparison.",
-            "title": "Gravitational signature of synchronized cell cultures in particular cell cycle stages",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-144",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Gravitational signature of synchronized cell cultures in particular cell cycle stages"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Gravitational signature of synchronized cell cultures in particular cell cycle stages"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://nasa3d.arc.nasa.gov/detail/mro",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://www.nasa.gov/mission_pages/MRO/main/index.html"
-            ],
-            "keyword": [
-                "satellite",
-                "mars",
-                "mro",
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
-            "identifier": "NASA-387",
             "description": "Mir. Polygons: 124 Vertices: 86",
-            "title": "NASA 3D Models: MRO",
-            "programCode": [
-                "026:045",
-                "026:046"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -998229,278 +998207,314 @@
                     "mediaType": "image/x-3ds"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-387",
+            "issued": "2018-06-25",
+            "keyword": [
+                "satellite",
+                "mars",
+                "mro",
+                "3d model"
+            ],
+            "landingPage": "http://nasa3d.arc.nasa.gov/detail/mro",
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
+                "http://www.nasa.gov/mission_pages/MRO/main/index.html"
+            ],
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "NASA 3D Models: MRO"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-REMS-5-UVRDR-V1.0",
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
+            "description": "UV fluxes measured by the UV sensor  of the Rover Environmental Monitoring  Station (REMS) aboard the Mars Science Laboratory in physical units, with corrections and modeling.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-rems-5-uvrdr-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars science laboratory"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-REMS-5-UVRDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-rems-5-uvrdr-v1.0",
-            "description": "UV fluxes measured by the UV sensor  of the Rover Environmental Monitoring  Station (REMS) aboard the Mars Science Laboratory in physical units, with corrections and modeling.",
-            "title": "MSL MARS ROVER ENV MONITORING STATION\n                                      5 UVRDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MSL MARS ROVER ENV MONITORING STATION\n                                      5 UVRDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/GCPEX/RADIOMETER/DATA102",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Loehnert, Ulrich and Maximillian Maahan.2014. GPM GROUND VALIDATION DUAL POLARIZATION RADIOMETER GCPEX [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/GCPEX/RADIOMETER/DATA102",
-            "issued": "2014-03-18",
-            "temporal": "2011-11-23T00:00:00Z/2012-03-01T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-10",
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
-            "identifier": "C1979693621-GHRC_DAAC",
             "description": "The GPM Ground Validation Dual Polarization Radiometer GCPEx dataset includes brightness temperature measurements at frequencies 90 GHz (not polarized) and 150 GHz (HV-polarized) for the GPM Cold-season Precipitation Experiment (GCPEx) which occurred in Ontario, Canada. GCPEx addressed shortcomings in the GPM snowfall retrieval algorithm by collecting microphysical properties, associated remote sensing observations, and coordinated model simulations of precipitating snow. This dual polarization radiometer (DPR) is sensitive to particle orientation since it observes the brightness temperature difference between the vertical and horizontal polarization channels at 150 GHz, and it is especially important for the retrievals of particle shape and orientation with polarization observations. DPR also has a high sensitivity to the supercooled liquid water in clouds due to the high-frequency window channels. Even though the netCDF data has regular scans, the browse images are only shown at 30 and 150 degrees. Ancillary data was also captured for the internal calibration of the instrument.",
-            "graphic-preview-description": "N/A",
-            "title": "GPM GROUND VALIDATION DUAL POLARIZATION RADIOMETER GCPEX V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/radiometer_dual_pol/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FGCPEX%2FRADIOMETER%2FDATA102",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FGCPEX%2FRADIOMETER%2FDATA102",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmraddpgcpex",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmraddpgcpex",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/radiometer_dual_pol/browse/gcpex_dpr_20111127_L1b.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/radiometer_dual_pol/browse/gcpex_dpr_20111127_L1b.png",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/radiometer_dual_pol/doc/gpmraddpgcpex_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/radiometer_dual_pol/doc/gpmraddpgcpex_dataset.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/micro-articles/snow-microphysics-event-during-gcpex-field-campaign",
-                    "description": "Snow Microphysics Event during GCPEx Field Campaign",
                     "@type": "dcat:Distribution",
+                    "description": "Snow Microphysics Event during GCPEx Field Campaign",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/micro-articles/snow-microphysics-event-during-gcpex-field-campaign",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/radiometer_dual_pol/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/radiometer_dual_pol/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/radiometer_dual_pol/browse/",
+            "identifier": "C1979693621-GHRC_DAAC",
+            "issued": "2014-03-18",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "infrared wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/GCPEX/RADIOMETER/DATA102",
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
             "spatial": "-79.92 44.11 -79.6 44.35",
+            "temporal": "2011-11-23T00:00:00Z/2012-03-01T23:59:59Z",
             "theme": [
                 "GCPEx",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM GROUND VALIDATION DUAL POLARIZATION RADIOMETER GCPEX V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MEaSUREs/LSTE/CAM5K30UC.003",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Eva Borbas. 2023-03-16. CAM5K30UC.003. Combined ASTER and MODIS Emissivity database over Land (CAMEL) Uncertainty Monthly Global 0.05Deg V003. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes DAAC. https://doi.org/10.5067/MEaSUREs/LSTE/CAM5K30UC.003. https://doi.org/10.5067/MEaSUREs/LSTE/CAM5K30UC.003. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2023-03-14",
-            "temporal": "2000-03-01T00:00:00Z/2024-01-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-01-01",
-            "keyword": [
-                "earth science",
-                "biosphere",
-                "land surface",
-                "ngda",
-                "snow/ice",
-                "terrestrial hydrosphere",
-                "surface thermal properties",
-                "surface radiative properties",
-                "vegetation",
-                "national geospatial data asset"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Eva Borbas",
                 "hasEmail": "mailto:eva.borbas@ssec.wisc.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
-            "identifier": "C2600365287-LPDAAC_ECS",
-            "description": "The NASA Making Earth System Data Records for Use in Research Environments (MEaSUREs) (https://earthdata.nasa.gov/community/community-data-system-programs/measures-projects) Combined Advanced Spaceborne Thermal Emission and Reflection Radiometer (ASTER) and Moderate Resolution Imaging Spectroradiometer (MODIS) Emissivity for Land (CAMEL) dataset provides monthly emissivity uncertainty at 0.05 degree (~5 kilometer) resolution (CAM5K30UC). CAM5K30UC is an estimation of total emissivity uncertainty comprising three independent components of variability: temporal, spatial, and algorithm. Each measure of uncertainty is provided for all 13 hinge points of emissivity and each latitude-longitude point. Additional details regarding the methodology are available in the User Guide and Algorithm Theoretical Basis Document (ATBD) (https://lpdaac.usgs.gov/documents/1612/CAMEL_V3_UG_ATBD.pdf). Corresponding emissivity values can be found in the CAM5K30EM (https://doi.org/10.5067/MEaSUREs/LSTE/CAM5K30EM.003) data product.\r\n\r\nProvided in the CAM5K30UC product are layers for algorithm uncertainty, spatial uncertainty, temporal uncertainty, total uncertainty, latitude, longitude, spectral wavelength, CAMEL quality, and total uncertainty quality information.",
-            "series-name": "CAM5K30UC.003",
             "creator": "Eva Borbas",
-            "title": "Combined ASTER and MODIS Emissivity database over Land (CAMEL) Uncertainty Monthly Global 0.05Deg V003",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The NASA Making Earth System Data Records for Use in Research Environments (MEaSUREs) (https://earthdata.nasa.gov/community/community-data-system-programs/measures-projects) Combined Advanced Spaceborne Thermal Emission and Reflection Radiometer (ASTER) and Moderate Resolution Imaging Spectroradiometer (MODIS) Emissivity for Land (CAMEL) dataset provides monthly emissivity uncertainty at 0.05 degree (~5 kilometer) resolution (CAM5K30UC). CAM5K30UC is an estimation of total emissivity uncertainty comprising three independent components of variability: temporal, spatial, and algorithm. Each measure of uncertainty is provided for all 13 hinge points of emissivity and each latitude-longitude point. Additional details regarding the methodology are available in the User Guide and Algorithm Theoretical Basis Document (ATBD) (https://lpdaac.usgs.gov/documents/1612/CAMEL_V3_UG_ATBD.pdf). Corresponding emissivity values can be found in the CAM5K30EM (https://doi.org/10.5067/MEaSUREs/LSTE/CAM5K30EM.003) data product.\r\n\r\nProvided in the CAM5K30UC product are layers for algorithm uncertainty, spatial uncertainty, temporal uncertainty, total uncertainty, latitude, longitude, spectral wavelength, CAMEL quality, and total uncertainty quality information.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEaSUREs%2FLSTE%2FCAM5K30UC.003",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEaSUREs%2FLSTE%2FCAM5K30UC.003",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MEaSUREs/LSTE/CAM5K30UC.003",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MEaSUREs/LSTE/CAM5K30UC.003",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/x-netcdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2600365287-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2600365287-LPDAAC_ECS",
+                    "mediaType": "application/x-netcdf",
                     "title": "Download this dataset"
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
-                    "mediaType": "application/x-netcdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MEASURES/CAM5K30UC.003",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MEASURES/CAM5K30UC.003",
+                    "mediaType": "application/x-netcdf",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1612/CAMEL_V3_UG_ATBD.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1612/CAMEL_V3_UG_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1612/CAMEL_V3_UG_ATBD.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1612/CAMEL_V3_UG_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/gzip",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1651/CAM5K30_Source_Code_V3.tar.gz",
-                    "description": "This documentation contains the software code used to generate high spectral resolution emissivity.",
                     "@type": "dcat:Distribution",
+                    "description": "This documentation contains the software code used to generate high spectral resolution emissivity.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1651/CAM5K30_Source_Code_V3.tar.gz",
+                    "mediaType": "application/gzip",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP109/MEASURES/CAM5K30UC.003/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP109/MEASURES/CAM5K30UC.003/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2600365287-LPDAAC_ECS",
+            "issued": "2023-03-14",
+            "keyword": [
+                "earth science",
+                "biosphere",
+                "land surface",
+                "ngda",
+                "snow/ice",
+                "terrestrial hydrosphere",
+                "surface thermal properties",
+                "surface radiative properties",
+                "vegetation",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEaSUREs/LSTE/CAM5K30UC.003",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-01-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "series-name": "CAM5K30UC.003",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-03-01T00:00:00Z/2024-01-01T00:00:00Z",
             "theme": [
                 "MEaSUREs",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Combined ASTER and MODIS Emissivity database over Land (CAMEL) Uncertainty Monthly Global 0.05Deg V003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/jvfz-7khi",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Transcriptional profiling of mammary tissue irradiated at 10 weeks of age with either 100 cGy sparsely ionizing gamma-rays or 10 cGy or 30 cGy densely ionizing radiation (350 MeV/amu Si). Mammary tissue was collected 1 weeks 4 weeks and 12 weeks post-irradiation. Four radiation treatment groups: sham 100 cGy sparsely ionizing gamma-rays 10 cGy or 30 cGy densely ionizing radiation (350 MeV/amu Si). Three time points post-irradiation (1 4 and 12 weeks). Three or four replicates per time point.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-80",
+                    "mediaType": "text/html",
+                    "title": "Response of mammary tissue to high-LET HZE particle (Silicon ions) radiation or low-LET gamma-rays"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-80_jvfz-7khi",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "labeling protocol",
                 "normalization data transformation",
@@ -998519,47 +998533,35 @@
                 "p-gse48392-7",
                 "rna extraction"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/jvfz-7khi",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-80_jvfz-7khi",
-            "description": "Transcriptional profiling of mammary tissue irradiated at 10 weeks of age with either 100 cGy sparsely ionizing gamma-rays or 10 cGy or 30 cGy densely ionizing radiation (350 MeV/amu Si). Mammary tissue was collected 1 weeks 4 weeks and 12 weeks post-irradiation. Four radiation treatment groups: sham 100 cGy sparsely ionizing gamma-rays 10 cGy or 30 cGy densely ionizing radiation (350 MeV/amu Si). Three time points post-irradiation (1 4 and 12 weeks). Three or four replicates per time point.",
-            "title": "Response of mammary tissue to high-LET HZE particle (Silicon ions) radiation or low-LET gamma-rays",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-80",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Response of mammary tissue to high-LET HZE particle (Silicon ions) radiation or low-LET gamma-rays"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Response of mammary tissue to high-LET HZE particle (Silicon ions) radiation or low-LET gamma-rays"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-ALICE-3-PLUTO-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Calibrated data taken by the New Horizons         Alice Ultraviolet Imaging Spectrograph                                 instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 3.0 of this data set.                    This data set contains ALICE observations taken during the               the Approach (Jan-Jul, 2015), Encounter, Departure, and                  Transition mission sub-phases, including flyby observations              taken on 14 July, 2015, and departure and calibration data               through late October, 2016.  This data set completes the                 Pluto mission phase deliveries for ALICE.                                This is version 3.0 of this dataset. Changes since version 2.0 include   the addition of data downlinked between the end of January, 2016 and the end of October, 2016, completing the delivery of all data covering the   Pluto Encounter and subsequent Calibration Campaign. It includes multi-  map and Lyman-alpha observations of Pluto and Charon, histograms of the  Pluto system moons, and a number of calibration observations of Rho Leo  and other stars.                                                         Also, updates were made to the calibration files, documentation, and     catalog files.  The data were re-run through the updated pipeline,       which changed the FITS headers of the raw data set, but not the FITS     data.  The updated Effective Area calibration file (pa_aeff_007.tab)     changed the calibrated data.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-alice-3-pluto-v3.0_jvgp-yhza",
             "issued": "2018-09-05",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "sun",
                 "new horizons",
@@ -998569,291 +998571,298 @@
                 "charon",
                 "hydra"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-ALICE-3-PLUTO-V3.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-alice-3-pluto-v3.0_jvgp-yhza",
-            "description": "This data set contains Calibrated data taken by the New Horizons         Alice Ultraviolet Imaging Spectrograph                                 instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 3.0 of this data set.                    This data set contains ALICE observations taken during the               the Approach (Jan-Jul, 2015), Encounter, Departure, and                  Transition mission sub-phases, including flyby observations              taken on 14 July, 2015, and departure and calibration data               through late October, 2016.  This data set completes the                 Pluto mission phase deliveries for ALICE.                                This is version 3.0 of this dataset. Changes since version 2.0 include   the addition of data downlinked between the end of January, 2016 and the end of October, 2016, completing the delivery of all data covering the   Pluto Encounter and subsequent Calibration Campaign. It includes multi-  map and Lyman-alpha observations of Pluto and Charon, histograms of the  Pluto system moons, and a number of calibration observations of Rho Leo  and other stars.                                                         Also, updates were made to the calibration files, documentation, and     catalog files.  The data were re-run through the updated pipeline,       which changed the FITS headers of the raw data set, but not the FITS     data.  The updated Effective Area calibration file (pa_aeff_007.tab)     changed the calibrated data.",
-            "title": "NEW HORIZONS                            \n      ALICE PLUTO ENCOUNTER                                                   \n      CALIBRATED V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS                            \n      ALICE PLUTO ENCOUNTER                                                   \n      CALIBRATED V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-SDC-3-JUPITER-V4.0",
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
-                "new horizons",
-                "dust"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Calibrated data taken by the New Horizons         Student Dust Counter                                                   instrument during the                                                    Jupiter encounter                                                      mission phase.  This is VERSION 4.0 of this data set.                    For the Jupiter encounter mission phase, SDC collected no science        data during the Jupiter flyby, as the requisite spacecraft               configuration prevented SDC from operating.  There were some very        sparse data taken from December, 2006 through April, 2007, and           some of very short (or zero) duration after the Jupiter flyby from       April, 2007 through June, 2007.                                          The changes in Version 4.0 were re-running of the ancillary data         in the data product, updated geometry from newer SPICE kernels,          minor editing of the documentation, catalogs, etc., and resolution       of liens from the December, 2014 review, plus those from the May,        2016 review of the Pluto Encounter data sets.  No new observations       were added with Version 4.0.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-sdc-3-jupiter-v4.0_jvhb-xir9",
+            "issued": "2018-09-05",
+            "keyword": [
+                "new horizons",
+                "dust"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-SDC-3-JUPITER-V4.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-sdc-3-jupiter-v4.0_jvhb-xir9",
-            "description": "This data set contains Calibrated data taken by the New Horizons         Student Dust Counter                                                   instrument during the                                                    Jupiter encounter                                                      mission phase.  This is VERSION 4.0 of this data set.                    For the Jupiter encounter mission phase, SDC collected no science        data during the Jupiter flyby, as the requisite spacecraft               configuration prevented SDC from operating.  There were some very        sparse data taken from December, 2006 through April, 2007, and           some of very short (or zero) duration after the Jupiter flyby from       April, 2007 through June, 2007.                                          The changes in Version 4.0 were re-running of the ancillary data         in the data product, updated geometry from newer SPICE kernels,          minor editing of the documentation, catalogs, etc., and resolution       of liens from the December, 2014 review, plus those from the May,        2016 review of the Pluto Encounter data sets.  No new observations       were added with Version 4.0.",
-            "title": "NEW HORIZONS                            \n      SDC JUPITER ENCOUNTER                                                   \n      CALIBRATED V4.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS                            \n      SDC JUPITER ENCOUNTER                                                   \n      CALIBRATED V4.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-NAVCAM-5-ROUGHNESS-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-navcam-5-roughness-ops-v1.0_jvhe-cuqg",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-NAVCAM-5-ROUGHNESS-OPS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-navcam-5-roughness-ops-v1.0_jvhe-cuqg",
-            "description": "not applicable",
-            "title": "MER 1 MARS NAVIGATION CAMERA SURFACE ROUGH RDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MER 1 MARS NAVIGATION CAMERA SURFACE ROUGH RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/IIBT502NXDNE",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SnowEx20 Airborne SWESARR Brightness Temperature V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/IIBT502NXDNE.",
-            "issued": "2020-02-10",
-            "temporal": "2020-02-10T00:00:00Z/2020-02-12T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-02-12",
-            "keyword": [
-                "microwave",
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
-            "identifier": "C2068420609-NSIDC_ECS",
             "description": "This data set contains airborne microwave brightness temperature observations from the Goddard Space Flight Center SWESARR (Snow\nWater Equivalent Synthetic Aperture Radar and Radiometer) instrument during the winter (10-12 February 2020) NASA SnowEx 2020 campaign at Grand Mesa, CO.\nObservations were made at three frequencies (10.65, 18.7, and 36.5 GHz; referred to as X, K, and Ka bands, respectively), at horizontal polarization with a nominal 45-degree look angle.",
-            "title": "SnowEx20 Airborne SWESARR Brightness Temperature V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIIBT502NXDNE",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIIBT502NXDNE",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_SWESARR_TB/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_SWESARR_TB/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_SWESARR_TB.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_SWESARR_TB.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX20_SWESARR_TB+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX20_SWESARR_TB+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/IIBT502NXDNE",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/IIBT502NXDNE",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/IIBT502NXDNE",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/IIBT502NXDNE",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2068420609-NSIDC_ECS",
+            "issued": "2020-02-10",
+            "keyword": [
+                "microwave",
+                "earth science",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/IIBT502NXDNE",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-02-12",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-108.242 38.987 -108.097 39.085",
+            "temporal": "2020-02-10T00:00:00Z/2020-02-12T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SnowEx20 Airborne SWESARR Brightness Temperature V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ERS1B-SNEN0",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "BYU/SCP. 2011-11-29. ERS-1 Gridded Level 3 Enhanced Resolution Sigma-0 from BYU. Version 1. ERS-1 Gridded Level 3 Enhanced Resolution Sigma-0 from BYU. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/ERS1B-SNEN0. https://podaac-tools.jpl.nasa.gov/drive/files/allData/ers1/L3/byu_scp/sigma0enhanced/docs/dLongERS1.html. BYU/SCP, PO.DAAC, 2011-11-29, ERS-1 Gridded Level 3 Enhanced Resolution Sigma-0 from BYU, https://podaac-tools.jpl.nasa.gov/drive/files/allData/ers1/L3/byu_scp/sigma0enhanced/docs/dLongERS1.html.",
-            "issued": "2011-11-21",
-            "temporal": "1992-01-01T00:00:00Z/1996-05-17T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2011-11-21",
-            "keyword": [
-                "spectral/engineering",
-                "radar",
-                "earth science",
-                "cryosphere",
-                "sea ice"
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
-            "identifier": "C2617226208-POCLOUD",
-            "description": "This European Remote Sensing (ERS) Sigma-0 dataset is generated by the Scatterometer Climate Record Pathfinder (SCP) project at Brigham Young University (BYU) and is generated using a Scatterometer Image Reconstruction (SIR) technique developed by Dr. David Long at BYU. The dataset provides SIR processed Sigma-0 data from the ERS-1 C-band scatterometer, which is also known as the Active Microwave Instrument (AMI). AMI is a multimode radar operating at a frequency of 5.3 GHz (C-band), using vertically polarized antennas for both transmission and reception. The SIR technique results in an enhanced resolution image reconstruction and gridded on an equal-area grid (for non-polar regions) at 8.9 km pixel resolution stored in SIR files; polar regions are gridded at the same resolution using a polar-stereographic technique. A non-enhanced version is provided at 44.5 km pixel resolution in a format known as GRD (i.e., gridded) files. All files are produced in IEEE formatted binary. All data files are separated and organized by region, parameter, and sampling technique (i.e., SIR vs. GRD). The regions of China and Japan are combined into a single region. In addition to Sigma-0, various statistical parameters are provided for added guidance, including but not limited to: standard deviation, measurement counts, pixel time, Sigma-0 error, and average incidence angle. This dataset was once distributed on tape, but has been made available on FTP thanks to the BYU SCP.",
-            "release-place": "PO.DAAC",
-            "series-name": "ERS-1 Gridded Level 3 Enhanced Resolution Sigma-0 from BYU",
-            "graphic-preview-description": "Thumbnail",
             "creator": "BYU/SCP",
-            "title": "ERS-1 Gridded Level 3 Enhanced Resolution Sigma-0 from BYU",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ERS-1_BYU_L3_OW_SIGMA0_ENHANCED.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This European Remote Sensing (ERS) Sigma-0 dataset is generated by the Scatterometer Climate Record Pathfinder (SCP) project at Brigham Young University (BYU) and is generated using a Scatterometer Image Reconstruction (SIR) technique developed by Dr. David Long at BYU. The dataset provides SIR processed Sigma-0 data from the ERS-1 C-band scatterometer, which is also known as the Active Microwave Instrument (AMI). AMI is a multimode radar operating at a frequency of 5.3 GHz (C-band), using vertically polarized antennas for both transmission and reception. The SIR technique results in an enhanced resolution image reconstruction and gridded on an equal-area grid (for non-polar regions) at 8.9 km pixel resolution stored in SIR files; polar regions are gridded at the same resolution using a polar-stereographic technique. A non-enhanced version is provided at 44.5 km pixel resolution in a format known as GRD (i.e., gridded) files. All files are produced in IEEE formatted binary. All data files are separated and organized by region, parameter, and sampling technique (i.e., SIR vs. GRD). The regions of China and Japan are combined into a single region. In addition to Sigma-0, various statistical parameters are provided for added guidance, including but not limited to: standard deviation, measurement counts, pixel time, Sigma-0 error, and average incidence angle. This dataset was once distributed on tape, but has been made available on FTP thanks to the BYU SCP.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FERS1B-SNEN0",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FERS1B-SNEN0",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ers1/open/L3/byu_scp/sigma0enhanced/docs/dLongERS1.html",
-                    "description": "Dataset User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Dataset User Guide",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ers1/open/L3/byu_scp/sigma0enhanced/docs/dLongERS1.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ERS-1_BYU_L3_OW_SIGMA0_ENHANCED.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ERS-1_BYU_L3_OW_SIGMA0_ENHANCED.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ers1/open/L3/byu_scp/sigma0enhanced/docs/dLongERS1.html",
-                    "description": "PO.DAAC Drive",
                     "@type": "dcat:Distribution",
+                    "description": "PO.DAAC Drive",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ers1/open/L3/byu_scp/sigma0enhanced/docs/dLongERS1.html",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2617226208-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2617226208-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2617226208-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2617226208-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ERS-1_BYU_L3_OW_SIGMA0_ENHANCED.jpg",
+            "identifier": "C2617226208-POCLOUD",
+            "issued": "2011-11-21",
+            "keyword": [
+                "spectral/engineering",
+                "radar",
+                "earth science",
+                "cryosphere",
+                "sea ice"
+            ],
+            "landingPage": "https://doi.org/10.5067/ERS1B-SNEN0",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2011-11-21",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "PO.DAAC",
+            "series-name": "ERS-1 Gridded Level 3 Enhanced Resolution Sigma-0 from BYU",
             "spatial": "-180.0 -79.7 180.0 88.2",
+            "temporal": "1992-01-01T00:00:00Z/1996-05-17T23:59:59Z",
             "theme": [
                 "SCP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ERS-1 Gridded Level 3 Enhanced Resolution Sigma-0 from BYU"
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
+            "description": "CDA, CIRS, ISS, RADAR, RPWS, RSS, SPICE, UVIS, VIMS",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20090403.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-700",
+            "issued": "2018-06-25",
             "keyword": [
                 "vims",
                 "uvis",
@@ -998866,1122 +998875,1095 @@
                 "cirs",
                 "iss"
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
-            "identifier": "NASA-700",
-            "description": "CDA, CIRS, ISS, RADAR, RPWS, RSS, SPICE, UVIS, VIMS",
-            "title": "PDS Cassini Data Release 17",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20090403.shtml",
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
+            "title": "PDS Cassini Data Release 17"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1658475760-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, OB.DAAC.",
-            "issued": "2019-06-23",
-            "temporal": "2012-01-02T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-08-08",
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
-                "name": "OB.DAAC"
-            },
-            "identifier": "C1658475760-OB_DAAC",
             "description": "The Visible and Infrared Imager/Radiometer Suite (VIIRS) is a multi-disciplinary instrument that is being flown on the Joint Polar Satellite System (JPSS) series of spacecraft, including the Suomi National Polar-orbiting Partnership (S-NPP) that launched in October 2011.  JPSS is a multi-platform, multi-agency program that consolidates the polar orbiting spacecraft of NASA and the National Oceanic and Atmospheric Administration (NOAA).  S-NPP is the initial spacecraft in this series, and VIIRS is the successor to MODIS for Earth science data product generation.  VIIRS has 22 spectral bands ranging from 412 nm to 12 nm.  There are 16 moderate-resolution bands (750m at nadir), 5 image-resolution bands (375m), and one day-night band (DNB).",
-            "title": "Suomi-NPP VIIRS Global Binned 11\u00b5m Daytime Sea Surface Temperature (SST) Data, version 2016.2",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directaccess/VIIRS-SNPP/L3BIN",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directaccess/VIIRS-SNPP/L3BIN",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NPP/VIIRS/L3B/SST/2016.2",
-                    "description": "VIIRS-Suomi-NPP L3B 11\u00b5m Daytime Sea Surface Temperature (SST) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS-Suomi-NPP L3B 11\u00b5m Daytime Sea Surface Temperature (SST) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NPP/VIIRS/L3B/SST/2016.2",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1658475760-OB_DAAC",
+            "issued": "2019-06-23",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "ocean temperature"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1658475760-OB_DAAC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-08-08",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "OB.DAAC"
+            },
             "spatial": "-180.0 90.0 -180.0 90.0",
+            "temporal": "2012-01-02T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Suomi-NPP VIIRS Global Binned 11\u00b5m Daytime Sea Surface Temperature (SST) Data, version 2016.2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/108",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Ungar, S. G. 1994. Soil Impedance Data (FIFE). Data set. Available on-line [http://www.daac.ornl.gov] from Oak Ridge National Laboratory Distributed Active Archive Center, Oak Ridge, Tennessee, U.S.A. Also published in D. E. Strebel, D. R. Landis, K. F. Huemmrich, and B. W. Meeson (eds.), Collected Data of the First ISLSCP Field Experiment, Vol. 1: Surface Observations and Non-Image Data Sets. CD-ROM. National Aeronautics and Space Administration, Goddard Space Flight Center, Greenbelt, Maryland, U.S.A. (available from http://www.daac.ornl.gov). doi:10.3334/ORNLDAAC/108",
-            "issued": "2024-05-06",
-            "temporal": "1987-05-24T00:00:00Z/1989-08-10T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-07",
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
-            "identifier": "C2980623813-ORNL_CLOUD",
             "description": "Soil impedance & temperature measured with Radio Frequency Soil Moisture Probe",
-            "graphic-preview-description": "Browse Image",
-            "title": "Soil Impedance Data (FIFE)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/fife_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F108",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F108",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_soilmstr_soil_imp/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_soilmstr_soil_imp/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/Soil_Impedance_Data.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/Soil_Impedance_Data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/108",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/108",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_soilmstr_soil_imp/comp/soil_imp.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_soilmstr_soil_imp/comp/soil_imp.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_soilmstr_soil_imp/comp/soil_imp.tdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_soilmstr_soil_imp/comp/soil_imp.tdf",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_soilmstr_soil_imp/comp/Soil_Impedance_Data.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_soilmstr_soil_imp/comp/Soil_Impedance_Data.pdf",
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
+            "identifier": "C2980623813-ORNL_CLOUD",
+            "issued": "2024-05-06",
+            "keyword": [
+                "soils",
+                "land surface",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/108",
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
             "spatial": "-96.61 38.98 -96.47 39.09",
+            "temporal": "1987-05-24T00:00:00Z/1989-08-10T23:59:59Z",
             "theme": [
                 "FIFE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Soil Impedance Data (FIFE)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL2TCST_L2.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MISR Science Team (2015), Terra/MISR Level 2, TOA/Cloud Stereo, version 2, Hampton, VA, USA: NASA Atmospheric Science Data Center (ASDC), Accessed <author citing data inserts date here> at doi: 10.5067/Terra/MISR/MIL2TCST_L2.002",
-            "issued": "2003-03-24",
-            "temporal": "2000-02-24T16:33:37Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-10-15",
-            "keyword": [
-                "earth science",
-                "clouds",
-                "atmosphere"
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
-            "identifier": "C43677714-LARC",
             "description": "Multi-angle Imaging SpectroRadiometer (MISR) is an instrument designed to view Earth with cameras pointed in 9 different directions. As the instrument flies overhead, each piece of Earth's surface below is successively imaged by all 9 cameras, in each of 4 wavelengths (blue, green, red, and near-infrared). The goal of MISR is to improve our understanding of the fate of sunlight in Earth environment, as well as distinguish different types of clouds, particles and surfaces. Specifically, MISR monitors the monthly, seasonal, and long-term trends in three areas: 1) amount and type of atmospheric particles (aerosols), including those formed by natural sources and by human activities; 2) amounts, types, and heights of clouds, and 3) distribution of land surface cover, including vegetation canopy structure. MISR Level 2 TOA/Cloud Stereo parameters V002 contains the Stereoscopically Derived Cloud Mask (SDCM), cloud winds, Reflecting Level Reference Altitude (RLRA), with associated data.",
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "title": "MISR Level 2 TOA/Cloud Stereo parameters V002",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL2TCST_L2.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL2TCST_L2.002",
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
+            "identifier": "C43677714-LARC",
+            "issued": "2003-03-24",
+            "keyword": [
+                "earth science",
+                "clouds",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL2TCST_L2.002",
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
+            "title": "MISR Level 2 TOA/Cloud Stereo parameters V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1286874966-LAADS.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "European Space Agency. 2016-08-01. OLCI/Sentinel-3A L1 Full Resolution Top of Atmosphere Reflectance. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/HBSL/BISB/MODAPS. https://www.esa.int/Our_Activities/Observing_the_Earth/Copernicus/Overview3.",
-            "issued": "2016-08-01",
-            "temporal": "2016-04-25T11:33:14Z/2025-01-06T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-03",
-            "keyword": [
-                "earth science",
-                "platform characteristics",
-                "atmospheric radiation",
-                "atmosphere",
-                "visible wavelengths",
-                "infrared wavelengths",
-                "spectral/engineering"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sentinel Data Technical support",
                 "hasEmail": "mailto:ops@eumetsat.int"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/HBSL/BISB/MODAPS"
-            },
-            "identifier": "C1286874966-LAADS",
-            "description": "The OLCI/Sentinel-3A L1 Full Resolution Top of Atmosphere Reflectance product, S3A_OL_1_EFR is generated from the data aquired by the Ocean and Land Colour Instrument (OLCI) on board European Earth Observation satellite mission, SENTINEL-3. The OLCI is a push-broom imaging spectrometer that measures solar radiation reflected by the Earth at a ground spatial resolution of around 300m, over all surfaces, in 21 spectral bands. OLCI is based on the imaging design of ENVISAT's Medium Resolution Imaging Spectrometer (MERIS). It has a 1270km wide swath. \r\n\r\nFor more information about the instrument and the mission, visit \"Sentinel Online\" at https://sentinel.esa.int/web/sentinel/home. \r\n\r\nThe S3A_OL_1_EFR is a Level-1B product. This is composed of an information package map, called a manifest, 22 measurement data files, and seven annotation data files. The 21 measurement data files (one for each band) consist of Top Of Atmosphere (TOA) radiances, calibrated to geophysical units (W.m-2. sr-1 Micro meter-1), georeferenced onto the Earth's surface, and spatially resampled onto an evenly spaced grid. Seven annotation files provide information on illumination and observation geometry, environment data (meteorological data) and quality and classification flags. Both measurement data files and annotation data files are written in netCDF 4 format. The manifest file is in XML format and contains metadata associated with the instrument and the processing. The S3A_OL_1_EFR is generated in Earth Observation (EO) processing mode and all parameters in this product are provided for each re-gridded pixel on the product image and for each removed pixel.\r\n\r\n\r\nThe OL_1_EFR product package is described below:\r\n\r\nElement name \t             Description\r\nManifest.safe \t        SENTINEL-SAFE product manifest\r\nOa##_radiance.nc \tRadiance for OLCI acquisition bands 01 to 21\r\nRemoved_pixels.nc \tRemoved pixels information needed for Level-1C generation\r\nTime_coordinates.nc \tTime stamp annotations\r\nGeo_coordinates.nc \tHigh resolution georeferencing data\r\nQuality_flags.nc \tClassification and quality flags\r\nTie_geo_coordinates.nc \tLow resolution georeferencing data\r\nTie_geometries.nc \tSun and view angles\r\nTie_meteo.nc \t        ECMWF meteorology data\r\nInstrument_data.nc \tInstrument data\r\n\r\nnote: Oa## represents all the OLCI channels (Oa1 to Oa21).\r\n\r\n\r\nFor more information about the product, read the SENTINEL-3 OLCI User Guide at https://sentinel.esa.int/web/sentinel/user-guides/sentinel-3-olci.",
             "creator": "European Space Agency",
-            "title": "OLCI/Sentinel-3A L1 Full Resolution Top of Atmosphere Reflectance",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The OLCI/Sentinel-3A L1 Full Resolution Top of Atmosphere Reflectance product, S3A_OL_1_EFR is generated from the data aquired by the Ocean and Land Colour Instrument (OLCI) on board European Earth Observation satellite mission, SENTINEL-3. The OLCI is a push-broom imaging spectrometer that measures solar radiation reflected by the Earth at a ground spatial resolution of around 300m, over all surfaces, in 21 spectral bands. OLCI is based on the imaging design of ENVISAT's Medium Resolution Imaging Spectrometer (MERIS). It has a 1270km wide swath. \r\n\r\nFor more information about the instrument and the mission, visit \"Sentinel Online\" at https://sentinel.esa.int/web/sentinel/home. \r\n\r\nThe S3A_OL_1_EFR is a Level-1B product. This is composed of an information package map, called a manifest, 22 measurement data files, and seven annotation data files. The 21 measurement data files (one for each band) consist of Top Of Atmosphere (TOA) radiances, calibrated to geophysical units (W.m-2. sr-1 Micro meter-1), georeferenced onto the Earth's surface, and spatially resampled onto an evenly spaced grid. Seven annotation files provide information on illumination and observation geometry, environment data (meteorological data) and quality and classification flags. Both measurement data files and annotation data files are written in netCDF 4 format. The manifest file is in XML format and contains metadata associated with the instrument and the processing. The S3A_OL_1_EFR is generated in Earth Observation (EO) processing mode and all parameters in this product are provided for each re-gridded pixel on the product image and for each removed pixel.\r\n\r\n\r\nThe OL_1_EFR product package is described below:\r\n\r\nElement name \t             Description\r\nManifest.safe \t        SENTINEL-SAFE product manifest\r\nOa##_radiance.nc \tRadiance for OLCI acquisition bands 01 to 21\r\nRemoved_pixels.nc \tRemoved pixels information needed for Level-1C generation\r\nTime_coordinates.nc \tTime stamp annotations\r\nGeo_coordinates.nc \tHigh resolution georeferencing data\r\nQuality_flags.nc \tClassification and quality flags\r\nTie_geo_coordinates.nc \tLow resolution georeferencing data\r\nTie_geometries.nc \tSun and view angles\r\nTie_meteo.nc \t        ECMWF meteorology data\r\nInstrument_data.nc \tInstrument data\r\n\r\nnote: Oa## represents all the OLCI channels (Oa1 to Oa21).\r\n\r\n\r\nFor more information about the product, read the SENTINEL-3 OLCI User Guide at https://sentinel.esa.int/web/sentinel/user-guides/sentinel-3-olci.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/450/",
-                    "description": "Direct access to S3A_OL_1_EFR C1 data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to S3A_OL_1_EFR C1 data set.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/450/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sentinel.esa.int/web/sentinel/user-guides/sentinel-3-olci/processing-levels/level-1",
-                    "description": "The Sentinel-3 OLCI  Level 1 product user guide.",
                     "@type": "dcat:Distribution",
+                    "description": "The Sentinel-3 OLCI  Level 1 product user guide.",
+                    "downloadURL": "https://sentinel.esa.int/web/sentinel/user-guides/sentinel-3-olci/processing-levels/level-1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "identifier": "C1286874966-LAADS",
+            "issued": "2016-08-01",
+            "keyword": [
+                "earth science",
+                "platform characteristics",
+                "atmospheric radiation",
+                "atmosphere",
+                "visible wavelengths",
+                "infrared wavelengths",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1286874966-LAADS.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-03",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/HBSL/BISB/MODAPS"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2016-04-25T11:33:14Z/2025-01-06T00:00:00Z",
             "theme": [
                 "Sentinel-3A",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OLCI/Sentinel-3A L1 Full Resolution Top of Atmosphere Reflectance"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2043",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hook, S.J., J.S. Myers, K.J. Thome, M. Fitzgerald, A.B. Kahle,  Airborne Sensor Facility NASA Ames Research Center, T.H. Painter, J. Dozier, and C.C. Moeller. 2022. MASTER: Airborne Science, Western US, April, 2004. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2043",
-            "issued": "2023-07-09",
-            "temporal": "2004-04-01T01:58:28Z/2004-04-13T20:03:08Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-13",
-            "keyword": [
-                "visible wavelengths",
-                "earth science",
-                "infrared wavelengths",
-                "spectral/engineering",
-                "ocean temperature",
-                "oceans",
-                "surface radiative properties",
-                "surface thermal properties",
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
-            "identifier": "C2731750468-ORNL_CLOUD",
             "description": "This dataset includes Level 1B (L1B) and Level 2 (L2) data products from the MODIS/ASTER Airborne Simulator (MASTER) instrument. The spectral data were collected during four flights aboard a NASA ER-2 aircraft over western U.S. and Pacific Ocean from 2004-04-01 to 2004-04-13. This deployment was coordinated by NASA's Dryden Flight Research Center (DRFC), renamed Armstrong Flight Research Center in 2014, located in Edwards, California. Data products include L1B georeferenced multispectral imagery of calibrated radiance in 50 bands covering wavelengths of 0.460 to 12.879 micrometers at approximately 50-meter spatial resolution. Derived L2 data products are emissivity in 5 bands in thermal infrared range (8.58 to 12.13 micrometers) and land surface temperature. The L1B file format is HDF-4, and L2 products are provided in ENVI and KMZ formats. In addition, the dataset includes flight paths, spectral band information, instrument configuration, ancillary notes, and summary information for each flight, and browse images derived from each L1B data file.",
-            "graphic-preview-description": "Single-band images and a RGB composite image from flight track 2 as acquired on 05 April 2004 over Crowley Lake southeast of Lee Vining, California, U.S. Source: MASTERL1B_0491900_02_20040405_1859_1901_V01.jpg",
-            "title": "MASTER: Airborne Science, Western US, April, 2004",
-            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_DFRC_April_2004_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2043",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2043",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/master/MASTER_DFRC_April_2004/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/master/MASTER_DFRC_April_2004/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_DFRC_April_2004.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_DFRC_April_2004.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2043",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2043",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_DFRC_April_2004/comp/MASTER_DFRC_April_2004.pdf",
-                    "description": "MASTER: Airborne Science, Western US, April, 2004: MASTER_DFRC_April_2004.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "MASTER: Airborne Science, Western US, April, 2004: MASTER_DFRC_April_2004.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_DFRC_April_2004/comp/MASTER_DFRC_April_2004.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_DFRC_April_2004_Fig1.jpg",
-                    "description": "Single-band images and a RGB composite image from flight track 2 as acquired on 05 April 2004 over Crowley Lake southeast of Lee Vining, California, U.S. Source: MASTERL1B_0491900_02_20040405_1859_1901_V01.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Single-band images and a RGB composite image from flight track 2 as acquired on 05 April 2004 over Crowley Lake southeast of Lee Vining, California, U.S. Source: MASTERL1B_0491900_02_20040405_1859_1901_V01.jpg",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_DFRC_April_2004_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Single-band images and a RGB composite image from flight track 2 as acquired on 05 April 2004 over Crowley Lake southeast of Lee Vining, California, U.S. Source: MASTERL1B_0491900_02_20040405_1859_1901_V01.jpg",
+            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_DFRC_April_2004_Fig1.jpg",
+            "identifier": "C2731750468-ORNL_CLOUD",
+            "issued": "2023-07-09",
+            "keyword": [
+                "visible wavelengths",
+                "earth science",
+                "infrared wavelengths",
+                "spectral/engineering",
+                "ocean temperature",
+                "oceans",
+                "surface radiative properties",
+                "surface thermal properties",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2043",
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
             "spatial": "-129.38 27.06 -101.25 45.09",
+            "temporal": "2004-04-01T01:58:28Z/2004-04-13T20:03:08Z",
             "theme": [
                 "MASTER",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MASTER: Airborne Science, Western US, April, 2004"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RPCLAP-2-CVP2-EDITED2-V1.0",
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
+            "description": "This data set contains EDITED\ndata from Rosetta RPC-LAP, acquired during the COMMISSIONING 2 mission\nphase where there was no primary target. It contains uncalibrated raw\ndata, i.e. the digital output of the instrument.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rpclap-2-cvp2-edited2-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "checkout"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RPCLAP-2-CVP2-EDITED2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rpclap-2-cvp2-edited2-v1.0",
-            "description": "This data set contains EDITED\ndata from Rosetta RPC-LAP, acquired during the COMMISSIONING 2 mission\nphase where there was no primary target. It contains uncalibrated raw\ndata, i.e. the digital output of the instrument.",
-            "title": "ROSETTA-ORBITER CHECK RPCLAP\n2 CVP2 EDITED2 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECK RPCLAP\n2 CVP2 EDITED2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-RSS-1-SROC13-V1.0",
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
+            "description": "The Cassini Radio Science Saturn Ring and Atmospheric Occultation experiments (SROC13) Raw Data Archive is a time-ordered collection of radio science raw data acquired on July 24 and September 2, 2010, during the Cassini Extended Mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-rss-1-sroc13-v1.0_jvvm-u9jw",
+            "issued": "2021-05-21",
+            "keyword": [
+                "saturn",
+                "cassini-huygens"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-RSS-1-SROC13-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-rss-1-sroc13-v1.0_jvvm-u9jw",
-            "description": "The Cassini Radio Science Saturn Ring and Atmospheric Occultation experiments (SROC13) Raw Data Archive is a time-ordered collection of radio science raw data acquired on July 24 and September 2, 2010, during the Cassini Extended Mission.",
-            "title": "CASSINI RSS RAW DATA SET - SROC13 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI RSS RAW DATA SET - SROC13 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LCROSS-X-NSP2-FL-2-RAW-V1.0",
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
-                "lunar crater observation and sensing satellite"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Raw, uncalibrated flash mode spectra from the Near Infrared Spectrometer 2 (NSP2) aboard the Lunar Crater Observation and Sensing Satellite (LCROSS).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lcross-x-nsp2-fl-2-raw-v1.0_jvw8-v2ks",
+            "issued": "2018-06-26",
+            "keyword": [
+                "sun",
+                "lunar crater observation and sensing satellite"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LCROSS-X-NSP2-FL-2-RAW-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lcross-x-nsp2-fl-2-raw-v1.0_jvw8-v2ks",
-            "description": "Raw, uncalibrated flash mode spectra from the Near Infrared Spectrometer 2 (NSP2) aboard the Lunar Crater Observation and Sensing Satellite (LCROSS).",
-            "title": "LCROSS SUN 2ND NEAR IR SPECTROMETER FLASH 2 RAW V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "LCROSS SUN 2ND NEAR IR SPECTROMETER FLASH 2 RAW V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GOES-18/CERES/GEO_Ed4_GOE18_SH_V01.2",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2018-08-08. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/GOES-18/CERES/GEO_Ed4_GOE18_SH_V01.2.",
-            "issued": "2023-04-07",
-            "temporal": "2023-01-04T00:00:00Z/2023-06-12T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-07",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "clouds"
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
-            "identifier": "C2650019074-LARC_ASDC",
             "description": "CER_GEO_Ed4_GOE18_SH_V01.2 is the Satellite ClOud and Radiation Property retrieval System (SatCORPS) Clouds and the Earth's Radiant Energy System (CERES) Geostationary Satellite (GEO) Edition 4 Geostationary Operational Environmental Satellite 18 (GOES-18) over the Southern Hemisphere (SH) Version 1.2 data product. Data was collected using the GOES-18 Imager on the GOES-18 Platform. Data collection for this product is in progress. \r\n\r\nThis data set is comprised of cloud micro-physical and radiation properties derived hourly from GOES-18 geostationary satellite imager data using the Langley Research Center (LaRC) SATCORPS algorithms in support of the CERES project. The cloud microphysical and radiation properties from each active geostationary satellite are merged together to create hourly global cloud properties that are used to estimate fluxes between CERES instrument measurements to account for the changing diurnal cycle. The data set is arranged as files for each hour and in netCDF-4 format. The observations are at 4-km resolution (at nadir) and are sub-sampled to 8 km.\r\n\r\nCERES is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions are a follow-on to the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument, the proto flight model (PFM), was launched on November 27, 1997, as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit onboard the Earth Observing System (EOS) flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched onboard Earth Observing System (EOS) Aqua on May 4, 2002. The CERES FM5 instrument was launched onboard the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The newest CERES instrument (FM6) was launched onboard the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite, now called NOAA-20, on November 18, 2017.",
-            "title": "SatCORPS CERES GEO Edition 4 GOES-18 Southern Hemisphere Version 1.2",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGOES-18%2FCERES%2FGEO_Ed4_GOE18_SH_V01.2",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGOES-18%2FCERES%2FGEO_Ed4_GOE18_SH_V01.2",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2650019074-LARC_ASDC",
-                    "description": "Earthdata Search for CER_GEO_Ed4_GOE18_SH_V01.2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CER_GEO_Ed4_GOE18_SH_V01.2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2650019074-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/GOES-18/CERES/GEO_Ed4_GOE18_SH_V01.2",
-                    "description": "DOI data set landing page for CER_GEO_Ed4_GOE18_SH_V01.2",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CER_GEO_Ed4_GOE18_SH_V01.2",
+                    "downloadURL": "https://doi.org/10.5067/GOES-18/CERES/GEO_Ed4_GOE18_SH_V01.2",
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
-                    "downloadURL": "https://eospso.gsfc.nasa.gov/atbd-category/40",
-                    "description": "CERES ATBD",
                     "@type": "dcat:Distribution",
+                    "description": "CERES ATBD",
+                    "downloadURL": "https://eospso.gsfc.nasa.gov/atbd-category/40",
+                    "mediaType": "text/html",
                     "title": "View this dataset's algorithm theoretical basis document"
                 }
             ],
+            "identifier": "C2650019074-LARC_ASDC",
+            "issued": "2023-04-07",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "clouds"
+            ],
+            "landingPage": "https://doi.org/10.5067/GOES-18/CERES/GEO_Ed4_GOE18_SH_V01.2",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-04-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-60.0 -180.0 -60.0 -90.0 0.0 -90.0 0.0 -180.0 -60.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2023-01-04T00:00:00Z/2023-06-12T00:00:00Z",
             "theme": [
                 "CERES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SatCORPS CERES GEO Edition 4 GOES-18 Southern Hemisphere Version 1.2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ICESAT/GLAS/DATA104",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "GLAS/ICESat L1A Global Laser Pointing Data (HDF5) V033. Version 033. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/ICESAT/GLAS/DATA104.",
-            "issued": "2003-02-20",
-            "temporal": "2003-02-20T00:00:00Z/2009-10-11T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2009-10-11",
-            "keyword": [
-                "spectral/engineering",
-                "earth science",
-                "platform characteristics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "H. Zwally",
                 "hasEmail": "mailto:Jay.Zwally@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C189991864-NSIDC_ECS",
             "description": "Level-1A global laser pointing data (GLAH04) contain two orbits of attitude data from the spacecraft star tracker, instrument star tracker, gyro, and laser reference system, and other spacecraft attitude data required to calculate precise laser pointing.",
-            "title": "GLAS/ICESat L1A Global Laser Pointing Data (HDF5) V033",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FICESAT%2FGLAS%2FDATA104",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FICESAT%2FGLAS%2FDATA104",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/GLAS/GLAH04.033",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/GLAS/GLAH04.033",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C189991864-NSIDC_ECS&m=-31.921875%210%211%211%210%210%2C2&q=GLAH04",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C189991864-NSIDC_ECS&m=-31.921875%210%211%211%210%210%2C2&q=GLAH04",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/GLAH04/versions/33/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/GLAH04/versions/33/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ICESAT/GLAS/DATA104",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/ICESAT/GLAS/DATA104",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ICESAT/GLAS/DATA104",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ICESAT/GLAS/DATA104",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C189991864-NSIDC_ECS",
+            "issued": "2003-02-20",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "platform characteristics"
+            ],
+            "landingPage": "https://doi.org/10.5067/ICESAT/GLAS/DATA104",
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
+            "title": "GLAS/ICESat L1A Global Laser Pointing Data (HDF5) V033"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H400001D",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Seirup, L., and G. Yetman. 2005-09-13. U.S. Population Grids (Summary File 1), 2000: Alabama, Louisiana, Mississippi and Texas, Alpha Version. Version alpha. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H400001D. https://doi.org/10.7927/H400001D.",
-            "issued": "2005-09-13",
-            "temporal": "2000-04-01T00:00:00Z/2000-04-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2005-09-13",
-            "references": [
-                "https://doi.org/10.7927/H4QJ7F75",
-                "https://doi.org/10.7927/H4V985ZG",
-                "https://doi.org/10.7927/H4KS6PHF",
-                "https://doi.org/10.7927/H4G15XS1"
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
-            "identifier": "C2214242102-SEDAC",
-            "description": "The U.S. Population Grids (Summary File 1), 2000: Alabama, Louisiana, Mississippi and Texas, Alpha Version data set contains an ARC/INFO Workspace with grids of demographic data from the year 2000 census. The grids have a resolution of 30 arc-seconds (0.0083 decimal degrees), or approximately 1 square km. The gridded variables are based on census block geography from Census 2000 TIGER/Line Files and census variables (population, households, and housing variables). This data set is produced by the Columbia University Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Seirup, L., and G. Yetman",
-            "title": "U.S. Population Grids (Summary File 1), 2000: Alabama, Louisiana, Mississippi and Texas, Alpha Version",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/pend/pend-summary-file1-2000-alabama-louisiana-mississippi-texas/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The U.S. Population Grids (Summary File 1), 2000: Alabama, Louisiana, Mississippi and Texas, Alpha Version data set contains an ARC/INFO Workspace with grids of demographic data from the year 2000 census. The grids have a resolution of 30 arc-seconds (0.0083 decimal degrees), or approximately 1 square km. The gridded variables are based on census block geography from Census 2000 TIGER/Line Files and census variables (population, households, and housing variables). This data set is produced by the Columbia University Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH400001D",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH400001D",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/pend/pend-summary-file1-2000-alabama-louisiana-mississippi-texas/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/pend/pend-summary-file1-2000-alabama-louisiana-mississippi-texas/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/pend-summary-file1-2000-alabama-louisiana-mississippi-texas/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/pend-summary-file1-2000-alabama-louisiana-mississippi-texas/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/pend-summary-file1-2000-alabama-louisiana-mississippi-texas/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/pend-summary-file1-2000-alabama-louisiana-mississippi-texas/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/pend-summary-file1-2000-alabama-louisiana-mississippi-texas",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/pend-summary-file1-2000-alabama-louisiana-mississippi-texas",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/pend/pend-summary-file1-2000-alabama-louisiana-mississippi-texas/sedac-logo.jpg",
+            "identifier": "C2214242102-SEDAC",
+            "issued": "2005-09-13",
+            "keyword": [
+                "population",
+                "human dimensions",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.7927/H400001D",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2005-09-13",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H4QJ7F75",
+                "https://doi.org/10.7927/H4V985ZG",
+                "https://doi.org/10.7927/H4KS6PHF",
+                "https://doi.org/10.7927/H4G15XS1"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-95.0 28.0 -84.0 36.0",
+            "temporal": "2000-04-01T00:00:00Z/2000-04-01T00:00:00Z",
             "theme": [
                 "PEND",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "U.S. Population Grids (Summary File 1), 2000: Alabama, Louisiana, Mississippi and Texas, Alpha Version"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1037-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-09-16T14:42:05.000 to 2015-09-16T17:32:19.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1037-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1037-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1037-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-09-16T14:42:05.000 to 2015-09-16T17:32:19.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1037 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1037 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2HCNNS.008",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AURA/TES/TL2HCNNS.008. https://asdc.larc.nasa.gov/project/TES.",
-            "issued": "2019-02-27",
-            "temporal": "2004-09-13T00:00:00Z/2018-01-22T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "earth science",
-                "atmosphere",
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
-            "identifier": "C1619907953-LARC",
             "description": "TL2HCNNS_8 is the Tropospheric Emission Spectrometer (TES)/Aura Level 2 Hydrogen Cyanide Nadir Special Observation Version 8 data product. TES Level 2 data contain retrieved species (or temperature) profiles at the observation targets and the estimated errors. The geolocation, quality, and other data (e.g., surface characteristics for nadir observations) are also provided. L2 modeled spectra are evaluated using radiative transfer modeling algorithms. The process, referred to as retrieval, compares observed spectra to the modeled spectra and iteratively updates the atmospheric parameters. L2 standard product files include information for one molecular species (or temperature) for an entire global survey or special observation run. A global survey consists of a maximum of 16 consecutive orbits.\rA Nadir sequence within the TES Global Survey is a fixed number of observations within an orbit for a Global Survey. Prior to April 24, 2005, it consisted of two low resolution scans over the same ground locations. After April 24, 2005, Global Survey data consisted of three low resolution scans. The Nadir standard product consists of four files, where each file is composed of the Global Survey Nadir observations from one of four focal planes for a single orbit, i.e. 72 orbit sequences. The Global Survey Nadir observations currently only use a single set of filter mix.\r\rA Global Survey consists of observations along 16 consecutive orbits at the start of a two day cycle, over which 3,200 retrievals are performed. Each observation is the input for retrievals of species Volume Mixing Ratios (VMR), temperature profiles, surface temperature and other data parameters with associated pressure levels, precision, total error, vertical resolution, total column density and other diagnostic quantities. Each TES Level 2 standard product reports information in a swath format conforming to the HDF-EOS Aura File Format Guidelines. Each Swath object is bounded by the number of observations in a global survey and a predefined set of pressure levels representing slices through the atmosphere. Each standard product can have a variable number of observations depending upon the Global Survey configuration and whether averaging is employed. Also, missing or bad retrievals are not reported.\r\rThe organization of data within the Swath object is based on a superset of the UARS pressure levels used to report concentrations of trace atmospheric gases. The reporting grid is the same pressure grid used for modeling. There are 67 reporting levels from 1211.53 hPa, which allows for very high surface pressure conditions, to 0.1 hPa, about 65 km. In addition, the products will report values directly at the surface when possible or at the observed cloud top level. Thus in the Standard Product files each observation can potentially contain estimates for the concentration of a particular molecule at 67 different pressure levels within the atmosphere. However, for most retrieved profiles, the highest pressure levels are not observed due to a surface at lower pressure or cloud obscuration. For pressure levels corresponding to altitudes below the cloud top or surface, where measurements were not possible, a fill value will be applied. \r\rTo minimize the duplication of information between the individual species standard products, data fields common to each species (such as spacecraft coordinates, emissivities, and other data fields) have been collected into a separate standard product, termed the TES L2 Ancillary Data product (ESDT short name: TL2ANC). Users of this product should also obtain the Ancillary Data product.",
-            "title": "TES/Aura L2 Hydrogen Cyanide Nadir Special Observation V008",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2HCNNS.008",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2HCNNS.008",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/TES",
-                    "description": "ASDC Data and Information for TES",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for TES",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/TES",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2HCNNS.008",
-                    "description": "DOI data set landing page for TL2HCNNS_8",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TL2HCNNS_8",
+                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2HCNNS.008",
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
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2HCNNS.008/contents.html",
-                    "description": "OPeNDAP data access for TL2HCNNS_8",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for TL2HCNNS_8",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2HCNNS.008/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1619907953-LARC",
-                    "description": "Earthdata Search for TL2HCNNS_8 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TL2HCNNS_8 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1619907953-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2HCNNS.008/",
-                    "description": "ASDC Direct Data Download for TL2HCNNS_8",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for TL2HCNNS_8",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2HCNNS.008/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/cgi-bin/DUE/tes_L2SpecObs.cgi",
-                    "description": "Report of TES Level 2 Special Observation Products Available from the ASDC",
                     "@type": "dcat:Distribution",
+                    "description": "Report of TES Level 2 Special Observation Products Available from the ASDC",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/cgi-bin/DUE/tes_L2SpecObs.cgi",
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
+            "identifier": "C1619907953-LARC",
+            "issued": "2019-02-27",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2HCNNS.008",
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
+            "title": "TES/Aura L2 Hydrogen Cyanide Nadir Special Observation V008"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DII-CAL-ITS-2-NAV-9P-CRUISE-V1.0",
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
+            "description": "This data set contains raw calibration and test images acquired by the Deep Impact Impactor Targeting Sensor Visible CCD during the cruise phase of the mission. These observations were used for optical and autonomous navigation (NAV) of the impactor spacecraft. These data were collected from 7 April to 30 April 2005. The comet was not imaged during cruise.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dii-cal-its-2-nav-9p-cruise-v1.0_jw8s-buzf",
+            "issued": "2018-06-26",
+            "keyword": [
+                "deep impact",
+                "calibration"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DII-CAL-ITS-2-NAV-9P-CRUISE-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dii-cal-its-2-nav-9p-cruise-v1.0_jw8s-buzf",
-            "description": "This data set contains raw calibration and test images acquired by the Deep Impact Impactor Targeting Sensor Visible CCD during the cruise phase of the mission. These observations were used for optical and autonomous navigation (NAV) of the impactor spacecraft. These data were collected from 7 April to 30 April 2005. The comet was not imaged during cruise.",
-            "title": "DEEP IMPACT 9P/TEMPEL CRUISE - RAW ITS NAV IMAGES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "DEEP IMPACT 9P/TEMPEL CRUISE - RAW ITS NAV IMAGES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-MAG-4-RDR-HGCOORDS-48.0SEC-V1.0",
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
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-mag-4-rdr-hgcoords-48.0sec-v1.0_jw8w-55tg",
+            "issued": "2021-05-21",
+            "keyword": [
+                "voyager",
+                "jupiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-MAG-4-RDR-HGCOORDS-48.0SEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-mag-4-rdr-hgcoords-48.0sec-v1.0_jw8w-55tg",
-            "description": "not applicable",
-            "title": "VG1 JUP MAG RESAMPLED HELIOGRAPHIC (RTN) COORDS 48.0SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG1 JUP MAG RESAMPLED HELIOGRAPHIC (RTN) COORDS 48.0SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-POS-4-SUMM-L1COORDS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-pos-4-summ-l1coords-v1.0_jwf8-54mk",
+            "issued": "2018-06-26",
+            "keyword": [
+                "voyager",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-POS-4-SUMM-L1COORDS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-pos-4-summ-l1coords-v1.0_jwf8-54mk",
-            "description": "not applicable",
-            "title": "VG2 SAT EPHEMERIS KRONOGRAPHIC (L1) COORDS BROWSE V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG2 SAT EPHEMERIS KRONOGRAPHIC (L1) COORDS BROWSE V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/jwgt-3cdb",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "temporal": "1977-01-01/2014-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "geography",
-                "nen",
-                "space science",
-                "wise"
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
-            "identifier": "NASA-0000038__1",
+            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
             "description": "Planetary nomenclature, like terrestrial nomenclature, is used to uniquely identify a feature on the surface of a planet or satellite so that the feature can be easily located, described, and discussed. This gazetteer contains detailed information about all names of topographic and albedo features on planets and satellites (and some planetary ring and ring-gap systems) that the International Astronomical Union (IAU) has named and approved from its founding in 1919 through the present time.",
-            "title": "Gazetteer of Planetary Nomenclature",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -999989,748 +999971,741 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
-            "accrualPeriodicity": "irregular"
+            "identifier": "NASA-0000038__1",
+            "issued": "2018-06-25",
+            "keyword": [
+                "geography",
+                "nen",
+                "space science",
+                "wise"
+            ],
+            "landingPage": "https://data.nasa.gov/d/jwgt-3cdb",
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
-            "issue-identification": "GSSTF_F08_2c",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/MEASURES/GSSTF/DATA321",
             "citation": "Shie, C.-L., K. Hilburn, L. S. Chiu, R. Adler, I-I Lin, E. Nelkin, and J. Ardizzone. Andrey Savtchenko. 2011-11-18. GSSTF_F08. Version 2c. Goddard Satellite-Based Surface Turbulent Fluxes, 1x1 deg Daily Grid, Satellite F08 V2c. Greenbelt, MD, USA. GSSTF_F08_2c. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/MEASURES/GSSTF/DATA321. https://disc.gsfc.nasa.gov/datacollection/GSSTF_F08_2c.html. Digital Science Data.",
-            "issued": "2011-11-18",
-            "temporal": "1987-07-09T00:00:00Z/1992-01-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2011-11-18",
-            "keyword": [
-                "atmospheric pressure",
-                "ocean winds",
-                "ocean temperature",
-                "oceans",
-                "ocean pressure",
-                "ocean heat budget",
-                "earth science",
-                "atmospheric winds",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "atmospheric radiation",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DAVID SILBERSTEIN",
                 "hasEmail": "mailto:david.s.silberstein@nasa.gov"
             },
+            "creator": "Shie, C.-L., K. Hilburn, L. S. Chiu, R. Adler, I-I Lin, E. Nelkin, and J. Ardizzone",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1237113365-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "These data are part of the Goddard Satellite-based Surface Turbulent Fluxes Version-2c (GSSTF 2c) Dataset recently produced through a MEaSURES funded project led by Dr. Chung-Lin Shie (UMBC/GEST, NASA/GSFC), converted to HDF-EOS5 format. The stewardship of this HDF-EOS5 dataset is part of the MEaSUREs project. \n\nThis is a Daily (24-hour) product; data are projected to equidistant Grid that covers the globe at 1x1 degree cell size, resulting in data arrays of 360x180 size. \n\nThe daily fluxes  are produced for each individual available SSM/I satellite tapes (e.g., F08, F10, F11, F13, F14 and F15), and then serve as input to the Combined daily fluxes (GSSTF_2c). A finer resolution, 0.25 deg,  of this product has been released as Version 3.\n      \n      The short name of this data set is GSSTF_F08.",
-            "editor": "Andrey Savtchenko",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "GSSTF_F08",
-            "creator": "Shie, C.-L., K. Hilburn, L. S. Chiu, R. Adler, I-I Lin, E. Nelkin, and J. Ardizzone",
-            "graphic-preview-description": "Goddard Satellite-based Surface Turbulent Fluxes (GSSTF)  Satellite F08 Total Precipitable Water 1 x 1 degree 01/01/1991 [g/cm2]",
-            "title": "Goddard Satellite-Based Surface Turbulent Fluxes, 1x1 deg Daily Grid, Satellite F08 V2c (GSSTF_F08) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GSSTF_F08_2c.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FGSSTF%2FDATA321",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FGSSTF%2FDATA321",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GSSTF_F08_2c.png",
-                    "description": "Goddard Satellite-based Surface Turbulent Fluxes (GSSTF)  Satellite F08 Total Precipitable Water 1 x 1 degree 01/01/1991 [g/cm2]\n      ",
                     "@type": "dcat:Distribution",
+                    "description": "Goddard Satellite-based Surface Turbulent Fluxes (GSSTF)  Satellite F08 Total Precipitable Water 1 x 1 degree 01/01/1991 [g/cm2]\n      ",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GSSTF_F08_2c.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GSSTF_F08_2c.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GSSTF_F08_2c.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/GSSTF/GSSTF_F08.2c/",
-                    "description": "Access the data via HTTP.\n      ",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.\n      ",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/GSSTF/GSSTF_F08.2c/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/GSSTF/GSSTF_F08.2c/doc/Readme.GSSTF2c.pdf",
-                    "description": "README Document\n      ",
                     "@type": "dcat:Distribution",
+                    "description": "README Document\n      ",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/GSSTF/GSSTF_F08.2c/doc/Readme.GSSTF2c.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GSSTF/Science_of_the_data.GSSTF2c.pdf",
-                    "description": "Science of the data\n      ",
                     "@type": "dcat:Distribution",
+                    "description": "Science of the data\n      ",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GSSTF/Science_of_the_data.GSSTF2c.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GSSTF_F08_2c",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GSSTF_F08_2c",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/GSSTF/GSSTF_F08.2c",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/GSSTF/GSSTF_F08.2c",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "editor": "Andrey Savtchenko",
+            "graphic-preview-description": "Goddard Satellite-based Surface Turbulent Fluxes (GSSTF)  Satellite F08 Total Precipitable Water 1 x 1 degree 01/01/1991 [g/cm2]",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GSSTF_F08_2c.png",
+            "identifier": "C1237113365-GES_DISC",
+            "issue-identification": "GSSTF_F08_2c",
+            "issued": "2011-11-18",
+            "keyword": [
+                "atmospheric pressure",
+                "ocean winds",
+                "ocean temperature",
+                "oceans",
+                "ocean pressure",
+                "ocean heat budget",
+                "earth science",
+                "atmospheric winds",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "atmospheric radiation",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/GSSTF/DATA321",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2011-11-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "GSSTF_F08",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1987-07-09T00:00:00Z/1992-01-01T23:59:59.999Z",
             "theme": [
                 "MEaSUREs",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Goddard Satellite-Based Surface Turbulent Fluxes, 1x1 deg Daily Grid, Satellite F08 V2c (GSSTF_F08) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-E-EPD-4-SUMM-EARTH1-15MIN-V1.0",
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
+            "description": "This data set contains fifteen minute averages for the energetic particle detector rate data obtained from the LEMMS telescope during the time the detector was operated during the Earth 1 encounter.  The data are recorded in thirty minute averages for each of 32 LEMMS channels and 32 CMS channels.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-e-epd-4-summ-earth1-15min-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "galileo",
+                "earth"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-E-EPD-4-SUMM-EARTH1-15MIN-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-e-epd-4-summ-earth1-15min-v1.0",
-            "description": "This data set contains fifteen minute averages for the energetic particle detector rate data obtained from the LEMMS telescope during the time the detector was operated during the Earth 1 encounter.  The data are recorded in thirty minute averages for each of 32 LEMMS channels and 32 CMS channels.",
-            "title": "GO EARTH EPD RESAMPLED SUMMARY EARTH1 15.0 MIN V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GO EARTH EPD RESAMPLED SUMMARY EARTH1 15.0 MIN V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO_L3G_MET.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Simon Hook, Gregory Halverson. 2024-04-25. ECOSTRESS Gridded Downscaled Meteorology Instantaneous L3 Global 70 m v002. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/ECOSTRESS/ECO_L3G_MET.002. https://doi.org/10.5067/ECOSTRESS/ECO_L3G_MET.002. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2024-04-25",
-            "temporal": "2018-07-09T00:00:00Z/2025-01-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-23",
-            "keyword": [
-                "atmospheric water vapor",
-                "atmosphere",
-                "atmospheric temperature",
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
-            "identifier": "C2074897737-LPCLOUD",
-            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found in Figure 2 on the ECOSTRESS website (https://ecostress.jpl.nasa.gov/science).\n\nThe ECOSTRESS Gridded Downscaled Meteorology Instantaneous L3 Global 70 m (ECO_L3G_MET) Version 2 data product provides instantaneous near-surface air temperature (Ta) and relative humidity (RH) estimates downscaled using linear regression. The linear regression uses up-sampled surface temperature (ST), normalized difference vegetation index (NDVI), and albedo as predictor variables and Ta or RH from Goddard Earth Observing System Version 5 (GEOS-5) Forward Processing (FP) as response variables for their relative outputs. Once the regression coefficients have been determined, they are applied to the 70 meter (m) ST, NDVI, and albedo as a first pass, which is then bias corrected using a GEOS-5 FP image. This data product is mosaicked from the L3 tiled MET (ECO_L3T_MET (https://doi.org/10.5067/ECOSTRESS/ECO_L3T_MET.002)) product, projected to a globally snapped 0.0006\u00b0 grid, and has a spatial resolution of 70 meters (m).\n\nThe ECO_L3G_MET Version 2 data product contains four layers distributed in an HDF5 format file including Ta, RH, cloud mask, and water mask.\n\nKnown Issues\n\n-\tData acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly, temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented, and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4, and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\n\n-\tData acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\n\n-\tData acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "Simon Hook, Gregory Halverson",
-            "title": "ECOSTRESS Gridded Downscaled Meteorology Instantaneous L3 Global 70 m V002",
-            "graphic-preview-file": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/ECO_L3G_MET.002/ECOv002_L3G_MET_32257_021_20240314T210201_0711_01/ECOv002_L3G_MET_32257_021_20240314T210201_0711_01.png",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found in Figure 2 on the ECOSTRESS website (https://ecostress.jpl.nasa.gov/science).\n\nThe ECOSTRESS Gridded Downscaled Meteorology Instantaneous L3 Global 70 m (ECO_L3G_MET) Version 2 data product provides instantaneous near-surface air temperature (Ta) and relative humidity (RH) estimates downscaled using linear regression. The linear regression uses up-sampled surface temperature (ST), normalized difference vegetation index (NDVI), and albedo as predictor variables and Ta or RH from Goddard Earth Observing System Version 5 (GEOS-5) Forward Processing (FP) as response variables for their relative outputs. Once the regression coefficients have been determined, they are applied to the 70 meter (m) ST, NDVI, and albedo as a first pass, which is then bias corrected using a GEOS-5 FP image. This data product is mosaicked from the L3 tiled MET (ECO_L3T_MET (https://doi.org/10.5067/ECOSTRESS/ECO_L3T_MET.002)) product, projected to a globally snapped 0.0006\u00b0 grid, and has a spatial resolution of 70 meters (m).\n\nThe ECO_L3G_MET Version 2 data product contains four layers distributed in an HDF5 format file including Ta, RH, cloud mask, and water mask.\n\nKnown Issues\n\n-\tData acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly, temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented, and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4, and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\n\n-\tData acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\n\n-\tData acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECOSTRESS%2FECO_L3G_MET.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECOSTRESS%2FECO_L3G_MET.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2074897737-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2074897737-LPCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO_L3G_MET.002",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO_L3G_MET.002",
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
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1869/ECOSTRESSL3JET_ATBD_V1.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1869/ECOSTRESSL3JET_ATBD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/ECO_L3G_MET.002/ECOv002_L3G_MET_32257_021_20240314T210201_0711_01/ECOv002_L3G_MET_32257_021_20240314T210201_0711_01.png",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/ECO_L3G_MET.002/ECOv002_L3G_MET_32257_021_20240314T210201_0711_01/ECOv002_L3G_MET_32257_021_20240314T210201_0711_01.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/ECO_L3G_MET.002/ECOv002_L3G_MET_32257_021_20240314T210201_0711_01/ECOv002_L3G_MET_32257_021_20240314T210201_0711_01.png",
+            "identifier": "C2074897737-LPCLOUD",
+            "issued": "2024-04-25",
+            "keyword": [
+                "atmospheric water vapor",
+                "atmosphere",
+                "atmospheric temperature",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO_L3G_MET.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-23",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -54.0 180.0 54.0",
+            "temporal": "2018-07-09T00:00:00Z/2025-01-27T00:00:00Z",
             "theme": [
                 "ECOSTRESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ECOSTRESS Gridded Downscaled Meteorology Instantaneous L3 Global 70 m V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-PANCAM-2-EDR-SCI-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-pancam-2-edr-sci-v1.0_jwpc-ae9n",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-PANCAM-2-EDR-SCI-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-pancam-2-edr-sci-v1.0_jwpc-ae9n",
-            "description": "NULL",
-            "title": "MER 2 MARS PANORAMIC CAMERA SCIENCE EDR\n                                      VERSION 1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MER 2 MARS PANORAMIC CAMERA SCIENCE EDR\n                                      VERSION 1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/AERDB_D3_VIIRS_SNPP.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA VIIRS Atmosphere SIPS. 2023-02-10. VIIRS/SNPP Deep Blue Level 3 daily aerosol data 1x1 degree grid. Version 2. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/VIIRS/AERDB_D3_VIIRS_SNPP.002. https://doi.org/10.5067/VIIRS/AERDB_D3_VIIRS_SNPP.002.",
-            "issued": "2023-01-10",
-            "temporal": "2012-03-01T00:00:00Z/2025-01-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-24",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "aerosols"
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
-            "identifier": "C2600306111-LAADS",
-            "description": "The VIIRS/SNPP Deep Blue Level 3 daily aerosol data, 1x1 degree grid, Short-name AERDB_D3_VIIRS_SNPP product is derived from the Version-2.0 (V2.0) L2 6-minute swath-based products (AERDB_L2_VIIRS_SNPP), and is provided in a 1 x 1 degree horizontal resolution grid.  Each data field, in most cases, represents the arithmetic mean of all the cells whose latitude and longitude coordinates positions them within each grid element\u2019s bounding limits.  Other measures like standard deviation are also provided.  This aggregated product is derived only using the best-estimate, QA-filtered retrievals.  Using only cells that were measured on the day of interest, the algorithm requires at least three retrieved measurements to render a given grid as valid on any given day.  This daily product record starts from March 1st, 2012 . This L3 daily product, in netCDF, contains 45 Science Data Set (SDS) layers.\r\n\r\nFor more information about the product and Science Data Set (SDS) layers, consult product page at:\r\nhttps://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/products/AERDB_D3_VIIRS_SNPP\r\n\r\nOr\r\n\r\nConsult Deep Blue aerosol team Page at: \r\nhttps://deepblue.gsfc.nasa.gov",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "NASA VIIRS Atmosphere SIPS",
-            "title": "VIIRS/SNPP Deep Blue Level 3 daily aerosol data, 1 degree x 1 degree grid",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The VIIRS/SNPP Deep Blue Level 3 daily aerosol data, 1x1 degree grid, Short-name AERDB_D3_VIIRS_SNPP product is derived from the Version-2.0 (V2.0) L2 6-minute swath-based products (AERDB_L2_VIIRS_SNPP), and is provided in a 1 x 1 degree horizontal resolution grid.  Each data field, in most cases, represents the arithmetic mean of all the cells whose latitude and longitude coordinates positions them within each grid element\u2019s bounding limits.  Other measures like standard deviation are also provided.  This aggregated product is derived only using the best-estimate, QA-filtered retrievals.  Using only cells that were measured on the day of interest, the algorithm requires at least three retrieved measurements to render a given grid as valid on any given day.  This daily product record starts from March 1st, 2012 . This L3 daily product, in netCDF, contains 45 Science Data Set (SDS) layers.\r\n\r\nFor more information about the product and Science Data Set (SDS) layers, consult product page at:\r\nhttps://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/products/AERDB_D3_VIIRS_SNPP\r\n\r\nOr\r\n\r\nConsult Deep Blue aerosol team Page at: \r\nhttps://deepblue.gsfc.nasa.gov",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FAERDB_D3_VIIRS_SNPP.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FAERDB_D3_VIIRS_SNPP.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://deepblue.gsfc.nasa.gov/publications",
-                    "description": "Data product documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data product documentation",
+                    "downloadURL": "https://deepblue.gsfc.nasa.gov/publications",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/1/AERDB_D3_VIIRS_SNPP--5200",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/1/AERDB_D3_VIIRS_SNPP--5200",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/5200/AERDB_D3_VIIRS_SNPP/",
-                    "description": "Direct link to Collection's OPeNDAP directory",
                     "@type": "dcat:Distribution",
+                    "description": "Direct link to Collection's OPeNDAP directory",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/5200/AERDB_D3_VIIRS_SNPP/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/api/v2/content/archives/Document%20Archive/Science%20Data%20Product%20Documentation/VIIRS_Deep_Blue_Aerosol_User_Guide_v2.pdf",
-                    "description": "SNPP VIIRS Deep Blue Aerosol User Guide V1.1",
                     "@type": "dcat:Distribution",
+                    "description": "SNPP VIIRS Deep Blue Aerosol User Guide V1.1",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/api/v2/content/archives/Document%20Archive/Science%20Data%20Product%20Documentation/VIIRS_Deep_Blue_Aerosol_User_Guide_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/viirs/SNPP-VIIRS_DB_Aerosol_ATBD.pdf",
-                    "description": "SNPP VIIRS Deep Blue Aerosol Product ATBD",
                     "@type": "dcat:Distribution",
+                    "description": "SNPP VIIRS Deep Blue Aerosol Product ATBD",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/viirs/SNPP-VIIRS_DB_Aerosol_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 }
             ],
+            "identifier": "C2600306111-LAADS",
+            "issued": "2023-01-10",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/AERDB_D3_VIIRS_SNPP.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-24",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-03-01T00:00:00Z/2025-01-27T00:00:00Z",
             "theme": [
                 "Suomi-NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/SNPP Deep Blue Level 3 daily aerosol data, 1 degree x 1 degree grid"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-GIA-3-ESC2-COMET-ESCORT-2-V1.0",
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
+            "description": "Comet Escort 2 Phase covers the period of time from 11 March 2015  until 30 June 2015. It started after Rosetta successfully completed the  Comet Escort 1 Phase. The present DataSet collects the GIADA data of ESC2 phase. The GIADA Scientific phase started on 7 May 2014 and was devoted to the characterization of the 67P environment.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-gia-3-esc2-comet-escort-2-v1.0_jx22-aeiy",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-GIA-3-ESC2-COMET-ESCORT-2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-gia-3-esc2-comet-escort-2-v1.0_jx22-aeiy",
-            "description": "Comet Escort 2 Phase covers the period of time from 11 March 2015  until 30 June 2015. It started after Rosetta successfully completed the  Comet Escort 1 Phase. The present DataSet collects the GIADA data of ESC2 phase. The GIADA Scientific phase started on 7 May 2014 and was devoted to the characterization of the 67P environment.",
-            "title": "ROSETTA-ORBITER 67P GIADA 3 ESC2 COMET ESCORT 2 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P GIADA 3 ESC2 COMET ESCORT 2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/897",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Harriss, R.C. 2008. Pre-LBA ABLE-2A and ABLE-2B Expedition Data. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/897",
-            "issued": "2023-10-03",
-            "temporal": "1985-07-11T00:00:00Z/1987-05-13T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-04",
-            "keyword": [
-                "atmospheric radiation",
-                "atmosphere",
-                "atmospheric temperature",
-                "atmospheric chemistry",
-                "earth science",
-                "aerosols"
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
-            "identifier": "C2777402194-ORNL_CLOUD",
             "description": "The ABLE 2A and 2B (Atmospheric Boundary Layer Experiments) data consists of  estimates of the rate of exchange of a wide variety of aerosols and gases between the Amazon Basin and its atmospheric boundary layer, and the processes by which these aerosols and gases are moved between the boundary layer and the free troposphere. The data are presented in gzipped ASCII text files in Global Tropospheric Experiment (GTE) format.The ABLE-2 project consisted of two expeditions: the first in the Amazonian dry season (ABLE-2A, July-August 1985); and the second in the wet season (ABLE-2B, April-May 1987). The ABLE-2 core research data were gathered by NASA Electra aircraft flights that stretched from Belem, at the mouth of the Amazon River, west to Tabatinga, on the Brazil-Colombia border, from a base at Manaus in the heart of the forest. See Figure 1. These observations were supplemented by ground based chemical and meteorological measurements in the dry forest, the Amazon floodplain, and the tributary rivers through use of enclosures, an instrumented tower in the jungle, a large tethered balloon, and weather and ozone sondes.This study showed air above the Amazon jungle to be extremely clean during the wet season but air quality deteriorated dramatically during the dry season as the result of biomass burning, performed mostly at the edges of the forest. Biomass burning is also a source of greenhouse gases carbon dioxide and methane, as well as other pollutants (carbon monoxide and oxides of nitrogen). Amazonian ozone deposition rates were found to be 5 to 50 times higher than those previously measured over pine forests and water surfaces. The Amazon River floodplain is a globally significant source of methane, supplying about 12% of the estimated worldwide total from all wetlands sources. Over Amazonia, carbon monoxide is enhanced by factors ranging from 1.2 to 2.7 by comparison with adjacent regions due to isoprene oxidation and biomass burning. Over the rainforest individual convective storms transport 200 megatons of air per hour, of which 3 megatons is water vapor that releases 100,000 megawatts of energy into the atmosphere through condensation into rain.The ABLE was a collaboration of U.S. and Brazilian scientists sponsored by NASA and Instituto Nacional de Pesquisas Espaciais (INPE) and supported by the Global Tropospheric Experiment (GTE) component of the NASA Tropospheric Chemistry Program.",
-            "graphic-preview-description": "Browse Image",
-            "title": "Pre-LBA ABLE-2A and ABLE-2B Expedition Data",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F897",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F897",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/atmos_chemistry/ABLE/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/atmos_chemistry/ABLE/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/Pre_LBA_ABLE.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/Pre_LBA_ABLE.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/897",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/897",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/atmos_chemistry/ABLE/comp/able2.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/atmos_chemistry/ABLE/comp/able2.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/atmos_chemistry/ABLE/comp/able2A.jpg",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/atmos_chemistry/ABLE/comp/able2A.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/atmos_chemistry/ABLE/comp/able2B_large.jpg",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/atmos_chemistry/ABLE/comp/able2B_large.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/atmos_chemistry/ABLE/comp/able3.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/atmos_chemistry/ABLE/comp/able3.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/atmos_chemistry/ABLE/comp/gte_fmt_2000.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/atmos_chemistry/ABLE/comp/gte_fmt_2000.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/atmos_chemistry/ABLE/comp/Pre_LBA_ABLE.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/atmos_chemistry/ABLE/comp/Pre_LBA_ABLE.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/atmos_chemistry/ABLE/comp/pwb-fmat_1994.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/atmos_chemistry/ABLE/comp/pwb-fmat_1994.pdf",
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
+            "identifier": "C2777402194-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "atmospheric radiation",
+                "atmosphere",
+                "atmospheric temperature",
+                "atmospheric chemistry",
+                "earth science",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/897",
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
             "spatial": "-70.0 -10.0 -50.0 0.0",
+            "temporal": "1985-07-11T00:00:00Z/1987-05-13T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Pre-LBA ABLE-2A and ABLE-2B Expedition Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/966",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Ramankutty,N. and J.A. Foley. 2010. ISLSCP II Historical Croplands Cover, 1700-1992. In Hall, Forest G., G. Collatz, B. Meeson, S. Los, E. Brown de Colstoun, and D. Landis (eds.). ISLSCP Initiative II Collection. Data set. Available on-line [http://daac.ornl.gov/] from Oak Ridge National Laboratory Distributed Active Archive Center, Oak Ridge, Tennessee, U.S.A.  doi:10.3334/ORNLDAAC/966",
-            "issued": "2023-10-15",
-            "temporal": "1700-01-01T00:00:00Z/1992-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-17",
-            "keyword": [
-                "biosphere",
-                "vegetation",
-                "surface radiative properties",
-                "ngda",
-                "national geospatial data asset",
-                "land use/land cover",
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
-            "identifier": "C2784888334-ORNL_CLOUD",
             "description": "The Historical Croplands Cover data set was developed to understand the consequences of historical changes in land use and land cover for ecosystem goods and services. In particular, this data set can be used to study how global changes in cultivated area has influenced climate, biogeochemical cycles, biodiversity, etc. This data set can be used directly within spatially-explicit climate and biogeochemical models.This is a gridded data set describing the fraction of each grid cell in the globe that is occupied by cultivated land from 1700 to 1992. Data layers are provided for every 50 years from 1700 to 1850, every 10 years from 1850 to 1980, and every year from 1986 to 1992.There are two sources of global land cover/land use data. The most recent estimates are derived from satellite measurements, and are available in a spatially-explicit fashion for roughly the last 30 years. The other estimate is based on ground-based sources such as census statistics, land surveys, estimates by historical geographers, etc. These land inventory data are only available at the scale of political units, but have the advantage of being historical. Ramankutty and Foley (1998) derived a spatially-explicit data set of croplands in 1992 by synthesizing remotely-sensed land cover data with contemporary land inventory data. Furthermore, Ramankutty and Foley (1999) extended this data set into the past (back to 1700) using historical land inventory data.The data set should only be used for continental-to-global scale analysis and modeling. The data set captures the broad patterns of cropland change over history, but not necessarily the fine details at local to regional scales - please check the data quality before using it at fine spatial scales. The quality of historical data for the Russian Federation is poor. The quality of data prior to 1850 is poor -- only continental-scale historical data were used for that period.",
-            "graphic-preview-description": "Browse Image",
-            "title": "ISLSCP II Historical Croplands Cover, 1700-1992",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/966_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F966",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F966",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/islscp_ii/vegetation/historic_cropland_xdeg/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/islscp_ii/vegetation/historic_cropland_xdeg/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ISLSCP_II/guides/historic_cropland_xdeg.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ISLSCP_II/guides/historic_cropland_xdeg.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/966",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/966",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/vegetation/historic_cropland_xdeg/comp/0_historic_cropland_readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/vegetation/historic_cropland_xdeg/comp/0_historic_cropland_readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/vegetation/historic_cropland_xdeg/comp/1_historic_cropland_doc.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/vegetation/historic_cropland_xdeg/comp/1_historic_cropland_doc.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/966_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/966_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=966",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=966",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/966/catalog.html",
-                    "description": "The THREDDS location for this Collection.",
                     "@type": "dcat:Distribution",
+                    "description": "The THREDDS location for this Collection.",
+                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/966/catalog.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/966_1_fit.png",
+            "identifier": "C2784888334-ORNL_CLOUD",
+            "issued": "2023-10-15",
+            "keyword": [
+                "biosphere",
+                "vegetation",
+                "surface radiative properties",
+                "ngda",
+                "national geospatial data asset",
+                "land use/land cover",
+                "land surface",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/966",
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
+            "temporal": "1700-01-01T00:00:00Z/1992-12-31T23:59:59Z",
             "theme": [
                 "ISLSCP II",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISLSCP II Historical Croplands Cover, 1700-1992"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-PLS-5-SUMM-ION-M-MODE-96S-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-pls-5-summ-ion-m-mode-96s-v1.0_jx76-esdv",
+            "issued": "2018-06-26",
+            "keyword": [
+                "jupiter",
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-PLS-5-SUMM-ION-M-MODE-96S-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-pls-5-summ-ion-m-mode-96s-v1.0_jx76-esdv",
-            "description": "not applicable",
-            "title": "VG1 JUP PLS DERIVED ION OUTBND MAGSHTH M-MODE 96SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG1 JUP PLS DERIVED ION OUTBND MAGSHTH M-MODE 96SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/MEASURES/GOZCARDS/DATA3013",
             "citation": "Froidevaux, L., R. A. Fuller, A. Lambert, N. J. Livesey, P. F. Bernath, and K. A. Walker. 2013-05-02. GozMmlpN2O. Version 1. GOZCARDS Merged Nitrous Oxide 1 month L3 10 degree Zonal Means on a Vertical Pressure Grid V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/MEASURES/GOZCARDS/DATA3013. https://disc.gsfc.nasa.gov/datacollection/GozMmlpN2O_1.html. Digital Science Data.",
-            "issued": "2013-05-02",
-            "temporal": "2004-08-01T00:00:00Z/2012-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2013-05-02",
-            "references": [
-                "https://doi.org/10.5194/acp-15-10471-201"
-            ],
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric chemistry"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "LUCIEN FROIDEVAUX",
                 "hasEmail": "mailto:lucien.froidevaux@jpl.nasa.gov"
             },
+            "creator": "Froidevaux, L., R. A. Fuller, A. Lambert, N. J. Livesey, P. F. Bernath, and K. A. Walker",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1251051239-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The GOZCARDS Merged Data for Nitrous Oxide 1 month L3 10 degree Zonal Averages on a Vertical Pressure Grid product (GozMmlpN2O) contains zonal means and related information (standard deviation, minimum/maximum value, etc.), calculated as a result of a merging process that ties together the source datasets, after bias removal and averaging. The merged N2O data are from the following satellite instruments: ACE-FTS (v2.2u; 2004 - onward), and Aura MLS (v3.3; 2004 - onward). The vertical pressure range for N2O is from 147 to 0.5 hPa. The input source data used to create this merged product are contained in a separate data product with the short name GozSmlpN2O.\n\nThe GozMmlpN2O merged data are distributed in netCDF4 format.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "GozMmlpN2O",
-            "creator": "Froidevaux, L., R. A. Fuller, A. Lambert, N. J. Livesey, P. F. Bernath, and K. A. Walker",
-            "title": "GOZCARDS Merged Nitrous Oxide 1 month L3 10 degree Zonal Means on a Vertical Pressure Grid V1 (GozMmlpN2O) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GozMmlpN2O_1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FGOZCARDS%2FDATA3013",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FGOZCARDS%2FDATA3013",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1000740,265 +1000715,262 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GozMmlpN2O_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GozMmlpN2O_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/GOZCARDS/GozMmlpN2O.1",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/GOZCARDS/GozMmlpN2O.1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/GOZCARDS/GozMmlpN2O.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/GOZCARDS/GozMmlpN2O.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/GOZCARDS/GozMmlpN2O.1/",
-                    "description": "Access the data using the THREDDS Catalog.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data using the THREDDS Catalog.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/GOZCARDS/GozMmlpN2O.1/",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GozMmlpN2O_1.png",
+            "identifier": "C1251051239-GES_DISC",
+            "issued": "2013-05-02",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/GOZCARDS/DATA3013",
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
+            "series-name": "GozMmlpN2O",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2004-08-01T00:00:00Z/2012-12-31T23:59:59.999Z",
             "theme": [
                 "MEaSUREs",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GOZCARDS Merged Nitrous Oxide 1 month L3 10 degree Zonal Means on a Vertical Pressure Grid V1 (GozMmlpN2O) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MARSIS-3-RDR-SS-EXT6-V1.0",
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
+            "description": "This dataset contains subsurface sounding data from the MARS EXPRESS MARS MARSIS EXPERIMENT DATA RECORD EXTENSION 6 V1.0 Data Set that have been uncompressed, corrected for Automated Gain Control, aligned to a reference altitude and, except for data acquired using the SS2 mode, range processed after correcting for the distortion of the transmitted signal caused by the ionosphere.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-marsis-3-rdr-ss-ext6-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars express",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MARSIS-3-RDR-SS-EXT6-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-marsis-3-rdr-ss-ext6-v1.0",
-            "description": "This dataset contains subsurface sounding data from the MARS EXPRESS MARS MARSIS EXPERIMENT DATA RECORD EXTENSION 6 V1.0 Data Set that have been uncompressed, corrected for Automated Gain Control, aligned to a reference altitude and, except for data acquired using the SS2 mode, range processed after correcting for the distortion of the transmitted signal caused by the ionosphere.",
-            "title": "MARS EXPRESS MARSIS REDUCED DATA SUBSURFACE EXT 6 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARSIS REDUCED DATA SUBSURFACE EXT 6 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1389-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-02-01T09:12:25.000 to 2016-02-01T12:59:05.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1389-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1389-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1389-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-02-01T09:12:25.000 to 2016-02-01T12:59:05.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1389 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1389 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-2-PRL-MTP008-V1.0",
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
+            "description": "This data set contains count rates (1/s) as measured by the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, along with their standard deviations.  The primary target is comet 67P/Churyumov-Gerasimenko. These are CODMAC Level 2 Experiment Data Record data, and provide a measure of the radiation in the spacecraft environment during the Medium Term Plan 8 period of the PRELANDING mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-2-prl-mtp008-v1.0_jxac-hymp",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-2-PRL-MTP008-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-2-prl-mtp008-v1.0_jxac-hymp",
-            "description": "This data set contains count rates (1/s) as measured by the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, along with their standard deviations.  The primary target is comet 67P/Churyumov-Gerasimenko. These are CODMAC Level 2 Experiment Data Record data, and provide a measure of the radiation in the spacecraft environment during the Medium Term Plan 8 period of the PRELANDING mission phase.",
-            "title": "ROSETTA-ORBITER 67P SREM 2 PRELANDING\n    MTP008 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GPM/SAPHIR/MT1/1C/07",
-            "citation": "Wesley Berg. 2022-05-09. GPM_1CMT1SAPHIR. GPM SAPHIR on MT1 Common Calibrated Brightness Temperature L1C 1.5 hours 10 km V07. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/SAPHIR/MT1/1C/07. https://disc.gsfc.nasa.gov/datacollection/GPM_1CMT1SAPHIR_07.html. Digital Science Data.",
-            "issued": "2022-05-01",
-            "temporal": "2011-10-13T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-01",
-            "references": [
-                "https://doi.org/10.1175/JTECH-D-16-0100.1",
-                "https://doi.org/10.3390/rs10081306"
-            ],
-            "keyword": [
-                "atmospheric water vapor",
-                "precipitation",
-                "atmosphere",
-                "earth science"
+            "title": "ROSETTA-ORBITER 67P SREM 2 PRELANDING\n    MTP008 V1.0"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
             ],
+            "citation": "Wesley Berg. 2022-05-09. GPM_1CMT1SAPHIR. GPM SAPHIR on MT1 Common Calibrated Brightness Temperature L1C 1.5 hours 10 km V07. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/SAPHIR/MT1/1C/07. https://disc.gsfc.nasa.gov/datacollection/GPM_1CMT1SAPHIR_07.html. Digital Science Data.",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "WESLEY BERG",
                 "hasEmail": "mailto:berg@atmos.colostate.edu"
             },
+            "creator": "Wesley Berg",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2264133181-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Version 07 is the current version of the data set. Older versions will no longer be available and have been superseded by Version 07.\n\n1CAMSR2 contains common calibrated brightness temperature from the AMSR2 passive microwave instrument flown on the GCOMW1 satellite. This products contains 6 swaths. Swath 1 has channels 10.65V 10.65H. Swath 2 has channels 18.7V 18.7H. Swath 3 has channels 23.8V 23.8H. Swath 4 has channels 36.5V 36.5H. Swath S5 has 2 high frequency A-Scan channels (89V 89H). Swath S6 has 2 high frequency B-Scan channels (89V 89H). Data for all six swaths is observed in the same revolution of the instrument. High frequency A and high frequency B data are observed in separate feedhorns. All 1C products have a common L1C data structure, simple and generic. Each L1C swath includes scan time, latitude and longitude, scan status, quality, incidence angle, Sun glint angle, and the intercalibrated brightness temperature (Tc). One or more swaths are included in a product. The radiometer data are recalibrated to a common basis so that precipitation products derived from them are consistent.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "GPM_1CMT1SAPHIR",
-            "creator": "Wesley Berg",
-            "graphic-preview-description": "Common Calibrated Brightness Temperature from GPM SAPHIR on MT1 (GPM_1CMT1SAPHIR)",
-            "title": "GPM SAPHIR on MT1 Common Calibrated Brightness Temperature L1C 1.5 hours 10 km V07 (GPM_1CMT1SAPHIR) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/1C-BR.MT1.SAPHIR.XCAL2016-V.20150101-S011534-E025729.016627.V05A.PNG",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FSAPHIR%2FMT1%2F1C%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FSAPHIR%2FMT1%2F1C%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/1C-BR.MT1.SAPHIR.XCAL2016-V.20150101-S011534-E025729.016627.V05A.PNG",
-                    "description": "Common Calibrated Brightness Temperature from GPM SAPHIR on MT1 (GPM_1CMT1SAPHIR)",
                     "@type": "dcat:Distribution",
+                    "description": "Common Calibrated Brightness Temperature from GPM SAPHIR on MT1 (GPM_1CMT1SAPHIR)",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/1C-BR.MT1.SAPHIR.XCAL2016-V.20150101-S011534-E025729.016627.V05A.PNG",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_1CMT1SAPHIR_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_1CMT1SAPHIR_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L1C/GPM_1CMT1SAPHIR.07/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L1C/GPM_1CMT1SAPHIR.07/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L1C/GPM_1CMT1SAPHIR.07/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L1C/GPM_1CMT1SAPHIR.07/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_1CMT1SAPHIR_07",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_1CMT1SAPHIR_07",
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
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L2/doc/README.GPM.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L2/doc/README.GPM.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
@@ -1001008,337 +1000980,367 @@
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.star.nesdis.noaa.gov/mirs/saphir.php",
-                    "description": "Instrument Description",
                     "@type": "dcat:Distribution",
+                    "description": "Instrument Description",
+                    "downloadURL": "https://www.star.nesdis.noaa.gov/mirs/saphir.php",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Common Calibrated Brightness Temperature from GPM SAPHIR on MT1 (GPM_1CMT1SAPHIR)",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/1C-BR.MT1.SAPHIR.XCAL2016-V.20150101-S011534-E025729.016627.V05A.PNG",
+            "identifier": "C2264133181-GES_DISC",
+            "issued": "2022-05-01",
+            "keyword": [
+                "atmospheric water vapor",
+                "precipitation",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/SAPHIR/MT1/1C/07",
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
+            "references": [
+                "https://doi.org/10.1175/JTECH-D-16-0100.1",
+                "https://doi.org/10.3390/rs10081306"
+            ],
+            "release-place": "Greenbelt, MD",
+            "series-name": "GPM_1CMT1SAPHIR",
             "spatial": "-180.0 -30.0 180.0 30.0",
+            "temporal": "2011-10-13T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "GPM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM SAPHIR on MT1 Common Calibrated Brightness Temperature L1C 1.5 hours 10 km V07 (GPM_1CMT1SAPHIR) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0231-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-22T13:10:05.000 to 2014-08-22T18:30:12.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0231-v1.0_jxc2-d2z8",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0231-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0231-v1.0_jxc2-d2z8",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-22T13:10:05.000 to 2014-08-22T18:30:12.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0231 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0231 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/821/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-07-29",
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
-            "identifier": "DASHLINK_821",
             "description": "Prognostics has taken center stage in Condition Based Maintenance (CBM) where it is desired to estimate Remaining Useful Life (RUL) of a system so that remedial measures may be taken in advance to avoid catastrophic events or unwanted downtimes. Validation of such predictions is an important but difficult proposition and a lack of appropriate evaluation methods renders prognostics meaningless. Evaluation methods currently used in the research community are not standardized and in many cases do not sufficiently assess key performance aspects expected out of a prognostics algorithm. In this paper we introduce several new evaluation metrics tailored for prognostics and show that they can effectively evaluate various algorithms as compared to other conventional metrics. Four prognostic algorithms, Relevance Vector Machine (RVM), Gaussian Process Regression (GPR), Artificial Neural Network (ANN), and Polynomial Regression (PR), are compared. These algorithms vary in complexity and their ability to manage uncertainty around predicted estimates. Results show that the new metrics rank these algorithms in a different manner; depending on the requirements and constraints suitable metrics may be chosen. Beyond these results, this paper offers ideas about how metrics suitable to prognostics may be designed so that the evaluation procedure can be standardized.",
-            "title": "Evaluating Algorithm Performance Metrics Tailored for Prognostics",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2009_IEEEAerospace_MetricsEvaluation_2.pdf",
-                    "description": "2009_IEEEAerospace_MetricsEvaluation.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "2009_IEEEAerospace_MetricsEvaluation.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2009_IEEEAerospace_MetricsEvaluation_2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "2009_IEEEAerospace_MetricsEvaluation.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_821",
+            "issued": "2013-07-29",
+            "keyword": [
+                "dashlink",
+                "ames",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/821/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Evaluating Algorithm Performance Metrics Tailored for Prognostics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-MI-5-MOSAIC-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-mi-5-mosaic-ops-v1.0_jxdz-fkhd",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-MI-5-MOSAIC-OPS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-mi-5-mosaic-ops-v1.0_jxdz-fkhd",
-            "description": "not applicable",
-            "title": "MER 2 MARS MICROSCOPIC IMAGER CAMERA MOSAICS RDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MER 2 MARS MICROSCOPIC IMAGER CAMERA MOSAICS RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGN-V-RDRS-5-TOPO-L2-V1.0",
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
+            "description": "This data set contains the Magellan Topography Model of Venus and was produced by a spherical harmonic analysis of the most complete set of Magellan altimetry data, augmented by Pioneer Venus and Venera data. A detailed report on this harmonic analysis and its scientific implications is in [RAPPAPORT&PLAUT1994].",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgn-v-rdrs-5-topo-l2-v1.0_jxga-8udq",
+            "issued": "2021-05-21",
+            "keyword": [
+                "magellan",
+                "venus"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGN-V-RDRS-5-TOPO-L2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgn-v-rdrs-5-topo-l2-v1.0_jxga-8udq",
-            "description": "This data set contains the Magellan Topography Model of Venus and was produced by a spherical harmonic analysis of the most complete set of Magellan altimetry data, augmented by Pioneer Venus and Venera data. A detailed report on this harmonic analysis and its scientific implications is in [RAPPAPORT&PLAUT1994].",
-            "title": "MGN V RDRS SPHERICAL HARMONIC AND TOPOGRAPHY MAP DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MGN V RDRS SPHERICAL HARMONIC AND TOPOGRAPHY MAP DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/41",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Shah, T., and E. T. Kanemasu. 1994. LAI and PAR Data: Light Bar - KSU (FIFE). Data set. Available on-line [http://www.daac.ornl.gov] from Oak Ridge National Laboratory Distributed Active Archive Center, Oak Ridge, Tennessee, U.S.A. Also published in D. E. Strebel, D. R. Landis, K. F. Huemmrich, and B. W. Meeson (eds.), Collected Data of the First ISLSCP Field Experiment, Vol. 1: Surface Observations and Non-Image Data Sets. CD-ROM. National Aeronautics and Space Administration, Goddard Space Flight Center, Greenbelt, Maryland, U.S.A. (available from http://www.daac.ornl.gov). doi:10.3334/ORNLDAAC/41",
-            "issued": "2024-05-05",
-            "temporal": "1989-07-03T00:00:00Z/1989-10-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-07",
-            "keyword": [
-                "atmospheric radiation",
-                "atmosphere",
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
-            "identifier": "C2980086740-ORNL_CLOUD",
             "description": "LAI and PAR above & below canopy measured with light bar by KSU staff science",
-            "graphic-preview-description": "Browse Image",
-            "title": "LAI & PAR Data: Light Bar - KSU (FIFE)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/fife_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F41",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F41",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_sur_refl_ltbr_ksu/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_sur_refl_ltbr_ksu/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/Light_Bar_KSU.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/Light_Bar_KSU.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/41",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/41",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_refl_ltbr_ksu/comp/lb_ksu.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_refl_ltbr_ksu/comp/lb_ksu.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_refl_ltbr_ksu/comp/lb_ksu.tdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_refl_ltbr_ksu/comp/lb_ksu.tdf",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_refl_ltbr_ksu/comp/Light_Bar_KSU.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_refl_ltbr_ksu/comp/Light_Bar_KSU.pdf",
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
+            "identifier": "C2980086740-ORNL_CLOUD",
+            "issued": "2024-05-05",
+            "keyword": [
+                "atmospheric radiation",
+                "atmosphere",
+                "biosphere",
+                "earth science",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/41",
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
             "spatial": "-96.61 38.98 -96.45 39.1",
+            "temporal": "1989-07-03T00:00:00Z/1989-10-31T23:59:59Z",
             "theme": [
                 "FIFE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LAI & PAR Data: Light Bar - KSU (FIFE)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-EXT3-67PCHURYUMOV-M35-V3.0",
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
+            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 3 mission phase, covering the period from 2016-09-26T06:40:00.000 to 2016-10-01T00:00:00.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Corrected START_TIME and STOP_TIME for BALLISTIC_STACKED images.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-ext3-67pchuryumov-m35-v3.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-EXT3-67PCHURYUMOV-M35-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-ext3-67pchuryumov-m35-v3.0",
-            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 3 mission phase, covering the period from 2016-09-26T06:40:00.000 to 2016-10-01T00:00:00.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Corrected START_TIME and STOP_TIME for BALLISTIC_STACKED images.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 2 EXT3-MTP035 EDR V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 2 EXT3-MTP035 EDR V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-E%2FV%2FH-MLA-2-EDR-RAWDATA-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Abstract ======== This data set consists of the MESSENGER Mercury Laser Altimeter (MLA) uncalibrated observations, also known as Experiment Data Records, or EDRs. The MLA is a solid-state pulsed laser that measures the distance between the spacecraft and the surface of Mercury. There are three EDR data products, MLASCIENCERAW, MLASTATUS, and MLAHDIAGNOSTIC, including the laser ranges, instrument status, and hardware diagnostic information.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-e-v-h-mla-2-edr-rawdata-v1.0_jxhy-6hht",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "calibration",
                 "earth",
@@ -1001346,783 +1001348,795 @@
                 "messenger",
                 "venus"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-E%2FV%2FH-MLA-2-EDR-RAWDATA-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-e-v-h-mla-2-edr-rawdata-v1.0_jxhy-6hht",
-            "description": "Abstract ======== This data set consists of the MESSENGER Mercury Laser Altimeter (MLA) uncalibrated observations, also known as Experiment Data Records, or EDRs. The MLA is a solid-state pulsed laser that measures the distance between the spacecraft and the surface of Mercury. There are three EDR data products, MLASCIENCERAW, MLASTATUS, and MLAHDIAGNOSTIC, including the laser ranges, instrument status, and hardware diagnostic information.",
-            "title": "MESSENGER E/V/H MERCURY LASER ALTIMETER 2 EDR RAW DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MESSENGER E/V/H MERCURY LASER ALTIMETER 2 EDR RAW DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP14A1.001",
             "citation": "Wilfrid Schroeder, Louis Giglio\r\n. 2019-07-01. VNP14A1. Version 001. VIIRS/NPP Thermal Anomalies and Fire Daily L3 Global 1km SIN Grid V001\r\n. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VNP14A1.001 . https://doi.org/10.5067/VIIRS/VNP14A1.001. Digital Science Data. This data set was provided by the NASA/NOAA NPP Project. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
-            "issued": "2019-07-01",
-            "temporal": "2012-01-19T00:00:00Z/2024-06-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-07-01",
-            "keyword": [
-                "land surface",
-                "ecological dynamics",
-                "biosphere",
-                "surface radiative properties",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Wilfrid Schroeder",
                 "hasEmail": "mailto:wilfrid.schroeder@noaa.gov"
             },
+            "creator": "Wilfrid Schroeder, Louis Giglio",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1523387372-LPDAAC_ECS",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
             "description": "The daily NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite  (VIIRS) Thermal Anomalies/Fire (VNP14A1) Version 1 data product provides daily information about active fires and other thermal anomalies. The VNP14A1 data product is a global, 1 kilometer (km) gridded composite of fire pixels detected from VIIRS 750 meter (m) bands over a daily (24-hour) period. The VNP14 data products are designed after the Moderate Resolution Imaging Spectroradiometer (MODIS) Thermal Anomalies/Fire product suite.\r\n\r\nThe VNP14A1 product provides a total of four Science Dataset (SDS) layers for the confidence of fire, maximum fire radiative power (FRP), quality assessment (QA), and position of fire within scan. Each data product file is provided in HDF-EOS5 format. A low resolution browse is also provided showing the fire mask layer with a color map applied in JPEG format.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "VNP14A1",
-            "creator": "Wilfrid Schroeder, Louis Giglio",
-            "title": "VIIRS/NPP Thermal Anomalies and Fire Daily L3 Global 1km SIN Grid V001",
-            "graphic-preview-description": "Browse image for Earthdata Search",
-            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2019.07.01/BROWSE.VNP14A1.A2019181.h11v08.001.2019182082815.1.jpg?_ga=2.108480450.116070394.1561987039-1109527761.1561753117",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP14A1.001+",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP14A1.001+",
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
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP14A1.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP14A1.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP14A1.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP14A1.001/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1523387372-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1523387372-LPDAAC_ECS",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP14A1.001/contents.html",
-                    "description": "OPeNDAP provides direct access to data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP provides direct access to data via HTTPS.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP14A1.001/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
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
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/133/VNP14_ATBD.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/133/VNP14_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP14A1",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP14A1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/427/VNP14_User_Guide_V1.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/427/VNP14_User_Guide_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2019.07.01/BROWSE.VNP14A1.A2019181.h11v08.001.2019182082815.1.jpg?_ga=2.108480450.116070394.1561987039-1109527761.1561753117",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2019.07.01/BROWSE.VNP14A1.A2019181.h11v08.001.2019182082815.1.jpg?_ga=2.108480450.116070394.1561987039-1109527761.1561753117",
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
-                    "downloadURL": "https://viirsland.gsfc.nasa.gov/Val/Fire_Val.html",
-                    "description": "Validation at stage 1 has been achieved for the VIIRS Thermal Anomalies & Fire product suite.",
                     "@type": "dcat:Distribution",
+                    "description": "Validation at stage 1 has been achieved for the VIIRS Thermal Anomalies & Fire product suite.",
+                    "downloadURL": "https://viirsland.gsfc.nasa.gov/Val/Fire_Val.html",
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
+            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2019.07.01/BROWSE.VNP14A1.A2019181.h11v08.001.2019182082815.1.jpg?_ga=2.108480450.116070394.1561987039-1109527761.1561753117",
+            "identifier": "C1523387372-LPDAAC_ECS",
+            "issued": "2019-07-01",
+            "keyword": [
+                "land surface",
+                "ecological dynamics",
+                "biosphere",
+                "surface radiative properties",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP14A1.001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-07-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
+            "series-name": "VNP14A1",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-19T00:00:00Z/2024-06-03T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP Thermal Anomalies and Fire Daily L3 Global 1km SIN Grid V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-MIDAS-3-CR2-PC1-2-V1.0",
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
+            "description": "The Micro-Imaging Dust Analysis System (MIDAS) is an instrument on the ROSETTA Orbiter that will provide 3D images and statistical parameters of pristine cometary particles hitting the detector. This data set includes all data from the CRUISE 2 mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-midas-3-cr2-pc1-2-v1.0_jxkc-3gvu",
+            "issued": "2021-05-21",
+            "keyword": [
+                "unknown",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-MIDAS-3-CR2-PC1-2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-midas-3-cr2-pc1-2-v1.0_jxkc-3gvu",
-            "description": "The Micro-Imaging Dust Analysis System (MIDAS) is an instrument on the ROSETTA Orbiter that will provide 3D images and statistical parameters of pristine cometary particles hitting the detector. This data set includes all data from the CRUISE 2 mission phase.",
-            "title": "ROSETTA-ORBITER CHECK MIDAS 3 CR2 PC1-2 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECK MIDAS 3 CR2 PC1-2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-IRPOL-3-RDR-HALLEY-V1.0",
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
-                "halley"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "NASA's International Halley Watch (IHW) has created a Comet Halley Archive. The collection of data spans the full wavelength range as submitted by scientists to the IHW. The observations belong to one of the following Disciplines: Amateur, Astrometry, Infrared Studies, Large-Scale Phenomena, Meteor Studies, Near-Nucleus Studies, Photometry and Polarimetry, Radio Studies, and Spectroscopy and Spectrophotometry. The data collected by these nine disciplines were augmented by Spacecraft measurements. The data were submitted to IHW, but the evaluation and selection for the Archive has been the primary responsibility of the Discipline Specialist Teams for each network in cooperation with the Lead Center. The data from the Infrared Polarimetry subnetwork contains 137 observations spanning dates from 1985 September 16 through 1986 June 1.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-irpol-3-rdr-halley-v1.0_jxni-h49r",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international halley watch",
+                "halley"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-IRPOL-3-RDR-HALLEY-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-irpol-3-rdr-halley-v1.0_jxni-h49r",
-            "description": "NASA's International Halley Watch (IHW) has created a Comet Halley Archive. The collection of data spans the full wavelength range as submitted by scientists to the IHW. The observations belong to one of the following Disciplines: Amateur, Astrometry, Infrared Studies, Large-Scale Phenomena, Meteor Studies, Near-Nucleus Studies, Photometry and Polarimetry, Radio Studies, and Spectroscopy and Spectrophotometry. The data collected by these nine disciplines were augmented by Spacecraft measurements. The data were submitted to IHW, but the evaluation and selection for the Archive has been the primary responsibility of the Discipline Specialist Teams for each network in cooperation with the Lead Center. The data from the Infrared Polarimetry subnetwork contains 137 observations spanning dates from 1985 September 16 through 1986 June 1.",
-            "title": "IHW COMET HALLEY INFRARED POLARIMETRY V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "IHW COMET HALLEY INFRARED POLARIMETRY V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TERRA/MODIS/L3B/POC/2022",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/TERRA/MODIS/L3B/POC/2022.",
-            "issued": "2019-06-23",
-            "temporal": "2000-02-24T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-08-08",
-            "keyword": [
-                "ocean chemistry",
-                "earth science",
-                "ngda",
-                "oceans",
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
-            "identifier": "C2331486856-OB_DAAC",
             "description": "MODIS (or Moderate-Resolution Imaging Spectroradiometer) is a key instrument aboard the Terra (EOS AM) and Aqua (EOS PM) satellites. Terra's orbit around the Earth is timed so that it passes from north to south across the equator in the morning, while Aqua passes south to north over the equator in the afternoon. Terra MODIS and Aqua MODIS are viewing the entire Earth's surface every 1 to 2 days, acquiring data in 36 spectral bands, or groups of wavelengths (see MODIS Technical Specifications). These data will improve our understanding of global dynamics and processes occurring on the land, in the oceans, and in the lower atmosphere. MODIS is playing a vital role in the development of validated, global, interactive Earth system models able to predict global change accurately enough to assist policy makers in making sound decisions concerning the protection of our environment.",
-            "title": "Terra MODIS Global Binned Particulate Organic Carbon (POC) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMODIS%2FL3B%2FPOC%2F2022",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMODIS%2FL3B%2FPOC%2F2022",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/TERRA/MODIS/L3B/POC/2022",
-                    "description": "MODIS-Terra L3B Particulate Organic Carbon (POC) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS-Terra L3B Particulate Organic Carbon (POC) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/TERRA/MODIS/L3B/POC/2022",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2331486856-OB_DAAC",
+            "issued": "2019-06-23",
+            "keyword": [
+                "ocean chemistry",
+                "earth science",
+                "ngda",
+                "oceans",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://doi.org/10.5067/TERRA/MODIS/L3B/POC/2022",
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
+            "temporal": "2000-02-24T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Terra MODIS Global Binned Particulate Organic Carbon (POC) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Colorado_Radiation_AircraftRemoteSensing_CAR_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2022-04-18. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Colorado_Radiation_AircraftRemoteSensing_CAR_Data_1.",
-            "issued": "2021-08-20",
-            "temporal": "2014-07-06T00:00:00Z/2014-08-14T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-18",
-            "keyword": [
-                "clouds",
-                "atmosphere",
-                "earth science",
-                "atmospheric radiation"
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
-            "identifier": "C2254457468-LARC_ASDC",
             "description": "DISCOVERAQ_Colorado_Radiation_AircraftRemoteSensing_CAR_Data contains remotely sensed data collected via the Cloud Absorption Radiometer (CAR) onboard NASA's P-3B aircraft during the Colorado (Denver) deployment of NASA's DISCOVER-AQ field study. This data product contains data for only the Colorado deployment and data collection is complete.\r\n\r\nUnderstanding the factors that contribute to near surface pollution is difficult using only satellite-based observations. The incorporation of surface-level measurements from aircraft and ground-based platforms provides the crucial information necessary to validate and expand upon the use of satellites in understanding near surface pollution. Deriving Information on Surface conditions from Column and Vertically Resolved Observations Relevant to Air Quality (DISCOVER-AQ) was a four-year campaign conducted in collaboration between NASA Langley Research Center, NASA Goddard Space Flight Center, NASA Ames Research Center, and multiple universities to improve the use of satellites to monitor air quality for public health and environmental benefit. Through targeted airborne and ground-based observations, DISCOVER-AQ enabled more effective use of current and future satellites to diagnose ground level conditions influencing air quality.\r\n\r\nDISCOVER-AQ employed two NASA aircraft, the P-3B and King Air, with the P-3B completing in-situ spiral profiling of the atmosphere (aerosol properties, meteorological variables, and trace gas species). The King Air conducted both passive and active remote sensing of the atmospheric column extending below the aircraft to the surface. Data from an existing network of surface air quality monitors, AERONET sun photometers, Pandora UV/vis spectrometers and model simulations were also collected. Further, DISCOVER-AQ employed many surface monitoring sites, with measurements being made on the ground, in conjunction with the aircraft. The B200 and P-3B conducted flights in Baltimore-Washington, D.C. in 2011, Houston, TX in 2013, San Joaquin Valley, CA in 2013, and Denver, CO in 2014. These regions were targeted due to being in violation of the National Ambient Air Quality Standards (NAAQS).\r\n\r\nThe first objective of DISCOVER-AQ was to determine and investigate correlations between surface measurements and satellite column observations for the trace gases ozone (O3), nitrogen dioxide (NO2), and formaldehyde (CH2O) to understand how satellite column observations can diagnose surface conditions. DISCOVER-AQ also had the objective of using surface-level measurements to understand how satellites measure diurnal variability and to understand what factors control diurnal variability. Lastly, DISCOVER-AQ aimed to explore horizontal scales of variability, such as regions with steep gradients and urban plumes.",
-            "title": "DISCOVER-AQ Colorado Deployment P-3B Aircraft Remotely Sensed Cloud Absorption Radiometer (CAR) Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDISCOVERAQ_Colorado_Radiation_AircraftRemoteSensing_CAR_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDISCOVERAQ_Colorado_Radiation_AircraftRemoteSensing_CAR_Data_1",
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
-                    "downloadURL": "https://car.gsfc.nasa.gov/",
-                    "description": "Cloud Absorption Radiometer (CAR) home page",
                     "@type": "dcat:Distribution",
+                    "description": "Cloud Absorption Radiometer (CAR) home page",
+                    "downloadURL": "https://car.gsfc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Colorado_Radiation_AircraftRemoteSensing_CAR_Data_1",
-                    "description": "DOI Data Set Landing Page for DISCOVERAQ_Colorado_Radiation_AircraftRemoteSensing_CAR_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI Data Set Landing Page for DISCOVERAQ_Colorado_Radiation_AircraftRemoteSensing_CAR_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Colorado_Radiation_AircraftRemoteSensing_CAR_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2254457468-LARC_ASDC",
-                    "description": "Earthdata Search Client for DISCOVERAQ_Colorado_Radiation_AircraftRemoteSensing_CAR_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search Client for DISCOVERAQ_Colorado_Radiation_AircraftRemoteSensing_CAR_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2254457468-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/DISCOVER-AQ/Colorado_Radiation_AircraftRemoteSensing_CAR_Data_1/",
-                    "description": "ASDC Direct Data Download for DISCOVERAQ_Colorado_Radiation_AircraftRemoteSensing_CAR_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for DISCOVERAQ_Colorado_Radiation_AircraftRemoteSensing_CAR_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/DISCOVER-AQ/Colorado_Radiation_AircraftRemoteSensing_CAR_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/DISCOVER-AQ/Colorado_Radiation_AircraftRemoteSensing_CAR_Data_1/contents.html",
-                    "description": "OPeNDAP data access for DISCOVERAQ_Colorado_Radiation_AircraftRemoteSensing_CAR_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for DISCOVERAQ_Colorado_Radiation_AircraftRemoteSensing_CAR_Data_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/DISCOVER-AQ/Colorado_Radiation_AircraftRemoteSensing_CAR_Data_1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2254457468-LARC_ASDC",
+            "issued": "2021-08-20",
+            "keyword": [
+                "clouds",
+                "atmosphere",
+                "earth science",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Colorado_Radiation_AircraftRemoteSensing_CAR_Data_1",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-13.0 -180.0 -13.0 5.0 85.0 5.0 85.0 -180.0 -13.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2014-07-06T00:00:00Z/2014-08-14T23:59:59.999Z",
             "theme": [
                 "DISCOVER-AQ",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "DISCOVER-AQ Colorado Deployment P-3B Aircraft Remotely Sensed Cloud Absorption Radiometer (CAR) Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SPUR1-SEASR",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SPURS PROJECT, Fred Bingham. 2015-05-11. Seasoar CTD data for the SPURS-1 N. Atlantic field campaign. Version 1.0. SPURS Field Campaign Seasoar Products. Department of Physics and Physical Oceanography, University on North Carolina, Wilmington, NC, USA. Archived by National Aeronautics and Space Administration, U.S. Government, SPURS Data Management PI, Fred Bingham. https://doi.org/10.5067/SPUR1-SEASR. http://podaac.jpl.nasa.gov/SPURS. SPURS PROJECT, Fred Bingham, SPURS Data Management PI, Fred Bingham, 2015-05-11, Seasoar CTD data for the SPURS-1 N. Atlantic field campaign, http://podaac.jpl.nasa.gov/SPURS.",
-            "issued": "2015-04-06",
-            "temporal": "2013-03-22T00:00:00Z/2013-04-08T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-04-28",
-            "keyword": [
-                "earth science",
-                "salinity/density",
-                "ocean temperature",
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
-            "identifier": "C2491772317-POCLOUD",
-            "description": "The SPURS (Salinity Processes in the Upper Ocean Regional Study) project is an oceanographic process study and associated field program that aim to elucidate key mechanisms responsible for near-surface salinity variations in the oceans. The project involves two field campaigns and a series of cruises in regions of the Atlantic and Pacific Oceans exhibiting salinity extremes.  SPURS employs a suite of state-of-the-art in-situ sampling technologies that, combined with remotely sensed salinity fields from the Aquarius/SAC-D and SMOS satellites, provide a detailed characterization of salinity structure over a continuum of spatio-temporal scales.  The SPURS-1 campaign involved a series of 5 cruises during 2012 - 2013 seeking to characterize the salinity structure and balance in a high salinity, high evaporation, and low rainfall region of the subtropical North Atlantic. It aims to resolve processes responsible for maintaining the subtropical surface salinity maximum in this region and within a 900 x 800-mile square study area centered at 25N, 38W.  The Seasoar is a towed vehicle equipped with impeller-forced wings that can be rotated on command to allow the vehicle to undulate in the upper ocean. Generally, Seasoar operates between the surface and about 400 meters depth while being towed on faired cable at about eight knots. A typical dive cycle takes about 12 minutes to complete, providing an up and down profile every 3 km.  For SPURS-1, a Seasoar was deployed exclusively during the Sarmiento cruise over the period 22 Mar-8 Apr, 2013 and to a maximum depth of 312m.  The Seasoar towed sensor system was equipped with dual pumped temperature/conductivity sensors.  The Seasoar data in netCDF form here contains a highly processed 1-meter gridded version of the original source dataset, which is comprised of temperature, conductivity, salinity, pressure observations from 1144 casts during 2013 Spring SPURS Cruise.",
-            "release-place": "Department of Physics and Physical Oceanography, University on North Carolina, Wilmington, NC, USA",
-            "series-name": "Seasoar CTD data for the SPURS-1 N. Atlantic field campaign",
-            "graphic-preview-description": "Thumbnail",
             "creator": "SPURS PROJECT, Fred Bingham",
-            "title": "Seasoar CTD data for the SPURS-1 N. Atlantic field campaign",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS1_SEASOAR.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The SPURS (Salinity Processes in the Upper Ocean Regional Study) project is an oceanographic process study and associated field program that aim to elucidate key mechanisms responsible for near-surface salinity variations in the oceans. The project involves two field campaigns and a series of cruises in regions of the Atlantic and Pacific Oceans exhibiting salinity extremes.  SPURS employs a suite of state-of-the-art in-situ sampling technologies that, combined with remotely sensed salinity fields from the Aquarius/SAC-D and SMOS satellites, provide a detailed characterization of salinity structure over a continuum of spatio-temporal scales.  The SPURS-1 campaign involved a series of 5 cruises during 2012 - 2013 seeking to characterize the salinity structure and balance in a high salinity, high evaporation, and low rainfall region of the subtropical North Atlantic. It aims to resolve processes responsible for maintaining the subtropical surface salinity maximum in this region and within a 900 x 800-mile square study area centered at 25N, 38W.  The Seasoar is a towed vehicle equipped with impeller-forced wings that can be rotated on command to allow the vehicle to undulate in the upper ocean. Generally, Seasoar operates between the surface and about 400 meters depth while being towed on faired cable at about eight knots. A typical dive cycle takes about 12 minutes to complete, providing an up and down profile every 3 km.  For SPURS-1, a Seasoar was deployed exclusively during the Sarmiento cruise over the period 22 Mar-8 Apr, 2013 and to a maximum depth of 312m.  The Seasoar towed sensor system was equipped with dual pumped temperature/conductivity sensors.  The Seasoar data in netCDF form here contains a highly processed 1-meter gridded version of the original source dataset, which is comprised of temperature, conductivity, salinity, pressure observations from 1144 casts during 2013 Spring SPURS Cruise.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSPUR1-SEASR",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSPUR1-SEASR",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs1/docs/SpursWebsiteContent/Calendar/SpursCalendar.pdf",
-                    "description": "Meeting Materials, Cruise Blogs, and other archive artifacts",
                     "@type": "dcat:Distribution",
+                    "description": "Meeting Materials, Cruise Blogs, and other archive artifacts",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs1/docs/SpursWebsiteContent/Calendar/SpursCalendar.pdf",
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS1_SEASOAR.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS1_SEASOAR.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs1/docs/CruiseReports/12-10_Knorr_Cruise_Report.pdf",
-                    "description": "Cruise Reports",
                     "@type": "dcat:Distribution",
+                    "description": "Cruise Reports",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs1/docs/CruiseReports/12-10_Knorr_Cruise_Report.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs1/docs/DataDocumentation/SPURS1_DataSubmissionReport.pdf",
-                    "description": "Data Submission Report, Instrument Calibration Report, etc",
                     "@type": "dcat:Distribution",
+                    "description": "Data Submission Report, Instrument Calibration Report, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs1/docs/DataDocumentation/SPURS1_DataSubmissionReport.pdf",
+                    "mediaType": "application/pdf",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772317-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772317-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772317-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772317-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS1_SEASOAR.jpg",
+            "identifier": "C2491772317-POCLOUD",
+            "issued": "2015-04-06",
+            "keyword": [
+                "earth science",
+                "salinity/density",
+                "ocean temperature",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/SPUR1-SEASR",
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
+            "release-place": "Department of Physics and Physical Oceanography, University on North Carolina, Wilmington, NC, USA",
+            "series-name": "Seasoar CTD data for the SPURS-1 N. Atlantic field campaign",
             "spatial": "-39.0 22.0 -36.0 26.0",
+            "temporal": "2013-03-22T00:00:00Z/2013-04-08T00:00:00Z",
             "theme": [
                 "SPURS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Seasoar CTD data for the SPURS-1 N. Atlantic field campaign"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1432636960-GES_DISC.html",
             "citation": "Oxford University AOPP. 2017-10-31. SCRN4L1RAD_CDROM. Version 001. SCR/Nimbus-4 Level 1 Radiance Data from CD-ROM V001. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/SCRN4L1RAD_CDROM_001.html. Digital Science Data.",
-            "issued": "1998-02-24",
-            "temporal": "1970-07-27T00:00:00Z/1972-11-02T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1998-02-24",
-            "references": [
-                "https://doi.org/10.1098/rspa.1970.0196"
-            ],
-            "keyword": [
-                "earth science",
-                "infrared wavelengths",
-                "spectral/engineering"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JAMES JOHNSON",
                 "hasEmail": "mailto:James.Johnson@nasa.gov"
             },
+            "creator": "Oxford University AOPP",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1432636960-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "SCRN4L1RAD_CDROM is the gridded Nimbus-4 Selective Chopper Radiometer (SCR) Level 1 Radiance Data Product. The radiances are measured by 16 channels at 2.3 to 15 micrometers with a ground resolution of 25 km. The CD-ROM contains corrected radiances in a daily 4 degree latitude x 10 degree longitude grid format, as well as the original orbit format. The data for this product are available from 27 July 1970 to 2 November 1972. The principal investigator for the SCR experiment was Dr. John T. Houghton from Oxford University.\n\nThis product was created by the Oxford University's Atmospheric, Oceanic and Planetary Physics (AOPP) group. The data are stored on a single CD-ROM in ASCII files of hexadecimal characters, and are available in a single gzipped Unix tar archive file. The byte-ordering in the data files follows the DEC convention for 16-bit integers of less significant byte first. Normal 2's complement integer storage is assumed.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "SCRN4L1RAD_CDROM",
-            "creator": "Oxford University AOPP",
-            "graphic-preview-description": "First SCR temperature sounding.",
-            "title": "SCR/Nimbus-4 Level 1 Radiance Data from CD-ROM V001 (SCRN4L1RAD_CDROM) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/images/N4SCR_sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/images/N4SCR_sample.png",
-                    "description": "First SCR temperature sounding.",
                     "@type": "dcat:Distribution",
+                    "description": "First SCR temperature sounding.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/images/N4SCR_sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SCRN4L1RAD_CDROM_001.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SCRN4L1RAD_CDROM_001.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus4_SCR_Level1/SCRN4L1RAD_CDROM.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus4_SCR_Level1/SCRN4L1RAD_CDROM.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SCRN4L1RAD_CDROM",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SCRN4L1RAD_CDROM",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus4_SCR_Level1/SCRN4L1RAD_CDROM.001/doc/README.SCRN4L1RAD_CDROM_001.txt",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus4_SCR_Level1/SCRN4L1RAD_CDROM.001/doc/README.SCRN4L1RAD_CDROM_001.txt",
+                    "mediaType": "text/html",
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
                 }
             ],
+            "graphic-preview-description": "First SCR temperature sounding.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/images/N4SCR_sample.png",
+            "identifier": "C1432636960-GES_DISC",
+            "issued": "1998-02-24",
+            "keyword": [
+                "earth science",
+                "infrared wavelengths",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1432636960-GES_DISC.html",
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
+                "https://doi.org/10.1098/rspa.1970.0196"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "SCRN4L1RAD_CDROM",
             "spatial": "-180.0 -80.0 180.0 80.0",
+            "temporal": "1970-07-27T00:00:00Z/1972-11-02T23:59:59.999Z",
             "theme": [
                 "Nimbus",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SCR/Nimbus-4 Level 1 Radiance Data from CD-ROM V001 (SCRN4L1RAD_CDROM) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0719-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-20T05:52:25.000 to 2015-04-20T13:00:09.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0719-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0719-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0719-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-20T05:52:25.000 to 2015-04-20T13:00:09.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0719 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0719 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSIWAC-3-CR4A-CHECKOUT-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the CRUISE 4-1 mission phase, covering the period  from 2008-01-28T00:00:00.000 to 2008-08-03T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Reprocessed dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osiwac-3-cr4a-checkout-v2.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "58 aql",
                 "international rosetta mission",
                 "16 cyg b",
                 "jupiter"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSIWAC-3-CR4A-CHECKOUT-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osiwac-3-cr4a-checkout-v2.0",
-            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the CRUISE 4-1 mission phase, covering the period  from 2008-01-28T00:00:00.000 to 2008-08-03T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Reprocessed dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER CHECKOUT OSIWAC 3 CR4A RDR V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECKOUT OSIWAC 3 CR4A RDR V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/jxtq-bsqu",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "To reveal outcomes of microgravity on molecular processes within the cellular environment we have employed a mass-spectrometry based proteomics approach. Proteomics analysis based on mass spectrometry allows for the relative quantitation of a large number of proteins concurrently and in a relatively unbiased manner. Mass spectrometry based proteomics can be rendered even more informative by addition of a labeling component to understand the dynamics of the changing protein content. In this study we utilized a combination of proteomics techniques namely label-free quantification and dynamic stable-isotope labeling by amino acids in cell culture (Dynamic SILAC) to characterize the microgravity stress response in primary cardiomyocytes.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-122",
+                    "mediaType": "text/html",
+                    "title": "Microgravity induces proteomics changes involved in endoplasmic reticulum stress and mitochondrial protection"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-122_jxtq-bsqu",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "data transformation",
                 "labeling",
@@ -1002132,104 +1002146,70 @@
                 "extraction",
                 "timepoint"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/jxtq-bsqu",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-122_jxtq-bsqu",
-            "description": "To reveal outcomes of microgravity on molecular processes within the cellular environment we have employed a mass-spectrometry based proteomics approach. Proteomics analysis based on mass spectrometry allows for the relative quantitation of a large number of proteins concurrently and in a relatively unbiased manner. Mass spectrometry based proteomics can be rendered even more informative by addition of a labeling component to understand the dynamics of the changing protein content. In this study we utilized a combination of proteomics techniques namely label-free quantification and dynamic stable-isotope labeling by amino acids in cell culture (Dynamic SILAC) to characterize the microgravity stress response in primary cardiomyocytes.",
-            "title": "Microgravity induces proteomics changes involved in endoplasmic reticulum stress and mitochondrial protection",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-122",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Microgravity induces proteomics changes involved in endoplasmic reticulum stress and mitochondrial protection"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Microgravity induces proteomics changes involved in endoplasmic reticulum stress and mitochondrial protection"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VEGA1-C-IKS-3-RDR-HALLEY-PROCESSED-V1.0",
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
-                "vega 1",
-                "halley"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The IKS data from Vega-1 came in various forms. The initial submission from IKI by Dyachkov was in GROUP FITS (binary) for the 'imaging channel'. A separate submission came through the IHW Infrared Studies Discipline and also contained data presented in the FITS format (IHW keywords) for the two 'infrared channels'. In the former case, the three Pvalues carried information on the distance and two angles used to locate the position of the comet on the slit. The other simple keyword values marked only the date, mission, and experiment. The latter data, had not only 101 individual spectra for the 3-5 micron measurements but a composite 'final' 6-12 micron spectrum with associated 'figure 7' from the published results (COMBES, M. et al. 1988, Icarus, 76, 404). For these 101 spectra a cometo-centric distance was quoted rather than a time micron data. Using this information, the distance range was 270534.9 to 39273.22 km. From this comparison, it is inferred that the distance quoted in the IKI submission is also cometo-centric (31596.0 to 16092 km)",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vega1-c-iks-3-rdr-halley-processed-v1.0_jxxg-pibt",
+            "issued": "2021-05-21",
+            "keyword": [
+                "vega 1",
+                "halley"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VEGA1-C-IKS-3-RDR-HALLEY-PROCESSED-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vega1-c-iks-3-rdr-halley-processed-v1.0_jxxg-pibt",
-            "description": "The IKS data from Vega-1 came in various forms. The initial submission from IKI by Dyachkov was in GROUP FITS (binary) for the 'imaging channel'. A separate submission came through the IHW Infrared Studies Discipline and also contained data presented in the FITS format (IHW keywords) for the two 'infrared channels'. In the former case, the three Pvalues carried information on the distance and two angles used to locate the position of the comet on the slit. The other simple keyword values marked only the date, mission, and experiment. The latter data, had not only 101 individual spectra for the 3-5 micron measurements but a composite 'final' 6-12 micron spectrum with associated 'figure 7' from the published results (COMBES, M. et al. 1988, Icarus, 76, 404). For these 101 spectra a cometo-centric distance was quoted rather than a time micron data. Using this information, the distance range was 270534.9 to 39273.22 km. From this comparison, it is inferred that the distance quoted in the IKI submission is also cometo-centric (31596.0 to 16092 km)",
-            "title": "VEGA1 INFRARED SPECTROMETER HIGH RESOLUTION DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VEGA1 INFRARED SPECTROMETER HIGH RESOLUTION DATA V1.0"
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
-                "tool",
-                "nasaview"
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
-            "identifier": "NASA-503",
             "description": "Nasaview (3.9.0)",
-            "title": "PDS Software Release Nasaview (3.9.0)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1002237,386 +1002217,415 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-503",
+            "issued": "2018-06-25",
+            "keyword": [
+                "pds",
+                "tool",
+                "nasaview"
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
+            "title": "PDS Software Release Nasaview (3.9.0)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7265/g2m7-7014",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Arctic Ice Dynamics Joint Experiment (AIDJEX) Second Pilot Study, March - May 1972: Still Images, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center. https://doi.org/10.7265/g2m7-7014.",
-            "issued": "1972-03-01",
-            "temporal": "1972-03-01T00:00:00Z/1972-05-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1972-05-31",
-            "keyword": [
-                "cryosphere",
-                "sea ice",
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
-            "identifier": "C2747978314-NSIDCV0",
             "description": "This data set contains photographs of camps on drifting sea ice from the early 1970s along with a few aerial photographs of the drifting ice station T-3. Most of the photos were taken during a pilot study conducted in 1972 in preparation for the AIDJEX main experiment of 1975 to 1976. There are 83 photos in JPEG format with captions available for 60 of them, which are listed in an accompanying Excel (.xlsx) file. The photos were taken by Tom Marlar of the U.S. Army Cold Regions Research and Engineering Laboratory (CRREL). Pat Martin took the aerial photographs.\n\nThe pilot study included a main camp on drifting sea ice in the Beaufort Sea north of Alaska along with two satellite camps forming a station triangle with a 100 km side length. Additional details on the AIDJEX experiment can be found on the <a href=\"https://nsidc.org/data/aidjex\">NOAA@NSIDC AIDJEX web site</a>. Also, a detailed description of the observational program and a running account of the results can be found in the AIDJEX Bulletin series published between 1970 and the end of the project in 1978. The Polar Science Center at the University of Washington maintains an AIDJEX electronic library at <a href=\"http://psc.apl.washington.edu/nonwp_projects/aidjex/\">http://psc.apl.washington.edu/nonwp_projects/aidjex/</a>. It includes downloadable copies of the contents of all 40 AIDJEX Bulletins, AIDJEX Operations Manuals for the Pilot Study and the Main Experiment, and other resources.\n\nThese photographs existed as 8\u201d x 10\u201d prints in the analog collection of material at NSIDC, and were scanned under the direction of the NSIDC archivist around 2007. The captions come from text that was written on the prints. Some captions may have been added to at a later date. \n\nAt least four of the photographs are not from AIDJEX, but are aerial photographs of Fletcher\u2019s Ice Island, or T-3.   In 1972, when the AIDJEX pilot study was taking place in the Beaufort Sea, T-3 was north of the Canadian Archipelago and on its way East, as explained in the caption for AIDJEX_1972_002.jpg.  According to the captions, the T-3 photos were taken in 1974.  We believe that these photographs, like other aerial shots, were taken by Pat Martin, and included with other 8\u201d x 10\u201d prints that may have been sent to NSIDC by personnel at CRREL.\n\nThe track of T-3, as well as data from T-3 and other drifting ice stations, can be found on the <a href=\"https://nsidc.org/data/g01938\">EWG Arctic Meteorology and Climate Atlas</a>",
-            "title": "Arctic Ice Dynamics Joint Experiment (AIDJEX) Second Pilot Study, March - May 1972: Still Images, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2Fg2m7-7014",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2Fg2m7-7014",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://noaadata.apps.nsidc.org/NOAA/G10042/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://noaadata.apps.nsidc.org/NOAA/G10042/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/g2m7-7014",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/g2m7-7014",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/g2m7-7014",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/g2m7-7014",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2747978314-NSIDCV0",
+            "issued": "1972-03-01",
+            "keyword": [
+                "cryosphere",
+                "sea ice",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.7265/g2m7-7014",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1972-05-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "-165.0 72.0 -125.0 80.0",
+            "temporal": "1972-03-01T00:00:00Z/1972-05-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Arctic Ice Dynamics Joint Experiment (AIDJEX) Second Pilot Study, March - May 1972: Still Images, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-ALBEDOS-V1.0",
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
+            "description": "Collected geometric albedos at various frequencies for 2030 asteroids.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-albedos-v1.0_jxzy-gu6g",
+            "issued": "2018-06-26",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-ALBEDOS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-albedos-v1.0_jxzy-gu6g",
-            "description": "Collected geometric albedos at various frequencies for 2030 asteroids.",
-            "title": "ASTEROID ALBEDOS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ASTEROID ALBEDOS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2331489981-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC.",
-            "issued": "2019-06-23",
-            "temporal": "2000-02-24T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-10-01",
-            "keyword": [
-                "national geospatial data asset",
-                "earth science",
-                "oceans",
-                "ocean optics",
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
-            "identifier": "C2331489981-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "Terra MODIS Global Binned Photosynthetically Available Radiation (PAR) - Near Real Time (NRT) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-3%20Binned/Terra-MODIS/",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-3%20Binned/Terra-MODIS/",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/TERRA/MODIS/L3B/PAR/2022",
-                    "description": "MODIS-Terra L3B Photosynthetically Available Radiation (PAR) - Near Real Time (NRT) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS-Terra L3B Photosynthetically Available Radiation (PAR) - Near Real Time (NRT) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/TERRA/MODIS/L3B/PAR/2022",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2331489981-OB_DAAC",
+            "issued": "2019-06-23",
+            "keyword": [
+                "national geospatial data asset",
+                "earth science",
+                "oceans",
+                "ocean optics",
+                "ngda"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2331489981-OB_DAAC.html",
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
+            "temporal": "2000-02-24T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Terra MODIS Global Binned Photosynthetically Available Radiation (PAR) - Near Real Time (NRT) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2H2ON_L2.007",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2017-10-17. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AURA/TES/TL2H2ON_L2.007. https://asdc.larc.nasa.gov/project/TES.",
-            "issued": "2015-08-27",
-            "temporal": "2004-08-22T00:00:00Z/2018-01-22T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "atmospheric temperature",
-                "atmosphere",
-                "clouds",
-                "earth science",
-                "atmospheric chemistry",
-                "atmospheric water vapor"
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
-            "identifier": "C1331182620-LARC",
             "description": "TL2H2ON_7 is the Tropospheric Emission Spectrometer (TES)/Aura Level 2 Water Vapor Nadir Version 7 data product. It consists of information for one molecular species for an entire Global Survey or Special Observation. TES was an instrument aboard NASA's Aura satellite and was launched from California on July 15, 2004. Data collection for TES is complete. TES Level 2 data contain retrieved species (or temperature) profiles at the observation targets and the estimated errors. The geolocation, quality, and other data (e.g., surface characteristics for nadir observations) were also provided. L2 modeled spectra were evaluated using radiative transfer modeling algorithms. The process, referred to as retrieval, compared observed spectra to the modeled spectra and iteratively updated the atmospheric parameters. L2 standard product files included information for one molecular species (or temperature) for an entire global survey or special observation run. A global survey consisted of a maximum of 16 consecutive orbits.\r\rNadir observations, which point directly to the surface of the Earth, are different from limb observations, which are pointed at various off-nadir angles into the atmosphere. Nadir and limb observations were added to separate L2 files, and a single ancillary file was composed of data that are common to both nadir and limb files. A Nadir sequence within the TES Global Survey was a fixed number of observations within an orbit for a Global Survey. Prior to April 24, 2005, it consisted of two low resolution scans over the same ground locations. After April 24, 2005, Global Survey data consisted of three low resolution scans. The Nadir standard product consists of four files, where each file is composed of the Global Survey Nadir observations from one of four focal planes for a single orbit, i.e. 72 orbit sequences. The Global Survey Nadir observations only used a single set of filter mix. \r\rA Global Survey consisted of observations along 16 consecutive orbits at the start of a two day cycle, over which 4,608 retrievals were performed. Each observation was the input for retrievals of species Volume Mixing Ratios (VMRs), temperature profiles, surface temperature, and other data parameters with associated pressure levels, precision, total error, vertical resolution, total column density, and other diagnostic quantities. Each TES Level 2 standard product reported information in a swath format conforming to the HDF-EOS Aura File Format Guidelines. Each Swath object was bounded by the number of observations in a global survey and a predefined set of pressure levels, representing slices through the atmosphere. Each standard product could have had a variable number of observations depending upon the Global Survey configuration and whether averaging was employed. Also, missing or bad retrievals were not reported. Further, observations were occasionally scheduled on non-global survey days. In general they were measurements made for validation purposes or with highly focused science objectives. Those non-global survey measurements were referred to as \u201cspecial observations.\u201d\r\rA Limb sequence within the TES Global Survey was three high-resolution scans over the same limb locations. The Limb standard product consists of four files, where each file is composed of the Global Survey Limb observations from one of four focal planes for a single orbit, i.e. 72 orbit sequences. The Global Survey Limb observations used a repeating sequence of filter wheel positions. Special Observations could only be scheduled during the 9 or 10 orbit gaps in the Global Surveys, and were conducted in any of three basic modes: stare, transect, step-and-stare. The mode used depended on the science requirement. Each limb observation Limb 1, Limb 2 and Limb 3, were processed independently. Thus, each limb standard product consisted of three sets where each set consisted of 1,152 observations. For TES, the swath object represented one of these sets. Thus, each limb s",
-            "title": "TES/Aura L2 Water Vapor Nadir V007",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2H2ON_L2.007",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2H2ON_L2.007",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1331182620-LARC",
-                    "description": "Earthdata Search for TL2H2ON_7 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TL2H2ON_7 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1331182620-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2H2ON_L2.007",
-                    "description": "DOI data set landing page for TL2H2ON_7",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TL2H2ON_7",
+                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2H2ON_L2.007",
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
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2H2ON.007/contents.html",
-                    "description": "OPeNDAP data access for TL2H2ON_7",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for TL2H2ON_7",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2H2ON.007/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2H2ON.007/",
-                    "description": "ASDC Direct Data Download for TL2H2ON_7",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for TL2H2ON_7",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2H2ON.007/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
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
+            "identifier": "C1331182620-LARC",
+            "issued": "2015-08-27",
+            "keyword": [
+                "atmospheric temperature",
+                "atmosphere",
+                "clouds",
+                "earth science",
+                "atmospheric chemistry",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2H2ON_L2.007",
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
+            "temporal": "2004-08-22T00:00:00Z/2018-01-22T23:59:59Z",
             "theme": [
                 "TES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TES/Aura L2 Water Vapor Nadir V007"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-ER-3-PREMAP%2FOMNIDIR-FLUX-V1.0",
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
+            "description": "The Electron Reflectometer Data Record (ERDR) is a time ordered series of electron measurements from the Mars Global Surveyor (MGS) Mission. Each record consists of a time tag with 19 scalar data points representing measurements of the electron flux in 19 different energy channels, ranging from 10 eV to 20 keV, with an energy resolution of 25%. Each data point is a measure of the electron flux (cm-2 sec-1 ster-1 eV-1) averaged over a 360 x 14 degree disk-shaped field of view (FOV). (Parts of this FOV are masked because of spacecraft obstructions, as described below.) During the Science Phasing Orbits (SPO), the spacecraft was in Array Normal Spin (ANS) configuration, for which the ER field of view sweeps out the entire sky (4-pi ster) every 50 minutes, which is much longer than the integration time per record (2 to 48 sec, depending on energy and telemetry rate) and much longer than most timescales of interest in Mars&apos; plasma environment.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-er-3-premap-omnidir-flux-v1.0_jy4s-qpuv",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars global surveyor"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-ER-3-PREMAP%2FOMNIDIR-FLUX-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-er-3-premap-omnidir-flux-v1.0_jy4s-qpuv",
-            "description": "The Electron Reflectometer Data Record (ERDR) is a time ordered series of electron measurements from the Mars Global Surveyor (MGS) Mission. Each record consists of a time tag with 19 scalar data points representing measurements of the electron flux in 19 different energy channels, ranging from 10 eV to 20 keV, with an energy resolution of 25%. Each data point is a measure of the electron flux (cm-2 sec-1 ster-1 eV-1) averaged over a 360 x 14 degree disk-shaped field of view (FOV). (Parts of this FOV are masked because of spacecraft obstructions, as described below.) During the Science Phasing Orbits (SPO), the spacecraft was in Array Normal Spin (ANS) configuration, for which the ER field of view sweeps out the entire sky (4-pi ster) every 50 minutes, which is much longer than the integration time per record (2 to 48 sec, depending on energy and telemetry rate) and much longer than most timescales of interest in Mars&apos; plasma environment.",
-            "title": "MGS MARS/MOONS MAG/ER PRE-MAP ER OMNIDIRECTIONAL FLUX V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MGS MARS/MOONS MAG/ER PRE-MAP ER OMNIDIRECTIONAL FLUX V1.0"
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
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20140602.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-441",
+            "issued": "2018-06-25",
             "keyword": [
                 "hirise",
                 "rss",
@@ -1002626,79 +1002635,96 @@
                 "ctx",
                 "crism"
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
-            "identifier": "NASA-441",
-            "description": "CRISM, CTX, HiRISE, MARCI, MCS, RSS, SPICE",
-            "title": "PDS Mars Reconnaissance Orbiter Data 29",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20140602.shtml",
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
+            "title": "PDS Mars Reconnaissance Orbiter Data 29"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=STARDUST-CAL-NC-2-PREFLIGHT-V1.0",
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
-                "stardust",
-                "calimg"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains the results of the preflight calibration of the Stardust Navigation Camera. The images were collected in an attempt to mimic the environment that the camera would experience during cruise and encounter with the comet Wild-2. These data are saved for historical reasons. They are not considered to be of archival quality.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.stardust-cal-nc-2-preflight-v1.0_jymb-j4ef",
+            "issued": "2021-05-21",
+            "keyword": [
+                "stardust",
+                "calimg"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=STARDUST-CAL-NC-2-PREFLIGHT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.stardust-cal-nc-2-preflight-v1.0_jymb-j4ef",
-            "description": "This data set contains the results of the preflight calibration of the Stardust Navigation Camera. The images were collected in an attempt to mimic the environment that the camera would experience during cruise and encounter with the comet Wild-2. These data are saved for historical reasons. They are not considered to be of archival quality.",
-            "title": "STARDUST NAVCAM PREFLIGHT CALIB ARCHIVE",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "STARDUST NAVCAM PREFLIGHT CALIB ARCHIVE"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "http://techport.nasa.gov/view/69",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Andrew Eckel",
+                "hasEmail": "mailto:andrew.j.eckel@nasa.gov"
+            },
+            "description": "&lt;p&gt;\r\n\tThe Space Technology Research Grants Program will accelerate the development of &amp;quot;push&amp;quot; technologies to support the future space science and exploration needs of NASA, other government agencies and the commercial space sector. Innovative efforts with high risk and high payoff will be encouraged. The program is composed of two competitively awarded components.&lt;/p&gt;",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://techport.nasa.gov/xml-api/69",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "TECHPORT_69",
             "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
+            "keyword": [
+                "program",
+                "nasa headquarters",
+                "active",
+                "strgp"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/69",
             "modified": "2020-01-29",
+            "programCode": [
+                "026:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Space Technology Mission Directorate"
+            },
             "references": [
                 "http://techport.nasa.gov/home",
                 "http://techport.nasa.gov/doc/home/TechPort_Advanced_Search.pdf",
@@ -1002709,47 +1002735,30 @@
                 "http://techport.nasa.gov/fetchFile?objectId=6560",
                 "http://techport.nasa.gov/fetchFile?objectId=3448"
             ],
-            "keyword": [
-                "program",
-                "nasa headquarters",
-                "active",
-                "strgp"
+            "title": "Space Technology Research Grants Program"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "026:00"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
-                "fn": "Andrew Eckel",
-                "hasEmail": "mailto:andrew.j.eckel@nasa.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Space Technology Mission Directorate"
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
-            "identifier": "TECHPORT_69",
-            "description": "&lt;p&gt;\r\n\tThe Space Technology Research Grants Program will accelerate the development of &amp;quot;push&amp;quot; technologies to support the future space science and exploration needs of NASA, other government agencies and the commercial space sector. Innovative efforts with high risk and high payoff will be encouraged. The program is composed of two competitively awarded components.&lt;/p&gt;",
-            "title": "Space Technology Research Grants Program",
-            "programCode": [
-                "026:000"
-            ],
+            "description": "APXS, HAZCAM, MB, MI, MTES, NAVCAM, PANCAM, SPICE",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "http://techport.nasa.gov/xml-api/69",
-                    "mediaType": "application/xml"
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/PDS-Subscription-Service-01-Feb-07.shtml",
+                    "mediaType": "application/html"
                 }
-            ]
-        },
-        {
-            "accessLevel": "restricted public",
-            "landingPage": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-Release.shtml",
-            "bureauCode": [
-                "026:00"
             ],
+            "identifier": "NASA-621",
             "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "https://pds.jpl.nasa.gov/"
-            ],
             "keyword": [
                 "mtes",
                 "apxs",
@@ -1002761,295 +1002770,262 @@
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
-            "identifier": "NASA-621",
-            "description": "APXS, HAZCAM, MB, MI, MTES, NAVCAM, PANCAM, SPICE",
-            "title": "PDS Mars Exploration Rovers Data Release 11",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/PDS-Subscription-Service-01-Feb-07.shtml",
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
+            "title": "PDS Mars Exploration Rovers Data Release 11"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/TAHOE/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/TAHOE/DATA001.",
-            "issued": "2001-09-18",
-            "temporal": "2001-09-18T16:30:00Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean optics",
-                "ocean chemistry",
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
-            "identifier": "C1633360670-OB_DAAC",
             "description": "Measurements made in Lake Tahoe in Northern California during 2001.",
-            "title": "Optical measurements in Lake Tahoe during 2001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FTAHOE%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FTAHOE%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/TAHOE/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/TAHOE/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360670-OB_DAAC",
+            "issued": "2001-09-18",
+            "keyword": [
+                "ocean optics",
+                "ocean chemistry",
+                "salinity/density",
+                "ocean temperature",
+                "oceans",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/TAHOE/DATA001",
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
+            "temporal": "2001-09-18T16:30:00Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Optical measurements in Lake Tahoe during 2001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "http://techport.nasa.gov/view/14675",
-            "issued": "2013-01-01",
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
-                "project",
-                "hyfoss",
-                "armstrong flight research center",
-                "active"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Allen Parker",
                 "hasEmail": "mailto:allen.r.parker@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Human Exploration and Operations Mission Directorate"
-            },
-            "identifier": "TECHPORT_14675",
             "description": "&lt;p&gt;Armstrong researchers are continuing their efforts to further develop FOSS technologies. A hybrid FOSS technique (HyFOSS) employs conventional continuous grating fibers and then overlays sections every 3-4 feet with &amp;ldquo;strong&amp;rdquo; gratings that can be sampled at higher rates. The new and stronger gratings can be sampled at rates up to 5,000 Hertz (Hz) while the continuous grating sections continue to be sampled at the lower 100 Hz rate. This technique enables higher spatial resolution at specific targets without sacrificing resolution in other areas. The ultimate goal is to achieve sampling rates up to 20 kHz.&lt;/p&gt;&lt;p&gt;&lt;strong&gt;Work to date&lt;/strong&gt;: The team began investigating the technique in early 2013 after a request from NASA Kennedy Space Center. Many aerospace and space vehicles &amp;ndash; fighter aircraft, UAVs, launch vehicles, and spacecraft &amp;ndash; could benefit from FOSS integration. Some of the applications require higher sample rates to maintain high spatial resolution. NASA Kennedy&amp;rsquo;s Launch Services Group requested that the NASA Armstrong Advanced Structures and Measurements Group investigate the development effort that would be required to increase the sample rate from 100 hertz (Hz) to over 20 kHz. This increased sampling capability would allow structural features related to high frequency shock and/or vibration to be captured. To date, the OFDR technology does not have the capability to achieve these higher sample rates, though the possibility of fusing Wavelength Division Multiplexing (WDM) is feasible yet with limited spatial resolution. To achieve this with existing instrumentation would require the installation of two technologies, one utilizing OFDR and the other using WDM, and would increase the weight and installation requirement of fiber optic instrumentation.&lt;/p&gt;&lt;p&gt;Combining the best of OFDR and WDM technologies into new hardware that utilizes the same optical fiber would allow for high spatial resolution with lower sample rates in addition to the ability to obtain high sample rates at strategically spaced points along the fiber. With this goal, the hybrid FOSS (hyFOSS) system was developed.&lt;/p&gt;&lt;p&gt;A series of weak and strong FBGs are written onto the optical fiber. Weak FBGs allow for spatial resolution of 0.25 inches. The maximum number of stronger, unique-wavelength FBGs and the minimum separation interval between the sensors are determined by the length of the fiber and the wavelength spectrum of the light source. However, there is latitude to allow for the number and placement of the sensors to be tailored to the testing application.&lt;/p&gt;&lt;p&gt;&lt;strong&gt;Looking ahead&lt;/strong&gt;: Researchers have asked the company that currently provides the fibers to supply a 40-ft strand embedded with the new technology. Next steps involving investigating the specimen in the laboratory environment. The Armstrong team is also investigating the possibilities of pushing the overall sample rate to 20kHz.&lt;/p&gt;&lt;p&gt;&lt;strong&gt;&lt;em&gt;Benefits&lt;/em&gt;&lt;/strong&gt;&lt;/p&gt;&lt;ul&gt;&lt;li&gt;&lt;strong&gt;More measurements&lt;/strong&gt;: Offers higher sampling rates (up to 5,000 Hz) for specific portions of the fiber&lt;/li&gt;&lt;li&gt;&lt;strong&gt;Fast processing&lt;/strong&gt;: Data can be collected at different resolutions enabling high resolution without sacrificing speed&lt;/li&gt;&lt;/ul&gt;&lt;p&gt;&lt;strong&gt;&lt;em&gt;Applications&lt;/em&gt;&lt;/strong&gt;&lt;/p&gt;&lt;ul&gt;&lt;li&gt;Aeronautics and launch vehicles&lt;/li&gt;&lt;/ul&gt;",
-            "title": "Hybrid FOSS Project",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "http://techport.nasa.gov/xml-api/14675",
                     "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "TECHPORT_14675",
+            "issued": "2013-01-01",
+            "keyword": [
+                "project",
+                "hyfoss",
+                "armstrong flight research center",
+                "active"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/14675",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Human Exploration and Operations Mission Directorate"
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
+            "title": "Hybrid FOSS Project"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FCAL-ALICE-2-ESC1-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains CODMAC Level 2 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the comet 67P/Churyumov-Gerasimenko Comet Escort 1 mission phase, which took place between 2014-11-20 and 2015-03-10.  The current V2.0 data set supersedes the previous V1.0 data set.  Pixel list data files have had corrections applied to their FITS formatting.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cal-alice-2-esc1-v2.0",
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
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FCAL-ALICE-2-ESC1-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cal-alice-2-esc1-v2.0",
-            "description": "This data set contains CODMAC Level 2 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the comet 67P/Churyumov-Gerasimenko Comet Escort 1 mission phase, which took place between 2014-11-20 and 2015-03-10.  The current V2.0 data set supersedes the previous V1.0 data set.  Pixel list data files have had corrections applied to their FITS formatting.",
-            "title": "ROSETTA-ORBITER 67P/CAL ALICE 2 ESC1 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P/CAL ALICE 2 ESC1 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC4-67P-M22-STR-REFL-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 4 mission phase, covering the period from 2015-10-20T23:25:00.000 to 2015-11-17T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc4-67p-m22-str-refl-v1.0_jywz-8gpi",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC4-67P-M22-STR-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc4-67p-m22-str-refl-v1.0_jywz-8gpi",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 4 mission phase, covering the period from 2015-10-20T23:25:00.000 to 2015-11-17T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC4-MTP022 RDR-STR-REFL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC4-MTP022 RDR-STR-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-CAL-HRIV-2-EPOXI-CALIBRATIONS-V1.0",
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
-                "calibration"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains raw calibration images acquired by the Deep Impact Medium Resolution Visible CCD from 04 October 2007 through 17 December 2008 for the EPOXI mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-cal-hriv-2-epoxi-calibrations-v1.0_jyxd-77ew",
+            "issued": "2021-05-21",
+            "keyword": [
+                "epoxi",
+                "calibration"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-CAL-HRIV-2-EPOXI-CALIBRATIONS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-cal-hriv-2-epoxi-calibrations-v1.0_jyxd-77ew",
-            "description": "This data set contains raw calibration images acquired by the Deep Impact Medium Resolution Visible CCD from 04 October 2007 through 17 December 2008 for the EPOXI mission.",
-            "title": "EPOXI INFLIGHT CALIBRATIONS - HRIV RAW IMAGES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "EPOXI INFLIGHT CALIBRATIONS - HRIV RAW IMAGES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/OMI/DATA2435",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Joanna Joiner. 2023-06-01. OMUFPSLV. Version 004. GEOS-5 FP-IT 3D Time-Averaged Single-Level Diagnostics Geo-Colocated to OMI/Aura UV2 1-Orbit L2 Swath 13x24km V4. NASA Goddard Space Flight Center. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/OMI/DATA2435. https://disc.gsfc.nasa.gov/datacollection/OMUFPSLV_004.html. Digital Science Data. https://aura.gsfc.nasa.gov/.",
-            "issued": "2023-03-31",
-            "temporal": "2004-10-01T00:00:00Z/2023-06-12T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-03-31",
-            "keyword": [
-                "earth science",
-                "atmospheric winds",
-                "atmosphere",
-                "atmospheric temperature",
-                "atmospheric pressure"
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
-            "identifier": "C2556147807-GES_DISC",
-            "description": "The GEOS-5 FP-IT 3D Time-Averaged Single-Level Diagnostics Geo-Colocated to OMI/Aura UV2 1-Orbit L2 Swath 13x24km (OMUFPSLV) provides selected parameters from GEOS-5 Forward Processing for Instrument Teams (FP-IT) assimilated product produced by the Global Modeling and Assimilation Office (GMAO) co-located in space and time with the OMI UV-2 swath.\n\nThe fields in this product include boundary layer top pressure, tropopause pressure, surface pressure, surface skin temperature, and vertical wind profiles at 10m. The OMI team also provides a corresponding product for the OMI VIS swath, OMVFPSLV. The product has been generated for convenient use by the OMI/Aura team in their L2 algorithms, and for research where those L2 products are used. The original GEOS-5 FP-IT data are reported on a 0.625 deg longitude by 0.5 deg latitude grid, whereas the OMI UV-2 spatial resolution is 13km x 24km at nadir.\n\nThe OMUFPSLV files are in netCDF4 format which is compatible with most netCDF and HDF5 readers and tools.  Each file is approximately 45mb in size. The lead for this product is Zachary Fasnacht of SSAI. Joanna Joiner is the responsible NASA official.",
-            "release-place": "NASA Goddard Space Flight Center",
-            "series-name": "OMUFPSLV",
             "creator": "Joanna Joiner",
-            "title": "GEOS-5 FP-IT 3D Time-Averaged Single-Level Diagnostics Geo-Colocated to OMI/Aura UV2 1-Orbit L2 Swath 13x24km V4 (OMUFPSLV) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMUFPSLV_004.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The GEOS-5 FP-IT 3D Time-Averaged Single-Level Diagnostics Geo-Colocated to OMI/Aura UV2 1-Orbit L2 Swath 13x24km (OMUFPSLV) provides selected parameters from GEOS-5 Forward Processing for Instrument Teams (FP-IT) assimilated product produced by the Global Modeling and Assimilation Office (GMAO) co-located in space and time with the OMI UV-2 swath.\n\nThe fields in this product include boundary layer top pressure, tropopause pressure, surface pressure, surface skin temperature, and vertical wind profiles at 10m. The OMI team also provides a corresponding product for the OMI VIS swath, OMVFPSLV. The product has been generated for convenient use by the OMI/Aura team in their L2 algorithms, and for research where those L2 products are used. The original GEOS-5 FP-IT data are reported on a 0.625 deg longitude by 0.5 deg latitude grid, whereas the OMI UV-2 spatial resolution is 13km x 24km at nadir.\n\nThe OMUFPSLV files are in netCDF4 format which is compatible with most netCDF and HDF5 readers and tools.  Each file is approximately 45mb in size. The lead for this product is Zachary Fasnacht of SSAI. Joanna Joiner is the responsible NASA official.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FOMI%2FDATA2435",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FOMI%2FDATA2435",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1003059,122 +1003035,123 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMUFPSLV_004.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMUFPSLV_004.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Ancillary/OMUFPSLV.004/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Ancillary/OMUFPSLV.004/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMUFPSLV_004",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMUFPSLV_004",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/opendap/Aura_OMI_Ancillary/OMUFPSLV.004/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/opendap/Aura_OMI_Ancillary/OMUFPSLV.004/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OMI/AURA-OMI-KNMI-L01B-0005-SD-iods-v024148-20210702.pdf",
-                    "description": "OMI v4 L01B Algorithm Theoretical Basis Documents",
                     "@type": "dcat:Distribution",
+                    "description": "OMI v4 L01B Algorithm Theoretical Basis Documents",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OMI/AURA-OMI-KNMI-L01B-0005-SD-iods-v024148-20210702.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level2/OMUFPSLV.004/doc/OMxFPSLV_README.pdf",
-                    "description": "Product README",
                     "@type": "dcat:Distribution",
+                    "description": "Product README",
+                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level2/OMUFPSLV.004/doc/OMxFPSLV_README.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OMI/OMUFPSLV.fs",
-                    "description": "File Specification Document",
                     "@type": "dcat:Distribution",
+                    "description": "File Specification Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OMI/OMUFPSLV.fs",
+                    "mediaType": "text/html",
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
-                    "downloadURL": "https://www.knmiprojects.nl/projects/ozone-monitoring-instrument",
-                    "description": "OMI KNMI Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "OMI KNMI Home Page",
+                    "downloadURL": "https://www.knmiprojects.nl/projects/ozone-monitoring-instrument",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://projects.knmi.nl/omi/research/documents/",
-                    "description": "List of Publications",
                     "@type": "dcat:Distribution",
+                    "description": "List of Publications",
+                    "downloadURL": "http://projects.knmi.nl/omi/research/documents/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMUFPSLV_004.png",
+            "identifier": "C2556147807-GES_DISC",
+            "issued": "2023-03-31",
+            "keyword": [
+                "earth science",
+                "atmospheric winds",
+                "atmosphere",
+                "atmospheric temperature",
+                "atmospheric pressure"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/OMI/DATA2435",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-03-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "NASA Goddard Space Flight Center",
+            "series-name": "OMUFPSLV",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2004-10-01T00:00:00Z/2023-06-12T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GEOS-5 FP-IT 3D Time-Averaged Single-Level Diagnostics Geo-Colocated to OMI/Aura UV2 1-Orbit L2 Swath 13x24km V4 (OMUFPSLV) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1236350970-GES_DISC.html",
             "citation": "OMI Science Team. GES DISC. 2012-07-01. OMSO2_CPR. Version 003. OMI/Aura Level 2 Sulphur Dioxide (SO2) Trace Gas Column Data 1-Orbit subset Swath along CloudSat track 1-Orbit Swath 13x24 km. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/OMSO2_CPR_003.html. Digital Science Data.",
-            "issued": "2006-06-01",
-            "temporal": "2006-06-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-03-02",
-            "keyword": [
-                "atmospheric chemistry",
-                "earth science",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NICKOLAY KROTKOV, PH. D",
                 "hasEmail": "mailto:Nickolay.A.Krotkov@nasa.gov"
             },
+            "creator": "OMI Science Team",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1236350970-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "This is a CloudSat-collocated subset of the original product OMSO2, for the purposes of the A-Train mission.  The goal of the subset is to select and return OMI data that are within +/-100 km across the CloudSat track. The resultant OMI subset swath is sought to be about 200 km cross-track of CloudSat. Even though collocated with CloudSat, this subset can serve many other A-Train applications.\n\n(The shortname for this CloudSat-collocated subset of the original product OMSO2 Product is OMSO2_CPR_V003)\n            \nThis document describes the original OMI SO2 product (OMSO2) produced from global mode UV measurements of the Ozone Monitoring Instrument (OMI). OMI was launched on July 15, 2004 on the EOS Aura satellite, which is in a sun-synchronous ascending polar orbit with 1:45pm local equator crossing time. The data collection started on August 17, 2004 (orbit 482) and continues to this day with only minor data gaps. The minimum SO2 mass detectable by OMI is about two orders of magnitude smaller than the detection threshold of the legacy Total Ozone Mapping Spectrometer (TOMS) SO2 data (1978-2005) [Krueger et al 1995]. This is due to smaller OMI footprint and the use of wavelengths better optimized for separating O3 from SO2.\n\nThe product file, called a data granule, covers the sunlit portion of the orbit with an approximately 2600 km wide swath containing 60 pixels per viewing line. During normal operations, 14 or 15 granules are produced daily, providing fully contiguous coverage of the globe. Currently, OMSO2 products are not produced when OMI goes into the \"zoom mode\" for one day every 452 orbits (~32 days). For each OMI pixel we provide 4 different estimates of the column density of SO2 in Dobson Units (1DU=2.69x10^16 molecules/cm2) obtained by making different assumptions about the vertical distribution of the SO2. However, it is important to note that in most cases the precise vertical distribution of SO2 is unimportant. The users can use either the SO2 plume height, or the center of mass altitude (CMA) derived from SO2 vertical distribution, to interpolate between the 4 values: \n\n1)Planetary Boundary Layer (PBL) SO2 column (ColumnAmountSO2_PBL), corresponding to CMA of 0.9 km.\n2)Lower tropospheric SO2 column (ColumnAmountSO2_TRL), corresponding to CMA of 2.5 km.\n3)Middle tropospheric SO2 column, (ColumnAmountSO2_TRM), usually produced by volcanic degassing, corresponding to CMA of 7.5 km,  \n4)Upper tropospheric and Stratospheric SO2 column (ColumnAmountSO2_STL), usually produced by explosive volcanic eruption, corresponding to CMA of 17 km. \n\nThe accuracy and precision of the derived SO2 columns vary significantly with the SO2 CMA and column amount, observational geometry, and slant column ozone. OMI becomes more sensitive to SO2 above clouds and snow/ice, and less sensitive to SO2 below clouds. Preliminary error estimates are discussed below (see Data Quality Assessment). \n\nOMSO2 files are stored in EOS Hierarchical Data Format\n(HDF-EOS5). Each file contains data from the day lit portion of an\norbit (53 minutes). There are approximately 14 orbits per day. The\nmaximum file size for the OMSO2 data product is about 9 Mbytes.",
-            "editor": "GES DISC",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OMSO2_CPR",
-            "creator": "OMI Science Team",
-            "title": "OMI/Aura Level 2 Sulphur Dioxide (SO2) Trace Gas Column Data 1-Orbit Subset and Collocated Swath along CloudSat V003 (OMSO2_CPR) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMSO2_CPR_003.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1003183,86 +1003160,92 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMSO2_CPR_003.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMSO2_CPR_003.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://atrain.gesdisc.eosdis.nasa.gov/data/OMI/OMSO2_CPR.003/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://atrain.gesdisc.eosdis.nasa.gov/data/OMI/OMSO2_CPR.003/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithm/ATBD-OMI-04.pdf",
-                    "description": "OMI Algorithm Theoretical Basis Document",
                     "@type": "dcat:Distribution",
+                    "description": "OMI Algorithm Theoretical Basis Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithm/ATBD-OMI-04.pdf",
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
-                    "downloadURL": "https://so2.gsfc.nasa.gov/docs.html",
-                    "description": "Principal Investigator Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Principal Investigator Documentation",
+                    "downloadURL": "https://so2.gsfc.nasa.gov/docs.html",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 }
             ],
+            "editor": "GES DISC",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMSO2_CPR_003.png",
+            "identifier": "C1236350970-GES_DISC",
+            "issued": "2006-06-01",
+            "keyword": [
+                "atmospheric chemistry",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1236350970-GES_DISC.html",
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
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "OMSO2_CPR",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2006-06-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "ATDD",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OMI/Aura Level 2 Sulphur Dioxide (SO2) Trace Gas Column Data 1-Orbit Subset and Collocated Swath along CloudSat V003 (OMSO2_CPR) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1000000044-CDDIS.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GGL/CDDIS.",
-            "issued": "1999-11-18",
-            "temporal": "2000-01-01T00:00:00Z/2022-01-17T00:00:00Z",
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
-            "identifier": "C1000000044-CDDIS",
             "description": "Earth Orientation Parameters (EOPs) product derived from analysis of Very Long Baseline Interferometry (VLBI) data. These products are the generated by analysis centers in support of the International VLBI Service for Geodesy and Astrometry (IVS).",
-            "title": "CDDIS_VLBI_products_eop",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1003271,101 +1003254,132 @@
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1000000044-CDDIS",
+            "issued": "1999-11-18",
+            "keyword": [
+                "nasa"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1000000044-CDDIS.html",
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
+            "temporal": "2000-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "IVS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CDDIS_VLBI_products_eop"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-EXT3-67PCHURYUMOV-M35-V3.0",
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
+            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 3 mission phase, covering the period from 2016-09-26T06:40:00.000 to 2016-10-01T00:00:00.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Corrected START_TIME and STOP_TIME for BALLISTIC_STACKED images. Improved calibration of WAC balistic mode images.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-ext3-67pchuryumov-m35-v3.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-EXT3-67PCHURYUMOV-M35-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-ext3-67pchuryumov-m35-v3.0",
-            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 3 mission phase, covering the period from 2016-09-26T06:40:00.000 to 2016-10-01T00:00:00.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Corrected START_TIME and STOP_TIME for BALLISTIC_STACKED images. Improved calibration of WAC balistic mode images.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 3 EXT3-MTP035 RDR V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 3 EXT3-MTP035 RDR V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Avg1-crs-jup-avg-flux&version=1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This bundle contains derived data from the Cosmic Ray Subsystem (CRS), which was designed for cosmic ray studies.  It consists of two high Energy Telescopes (HET), four Low Energy Telescopes (LET) and The Electron Telescope (TET).",
+            "identifier": "urn:nasa:pds:vg1-crs-jup-avg-flux",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "voyager",
                 "io",
                 "jupiter"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Avg1-crs-jup-avg-flux&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:vg1-crs-jup-avg-flux",
-            "description": "This bundle contains derived data from the Cosmic Ray Subsystem (CRS), which was designed for cosmic ray studies.  It consists of two high Energy Telescopes (HET), four Low Energy Telescopes (LET) and The Electron Telescope (TET).",
-            "title": "Voyager 1 Jupiter CRS Derived Proton/Ion/Electron Flux Browse Data Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Voyager 1 Jupiter CRS Derived Proton/Ion/Electron Flux Browse Data Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TERRA/MISR/MIL2ASLS_L2.003-23",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 2 Land Surface Parameters;See ProductionDateTime for published Date.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "David Diner",
+                "hasEmail": "mailto:david.j.diner@jpl.nasa.gov"
+            },
+            "description": "This Level 2 Land Surface product contains directional reflectance properties,albedo(spectral & PAR integrated),FPAR, radiation parameters & terrain-referenced geometric parameters.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMISR%2FMIL2ASLS_L2.003-23",
+                    "mediaType": "text/html",
+                    "title": "Google Scholar search results"
+                }
+            ],
+            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
+            "identifier": "C1542384334-LARC",
             "issued": "2016-10-20",
-            "temporal": "2000-03-01T01:06:13Z/2022-05-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-26",
             "keyword": [
                 "land surface",
                 "surface radiative properties",
@@ -1003374,88 +1003388,47 @@
                 "earth science",
                 "land use/land cover"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "David Diner",
-                "hasEmail": "mailto:david.j.diner@jpl.nasa.gov"
-            },
+            "landingPage": "https://doi.org/10.5067/TERRA/MISR/MIL2ASLS_L2.003-23",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-04-26",
+            "programCode": [
+                "026:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "NASA/LARC/SD/ASDC"
             },
-            "identifier": "C1542384334-LARC",
-            "description": "This Level 2 Land Surface product contains directional reflectance properties,albedo(spectral & PAR integrated),FPAR, radiation parameters & terrain-referenced geometric parameters.",
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "title": "MISR Level 2 Surface parameters V003",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "programCode": [
-                "026:001"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMISR%2FMIL2ASLS_L2.003-23",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "@type": "dcat:Distribution",
-                    "title": "Google Scholar search results"
-                }
-            ],
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-03-01T01:06:13Z/2022-05-03T00:00:00Z",
             "theme": [
                 "MISR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR Level 2 Surface parameters V003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA2006",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Livesey, N. and Read, W.. 2015-02-19. ML2DGG. Version 004. MLS/Aura Level 2 Diagnostics, Geophysical Parameter Grid V004. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA2006. https://disc.gsfc.nasa.gov/datacollection/ML2DGG_004.html. Digital Science Data.",
-            "issued": "2015-02-19",
-            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-02-19",
-            "keyword": [
-                "atmospheric chemistry",
-                "microwave",
-                "earth science",
-                "clouds",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "atmosphere",
-                "spectral/engineering"
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
-            "identifier": "C1251101324-GES_DISC",
-            "description": "ML2DGG is the EOS Aura Microwave Limb Sounder (MLS) product containing geophysical diagnostic quantities pertaining directly to the standard geophysical data products, generally on a similar (or identical) grid, and at different spectral ranges. The data version is 4.2. Data coverage is from August 8, 2004 to current. Spatial coverage is near-global (-82 degrees to +82 degrees latitude), with each profile spaced 1.5 degrees or ~165 km along the orbit track (roughly 15 orbits per day). Vertical resolution varies between species and typically ranges from 3 - 6 km. Users of the ML2DGG data product should read the EOS MLS Level 2 Version 4 Quality Document for more information.\n\nThe data are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5), which is based on the version 5 Hierarchical Data Format, or HDF-5. Each file contain swaths objects for each diagnostics measurement. Each swath has a set of data and geolocation fields, swath attributes, and metadata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML2DGG",
             "creator": "Livesey, N. and Read, W.",
-            "title": "MLS/Aura Level 2 Diagnostics, Geophysical Parameter Grid V004 (ML2DGG) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2DGG_004.jpeg",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "ML2DGG is the EOS Aura Microwave Limb Sounder (MLS) product containing geophysical diagnostic quantities pertaining directly to the standard geophysical data products, generally on a similar (or identical) grid, and at different spectral ranges. The data version is 4.2. Data coverage is from August 8, 2004 to current. Spatial coverage is near-global (-82 degrees to +82 degrees latitude), with each profile spaced 1.5 degrees or ~165 km along the orbit track (roughly 15 orbits per day). Vertical resolution varies between species and typically ranges from 3 - 6 km. Users of the ML2DGG data product should read the EOS MLS Level 2 Version 4 Quality Document for more information.\n\nThe data are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5), which is based on the version 5 Hierarchical Data Format, or HDF-5. Each file contain swaths objects for each diagnostics measurement. Each swath has a set of data and geolocation fields, swath attributes, and metadata.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA2006",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA2006",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1003465,82 +1003438,123 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML2DGG_004.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML2DGG_004.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level2/ML2DGG.004/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level2/ML2DGG.004/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML2DGG_004",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML2DGG_004",
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
-                    "description": "MLS Science Team home page.",
                     "@type": "dcat:Distribution",
+                    "description": "MLS Science Team home page.",
+                    "downloadURL": "https://mls.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2DGG_004.jpeg",
+            "identifier": "C1251101324-GES_DISC",
+            "issued": "2015-02-19",
+            "keyword": [
+                "atmospheric chemistry",
+                "microwave",
+                "earth science",
+                "clouds",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "atmosphere",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA2006",
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
+            "series-name": "ML2DGG",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MLS/Aura Level 2 Diagnostics, Geophysical Parameter Grid V004 (ML2DGG) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220566340-USGS_LTA.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "EROS Long Term Archive. 1994-01-01. AVHRR 1-km Orbital Segments. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, U.S. Geological Survey. Remote Sensing Image.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EROS CENTER",
+                "hasEmail": "mailto:lta@usgs.gov"
+            },
+            "creator": "EROS Long Term Archive",
+            "data-presentation-form": "Remote Sensing Image",
+            "description": "The Advanced Very High Resolution Radiometer (AVHRR) 1-km Orbital\n       Segments data set is a component of the National Aeronautics and\n       Space Administration (NASA) AVHRR Pathfinder Program and contains\n       global coverage of land masses at 1-kilometer resolution.\n\n       The data set is the result of an international effort to acquire,\n       process, and distribute AVHRR data of the entire global land surface\n       to meet the needs of the international science community.  The \n       orbital segments are comprised of raw AVHRR scenes consisting of\n       5-channel, 10-bit, AVHRR data at 1.1-km resolution at nadir.  The raw\n       data are used to produce vegetation index composites; to support fire \n       detection and cloud screening activities; to support research in\n       atmospheric correction; to develop algorithms; and to support a host of\n       research activities that may require the inclusion of raw AVHRR data.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "\n         EarthExplorer is a complete search and order tool for aerial photos, elevation data and satellite products distributed by the USGS.\n      ",
+                    "downloadURL": "http://earthexplorer.usgs.gov",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                }
+            ],
+            "identifier": "C1220566340-USGS_LTA",
             "issued": "1992-04-01",
-            "temporal": "1992-04-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-03-25",
             "keyword": [
                 "land use/land cover",
                 "land surface",
@@ -1003549,1142 +1003563,1103 @@
                 "visible wavelengths",
                 "earth science"
             ],
-            "data-presentation-form": "Remote Sensing Image",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EROS CENTER",
-                "hasEmail": "mailto:lta@usgs.gov"
-            },
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220566340-USGS_LTA.html",
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
-            "identifier": "C1220566340-USGS_LTA",
-            "description": "The Advanced Very High Resolution Radiometer (AVHRR) 1-km Orbital\n       Segments data set is a component of the National Aeronautics and\n       Space Administration (NASA) AVHRR Pathfinder Program and contains\n       global coverage of land masses at 1-kilometer resolution.\n\n       The data set is the result of an international effort to acquire,\n       process, and distribute AVHRR data of the entire global land surface\n       to meet the needs of the international science community.  The \n       orbital segments are comprised of raw AVHRR scenes consisting of\n       5-channel, 10-bit, AVHRR data at 1.1-km resolution at nadir.  The raw\n       data are used to produce vegetation index composites; to support fire \n       detection and cloud screening activities; to support research in\n       atmospheric correction; to develop algorithms; and to support a host of\n       research activities that may require the inclusion of raw AVHRR data.",
             "release-place": "Sioux Falls, South Dakota, USA",
-            "creator": "EROS Long Term Archive",
-            "title": "AVHRR 1-km Orbital Segments",
-            "programCode": [
-                "026:001"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://earthexplorer.usgs.gov",
-                    "description": "\n         EarthExplorer is a complete search and order tool for aerial photos, elevation data and satellite products distributed by the USGS.\n      ",
-                    "@type": "dcat:Distribution",
-                    "title": "Download this dataset"
-                }
-            ],
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1992-04-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "AVHRR 1-KM PATHFINDER",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AVHRR 1-km Orbital Segments"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1363-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-23T09:19:45.000 to 2016-01-23T13:39:11.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1363-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1363-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1363-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-23T09:19:45.000 to 2016-01-23T13:39:11.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1363 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1363 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-SWAP-2-PLUTOCRUISE-V3.0",
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
+            "description": "This data set contains Raw data taken by the New Horizons                Solar Wind Around Pluto                                                instrument during the                                                    pluto cruise                                                           mission phase.  This is VERSION 3.0 of this data set.                    Per the original mission plan for cruise operations, the SWAP              instrument was off for the first 460+ days of Pluto Cruise.  After         that the operations were sporadic (just a few days in 2009) and            mostly Science, alternating with Channel Electron Multiplier gain          tests during Annual CheckOuts.  After extensive testing in early           2012, in July of that year the project approved daily science              operations for the SWAP and PEPSSI instruments throughout the rest         of the cruise to Pluto.                                                    The changes in Version 3.0 were re-running of the ancillary data         in the data product, updated geometry from newer SPICE kernels,          minor editing of the documentation, catalogs, etc., and resolution       of liens from the December, 2014 review, plus those from the May,        2016 review of the Pluto Encounter data sets.                            New observations added with this version (V3.0) include ongoing          cruise observations from August, 2014 through January, 2015.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-swap-2-plutocruise-v3.0_jzas-4wa4",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-SWAP-2-PLUTOCRUISE-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-swap-2-plutocruise-v3.0_jzas-4wa4",
-            "description": "This data set contains Raw data taken by the New Horizons                Solar Wind Around Pluto                                                instrument during the                                                    pluto cruise                                                           mission phase.  This is VERSION 3.0 of this data set.                    Per the original mission plan for cruise operations, the SWAP              instrument was off for the first 460+ days of Pluto Cruise.  After         that the operations were sporadic (just a few days in 2009) and            mostly Science, alternating with Channel Electron Multiplier gain          tests during Annual CheckOuts.  After extensive testing in early           2012, in July of that year the project approved daily science              operations for the SWAP and PEPSSI instruments throughout the rest         of the cruise to Pluto.                                                    The changes in Version 3.0 were re-running of the ancillary data         in the data product, updated geometry from newer SPICE kernels,          minor editing of the documentation, catalogs, etc., and resolution       of liens from the December, 2014 review, plus those from the May,        2016 review of the Pluto Encounter data sets.                            New observations added with this version (V3.0) include ongoing          cruise observations from August, 2014 through January, 2015.",
-            "title": "NEW HORIZONS                            \n      SWAP PLUTO CRUISE                                                       \n      RAW V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS                            \n      SWAP PLUTO CRUISE                                                       \n      RAW V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-DERIVED-LIGHTCURVE-V7.0",
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
+            "description": "This is a compilation of published lightcurve results through February, 2005.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-derived-lightcurve-v7.0_jzdt-cfyx",
+            "issued": "2021-05-21",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-DERIVED-LIGHTCURVE-V7.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-derived-lightcurve-v7.0_jzdt-cfyx",
-            "description": "This is a compilation of published lightcurve results through February, 2005.",
-            "title": "ASTEROID LIGHTCURVE DERIVED DATA V7.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ASTEROID LIGHTCURVE DERIVED DATA V7.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TERRA/CERES/CRS1DEGHOUR_L3.004A",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/TERRA/CERES/CRS1DEGHOUR_L3.004A. https://doi.org/10.5067/TERRA/CERES/CRS1DEGHOUR_L3.004A.",
-            "issued": "2024-01-08",
-            "temporal": "2018-01-01T00:00:00Z/2022-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-01-08",
-            "keyword": [
-                "clouds",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "atmospheric radiation",
-                "atmospheric pressure",
-                "atmosphere",
-                "aerosols",
-                "atmospheric winds",
-                "earth science"
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
-            "identifier": "C2842857656-LARC_ASDC",
             "description": "CER_CRS1deg-Hour_Terra-MODIS_Edition4A is the Terra Clouds and the Earth's Radiant Energy System (CERES) Level 3 computed flux Edition4A data product. The Cloud and Radiative Swath One Degree (CRS1deg) Hour provides data hourly on a 1-degree latitude and longitude global grid from the Terra CERES Flight Model 1 (FM1) or FM2 CER_CRS_Terra-FM1-MODIS_Edition4A instantaneous footprint data. The data provides instantaneous averages of computed top of atmosphere (ToA) (0.01-hPa), within the atmosphere (850-, 500-, 200-, and 70-hPa), and surface fluxes (Wm-2). Four assumptions are used in the Fu-Liou radiative transfer model (RTM): Total-sky, clear-sky (no clouds, but aerosol), pristine (no clouds or aerosols), and total-sky, no aerosol as described in Scott 2022. Variables from these footprints are then assigned to a grid box and linearly averaged.\r\n\r\nThe data has been processed from January 1, 2018, to December 31, 2022, and is available in daily netCDF4 files. This single satellite product uses the primary CERES instrument in cross-track mode. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels: total, shortwave, and window. Longwave fluxes are obtained by subtracting shortwave from the total.\r\n \r\nA few variables from the SSF have been included in this product, such as observed CERES shortwave and longwave ToA fluxes and cloud fraction. MODIS measurements are not directly used in this dataset. The MODIS data is used during SSF processing to obtain cloud properties. These cloud properties are then used to compute the CRS fluxes.\r\nStill, this product should be used in conjunction with the CER_SSF1deg-Hour_Terra-MODIS_Edition4A product, which has additional cloud and aerosol properties. The CER_SYN1deg-1Hour_Terra-Aqua-MODIS_Edition4A is another related product that averages the cloud properties to the one-degree grid before performing the Fu-Liou RTM calculations. The SYN1deg-1Hour product also brings in cloud properties derived from geostationary imagers between 60 N and 60 S to provide information to provide a complete diurnal cycle.",
-            "graphic-preview-description": "Mission Logo",
-            "title": "CERES Regionally Averaged Computed TOA, within the Atmosphere, and Surface Fluxes Hourly Terra Edition4A",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/ceres.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FCERES%2FCRS1DEGHOUR_L3.004A",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FCERES%2FCRS1DEGHOUR_L3.004A",
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
-                    "downloadURL": "https://doi.org/10.5067/TERRA/CERES/CRS1DEGHOUR_L3.004A",
-                    "description": "DOI data set landing page for CER_SSF1deg-Hour_Terra-MODIS_Edition4A",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CER_SSF1deg-Hour_Terra-MODIS_Edition4A",
+                    "downloadURL": "https://doi.org/10.5067/TERRA/CERES/CRS1DEGHOUR_L3.004A",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2842857656-LARC_ASDC",
-                    "description": "Earthdata Search for CER_CRS1deg-Hour_Terra-MODIS_Edition4A (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CER_CRS1deg-Hour_Terra-MODIS_Edition4A (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2842857656-LARC_ASDC",
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
-                    "downloadURL": "https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_CRS1deg_Ed4A_DQS.pdf",
-                    "description": "Quality Summary: CERES_CRS1deg-Hour_Ed4A (1/31/2024)",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Summary: CERES_CRS1deg-Hour_Ed4A (1/31/2024)",
+                    "downloadURL": "https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_CRS1deg_Ed4A_DQS.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's data quality document"
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
-                    "downloadURL": "https://terra.nasa.gov/?section=60",
-                    "description": "TERRA Overview",
                     "@type": "dcat:Distribution",
+                    "description": "TERRA Overview",
+                    "downloadURL": "https://terra.nasa.gov/?section=60",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/guide/cer_crs1deg-hour.pdf",
-                    "description": "CERES Hourly Gridded Computed TOA, withiin the Atmosphere, and Surface (CRS1deg-Hour) Data Set Abstract",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Hourly Gridded Computed TOA, withiin the Atmosphere, and Surface (CRS1deg-Hour) Data Set Abstract",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/guide/cer_crs1deg-hour.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/DPC_CRS1deg_R4V1.pdf",
-                    "description": "CERES Data Products Catalog R4V110/1/2004 Clouds and Radiative Swath One-Degree",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Data Products Catalog R4V110/1/2004 Clouds and Radiative Swath One-Degree",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/DPC_CRS1deg_R4V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/readme_cer_ssf_SampleRead_R3-358.txt",
-                    "description": "Sample read software for CERES SSF Data Products",
                     "@type": "dcat:Distribution",
+                    "description": "Sample read software for CERES SSF Data Products",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/readme_cer_ssf_SampleRead_R3-358.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/coastal_water.pdf",
-                    "description": "Discussion of the Coastal Water Percentage Issue",
                     "@type": "dcat:Distribution",
+                    "description": "Discussion of the Coastal Water Percentage Issue",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/coastal_water.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's documented anomalies"
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
-                    "downloadURL": "https://ceres.larc.nasa.gov/data/#crs1deg-level-3",
-                    "description": "CERES Data Page",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Data Page",
+                    "downloadURL": "https://ceres.larc.nasa.gov/data/#crs1deg-level-3",
+                    "mediaType": "text/html",
                     "title": "Subset this dataset using a web based subsetter"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ceres-tool.larc.nasa.gov/ord-tool/jsp/CRS1degHourEd41Selection.jsp",
-                    "description": "CERES Ordering Tool",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Ordering Tool",
+                    "downloadURL": "https://ceres-tool.larc.nasa.gov/ord-tool/jsp/CRS1degHourEd41Selection.jsp",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through the CERES Ordering Tool"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/CRS/Terra-MODIS_Edition4A/",
-                    "description": "ASDC Direct Data Download for CER_CRS1deg-Hour_Terra-MODIS_Edition4A",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CER_CRS1deg-Hour_Terra-MODIS_Edition4A",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/CRS/Terra-MODIS_Edition4A/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/CRS/Terra-MODIS_Edition4A/contents.html",
-                    "description": "OPeNDAP data access for CER_CRS1deg-Hour_Terra-MODIS_Edition4A",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CER_CRS1deg-Hour_Terra-MODIS_Edition4A",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/CRS/Terra-MODIS_Edition4A/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Mission Logo",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/ceres.png",
+            "identifier": "C2842857656-LARC_ASDC",
+            "issued": "2024-01-08",
+            "keyword": [
+                "clouds",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "atmospheric radiation",
+                "atmospheric pressure",
+                "atmosphere",
+                "aerosols",
+                "atmospheric winds",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/TERRA/CERES/CRS1DEGHOUR_L3.004A",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-01-08",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2018-01-01T00:00:00Z/2022-12-31T23:59:59Z",
             "theme": [
                 "CERES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CERES Regionally Averaged Computed TOA, within the Atmosphere, and Surface Fluxes Hourly Terra Edition4A"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-MASTCAM-2-EDR-VID-V1.0",
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
-                "mars science laboratory",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "NULL",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-mastcam-2-edr-vid-v1.0_jzi5-8pfj",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars science laboratory",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-MASTCAM-2-EDR-VID-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-mastcam-2-edr-vid-v1.0_jzi5-8pfj",
-            "description": "NULL",
-            "title": "MSL MARS MAST CAMERA 2\n                                      EDR VIDEO V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MSL MARS MAST CAMERA 2\n                                      EDR VIDEO V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Suborbital/OWLETS-2/SurfaceLidar_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2021-01-27. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/Suborbital/OWLETS-2/SurfaceLidar_Data_1.",
-            "issued": "2020-11-18",
-            "temporal": "2018-05-23T00:00:00Z/2018-11-13T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-20",
-            "keyword": [
-                "atmospheric chemistry",
-                "atmospheric winds",
-                "earth science",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Sullivan",
                 "hasEmail": "mailto:john.t.sullivan@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1997469946-LARC_ASDC",
             "description": "OWLETS2_SurfaceLidar_Data_1 is the Ozone Water-Land Environmental Transition Study (OWLETS-2) NASA GSFC TROPOZ, NASA LMOL, and wind lidar data collected at Hart Miller Island site and UMBC site during the OWLETS-2 field campaign. OWLETS was supported by the NASA Science Innovation Fund (SIF). Data collection is complete.\r\n\r\nCoastal regions have typically posed a challenge for air quality researchers due to a lack of measurements available over water and water-land boundary transitions. Supported by NASA\u2019s Science Innovation Fund (SIF), the Ozone Water-Land Environmental Transition Study (OWLETS) field campaign examined ozone concentrations and gradients over the Chesapeake Bay from July 5, 2017 \u2013 August 3, 2017, with twelve intensive measurement days occurring during this time period. OWLETS utilized a unique combination of instrumentation, including aircraft, TOLNet ozone lidars (NASA Goddard Space Flight Center Tropospheric Ozone Differential Absorption Lidar and NASA Langley Research Center Mobile Ozone Lidar), UAV/drones, ozonesondes, AERONET sun photometers, and mobile and ship-based measurements, to characterize the land-water differences in ozone and other pollutants. Two main research sites were established as part of the campaign: an over-land site at NASA LaRC, and an over-water site at the Chesapeake Bay Bridge Tunnel. These two research sites were established to provide synchronous vertical measurements of meteorology and pollutants over water and over land. In combination with mobile observations between the two sites, pollutant gradients were able to be observed and used to better understand the fundamental processes occurring at the land-water interface. OWLETS-2 was completed from June 6, 2018 \u2013 July 6, 2018 in the upper Chesapeake Bay region. Research sites were established at the University of Maryland, Baltimore County (UMBC), Hart Miller Island (HMI), and Howard University Beltsville (HUBV), with HMI representing the over-water location and UMBC and HUBV representing the over-land sites. Similar measurements were carried out to further characterize water-land gradients in the upper Chesapeake Bay. The measurements completed during OWLETS are of importance in enhancing air quality models, and improving future satellite retrievals, particularly, NASA\u2019s Tropospheric Emissions: Monitoring of Pollution, which is scheduled to launch in 2022.",
-            "title": "OWLETS-2 Surface Lidar Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSuborbital%2FOWLETS-2%2FSurfaceLidar_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSuborbital%2FOWLETS-2%2FSurfaceLidar_Data_1",
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
-                    "downloadURL": "https://doi.org/10.5067/Suborbital/OWLETS-2/SurfaceLidar_Data_1",
-                    "description": "DOI data set landing page for OWLETS2_SurfaceLidar_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for OWLETS2_SurfaceLidar_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/Suborbital/OWLETS-2/SurfaceLidar_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1997469946-LARC_ASDC",
-                    "description": "Earthdata Search for OWLETS2_SurfaceLidar_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for OWLETS2_SurfaceLidar_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1997469946-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/OWLETS/2_SurfaceLidar_Data_1/",
-                    "description": "ASDC Direct Data Download for OWLETS2_SurfaceLidar_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for OWLETS2_SurfaceLidar_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/OWLETS/2_SurfaceLidar_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/OWLETS/2_SurfaceLidar_Data_1/contents.html",
-                    "description": "OPeNDAP data access for OWLETS2_SurfaceLidar_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for OWLETS2_SurfaceLidar_Data_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/OWLETS/2_SurfaceLidar_Data_1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1997469946-LARC_ASDC",
+            "issued": "2020-11-18",
+            "keyword": [
+                "atmospheric chemistry",
+                "atmospheric winds",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/Suborbital/OWLETS-2/SurfaceLidar_Data_1",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>36.0 -78.0 36.0 -75.0 41.0 -75.0 41.0 -78.0 36.0 -78.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2018-05-23T00:00:00Z/2018-11-13T23:59:59.999Z",
             "theme": [
                 "OWLETS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OWLETS-2 Surface Lidar Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSINAC-3-CR4B-CRUISE4B-V1.4",
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
+            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera\nduring the CRUISE 4-2 mission phase",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osinac-3-cr4b-cruise4b-v1.4",
+            "issued": "2021-05-21",
+            "keyword": [
+                "calibration",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSINAC-3-CR4B-CRUISE4B-V1.4",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osinac-3-cr4b-cruise4b-v1.4",
-            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera\nduring the CRUISE 4-2 mission phase",
-            "title": "ROSETTA-ORBITER CRUISE 4-2 OSINAC 3 RDR data",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CRUISE 4-2 OSINAC 3 RDR data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1615929578-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, OB.DAAC.",
-            "issued": "2019-06-23",
-            "temporal": "2002-07-04T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-10-01",
-            "keyword": [
-                "earth science",
-                "oceans",
-                "ocean temperature",
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
-                "name": "OB.DAAC"
-            },
-            "identifier": "C1615929578-OB_DAAC",
             "description": "MODIS (or Moderate Resolution Imaging Spectroradiometer) is a key instrument aboard the Terra (EOS AM) and Aqua (EOS PM) satellites. Terra's orbit around the Earth is timed so that it passes from north to south across the equator in the morning, while Aqua passes south to north over the equator in the afternoon. Terra MODIS and Aqua MODIS are viewing the entire Earth's surface every 1 to 2 days, acquiring data in 36 spectral bands, or groups of wavelengths (see MODIS Technical Specifications). These data will improve our understanding of global dynamics and processes occurring on the land, in the oceans, and in the lower atmosphere. MODIS is playing a vital role in the development of validated, global, interactive Earth system models able to predict global change accurately enough to assist policy makers in making sound decisions concerning the protection of our environment.",
-            "title": "Aqua MODIS Global Mapped 4\u00b5m Nighttime Sea Surface Temperature (SST4) Data, version R2019.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directaccess/MODIS-Aqua/L3SMI/",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directaccess/MODIS-Aqua/L3SMI/",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/AQUA/MODIS/L3M/SST4/R2019.0",
-                    "description": "MODIS-Aqua L3M 4\u00b5m Nighttime Sea Surface Temperature (SST4) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS-Aqua L3M 4\u00b5m Nighttime Sea Surface Temperature (SST4) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/AQUA/MODIS/L3M/SST4/R2019.0",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/MODISA/L3SMI/",
-                    "description": "OB.DAAC OPeNDAP Site for Aqua MODIS Standard Mapped Image (SMI) Product",
                     "@type": "dcat:Distribution",
+                    "description": "OB.DAAC OPeNDAP Site for Aqua MODIS Standard Mapped Image (SMI) Product",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/MODISA/L3SMI/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1615929578-OB_DAAC",
+            "issued": "2019-06-23",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "ocean temperature",
+                "ngda",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1615929578-OB_DAAC.html",
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
+            "title": "Aqua MODIS Global Mapped 4\u00b5m Nighttime Sea Surface Temperature (SST4) Data, version R2019.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SMODE-MASS1V",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Luc Lenain and Nick Statom. 2022-12-01. S-MODE MASS Level 1 Visible Imagery Version 1. Version 1. S-MODE MASS Level 1 Visible Imagery Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, S-MODE Project Data Manager, Fred Bingham. https://doi.org/10.5067/SMODE-MASS1V. http://podaac.jpl.nasa.gov/SMODE.",
-            "issued": "2021-10-22",
-            "temporal": "2021-10-22T19:00:00Z/2023-05-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-27",
-            "keyword": [
-                "earth science",
-                "spectral/engineering",
-                "visible wavelengths"
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
-            "identifier": "C2431654574-POCLOUD",
-            "description": "This dataset contains airborne visible imagery from the Sub-Mesoscale Ocean Dynamics Experiment (S-MODE) during a pilot campaign conducted approximately 300 km offshore of San Francisco over two weeks in October 2021.  S-MODE aims to understand how ocean dynamics acting on short spatial scales influence the vertical exchange of physical and biological variables in the ocean. The Modular Aerial Sensing System (MASS) is an airborne instrument package that is mounted on the DHC-6 Twin Otter aircraft which flies long duration detailed surveys of the field domain during deployments. MASS includes an IO Industries Flare 12M125-CL camera with 14mm lens mounted nadir in the aircraft in an orientation so that the short edge of the image was parallel with the aircraft heading. The camera was synchronized to a coupled GPS/IMU system with images taken at 5hz. Raw images were calibrated for lens distortion and boresight misalignment with the GPS/IMU. Images were georeferenced to the post-processed aircraft trajectory and exported with reference to WGS84 datum with a UTM zone 10 projection (EPSG 32610) at an altitude-dependent spatial resolution. Level 1 images are available in TIFF format.",
-            "series-name": "S-MODE MASS Level 1 Visible Imagery Version 1",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Luc Lenain and Nick Statom",
-            "title": "S-MODE MASS Level 1 Visible Imagery Version 1",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SMODE_L1_MASS_DOPVISIBLE_V1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset contains airborne visible imagery from the Sub-Mesoscale Ocean Dynamics Experiment (S-MODE) during a pilot campaign conducted approximately 300 km offshore of San Francisco over two weeks in October 2021.  S-MODE aims to understand how ocean dynamics acting on short spatial scales influence the vertical exchange of physical and biological variables in the ocean. The Modular Aerial Sensing System (MASS) is an airborne instrument package that is mounted on the DHC-6 Twin Otter aircraft which flies long duration detailed surveys of the field domain during deployments. MASS includes an IO Industries Flare 12M125-CL camera with 14mm lens mounted nadir in the aircraft in an orientation so that the short edge of the image was parallel with the aircraft heading. The camera was synchronized to a coupled GPS/IMU system with images taken at 5hz. Raw images were calibrated for lens distortion and boresight misalignment with the GPS/IMU. Images were georeferenced to the post-processed aircraft trajectory and exported with reference to WGS84 datum with a UTM zone 10 projection (EPSG 32610) at an altitude-dependent spatial resolution. Level 1 images are available in TIFF format.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSMODE-MASS1V",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSMODE-MASS1V",
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
-                    "downloadURL": "http://podaac.jpl.nasa.gov/smode",
-                    "description": "Field Campaign and Instrument Overview for S-MODE",
                     "@type": "dcat:Distribution",
+                    "description": "Field Campaign and Instrument Overview for S-MODE",
+                    "downloadURL": "http://podaac.jpl.nasa.gov/smode",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SMODE_L1_MASS_DOPVISIBLE_V1.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SMODE_L1_MASS_DOPVISIBLE_V1.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2431654574-POCLOUD",
-                    "description": "Browse and download granules over HTTPS using the virtual directories",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2431654574-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2431654574-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2431654574-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/dataset/SMODE_L1_MASS_VISIBLE_V1",
-                    "description": "S-MODE MASS Level 1 Visible Imagery Version 1",
                     "@type": "dcat:Distribution",
+                    "description": "S-MODE MASS Level 1 Visible Imagery Version 1",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/dataset/SMODE_L1_MASS_VISIBLE_V1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
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
-                    "description": "2022 Open Data Workshop Presentations and Recordings",
                     "@type": "dcat:Distribution",
+                    "description": "2022 Open Data Workshop Presentations and Recordings",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SMODE_L1_MASS_DOPVISIBLE_V1.jpg",
+            "identifier": "C2431654574-POCLOUD",
+            "issued": "2021-10-22",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/SMODE-MASS1V",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-04-27",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "series-name": "S-MODE MASS Level 1 Visible Imagery Version 1",
             "spatial": "-125.4 36.3 -122.9 38.1",
+            "temporal": "2021-10-22T19:00:00Z/2023-05-31T00:00:00Z",
             "theme": [
                 "S-MODE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "S-MODE MASS Level 1 Visible Imagery Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-3-TNO-CEN-COLOR-V5.0",
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
+            "description": "This data set is intended to include published broadband colors of centaurs and Transneptunian Objects (TNOs) published through December 2007. It supersedes all versions of the TNO colors data set EAR-A-3-RDR-TNO-PHOT.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-3-tno-cen-color-v5.0_jznq-4wmr",
+            "issued": "2021-05-21",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-3-TNO-CEN-COLOR-V5.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-3-tno-cen-color-v5.0_jznq-4wmr",
-            "description": "This data set is intended to include published broadband colors of centaurs and Transneptunian Objects (TNOs) published through December 2007. It supersedes all versions of the TNO colors data set EAR-A-3-RDR-TNO-PHOT.",
-            "title": "TNO AND CENTAUR COLORS V5.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "TNO AND CENTAUR COLORS V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL3HDOD.006",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AURA/TES/TL3HDOD.006. https://asdc.larc.nasa.gov/project/TES.",
-            "issued": "2019-02-27",
-            "temporal": "2004-09-03T00:00:00Z/2018-01-22T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "atmospheric temperature",
-                "atmospheric pressure",
-                "atmospheric chemistry"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "SCOTT GLUCK",
                 "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1629265632-LARC",
             "description": "TL3HDOD_6 is the Tropospheric Emission Spectrometer (TES)/Aura Level 3 (L3) 3 Deuterium Oxide Daily Gridded Version 6 data product. It consists of daily atmospheric temperature and volume mixing ratio (VMR) for the deuterium oxide atmospheric species, which are provided at 2 degree latitude by 4 degree longitude spatial grids and at a subset of TES standard pressure levels. TES was an instrument aboard NASA's Aura satellite and was launched from California on July 15, 2004. Data collection for TES is complete. \r\rThe TES Science Data Processing L3 subsystem interpolated L2 atmospheric profiles collected in a Global Survey onto a global grid uniform in latitude and longitude to provide a 3-D representation of the distribution of atmospheric gasses. The L3 standard data products are composed of L3 HDF-EOS grid data. A separate product file was produced for each different atmospheric species. TES obtained data in two basic observation modes: Limb or Nadir; Nadir observations, which point directly to the surface of the Earth, are different from limb observations, which are pointed at various off-nadir angles into the atmosphere. The product file may contain, in separate folders, limb data, nadir data, or both folders may be present. Specific to L3 processing were the terms Daily and Monthly representing the approximate time coverage of the L3 products. However, the input data granules to the L3 process are complete Global Surveys; in other words a Global Survey was not split in relation to time when input to the L3 processes even if they exceed the usual understood meanings of a day or month. More specifically, Daily L3 products represented a single Global Survey (approximately 26 hours) and Monthly L3 products represent Global Surveys that are initiated within that calendar month. The data granules defined for L3 standard products were daily and monthly.",
-            "title": "TES/Aura L3 Deuterium Oxide Daily Gridded V006",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL3HDOD.006",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL3HDOD.006",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/README_L3ReadSoftwareV1.txt",
-                    "description": "Basic IDL Tools for extracting information from TES L3 HDF Product files",
                     "@type": "dcat:Distribution",
+                    "description": "Basic IDL Tools for extracting information from TES L3 HDF Product files",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/README_L3ReadSoftwareV1.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
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
-                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL3HDOD.006",
-                    "description": "DOI data set landing page for TL3HDOD_6",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TL3HDOD_6",
+                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL3HDOD.006",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL3HDOD.006/contents.html",
-                    "description": "OPeNDAP data access for TL3HDOD_6",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for TL3HDOD_6",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL3HDOD.006/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1629265632-LARC",
-                    "description": "Earthdata Search for TL3HDOD_6 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TL3HDOD_6 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1629265632-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL3HDOD.006/",
-                    "description": "ASDC Direct Data Download for TL3HDOD_6",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for TL3HDOD_6",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL3HDOD.006/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1629265632-LARC",
+            "issued": "2019-02-27",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric temperature",
+                "atmospheric pressure",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TL3HDOD.006",
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
+            "temporal": "2004-09-03T00:00:00Z/2018-01-22T23:59:59Z",
             "theme": [
                 "TES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TES/Aura L3 Deuterium Oxide Daily Gridded V006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SENTINEL5P/S5P_L1B_IR_SIR.1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Copernicus Sentinel data processed by ESA, Koninklijk Nederlands Meteorologisch Instituut (KNMI). 2018-08-23. S5P_L1B_IR_SIR. Version 1. Sentinel-5P TROPOMI L1B Irradiance product SWIR module. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/SENTINEL5P/S5P_L1B_IR_SIR.1. https://disc.gsfc.nasa.gov/datacollection/S5P_L1B_IR_SIR_1.html. Digital Science Data.",
-            "issued": "2014-12-09",
-            "temporal": "2018-04-30T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2014-12-09",
-            "keyword": [
-                "platform characteristics",
-                "atmospheric radiation",
-                "earth science",
-                "atmosphere",
-                "spectral/engineering",
-                "sensor characteristics"
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
-            "identifier": "C1442068494-GES_DISC",
-            "description": "The Copernicus Sentinel-5 Precursor (Sentinel-5P or S5P) satellite mission is one of the European Space Agency's (ESA) new mission family - Sentinels, and it is a joint initiative between the Kingdom of the Netherlands and the ESA. The sole payload on Sentinel-5P is the TROPOspheric Monitoring Instrument (TROPOMI), which is a nadir-viewing 108 degree Field-of-View push-broom grating hyperspectral spectrometer, covering the wavelength of ultraviolet-visible (UV-VIS, 270nm to 495nm), near infrared (NIR, 675nm to 775nm), and shortwave infrared (SWIR, 2305nm-2385nm).\nTROPOMI Level-1B (L1B) product is generated by the Koninklijk Nederlands Meteoroligisch Instituut (KNMI) TROPOMI L01B processor from Level-0 input data and auxiliary data products with the netCDF-4 enhanced model. It provides users with radiance, irradiance, calibration and engineering products.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "S5P_L1B_IR_SIR",
             "creator": "Copernicus Sentinel data processed by ESA, Koninklijk Nederlands Meteorologisch Instituut (KNMI)",
-            "title": "Sentinel-5P TROPOMI Irradiance product SWIR module L1B V1 (S5P_L1B_IR_SIR) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/S5P_OFFL_L1B_IR_SIR_1.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The Copernicus Sentinel-5 Precursor (Sentinel-5P or S5P) satellite mission is one of the European Space Agency's (ESA) new mission family - Sentinels, and it is a joint initiative between the Kingdom of the Netherlands and the ESA. The sole payload on Sentinel-5P is the TROPOspheric Monitoring Instrument (TROPOMI), which is a nadir-viewing 108 degree Field-of-View push-broom grating hyperspectral spectrometer, covering the wavelength of ultraviolet-visible (UV-VIS, 270nm to 495nm), near infrared (NIR, 675nm to 775nm), and shortwave infrared (SWIR, 2305nm-2385nm).\nTROPOMI Level-1B (L1B) product is generated by the Koninklijk Nederlands Meteoroligisch Instituut (KNMI) TROPOMI L01B processor from Level-0 input data and auxiliary data products with the netCDF-4 enhanced model. It provides users with radiance, irradiance, calibration and engineering products.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSENTINEL5P%2FS5P_L1B_IR_SIR.1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSENTINEL5P%2FS5P_L1B_IR_SIR.1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1004694,108 +1004669,115 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/S5P_L1B_IR_SIR_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/S5P_L1B_IR_SIR_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/opendap/S5P_TROPOMI_Level1B/S5P_L1B_IR_SIR.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/opendap/S5P_TROPOMI_Level1B/S5P_L1B_IR_SIR.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/data/S5P_TROPOMI_Level1B/S5P_L1B_IR_SIR.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/data/S5P_TROPOMI_Level1B/S5P_L1B_IR_SIR.1/",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=S5P_L1B_IR_SIR_1",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=S5P_L1B_IR_SIR_1",
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
-                    "description": "Description of S5P TROPOMI data collection sequences ",
                     "@type": "dcat:Distribution",
+                    "description": "Description of S5P TROPOMI data collection sequences ",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/glossary?title=Sentinel-5P",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product history"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/S5P_OFFL_L1B_IR_SIR_1.png",
+            "identifier": "C1442068494-GES_DISC",
+            "issued": "2014-12-09",
+            "keyword": [
+                "platform characteristics",
+                "atmospheric radiation",
+                "earth science",
+                "atmosphere",
+                "spectral/engineering",
+                "sensor characteristics"
+            ],
+            "landingPage": "https://doi.org/10.5067/SENTINEL5P/S5P_L1B_IR_SIR.1",
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
+            "series-name": "S5P_L1B_IR_SIR",
+            "temporal": "2018-04-30T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Sentinel-5P",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sentinel-5P TROPOMI Irradiance product SWIR module L1B V1 (S5P_L1B_IR_SIR) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/jzqf-aees",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "temporal": "1977-01-01/1996-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "wise",
-                "geography",
-                "space science",
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
-            "identifier": "NASA-0000037__3",
+            "describedBy": "http://www.lpi.usra.edu/resources/gc/gcreadme.html",
             "description": "Planetary nomenclature, like terrestrial nomenclature, is used to uniquely identify a feature on the surface of a planet or satellite so that the feature can be easily located, described, and discussed. This gazetteer contains detailed information about all names of topographic and albedo features on planets and satellites (and some planetary ring and ring-gap systems) that the International Astronomical Union (IAU) has named and approved from its founding in 1919 through the present time.",
-            "title": "Gateway to Astronaut Photography of Earth",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1004803,385 +1004785,415 @@
                     "mediaType": "text/html"
                 }
             ],
-            "describedBy": "http://www.lpi.usra.edu/resources/gc/gcreadme.html",
-            "accrualPeriodicity": "irregular"
+            "identifier": "NASA-0000037__3",
+            "issued": "2018-06-25",
+            "keyword": [
+                "wise",
+                "geography",
+                "space science",
+                "nen"
+            ],
+            "landingPage": "https://data.nasa.gov/d/jzqf-aees",
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-SSI-2-EDR-V1.0",
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
+            "description": "The Surface Stereo Imager (SSI) experiment on the Mars Phoenix Lander consists of one instrument component plus command electronics. This SSI Imaging Operations EDR data set contains raw data from the Surface Stereo Imager (SSI).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-ssi-2-edr-v1.0_jzqw-jysh",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "phoenix"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-SSI-2-EDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-ssi-2-edr-v1.0_jzqw-jysh",
-            "description": "The Surface Stereo Imager (SSI) experiment on the Mars Phoenix Lander consists of one instrument component plus command electronics. This SSI Imaging Operations EDR data set contains raw data from the Surface Stereo Imager (SSI).",
-            "title": "PHOENIX MARS SURFACE STEREO IMAGER 2 EDR VERSION 1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "PHOENIX MARS SURFACE STEREO IMAGER 2 EDR VERSION 1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-ALICE-3-CR1-V1.0",
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
-                "unknown"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains CODMAC level 3 instrument checkout data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the first cruise phase of the Rosetta mission, which occurred 2004-06-07 to 2004-09-05.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-alice-3-cr1-v1.0_jzsm-84at",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international rosetta mission",
+                "unknown"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-ALICE-3-CR1-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-alice-3-cr1-v1.0_jzsm-84at",
-            "description": "This data set contains CODMAC level 3 instrument checkout data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the first cruise phase of the Rosetta mission, which occurred 2004-06-07 to 2004-09-05.",
-            "title": "ROSETTA-ORBITER CHECK ALICE 3 CR1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER CHECK ALICE 3 CR1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1552",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Goncalves, F.G., R.N. Treuhaft, J.R. Dos santos, P. Graca, A. Almeida, and B.E. Law. 2018. Tree Inventory and Biometry Measurements, Tapajos National Forest, Para, Brazil, 2010. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1552",
-            "issued": "2018-02-22",
-            "temporal": "2010-08-31T00:00:00Z/2010-09-16T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-11",
-            "keyword": [
-                "earth science",
-                "vegetation",
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
-            "identifier": "C2764883885-ORNL_CLOUD",
             "description": "This dataset provides tree inventory, tree height, diameter at breast height (DBH), and estimated crown measurements from 30 plots located in the Tapajos National Forest, Para, Brazil collected in September 2010. The plots were located in primary forest, primary forest subject to reduced-impact selective logging (PFL) between 1999 and 2003, and secondary forest (SF) with different age and disturbance histories. Plots were centered on GLAS (the Geoscience Laser Altimeter System) LiDAR instrument footprints selected along two sensor acquisition tracks spanning a wide range in vertical structure and aboveground biomass.",
-            "graphic-preview-description": "Geographical location of the Tapajos National Forest, PA, Brazil, outlined in yellow. The gray lines are GLAS tracks from 2003 to 2009 and the blue circles are the plots sampled. The pictures on the right illustrate three of the stands where plots were located (Goncalves et al., 2017).",
-            "title": "Tree Inventory and Biometry Measurements, Tapajos National Forest, Para, Brazil, 2010",
-            "graphic-preview-file": "https://daac.ornl.gov/VEGETATION/guides/Forest_Inventory_Tapajos_Fig1.PNG",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1552",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1552",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/Forest_Inventory_Tapajos/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/Forest_Inventory_Tapajos/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/Forest_Inventory_Tapajos.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/Forest_Inventory_Tapajos.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1552",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1552",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/vnd.google-earth.kmz",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/Forest_Inventory_Tapajos/comp/forest_inventory_tapajos.kmz",
-                    "description": "A kmz file with the study plot locations in the Tapajos National Forest, Para, Brazil",
                     "@type": "dcat:Distribution",
+                    "description": "A kmz file with the study plot locations in the Tapajos National Forest, Para, Brazil",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/Forest_Inventory_Tapajos/comp/forest_inventory_tapajos.kmz",
+                    "mediaType": "application/vnd.google-earth.kmz",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/Forest_Inventory_Tapajos/comp/Forest_Inventory_Tapajos.pdf",
-                    "description": "A PDF of the guide document",
                     "@type": "dcat:Distribution",
+                    "description": "A PDF of the guide document",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/Forest_Inventory_Tapajos/comp/Forest_Inventory_Tapajos.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/Forest_Inventory_Tapajos_Fig1.PNG",
-                    "description": "Geographical location of the Tapajos National Forest, PA, Brazil, outlined in yellow. The gray lines are GLAS tracks from 2003 to 2009 and the blue circles are the plots sampled. The pictures on the right illustrate three of the stands where plots were located (Goncalves et al., 2017).",
                     "@type": "dcat:Distribution",
+                    "description": "Geographical location of the Tapajos National Forest, PA, Brazil, outlined in yellow. The gray lines are GLAS tracks from 2003 to 2009 and the blue circles are the plots sampled. The pictures on the right illustrate three of the stands where plots were located (Goncalves et al., 2017).",
+                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/Forest_Inventory_Tapajos_Fig1.PNG",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Geographical location of the Tapajos National Forest, PA, Brazil, outlined in yellow. The gray lines are GLAS tracks from 2003 to 2009 and the blue circles are the plots sampled. The pictures on the right illustrate three of the stands where plots were located (Goncalves et al., 2017).",
+            "graphic-preview-file": "https://daac.ornl.gov/VEGETATION/guides/Forest_Inventory_Tapajos_Fig1.PNG",
+            "identifier": "C2764883885-ORNL_CLOUD",
+            "issued": "2018-02-22",
+            "keyword": [
+                "earth science",
+                "vegetation",
+                "biosphere",
+                "ecosystems"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1552",
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
             "spatial": "-54.99 -3.15 -54.95 -2.86",
+            "temporal": "2010-08-31T00:00:00Z/2010-09-16T23:59:59Z",
             "theme": [
                 "Vegetation",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Tree Inventory and Biometry Measurements, Tapajos National Forest, Para, Brazil, 2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/PRESW-BSJ10",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Menemenlis, D., Hill, C., Henze, C. E., Wang, J., & Fenty, I.. 2021-02-10. Bass Strait Pre-SWOT Level-4 Hourly MITgcm LLC4320 Native Grid 2km Oceanographic Dataset Version 1.0. Version 1.0. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/PRESW-BSJ10. Menemenlis, D., Hill, C., Henze, C. E., Wang, J., & Fenty, I. 2021. Bass Strait Pre-SWOT Level-4 Hourly MITgcm LLC4320 Native Grid 2km Oceanographic Dataset Version 1.0. PO.DAAC, CA, USA. Dataset accessed[YYYY-MM-DD] at https://doi.org/10.5067/PRESW-BSJ10.",
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
-                "salinity/density",
-                "ocean circulation",
-                "oceans",
-                "earth science",
-                "ocean heat budget",
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
-            "identifier": "C2006849866-POCLOUD",
-            "description": "This dataset provides a regional multivariate oceanographic state estimate from a global ocean numerical simulation with a focus on the Bass Strait region. The global ocean simulation is based on the MIT general circulation model (MITgcm) with Lat-Lon-Cap grid (LLC) layout and 1/48-degree (2km at equator) nominal horizontal resolution. This simulation is often referred to as LLC4320 in the community and existing publications. The simulation has 90 vertical levels, with about 1-m vertical resolution at the surface and 30 m down to 500 m, for optimized resolution of the upper-ocean processes. The model has zero parameterized horizontal diffusivity. In the vertical direction, the K-Profile Parameterization (KPP) is used for boundary layer turbulent mixing. It is spun up progressively from the lower resolution MITgcm simulation from the Estimating the Circulation & Climate of the Ocean (ECCO), and forced by the 6-hourly ERA-Interim atmosphere reanalysis ( https://www.ecmwf.int/en/forecasts/datasets/reanalysis-datasets/era-interim ). A synthetic surface pressure field consisting of the 16 most dominant tidal constituents is used to dynamically mimic the tidal forcing. The dataset provides hourly oceanographic variables at native grid. Three-dimensional variables include temperature, salinity, and velocity. Two-dimensional variables include sea level anomaly, ocean mixed layer thickness, bottom pressure anomaly, net freshwater flux, net heat flux, shortwave radiative flux, net salt flux, and ocean surface stress.",
-            "release-place": "PO.DAAC",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Menemenlis, D., Hill, C., Henze, C. E., Wang, J., & Fenty, I.",
-            "title": "Bass Strait Pre-SWOT Level-4 Hourly MITgcm LLC4320 Native Grid 2km Oceanographic Dataset Version 1.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MITgcm_LLC4320_Pre-SWOT_JPL_L4_BassStrait_v1.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset provides a regional multivariate oceanographic state estimate from a global ocean numerical simulation with a focus on the Bass Strait region. The global ocean simulation is based on the MIT general circulation model (MITgcm) with Lat-Lon-Cap grid (LLC) layout and 1/48-degree (2km at equator) nominal horizontal resolution. This simulation is often referred to as LLC4320 in the community and existing publications. The simulation has 90 vertical levels, with about 1-m vertical resolution at the surface and 30 m down to 500 m, for optimized resolution of the upper-ocean processes. The model has zero parameterized horizontal diffusivity. In the vertical direction, the K-Profile Parameterization (KPP) is used for boundary layer turbulent mixing. It is spun up progressively from the lower resolution MITgcm simulation from the Estimating the Circulation & Climate of the Ocean (ECCO), and forced by the 6-hourly ERA-Interim atmosphere reanalysis ( https://www.ecmwf.int/en/forecasts/datasets/reanalysis-datasets/era-interim ). A synthetic surface pressure field consisting of the 16 most dominant tidal constituents is used to dynamically mimic the tidal forcing. The dataset provides hourly oceanographic variables at native grid. Three-dimensional variables include temperature, salinity, and velocity. Two-dimensional variables include sea level anomaly, ocean mixed layer thickness, bottom pressure anomaly, net freshwater flux, net heat flux, shortwave radiative flux, net salt flux, and ocean surface stress.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FPRESW-BSJ10",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FPRESW-BSJ10",
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
```

