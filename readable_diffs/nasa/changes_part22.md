# Change History for nasa.json (Part 22)

### Changes from 31606f9 to dd2190f (Part 11/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/UserGuideAquariusCelestialSkyMicrowaveEmissionMapProduct.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_DENSITY_SMIA_SEASONAL-CLIMATOLOGY_V5.jpg",
+            "identifier": "C2491756018-POCLOUD",
+            "issued": "2017-10-21",
+            "keyword": [
+                "earth science",
+                "salinity/density",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQR50-3DVAE",
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
+            "series-name": "Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Ascending Seasonal Climatology Data",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T01:55:23Z/2015-06-07T11:41:38Z",
             "theme": [
                 "AQUARIUS SAC-D",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Ascending Seasonal Climatology Data V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-MAG-4-RDR-S3COORDS-1.92SEC-V1.1",
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
+            "description": "This data set includes Voyager 2 Jupiter encounter magnetometer data from the Low Field Magnetometer (LFM) resampled at a 1.92 second sample rate from the 60 msec instrument sampling rate. Data coverage begins in the solar wind and continues until at least the first magnetopause crossing. The data are given in Jovicentric System III (1965) right handed coordinates. The data set is composed of the following columns: 1) time - UT of the sample in the format yyyy-mm-ddThh:mm:ss.sssZ, 2) spacecraft clock values (m65536:mod60:fds_line), 3) mag_id - magnetometer id (1 = LFM, 2 = HFM), 4) Br - radial (Jupiter to spacecraft) B-field component, 5) Btheta - North/South (system III) B-field component (positive southward), 6) Bphi - azimuthal (system III) B-field component (positive eastward), 7) Bmag - magnitude of the averaged magnetic field components, 8) avg_Bmag - average of the magnetic field magnitudes, 9) delta - magnetic latitude = arcsin(Btheta/Bmag), 10) lambda - longitude = 180. - atan(Bphi/-Br), 11-13) rms_br, rms_bt, and rms_bn - rms vectors, 14) npts - number of points in average.  All magnetic field observations are measured in nanoTesla. All of the magnetic field data are calibrated (see the instrument calibration description for more details).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-mag-4-rdr-s3coords-1.92sec-v1.1_3ujb-dqd4",
+            "issued": "2021-05-21",
+            "keyword": [
+                "jupiter",
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-MAG-4-RDR-S3COORDS-1.92SEC-V1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-mag-4-rdr-s3coords-1.92sec-v1.1_3ujb-dqd4",
-            "description": "This data set includes Voyager 2 Jupiter encounter magnetometer data from the Low Field Magnetometer (LFM) resampled at a 1.92 second sample rate from the 60 msec instrument sampling rate. Data coverage begins in the solar wind and continues until at least the first magnetopause crossing. The data are given in Jovicentric System III (1965) right handed coordinates. The data set is composed of the following columns: 1) time - UT of the sample in the format yyyy-mm-ddThh:mm:ss.sssZ, 2) spacecraft clock values (m65536:mod60:fds_line), 3) mag_id - magnetometer id (1 = LFM, 2 = HFM), 4) Br - radial (Jupiter to spacecraft) B-field component, 5) Btheta - North/South (system III) B-field component (positive southward), 6) Bphi - azimuthal (system III) B-field component (positive eastward), 7) Bmag - magnitude of the averaged magnetic field components, 8) avg_Bmag - average of the magnetic field magnitudes, 9) delta - magnetic latitude = arcsin(Btheta/Bmag), 10) lambda - longitude = 180. - atan(Bphi/-Br), 11-13) rms_br, rms_bt, and rms_bn - rms vectors, 14) npts - number of points in average.  All magnetic field observations are measured in nanoTesla. All of the magnetic field data are calibrated (see the instrument calibration description for more details).",
-            "title": "VG2 JUP MAG RESAMPLED SYSTEM III (1965)\nCOORDS 1.92SEC V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG2 JUP MAG RESAMPLED SYSTEM III (1965)\nCOORDS 1.92SEC V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/3ujn-ffq2",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "The experiment is part of a project to study DNA repair process after ionizing radiation in organotypic 3-dimentional human bronchial epithlial cell culture. Human bronchial epithelial cells were grown in tissue culture flask (2D) or in matrics gel (3D). Three independent cultures were done for each condition.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-149",
+                    "mediaType": "text/html",
+                    "title": "Comparison of gene expression profiles of normal human bronchial epithelial cells in 2D and 3D cultural conditions"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-149_3ujn-ffq2",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "p-gse27520-2",
                 "p-gse27520-1",
@@ -104720,336 +104734,300 @@
                 "p-gse27520-5",
                 "p-gse27520-6"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/3ujn-ffq2",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-149_3ujn-ffq2",
-            "description": "The experiment is part of a project to study DNA repair process after ionizing radiation in organotypic 3-dimentional human bronchial epithlial cell culture. Human bronchial epithelial cells were grown in tissue culture flask (2D) or in matrics gel (3D). Three independent cultures were done for each condition.",
-            "title": "Comparison of gene expression profiles of normal human bronchial epithelial cells in 2D and 3D cultural conditions",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-149",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Comparison of gene expression profiles of normal human bronchial epithelial cells in 2D and 3D cultural conditions"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Comparison of gene expression profiles of normal human bronchial epithelial cells in 2D and 3D cultural conditions"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/C1JYLA4YUO5X",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SnowEx20 Grand Mesa Autumn 2019 Snow Depth V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/C1JYLA4YUO5X.",
-            "issued": "2019-11-04",
-            "temporal": "2019-11-04T00:00:00Z/2019-11-07T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-11-07",
-            "keyword": [
-                "earth science",
-                "terrestrial hydrosphere",
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
-            "identifier": "C2107120672-NSIDC_ECS",
             "description": "Snow depth was measured in autumn 2019 as part of the NASA SnowEx 2020 campaign at Grand Mesa, CO. Measurements were taken in the vicinity of snow pit locations and between pit locations using a Magnaprobe or manual depth probes.",
-            "title": "SnowEx20 Grand Mesa Autumn 2019 Snow Depth V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FC1JYLA4YUO5X",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FC1JYLA4YUO5X",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_A19_SD.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_A19_SD.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_A19_SD/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_A19_SD/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX20_A19_SD+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX20_A19_SD+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/C1JYLA4YUO5X",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/C1JYLA4YUO5X",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/C1JYLA4YUO5X",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/C1JYLA4YUO5X",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2107120672-NSIDC_ECS",
+            "issued": "2019-11-04",
+            "keyword": [
+                "earth science",
+                "terrestrial hydrosphere",
+                "snow/ice"
+            ],
+            "landingPage": "https://doi.org/10.5067/C1JYLA4YUO5X",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-11-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-108.212901 39.003473 -108.129346 39.043616",
+            "temporal": "2019-11-04T00:00:00Z/2019-11-07T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SnowEx20 Grand Mesa Autumn 2019 Snow Depth V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-5-ESC3-MTP021-V1.0",
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
+            "description": "This data set contains derived electron and proton flux energies in MeV from the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, which had the primary target of comet 67P/Churyumov-Gerasimenko. These are CODMAC Level 5 derived data, and measure the radiation in the spacecraft environment during the Medium Term Plan 21 period of the ESCORT 3 mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-5-esc3-mtp021-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-5-ESC3-MTP021-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-5-esc3-mtp021-v1.0",
-            "description": "This data set contains derived electron and proton flux energies in MeV from the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, which had the primary target of comet 67P/Churyumov-Gerasimenko. These are CODMAC Level 5 derived data, and measure the radiation in the spacecraft environment during the Medium Term Plan 21 period of the ESCORT 3 mission phase.",
-            "title": "ROSETTA-ORBITER 67P SREM 5 ESCORT 3\n    MTP021 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P SREM 5 ESCORT 3\n    MTP021 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1220",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wei, Y., Shishi Liu, D.N. Huntzinger, A.M. Michalak, N. Viovy, W.M. Post, C.R. Schwalm, K. Schaefer, A.R. Jacobson, C. Lu, H. Tian, D.M. Ricciuto, R.B. Cook, J. Mao, and X. Shi. 2014. NACP MsTMIP: Global and North American Driver Data for Multi-Model Intercomparison. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1220",
-            "issued": "2022-11-21",
-            "temporal": "1700-01-01T00:00:00Z/2010-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-17",
-            "keyword": [
-                "precipitation",
-                "earth science",
-                "atmospheric chemistry",
-                "ecosystems",
-                "atmospheric temperature",
-                "atmosphere",
-                "vegetation",
-                "soils",
-                "land surface",
-                "land use/land cover",
-                "biosphere",
-                "atmospheric radiation"
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
-            "identifier": "C2552206090-ORNL_CLOUD",
             "description": "This data set provides environmental data that have been standardized and aggregated for use as input to carbon cycle models at global (0.5-degree resolution) and regional (North America at 0.25-degree resolution) scales. The data were compiled from selected sources (Table 2) and integrated into gridded global and regional collections of climatology variables (precipitation, air temperature, air specific humidity, air relative humidity (NA only), pressure, downward longwave radiation, downward shortwave radiation, and wind speed), time-varying atmospheric CO2 concentrations, time-varying nitrogen deposition, biome fraction and type, land-use and land-cover change, C3/C4 grasses fractions, major crop distribution, phenology, multiple soil characteristics, and a land-water mask. The temporal ranges of the data are sufficient for carbon cycle model simulations from 1801 to 2010. These data were compiled specifically for the North American Carbon Program (NACP) Multi-Scale Synthesis and Terrestrial Model Intercomparison Project (MsTMIP) as the prescribed model input driver data (Huntzinger et al., 2013). The driver data were used by 22 terrestrial biosphere models to run baseline and sensitivity simulations. The standardized data provided consistent model inputs to minimize the inter-model variability caused by differences in environmental drivers and initial conditions. Together with the sensitivity simulations, the standardized input data enable better interpretation and quantification of structural and parameter uncertainties of model estimates. Data are provided in Climate and Forecast (CF) metadata convention compliant (version 1.4) netCDF-4 file formats. There are 3,152 *.nc4 data files with this data set.",
-            "graphic-preview-description": "Browse Image",
-            "title": "NACP MsTMIP: Global and North American Driver Data for Multi-Model Intercomparison",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1220_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1220",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1220",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/nacp/NACP_MsTMIP_Model_Driver/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/nacp/NACP_MsTMIP_Model_Driver/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/NACP/guides/NACP_MsTMIP_Model_Driver.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/NACP/guides/NACP_MsTMIP_Model_Driver.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1220",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1220",
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
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_MsTMIP_Model_Driver/comp/NACP_MsTMIP_Model_Driver.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_MsTMIP_Model_Driver/comp/NACP_MsTMIP_Model_Driver.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1220_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1220_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1220/catalog.html",
-                    "description": "The THREDDS location for this Collection.",
                     "@type": "dcat:Distribution",
+                    "description": "The THREDDS location for this Collection.",
+                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1220/catalog.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1220_1_fit.png",
+            "identifier": "C2552206090-ORNL_CLOUD",
+            "issued": "2022-11-21",
+            "keyword": [
+                "precipitation",
+                "earth science",
+                "atmospheric chemistry",
+                "ecosystems",
+                "atmospheric temperature",
+                "atmosphere",
+                "vegetation",
+                "soils",
+                "land surface",
+                "land use/land cover",
+                "biosphere",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1220",
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
             "spatial": "-178.75 -78.25 179.95 89.75",
+            "temporal": "1700-01-01T00:00:00Z/2010-12-31T23:59:59Z",
             "theme": [
                 "NACP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NACP MsTMIP: Global and North American Driver Data for Multi-Model Intercomparison"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0544-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-01-21T04:19:50.000 to 2015-01-21T11:23:33.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0544-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0544-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0544-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-01-21T04:19:50.000 to 2015-01-21T11:23:33.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0544 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0544 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://curator.jsc.nasa.gov/lunar/catalogs/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://curator.jsc.nasa.gov/lunar/catalogs/apollo14catalog.cfm"
-            ],
-            "keyword": [
-                "apollo",
-                "sample",
-                "lunar",
-                "jsc",
-                "catalog"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Carlton Allen",
                 "hasEmail": "mailto:carlton.c.allen@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-877",
             "description": "Apollo 16 Sample Catalog by Graham Ryder and Marc D. Norman",
-            "title": "Apollo 16 Sample Catalog",
-            "programCode": [
-                "026:008"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -105057,435 +105035,435 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-877",
+            "issued": "2018-06-25",
+            "keyword": [
+                "apollo",
+                "sample",
+                "lunar",
+                "jsc",
+                "catalog"
+            ],
+            "landingPage": "http://curator.jsc.nasa.gov/lunar/catalogs/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:008"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "references": [
+                "http://curator.jsc.nasa.gov/lunar/catalogs/apollo14catalog.cfm"
+            ],
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "Apollo 16 Sample Catalog"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/3upt-7jnj",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "keyword": [
-                "['microgravity simulation' 'treatment']",
-                "['treatment protocol' 'nucleic acid extraction' 'library construction' 'nucleic acid sequencing']"
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
-            "identifier": "nasa_genelab_GLDS-373_3upt-7jnj",
             "description": "['To reveal the potential mechanisms involved in the dysfunction of antiviral immune responses under simulated microgravity conditions, we investigated the transcriptional changes related to the status of innate immune responses by RNA-seq with poly I:C or mock PBS treatment under Normal gravity or simulated microgravity conditions. Our results indicate that the retinoic acid inducible gene (RIG)-I-like receptor (RLR) and Toll-like receptor (TLR) signal pathways, which are both involved in the type-I interferon induction, are significantly inhibited by simulated microgravity effects.']",
-            "title": "['RNA sequencing of zebrafish embryos under simulated microgravity conditions']",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-373",
-                    "description": "GeneLab Study Page",
                     "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-373",
+                    "mediaType": "text/html",
                     "title": "['RNA sequencing of zebrafish embryos under simulated microgravity conditions']"
                 }
             ],
+            "identifier": "nasa_genelab_GLDS-373_3upt-7jnj",
+            "issued": "2021-05-21",
+            "keyword": [
+                "['microgravity simulation' 'treatment']",
+                "['treatment protocol' 'nucleic acid extraction' 'library construction' 'nucleic acid sequencing']"
+            ],
+            "landingPage": "https://data.nasa.gov/d/3upt-7jnj",
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
+            "title": "['RNA sequencing of zebrafish embryos under simulated microgravity conditions']"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0059",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2004-02-03. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDCDAAC/NARSTO/0059.",
-            "issued": "2004-02-02",
-            "temporal": "1999-07-29T00:00:00Z/1999-09-02T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-04-18",
-            "keyword": [
-                "atmosphere",
-                "atmospheric winds",
-                "earth science",
-                "atmospheric temperature"
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
-            "identifier": "C1000000081-LARC_ASDC",
             "description": "NARSTO_EPA_SS_ATLANTA_1999_UAH_MIPS_DATA is the North American Research Strategy for Tropospheric Ozone (NARSTO) Environmental Protection Agency (EPA) Supersite (SS) Atlanta 1999 University of Alabama-Huntsville (UAH) Mobile Integrated Profiling System (MIPS) Wind Data product. Files for this data product were obtained from July to September 1999 during the Atlanta Experiment of the EPA Particulate Matter Supersites Program. The UAH MIPS Doppler profiler (915 MHz radar) was used to estimate the vertical distribution of horizontal wind speed and wind direction. Radial velocity along six beams was used to obtain the horizontal wind speed and wind direction. The consensus averaging time was 55 minutes, the number of beams is 6, and the number of range gates was 41. For beam 1, the number of records required to make consensus was 16, the total number of records was 26, and the consensus window size was 4 m/s. For beams 2 and 3, the number of records required to make consensus was 13, the total number of records was 26, and the consensus window size was 3 m/s. There was no data for beams 4 and 5. For beam 6, the number of records required to make consensus was 16, the total number of records was 26 and the consensus window size was 3 m/s. The azimuth and elevation for beams 1 to 6 were: 358 and 90; 88 and 66.4; 178 and 66.4; none; none; 88 and 90.\r\n\r\nThe EPA selected Atlanta as one of the first Supersites Programs dedicated to the study of fine particles (or Particulate Matter (PM) 2.5). The Southern Oxidants Study (SOS) in conjunction with the Georgia Institute of Technology, Earth and Atmospheric Sciences Department developed and implemented the scientific research plan for this initial Supersites Program effort. The Atlanta field experiment was a 4-week long campaign aimed at comprehensively addressing issues related to the measurement and characterization of fine particles in the polluted or urban atmosphere. The experiment took place during the August 1999 and deployed a wide array of instrumentation at a measurement site located on Jefferson Street in Midtown Atlanta. \r\n\r\nGoals of the Atlanta Supersite Program were twofold: first, to provide a platform for testing and contrasting some of the newer particle measurement techniques; and second, to provide data to advance our scientific understanding of atmospheric processes regarding atmospheric particles. Specific objectives were: (1) to characterize the performance of emerging and/or state-of-the-science PM Measurements; (2) to compare and contrast similar and dissimilar PM Measurements; (3) to evaluate the precision, accuracy, and completeness of information that can be gained from the planned EPA PM mass and chemical composition networks; (4) to evaluate the scientific information gained by combining various independent and complementary PM Measurements; and (5) to address various scientific issues and their ozone- and PM-related policy implications with this data base.\r\n\r\nThe EPA PM Supersites Program was an ambient air monitoring research program from 1999-2004 designed to provide information of value to the atmospheric sciences, and human health and exposure research communities. Eight geographically diverse projects were chosen to specifically address the following EPA research priorities: (1) to characterize PM, its constituents, precursors, co-pollutants, atmospheric transport, and its source categories that affect the PM in any region; (2) to address the research questions and scientific uncertainties about PM source-receptor and exposure-health effects relationships; and (3) to compare and evaluate different methods of characterizing PM including testing new and emerging measurement methods.\r\n\r\nNARSTO, which has since disbanded, was a public/private partnership, whose membership spanned across government, utilities, industry, and academe throughout Mexico, the United States, and Canada. The primary mission was to coordinate and enhance policy-relevant scientific rese",
-            "title": "NARSTO EPA Supersite (SS) Atlanta 1999 University of Alabama-Huntsville (UAH) Mobile Integrated Profiling System (MIPS) Wind Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDCDAAC%2FNARSTO%2F0059",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDCDAAC%2FNARSTO%2F0059",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000081-LARC_ASDC",
-                    "description": "Earthdata Search for NARSTO_EPA_SS_ATLANTA_1999_UAH_MIPS_DATA_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for NARSTO_EPA_SS_ATLANTA_1999_UAH_MIPS_DATA_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000081-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0059",
-                    "description": "DOI data set landing page for NARSTO_EPA_SS_ATLANTA_1999_UAH_MIPS_DATA_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for NARSTO_EPA_SS_ATLANTA_1999_UAH_MIPS_DATA_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0059",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/guide/narsto_epa_ss_atlanta_1999_uah_mips_data.pdf",
-                    "description": "Guide for NARSTO EPA_SS_ATLANTA 1999UAH Mobile Integrated Profiling System Data",
                     "@type": "dcat:Distribution",
+                    "description": "Guide for NARSTO EPA_SS_ATLANTA 1999UAH Mobile Integrated Profiling System Data",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/guide/narsto_epa_ss_atlanta_1999_uah_mips_data.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/NARSTO/EPA_SS_ATLANTA_1999_UAH_MIPS_DATA_1/",
-                    "description": "ASDC Direct Data Download for NARSTO_EPA_SS_ATLANTA_1999_UAH_MIPS_DATA_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for NARSTO_EPA_SS_ATLANTA_1999_UAH_MIPS_DATA_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/NARSTO/EPA_SS_ATLANTA_1999_UAH_MIPS_DATA_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1000000081-LARC_ASDC",
+            "issued": "2004-02-02",
+            "keyword": [
+                "atmosphere",
+                "atmospheric winds",
+                "earth science",
+                "atmospheric temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0059",
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
             "spatial": "33.78 -84.41",
+            "temporal": "1999-07-29T00:00:00Z/1999-09-02T23:59:59.999Z",
             "theme": [
                 "NARSTO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NARSTO EPA Supersite (SS) Atlanta 1999 University of Alabama-Huntsville (UAH) Mobile Integrated Profiling System (MIPS) Wind Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0004",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1999-08-13. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/FIRE/0004.",
-            "issued": "1999-08-13",
-            "temporal": "1998-05-13T00:00:00Z/1998-06-08T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-02",
-            "keyword": [
-                "earth science",
-                "visible wavelengths",
-                "spectral/engineering",
-                "infrared wavelengths"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "PAUL HUBANKS",
                 "hasEmail": "mailto:paul.a.hubanks@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1000000941-LARC_ASDC",
             "description": "This data set consists of radiance measurements from the NASA ER2 Moderate Resolution Imaging Spectroradiometer (MODIS) Airborne Simulator (MAS) during the First ISCCP Regional Experiment (FIRE) Arctic Cloud Experiment (ACE).The First ISCCP Regional Experiments have been designed to improve data products and cloud/radiation parameterizations used in general circulation models (GCMs). Specifically, the goals of FIRE are (1) to improve basic understanding of the interaction of physical processes in determining life cycles of cirrus and marine stratocumulus systems and the radiative properties of these clouds during their life cycles and (2) to investigate the interrelationships between the ISCCP data, GCM parameterizations, and higher space and time resolution cloud data.",
-            "title": "First ISCCP Regional Experiment (FIRE) Arctic Cloud Experiment (ACE) from the the NASA ER2 MODIS Airborne Simulator (MAS)",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0004",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0004",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000941-LARC_ASDC",
-                    "description": "Earthdata Search for FIRE_ACE_ER2_MAS_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FIRE_ACE_ER2_MAS_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000941-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_ACE_ER2_MAS/contents.html",
-                    "description": "OPeNDAP data access for FIRE_ACE_ER2_MAS_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for FIRE_ACE_ER2_MAS_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_ACE_ER2_MAS/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/fire_ace_er2_mas.readme.txt",
-                    "description": "Readme file for the FIRE ACE ER2 MAS Data Sets",
                     "@type": "dcat:Distribution",
+                    "description": "Readme file for the FIRE ACE ER2 MAS Data Sets",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/fire_ace_er2_mas.readme.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/ace_er2_mas_read_netcdf.c",
-                    "description": "Readme to produce a general read program for users to access Data Sets written in NCSA's HDF netCDF format - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "Readme to produce a general read program for users to access Data Sets written in NCSA's HDF netCDF format - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/ace_er2_mas_read_netcdf.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/ace_er2_mas_read_netcdf_idl.pro",
-                    "description": "Readme to open the PRO MAS_READ_NETCDF_IDL file and initialize the SDS interface",
                     "@type": "dcat:Distribution",
+                    "description": "Readme to open the PRO MAS_READ_NETCDF_IDL file and initialize the SDS interface",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/ace_er2_mas_read_netcdf_idl.pro",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/fire3_ace/ACEDOCS/data/logs/er-2/ace_ER-2_fltloglist.pdf",
-                    "description": "FIRE-ACE ER-2 Flight Logs and Flight Track Images",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE-ACE ER-2 Flight Logs and Flight Track Images",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/fire3_ace/ACEDOCS/data/logs/er-2/ace_ER-2_fltloglist.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0004",
-                    "description": "DOI data set landing page for FIRE_ACE_ER2_MAS_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIRE_ACE_ER2_MAS_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0004",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/fire3_ace/ACEDOCS/index.pdf",
-                    "description": "FIRE Arctic Cloud Experiment (FIRE.ACE) Home Page Document",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE Arctic Cloud Experiment (FIRE.ACE) Home Page Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/fire3_ace/ACEDOCS/index.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ace_ampr",
-                    "description": "Readme Information about the data provided by the AMPR flown onboard the ER2 aircraft during the FIRE ACE field campaign",
                     "@type": "dcat:Distribution",
+                    "description": "Readme Information about the data provided by the AMPR flown onboard the ER2 aircraft during the FIRE ACE field campaign",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ace_ampr",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/read_fire_ace_ampr.f",
-                    "description": "Program to read SRB Release 3 Shortwave 3 Hourly nc - Direct File Download (.f)",
                     "@type": "dcat:Distribution",
+                    "description": "Program to read SRB Release 3 Shortwave 3 Hourly nc - Direct File Download (.f)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/read_fire_ace_ampr.f",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/MAS",
-                    "description": "ASDC Data and Information for MAS",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for MAS",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/MAS",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://mas.arc.nasa.gov/data/deploy_html/fire_home.html",
-                    "description": "Campaign Summary Information for First ISCCP Regional Experiment (FIRE)",
                     "@type": "dcat:Distribution",
+                    "description": "Campaign Summary Information for First ISCCP Regional Experiment (FIRE)",
+                    "downloadURL": "https://mas.arc.nasa.gov/data/deploy_html/fire_home.html",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://mas.arc.nasa.gov/data/deploy_html/fireace_home.html",
-                    "description": "Campaign Summary Information for First ISSCP Regional Experiment - Arctic Cloud Experiment (FIRE-ACE)",
                     "@type": "dcat:Distribution",
+                    "description": "Campaign Summary Information for First ISSCP Regional Experiment - Arctic Cloud Experiment (FIRE-ACE)",
+                    "downloadURL": "https://mas.arc.nasa.gov/data/deploy_html/fireace_home.html",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://mas.arc.nasa.gov/",
-                    "description": "Enhanced MODIS Airborne Simulator (eMAS) Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "Enhanced MODIS Airborne Simulator (eMAS) Project Home Page",
+                    "downloadURL": "https://mas.arc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
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
-                    "downloadURL": "https://mas.arc.nasa.gov/data/srf/ARC-Jun95/msr0695.ph",
-                    "description": "MAS Spectral Response Summary",
                     "@type": "dcat:Distribution",
+                    "description": "MAS Spectral Response Summary",
+                    "downloadURL": "https://mas.arc.nasa.gov/data/srf/ARC-Jun95/msr0695.ph",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_ACE_ER2_MAS/",
-                    "description": "ASDC Direct Data Download for FIRE_ACE_ER2_MAS_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIRE_ACE_ER2_MAS_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_ACE_ER2_MAS/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1000000941-LARC_ASDC",
+            "issued": "1999-08-13",
+            "keyword": [
+                "earth science",
+                "visible wavelengths",
+                "spectral/engineering",
+                "infrared wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0004",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-07-02",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>35.56 -174.11 35.56 -118.51 78.2 -118.51 78.2 -174.11 35.56 -174.11</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1998-05-13T00:00:00Z/1998-06-08T23:59:59.999Z",
             "theme": [
                 "FIRE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "First ISCCP Regional Experiment (FIRE) Arctic Cloud Experiment (ACE) from the the NASA ER2 MODIS Airborne Simulator (MAS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1237114214-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "TOMS Science Team. TOMSN7L3dery. Version 008. TOMS Nimbus-7 UV-B Erythemal Local Noon Irradiance Daily L3 Global 1 deg x 1.25 deg Lat/Lon Grid V008. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/TOMSN7L3dery_008.html. Digital Science Data.",
-            "issued": "2004-04-30",
-            "temporal": "1978-11-01T00:00:00Z/1993-05-06T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2004-04-30",
-            "keyword": [
-                "earth science",
-                "atmosphere",
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
-            "identifier": "C1237114214-GES_DISC",
-            "description": "This Nimbus-7 Total Ozone Mapping Spectrometer (TOMS) version 8 daily global gridded data product contains UV-B erythemal local noon irradiance values. The data are mapped to a global grid of size 180 x 288 with a lat-long resolution of 1.00 x 1.25 degrees. These data are stored in an ASCII format.\n\nThe TOMS data were produced by the Laboratory for Atmospheres at NASA Goddard Space Flight Center (Code 614).",
-            "release-place": "Greenbelt, MD",
-            "series-name": "TOMSN7L3dery",
             "creator": "TOMS Science Team",
-            "title": "TOMS Nimbus-7 UV-B Erythemal Local Noon Irradiance Daily L3 Global 1 deg x 1.25 deg Lat/Lon Grid V008 (TOMSN7L3dery) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOMSN7L3dery_008.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "This Nimbus-7 Total Ozone Mapping Spectrometer (TOMS) version 8 daily global gridded data product contains UV-B erythemal local noon irradiance values. The data are mapped to a global grid of size 180 x 288 with a lat-long resolution of 1.00 x 1.25 degrees. These data are stored in an ASCII format.\n\nThe TOMS data were produced by the Laboratory for Atmospheres at NASA Goddard Space Flight Center (Code 614).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -105494,254 +105472,290 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TOMSN7L3dery_008.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TOMSN7L3dery_008.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus7_TOMS_Level3/TOMSN7L3dery.008/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus7_TOMS_Level3/TOMSN7L3dery.008/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TOMSN7L3dery",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TOMSN7L3dery",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TOMS/NIMBUS7_USERGUIDE.PDF",
-                    "description": "Nimbus-7 TOMS Data Product User's Guide.",
                     "@type": "dcat:Distribution",
+                    "description": "Nimbus-7 TOMS Data Product User's Guide.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TOMS/NIMBUS7_USERGUIDE.PDF",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOMSN7L3dery_008.png",
+            "identifier": "C1237114214-GES_DISC",
+            "issued": "2004-04-30",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1237114214-GES_DISC.html",
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
+            "series-name": "TOMSN7L3dery",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1978-11-01T00:00:00Z/1993-05-06T23:59:59.999Z",
             "theme": [
                 "TOMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TOMS Nimbus-7 UV-B Erythemal Local Noon Irradiance Daily L3 Global 1 deg x 1.25 deg Lat/Lon Grid V008 (TOMSN7L3dery) at GES DISC"
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmag-4-esc1-resampled-v5.0_3uup-zurk",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "checkout",
                 "solar wind",
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMAG-4-ESC1-RESAMPLED-V5.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmag-4-esc1-resampled-v5.0_3uup-zurk",
-            "description": "This dataset contains RESAMPLED DATA (CODMAC LEVEL 4) of the COMET\nESCORT1 Phase from November 22, 2014 until March 10, 2015 of the\nROSETTA orbiter magnetometer RPCMAG. Data are averaged to 60s means.\nObservations are done in the vicinity of comet\n67P/CHURYUMOV-GERASIMENKO 1 (1969 R1).\nVersion V5.0 is the first version being released.",
-            "title": "ROSETTA-ORBITER 67P RPCMAG 4 ESC1 RESAMPLED V5.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER 67P RPCMAG 4 ESC1 RESAMPLED V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-PRL-67PCHURYUMOV-M06-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-08-01T10:00:00.000 to 2014-09-02T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-prl-67pchuryumov-m06-v3.0",
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
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-PRL-67PCHURYUMOV-M06-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-prl-67pchuryumov-m06-v3.0",
-            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-08-01T10:00:00.000 to 2014-09-02T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 3 PRL-MTP006 RDR V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 3 PRL-MTP006 RDR V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0576-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-02-12T08:54:45.000 to 2015-02-12T10:45:07.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0576-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0576-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0576-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-02-12T08:54:45.000 to 2015-02-12T10:45:07.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0576 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0576 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-GRS-2-EDR-CRUISE2-V1.0",
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
+            "description": "This data set contains Gamma Ray Spectrometer (GRS) observations made during the second cruise phase of the NEAR mission. The individual observations are combined into a single file per day for each sensor.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-grs-2-edr-cruise2-v1.0_3uzs-sp3r",
+            "issued": "2021-05-21",
+            "keyword": [
+                "solar system",
+                "near earth asteroid rendezvous"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-GRS-2-EDR-CRUISE2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-grs-2-edr-cruise2-v1.0_3uzs-sp3r",
-            "description": "This data set contains Gamma Ray Spectrometer (GRS) observations made during the second cruise phase of the NEAR mission. The individual observations are combined into a single file per day for each sensor.",
-            "title": "NEAR GRS SPECTRA FOR CRUISE 2 PHASE",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEAR GRS SPECTRA FOR CRUISE 2 PHASE"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-SDC-3-PLUTO-V1.0",
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
+            "description": "This data set contains Calibrated data taken by the New Horizons         Student Dust Counter                                                   instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 1.0 of this data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-sdc-3-pluto-v1.0_3v4e-kesy",
+            "issued": "2018-09-05",
+            "keyword": [
+                "dust",
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-SDC-3-PLUTO-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-sdc-3-pluto-v1.0_3v4e-kesy",
-            "description": "This data set contains Calibrated data taken by the New Horizons         Student Dust Counter                                                   instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 1.0 of this data set.",
-            "title": "NEW HORIZONS                            \n      SDC PLUTO ENCOUNTER                                                     \n      CALIBRATED V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS                            \n      SDC PLUTO ENCOUNTER                                                     \n      CALIBRATED V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220565954-USGS_LTA.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "U.S. Geological Survey. 1990-01-01. Alaska AVHRR Twice-Monthly Composites. Sioux Falls, South Dakota, \nUSA. Archived by National Aeronautics and Space Administration, U.S. Government, U.S. Geological Survey. Remote Sensing \nImage.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EROS CENTER",
+                "hasEmail": "mailto:lta@usgs.gov"
+            },
+            "creator": "U.S. Geological Survey",
+            "data-presentation-form": "Remote Sensing \nImage",
+            "description": "The goal of the Alaska Advanced Very High Resolution Radiometer  (AVHRR) project is to compile a time series data set of calibrated,  georegistered  daily observations and twice-monthly maximum normalized difference  vegetation index (NDVI) composites for Alaska's annual growing  season (April-October). This data set has applications for environmental monitoring and for assessing impacts of global climate change.  An Alaska AVHRR data set is comprised of twice-monthly maximum NDVI composites of daily satellite observations.  The NDVI composites  contain 10 bands of information, including AVHRR channels 1-5, maximum NDVI, satellite zenith, solar zenith, and relative azimuth.  The daily   observations, bands 1-9, have been calibrated to reflectance, scaled  to   byte data, and geometrically registered to the Albers Equal-Area  Conic map projection. The 10th band is a pointer to identify the date and  scene ID of  the source daily observation (scene) for each pixel.\n\nThe compositing process required each daily overpass to be  registered to a common map projection to ensure that from day to day each 1-km pixel represented the exact same ground location.  The Albers Equal-Area Conic map projection provides for equal area representation, which enables  easy measurement of area throughout the data.  Each daily observation for  the growing season was registered to a base image using image-to-image correlation.\n\nThe NDVI data are calculated from the calibrated, geometrically  registered daily observations. The NDVI value is the difference between  near-infrared (AVHRR Channel 2) and visible (AVHRR Channel 1) reflectance values  divided by total measured reflectance.  A maximum NDVI compositing process  was used on the daily observations.  The NDVI is examined pixel by pixel for  each observation during the compositing period to determine and retain  the maximum value.  Often when displaying data covering large areas, such as AVHRR data,  it is beneficial to include an overlay of either familiar linework for  reflectance or polygon data sets to derive statistical summaries of regions.  All of the linework images represent lines in raster format as 1-km cells and  the strata are represented as polygons registered to the AVHRR data.  The  linework and polygon data sets include international boundaries, Alaskan roads  with the Trans-Alaska Pipeline, and a raster polygon mask of the State.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "\n         Query and order satellite images, aerial photographs, and  cartographic products through the U.S. Geological Survey. Log in as a guest or  as a registered user. Registered users have access to more features  than guests do. If you plan on using EarthExplorer frequently, you may wish to  register. Please note that this site uses Session Cookies and Java applets.\n      ",
+                    "downloadURL": "http://earthexplorer.usgs.gov/",
+                    "mediaType": "text/html",
+                    "title": "The dataset's project home page"
+                }
+            ],
+            "identifier": "C1220565954-USGS_LTA",
             "issued": "1990-06-16",
-            "temporal": "1990-06-16T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-03-25",
             "keyword": [
                 "biosphere",
                 "spectral/engineering",
@@ -105750,424 +105764,390 @@
                 "infrared wavelengths",
                 "visible wavelengths"
             ],
-            "data-presentation-form": "Remote Sensing \nImage",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EROS CENTER",
-                "hasEmail": "mailto:lta@usgs.gov"
-            },
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220565954-USGS_LTA.html",
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
-            "identifier": "C1220565954-USGS_LTA",
-            "description": "The goal of the Alaska Advanced Very High Resolution Radiometer  (AVHRR) project is to compile a time series data set of calibrated,  georegistered  daily observations and twice-monthly maximum normalized difference  vegetation index (NDVI) composites for Alaska's annual growing  season (April-October). This data set has applications for environmental monitoring and for assessing impacts of global climate change.  An Alaska AVHRR data set is comprised of twice-monthly maximum NDVI composites of daily satellite observations.  The NDVI composites  contain 10 bands of information, including AVHRR channels 1-5, maximum NDVI, satellite zenith, solar zenith, and relative azimuth.  The daily   observations, bands 1-9, have been calibrated to reflectance, scaled  to   byte data, and geometrically registered to the Albers Equal-Area  Conic map projection. The 10th band is a pointer to identify the date and  scene ID of  the source daily observation (scene) for each pixel.\n\nThe compositing process required each daily overpass to be  registered to a common map projection to ensure that from day to day each 1-km pixel represented the exact same ground location.  The Albers Equal-Area Conic map projection provides for equal area representation, which enables  easy measurement of area throughout the data.  Each daily observation for  the growing season was registered to a base image using image-to-image correlation.\n\nThe NDVI data are calculated from the calibrated, geometrically  registered daily observations. The NDVI value is the difference between  near-infrared (AVHRR Channel 2) and visible (AVHRR Channel 1) reflectance values  divided by total measured reflectance.  A maximum NDVI compositing process  was used on the daily observations.  The NDVI is examined pixel by pixel for  each observation during the compositing period to determine and retain  the maximum value.  Often when displaying data covering large areas, such as AVHRR data,  it is beneficial to include an overlay of either familiar linework for  reflectance or polygon data sets to derive statistical summaries of regions.  All of the linework images represent lines in raster format as 1-km cells and  the strata are represented as polygons registered to the AVHRR data.  The  linework and polygon data sets include international boundaries, Alaskan roads  with the Trans-Alaska Pipeline, and a raster polygon mask of the State.",
             "release-place": "Sioux Falls, South Dakota, \nUSA",
-            "creator": "U.S. Geological Survey",
-            "title": "Alaska AVHRR Twice-Monthly Composites",
-            "programCode": [
-                "026:001"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://earthexplorer.usgs.gov/",
-                    "description": "\n         Query and order satellite images, aerial photographs, and  cartographic products through the U.S. Geological Survey. Log in as a guest or  as a registered user. Registered users have access to more features  than guests do. If you plan on using EarthExplorer frequently, you may wish to  register. Please note that this site uses Session Cookies and Java applets.\n      ",
-                    "@type": "dcat:Distribution",
-                    "title": "The dataset's project home page"
-                }
-            ],
             "spatial": "-179.0 51.0 -116.0 70.0",
+            "temporal": "1990-06-16T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Alaska AVHRR Twice-Monthly Composites"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SENTINEL-3B/OLCI/L3B/CYAN/TC/5",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SENTINEL-3B/OLCI/L3B/CYAN/TC/5.",
-            "issued": "2022-09-13",
-            "temporal": "2018-04-25T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-13",
-            "keyword": [
-                "oceans",
-                "environmental advisories",
-                "biological classification",
-                "environmental governance/management",
-                "surface water",
-                "aquatic sciences",
-                "ecosystems",
-                "bacteria/archaea",
-                "terrestrial hydrosphere",
-                "water quality/water chemistry",
-                "coastal processes",
-                "human dimensions",
-                "hydrological advisories",
-                "marine environment monitoring",
-                "earth science",
-                "earth science services",
-                "biosphere",
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
-            "identifier": "C2561580607-OB_DAAC",
             "description": "Cyanobacteria Assessment Network (CyAN) is a multi-agency project among EPA, the National Aeronautics and Space Administration (NASA), the National Oceanic and Atmospheric Administration (NOAA), and the United States Geological Survey (USGS) to support the environmental management and public use of U.S. lakes and estuaries by providing a capability of detecting and quantifying cyanobacteria algal blooms. This effort has resulted in the production of satellite remote sensing products using the cyanobacteria index (CI) algorithm to estimate cyanobacteria concentrations (CI_cyano) in lakes across the contiguous United States (CONUS) and Alaska. The Merged S3 product combines Sentinel-3A and Sentinel-3B OLCI data.",
-            "title": "Sentinel-3B OLCI Global Binned CyAN Project, True Color (TC) Data, version 5.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSENTINEL-3B%2FOLCI%2FL3B%2FCYAN%2FTC%2F5",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSENTINEL-3B%2FOLCI%2FL3B%2FCYAN%2FTC%2F5",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/SENTINEL-3B/OLCI/L3B/CYAN/TC/5",
-                    "description": "OLCI-Sentinel-3B L3B CyAN Project, True Color (TC) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "OLCI-Sentinel-3B L3B CyAN Project, True Color (TC) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/SENTINEL-3B/OLCI/L3B/CYAN/TC/5",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2561580607-OB_DAAC",
+            "issued": "2022-09-13",
+            "keyword": [
+                "oceans",
+                "environmental advisories",
+                "biological classification",
+                "environmental governance/management",
+                "surface water",
+                "aquatic sciences",
+                "ecosystems",
+                "bacteria/archaea",
+                "terrestrial hydrosphere",
+                "water quality/water chemistry",
+                "coastal processes",
+                "human dimensions",
+                "hydrological advisories",
+                "marine environment monitoring",
+                "earth science",
+                "earth science services",
+                "biosphere",
+                "ocean optics"
+            ],
+            "landingPage": "https://doi.org/10.5067/SENTINEL-3B/OLCI/L3B/CYAN/TC/5",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-09-13",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-04-25T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sentinel-3B OLCI Global Binned CyAN Project, True Color (TC) Data, version 5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ZGUTYDVAS74J",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "AMSRIce03 Snow Ice Temperature Data, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/ZGUTYDVAS74J.",
-            "issued": "2003-03-13",
-            "temporal": "2003-03-13T00:00:00Z/2003-03-20T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2003-03-20",
-            "keyword": [
-                "atmosphere",
-                "atmospheric temperature",
-                "snow/ice",
-                "sea ice",
-                "earth science",
-                "cryosphere",
-                "oceans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Matthew Sturm",
                 "hasEmail": "mailto:msturm@crrel.usace.army.mil"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1386205140-NSIDCV0",
             "description": "Notice to Data Users: The documentation for this data set was provided solely by the Principal Investigator(s) and was not further developed, thoroughly reviewed, or edited by NSIDC. Thus, support for this data set may be limited.\n\nThis data set contains snow ice temperature measurements collected over sea ice in the Barrow, Alaska USA area as part of the joint in situ and aircraft AMSRIce03 campaign.",
-            "title": "AMSRIce03 Snow Ice Temperature Data, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FZGUTYDVAS74J",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FZGUTYDVAS74J",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/cryosphere/AMSRIce03/ground_data/snowicetemps/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/cryosphere/AMSRIce03/ground_data/snowicetemps/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/cryosphere/AMSRIce03/ground_data/snowicetemps/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/cryosphere/AMSRIce03/ground_data/snowicetemps/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ZGUTYDVAS74J",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/ZGUTYDVAS74J",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ZGUTYDVAS74J",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ZGUTYDVAS74J",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386205140-NSIDCV0",
+            "issued": "2003-03-13",
+            "keyword": [
+                "atmosphere",
+                "atmospheric temperature",
+                "snow/ice",
+                "sea ice",
+                "earth science",
+                "cryosphere",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/ZGUTYDVAS74J",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2003-03-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-156.4 71.18 -156.15 71.28",
+            "temporal": "2003-03-13T00:00:00Z/2003-03-20T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AMSRIce03 Snow Ice Temperature Data, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/FNGNX6AQJT3W",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "ICESat-2 Pre-Launch Simulated Multiple Altimeter Beam Experimental Lidar Advanced Topographic Laser Altimeter System (MATLAS) Data, Version 2. Version 2. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/FNGNX6AQJT3W.",
-            "issued": "2012-02-24",
-            "temporal": "2012-02-24T00:00:00Z/2012-09-27T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2012-09-27",
-            "keyword": [
-                "spectral/engineering",
-                "infrared wavelengths",
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
-            "identifier": "C3180972416-NSIDCV0",
             "description": "Multiple Altimeter Beam Experimental Lidar (MABEL) Advanced Topographic Laser Altimeter System (MATLAS) simulates the expected performance of the ICESat-2 ATLAS instrument. The data are produced from MABEL data by adjusting the detected number of signal and noise photons to that predicted using ATLAS instrument model design cases. Each data file consists of approximately 1 minute of HDF5-derived MABEL data.",
-            "title": "ICESat-2 Pre-Launch Simulated Multiple Altimeter Beam Experimental Lidar Advanced Topographic Laser Altimeter System (MATLAS) Data, Version 2",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FFNGNX6AQJT3W",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FFNGNX6AQJT3W",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/IS2PLMATLAS_v2/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/IS2PLMATLAS_v2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/FNGNX6AQJT3W",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/FNGNX6AQJT3W",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/FNGNX6AQJT3W",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/FNGNX6AQJT3W",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C3180972416-NSIDCV0",
+            "issued": "2012-02-24",
+            "keyword": [
+                "spectral/engineering",
+                "infrared wavelengths",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/FNGNX6AQJT3W",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2012-09-27",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-123.725 35.9876 -17.7799 74.3744",
+            "temporal": "2012-02-24T00:00:00Z/2012-09-27T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ICESat-2 Pre-Launch Simulated Multiple Altimeter Beam Experimental Lidar Advanced Topographic Laser Altimeter System (MATLAS) Data, Version 2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-PPFLX-3-RDR-HALLEY-V2.0",
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
-                "1p/halley 1 (1682 q1)"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set presents the fluxes derived from narrow band photometry of Comet 1P/Halley as part of the International Halley Watch (IHW) Photometry and Polarimetry Netword (PPN). Standard filters, reference stars and reduction procedures were used as far as possible to reduce all narrowband data submitted to the PPN. The original data have been reformatted data supplied as addenda to the original submission have been added and the accompanying documentation updated in this revised version.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-ppflx-3-rdr-halley-v2.0_3vet-h7pm",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international halley watch",
+                "1p/halley 1 (1682 q1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-PPFLX-3-RDR-HALLEY-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-ppflx-3-rdr-halley-v2.0_3vet-h7pm",
-            "description": "This data set presents the fluxes derived from narrow band photometry of Comet 1P/Halley as part of the International Halley Watch (IHW) Photometry and Polarimetry Netword (PPN). Standard filters, reference stars and reduction procedures were used as far as possible to reduce all narrowband data submitted to the PPN. The original data have been reformatted data supplied as addenda to the original submission have been added and the accompanying documentation updated in this revised version.",
-            "title": "IHW COMET HALLEY PHOTOMETRIC FLUXES, V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "IHW COMET HALLEY PHOTOMETRIC FLUXES, V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0927-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-07-29T10:40:15.000 to 2015-07-29T17:28:59.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0927-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0927-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0927-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-07-29T10:40:15.000 to 2015-07-29T17:28:59.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0927 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0927 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0577-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-02-12T11:02:00.000 to 2015-02-12T15:49:10.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0577-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0577-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0577-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-02-12T11:02:00.000 to 2015-02-12T15:49:10.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0577 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0577 V1.0"
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
-            "identifier": "NASA-638",
             "description": "Data Dictionary and Index Files",
-            "title": "PDS Data Dictionary (1r72)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -106175,460 +106155,458 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-638",
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
+            "title": "PDS Data Dictionary (1r72)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-ALICE-3-LAUNCH-V1.0",
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
+            "description": "This data set contains Calibrated data taken by the New Horizons Alice UV Imager instrument during the post-launch checkout mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-alice-3-launch-v1.0_3vga-2m3n",
+            "issued": "2018-06-26",
+            "keyword": [
+                "new horizons",
+                "calibration"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-ALICE-3-LAUNCH-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-alice-3-launch-v1.0_3vga-2m3n",
-            "description": "This data set contains Calibrated data taken by the New Horizons Alice UV Imager instrument during the post-launch checkout mission phase.",
-            "title": "NEW HORIZONS ALICE POST-LAUNCH CHECKOUT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS ALICE POST-LAUNCH CHECKOUT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ENVISAT/MERIS/L1B/RR/4",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/ENVISAT/MERIS/L1B/RR/4.",
-            "issued": "2022-01-31",
-            "temporal": "2002-03-21T00:00:00Z/2012-05-09T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-31",
-            "keyword": [
-                "ocean optics",
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
-            "identifier": "C1569867388-OB_DAAC",
             "description": "MERIS (Medium Resolution Imaging Spectrometer) is a programmable, medium-spectral resolution, imaging spectrometer operating in the solar reflective spectral range. Fifteen spectral bands can be selected by ground command. The instrument scans the Earth's surface by the so called 'push-broom' method. Linear CCD arrays provide spatial sampling in the across-track direction, while the satellite's motion provides scanning in the along-track direction. MERIS is designed so that it can acquire data over the Earth whenever illumination conditions are suitable. The instrument's 68.5-degree field-of-view around nadir covers a swath width of 1150 km. This wide field of view is shared between five identical optical modules arranged in a fan shape configuration.",
-            "title": "ENVISAT MERIS Reduced Resolution (RR) Data, version 4",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FENVISAT%2FMERIS%2FL1B%2FRR%2F4",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FENVISAT%2FMERIS%2FL1B%2FRR%2F4",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directaccess/MERIS/L1/",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directaccess/MERIS/L1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/ENVISAT/MERIS/L1B/RR/4",
-                    "description": "MERIS L1B Reduced Resolution (RR) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "MERIS L1B Reduced Resolution (RR) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/ENVISAT/MERIS/L1B/RR/4",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1569867388-OB_DAAC",
+            "issued": "2022-01-31",
+            "keyword": [
+                "ocean optics",
+                "oceans",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ENVISAT/MERIS/L1B/RR/4",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-01-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-03-21T00:00:00Z/2012-05-09T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ENVISAT MERIS Reduced Resolution (RR) Data, version 4"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_California_Ozonesondes_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2022-07-26. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_California_Ozonesondes_Data_1.",
-            "issued": "2021-08-19",
-            "temporal": "2013-01-13T00:00:00Z/2013-02-08T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-07-26",
-            "keyword": [
-                "atmospheric chemistry",
-                "atmosphere",
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
-            "identifier": "C2404262857-LARC_ASDC",
             "description": "DISCOVERAQ_California_Ozonesondes_Data contains data collected via ozonesonde lauches at the Porterville ground site during the California (San Joaquin Valley) deployment of NASA's DISCOVER-AQ field study. This data product contains data for only the California deployment and data collection is complete.\r\n\r\nUnderstanding the factors that contribute to near surface pollution is difficult using only satellite-based observations. The incorporation of surface-level measurements from aircraft and ground-based platforms provides the crucial information necessary to validate and expand upon the use of satellites in understanding near surface pollution. Deriving Information on Surface conditions from Column and Vertically Resolved Observations Relevant to Air Quality (DISCOVER-AQ) was a four-year campaign conducted in collaboration between NASA Langley Research Center, NASA Goddard Space Flight Center, NASA Ames Research Center, and multiple universities to improve the use of satellites to monitor air quality for public health and environmental benefit. Through targeted airborne and ground-based observations, DISCOVER-AQ enabled more effective use of current and future satellites to diagnose ground level conditions influencing air quality.\r\n\r\nDISCOVER-AQ employed two NASA aircraft, the P-3B and King Air, with the P-3B completing in-situ spiral profiling of the atmosphere (aerosol properties, meteorological variables, and trace gas species). The King Air conducted both passive and active remote sensing of the atmospheric column extending below the aircraft to the surface. Data from an existing network of surface air quality monitors, AERONET sun photometers, Pandora UV/vis spectrometers and model simulations were also collected. Further, DISCOVER-AQ employed many surface monitoring sites, with measurements being made on the ground, in conjunction with the aircraft. The B200 and P-3B conducted flights in Baltimore-Washington, D.C. in 2011, Houston, TX in 2013, San Joaquin Valley, CA in 2013, and Denver, CO in 2014. These regions were targeted due to being in violation of the National Ambient Air Quality Standards (NAAQS).\r\n\r\nThe first objective of DISCOVER-AQ was to determine and investigate correlations between surface measurements and satellite column observations for the trace gases ozone (O3), nitrogen dioxide (NO2), and formaldehyde (CH2O) to understand how satellite column observations can diagnose surface conditions. DISCOVER-AQ also had the objective of using surface-level measurements to understand how satellites measure diurnal variability and to understand what factors control diurnal variability. Lastly, DISCOVER-AQ aimed to explore horizontal scales of variability, such as regions with steep gradients and urban plumes.",
-            "title": "DISCOVER-AQ California Deployment Ozonesonde Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDISCOVERAQ_California_Ozonesondes_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDISCOVERAQ_California_Ozonesondes_Data_1",
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
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_California_Ozonesondes_Data_1",
-                    "description": "DOI for DISCOVERAQ_CALIFORNIA_OZONESONDES_DATA_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for DISCOVERAQ_CALIFORNIA_OZONESONDES_DATA_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_California_Ozonesondes_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2404262857-LARC_ASDC",
-                    "description": "Earthdata Search client for DISCOVERAQ_CALIFORNIA_OZONESONDES_DATA_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search client for DISCOVERAQ_CALIFORNIA_OZONESONDES_DATA_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2404262857-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/DISCOVER-AQ/California_Ozonesondes_Data_1/",
-                    "description": "ASDC Direct Data Download for DISCOVERAQ_California_Ozonesondes_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for DISCOVERAQ_California_Ozonesondes_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/DISCOVER-AQ/California_Ozonesondes_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2404262857-LARC_ASDC",
+            "issued": "2021-08-19",
+            "keyword": [
+                "atmospheric chemistry",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_California_Ozonesondes_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-07-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>25.0 -130.0 25.0 -70.0 45.0 -70.0 45.0 -130.0 25.0 -130.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2013-01-13T00:00:00Z/2013-02-08T23:59:59.999Z",
             "theme": [
                 "DISCOVER-AQ",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "DISCOVER-AQ California Deployment Ozonesonde Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/TVJ4MHBED39L",
             "citation": "Global Modeling and Assimilation Office (GMAO). 2015-06-30. M2IUNXGAS. Version 5.12.4. MERRA-2 instU_2d_gas_Nx: 2d,diurnal,Instantaneous,Single-Level,Assimilation,Aerosol Optical Depth Analysis V5.12.4. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/TVJ4MHBED39L. https://disc.gsfc.nasa.gov/datacollection/M2IUNXGAS_5.12.4.html. Digital Science Data.",
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
-                "aerosols",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DANA OSTRENGA",
                 "hasEmail": "mailto:dana.ostrenga@nasa.gov"
             },
+            "creator": "Global Modeling and Assimilation Office (GMAO)",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1276812826-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "M2IUNXGAS (or  instU_3d_gas_Nx) is an instantaneous 2-dimensional monthly diurnal means data collection in Modern-Era Retrospective analysis for Research and Applications version 2 (MERRA-2).  This collection consists of assimilation of aerosol optical depth analysis and aerosol optical depth analysis increment.  It consists of the monthly mean of the data fields every three hour starting from 00:00 UTC, e.g.:  00:00, 03:00, \u2026 , 21:00 UTC. \n\nMERRA-2 is the latest version of global atmospheric reanalysis for the satellite era produced by NASA Global Modeling and Assimilation Office (GMAO) using the Goddard Earth Observing System Model (GEOS) version 5.12.4.  The dataset covers the period of 1980-present with the latency of ~3 weeks after the end of a month. \n\nData Reprocessing:  Please check \u201cRecords of MERRA-2 Data Reprocessing and Service Changes\u201d linked from the \u201cDocumentation\u201d tab on this page.  Note that a reprocessed data filename is different from the original file.\n\nMERRA-2 Mailing List: Sign up to receive information on reprocessing of data, changing of tools and services, as well as data announcements from GMAO. Contact the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov) to be added to the list.\n\nQuestions: If you have a question, please read \"MERRA-2 File Specification Document\",  \u201cMERRA-2 Data Access \u2013 Quick Start Guide\u201d, and FAQs linked from the \u201dDocumentation\u201d tab on this page.  If that does not answer your question, you may email the question on data access to the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov), or the question on science to the MERRA-2 science team (merra-questions@lists.nasa.gov).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "M2IUNXGAS",
-            "creator": "Global Modeling and Assimilation Office (GMAO)",
-            "graphic-preview-description": "M2IUNXGAS variable",
-            "title": "MERRA-2 instU_2d_gas_Nx: 2d,diurnal,Instantaneous,Single-Level,Assimilation,Aerosol Optical Depth Analysis 0.625 x 0.5 degree V5.12.4 (M2IUNXGAS) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2IUNXGAS_5.12.4.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTVJ4MHBED39L",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTVJ4MHBED39L",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2IUNXGAS_5.12.4.png",
-                    "description": "M2IUNXGAS variable",
                     "@type": "dcat:Distribution",
+                    "description": "M2IUNXGAS variable",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2IUNXGAS_5.12.4.png",
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
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2IUNXGAS_5.12.4.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2IUNXGAS_5.12.4.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_DIURNAL/M2IUNXGAS.5.12.4/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_DIURNAL/M2IUNXGAS.5.12.4/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2IUNXGAS",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2IUNXGAS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/dods/M2IUNXGAS.info",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/dods/M2IUNXGAS.info",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2_DIURNAL/M2IUNXGAS.5.12.4/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2_DIURNAL/M2IUNXGAS.5.12.4/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_DIURNAL_aggregation/catalog.html?dataset=merra2_diurnal_aggregation%2FM2IUNXGAS.5.12.4_Aggregation.ncml",
-                    "description": "Time aggregated THREDDS Data Server (TDS) ",
                     "@type": "dcat:Distribution",
+                    "description": "Time aggregated THREDDS Data Server (TDS) ",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_DIURNAL_aggregation/catalog.html?dataset=merra2_diurnal_aggregation%2FM2IUNXGAS.5.12.4_Aggregation.ncml",
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
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_DIURNAL/M2IUNXGAS.5.12.4/doc/MERRA2.README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_DIURNAL/M2IUNXGAS.5.12.4/doc/MERRA2.README.pdf",
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
+            "graphic-preview-description": "M2IUNXGAS variable",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2IUNXGAS_5.12.4.png",
+            "identifier": "C1276812826-GES_DISC",
+            "issued": "2007-06-14",
+            "keyword": [
+                "earth science",
+                "aerosols",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/TVJ4MHBED39L",
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
+            "series-name": "M2IUNXGAS",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1980-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "MERRA-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MERRA-2 instU_2d_gas_Nx: 2d,diurnal,Instantaneous,Single-Level,Assimilation,Aerosol Optical Depth Analysis 0.625 x 0.5 degree V5.12.4 (M2IUNXGAS) at GES DISC"
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
-                "radio science",
-                "pds",
-                "grs",
-                "spice",
-                "themis"
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
-            "identifier": "NASA-457",
             "description": "GRS, RADIO SCIENCE (Releases 136-138), SPICE, THEMIS",
-            "title": "PDS Odyssey Data Release 46",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -106636,20 +106614,54 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-457",
+            "issued": "2018-06-25",
+            "keyword": [
+                "radio science",
+                "pds",
+                "grs",
+                "spice",
+                "themis"
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
+            "title": "PDS Odyssey Data Release 46"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/3vrm-5u9n",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Gerald Steeman",
+                "hasEmail": "mailto:Gerald.Steeman@nasa.gov"
+            },
+            "description": "The NTRS is a valuable resource for researchers, students, educators, and the public to access NASA's current and historical technical literature and engineering results. Over 500,000 aerospace-related citations, over 200,000 full-text online documents, and over 500,000 images and videos are available. NTRS content continues to grow as new scientific and technical information (STI) is created or funded by NASA. The types of information found in the NTRS include: conference papers, journal articles, meeting papers, patents, research reports, images, movies, and technical videos.  NTRS is&#160;Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH) enabled",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://nix.nasa.gov/",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000091",
             "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "ntrs",
                 "aeronautics",
@@ -106670,304 +106682,269 @@
                 "sti",
                 "technical reports"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Gerald Steeman",
-                "hasEmail": "mailto:Gerald.Steeman@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/3vrm-5u9n",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:046"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000091",
-            "description": "The NTRS is a valuable resource for researchers, students, educators, and the public to access NASA's current and historical technical literature and engineering results. Over 500,000 aerospace-related citations, over 200,000 full-text online documents, and over 500,000 images and videos are available. NTRS content continues to grow as new scientific and technical information (STI) is created or funded by NASA. The types of information found in the NTRS include: conference papers, journal articles, meeting papers, patents, research reports, images, movies, and technical videos.  NTRS is&#160;Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH) enabled",
-            "title": "NASA Technical Reports Server (NTRS)",
-            "programCode": [
-                "026:046"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://nix.nasa.gov/",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "NASA Technical Reports Server (NTRS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/QTDN06JJU27T",
             "citation": "Global Modeling and Assimilation Office (GMAO). 2022-11-08. M2TCNPLTM. Version 2. MERRA-2 tavgC_3d_ltm_Np: 3d, Long Term Mean 3-Dimensional Meteorological Fields based on 1991-2020 V2. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/QTDN06JJU27T. https://disc.gsfc.nasa.gov/datacollection/M2TCNPLTM_2.html. Digital Science Data.",
-            "issued": "2022-11-01",
-            "temporal": "1991-01-01T00:00:00Z/2020-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-11-01",
-            "references": [
-                "https://doi.org/10.1175/JCLI-D-16-0758.1"
-            ],
-            "keyword": [
-                "atmospheric winds",
-                "atmosphere",
-                "atmospheric temperature",
-                "earth science",
-                "altitude",
-                "atmospheric water vapor"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Xiaohua Pan",
                 "hasEmail": "mailto:xiaohua.pan@nasa.gov"
             },
+            "creator": "Global Modeling and Assimilation Office (GMAO)",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2531964023-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "M2TCNPLTM (or tavgC_3d_ltm_Np) is a 3-dimensional monthly data collection for climatological long term mean and standard deviation representing the interannual variability on a monthly timescale, derived from monthly Modern-Era Retrospective analysis for Research and Applications version 2 (MERRA-2) datasets. V2 of this data collection is calculated with data from January 1991 to December 2020. In contrast, V1, the original version, is computed with data from an earlier 30-year time of 1981-2010.\n\nThis collection consists of meteorological diagnostics at 12 vertical pressure levels (e.g.,850 hPa, 500hPa, and 200 hPa), such as air temperature, wind components, and both relative and specific humidity. \n\nMERRA-2 is the latest version of global atmospheric reanalysis for the satellite era produced by the NASA Global Modeling and Assimilation Office (GMAO) using the Goddard Earth Observing System Model (GEOS) version 5.12.4. The dataset covers the period of 1980-present, with a  latency of ~3 weeks after the end of the previous month.\n\nData Reprocessing: Please check \u201cRecords of MERRA-2 Data Reprocessing and Service Changes\u201d,  linked from the \u201cDocumentation\u201d tab on this page. Note that a reprocessed data filename is different from the original filename.\n\nMERRA-2 Mailing List: Sign up to receive information on reprocessing of data, changes to tools and services, as well as data announcements from GMAO. Contact the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov) to be added to the list.\n\nQuestions: If you have a question, please read the \"MERRA-2 File Specification Document'', \u201cMERRA-2 Data Access \u2013 Quick Start Guide\u201d, and FAQs linked from the \u201dDocumentation\u201d tab on this page for more information. If these documents  do not answer your question, you may email the question on data access to the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov), or the question on science to the MERRA-2 science team (merra-questions@lists.nasa.gov)",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "M2TCNPLTM",
-            "creator": "Global Modeling and Assimilation Office (GMAO)",
-            "graphic-preview-description": "M2TCNPLTM sample image: Monthly climatology of relative humidity after moist (RH) at 700hPa, Jan.   The base period of the climatology is 1991-2020.",
-            "title": "MERRA-2 tavgC_3d_ltm_Np: 3d, Long Term Mean 3-Dimensional Meteorological Fields based on 1991-2020 V2 (M2TCNPLTM) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2TCNPLTM_2.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FQTDN06JJU27T",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FQTDN06JJU27T",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2TCNPLTM_2.png",
-                    "description": "M2TCNPLTM sample image: Monthly climatology of relative humidity after moist (RH) at 700hPa, Jan.   The base period of the climatology is 1991-2020.",
                     "@type": "dcat:Distribution",
+                    "description": "M2TCNPLTM sample image: Monthly climatology of relative humidity after moist (RH) at 700hPa, Jan.   The base period of the climatology is 1991-2020.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2TCNPLTM_2.png",
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
-                    "downloadURL": "https://gmao.gsfc.nasa.gov/pubs/docs/Collow1437.pdf",
-                    "description": "File Specification Document",
                     "@type": "dcat:Distribution",
+                    "description": "File Specification Document",
+                    "downloadURL": "https://gmao.gsfc.nasa.gov/pubs/docs/Collow1437.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2TCNPLTM_2.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2TCNPLTM_2.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_CLIM/M2TCNPLTM.2/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_CLIM/M2TCNPLTM.2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2TCNPLTM_2",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2TCNPLTM_2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2_CLIM/M2TCNPLTM.2/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2_CLIM/M2TCNPLTM.2/contents.html",
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
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_CLIM/M2TCNPLTM.2/doc/README_MERRA2_CLIMSTAT_V2.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_CLIM/M2TCNPLTM.2/doc/README_MERRA2_CLIMSTAT_V2.pdf",
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
+            "graphic-preview-description": "M2TCNPLTM sample image: Monthly climatology of relative humidity after moist (RH) at 700hPa, Jan.   The base period of the climatology is 1991-2020.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2TCNPLTM_2.png",
+            "identifier": "C2531964023-GES_DISC",
+            "issued": "2022-11-01",
+            "keyword": [
+                "atmospheric winds",
+                "atmosphere",
+                "atmospheric temperature",
+                "earth science",
+                "altitude",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://doi.org/10.5067/QTDN06JJU27T",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-11-01",
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
+            "series-name": "M2TCNPLTM",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1991-01-01T00:00:00Z/2020-12-31T23:59:59.999Z",
             "theme": [
                 "MERRA-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MERRA-2 tavgC_3d_ltm_Np: 3d, Long Term Mean 3-Dimensional Meteorological Fields based on 1991-2020 V2 (M2TCNPLTM) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1133",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Long, C.M., and T.M. Pavelsky. 2012. Water Quality and Spectral Reflectance, Peace-Athabasca Delta, Canada, 2010-2011. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1133",
-            "issued": "2012-10-24",
-            "temporal": "2010-06-21T00:00:00Z/2011-07-06T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-24",
-            "keyword": [
-                "water quality/water chemistry",
-                "earth science",
-                "land surface",
-                "surface radiative properties",
-                "surface water",
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
-            "identifier": "C2756238692-ORNL_CLOUD",
             "description": "The Peace-Athabasca Delta (PAD) is a hydrologically complex and ecologically diverse freshwater delta formed by the confluence of the Peace, Athabasca, and Birch Rivers near the western end of Lake Athabasca, Alberta, Canada. This data set includes 3 comma-delimited ASCII files: one containing water quality data and site characteristics from June and July 2010, a second containing water quality data and site characteristics for June and July 2011, and a third containing spectral reflectance of the water surface for 2011. The 2010 data file has measurements from 62 unique sites, the majority of which were revisited in 2011. Both of the 2011 data files have measurements from 99 unique sites visited 1-4 times.",
-            "graphic-preview-description": "Map of the central PAD showing locations for water quality and reflectance data collection in 2011.",
-            "title": "Water Quality and Spectral Reflectance, Peace-Athabasca Delta, Canada, 2010-2011",
-            "graphic-preview-file": "https://daac.ornl.gov/HYDROCLIMATOLOGY/guides/PAD_2011_Location_Map.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1133",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1133",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/global_hydroclimatology/PAD_2011/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/global_hydroclimatology/PAD_2011/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/HYDROCLIMATOLOGY/guides/PAD_2011.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/HYDROCLIMATOLOGY/guides/PAD_2011.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1133",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1133",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_hydroclimatology/PAD_2011/comp/PAD_2011.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_hydroclimatology/PAD_2011/comp/PAD_2011.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/HYDROCLIMATOLOGY/guides/PAD_2011_Location_Map.jpg",
-                    "description": "Map of the central PAD showing locations for water quality and reflectance data collection in 2011.",
                     "@type": "dcat:Distribution",
+                    "description": "Map of the central PAD showing locations for water quality and reflectance data collection in 2011.",
+                    "downloadURL": "https://daac.ornl.gov/HYDROCLIMATOLOGY/guides/PAD_2011_Location_Map.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Map of the central PAD showing locations for water quality and reflectance data collection in 2011.",
+            "graphic-preview-file": "https://daac.ornl.gov/HYDROCLIMATOLOGY/guides/PAD_2011_Location_Map.jpg",
+            "identifier": "C2756238692-ORNL_CLOUD",
+            "issued": "2012-10-24",
+            "keyword": [
+                "water quality/water chemistry",
+                "earth science",
+                "land surface",
+                "surface radiative properties",
+                "surface water",
+                "terrestrial hydrosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1133",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-08-24",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-111.93 58.39 -110.84 58.99",
+            "temporal": "2010-06-21T00:00:00Z/2011-07-06T23:59:59Z",
             "theme": [
                 "Hydroclimatology",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Water Quality and Spectral Reflectance, Peace-Athabasca Delta, Canada, 2010-2011"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2179081510-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "GPM Science Team. 2021-12-10. GPM_2ADPRENV. Version 07. GPM DPR L2A Environment 1.5 hours 5 km V07. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Goddard Earth Science Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/GPM_2ADPRENV_07.html. Digital Science Data.",
-            "issued": "2021-12-06",
-            "temporal": "2014-03-08T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-12-06",
-            "keyword": [
-                "atmospheric water vapor",
-                "atmosphere",
-                "precipitation",
-                "earth science"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "GEORGE HUFFMAN",
                 "hasEmail": "mailto:George.J.Huffman@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C2179081510-GES_DISC",
-            "description": "Version 07 is the current version of the data set. Older versions will no longer be available and have been superseded by Version 07.\n.\n\nThis is environmental data that includes the profiles of atmospheric parameters assumed in the L2 retrieval algorithm.\n\nThis GPM data type provides single- and dual-frequency-derived precipitation estimates from the Ku and Ka radars of the Dual-Frequency Precipitation Radar (DPR) on the core GPM spacecraft. The output consists of three main classes of precipitation products derived from the: \n+ the Ku-band frequency over a wide swath (245 km);\n+ the Ka-band frequency over a narrow swath (125 km), and\n+ the dual-frequency data over the narrow swath. \n\nThe Ka-band results are further divided into the standard and high-sensitivity estimates. In the standard sensitivity mode, the fields of view within the inner swath are matched to those of the Ku-band. Data from these matched-beam Ku- and Ka-band fields of view are used to derive the dual-frequency precipitation products. The retrievals are performed at each radar range bin along the slant path of the radar instrument field of view (IFOV). \n\nThe dual-frequency retrieval benefits from having co-aligned measurements at Ku- and Ka-bands. Data from these measurements are used to infer properties of the particle size distribution, which are expected to lead to improved estimates of rainfall rate and equivalent liquid water content. Dual-frequency data are expected to improve the capability to discriminate among water, ice, and mixed-phase hydrometeors as a function of height. This capability is particularly important in convective storms where a bright-band signature, associated with mixed-phase hydrometeors, is usually not detectable. In addition, the different attenuation rates of the Ku- and Ka-bands allow differential attenuation techniques to be used to estimate the path integrated attenuation. The high-sensitivity Ka-band channel is expected to have 6 dB greater sensitivity than the Ku- and standard Ka-band channels and to provide enhanced detection capabilities at the light rainfall rates.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "GPM_2ADPRENV",
             "creator": "GPM Science Team",
-            "title": "GPM DPR L2A Environment 1.5 hours 5 km V07 (GPM_2ADPRENV) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_2ADPRENV.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Version 07 is the current version of the data set. Older versions will no longer be available and have been superseded by Version 07.\n.\n\nThis is environmental data that includes the profiles of atmospheric parameters assumed in the L2 retrieval algorithm.\n\nThis GPM data type provides single- and dual-frequency-derived precipitation estimates from the Ku and Ka radars of the Dual-Frequency Precipitation Radar (DPR) on the core GPM spacecraft. The output consists of three main classes of precipitation products derived from the: \n+ the Ku-band frequency over a wide swath (245 km);\n+ the Ka-band frequency over a narrow swath (125 km), and\n+ the dual-frequency data over the narrow swath. \n\nThe Ka-band results are further divided into the standard and high-sensitivity estimates. In the standard sensitivity mode, the fields of view within the inner swath are matched to those of the Ku-band. Data from these matched-beam Ku- and Ka-band fields of view are used to derive the dual-frequency precipitation products. The retrievals are performed at each radar range bin along the slant path of the radar instrument field of view (IFOV). \n\nThe dual-frequency retrieval benefits from having co-aligned measurements at Ku- and Ka-bands. Data from these measurements are used to infer properties of the particle size distribution, which are expected to lead to improved estimates of rainfall rate and equivalent liquid water content. Dual-frequency data are expected to improve the capability to discriminate among water, ice, and mixed-phase hydrometeors as a function of height. This capability is particularly important in convective storms where a bright-band signature, associated with mixed-phase hydrometeors, is usually not detectable. In addition, the different attenuation rates of the Ku- and Ka-bands allow differential attenuation techniques to be used to estimate the path integrated attenuation. The high-sensitivity Ka-band channel is expected to have 6 dB greater sensitivity than the Ku- and standard Ka-band channels and to provide enhanced detection capabilities at the light rainfall rates.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -106976,170 +106953,205 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_2ADPRENV_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_2ADPRENV_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L2/GPM_2ADPRENV.07/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L2/GPM_2ADPRENV.07/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_2ADPRENV_07",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_2ADPRENV_07",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L2/GPM_2ADPRENV.07/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L2/GPM_2ADPRENV.07/contents.html",
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
-                    "downloadURL": "https://pps.gsfc.nasa.gov/Documents/ReleaseNote_DPRL2L3_productV07A_20211117.pdf",
-                    "description": "Release Notes",
                     "@type": "dcat:Distribution",
+                    "description": "Release Notes",
+                    "downloadURL": "https://pps.gsfc.nasa.gov/Documents/ReleaseNote_DPRL2L3_productV07A_20211117.pdf",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_2ADPRENV.png",
+            "identifier": "C2179081510-GES_DISC",
+            "issued": "2021-12-06",
+            "keyword": [
+                "atmospheric water vapor",
+                "atmosphere",
+                "precipitation",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2179081510-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-12-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "GPM_2ADPRENV",
             "spatial": "-180.0 -70.0 180.0 70.0",
+            "temporal": "2014-03-08T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "GPM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM DPR L2A Environment 1.5 hours 5 km V07 (GPM_2ADPRENV) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-CAL-CONSERT-2-MARS-V2.0",
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
+            "description": "This archive contains edited data from the CONSERT instrument onboard ROSETTA Orbiter and Lander, acquired during the MARS (Mars fly-by) phase. It also contains documentation which describes the CONSERT experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.  This data set supersedes RO/RL-M-CONSERT-2-MARS-V1.0.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-cal-consert-2-mars-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "calibration"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-CAL-CONSERT-2-MARS-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-cal-consert-2-mars-v2.0",
-            "description": "This archive contains edited data from the CONSERT instrument onboard ROSETTA Orbiter and Lander, acquired during the MARS (Mars fly-by) phase. It also contains documentation which describes the CONSERT experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.  This data set supersedes RO/RL-M-CONSERT-2-MARS-V1.0.",
-            "title": "ROSETTA-ORBITER/ROSETTA-LANDER CAL\n                           CONSERT 2 MARS V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER/ROSETTA-LANDER CAL\n                           CONSERT 2 MARS V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DII-C-ITS-2-9P-ENCOUNTER-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains raw 9P/Tempel 1 and science calibration images acquired by the Deep Impact Impactor Targeting Sensor Visible CCD during the 9P encounter phase of the mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dii-c-its-2-9p-encounter-v1.0_3vut-txbj",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "deep impact",
                 "9p/tempel 1 (1867 g1)",
                 "calibration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DII-C-ITS-2-9P-ENCOUNTER-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dii-c-its-2-9p-encounter-v1.0_3vut-txbj",
-            "description": "This data set contains raw 9P/Tempel 1 and science calibration images acquired by the Deep Impact Impactor Targeting Sensor Visible CCD during the 9P encounter phase of the mission.",
-            "title": "DEEP IMPACT 9P/TEMPEL ENCOUNTER - RAW ITS DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "DEEP IMPACT 9P/TEMPEL ENCOUNTER - RAW ITS DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/3vxg-rtfp",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Kim Tolbert",
+                "hasEmail": "mailto:kim.tolbert@nasa.gov"
+            },
+            "describedBy": "http://hesperia.gsfc.nasa.gov/fermi/lat/qlook/LAT_qlook_plots.htm",
+            "description": "LAT solar gamma-ray flux > 100 MeV, one point per solar exposure (i.e. average of the 20-40 minutes of solar observation every ~1.5 hours) calculated by two different methods.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://hesperia.gsfc.nasa.gov/fermi/lat/qlook/max_likelihood/",
+                    "mediaType": "image/png"
+                }
+            ],
+            "identifier": "NASA-0000247__2",
             "issued": "2018-06-25",
-            "temporal": "2008-08-12/2014-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "solar",
                 "gbo",
@@ -107149,476 +107161,478 @@
                 "telescope",
                 "gbm"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kim Tolbert",
-                "hasEmail": "mailto:kim.tolbert@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/3vxg-rtfp",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000247__2",
-            "description": "LAT solar gamma-ray flux > 100 MeV, one point per solar exposure (i.e. average of the 20-40 minutes of solar observation every ~1.5 hours) calculated by two different methods.",
-            "title": "LAT 4-day Quicklook Plots",
-            "programCode": [
-                "026:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://hesperia.gsfc.nasa.gov/fermi/lat/qlook/max_likelihood/",
-                    "mediaType": "image/png"
-                }
-            ],
-            "describedBy": "http://hesperia.gsfc.nasa.gov/fermi/lat/qlook/LAT_qlook_plots.htm",
-            "accrualPeriodicity": "irregular",
+            "temporal": "2008-08-12/2014-01-01",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "LAT 4-day Quicklook Plots"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-ASE-2-EDL-V1.0",
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
-                "phoenix"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Unknown",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-ase-2-edl-v1.0_3vz5-grwy",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "phoenix"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-ASE-2-EDL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-ase-2-edl-v1.0_3vz5-grwy",
-            "description": "Unknown",
-            "title": "PHOENIX MARS ATMOSPHERIC STRUCTURE EXPERIMENT DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "PHOENIX MARS ATMOSPHERIC STRUCTURE EXPERIMENT DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/730",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Holland, E.A., B.H. Braswell, J.M. Sulzman, and J.-F. Lamarque. 2004. Nitrogen Deposition onto the United States and Western Europe. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/730",
-            "issued": "2023-10-02",
-            "temporal": "1987-01-01T00:00:00Z/1994-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-03",
-            "keyword": [
-                "earth science",
-                "atmospheric chemistry",
-                "biosphere",
-                "ecological dynamics",
-                "environmental impacts",
-                "human dimensions",
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
-            "identifier": "C2776873201-ORNL_CLOUD",
             "description": "This data set contains data for wet and dry nitrogen-species deposition for the United States and Western Europe. Deposition data were acquired directly from monitoring programs in the United States and Europe for time periods from 1978-1994 for wet deposition and from 1989-1994 for dry deposition and evaluated using similar quality assurance criteria to ensure comparability. A standard geostatistical method (kriging) was used to interpolate data onto a 0.5 x 0.5 degree resolution map for wet and dry deposition.",
-            "graphic-preview-description": "Browse Image",
-            "title": "Nitrogen Deposition onto the United States and Western Europe",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/730_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F730",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F730",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/global_climate/nitrogen_deposition/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/global_climate/nitrogen_deposition/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/CLIMATE/guides/nitrogen_deposition.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/CLIMATE/guides/nitrogen_deposition.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/730",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/730",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_climate/nitrogen_deposition/comp/CASTNET_Network_summary.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_climate/nitrogen_deposition/comp/CASTNET_Network_summary.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_climate/nitrogen_deposition/comp/EMEP_cccr1-95rev.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_climate/nitrogen_deposition/comp/EMEP_cccr1-95rev.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_climate/nitrogen_deposition/comp/NADP-QMP-Dec2003.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_climate/nitrogen_deposition/comp/NADP-QMP-Dec2003.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_climate/nitrogen_deposition/comp/nitrogen_deposition.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_climate/nitrogen_deposition/comp/nitrogen_deposition.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_climate/nitrogen_deposition/comp/N_Deposition_Maps_20040917.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_climate/nitrogen_deposition/comp/N_Deposition_Maps_20040917.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/730_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/730_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=730",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=730",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/730/catalog.html",
-                    "description": "The THREDDS location for this Collection.",
                     "@type": "dcat:Distribution",
+                    "description": "The THREDDS location for this Collection.",
+                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/730/catalog.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/730_1_fit.png",
+            "identifier": "C2776873201-ORNL_CLOUD",
+            "issued": "2023-10-02",
+            "keyword": [
+                "earth science",
+                "atmospheric chemistry",
+                "biosphere",
+                "ecological dynamics",
+                "environmental impacts",
+                "human dimensions",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/730",
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
             "spatial": "-124.0 25.0 44.5 70.5",
+            "temporal": "1987-01-01T00:00:00Z/1994-12-31T23:59:59Z",
             "theme": [
                 "Climate",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Nitrogen Deposition onto the United States and Western Europe"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSIWAC-3-CVP-COMMISSIONING-V1.4",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera during the COMMISSIONING mission phase",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osiwac-3-cvp-commissioning-v1.4_3w4a-h2k6",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "eps aqr",
                 "calibration",
                 "m42"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSIWAC-3-CVP-COMMISSIONING-V1.4",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osiwac-3-cvp-commissioning-v1.4_3w4a-h2k6",
-            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera during the COMMISSIONING mission phase",
-            "title": "ROSETTA-ORBITER COMMISSIONING OSIWAC 3 RDR V1.4",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER COMMISSIONING OSIWAC 3 RDR V1.4"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/PELICAN_PCO2/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/PELICAN_PCO2/DATA001.",
-            "issued": "2006-04-27",
-            "temporal": "2006-04-27T19:20:00Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "oceans",
-                "salinity/density",
-                "ocean temperature",
-                "ocean optics",
-                "ocean chemistry",
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
-            "identifier": "C1633360591-OB_DAAC",
             "description": "Measurements from the Pelican research vessel made off the southern coast of Louisiana in the Gulf of Mexico from 2006.",
-            "title": "Partial pressure of carbon dioxide (PCO2) onboard the Pelican research vessel",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FPELICAN_PCO2%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FPELICAN_PCO2%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Pelican_PCO2/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Pelican_PCO2/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360591-OB_DAAC",
+            "issued": "2006-04-27",
+            "keyword": [
+                "oceans",
+                "salinity/density",
+                "ocean temperature",
+                "ocean optics",
+                "ocean chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/PELICAN_PCO2/DATA001",
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
+            "temporal": "2006-04-27T19:20:00Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Partial pressure of carbon dioxide (PCO2) onboard the Pelican research vessel"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1666",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Rocha, A.V., and K.S. Wright. 2019. ABoVE: MODIS- and CCAN-Derived NDVI and Trends, North Slope of Alaska, 2000-2015. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1666",
-            "issued": "2019-02-26",
-            "temporal": "2000-01-01T00:00:00Z/2015-12-31T11:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "national geospatial data asset",
-                "biosphere",
-                "earth science",
-                "ecological dynamics",
-                "ngda",
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
-            "identifier": "C2170972734-ORNL_CLOUD",
             "description": "This dataset provides the average Normalized Difference Vegetation Index (NDVI) at 1-km resolution over the north slope of Alaska, USA, for the growing season (June-August) of each year from 2000-2015, and NDVI trends for the same period. The dataset presents growing-season averages and trends from two sources: 1) derived from 1-km, 8-day data from the Moderate Resolution Imaging Spectroradiometer (MODIS) NDVI (MOD13A2) product, and 2) predicted by the Coupled Carbon and Nitrogen model (CCaN). CCaN is a mass balance carbon and nitrogen model that was driven by 1-km MODIS surface temperature and climate data for the North Slope of Alaska and parameterized using model-data fusion, where model predictions were ecologically constrained with historical ecological ground and satellite-based data.",
-            "graphic-preview-description": "MODIS (A) and CCaN (B) average growing season NDVI. From Figure 2 of Rocha et al. (2018).",
-            "title": "ABoVE: MODIS- and CCAN-Derived NDVI and Trends, North Slope of Alaska, 2000-2015",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/MODIS_CCaN_NDVI_Trends_Alaska_Fig1.PNG",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1666",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1666",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/MODIS_CCaN_NDVI_Trends_Alaska/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/MODIS_CCaN_NDVI_Trends_Alaska/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/MODIS_CCaN_NDVI_Trends_Alaska.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/MODIS_CCaN_NDVI_Trends_Alaska.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1666",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1666",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/MODIS_CCaN_NDVI_Trends_Alaska/comp/MODIS_CCaN_NDVI_Trends_Alaska.pdf",
-                    "description": "ABoVE: MODIS- and CCAN-Derived NDVI and Trends, North Slope of Alaska, 2000-2015: MODIS_CCaN_NDVI_Trends_Alaska.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: MODIS- and CCAN-Derived NDVI and Trends, North Slope of Alaska, 2000-2015: MODIS_CCaN_NDVI_Trends_Alaska.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/MODIS_CCaN_NDVI_Trends_Alaska/comp/MODIS_CCaN_NDVI_Trends_Alaska.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/MODIS_CCaN_NDVI_Trends_Alaska_Fig1.PNG",
-                    "description": "MODIS (A) and CCaN (B) average growing season NDVI. From Figure 2 of Rocha et al. (2018).",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS (A) and CCaN (B) average growing season NDVI. From Figure 2 of Rocha et al. (2018).",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/MODIS_CCaN_NDVI_Trends_Alaska_Fig1.PNG",
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
+            "graphic-preview-description": "MODIS (A) and CCaN (B) average growing season NDVI. From Figure 2 of Rocha et al. (2018).",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/MODIS_CCaN_NDVI_Trends_Alaska_Fig1.PNG",
+            "identifier": "C2170972734-ORNL_CLOUD",
+            "issued": "2019-02-26",
+            "keyword": [
+                "national geospatial data asset",
+                "biosphere",
+                "earth science",
+                "ecological dynamics",
+                "ngda",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1666",
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
             "spatial": "-166.85 66.99 -140.98 71.38",
+            "temporal": "2000-01-01T00:00:00Z/2015-12-31T11:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE: MODIS- and CCAN-Derived NDVI and Trends, North Slope of Alaska, 2000-2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/DORIS/DORIS_IDSORB_001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "IDS Orbit product, Greenbelt, MD, U.S.A: NASA Crustal Dynamics Data Information System (CDDIS), Accessed [[enter user data access date]] at doi: 10.5067/DORIS/DORIS_IDSORB_001",
-            "issued": "1993-01-01",
-            "temporal": "1992-01-01T00:00:00Z/2025-01-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-07",
-            "keyword": [
-                "earth science",
-                "solid earth",
-                "geodetics",
-                "gravity/gravitational field",
-                "tectonics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Benjamin Michael",
                 "hasEmail": "mailto:benjamin.p.patrick@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "CDDIS"
-            },
-            "identifier": "C1602851234-CDDIS",
             "description": "Doppler Orbitography by Radiopositioning Integrated on Satellite (DORIS) Satellite Orbit Product from the NASA Crustal Dynamics Data Information System (CDDIS). DORIS is a dual-frequency Doppler system consisting of a receiver flying aboard a satellite and a globally distributed network of ground beacons. The DORIS receiver on-board the orbiting satellite tracks the dual-frequency radio signals transmitted by the network of ground beacons and generates the DORIS data. A measurement is made of either the Doppler shift or absolute phase as the satellite\u2019s orbit moves over the ground-based beacon. DORIS data records contain a time-tagged range-rate measurement with associated ancillary information. DORIS observations from a global network can be utilized for a variety of products. Analysis Centers (ACs) of the International DORIS Service (IDS) retrieve DORIS data on a regular basis to compute various DORIS products from data generated by the DORIS beacons supporting the IDS network. These products include orbits of satellites with DORIS receivers onboard. These orbit products are available in SP1 or SP3 orbit format.",
-            "title": "Ground-Based Doppler Orbitography by Radiopositioning Integrated on Satellite (DORIS) Satellite Orbit Product from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FDORIS%2FDORIS_IDSORB_001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FDORIS%2FDORIS_IDSORB_001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/archive/doris/products/orbits",
-                    "description": "URL for retrieval of DORIS products through https",
                     "@type": "dcat:Distribution",
+                    "description": "URL for retrieval of DORIS products through https",
+                    "downloadURL": "https://cddis.nasa.gov/archive/doris/products/orbits",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/DORIS/DORIS_product_holdings.html",
-                    "description": "URL for more information about DORIS products",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about DORIS products",
+                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/DORIS/DORIS_product_holdings.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://doi.org/10.5067/DORIS/DORIS_IDSORB_001",
-                    "description": "URL for more information about DORIS products",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about DORIS products",
+                    "downloadURL": "http://doi.org/10.5067/DORIS/DORIS_IDSORB_001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1602851234-CDDIS",
+            "issued": "1993-01-01",
+            "keyword": [
+                "earth science",
+                "solid earth",
+                "geodetics",
+                "gravity/gravitational field",
+                "tectonics"
+            ],
+            "landingPage": "https://doi.org/10.5067/DORIS/DORIS_IDSORB_001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-07",
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
                 "IDS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Ground-Based Doppler Orbitography by Radiopositioning Integrated on Satellite (DORIS) Satellite Orbit Product from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/3w6m-cwd9",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Gene expression levels were determined in 3rd instar and adult Drosophila melanogaster reared during spaceflight to elucidate the genetic and molecular mechanisms underpinning the effects of microgravity on the immune system. The goal was to validate the Drosophila model for understanding alterations of innate immune responses in humans due to spaceflight. Five containers of flies with ten female and five male fruit flies in each container were housed and bred on the space shuttle (average orbit altitude of 330.35 km) for 12 days and 18.5 hours with a new generation reared in microgravity. RNA was extracted on the day of shuttle landing from whole body animals (3rd instar larvae and adults) hybridized to Drosophila 2.0 Affymetrix genome arrays and the expression level of all genes was normalized against the gene expression level from the corresponding developmental stage animals raised on ground. Spaceflight altered the expression of larval genes involved in the maturation of plasmatocytes (macrophages) and their phagocytic response as well as the level of constitutive expression of pattern recognition receptors and opsonins that specifically recognize bacteria and of lysozymes antimicrobial peptide pathway and immune stress genes hallmarks of humoral immunity. Larval microarrays (FL 6 samples) are based on RNA extracted from 6 independent sets of 50 mid 3rd instar larvae reared in microgravity and collected on the day of landing after 12 days and 18.5 hours on the space shuttle and the same number of control larvae raised on ground (GL 6 samples). Adults microarrays (F1 3 samples) are based on RNA from 3 sets of 20 adult females each that emerged during spaceflight and within 4 hours of landing and the same number of adult females from the corresponding ground control containers (G1 3 samples).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-3",
+                    "mediaType": "text/html",
+                    "title": "Drosophila melanogaster gene expression changes after spaceflight."
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-3_3w6m-cwd9",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "developmental stage",
                 "feature_extraction",
@@ -107638,45 +107652,42 @@
                 "p-gse23880-2",
                 "radiation dosimetry"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/3w6m-cwd9",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-3_3w6m-cwd9",
-            "description": "Gene expression levels were determined in 3rd instar and adult Drosophila melanogaster reared during spaceflight to elucidate the genetic and molecular mechanisms underpinning the effects of microgravity on the immune system. The goal was to validate the Drosophila model for understanding alterations of innate immune responses in humans due to spaceflight. Five containers of flies with ten female and five male fruit flies in each container were housed and bred on the space shuttle (average orbit altitude of 330.35 km) for 12 days and 18.5 hours with a new generation reared in microgravity. RNA was extracted on the day of shuttle landing from whole body animals (3rd instar larvae and adults) hybridized to Drosophila 2.0 Affymetrix genome arrays and the expression level of all genes was normalized against the gene expression level from the corresponding developmental stage animals raised on ground. Spaceflight altered the expression of larval genes involved in the maturation of plasmatocytes (macrophages) and their phagocytic response as well as the level of constitutive expression of pattern recognition receptors and opsonins that specifically recognize bacteria and of lysozymes antimicrobial peptide pathway and immune stress genes hallmarks of humoral immunity. Larval microarrays (FL 6 samples) are based on RNA extracted from 6 independent sets of 50 mid 3rd instar larvae reared in microgravity and collected on the day of landing after 12 days and 18.5 hours on the space shuttle and the same number of control larvae raised on ground (GL 6 samples). Adults microarrays (F1 3 samples) are based on RNA from 3 sets of 20 adult females each that emerged during spaceflight and within 4 hours of landing and the same number of adult females from the corresponding ground control containers (G1 3 samples).",
-            "title": "Drosophila melanogaster gene expression changes after spaceflight.",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-3",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Drosophila melanogaster gene expression changes after spaceflight."
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Drosophila melanogaster gene expression changes after spaceflight."
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/3w83-83pw",
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
+                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_lid_l1-valstage1-v3-02_table",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000191",
             "issued": "2018-06-25",
-            "temporal": "2011-11-01/2013-02-28",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "satellite",
                 "climate",
@@ -107686,190 +107697,190 @@
                 "aerosol",
                 "radiation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John M. Kusterer",
-                "hasEmail": "mailto:john.m.kusterer@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/3w83-83pw",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:004"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000191",
-            "description": "Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) was launched on April 28, 2006 to study the impact of clouds and aerosols on the Earth\u2019s radiation budget and climate. It flies in formation with five other satellites in the international \u201cA-Train\u201d (PDF) constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments, the Cloud-Aerosol LIdar with Orthogonal Polarization (CALIOP), the Imaging Infrared Radiometer (IIR), and the Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES. These data consist 5 km aerosol layer data.",
-            "title": "CALIPSO Lidar L1B Profile Data V3-02",
-            "programCode": [
-                "026:004"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_lid_l1-valstage1-v3-02_table",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
+            "temporal": "2011-11-01/2013-02-28",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CALIPSO Lidar L1B Profile Data V3-02"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/270/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2010-11-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "nasa",
-                "ames"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "SCOTT POLL",
                 "hasEmail": "mailto:scott.d.poll@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_270",
             "description": "A framework to compare and evaluate diagnosis algorithms (DAs) has been created jointly by NASA Ames Research Center and PARC. In this paper, we present the first concrete implementation of this framework as a competition called DXC\u201909. The goal of this competition was to evaluate and compare DAs in a common platform and to determine a winner based on diagnosis results. 12 DAs (model-based and otherwise) competed in this first year of the competition in 3 tracks that included industrial and synthetic systems. Specifically, the participants provided algorithms that communicated with the run-time architecture to receive scenario data and return diagnostic results. These algorithms were run on extended scenario data sets (different from sample set) to compute a set of pre-defined metrics. A ranking scheme based on weighted metrics was used to declare winners. This paper presents the systems used in DXC\u201909, description of faults and data sets, a listing of participating DAs, the metrics and results computed from running the DAs, and a superficial analysis of the results.",
-            "title": "First International Diagnosis Competition \u2013 DXC\u201909",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/DXC09_Competition_Final.pdf",
-                    "description": "20th International Workshop on Principles of Diagnosis paper",
                     "@type": "dcat:Distribution",
+                    "description": "20th International Workshop on Principles of Diagnosis paper",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/DXC09_Competition_Final.pdf",
+                    "mediaType": "application/pdf",
                     "title": "DXC09_Competition_Final.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_270",
+            "issued": "2010-11-22",
+            "keyword": [
+                "dashlink",
+                "nasa",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/270/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "First International Diagnosis Competition \u2013 DXC\u201909"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/M2YSWFL9RSSH",
             "citation": "Miyazaki, Kazuyuki. 2024-02-06. TRPSCRENOXLM2D. Version 1. TROPESS Chemical Reanalysis Lightning NOx emissions Monthly 2-dimensional Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/M2YSWFL9RSSH. https://disc.gsfc.nasa.gov/datacollection/TRPSCRENOXLM2D_1.html. Digital Science Data.",
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
-            "identifier": "C2837624975-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS Chemical Reanalysis Lightning NOx emissions Monthly 2-dimensional Product contains nitrogen oxides (NO and NO2) emissions from lightning strikes. The data are part of the Tropospheric Chemical Reanalysis v2 (TCR-2) for the period 2005-2021. TCR-2 uses JPL's Multi-mOdel Multi-cOnstituent Chemical (MOMO-Chem) data assimilation framework that simultaneously optimizes both concentrations and emissions of multiple species from multiple satellite sensors.\n\nThe data files are written in the netCDF version 4 file format, and each file contains a year of data at monthly resolution, and a spatial resolution of 1.125 x 1.125 degrees. The principal investigator for the TCR-2 data is Miyazaki, Kazuyuki.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSCRENOXLM2D",
-            "creator": "Miyazaki, Kazuyuki",
-            "graphic-preview-description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
-            "title": "TROPESS Chemical Reanalysis Lightning NOx emissions Monthly 2-dimensional Product V1 (TRPSCRENOXLM2D) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRENOXLM2D_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FM2YSWFL9RSSH",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FM2YSWFL9RSSH",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRENOXLM2D_Sample.png",
-                    "description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRENOXLM2D_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSCRENOXLM2D_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSCRENOXLM2D_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_MON_VERTCONCS/TRPSCRENOXLM2D.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_MON_VERTCONCS/TRPSCRENOXLM2D.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSCRENOXLM2D_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSCRENOXLM2D_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TCR2_MON_VERTCONCS/TRPSCRENOXLM2D.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TCR2_MON_VERTCONCS/TRPSCRENOXLM2D.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_MON_VERTCONCS/TRPSCRENOXLM2D.1/doc/TROPESS_ChemReanalysis_Forward_Stream_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_MON_VERTCONCS/TRPSCRENOXLM2D.1/doc/TROPESS_ChemReanalysis_Forward_Stream_README.pdf",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRENOXLM2D_Sample.png",
+            "identifier": "C2837624975-GES_DISC",
+            "issued": "2023-01-09",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/M2YSWFL9RSSH",
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
+            "series-name": "TRPSCRENOXLM2D",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2005-01-01T00:00:00Z/2024-02-12T00:00:00Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS Chemical Reanalysis Lightning NOx emissions Monthly 2-dimensional Product V1 (TRPSCRENOXLM2D) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/3w9f-95bt",
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
+                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_lid_l2_01kmclay-valstage1-V1-20_table",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000164",
             "issued": "2018-06-25",
-            "temporal": "2007-03-01/2007-11-11",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "eos",
                 "satellite",
@@ -107879,79 +107890,80 @@
                 "cloud",
                 "radiation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John M. Kusterer",
-                "hasEmail": "mailto:john.m.kusterer@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/3w9f-95bt",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:004"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000164",
-            "description": "Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) was launched on April 28, 2006 to study the impact of clouds and aerosols on the Earth\u2019s radiation budget and climate. It flies in formation with five other satellites in the international \u201cA-Train\u201d (PDF) constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments, the Cloud-Aerosol LIdar with Orthogonal Polarization (CALIOP), the Imaging Infrared Radiometer (IIR), and the Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES. These data consist 5 km aerosol layer data.",
-            "title": "CALIPSO Lidar L2 1 km Cloud Layer Data V1-20",
-            "programCode": [
-                "026:004"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_lid_l2_01kmclay-valstage1-V1-20_table",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
+            "temporal": "2007-03-01/2007-11-11",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CALIPSO Lidar L2 1 km Cloud Layer Data V1-20"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CLEM1-L-RSS-5-BSR-V1.0",
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
-                "deep space program science experiment"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Partially and fully processed data from Clementine (DSPSE) bistatic radar observations of the Moon.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.clem1-l-rss-5-bsr-v1.0_3wda-xmwr",
+            "issued": "2021-05-21",
+            "keyword": [
+                "moon",
+                "deep space program science experiment"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CLEM1-L-RSS-5-BSR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.clem1-l-rss-5-bsr-v1.0_3wda-xmwr",
-            "description": "Partially and fully processed data from Clementine (DSPSE) bistatic radar observations of the Moon.",
-            "title": "CLEM1 INTERMEDIATE AND REDUCED BISTATIC RADAR DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CLEM1 INTERMEDIATE AND REDUCED BISTATIC RADAR DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/3wfw-7jtf",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Phil Newman",
+                "hasEmail": "mailto:panewman@lheapop.gsfc.nasa.gov"
+            },
+            "description": "The Galactic model is a spatial and spectral template. The model for the Galactic diffuse emission was developed using spectral line surveys of HI and CO (as a tracer of H2) to derive the distribution of interstellar gas in Galactocentric rings. Infrared tracers of dust column density were used to correct column densities in directions where the optical depth of HI was either over or under-estimated. The model of the diffuse gamma-ray emission was then constructed by fitting the gamma-ray emissivities of the rings in several energy bands to the LAT observations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://fermi.gsfc.nasa.gov/ssc/data/access/lat/BackgroundModels.html",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000227",
             "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "acd",
                 "energy",
@@ -107969,45 +107981,44 @@
                 "gro",
                 "balloon"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Phil Newman",
-                "hasEmail": "mailto:panewman@lheapop.gsfc.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/3wfw-7jtf",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:014"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000227",
-            "description": "The Galactic model is a spatial and spectral template. The model for the Galactic diffuse emission was developed using spectral line surveys of HI and CO (as a tracer of H2) to derive the distribution of interstellar gas in Galactocentric rings. Infrared tracers of dust column density were used to correct column densities in directions where the optical depth of HI was either over or under-estimated. The model of the diffuse gamma-ray emission was then constructed by fitting the gamma-ray emissivities of the rings in several energy bands to the LAT observations.",
-            "title": "LAT Background Models",
-            "programCode": [
-                "026:014"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://fermi.gsfc.nasa.gov/ssc/data/access/lat/BackgroundModels.html",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "LAT Background Models"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/api-documents/foundry/#/data.nasa.gov/mc52-syum",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2015-11-30",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "https://data.nasa.gov/developer"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Jason Duley",
+                "hasEmail": "mailto:jason.duley@nasa.gov"
+            },
+            "description": "API using chronological data summary of fireball and bolide events provided by U.S. Government sensors.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "API using chronological data summary of fireball and bolide events provided by U.S. Government sensors.",
+                    "downloadURL": "https://data.nasa.gov/resource/mc52-syum.json",
+                    "mediaType": "text/html",
+                    "title": "Fireball And Bolide Reports API"
+                }
             ],
+            "identifier": "API-10",
+            "issued": "2015-11-30",
             "keyword": [
                 "fireball",
                 "meteor",
@@ -108018,353 +108029,351 @@
                 "atmosphere",
                 "landing"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Jason Duley",
-                "hasEmail": "mailto:jason.duley@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/api-documents/foundry/#/data.nasa.gov/mc52-syum",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "API-10",
-            "description": "API using chronological data summary of fireball and bolide events provided by U.S. Government sensors.",
-            "title": "Fireball And Bolide Reports API",
-            "programCode": [
-                "026:001"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.nasa.gov/resource/mc52-syum.json",
-                    "description": "API using chronological data summary of fireball and bolide events provided by U.S. Government sensors.",
-                    "@type": "dcat:Distribution",
-                    "title": "Fireball And Bolide Reports API"
-                }
+            "references": [
+                "https://data.nasa.gov/developer"
             ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Fireball And Bolide Reports API"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-MAG-1-MAP%2FHIGHRES-FLUX-V1.0",
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
+            "description": "Unknown",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-mag-1-map-highres-flux-v1.0_3wis-9swf",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars global surveyor",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-MAG-1-MAP%2FHIGHRES-FLUX-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-mag-1-map-highres-flux-v1.0_3wis-9swf",
-            "description": "Unknown",
-            "title": "MGS MARS MAG MAPPING DETAIL WORD RESOLUTION V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MGS MARS MAG MAPPING DETAIL WORD RESOLUTION V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1627523807-LARC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MISR Science Team (2004), Terra/MISR Level 3, Component Global Aerosol Product covering a day subset for the UAE region, version 4, Hampton, VA, USA: NASA Atmospheric Science Data Center (ASDC), Accessed <author citing data inserts date here> at doi: TBD",
-            "issued": "2019-07-31",
-            "temporal": "2004-07-01T00:00:00Z/2004-10-05T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-08-01",
-            "keyword": [
-                "air quality",
-                "earth science",
-                "aerosols",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "David Diner",
                 "hasEmail": "mailto:david.j.diner@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1627523807-LARC",
             "description": "The Multi-angle Imaging SpecrtroRadiometer (MISR) Level 3 Component Global Aerosol Product covering a day subset for the UAE region V004 contains a statistical summary of column aerosol 555 nanometer optical depth, and a monthly aersosol compositional type frequency histogram. This data product is a regional summary of the Level 2 aerosol parameters of interest averaged over a day and reported on a geographic grid, with resolution of 0.5 degree by 0.5 degree. The MISR instrument consists of nine pushbroom cameras which measure radiance in four spectral bands. Global coverage is achieved in nine days. The cameras are arranged with one camera pointing toward the nadir, four cameras pointing forward and four cameras pointing aftward. It takes 7 minutes for all nine cameras to view the same surface location. The view angles relative to the surface reference ellipsoid, are 0, 26.1, 45.6, 60.0, and 70.5 degrees. The spectral band shapes are nominally gaussian, centered at 443, 555, 670, and 865 nm.",
-            "title": "MISR Level 3 Component Global Aerosol Product covering a day subset for the UAE region V004",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1627523807-LARC.html",
-                    "description": "View this dataset on the CMR (Common Metadata Repository)",
                     "@type": "dcat:Distribution",
+                    "description": "View this dataset on the CMR (Common Metadata Repository)",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1627523807-LARC.html",
+                    "mediaType": "text/html",
                     "title": "CMR"
                 }
             ],
+            "identifier": "C1627523807-LARC",
+            "issued": "2019-07-31",
+            "keyword": [
+                "air quality",
+                "earth science",
+                "aerosols",
+                "atmosphere"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1627523807-LARC.html",
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
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2004-07-01T00:00:00Z/2004-10-05T23:59:59Z",
             "theme": [
                 "UAE_2004",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR Level 3 Component Global Aerosol Product covering a day subset for the UAE region V004"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC2-67PCHURYUMOV-M17-V2.0",
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
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 2 mission phase, covering the period from 2015-06-02T23:25:00.000 to 2015-06-30T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc2-67pchuryumov-m17-v2.0_3wjt-3349",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC2-67PCHURYUMOV-M17-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc2-67pchuryumov-m17-v2.0_3wjt-3349",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 2 mission phase, covering the period from 2015-06-02T23:25:00.000 to 2015-06-30T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC2-MTP017 RDR V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC2-MTP017 RDR V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-MAG-4-RDR-HGCOORDS-1.92SEC-V1.0",
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
+            "description": "This data set includes Voyager 2 Jupiter encounter magnetometer data given in Heliographic coordinates and averaged from the 60 ms instrument sample rate to a 1.92 second resampled rate. The data set consists of the following columns: 1) UT of the sample in the format yyyy-mm-ddThh:mm:ss.sssZ, 2) spacecraft clock (m65536:mod60:fds-line), 3) magnetometer id (1 = LFM, 2 = HFM), 4) Br (radial, Sun to spacecraft, B-field component), 5) Bt (azimuthal B-field component, positive in the direction of planetary orbital motion), 6) Bn (North/South B-field component, positive northward), 7) Bmag (magnitude of the averaged components), 8) avg_Bmag (average of the magnetic field magnitudes), 9) delta (latitude = arcsin(Bn/Bmag)), 10) lambda (longitude = 180. - atan(Bt/Br)), 11-13) rms vectors, 14) npts (number of points in average). All magnetic field observations are measured in nanoTesla.  All of the magnetic field data are calibrated (see the instrument calibration description for more details).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-mag-4-rdr-hgcoords-1.92sec-v1.0_3wjw-vncz",
+            "issued": "2021-05-21",
+            "keyword": [
+                "voyager",
+                "jupiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-MAG-4-RDR-HGCOORDS-1.92SEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-mag-4-rdr-hgcoords-1.92sec-v1.0_3wjw-vncz",
-            "description": "This data set includes Voyager 2 Jupiter encounter magnetometer data given in Heliographic coordinates and averaged from the 60 ms instrument sample rate to a 1.92 second resampled rate. The data set consists of the following columns: 1) UT of the sample in the format yyyy-mm-ddThh:mm:ss.sssZ, 2) spacecraft clock (m65536:mod60:fds-line), 3) magnetometer id (1 = LFM, 2 = HFM), 4) Br (radial, Sun to spacecraft, B-field component), 5) Bt (azimuthal B-field component, positive in the direction of planetary orbital motion), 6) Bn (North/South B-field component, positive northward), 7) Bmag (magnitude of the averaged components), 8) avg_Bmag (average of the magnetic field magnitudes), 9) delta (latitude = arcsin(Bn/Bmag)), 10) lambda (longitude = 180. - atan(Bt/Br)), 11-13) rms vectors, 14) npts (number of points in average). All magnetic field observations are measured in nanoTesla.  All of the magnetic field data are calibrated (see the instrument calibration description for more details).",
-            "title": "VG2 JUP MAG RESAMPLED HELIOGRAPHIC (RTN)\nCOORDS 1.92SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG2 JUP MAG RESAMPLED HELIOGRAPHIC (RTN)\nCOORDS 1.92SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-A-NIMS-4-IDACUBE-V1.0",
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
-                "galileo",
-                "ida"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data volume contains 17 channel spectral image cubes of asteroid 243 Ida ranging from 0.7 to 5.2 micrometers in wavelength in cgs units of radiance. These data were obtained by the Galileo spacecraft Near Infrared Mapping Spectrometer on August 28, 1993. They were radiometrically calibrated using calibration measurements obtained by the Near Infrared Mapping Spectrometer during its observations of Europa on June 28, 1996.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-a-nims-4-idacube-v1.0_3wkf-44er",
+            "issued": "2021-05-21",
+            "keyword": [
+                "galileo",
+                "ida"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-A-NIMS-4-IDACUBE-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-a-nims-4-idacube-v1.0_3wkf-44er",
-            "description": "This data volume contains 17 channel spectral image cubes of asteroid 243 Ida ranging from 0.7 to 5.2 micrometers in wavelength in cgs units of radiance. These data were obtained by the Galileo spacecraft Near Infrared Mapping Spectrometer on August 28, 1993. They were radiometrically calibrated using calibration measurements obtained by the Near Infrared Mapping Spectrometer during its observations of Europa on June 28, 1996.",
-            "title": "HIRES NIMS IDA SPECTRAL IMAGE CUBES",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "HIRES NIMS IDA SPECTRAL IMAGE CUBES"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-NEO-LIGHTCURVES-V1.0",
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
+            "description": "This data set contains photometric lightcurves of near-earth asteroids obtained by Petr Pravec and his collaborators at Ondrejov Observatory. Lightcurves for 42 asteroids are included. These asteroids were included based on a slightly wider criterion for a NEA: q < 1.33 AU (rather than the standard definition of q < 1.3 AU). As a result, some asteroids may be included which other researchers would classify as Mars-crossers.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-neo-lightcurves-v1.0_3wmv-kp8f",
+            "issued": "2021-05-21",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-NEO-LIGHTCURVES-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-neo-lightcurves-v1.0_3wmv-kp8f",
-            "description": "This data set contains photometric lightcurves of near-earth asteroids obtained by Petr Pravec and his collaborators at Ondrejov Observatory. Lightcurves for 42 asteroids are included. These asteroids were included based on a slightly wider criterion for a NEA: q < 1.33 AU (rather than the standard definition of q < 1.3 AU). As a result, some asteroids may be included which other researchers would classify as Mars-crossers.",
-            "title": "NEAR EARTH ASTEROID LIGHTCURVES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEAR EARTH ASTEROID LIGHTCURVES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-PPMAG-3-RDR-CROMMELIN-V1.0",
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
+            "description": "In preparation for the concerted international study of Comet Halley, the IHW conducted a trial run with observations of Comet Crommelin, largely during February and March of 1984.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-ppmag-3-rdr-crommelin-v1.0_3wp3-kaav",
+            "issued": "2018-06-26",
+            "keyword": [
+                "halley",
+                "international halley watch"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-PPMAG-3-RDR-CROMMELIN-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-ppmag-3-rdr-crommelin-v1.0_3wp3-kaav",
-            "description": "In preparation for the concerted international study of Comet Halley, the IHW conducted a trial run with observations of Comet Crommelin, largely during February and March of 1984.",
-            "title": "IHW COMET PPMAG CALIB REDUCED DATA RECORD CROMMELIN V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "IHW COMET PPMAG CALIB REDUCED DATA RECORD CROMMELIN V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MRO-M-SHARAD-4-RDR-V1.0",
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
-                "mars reconnaissance orbiter"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains RDR (derived) data from the SHARAD (Shallow Radar) instrument on Mars Reconnaissance Orbiter. SHARAD is the sub-surface sounding radar provided by the Italian Space Agency (ASI).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mro-m-sharad-4-rdr-v1.0_3wpd-cjnt",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "mars reconnaissance orbiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MRO-M-SHARAD-4-RDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mro-m-sharad-4-rdr-v1.0_3wpd-cjnt",
-            "description": "This dataset contains RDR (derived) data from the SHARAD (Shallow Radar) instrument on Mars Reconnaissance Orbiter. SHARAD is the sub-surface sounding radar provided by the Italian Space Agency (ASI).",
-            "title": "MRO SHARAD REDUCED DATA RECORD V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MRO SHARAD REDUCED DATA RECORD V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://nasa3d.arc.nasa.gov/detail/eoss-mgs",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://www.nasa.gov/mission_pages/mgs/index.html"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brian Kumanchik",
+                "hasEmail": "mailto:brian.kumanchik@jpl.nasa.gov"
+            },
+            "description": "Model of the Mars Global Surveyor spacecraft. Polygons: 3543 Vertices: 4754",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://nasa3d.arc.nasa.gov/shared_assets/models/eoss-mgs/Mars-Global-Surveyor.zip",
+                    "mediaType": "application/blender"
+                }
             ],
+            "identifier": "NASA-379",
+            "issued": "2018-06-25",
             "keyword": [
                 "3d model",
                 "spacecraft",
@@ -108373,108 +108382,74 @@
                 "eyes on the solar system",
                 "mars global surveyor"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brian Kumanchik",
-                "hasEmail": "mailto:brian.kumanchik@jpl.nasa.gov"
-            },
+            "landingPage": "http://nasa3d.arc.nasa.gov/detail/eoss-mgs",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:007"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-379",
-            "description": "Model of the Mars Global Surveyor spacecraft. Polygons: 3543 Vertices: 4754",
-            "title": "NASA 3D Models: Mars Global Surveyor",
-            "programCode": [
-                "026:007"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://nasa3d.arc.nasa.gov/shared_assets/models/eoss-mgs/Mars-Global-Surveyor.zip",
-                    "mediaType": "application/blender"
-                }
+            "references": [
+                "http://www.nasa.gov/mission_pages/mgs/index.html"
             ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "NASA 3D Models: Mars Global Surveyor"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL-ALICE-2-CR4B-V1.0",
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
-                "calibration"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains CODMAC level 2 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the second half of the Cruise 4 phase, which took place between 2008-10-06 and 2009-09-13.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-alice-2-cr4b-v1.0_3wqh-apup",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "calibration"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL-ALICE-2-CR4B-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-alice-2-cr4b-v1.0_3wqh-apup",
-            "description": "This data set contains CODMAC level 2 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the second half of the Cruise 4 phase, which took place between 2008-10-06 and 2009-09-13.",
-            "title": "ROSETTA-ORBITER CAL ALICE 2 CR4B V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CAL ALICE 2 CR4B V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1282110402-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Tropical Rainfall Measuring Mission (TRMM). 2011-07-01. TRMM_1B11. TRMM Microwave Imager Calibrated Radiances L1B 1.5 hours V7. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/TRMM_1B11_7.html.",
-            "issued": "2011-07-01",
-            "temporal": "1997-12-07T00:00:00Z/2015-04-08T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-04-20",
-            "keyword": [
-                "spectral/engineering",
-                "visible wavelengths",
-                "platform characteristics",
-                "infrared wavelengths",
-                "earth science",
-                "sensor characteristics"
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
-            "identifier": "C1282110402-GES_DISC",
-            "description": "This dataset contains TRMM Micrwave Imager (TMI) L1B calibrated radiances in terms of Brightness Temperatures.\n\nThe TMI calibration algorithm (1B11) converts the radiometer counts to antenna temperatures by applying a linear relationship of the form Ta = c1 + c2 x count. The coefficients are provided by the instrument contractor. Antenna temperatures are corrected for cross-polarization and spill over to produce brightness temperatures (Tb), but no antenna beam pattern correction or sample to pixel averaging are performed. Temperatures are provided at 104 scan positions for the low frequency channels and 208 scan positions at 85 GHz. There are four samples per pixel (3 -dB beamwidth) at 10 GHz, two samples at 19, 22, and 37 GHz, and one sample per pixel for the 85 GHz.\nData Flow Description\n\n\nChanges in horizontal resolution resulting from the TRMM boost that occurred on 24 August 2001:\n\nPre-Boost (before 7 August 2001): Temporal Resolution: 91.5 min/orbit ~ 16 orbits/day; Swath Width: 760 km; Horizontal Resolution: 4.4 km \n\nPost-Boost (after 24 August 2001): Temporal Resolution: 92.5 min/orbit ~ 16 orbits/day; Swath Width: 878 km; Horizontal Resolution: 5.1 km",
-            "release-place": "Greenbelt, MD",
-            "series-name": "TRMM_1B11",
             "creator": "Tropical Rainfall Measuring Mission (TRMM)",
-            "title": "TRMM Microwave Imager Calibrated Radiances L1B 1.5 hours V7 (TRMM_1B11) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TRMM_1B11_7.png",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset contains TRMM Micrwave Imager (TMI) L1B calibrated radiances in terms of Brightness Temperatures.\n\nThe TMI calibration algorithm (1B11) converts the radiometer counts to antenna temperatures by applying a linear relationship of the form Ta = c1 + c2 x count. The coefficients are provided by the instrument contractor. Antenna temperatures are corrected for cross-polarization and spill over to produce brightness temperatures (Tb), but no antenna beam pattern correction or sample to pixel averaging are performed. Temperatures are provided at 104 scan positions for the low frequency channels and 208 scan positions at 85 GHz. There are four samples per pixel (3 -dB beamwidth) at 10 GHz, two samples at 19, 22, and 37 GHz, and one sample per pixel for the 85 GHz.\nData Flow Description\n\n\nChanges in horizontal resolution resulting from the TRMM boost that occurred on 24 August 2001:\n\nPre-Boost (before 7 August 2001): Temporal Resolution: 91.5 min/orbit ~ 16 orbits/day; Swath Width: 760 km; Horizontal Resolution: 4.4 km \n\nPost-Boost (after 24 August 2001): Temporal Resolution: 92.5 min/orbit ~ 16 orbits/day; Swath Width: 878 km; Horizontal Resolution: 5.1 km",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -108483,238 +108458,277 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRMM_1B11_7.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRMM_1B11_7.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L1/TRMM_1B11.7",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L1/TRMM_1B11.7",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/opendap/TRMM_L1/TRMM_1B11.7/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/opendap/TRMM_L1/TRMM_1B11.7/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRMM_1B11",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRMM_1B11",
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
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L1/TRMM_1B11/doc/README.TRMM_V7.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L1/TRMM_1B11/doc/README.TRMM_V7.pdf",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TRMM_1B11_7.png",
+            "identifier": "C1282110402-GES_DISC",
+            "issued": "2011-07-01",
+            "keyword": [
+                "spectral/engineering",
+                "visible wavelengths",
+                "platform characteristics",
+                "infrared wavelengths",
+                "earth science",
+                "sensor characteristics"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1282110402-GES_DISC.html",
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
+            "series-name": "TRMM_1B11",
             "spatial": "-180.0 -38.0 180.0 38.0",
+            "temporal": "1997-12-07T00:00:00Z/2015-04-08T23:59:59.999Z",
             "theme": [
                 "TRMM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TRMM Microwave Imager Calibrated Radiances L1B 1.5 hours V7 (TRMM_1B11) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSSSO-J-CASPIR-3-RDR-SL9-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This archive contains images of the collision of Comet Shoemaker-Levy 9 with Jupiter obtained with CASPIR on the Australian National University 2.3 m telescope at Siding Spring Observatory, Australia, by Peter J. McGregor and Mark G. Allen. Each subdirectory contains data for one night. A more specific description of the state of the data is given below.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mssso-j-caspir-3-rdr-sl9-v1.0_3wtp-d63b",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "sl9",
                 "comet sl9/jupiter collision",
                 "jupiter"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSSSO-J-CASPIR-3-RDR-SL9-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mssso-j-caspir-3-rdr-sl9-v1.0_3wtp-d63b",
-            "description": "This archive contains images of the collision of Comet Shoemaker-Levy 9 with Jupiter obtained with CASPIR on the Australian National University 2.3 m telescope at Siding Spring Observatory, Australia, by Peter J. McGregor and Mark G. Allen. Each subdirectory contains data for one night. A more specific description of the state of the data is given below.",
-            "title": "MSSSO CASPIR IMAGES FROM THE SL9 IMPACTS WITH JUPITER V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MSSSO CASPIR IMAGES FROM THE SL9 IMPACTS WITH JUPITER V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1459756630-GES_DISC.html",
             "citation": "NASA/GSFC. 2018-01-31. SCRN4L1RAD. Version 001. SCR/Nimbus-4 Level 1 Calibrated Radiances V001. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/SCRN4L1RAD_001.html. Digital Science Data.",
-            "issued": "1998-02-24",
-            "temporal": "1970-07-27T00:00:00Z/1973-02-20T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1998-02-24",
-            "references": [
-                "https://doi.org/10.1098/rspa.1970.0196"
-            ],
-            "keyword": [
-                "infrared wavelengths",
-                "spectral/engineering",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JAMES JOHNSON",
                 "hasEmail": "mailto:James.Johnson@nasa.gov"
             },
+            "creator": "NASA/GSFC",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1459756630-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "SCRN4L1RAD is the Nimbus-4 Selective Chopper Radiometer (SCR) Level 1 Calibrated Radiances data product. The calibrated radiances are measured at 6 channels from 2.3 to 15 micrometers with a ground resolution of 25 km, and are \"declouded\" (interpolated and smoothed across regions of cloud). The radiances were used to obtain the temperatures of six successive 10-km layers of the atmosphere from earth or cloudtop level to 60-km height. The data were recovered from the original 9-track tapes, and are now stored online as daily files in their original proprietary binary format with about 14 orbits per day.\n\nSpatial coverage is near global from latitude -80 to +80 degrees. The data are available from 27 July 1970 (day of year 208) to 20 February 1973 (day of year 51). The channel 1 temperature monitoring system failed on June 15, 1970, thereby reducing the accuracy of the SCR data. Channels 3 and 4 became noisy and unusable on April 18, 1972. The principal investigator for the SCR experiment was Dr. John T. Houghton from Oxford University.                                         \n\nThis product was previously available from the NSSDC with the identifier ESAD-00096 (old ID 78-098A-10E).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "SCRN4L1RAD",
-            "creator": "NASA/GSFC",
-            "graphic-preview-description": "Typical data coverage of a Nimbus 4 SCR Level 1 daily data file.",
-            "title": "SCR/Nimbus-4 Level 1 Calibrated Radiances V001 (SCRN4L1RAD) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/images/SCRN4L1RAD_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/images/SCRN4L1RAD_Sample.png",
-                    "description": "Typical data coverage of a Nimbus 4 SCR Level 1 daily data file.",
                     "@type": "dcat:Distribution",
+                    "description": "Typical data coverage of a Nimbus 4 SCR Level 1 daily data file.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/images/SCRN4L1RAD_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SCRN4L1RAD_001.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SCRN4L1RAD_001.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus4_SCR_Level1/SCRN4L1RAD.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus4_SCR_Level1/SCRN4L1RAD.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SCRN4L1RAD",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SCRN4L1RAD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus4_SCR_Level1/SCRN4L1RAD.001/doc/README.SCRN4L1RAD.001.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus4_SCR_Level1/SCRN4L1RAD.001/doc/README.SCRN4L1RAD.001.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.2_Product_Rqmts_Design/N4_SCR_onN4.pdf",
-                    "description": "The Selective Chopper Radiometer on Nimbus IV Archived Data",
                     "@type": "dcat:Distribution",
+                    "description": "The Selective Chopper Radiometer on Nimbus IV Archived Data",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.2_Product_Rqmts_Design/N4_SCR_onN4.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/NIMBUS/3.3_Product_Documentation/3.3.5_Product_Quality/NimbusIVUG.pdf",
-                    "description": "Nimbus 4 User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Nimbus 4 User's Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/NIMBUS/3.3_Product_Documentation/3.3.5_Product_Quality/NimbusIVUG.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/gzip",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/NIMBUS/3.3_Product_Documentation/3.3.5_Product_Quality/DataCatalogNimbus4.tar.gz",
-                    "description": "Nimbus 4 Data Catalog",
                     "@type": "dcat:Distribution",
+                    "description": "Nimbus 4 Data Catalog",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/NIMBUS/3.3_Product_Documentation/3.3.5_Product_Quality/DataCatalogNimbus4.tar.gz",
+                    "mediaType": "application/gzip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/N4_SCR_Inventory.xlsx",
-                    "description": "N4 SCR Inventory",
                     "@type": "dcat:Distribution",
+                    "description": "N4 SCR Inventory",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/N4_SCR_Inventory.xlsx",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Typical data coverage of a Nimbus 4 SCR Level 1 daily data file.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/images/SCRN4L1RAD_Sample.png",
+            "identifier": "C1459756630-GES_DISC",
+            "issued": "1998-02-24",
+            "keyword": [
+                "infrared wavelengths",
+                "spectral/engineering",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1459756630-GES_DISC.html",
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
+            "series-name": "SCRN4L1RAD",
             "spatial": "-180.0 -80.0 180.0 80.0",
+            "temporal": "1970-07-27T00:00:00Z/1973-02-20T23:59:59.999Z",
             "theme": [
                 "Nimbus",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SCR/Nimbus-4 Level 1 Calibrated Radiances V001 (SCRN4L1RAD) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/3wvv-bh9x",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Spaceflight imposes the risk of skeletal muscle atrophy for astronauts. The understanding of muscle atrophy because of spaceflight is limited but continued efforts are essential for developing countermeasures of this effect. A distinct difference between spaceflight-induced muscle atrophy and other forms of atrophy is the additional effect of cosmic rays in outer space. To study spaceflight-induced muscle atrophy we performed two ground-based models of microgravity in a low dose radiation environment and studied transcriptional changes in rat soleus muscle using microarray technology.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-225",
+                    "mediaType": "text/html",
+                    "title": "Expression profiling of soleus muscle under the effect of simulated spaceflight"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-225_3wvv-bh9x",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "growth protocol",
                 "data transformation",
@@ -108724,78 +108738,42 @@
                 "nucleic acid hybridization",
                 "rna extraction"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/3wvv-bh9x",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-225_3wvv-bh9x",
-            "description": "Spaceflight imposes the risk of skeletal muscle atrophy for astronauts. The understanding of muscle atrophy because of spaceflight is limited but continued efforts are essential for developing countermeasures of this effect. A distinct difference between spaceflight-induced muscle atrophy and other forms of atrophy is the additional effect of cosmic rays in outer space. To study spaceflight-induced muscle atrophy we performed two ground-based models of microgravity in a low dose radiation environment and studied transcriptional changes in rat soleus muscle using microarray technology.",
-            "title": "Expression profiling of soleus muscle under the effect of simulated spaceflight",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-225",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Expression profiling of soleus muscle under the effect of simulated spaceflight"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Expression profiling of soleus muscle under the effect of simulated spaceflight"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA2515",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Lambert, A., Livesey, N. and Read, W.. 2020-06-11. ML2N2O. Version 005. MLS/Aura Level 2 Nitrous Oxide (N2O) Mixing Ratio V005. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA2515. https://disc.gsfc.nasa.gov/datacollection/ML2N2O_005.html. Digital Science Data.",
-            "issued": "2020-02-04",
-            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-02-04",
-            "keyword": [
-                "atmosphere",
-                "earth science",
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
-            "identifier": "C1729925686-GES_DISC",
-            "description": "ML2N2O is the EOS Aura Microwave Limb Sounder (MLS) standard product for nitrous oxide derived from radiances measured primarily by the 640 GHz radiometer (Band 12) until August 6, 2013, after this date using the 190 GHz radiometer (Band 3). The data version is 5.0. Spatial coverage is near-global (-82 degrees to +82 degrees latitude), with each profile spaced 1.5 degrees or ~165 km along the orbit track (roughly 15 orbits per day). The recommended useful vertical range is from 68.1 to 0.464 hPa, and the vertical resolution is between 4 and 6 km. Users of the ML2N2O data product should read section 3.17 of the EOS MLS Level 2 Version 5 Quality Document for more information.\n\nThe data are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5), which is based on the version 5 Hierarchical Data Format, or HDF5. Each file contains two swath objects (profile and column data), each with a set of data and geolocation fields, swath attributes, and metadata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML2N2O",
             "creator": "Lambert, A., Livesey, N. and Read, W.",
-            "title": "MLS/Aura Level 2 Nitrous Oxide (N2O) Mixing Ratio V005 (ML2N2O) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2N2O_005.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "ML2N2O is the EOS Aura Microwave Limb Sounder (MLS) standard product for nitrous oxide derived from radiances measured primarily by the 640 GHz radiometer (Band 12) until August 6, 2013, after this date using the 190 GHz radiometer (Band 3). The data version is 5.0. Spatial coverage is near-global (-82 degrees to +82 degrees latitude), with each profile spaced 1.5 degrees or ~165 km along the orbit track (roughly 15 orbits per day). The recommended useful vertical range is from 68.1 to 0.464 hPa, and the vertical resolution is between 4 and 6 km. Users of the ML2N2O data product should read section 3.17 of the EOS MLS Level 2 Version 5 Quality Document for more information.\n\nThe data are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5), which is based on the version 5 Hierarchical Data Format, or HDF5. Each file contains two swath objects (profile and column data), each with a set of data and geolocation fields, swath attributes, and metadata.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA2515",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA2515",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -108805,492 +108783,528 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML2N2O_005.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML2N2O_005.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level2/ML2N2O.005/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level2/ML2N2O.005/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level2/ML2N2O.005/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level2/ML2N2O.005/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML2N2O_005",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML2N2O_005",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2N2O_005.png",
+            "identifier": "C1729925686-GES_DISC",
+            "issued": "2020-02-04",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA2515",
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
+            "series-name": "ML2N2O",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MLS/Aura Level 2 Nitrous Oxide (N2O) Mixing Ratio V005 (ML2N2O) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/WFF/APU/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wolff, David , Ali  Tokay and Matthew T. Wingo.2018. GPM Ground Validation Autonomous Parsivel Unit (APU) Wallops Flight Facility (WFF) [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/WFF/APU/DATA101",
-            "issued": "2018-12-17",
-            "temporal": "2013-05-08T21:26:00Z/2014-10-08T05:30:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
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
-            "identifier": "C1979128844-GHRC_DAAC",
             "description": "The GPM Ground Validation Autonomous Parsivel Unit (APU) Wallops Flight Facility (WFF) dataset consists of precipitation data including precipitation amount, precipitation rate, reflectivity in Rayleigh regime, liquid water content, drop diameter, and drop concentration obtained from six Autonomous Parsivel Units (APUs) positioned at the Wallops Flight Facility (WFF) in support of the Global Precipitation Mission (GPM). The APU is an optical laser-disdrometer based on single particle extinction that measures particle size and fall velocity. It consists of the Parsivel2 developed by OTT in Germany and supporting hardware developed by University of Alabama. Data are available in ASCII format for the period of May 6, 2013 through October 9, 2014.",
-            "title": "GPM Ground Validation Autonomous Parsivel Unit (APU) Wallops Flight Facility (WFF) V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FWFF%2FAPU%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FWFF%2FAPU%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmapuwff",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmapuwff",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/relatedProjects/wff/parsivel/doc/gpmapuwff_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/relatedProjects/wff/parsivel/doc/gpmapuwff_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/relatedProjects/wff/parsivel/doc/readme_apu_wff.pdf",
-                    "description": "Automated Parsivel Unit (APU) data processing during Wallops Flight Facility operation",
                     "@type": "dcat:Distribution",
+                    "description": "Automated Parsivel Unit (APU) data processing during Wallops Flight Facility operation",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/relatedProjects/wff/parsivel/doc/readme_apu_wff.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/1520-0469(1976)033%3C0851:TVASOC%3E2.0.CO;2",
-                    "description": "Terminal velocity and shape of cloud and precipitation drops aloft",
                     "@type": "dcat:Distribution",
+                    "description": "Terminal velocity and shape of cloud and precipitation drops aloft",
+                    "downloadURL": "https://doi.org/10.1175/1520-0469(1976)033%3C0851:TVASOC%3E2.0.CO;2",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/JTECH-D-12-00254.1",
-                    "description": "Articulating and Stationary PARSIVEL Disdrometer Measurements in Conditions with Strong Winds and Heavy Rainfall",
                     "@type": "dcat:Distribution",
+                    "description": "Articulating and Stationary PARSIVEL Disdrometer Measurements in Conditions with Strong Winds and Heavy Rainfall",
+                    "downloadURL": "https://doi.org/10.1175/JTECH-D-12-00254.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/2010JHM1244.1",
-                    "description": "Experimental quantification of the sampling uncertainty associated with measurements from PARSIVEL Disdrometers",
                     "@type": "dcat:Distribution",
+                    "description": "Experimental quantification of the sampling uncertainty associated with measurements from PARSIVEL Disdrometers",
+                    "downloadURL": "https://doi.org/10.1175/2010JHM1244.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/1520-0450(2001)040%3C2083:CODSDM%3E2.0.CO;2",
-                    "description": "Comparison of drop size distribution measurements by impact and optical disdrometers",
                     "@type": "dcat:Distribution",
+                    "description": "Comparison of drop size distribution measurements by impact and optical disdrometers",
+                    "downloadURL": "https://doi.org/10.1175/1520-0450(2001)040%3C2083:CODSDM%3E2.0.CO;2",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/JTECH-D-13-00174.1",
-                    "description": "Evaluation of the New Version of the Laser-Optical Disdrometer, OTT Parsivel2",
                     "@type": "dcat:Distribution",
+                    "description": "Evaluation of the New Version of the Laser-Optical Disdrometer, OTT Parsivel2",
+                    "downloadURL": "https://doi.org/10.1175/JTECH-D-13-00174.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://wallops-prf.gsfc.nasa.gov/",
-                    "description": "GPM Precipitation Science Research Facility at Wallops Flight Facility",
                     "@type": "dcat:Distribution",
+                    "description": "GPM Precipitation Science Research Facility at Wallops Flight Facility",
+                    "downloadURL": "http://wallops-prf.gsfc.nasa.gov/",
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
+            "identifier": "C1979128844-GHRC_DAAC",
+            "issued": "2018-12-17",
+            "keyword": [
+                "precipitation",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/WFF/APU/DATA101",
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
             "spatial": "-75.5812 37.8294 -75.3562 38.0442",
+            "temporal": "2013-05-08T21:26:00Z/2014-10-08T05:30:00Z",
             "theme": [
                 "GPMGV",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM Ground Validation Autonomous Parsivel Unit (APU) Wallops Flight Facility (WFF) V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4H70CRF",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for International Earth Science Information Network - CIESIN - Columbia University. 2016-10-21. Global Urban Heat Island (UHI) Data Set, 2013. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H4H70CRF. https://doi.org/10.7927/H4H70CRF.",
-            "issued": "2016-10-21",
-            "temporal": "2013-01-01T00:00:00Z/2013-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-10-21",
-            "references": [
-                "http://doi.org/10.7927/H408638T",
-                "https://doi.org/10.7927/H44M92HC"
-            ],
-            "keyword": [
-                "land surface",
-                "surface thermal properties",
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
-            "identifier": "C1399941740-SEDAC",
-            "description": "The Urban Heat Island (UHI) effect represents the relatively higher temperatures found in urban areas compared to surrounding rural areas owing to higher proportions of impervious surfaces and the release of waste heat from vehicles and heating and cooling systems. Paved surfaces and built structures tend to absorb shortwave radiation from the sun and release long-wave radiation after a lag of a few hours. The Global Urban Heat Island (UHI) Data Set, 2013, estimates the land surface temperature within urban areas in degrees Celsius (average summer daytime maximum and average summer nighttime minimum) as well as the difference between those temperatures and the temperatures in surrounding rural areas, defined as a 10km buffer around the urban extent. Urban extents are from SEDAC\u00ef\u00bf\u00bds Global Rural-Urban Mapping Project, Version 1 (GRUMPv1), and land surface temperatures are from SEDAC\u00ef\u00bf\u00bds Global Summer Land Surface Temperature (LST) Grids, 2013, which are derived from the Aqua Level-3 Moderate Resolution Imaging Spectroradiometer (MODIS) Version 5 global daytime and nighttime Land Surface Temperature (LST) 8-day composite data (MYD11A2). For most regions, the UHI data set provides the average daytime maximum (1:30 p.m. overpass) and average nighttime minimum (1:30 a.m. overpass) temperatures in urban and rural areas, and the urban-rural temperature differences, derived from LST data representing a 40-day time-span during July-August (Julian days 185-224) in the northern hemisphere and January-February (Julian days 001-040) in the southern hemisphere. LST grid cells with missing values resulting from high cloud cover in tropical regions were filled with daytime maximum and nighttime minimum LST values from April-May 2013 in the northern hemisphere and December 2013-January 2014 in the southern hemisphere, where available. Some data gaps remain in areas where data were insufficient (e.g., Central Africa).",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Center for International Earth Science Information Network - CIESIN - Columbia University",
-            "title": "Global Urban Heat Island (UHI) Data Set, 2013",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/sdei-global-uhi-2013/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Urban Heat Island (UHI) effect represents the relatively higher temperatures found in urban areas compared to surrounding rural areas owing to higher proportions of impervious surfaces and the release of waste heat from vehicles and heating and cooling systems. Paved surfaces and built structures tend to absorb shortwave radiation from the sun and release long-wave radiation after a lag of a few hours. The Global Urban Heat Island (UHI) Data Set, 2013, estimates the land surface temperature within urban areas in degrees Celsius (average summer daytime maximum and average summer nighttime minimum) as well as the difference between those temperatures and the temperatures in surrounding rural areas, defined as a 10km buffer around the urban extent. Urban extents are from SEDAC\u00ef\u00bf\u00bds Global Rural-Urban Mapping Project, Version 1 (GRUMPv1), and land surface temperatures are from SEDAC\u00ef\u00bf\u00bds Global Summer Land Surface Temperature (LST) Grids, 2013, which are derived from the Aqua Level-3 Moderate Resolution Imaging Spectroradiometer (MODIS) Version 5 global daytime and nighttime Land Surface Temperature (LST) 8-day composite data (MYD11A2). For most regions, the UHI data set provides the average daytime maximum (1:30 p.m. overpass) and average nighttime minimum (1:30 a.m. overpass) temperatures in urban and rural areas, and the urban-rural temperature differences, derived from LST data representing a 40-day time-span during July-August (Julian days 185-224) in the northern hemisphere and January-February (Julian days 001-040) in the southern hemisphere. LST grid cells with missing values resulting from high cloud cover in tropical regions were filled with daytime maximum and nighttime minimum LST values from April-May 2013 in the northern hemisphere and December 2013-January 2014 in the southern hemisphere, where available. Some data gaps remain in areas where data were insufficient (e.g., Central Africa).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4H70CRF",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4H70CRF",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/sdei/sdei-global-uhi-2013/sdei-global-uhi-2013-urban-day-mean-global-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/sdei/sdei-global-uhi-2013/sdei-global-uhi-2013-urban-day-mean-global-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdei-global-uhi-2013/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdei-global-uhi-2013/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdei-global-uhi-2013/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdei-global-uhi-2013/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/sdei-global-uhi-2013/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/sdei-global-uhi-2013/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdei-global-uhi-2013/maps/services",
-                    "description": "Web Map Service Page",
                     "@type": "dcat:Distribution",
+                    "description": "Web Map Service Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdei-global-uhi-2013/maps/services",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdei-global-uhi-2013",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdei-global-uhi-2013",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/sdei-global-uhi-2013/maps",
+            "identifier": "C1399941740-SEDAC",
+            "issued": "2016-10-21",
+            "keyword": [
+                "land surface",
+                "surface thermal properties",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4H70CRF",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2016-10-21",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "http://doi.org/10.7927/H408638T",
+                "https://doi.org/10.7927/H44M92HC"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-176.2 -54.86 179.46 78.28",
+            "temporal": "2013-01-01T00:00:00Z/2013-12-31T00:00:00Z",
             "theme": [
                 "SDEI",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Urban Heat Island (UHI) Data Set, 2013"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LRO-L-LOLA-5-SHADR-V1.0",
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
-                "lunar reconnaissance orbiter"
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
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lro-l-lola-5-shadr-v1.0_3x2x-pz8x",
             "description": "This data set contains spherical harmonic topographic (shape) and gravity potential models from the Lunar Orbiter Laser Altimeter instrument, LRO Laser Ranging, and radio tracking.",
-            "title": "LRO MOON LASER ALTIMETER 5 SHADR V1.0",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lro-l-lola-5-shadr-v1.0_3x2x-pz8x",
+            "issued": "2021-05-21",
+            "keyword": [
+                "moon",
+                "lunar reconnaissance orbiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LRO-L-LOLA-5-SHADR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
             "programCode": [
                 "026:005"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
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
+            "title": "LRO MOON LASER ALTIMETER 5 SHADR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GNSS/GNSS_IGSIONOTEC_001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "International GNSS Service, GNSS Final Daily Ionosphere Total Electron Content Grid Product, Greenbelt, MD, USA:NASA Crustal Dynamics Data Information System (CDDIS), Accessed [[enter user data access date]] at doi: 10.5067/GNSS/gnss_igsionotec_001",
-            "issued": "1998-01-01",
-            "temporal": "1998-01-01T00:00:00Z/2025-01-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-11",
-            "keyword": [
-                "geodetics",
-                "tectonics",
-                "earth science",
-                "solid earth",
-                "gravity/gravitational field"
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
-            "identifier": "C1511761518-CDDIS",
             "description": "This derived product set consists of Global Navigation Satellite System Final Ionosphere Vertical Total Electron Content (VTEC) product (daily files) from the NASA Crustal Dynamics Data Information System (CDDIS). The VTEC product files also include Delay Code Bias (DCB) values for GNSS satellites and ground receivers derived during the analysis. GNSS provide autonomous geo-spatial positioning with global coverage. GNSS data sets from ground receivers at the CDDIS consist primarily of the data from the U.S. Global Positioning System (GPS) and the Russian GLObal NAvigation Satellite System (GLONASS). Since 2011, the CDDIS GNSS archive includes data from other GNSS (Europe\u2019s Galileo, China\u2019s Beidou, Japan\u2019s Quasi-Zenith Satellite System/QZSS, the Indian Regional Navigation Satellite System/IRNSS, and worldwide Satellite Based Augmentation Systems/SBASs), which are similar to the U.S. GPS in terms of the satellite constellation, orbits, and signal structure. GNSS observations from a global network can be utilized for atmospheric measurements. Analysis Centers (ACs) of the International GNSS Service (IGS) retrieve GNSS data on regular schedules to produce independently computed VTEC maps. The IGS Ionosphere Analysis Center Coordinator (ACC) uses these individual AC solutions to generate the official IGS VTEC maps. The final VTEC maps are computed with a resolution of 2 hours in UT, 5 degrees in longitude and 2.5 degrees in latitude; they have an availability with a latency of 11 days.",
-            "title": "Global Navigation Satellite System (GNSS) Ionosphere Vertical Total Electron Content (VTEC) Final Product from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGNSS_IGSIONOTEC_001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGNSS_IGSIONOTEC_001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/archive/gnss/products",
-                    "description": "URL for retrieval of GNSS derived products through http",
                     "@type": "dcat:Distribution",
+                    "description": "URL for retrieval of GNSS derived products through http",
+                    "downloadURL": "https://cddis.nasa.gov/archive/gnss/products",
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
-                    "downloadURL": "http://doi.org/10.5067/GNSS/GNSS_IGSIONOTEC_001",
-                    "description": "URL for more information about GNSS derived products",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about GNSS derived products",
+                    "downloadURL": "http://doi.org/10.5067/GNSS/GNSS_IGSIONOTEC_001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1511761518-CDDIS",
+            "issued": "1998-01-01",
+            "keyword": [
+                "geodetics",
+                "tectonics",
+                "earth science",
+                "solid earth",
+                "gravity/gravitational field"
+            ],
+            "landingPage": "https://doi.org/10.5067/GNSS/GNSS_IGSIONOTEC_001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-11",
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
+            "title": "Global Navigation Satellite System (GNSS) Ionosphere Vertical Total Electron Content (VTEC) Final Product from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/0Q8WOQ3RC8DQ",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMEX02 Regional Vegetation Sampling Data, Iowa, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/0Q8WOQ3RC8DQ.",
-            "issued": "2002-06-30",
-            "temporal": "2002-06-30T00:00:00Z/2002-07-28T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2002-07-28",
-            "keyword": [
-                "earth science",
-                "vegetation",
-                "plant commodities",
-                "agriculture",
-                "biosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Martha Anderson",
                 "hasEmail": "mailto:mcanders@facstaff.wisc.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1386204110-NSIDCV0",
             "description": "This data set contains the vegetation parameters plant height, row spacing, stand density, and leaf area index (LAI) as part of the Soil Moisture Experiment 2002 (SMEX02).",
-            "title": "SMEX02 Regional Vegetation Sampling Data, Iowa, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F0Q8WOQ3RC8DQ",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F0Q8WOQ3RC8DQ",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX02/vegetation/regional_veg_and_LAI/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX02/vegetation/regional_veg_and_LAI/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX02/vegetation/regional_veg_and_LAI/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX02/vegetation/regional_veg_and_LAI/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/0Q8WOQ3RC8DQ",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/0Q8WOQ3RC8DQ",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/0Q8WOQ3RC8DQ",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/0Q8WOQ3RC8DQ",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386204110-NSIDCV0",
+            "issued": "2002-06-30",
+            "keyword": [
+                "earth science",
+                "vegetation",
+                "plant commodities",
+                "agriculture",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/0Q8WOQ3RC8DQ",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2002-07-28",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-93.8 41.7 -93.2 42.7",
+            "temporal": "2002-06-30T00:00:00Z/2002-07-28T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMEX02 Regional Vegetation Sampling Data, Iowa, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/3xaq-6cdn",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "The goal of this study was to assess whether low shear-modeled microgravity (LSMMG) effects yeast ,genomic expression patterns using the powerful tool of whole genome microarray hybridization. We determined ,changes in the yeast model organism Saccharomyces cerevisisae when grown in LSMMG using the rotating High ,Aspect Ratio Vessel (HARV). A significant number of genes were up- or down-regulated by at least two fold in cells ,that were grown for 5 generations or 25 generations in HARVs. We identified genes in cell wall integrity signaling ,pathways containing MAP kinase cascades that may provide clues to novel physiological responses of eukaryotic ,cells to the external stress of a low-shear modeled microgravity environment. A comparison of the microgravity ,response to other environmental stress response (ESR) genes showed that 26% of the genes that respond ,significantly to LSMMG are involved in a general environmental stress response while 74% of the genes may ,represent a unique transcriptional response to microgravity. In addition we found changes in genes involved in ,budding cell polarity establishment and cell separation that confirm our hypothesis that exposure to LSMMG ,causes changes in gene transcription resulting in a phenotypic response. The results of the study provide interesting ,clues to potential mechanisms involved in the response to adaptation to and survival of eukaryotic cells in a ,microgravity environment and our findings may have important health implications for human spaceflight. Experiment Overall Design: Four conditions are compared with three replicates each: yeast grown in low-shear modeled microgravity (HARV bioreactor) for 5 and 25 generations; yeast grown in a horizontal (non-LSMMG) HARV bioreactor for 5 and 25 generations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-12",
+                    "mediaType": "text/html",
+                    "title": "Transcription profiling of S. cerevisiae cultures grown under low shear-modeled microgravity"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-12_3xaq-6cdn",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "p-g4136-2",
                 "environmentalstress",
@@ -109301,47 +109315,35 @@
                 "labeling",
                 "nucleic_acid_extraction"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/3xaq-6cdn",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-12_3xaq-6cdn",
-            "description": "The goal of this study was to assess whether low shear-modeled microgravity (LSMMG) effects yeast ,genomic expression patterns using the powerful tool of whole genome microarray hybridization. We determined ,changes in the yeast model organism Saccharomyces cerevisisae when grown in LSMMG using the rotating High ,Aspect Ratio Vessel (HARV). A significant number of genes were up- or down-regulated by at least two fold in cells ,that were grown for 5 generations or 25 generations in HARVs. We identified genes in cell wall integrity signaling ,pathways containing MAP kinase cascades that may provide clues to novel physiological responses of eukaryotic ,cells to the external stress of a low-shear modeled microgravity environment. A comparison of the microgravity ,response to other environmental stress response (ESR) genes showed that 26% of the genes that respond ,significantly to LSMMG are involved in a general environmental stress response while 74% of the genes may ,represent a unique transcriptional response to microgravity. In addition we found changes in genes involved in ,budding cell polarity establishment and cell separation that confirm our hypothesis that exposure to LSMMG ,causes changes in gene transcription resulting in a phenotypic response. The results of the study provide interesting ,clues to potential mechanisms involved in the response to adaptation to and survival of eukaryotic cells in a ,microgravity environment and our findings may have important health implications for human spaceflight. Experiment Overall Design: Four conditions are compared with three replicates each: yeast grown in low-shear modeled microgravity (HARV bioreactor) for 5 and 25 generations; yeast grown in a horizontal (non-LSMMG) HARV bioreactor for 5 and 25 generations.",
-            "title": "Transcription profiling of S. cerevisiae cultures grown under low shear-modeled microgravity",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-12",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Transcription profiling of S. cerevisiae cultures grown under low shear-modeled microgravity"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Transcription profiling of S. cerevisiae cultures grown under low shear-modeled microgravity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-THREEMICRON-V1.2",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "3-micron spectrophotometric data on asteroids collected from several papers by Lebofsky, Jones, and Feierberg and their collaborators, published 1980-1990.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-threemicron-v1.2_3xb9-bbh4",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "36 atalante",
                 "1 ceres",
@@ -109398,795 +109400,807 @@
                 "70 panopaea",
                 "19 fortuna"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-THREEMICRON-V1.2",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-threemicron-v1.2_3xb9-bbh4",
-            "description": "3-micron spectrophotometric data on asteroids collected from several papers by Lebofsky, Jones, and Feierberg and their collaborators, published 1980-1990.",
-            "title": "LEBOFSKY ET AL. 3-MICRON ASTEROID DATA V1.2",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "LEBOFSKY ET AL. 3-MICRON ASTEROID DATA V1.2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL%2FE-ALICE-4-EAR3-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains CODMAC level 4 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the third earth flyby mission phase, which took place between 2009-09-14 and 2009-12-13.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-e-alice-4-ear3-v1.0_3xbc-vqit",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "moon",
                 "earth",
                 "international rosetta mission",
                 "calibration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL%2FE-ALICE-4-EAR3-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-e-alice-4-ear3-v1.0_3xbc-vqit",
-            "description": "This data set contains CODMAC level 4 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the third earth flyby mission phase, which took place between 2009-09-14 and 2009-12-13.",
-            "title": "ROSETTA-ORBITER CAL/EARTH ALICE 4 EAR3 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CAL/EARTH ALICE 4 EAR3 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/766/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-06-19",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "nasa",
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
-            "identifier": "DASHLINK_766",
             "description": "This article reports on preliminary results of a study conducted to examine how temporary electrical overstress seed fault conditions in discrete power electronic components that cannot be detected with reliability tests but impact longevity of the device. These defects do not result in formal parametric failures per datasheet specifications, but result in substantial change in the electrical characteristics when compared with pristine device parameters. Tests were carried out on commercially available 600V IGBT devices using transmission line pulse (TLP) and system level ESD stress.* It was hypothesized that the ESD causes local damage during the ESD discharge which may greatly accelerate degradation mechanisms and thus reduce the life of the components. This hypothesis was explored in simulation studies where different types of damage were imposed to different parts of the device. Experimental results agree qualitatively with the simulation for a number of tests which will motivate more in-depth modeling of the damage.",
-            "title": "Effect of Electrostatic Discharge on Electrical Characteristics of Discrete Electronic Components",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2009_PHM_ESD.pdf",
-                    "description": "2009_PHM_ESD.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "2009_PHM_ESD.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2009_PHM_ESD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "2009_PHM_ESD.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_766",
+            "issued": "2013-06-19",
+            "keyword": [
+                "dashlink",
+                "nasa",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/766/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Effect of Electrostatic Discharge on Electrical Characteristics of Discrete Electronic Components"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/269",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Harding, R., and K.F. Huemmrich. 1999. BOREAS HYD-05 Bear Trap Creek and Namekus Lake Winter Surface Flux Data. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/269",
-            "issued": "2023-11-22",
-            "temporal": "1994-02-01T00:00:00Z/1996-04-11T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-27",
-            "keyword": [
-                "atmospheric temperature",
-                "atmospheric radiation",
-                "earth science",
-                "atmospheric winds",
-                "ecosystems",
-                "atmosphere",
-                "biosphere",
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
-            "identifier": "C2807625820-ORNL_CLOUD",
             "description": "Contains the HYD-05 flux, and meteorological measurements from Bear Trap Forest, Saskatchewan in the winter of 1994. Contains the HYD-05 flux, meteorological, and infrared thermometer measurements from Namekus Lake, Saskatchewan in the winters of 1994 and",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS HYD-05 Bear Trap Creek and Namekus Lake Winter Surface Flux Data",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F269",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F269",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/HYD/h5flxd/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/HYD/h5flxd/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/HYD05_Flux.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/HYD05_Flux.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/269",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/269",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h5flxd/comp/h5flxd.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h5flxd/comp/h5flxd.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h5flxd/comp/HYD05_Flux.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h5flxd/comp/HYD05_Flux.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h5flxd/comp/HYD05_Flux.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h5flxd/comp/HYD05_Flux.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h5flxd/comp/HYD05_Flux.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h5flxd/comp/HYD05_Flux.txt",
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
+            "identifier": "C2807625820-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "atmospheric temperature",
+                "atmospheric radiation",
+                "earth science",
+                "atmospheric winds",
+                "ecosystems",
+                "atmosphere",
+                "biosphere",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/269",
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
             "spatial": "-106.17 53.83 -106.04 53.85",
+            "temporal": "1994-02-01T00:00:00Z/1996-04-11T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS HYD-05 Bear Trap Creek and Namekus Lake Winter Surface Flux Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2242",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Bohn, N., P.G. Brodrick, D.R. Thompson, R. Eckert, and P. Lovegreen. 2023. SHIFT: AVIRIS-NG Derived Gridded Mosaicked Canopy Water Content, California, 2022. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2242",
-            "issued": "2023-08-22",
-            "temporal": "2022-02-24T00:00:00Z/2022-05-17T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-23",
-            "keyword": [
-                "vegetation",
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
-            "identifier": "C2755452168-ORNL_CLOUD",
             "description": "This dataset provides per-pixel vegetation canopy water content (CWC) derived from surface reflectance measured by the Airborne Visible/Infrared Imaging Spectrometer-Next Generation (AVIRIS-NG) instrument from 2022-02-24 to 2022-05-17. This imagery was acquired as part of the Surface Biology and Geology High-Frequency Time Series (SHIFT) campaign. AVIRIS-NG measures reflected radiance in 425 bands at 5-nanometer (nm) intervals in the visible to shortwave infrared spectral range between 380 and 2510 nm. Measurements were radiometrically and geometrically calibrated as well as atmospherically corrected, and are provided at approximately 5-meter spatial resolution. These data include mosaics of several flight lines that were flown on a weekly basis covering a 640-square-mile (1,656-square-kilometer) study area, which stretches from Los Padres National Forest in the east to the Central California coast and into the coastal ocean in the west, including Dangermond Preserve and UCSB's Sedgwick Reserve. These data will help track changes in vegetation characteristics from late winter through early summer by providing insights into health and resilience of ecosystems as California's climate grows drier. In particular, temporal and spatial patterns of CWC will indicate drought stress and increased wildfire risk. The CWC files in this publication were processed by applying a simple fitting of spectral absorption features of liquid water and are distributed in cloud-optimized GeoTIFF (COG) format.",
-            "graphic-preview-description": "Canopy water content on 2022-02-24 for Dangermond Preserve, Santa Barbara County, California.",
-            "title": "SHIFT: AVIRIS-NG Derived Gridded Mosaicked Canopy Water Content, California, 2022",
-            "graphic-preview-file": "https://daac.ornl.gov/SHIFT/guides/SHIFT_AVNG_Canopy_WaterContent_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2242",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2242",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/shift/SHIFT_AVNG_Canopy_WaterContent/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/shift/SHIFT_AVNG_Canopy_WaterContent/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/SHIFT/guides/SHIFT_AVNG_Canopy_WaterContent.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/SHIFT/guides/SHIFT_AVNG_Canopy_WaterContent.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2242",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2242",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/shift/SHIFT_AVNG_Canopy_WaterContent/comp/SHIFT_AVNG_Canopy_WaterContent.pdf",
-                    "description": "SHIFT: AVIRIS-NG Derived Gridded Mosaicked Canopy Water Content, California, 2022: SHIFT_AVNG_Canopy_WaterContent.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "SHIFT: AVIRIS-NG Derived Gridded Mosaicked Canopy Water Content, California, 2022: SHIFT_AVNG_Canopy_WaterContent.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/shift/SHIFT_AVNG_Canopy_WaterContent/comp/SHIFT_AVNG_Canopy_WaterContent.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/SHIFT/guides/SHIFT_AVNG_Canopy_WaterContent_Fig1.png",
-                    "description": "Canopy water content on 2022-02-24 for Dangermond Preserve, Santa Barbara County, California.",
                     "@type": "dcat:Distribution",
+                    "description": "Canopy water content on 2022-02-24 for Dangermond Preserve, Santa Barbara County, California.",
+                    "downloadURL": "https://daac.ornl.gov/SHIFT/guides/SHIFT_AVNG_Canopy_WaterContent_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Canopy water content on 2022-02-24 for Dangermond Preserve, Santa Barbara County, California.",
+            "graphic-preview-file": "https://daac.ornl.gov/SHIFT/guides/SHIFT_AVNG_Canopy_WaterContent_Fig1.png",
+            "identifier": "C2755452168-ORNL_CLOUD",
+            "issued": "2023-08-22",
+            "keyword": [
+                "vegetation",
+                "biosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2242",
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
             "spatial": "-120.63 34.35 -119.87 34.91",
+            "temporal": "2022-02-24T00:00:00Z/2022-05-17T23:59:59Z",
             "theme": [
                 "SHIFT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SHIFT: AVIRIS-NG Derived Gridded Mosaicked Canopy Water Content, California, 2022"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-PRL-EDITED2-V1.0",
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
+            "description": "This data set contains EDITED\ndata from Rosetta RPC-LAP, acquired during the PRELANDING mission phase\nwhere the primary target was the comet 67P/CHURYUMOV-GERASIMENKO 1 (1969\nR1). It contains uncalibrated raw data, i.e. the digital output of the\ninstrument. This version reorganizes the data into fewer files with\nlonger time series and sorted by type of measurement. It also supersedes\nprevious versions that were split into MTPs. The version number starts\nover from V1.0 due to a change in naming convention.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-prl-edited2-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-PRL-EDITED2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-prl-edited2-v1.0",
-            "description": "This data set contains EDITED\ndata from Rosetta RPC-LAP, acquired during the PRELANDING mission phase\nwhere the primary target was the comet 67P/CHURYUMOV-GERASIMENKO 1 (1969\nR1). It contains uncalibrated raw data, i.e. the digital output of the\ninstrument. This version reorganizes the data into fewer files with\nlonger time series and sorted by type of measurement. It also supersedes\nprevious versions that were split into MTPs. The version number starts\nover from V1.0 due to a change in naming convention.",
-            "title": "ROSETTA-ORBITER 67P RPCLAP 2\nPRL EDITED2 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCLAP 2\nPRL EDITED2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/90",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Betts, A.K. 1994. Site Averaged AMS Data: 1988 (Betts) . ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/90",
-            "issued": "2023-11-21",
-            "temporal": "1988-01-01T00:00:00Z/1988-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-12-02",
-            "keyword": [
-                "precipitation",
-                "atmospheric radiation",
-                "land surface",
-                "earth science",
-                "atmospheric winds",
-                "atmospheric temperature",
-                "soils",
-                "atmosphere",
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
-            "identifier": "C2810659939-ORNL_CLOUD",
             "description": "Site averaged product of the Portable Automatic Meteorological Station (AMS) data acquired during the 1987-1989 FIFE experiment. Data are in 30-minute time intervals in 1988.",
-            "graphic-preview-description": "Browse Image",
-            "title": "Site Averaged AMS Data: 1988 (Betts)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/fife_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F90",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F90",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/ffo_Betts_1988_ams/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/ffo_Betts_1988_ams/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/FIFE/Follow_On/guides/Betts_AMS_data_88.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/FIFE/Follow_On/guides/Betts_AMS_data_88.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/90",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/90",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/ffo_Betts_1988_ams/comp/Betts_AMS_data_88.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/ffo_Betts_1988_ams/comp/Betts_AMS_data_88.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/ffo_Betts_1988_ams/comp/Betts_AMS_data_88.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/ffo_Betts_1988_ams/comp/Betts_AMS_data_88.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/ffo_Betts_1988_ams/comp/ffoams88.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/ffo_Betts_1988_ams/comp/ffoams88.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/ffo_Betts_1988_ams/comp/ffo_ams.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/ffo_Betts_1988_ams/comp/ffo_ams.txt",
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
+            "identifier": "C2810659939-ORNL_CLOUD",
+            "issued": "2023-11-21",
+            "keyword": [
+                "precipitation",
+                "atmospheric radiation",
+                "land surface",
+                "earth science",
+                "atmospheric winds",
+                "atmospheric temperature",
+                "soils",
+                "atmosphere",
+                "atmospheric pressure"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/90",
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
+            "temporal": "1988-01-01T00:00:00Z/1988-12-31T23:59:59Z",
             "theme": [
                 "FIFE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Site Averaged AMS Data: 1988 (Betts)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/FIREXAQ_TraceGas_AircraftRemoteSensing_ER2_GCAS_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2020-07-27. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/FIREXAQ_TraceGas_AircraftRemoteSensing_ER2_GCAS_Data_1.",
-            "issued": "2020-04-07",
-            "temporal": "2019-08-02T00:00:00Z/2019-08-21T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-15",
-            "keyword": [
-                "atmosphere",
-                "earth science",
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
-            "identifier": "C1917876335-LARC_ASDC",
             "description": "FIREXAQ_TraceGas_AircraftRemoteSensing_ER2_GCAS_Data are remotely sensed data collected by the GEOstationary Coastal and Air Pollution Events (GEO-CAPE) Airborne Simulator (GCAS) onboard the ER-2 aircraft during FIREX-AQ. \r\n\r\nCompleted during summer 2019, FIREX-AQ utilized a combination of instrumented airplanes, satellites, and ground-based instrumentation. Detailed fire plume sampling was carried out by the NASA DC-8 aircraft, which had a comprehensive instrument payload capable of measuring over 200 trace gas species, as well as aerosol microphysical, optical, and chemical properties. The DC-8 aircraft completed 23 science flights, including 15 flights from Boise, Idaho and 8 flights from Salina, Kansas. NASA\u2019s ER-2 completed 11 flights, partially in support of the FIREX-AQ effort. The ER-2 payload was made up of 8 satellite analog instruments and provided critical fire information, including fire temperature, fire plume heights, and vegetation/soil albedo information. NOAA provided the NOAA-CHEM Twin Otter and the NOAA-MET Twin Otter aircraft to measure chemical processing in the lofted plumes of Western wildfires. The NOAA-CHEM Twin Otter focused on nighttime plume chemistry, from which data is archived at the NASA Atmospheric Science Data Center (ASDC). The NOAA-MET Twin Otter collected measurements of air movements at fire boundaries with the goal of understanding the local weather impacts of fires and the movement patterns of fires. NOAA-MET Twin Otter data will be archived at the ASDC in the future. Additionally, a ground-based station in McCall, Idaho and several mobile laboratories provided in-situ measurements of aerosol microphysical and optical properties, aerosol chemical compositions, and trace gas species. \r\n\r\nThe Fire Influence on Regional to Global Environments and Air Quality (FIREX-AQ) campaign was a NOAA/NASA interagency intensive study of North American fires to gain an understanding on the integrated impact of the fire emissions on the tropospheric chemistry and composition and to assess the satellite\u2019s capability for detecting fires and estimating fire emissions. The overarching goal of FIREX-AQ was to provide measurements of trace gas and aerosol emissions for wildfires and prescribed fires in great detail, relate them to fuel and fire conditions at the point of emission, characterize the conditions relating to plume rise, and follow plumes downwind to understand chemical transformation and air quality impacts.",
-            "title": "FIREX-AQ ER-2 Remotely Sensed GEOstationary Coastal and Air Pollution Events (GEO-CAPE) Airborne Simulator (GCAS)",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FFIREXAQ_TraceGas_AircraftRemoteSensing_ER2_GCAS_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FFIREXAQ_TraceGas_AircraftRemoteSensing_ER2_GCAS_Data_1",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1917876335-LARC_ASDC",
-                    "description": "Earthdata Search for Product_Short_Name (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for Product_Short_Name (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1917876335-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/FIREXAQ_TraceGas_AircraftRemoteSensing_ER2_GCAS_Data_1",
-                    "description": "DOI data set landing page for FIREXAQ_TraceGas_AircraftRemoteSensing_ER2_GCAS_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIREXAQ_TraceGas_AircraftRemoteSensing_ER2_GCAS_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/FIREXAQ_TraceGas_AircraftRemoteSensing_ER2_GCAS_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIREX-AQ/TraceGas_AircraftRemoteSensing_ER2_GCAS_Data_1/",
-                    "description": "ASDC Direct Data Download for FIREXAQ_TraceGas_AircraftRemoteSensing_ER2_GCAS_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIREXAQ_TraceGas_AircraftRemoteSensing_ER2_GCAS_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIREX-AQ/TraceGas_AircraftRemoteSensing_ER2_GCAS_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIREX-AQ/TraceGas_AircraftRemoteSensing_ER2_GCAS_Data_1/contents.html",
-                    "description": "OPeNDAP data access for FIREXAQ_TraceGas_AircraftRemoteSensing_ER2_GCAS_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for FIREXAQ_TraceGas_AircraftRemoteSensing_ER2_GCAS_Data_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIREX-AQ/TraceGas_AircraftRemoteSensing_ER2_GCAS_Data_1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1917876335-LARC_ASDC",
+            "issued": "2020-04-07",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/FIREXAQ_TraceGas_AircraftRemoteSensing_ER2_GCAS_Data_1",
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
+            "temporal": "2019-08-02T00:00:00Z/2019-08-21T23:59:59.999Z",
             "theme": [
                 "FIREX-AQ",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FIREX-AQ ER-2 Remotely Sensed GEOstationary Coastal and Air Pollution Events (GEO-CAPE) Airborne Simulator (GCAS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-E-PPR-2-EDR-EARTH1-V1.0",
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
-                "galileo"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "ARCHIVE_STATUS, ,DATA_SET_TERSE_DESC,This data set contains the R_EDR data for the Galileo Orbiter PPR instrument for the period corresponding to the Earth-1 encounter observations in November-December 1990.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-e-ppr-2-edr-earth1-v1.0_3xje-v7n9",
+            "issued": "2018-06-26",
+            "keyword": [
+                "earth",
+                "galileo"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-E-PPR-2-EDR-EARTH1-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-e-ppr-2-edr-earth1-v1.0_3xje-v7n9",
-            "description": "ARCHIVE_STATUS, ,DATA_SET_TERSE_DESC,This data set contains the R_EDR data for the Galileo Orbiter PPR instrument for the period corresponding to the Earth-1 encounter observations in November-December 1990.",
-            "title": "GLL PPR EARTH-1 ENCOUNTER EDR",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GLL PPR EARTH-1 ENCOUNTER EDR"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Alp_rs_goddard_gravity_derived&version=1.0",
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
-                "lunar prospector",
-                "moon"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This bundle contains several gravity models for the Moon derived from Lunar Prospector and previous Lunar mission data. The models were derived by investigators at the Goddard Space Flight Center.",
+            "identifier": "urn:nasa:pds:lp_rs_goddard_gravity_derived",
+            "issued": "2021-05-21",
+            "keyword": [
+                "lunar prospector",
+                "moon"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Alp_rs_goddard_gravity_derived&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:lp_rs_goddard_gravity_derived",
-            "description": "This bundle contains several gravity models for the Moon derived from Lunar Prospector and previous Lunar mission data. The models were derived by investigators at the Goddard Space Flight Center.",
-            "title": "Goddard Lunar Gravity Model Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Goddard Lunar Gravity Model Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NOAA-20/VIIRS/L3M/RRS/2022",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/NOAA-20/VIIRS/L3M/RRS/2022.",
-            "issued": "2022-09-14",
-            "temporal": "2017-11-29T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-14",
-            "keyword": [
-                "aerosols",
-                "oceans",
-                "ocean optics",
-                "earth science",
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
-            "identifier": "C2340494643-OB_DAAC",
             "description": "The Visible and Infrared Imager/Radiometer Suite (VIIRS) is a multi-disciplinary instrument that is being flown on the Joint Polar Satellite System (JPSS) series of spacecraft, including the Suomi National Polar-orbiting Partnership (S-NPP) that launched in October 2011. JPSS is a multi-platform, multi-agency program that consolidates the polar orbiting spacecraft of NASA and the National Oceanic and Atmospheric Administration (NOAA). S-NPP is the initial spacecraft in this series, and VIIRS is the successor to MODIS for Earth science data product generation. VIIRS has 22 spectral bands ranging from 412 nm to 12 nm. There are 16 moderate-resolution bands (750m at nadir), 5 image-resolution bands (375m), and one day-night band (DNB).",
-            "title": "NOAA-20 VIIRS Global Mapped Remote-Sensing Reflectance (RRS) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNOAA-20%2FVIIRS%2FL3M%2FRRS%2F2022",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNOAA-20%2FVIIRS%2FL3M%2FRRS%2F2022",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NOAA-20/VIIRS/L3M/RRS/2022",
-                    "description": "VIIRS-NOAA-20 L3M Remote-Sensing Reflectance (RRS) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS-NOAA-20 L3M Remote-Sensing Reflectance (RRS) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NOAA-20/VIIRS/L3M/RRS/2022",
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
+            "identifier": "C2340494643-OB_DAAC",
+            "issued": "2022-09-14",
+            "keyword": [
+                "aerosols",
+                "oceans",
+                "ocean optics",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/NOAA-20/VIIRS/L3M/RRS/2022",
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
+            "title": "NOAA-20 VIIRS Global Mapped Remote-Sensing Reflectance (RRS) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.nasa.gov/content/it-policies-and-standards/#.VZFTzuuxEwB",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Lori Parker",
+                "hasEmail": "mailto:lori.parker-1@nasa.gov"
+            },
+            "description": "The documents contained in this dataset reflect NASA's comprehensive IT policy in compliance with Federal Government laws and regulations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "NASA Enterprise Architecture Procedures",
+                    "downloadURL": "http://nodis3.gsfc.nasa.gov/npg_img/N_PR_2830_001A_/N_PR_2830_001A_.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "NPR2830.1A.pdf"
+                }
+            ],
+            "identifier": "OCIO-Fitara-10",
             "issued": "2013-12-19",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "nasa it policy",
                 "it policy",
@@ -110196,1214 +110210,1214 @@
                 "enterprise architecture",
                 "ea"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Lori Parker",
-                "hasEmail": "mailto:lori.parker-1@nasa.gov"
-            },
+            "landingPage": "http://www.nasa.gov/content/it-policies-and-standards/#.VZFTzuuxEwB",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:046"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "OCIO-Fitara-10",
-            "description": "The documents contained in this dataset reflect NASA's comprehensive IT policy in compliance with Federal Government laws and regulations.",
-            "title": "IT Policies and Standards - NASA Enterprise Architecture Procedures",
-            "programCode": [
-                "026:046"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://nodis3.gsfc.nasa.gov/npg_img/N_PR_2830_001A_/N_PR_2830_001A_.pdf",
-                    "description": "NASA Enterprise Architecture Procedures",
-                    "@type": "dcat:Distribution",
-                    "title": "NPR2830.1A.pdf"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "IT Policies and Standards - NASA Enterprise Architecture Procedures"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SWOT-NALT-IGDR-1.0",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Surface Water Ocean Topography (SWOT). 2023-06-28. SWOT Level 2 Nadir Altimeter Interim Geophysical Data Record with Waveforms. Version 1.0. SWOT Level 2 Nadir Altimeter Interim Geophysical Data Record with Waveforms Version 1.0. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/JPL/PODAAC. https://doi.org/10.5067/SWOT-NALT-IGDR-1.0. https://swot.jpl.nasa.gov.",
-            "issued": "2022-06-28",
-            "temporal": "2022-12-16T00:00:00Z/2023-07-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-06-28",
-            "keyword": [
-                "oceans",
-                "ocean waves",
-                "sea surface topography",
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
-            "identifier": "C2296989380-POCLOUD",
-            "description": "The SWOT Level 2 Nadir Altimeter Interim Geophysical Data Record (IGDR) Version 1.0 dataset produced by the Surface Water and Ocean Topography (SWOT) mission provides sea surface height, significant wave height and wind speed measurements from the Poseidon-3C nadir altimeter, a Jason-class dual frequency (Ku/C) altimeter. SWOT is a joint mission between NASA and CNES that launched on December 16, 2022. It aims to measure ocean surface topography with unprecedented resolution and accuracy, as well as map inland water bodies globally.\r\nThe IGDR dataset consists of discrete measurements along the nadir track with sampling resolutions of approximately 6-km and 300-m at 1Hz and 20Hz, respectively. The data were processed using the Medium-accuracy (preliminary) Orbit Ephemeris (MOE) and preliminary values for certain auxiliary data. The IGDR data are distributed as one file per half orbit in netCDF-4 file format with a nominal latency of < 1.5 days.",
-            "series-name": "SWOT Level 2 Nadir Altimeter Interim Geophysical Data Record with Waveforms",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Surface Water Ocean Topography (SWOT)",
-            "title": "SWOT Level 2 Nadir Altimeter Interim Geophysical Data Record with Waveforms Version 1.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_NALT_IGDR_1.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The SWOT Level 2 Nadir Altimeter Interim Geophysical Data Record (IGDR) Version 1.0 dataset produced by the Surface Water and Ocean Topography (SWOT) mission provides sea surface height, significant wave height and wind speed measurements from the Poseidon-3C nadir altimeter, a Jason-class dual frequency (Ku/C) altimeter. SWOT is a joint mission between NASA and CNES that launched on December 16, 2022. It aims to measure ocean surface topography with unprecedented resolution and accuracy, as well as map inland water bodies globally.\r\nThe IGDR dataset consists of discrete measurements along the nadir track with sampling resolutions of approximately 6-km and 300-m at 1Hz and 20Hz, respectively. The data were processed using the Medium-accuracy (preliminary) Orbit Ephemeris (MOE) and preliminary values for certain auxiliary data. The IGDR data are distributed as one file per half orbit in netCDF-4 file format with a nominal latency of < 1.5 days.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSWOT-NALT-IGDR-1.0",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSWOT-NALT-IGDR-1.0",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2296989380-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2296989380-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2296989380-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2296989380-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_NALT_IGDR_1.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_NALT_IGDR_1.0.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/swot_mission_docs/pdd/SALP-ST-M-EA-17043-CN_0103_20220411_Rev1.3.pdf",
-                    "description": "Product Description Document (PDD)",
                     "@type": "dcat:Distribution",
+                    "description": "Product Description Document (PDD)",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/swot_mission_docs/pdd/SALP-ST-M-EA-17043-CN_0103_20220411_Rev1.3.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_NALT_IGDR_1.0.jpg",
+            "identifier": "C2296989380-POCLOUD",
+            "issued": "2022-06-28",
+            "keyword": [
+                "oceans",
+                "ocean waves",
+                "sea surface topography",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SWOT-NALT-IGDR-1.0",
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
+            "series-name": "SWOT Level 2 Nadir Altimeter Interim Geophysical Data Record with Waveforms",
             "spatial": "-180.0 -77.6 180.0 77.6",
+            "temporal": "2022-12-16T00:00:00Z/2023-07-03T00:00:00Z",
             "theme": [
                 "SWOT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SWOT Level 2 Nadir Altimeter Interim Geophysical Data Record with Waveforms Version 1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQR00-SKY01",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Emmanuel Dinnat. 2018-07-04. Aquarius Celestial Sky Products. Version 1. Aquarius Celestial Sky Products. Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, Md., 20771. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Goddard Space Flight Center (GSFC). https://doi.org/10.5067/AQR00-SKY01. http://podaac.jpl.nasa.gov/salinity/data.html. Emmanuel Dinnat, NASA Goddard Space Flight Center (GSFC), 2018-07-04, Aquarius Celestial Sky Microwave Emission Map Ancillary Dataset V1.0, http://podaac.jpl.nasa.gov/salinity/data.html.",
-            "issued": "2018-06-12",
-            "temporal": "2011-09-01T00:00:00Z/2015-06-07T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-06-12",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "atmospheric radiation"
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
-            "identifier": "C2617176761-POCLOUD",
-            "description": "This datasets contains three maps of L-band (wavelength = 21 cm) brightness temperature of the celestial sky (\"Galaxy\") used in the processing of the NASA Aquarius instrument data. The maps report Sky brightness temperatures in Kelvin gridded on the Earth Centered Inertial (ECI) reference frame epoch J2000. They are sampled over 721 Declinations between -90 degrees and +90 degrees and 1441 Right Ascensions between 0 degrees and 360 degrees, all evenly spaced at 0.25 degrees intervals. The brightness temperatures are assumed temporally invariant and polarization has been neglected.  They include microwave continuum and atomic hydrogen line (HI) emissions. The maps differ only in how the strong radio source Cassiopeia A has been included into the whole sky background surveys: 1/ TB_no_Cas_A does not include Cassiopeia A and reports only the whole Sky surveys. 2/ TB_Cas_A_1cell spread Cas A total flux homogeneously over 1 map grid cell (i.e. 9.8572E-6 sr). 3/ TB_Cas_A_beam spreads Cas A over surrounding grid cells using a convolution by a Gaussian beam with HPBW of 35 arcmin (equivalent to the instrument used for the Sky surveys). Cassiopeia A  is a supernova remnant (SNR) in the constellation Cassiopeia and the brightest extra-solar radio source in the sky at frequencies above 1.",
-            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, Md., 20771",
-            "series-name": "Aquarius Celestial Sky Products",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Emmanuel Dinnat",
-            "title": "Aquarius Celestial Sky Microwave Emission Map Ancillary Dataset V1.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_ANCILLARY_CELESTIALSKY_V1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This datasets contains three maps of L-band (wavelength = 21 cm) brightness temperature of the celestial sky (\"Galaxy\") used in the processing of the NASA Aquarius instrument data. The maps report Sky brightness temperatures in Kelvin gridded on the Earth Centered Inertial (ECI) reference frame epoch J2000. They are sampled over 721 Declinations between -90 degrees and +90 degrees and 1441 Right Ascensions between 0 degrees and 360 degrees, all evenly spaced at 0.25 degrees intervals. The brightness temperatures are assumed temporally invariant and polarization has been neglected.  They include microwave continuum and atomic hydrogen line (HI) emissions. The maps differ only in how the strong radio source Cassiopeia A has been included into the whole sky background surveys: 1/ TB_no_Cas_A does not include Cassiopeia A and reports only the whole Sky surveys. 2/ TB_Cas_A_1cell spread Cas A total flux homogeneously over 1 map grid cell (i.e. 9.8572E-6 sr). 3/ TB_Cas_A_beam spreads Cas A over surrounding grid cells using a convolution by a Gaussian beam with HPBW of 35 arcmin (equivalent to the instrument used for the Sky surveys). Cassiopeia A  is a supernova remnant (SNR) in the constellation Cassiopeia and the brightest extra-solar radio source in the sky at frequencies above 1.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR00-SKY01",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR00-SKY01",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://aquarius.oceansciences.org/",
-                    "description": "NASA Aquarius/SAC-D mission website",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Aquarius/SAC-D mission website",
+                    "downloadURL": "https://aquarius.oceansciences.org/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/EDinnat_etal_Paper_SkyTBMap_Lband.pdf",
-                    "description": "Publication on Aquarius Celestial Sky Map Product",
                     "@type": "dcat:Distribution",
+                    "description": "Publication on Aquarius Celestial Sky Map Product",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/EDinnat_etal_Paper_SkyTBMap_Lband.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_ANCILLARY_CELESTIALSKY_V1.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_ANCILLARY_CELESTIALSKY_V1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/UserGuideAquariusCelestialSkyMicrowaveEmissionMapProduct.pdf",
-                    "description": "Aquarius Celestial Sky Map Product User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Aquarius Celestial Sky Map Product User's Guide",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/UserGuideAquariusCelestialSkyMicrowaveEmissionMapProduct.pdf",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2617176761-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2617176761-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2617176761-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2617176761-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/sw/idl/aquarius_IDL_readers.tgz",
-                    "description": "MATLAB read software",
                     "@type": "dcat:Distribution",
+                    "description": "MATLAB read software",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/sw/idl/aquarius_IDL_readers.tgz",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/sw/matlab/aquarius_matlab_readers.tgz",
-                    "description": "Interactive Data Language read software",
                     "@type": "dcat:Distribution",
+                    "description": "Interactive Data Language read software",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/sw/matlab/aquarius_matlab_readers.tgz",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_ANCILLARY_CELESTIALSKY_V1.jpg",
+            "identifier": "C2617176761-POCLOUD",
+            "issued": "2018-06-12",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQR00-SKY01",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-06-12",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, Md., 20771",
+            "series-name": "Aquarius Celestial Sky Products",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-09-01T00:00:00Z/2015-06-07T23:59:59.999Z",
             "theme": [
                 "AQUARIUS SAC-D",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aquarius Celestial Sky Microwave Emission Map Ancillary Dataset V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VL1%2FVL2-M-MET-4-BINNED-P-T-V-V1.0",
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
-                "viking"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains binned and splined data obtained from the Viking Meteorology Instrument System (VMIS) through most of the Viking Lander 2 mission and the early days of the Lander 1 mission. The data set consists of mean values of pressure, temperature, and wind speed (zonal, meridional, and combined) and relevant statistics and warning flags calculated for 25 bins of equal duration per day. The effect of Lander interference on the temperature measurements is also estimated. The data are presented on a bin by bin basis for Lander 1 sol (Mars solar day after landing) 1-45 and for Lander 2 sol 1-1050 (with the only major gap occurring between sol 561 and 625). Failure of the quadrant sensor on Lander 1 sol 45 (see HESS_ETAL_1977) precludes unambiguous determination of wind direction without modification to the analysis techniques and software used to generate this data set (see HESS_ETAL_1977) therefore, this data set does not include Lander 1 measurements made after sol 45. A data set which has recovered a period of measurements made between Lander 1 sol 1 and 350 is available refer to PDS data set id VL1-M-MET-4-BINNED-P-T-V-CORR-V1.0.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vl1-vl2-m-met-4-binned-p-t-v-v1.0_3xvk-g4af",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "viking"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VL1%2FVL2-M-MET-4-BINNED-P-T-V-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vl1-vl2-m-met-4-binned-p-t-v-v1.0_3xvk-g4af",
-            "description": "This data set contains binned and splined data obtained from the Viking Meteorology Instrument System (VMIS) through most of the Viking Lander 2 mission and the early days of the Lander 1 mission. The data set consists of mean values of pressure, temperature, and wind speed (zonal, meridional, and combined) and relevant statistics and warning flags calculated for 25 bins of equal duration per day. The effect of Lander interference on the temperature measurements is also estimated. The data are presented on a bin by bin basis for Lander 1 sol (Mars solar day after landing) 1-45 and for Lander 2 sol 1-1050 (with the only major gap occurring between sol 561 and 625). Failure of the quadrant sensor on Lander 1 sol 45 (see HESS_ETAL_1977) precludes unambiguous determination of wind direction without modification to the analysis techniques and software used to generate this data set (see HESS_ETAL_1977) therefore, this data set does not include Lander 1 measurements made after sol 45. A data set which has recovered a period of measurements made between Lander 1 sol 1 and 350 is available refer to PDS data set id VL1-M-MET-4-BINNED-P-T-V-CORR-V1.0.",
-            "title": "VL1/VL2 MARS METEOROLOGY RESAMPLED DATA BINNED-P-T-V V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VL1/VL2 MARS METEOROLOGY RESAMPLED DATA BINNED-P-T-V V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GNSS/GNSS_IGSACCLK_001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GGL/CDDIS. https://doi.org/10.5067/GNSS/GNSS_IGSACCLK_001.",
-            "issued": "1992-01-01",
-            "temporal": "1992-01-01T00:00:00Z/2023-03-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-03-18",
-            "keyword": [
-                "geodetics",
-                "gravity/gravitational field",
-                "tectonics",
-                "solid earth",
-                "earth science"
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
-            "identifier": "C1620484183-CDDIS",
             "description": "This derived product set consists of Global Navigation Satellite System Final Satellite and Receiver Clock Product (30-second granularity, daily files, generated weekly) from the NASA Crustal Dynamics Data Information System (CDDIS). GNSS provide autonomous geo-spatial positioning with global coverage. GNSS data sets from ground receivers at the CDDIS consist primarily of the data from the U.S. Global Positioning System (GPS) and the Russian GLObal NAvigation Satellite System (GLONASS). Since 2011, the CDDIS GNSS archive includes data from other GNSS (Europe\u2019s Galileo, China\u2019s Beidou, Japan\u2019s Quasi-Zenith Satellite System/QZSS, the Indian Regional Navigation Satellite System/IRNSS, and worldwide Satellite Based Augmentation Systems/SBASs), which are similar to the U.S. GPS in terms of the satellite constellation, orbits, and signal structure.  Analysis Centers (ACs) of the International GNSS Service (IGS) retrieve GNSS data on regular schedules to produce GNSS satellite and ground receiver clock values. The IGS Analysis Center Coordinator (ACC) uses these individual AC solutions to generate the official IGS final combined satellite and receiver clock products. The AC clock products consist of daily station and satellite clock solution files, generated on a weekly basis with a delay of approximately 10 days (from the last day of the week). All satellite and receiver clock solution files utilize the clock RINEX format and span 24 hours from 00:00 to 23:45 UTC.",
-            "title": "Global Navigation Satellite System (GNSS) Analysis Center Final Clock Product (daily files, generated weekly) from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGNSS_IGSACCLK_001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGNSS_IGSACCLK_001",
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
-                    "downloadURL": "http://dx.doi.org/10.5067/GNSS/GNSS_IGSACCLK_001",
-                    "description": "URL for more information about GNSS derived products",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about GNSS derived products",
+                    "downloadURL": "http://dx.doi.org/10.5067/GNSS/GNSS_IGSACCLK_001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1620484183-CDDIS",
+            "issued": "1992-01-01",
+            "keyword": [
+                "geodetics",
+                "gravity/gravitational field",
+                "tectonics",
+                "solid earth",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GNSS/GNSS_IGSACCLK_001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-03-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GGL/CDDIS"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1992-01-01T00:00:00Z/2023-03-27T00:00:00Z",
             "theme": [
                 "IGS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Navigation Satellite System (GNSS) Analysis Center Final Clock Product (daily files, generated weekly) from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2574191901-POCLOUD.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "S-MODE Team. 2023-02-01. S-MODE Temperature and Salinity from Saildrones Version 1. Version 1. S-MODE Temperature and Salinity from Saildrones Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, S-MODE Project Data Manager, Fred Bingham. http://podaac.jpl.nasa.gov/S-MODE.",
-            "issued": "2021-10-19",
-            "temporal": "2021-10-01T00:00:00Z/2022-11-30T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-10-27",
-            "keyword": [
-                "ocean winds",
-                "atmosphere",
-                "atmospheric temperature",
-                "oceans",
-                "ocean optics",
-                "ocean circulation",
-                "ocean chemistry",
-                "ocean waves",
-                "earth science",
-                "atmospheric water vapor",
-                "ocean temperature",
-                "atmospheric radiation",
-                "atmospheric pressure",
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
-            "identifier": "C2574191901-POCLOUD",
-            "description": "This dataset contains a suite of Saildrone in-situ measurements (including but not limited to temperature, salinity, currents, biochemistry, and meteorology) taken during the Sub-Mesoscale Ocean Dynamics Experiment (S-MODE) conducted approximately 300 km offshore of San Francisco during a pilot campaign spanning two weeks in October 2021, and two intensive operating periods (IOPs) in Fall 2022 and Spring 2023. S-MODE aims to understand how ocean dynamics acting on short spatial scales influence the vertical exchange of physical and biological variables in the ocean. Saildrones are wind-and-solar-powered unmanned surface vehicles rigged with atmospheric and oceanic sensors that measure upper ocean horizontal velocities, near-surface temperature and salinity, Chlorophyll-a fluorescence, dissolved oxygen concentration, 5-m winds, air temperature, and surface radiation. Acoustic Doppler Current Profiler (ADCP) data samples are available in their raw 1 Hz sampling frequency as well as 5 minute averages, the latter available with navigation data. Other measurements are available as raw files (1Hz or 20 Hz where applicable), as well as 1 minute averages. L1 data are available as a zip file.",
-            "series-name": "S-MODE Temperature and Salinity from Saildrones Version 1",
-            "graphic-preview-description": "Thumbnail",
             "creator": "S-MODE Team",
-            "title": "S-MODE Saildrone Level 1 Observations",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SMODE_L0_SAILDRONES_V1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset contains a suite of Saildrone in-situ measurements (including but not limited to temperature, salinity, currents, biochemistry, and meteorology) taken during the Sub-Mesoscale Ocean Dynamics Experiment (S-MODE) conducted approximately 300 km offshore of San Francisco during a pilot campaign spanning two weeks in October 2021, and two intensive operating periods (IOPs) in Fall 2022 and Spring 2023. S-MODE aims to understand how ocean dynamics acting on short spatial scales influence the vertical exchange of physical and biological variables in the ocean. Saildrones are wind-and-solar-powered unmanned surface vehicles rigged with atmospheric and oceanic sensors that measure upper ocean horizontal velocities, near-surface temperature and salinity, Chlorophyll-a fluorescence, dissolved oxygen concentration, 5-m winds, air temperature, and surface radiation. Acoustic Doppler Current Profiler (ADCP) data samples are available in their raw 1 Hz sampling frequency as well as 5 minute averages, the latter available with navigation data. Other measurements are available as raw files (1Hz or 20 Hz where applicable), as well as 1 minute averages. L1 data are available as a zip file.",
             "distribution": [
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SMODE_L0_SAILDRONES_V1.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SMODE_L0_SAILDRONES_V1.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2574191901-POCLOUD",
-                    "description": "Browse and download granules over HTTPS using the virtual directories",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2574191901-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2574191901-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2574191901-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SMODE_L0_SAILDRONES_V1.jpg",
+            "identifier": "C2574191901-POCLOUD",
+            "issued": "2021-10-19",
+            "keyword": [
+                "ocean winds",
+                "atmosphere",
+                "atmospheric temperature",
+                "oceans",
+                "ocean optics",
+                "ocean circulation",
+                "ocean chemistry",
+                "ocean waves",
+                "earth science",
+                "atmospheric water vapor",
+                "ocean temperature",
+                "atmospheric radiation",
+                "atmospheric pressure",
+                "salinity/density"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2574191901-POCLOUD.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-10-27",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "series-name": "S-MODE Temperature and Salinity from Saildrones Version 1",
             "spatial": "-125.4 36.3 -122.9 38.1",
+            "temporal": "2021-10-01T00:00:00Z/2022-11-30T00:00:00Z",
             "theme": [
                 "S-MODE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "S-MODE Saildrone Level 1 Observations"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-PEPSSI-3-PLUTO-V1.0",
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
-                "solar wind"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Calibrated data taken by the New Horizons Pluto Energetic Particle Spectrometer Science Investigation instrument during the Pluto encounter mission phase.  This is VERSION 1.0 of this data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-pepssi-3-pluto-v1.0_3xwz-miq2",
+            "issued": "2018-06-26",
+            "keyword": [
+                "new horizons",
+                "solar wind"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-PEPSSI-3-PLUTO-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-pepssi-3-pluto-v1.0_3xwz-miq2",
-            "description": "This data set contains Calibrated data taken by the New Horizons Pluto Energetic Particle Spectrometer Science Investigation instrument during the Pluto encounter mission phase.  This is VERSION 1.0 of this data set.",
-            "title": "NEW HORIZONS\n      PEPSSI PLUTO ENCOUNTER\n      CALIBRATED V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS\n      PEPSSI PLUTO ENCOUNTER\n      CALIBRATED V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/513/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2012-01-27",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "ames",
-                "nasa"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ashok Srivastava",
                 "hasEmail": "mailto:ashok.n.srivastava@gmail.com"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_513",
             "description": "Sparse machine learning has recently \r\nemerged as powerful tool to obtain models of high-dimensional data with high degree of interpretability, at low computational cost. This paper posits that these methods can be extremely useful for understanding large collections of text documents, without requiring user expertise in machine learning. Our approach relies on three main ingredients: (a) multi-document text summarization and (b) comparative summarization of two corpora, both using \r\nparse regression or classifi\fcation; (c) sparse principal components and sparse graphical models for unsupervised analysis and visualization of large text \r\ncorpora. We validate our approach using a corpus of Aviation Safety Reporting System (ASRS) reports and demonstrate that the methods can reveal causal and contributing factors in runway incursions. Furthermore, we show that the methods automatically discover four main tasks that pilots perform during \r\nflight, which can aid in further understanding the causal and contributing factors to runway incursions and other drivers for aviation safety incidents. \r\n\r\nCitation:  L. El Ghaoui, G. C. Li, V. Duong, V. Pham, A. N. Srivastava, and K. Bhaduri, \u201cSparse Machine Learning Methods for Understanding Large Text Corpora,\u201d Proceedings of the Conference on Intelligent Data Understanding, 2011.",
-            "title": "Sparse Machine Learning Methods for Understanding Large Text Corpora",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/cidu2011-dashlink.pdf",
-                    "description": "cidu2011-dashlink.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "cidu2011-dashlink.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/cidu2011-dashlink.pdf",
+                    "mediaType": "application/pdf",
                     "title": "cidu2011-dashlink.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_513",
+            "issued": "2012-01-27",
+            "keyword": [
+                "dashlink",
+                "ames",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/513/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Sparse Machine Learning Methods for Understanding Large Text Corpora"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC3-67P-M18-STR-REFL-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-06-30T23:25:00.000 to 2015-07-28T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc3-67p-m18-str-refl-v1.0_3xye-jnhn",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "pluto",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC3-67P-M18-STR-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc3-67p-m18-str-refl-v1.0_3xye-jnhn",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-06-30T23:25:00.000 to 2015-07-28T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC3-MTP018 RDR-STR-REFL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC3-MTP018 RDR-STR-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-IRFTAB-3-RDR-HALLEY-V2.0",
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
-                "international halley watch"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains filter set parameters for all IR filters referenced in any of the data sets archived by the International Halley Watch (IHW) Infrared Studies Network (IRSN).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-irftab-3-rdr-halley-v2.0_3y2h-yds2",
+            "issued": "2021-05-21",
+            "keyword": [
+                "calibration",
+                "international halley watch"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-IRFTAB-3-RDR-HALLEY-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-irftab-3-rdr-halley-v2.0_3y2h-yds2",
-            "description": "This data set contains filter set parameters for all IR filters referenced in any of the data sets archived by the International Halley Watch (IHW) Infrared Studies Network (IRSN).",
-            "title": "IHW COMET HALLEY INFRARED FILTER SETS, V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "IHW COMET HALLEY INFRARED FILTER SETS, V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=BUGLAB-E-BUG-4-V1.0",
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
-                "earth"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Bloomsburg University Goniometer (BUG) was used to make bidirectional reflectance distribution function (BRDF) measurements of Mars soil analogs at Mars Exploration Rover (MER) Panoramic Camera (Pancam) wavelengths.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.buglab-e-bug-4-v1.0_3y5c-5hbp",
+            "issued": "2021-05-21",
+            "keyword": [
+                "earth"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=BUGLAB-E-BUG-4-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.buglab-e-bug-4-v1.0_3y5c-5hbp",
-            "description": "The Bloomsburg University Goniometer (BUG) was used to make bidirectional reflectance distribution function (BRDF) measurements of Mars soil analogs at Mars Exploration Rover (MER) Panoramic Camera (Pancam) wavelengths.",
-            "title": "MARS ANALOG SOIL BUG OBSERVATIONS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS ANALOG SOIL BUG OBSERVATIONS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GHRC/AMSU-A/DATA201",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Spencer, Roy W and William D Braswell.1999. ADVANCED MICROWAVE SOUNDING UNIT-A (AMSU-A) SWATH FROM NOAA-15 [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GHRC/AMSU-A/DATA201",
-            "issued": "1999-03-19",
-            "temporal": "1998-08-03T01:51:10Z/2022-06-13T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-06-09",
-            "keyword": [
-                "microwave",
-                "atmosphere",
-                "spectral/engineering",
-                "earth science",
-                "atmospheric water vapor",
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
-            "identifier": "C1996541017-GHRC_DAAC",
             "description": "AMSU-A, the Advanced Microwave Sounding Unit, is a 15-channel passive microwave radiometer used to profile atmospheric temperature and moisture from the earth's surface to ~45 km (3 millibars). All orbits beginning in the day (00:00:00 - 23:59:59 UTC) are stored in one daily HDF-EOS file. Each file contains 15 (channel) arrays, as well as corresponding latitude, longitude, and time. AMSU flies on the National Oceanic and Atmospheric Administration (NOAA) polar orbiting spacecraft as part of the National Polar-orbiting Operational Environmental Satellite System (NPOESS). NOAA-15 was the first spacecraft to fly AMSU. Launched on 13 May 1998, NOAA-15 is in a sun synchronous near polar orbit.",
-            "graphic-preview-description": "N/A",
-            "title": "ADVANCED MICROWAVE SOUNDING UNIT-A (AMSU-A) SWATH FROM NOAA-15 V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/amsu-a/noaa-15/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHRC%2FAMSU-A%2FDATA201",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHRC%2FAMSU-A%2FDATA201",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=amsua15sp",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=amsua15sp",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/amsu-a/noaa-15/browse/2017/0105/amsua15_2017.005_C01_A.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/amsu-a/noaa-15/browse/2017/0105/amsua15_2017.005_C01_A.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/amsu_a/amsu-a_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/amsu_a/amsu-a_dataset.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/amsu_a/amsuareader.c",
-                    "description": "PROGRAM - Reads the Nth scan line from the given file, or the first if \"N\" is not specified",
                     "@type": "dcat:Distribution",
+                    "description": "PROGRAM - Reads the Nth scan line from the given file, or the first if \"N\" is not specified",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/amsu_a/amsuareader.c",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/amsu-a/noaa-15/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/amsu-a/noaa-15/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/amsu-a/noaa-15/browse/",
+            "identifier": "C1996541017-GHRC_DAAC",
+            "issued": "1999-03-19",
+            "keyword": [
+                "microwave",
+                "atmosphere",
+                "spectral/engineering",
+                "earth science",
+                "atmospheric water vapor",
+                "atmospheric temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/GHRC/AMSU-A/DATA201",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-06-09",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/MSFC/GHRC"
+            },
             "spatial": "-180.0 -90.0 180.0 89.756",
+            "temporal": "1998-08-03T01:51:10Z/2022-06-13T00:00:00Z",
             "theme": [
                 "NOT APPLICABLE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ADVANCED MICROWAVE SOUNDING UNIT-A (AMSU-A) SWATH FROM NOAA-15 V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-ROSINA-2-PRL-V2.0",
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
+            "description": "This data set contains CODMAC level 2 science data acquired by the COPS, DFMS and RTOF ROSINA sensors between 2014-03-29 and 2014-11-18 during the Prelanding phase of the Rosetta mission to comet 67P/CG. V2.0 : Some missing DFMS PDS files were added and corrupted files have been removed.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rosina-2-prl-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-ROSINA-2-PRL-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rosina-2-prl-v2.0",
-            "description": "This data set contains CODMAC level 2 science data acquired by the COPS, DFMS and RTOF ROSINA sensors between 2014-03-29 and 2014-11-18 during the Prelanding phase of the Rosetta mission to comet 67P/CG. V2.0 : Some missing DFMS PDS files were added and corrupted files have been removed.",
-            "title": "ROSETTA-ORBITER 67P ROSINA 2\n                                      PRL V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P ROSINA 2\n                                      PRL V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-OCCULTATIONS-V9.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set is intended to include all reported timings of observed asteroid, planet, and planetary satellite occultation events as well as occultation axes derived from those timings by David W. Dunham and David Herald. This version is complete through April 2011.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-occultations-v9.0_3y9u-qzyq",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "support archives",
                 "asteroid",
                 "satellite"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-OCCULTATIONS-V9.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-occultations-v9.0_3y9u-qzyq",
-            "description": "This data set is intended to include all reported timings of observed asteroid, planet, and planetary satellite occultation events as well as occultation axes derived from those timings by David W. Dunham and David Herald. This version is complete through April 2011.",
-            "title": "ASTEROID OCCULTATIONS V9.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ASTEROID OCCULTATIONS V9.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GP-J-ASI-3-ENTRY-V1.0",
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
+            "description": "This data set is most accurately described in [SEIFFETAL1996]:",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.gp-j-asi-3-entry-v1.0_3yat-mtrj",
+            "issued": "2021-05-21",
+            "keyword": [
+                "jupiter",
+                "galileo"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GP-J-ASI-3-ENTRY-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.gp-j-asi-3-entry-v1.0_3yat-mtrj",
-            "description": "This data set is most accurately described in [SEIFFETAL1996]:",
-            "title": "GALILEO PROBE ASI RAW DATA SET",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GALILEO PROBE ASI RAW DATA SET"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-FC2-2-EDR-CERES-IMAGES-V1.0",
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
+            "description": "Abstract                                                                   ========                                                                   This data set includes the Experiment Data Record (EDR) version of all   available images acquired during the Ceres Prime Mission (Approach,      Transfer to Survey, Survey, HAMO, and LAMO),and extended missions 1      (XMO1, XMO2, XMO3, XMO4) and 2 (XMO6, XMO7). In addition to the imagery, ancillary information is stored within the image headers. Calibration    files needed for further processing are archived as a separate data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-fc2-2-edr-ceres-images-v1.0_3ybh-pjsu",
+            "issued": "2021-05-21",
+            "keyword": [
+                "1 ceres",
+                "dawn mission to vesta and ceres"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-FC2-2-EDR-CERES-IMAGES-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-fc2-2-edr-ceres-images-v1.0_3ybh-pjsu",
-            "description": "Abstract                                                                   ========                                                                   This data set includes the Experiment Data Record (EDR) version of all   available images acquired during the Ceres Prime Mission (Approach,      Transfer to Survey, Survey, HAMO, and LAMO),and extended missions 1      (XMO1, XMO2, XMO3, XMO4) and 2 (XMO6, XMO7). In addition to the imagery, ancillary information is stored within the image headers. Calibration    files needed for further processing are archived as a separate data set.",
-            "title": "DAWN FC2 RAW (EDR) CERES IMAGES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "DAWN FC2 RAW (EDR) CERES IMAGES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/362/",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Farzad amirjavid",
+                "hasEmail": "mailto:farzad.amirjavid@gmail.com"
+            },
+            "description": "A primary goal to design smart homes is to provide automatic assistance for the residents to make them able to live independently at home.  Activity recognition is done to achieve the mentioned goal and then to provide assistance, we would need three sort of information. First, we would need to know the goal of the resident, then the pattern that the resident should obey to achieve its goal and third sort of needed information is the deviations from the previously known patterns.  In the presented paper, spatiotemporal aspects of daily activities are surveyed to mine the patterns of activities realized by the smart homes residents.  Necessary data to model the spatiotemporal aspects of daily activities is provided by embedded sensors in the smart home. We believe that to accomplish daily activities, specific objects are applied and by analyzing the movement of objects and resident(s), we would obtain valuable information to model the daily activities of the Smart Home\u2019s residents.",
+            "identifier": "DASHLINK_362",
             "issued": "2011-04-28",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "dashlink",
                 "ames",
                 "nasa"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Farzad amirjavid",
-                "hasEmail": "mailto:farzad.amirjavid@gmail.com"
-            },
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/362/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Dashlink"
             },
-            "identifier": "DASHLINK_362",
-            "description": "A primary goal to design smart homes is to provide automatic assistance for the residents to make them able to live independently at home.  Activity recognition is done to achieve the mentioned goal and then to provide assistance, we would need three sort of information. First, we would need to know the goal of the resident, then the pattern that the resident should obey to achieve its goal and third sort of needed information is the deviations from the previously known patterns.  In the presented paper, spatiotemporal aspects of daily activities are surveyed to mine the patterns of activities realized by the smart homes residents.  Necessary data to model the spatiotemporal aspects of daily activities is provided by embedded sensors in the smart home. We believe that to accomplish daily activities, specific objects are applied and by analyzing the movement of objects and resident(s), we would obtain valuable information to model the daily activities of the Smart Home\u2019s residents.",
-            "title": "Fuzzy Spatiotemporal Data Mining to Activity Recognition in Smart Homes",
-            "programCode": [
-                "026:029"
-            ],
-            "accrualPeriodicity": "irregular"
+            "title": "Fuzzy Spatiotemporal Data Mining to Activity Recognition in Smart Homes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0030",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2000-04-07. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/FIRE/0030.",
-            "issued": "2000-03-17",
-            "temporal": "1992-05-29T00:00:00Z/1992-06-23T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-06",
-            "keyword": [
-                "visible wavelengths",
-                "infrared wavelengths",
-                "spectral/engineering",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DR. MICHAEL KING",
                 "hasEmail": "mailto:michael.d.king@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1000000995-LARC_ASDC",
             "description": "The First ISCCP Regional Experiments have been designed to improve data products and cloud/radiation parameterizations used in general circulation models (GCMs). Specifically, the goals of FIRE are (1) to improve the basic understanding of the interaction of physical processes in determining life cycles of cirrus and marine stratocumulus systems and the radiative properties of these clouds during their life cycles and (2) to investigate the interrelationships between the ISCCP data, GCM parameterizations, and higher space and time resolution cloud data. To-date, four intensive field-observation periods were planned and executed: a cirrus IFO (October 13 - November 2, 1986); a marine stratocumulus IFO off the southwestern coast of California (June 29 - July 20, 1987); a second cirrus IFO in southeastern Kansas (November 13 - December 7, 1991); and a second marine stratocumulus IFO in the eastern North Atlantic Ocean (June 1 - June 28, 1992). Each mission combined coordinated satellite, airborne, and surface observations with modeling studies to investigate the cloud properties and physical processes of the cloud systems.The MODIS Airbourne Simulator (MAS) is a modified Daedalus Wildfire scanning spectrometer which flies on a NASA ER-2 and provides spectral information similar to that which will be provided by the Moderate Resolution Imaging Spectroradiometer (MODIS), scheduled to be launched on the EOS-AM platform in 1998 (King et al. 1992). The principal investigators for the MAS are Dr. Michael King (NASA/GSFC, Greenbelt MD), and Dr. Paul Menzel (NOAA/NESDIS, Madison WI).In January 1992, the modified Wildfire instrument was converted to MAS configuration. In June 1992 the MAS was flown over portions of the Atlantic Ocean in the region of the Azores during the ASTEX experiment. Although the MAS instrument is a 50 band spectrometer, the data system used in this experiment could only record 12 channels (at 8-bit resolution). The MAS spectrometer acquires high spatial resolution imagery in the wavelength range of 0.55 to 14.3 microns. A total of 50 spectral bands are available in this range, and the digitizer can be configured to collect data from any 12 of these bands. The digitizer was configured with four 10-bit channels and seven 8-bit channels. The MAS spectrometer was mated to a scanner subassembly which collected image data with an IFOV of 2.5 mrad, giving a ground resolution of 50 meters from 20000 meters altitude, and a cross track scan width of 85.92 degrees. The data granules were written using the self documenting file storage format provided through the netCDF interface routines included in the HDF libraries.",
-            "title": "First ISCCP Regional Experiment (FIRE) Atlantic Stratocumulus & Transition Experiment (ASTEX) NASA ER-2 MODIS Airborne Simulator (MAS) Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0030",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0030",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000995-LARC_ASDC",
-                    "description": "Earthdata Search for FIRE_AX_ER2_MAS_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FIRE_AX_ER2_MAS_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000995-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/ax_er2_mas_read_netcdf_idl.pro",
-                    "description": "Project/Campaign Document: ARB 48-inch Lidar Langley DAAC",
                     "@type": "dcat:Distribution",
+                    "description": "Project/Campaign Document: ARB 48-inch Lidar Langley DAAC",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/ax_er2_mas_read_netcdf_idl.pro",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/ax_er2_mas_read_netcdf.c",
-                    "description": "Project/Campaign Document: ARESE Langley DAAC",
                     "@type": "dcat:Distribution",
+                    "description": "Project/Campaign Document: ARESE Langley DAAC",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/ax_er2_mas_read_netcdf.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ax_er2_mas_dataset.pdf",
-                    "description": "FIRE ASTEX NASA ER-2 MODIS Airborne Simulator (MAS) (FIRE_AX_ER2_MAS) Langley DAAC Data Set Document",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE ASTEX NASA ER-2 MODIS Airborne Simulator (MAS) (FIRE_AX_ER2_MAS) Langley DAAC Data Set Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ax_er2_mas_dataset.pdf",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/fire_ax_er2_mas.readme.txt",
-                    "description": "Information about MAS data sets sample read software and data files for the FIRE ASTEX ER2 MAS (FIRE_AX_ER2_MAS) data set Readme",
                     "@type": "dcat:Distribution",
+                    "description": "Information about MAS data sets sample read software and data files for the FIRE ASTEX ER2 MAS (FIRE_AX_ER2_MAS) data set Readme",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/fire_ax_er2_mas.readme.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/postscript",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ax_er2_mas_gen.ps",
-                    "description": "FIRE ASTEX sample read software and data files - Direct File Download (.ps)",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE ASTEX sample read software and data files - Direct File Download (.ps)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ax_er2_mas_gen.ps",
+                    "mediaType": "application/postscript",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0030",
-                    "description": "DOI data set landing page for FIRE_AX_ER2_MAS_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIRE_AX_ER2_MAS_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0030",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/MAS",
-                    "description": "ASDC Data and Information for MAS",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for MAS",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/MAS",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://mas.arc.nasa.gov/data/deploy_html/astex_home.html",
-                    "description": "Campaign Summary Information for Atlantic Stratocumulus Transition Experiment (ASTEx)",
                     "@type": "dcat:Distribution",
+                    "description": "Campaign Summary Information for Atlantic Stratocumulus Transition Experiment (ASTEx)",
+                    "downloadURL": "https://mas.arc.nasa.gov/data/deploy_html/astex_home.html",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://mas.arc.nasa.gov/data/deploy_html/fire_home.html",
-                    "description": "Campaign Summary Information for First ISCCP Regional Experiment (FIRE)",
                     "@type": "dcat:Distribution",
+                    "description": "Campaign Summary Information for First ISCCP Regional Experiment (FIRE)",
+                    "downloadURL": "https://mas.arc.nasa.gov/data/deploy_html/fire_home.html",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://mas.arc.nasa.gov/",
-                    "description": "Enhanced MODIS Airborne Simulator (eMAS) Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "Enhanced MODIS Airborne Simulator (eMAS) Project Home Page",
+                    "downloadURL": "https://mas.arc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
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
-                    "downloadURL": "https://mas.arc.nasa.gov/data/srf/ARC-Jun95/msr0695.ph",
-                    "description": "MAS Spectral Response Summary",
                     "@type": "dcat:Distribution",
+                    "description": "MAS Spectral Response Summary",
+                    "downloadURL": "https://mas.arc.nasa.gov/data/srf/ARC-Jun95/msr0695.ph",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_AX_ER2_MAS/",
-                    "description": "ASDC Direct Data Download for FIRE_AX_ER2_MAS_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIRE_AX_ER2_MAS_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_AX_ER2_MAS/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_AX_ER2_MAS/contents.html",
-                    "description": "OPeNDAP data access for FIRE_AX_ER2_MAS_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for FIRE_AX_ER2_MAS_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_AX_ER2_MAS/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1000000995-LARC_ASDC",
+            "issued": "2000-03-17",
+            "keyword": [
+                "visible wavelengths",
+                "infrared wavelengths",
+                "spectral/engineering",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0030",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>32.27 -122.02 32.27 -15.31 41.02 -15.31 41.02 -122.02 32.27 -122.02</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1992-05-29T00:00:00Z/1992-06-23T23:59:59.999Z",
             "theme": [
                 "FIRE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "First ISCCP Regional Experiment (FIRE) Atlantic Stratocumulus & Transition Experiment (ASTEX) NASA ER-2 MODIS Airborne Simulator (MAS) Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/3yij-9hmj",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Gene expression levels were determined in 3rd instar and adult Drosophila melanogaster reared during spaceflight to elucidate the genetic and molecular mechanisms underpinning the effects of microgravity on the immune system. The goal was to validate the Drosophila model for understanding alterations of innate immune responses in humans due to spaceflight. Five containers of flies with ten female and five male fruit flies in each container were housed and bred on the space shuttle (average orbit altitude of 330.35 km) for 12 days and 18.5 hours with a new generation reared in microgravity. RNA was extracted on the day of shuttle landing from whole body animals (3rd instar larvae and adults) hybridized to Drosophila 2.0 Affymetrix genome arrays and the expression level of all genes was normalized against the gene expression level from the corresponding developmental stage animals raised on ground. Spaceflight altered the expression of larval genes involved in the maturation of plasmatocytes (macrophages) and their phagocytic response as well as the level of constitutive expression of pattern recognition receptors and opsonins that specifically recognize bacteria and of lysozymes antimicrobial peptide pathway and immune stress genes hallmarks of humoral immunity. Larval microarrays (FL 6 samples) are based on RNA extracted from 6 independent sets of 50 mid 3rd instar larvae reared in microgravity and collected on the day of landing after 12 days and 18.5 hours on the space shuttle and the same number of control larvae raised on ground (GL 6 samples). Adults microarrays (F1 3 samples) are based on RNA from 3 sets of 20 adult females each that emerged during spaceflight and within 4 hours of landing and the same number of adult females from the corresponding ground control containers (G1 3 samples).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-3",
+                    "mediaType": "text/html",
+                    "title": "Drosophila melanogaster gene expression changes after spaceflight."
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-3_3yij-9hmj",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "p-gse23880-5",
                 "sample collection protocol",
@@ -111425,86 +111439,82 @@
                 "hybridization",
                 "cosmic radiation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/3yij-9hmj",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-3_3yij-9hmj",
-            "description": "Gene expression levels were determined in 3rd instar and adult Drosophila melanogaster reared during spaceflight to elucidate the genetic and molecular mechanisms underpinning the effects of microgravity on the immune system. The goal was to validate the Drosophila model for understanding alterations of innate immune responses in humans due to spaceflight. Five containers of flies with ten female and five male fruit flies in each container were housed and bred on the space shuttle (average orbit altitude of 330.35 km) for 12 days and 18.5 hours with a new generation reared in microgravity. RNA was extracted on the day of shuttle landing from whole body animals (3rd instar larvae and adults) hybridized to Drosophila 2.0 Affymetrix genome arrays and the expression level of all genes was normalized against the gene expression level from the corresponding developmental stage animals raised on ground. Spaceflight altered the expression of larval genes involved in the maturation of plasmatocytes (macrophages) and their phagocytic response as well as the level of constitutive expression of pattern recognition receptors and opsonins that specifically recognize bacteria and of lysozymes antimicrobial peptide pathway and immune stress genes hallmarks of humoral immunity. Larval microarrays (FL 6 samples) are based on RNA extracted from 6 independent sets of 50 mid 3rd instar larvae reared in microgravity and collected on the day of landing after 12 days and 18.5 hours on the space shuttle and the same number of control larvae raised on ground (GL 6 samples). Adults microarrays (F1 3 samples) are based on RNA from 3 sets of 20 adult females each that emerged during spaceflight and within 4 hours of landing and the same number of adult females from the corresponding ground control containers (G1 3 samples).",
-            "title": "Drosophila melanogaster gene expression changes after spaceflight.",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-3",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Drosophila melanogaster gene expression changes after spaceflight."
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Drosophila melanogaster gene expression changes after spaceflight."
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-PANCAM-5-MOSAIC-OPS-V1.0",
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
+            "description": "NULL",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-pancam-5-mosaic-ops-v1.0_3yin-p8h3",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars exploration rover",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-PANCAM-5-MOSAIC-OPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-pancam-5-mosaic-ops-v1.0_3yin-p8h3",
-            "description": "NULL",
-            "title": "MER 2 MARS PANORAMIC CAMERA\n                                      MOSAICS RDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MER 2 MARS PANORAMIC CAMERA\n                                      MOSAICS RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://aeronet.gsfc.nasa.gov/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "temporal": "1993-01-01/2014-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://aeronet.gsfc.nasa.gov/new_web/Documents/Inversion_products_V2.pdf"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brent Holben",
+                "hasEmail": "mailto:Brent.N.Holben@nasa.gov"
+            },
+            "describedBy": "http://aeronet.gsfc.nasa.gov/new_web/Documents/Inversion_products_V2.pdf",
+            "describedByType": "application/pdf",
+            "description": "AERONET inversion code provides aerosoloptical properties in the total atmospheric column derived from the direct and diffuse radiation measured byAERONETCimel sun/sky-radiometers. AERONET inversion developmentand researchactivitiesare described in the papers by Dubovik and King, [2000], Dubovik et al. [2000], Dubovik et al. [2002a], Dubovik et al. [2002b], Dubovik et al., [2006a], Sinyuk et al. [2006]. The Version 2(V2)inversion (or retrieval)products are summarized below. These products are available through the internal analysis system&#x0022;demonstrat&#x0022; and the AERONET website. Adetailed description of V2 AERONET retrieval will be provided in the paper by Dubovik et al., [2006b].",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://aeronet.gsfc.nasa.gov/data_push/INV/INV_PFN_Level15_Daily_V2.tar.gz",
+                    "mediaType": "application/x-tar"
+                }
             ],
+            "identifier": "NASA-0000005__1",
+            "issued": "2018-06-25",
             "keyword": [
                 "inversions",
                 "satellite",
@@ -111514,82 +111524,46 @@
                 "clouds",
                 "aerosols"
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
-            "identifier": "NASA-0000005__1",
-            "description": "AERONET inversion code provides aerosoloptical properties in the total atmospheric column derived from the direct and diffuse radiation measured byAERONETCimel sun/sky-radiometers. AERONET inversion developmentand researchactivitiesare described in the papers by Dubovik and King, [2000], Dubovik et al. [2000], Dubovik et al. [2002a], Dubovik et al. [2002b], Dubovik et al., [2006a], Sinyuk et al. [2006]. The Version 2(V2)inversion (or retrieval)products are summarized below. These products are available through the internal analysis system&#x0022;demonstrat&#x0022; and the AERONET website. Adetailed description of V2 AERONET retrieval will be provided in the paper by Dubovik et al., [2006b].",
-            "title": "Level 1.5 Almucantar Inversion Products Phase Functions",
-            "describedByType": "application/pdf",
-            "programCode": [
-                "026:001"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://aeronet.gsfc.nasa.gov/data_push/INV/INV_PFN_Level15_Daily_V2.tar.gz",
-                    "mediaType": "application/x-tar"
-                }
+            "references": [
+                "http://aeronet.gsfc.nasa.gov/new_web/Documents/Inversion_products_V2.pdf"
             ],
             "spatial": "Global",
-            "describedBy": "http://aeronet.gsfc.nasa.gov/new_web/Documents/Inversion_products_V2.pdf",
-            "accrualPeriodicity": "irregular",
+            "temporal": "1993-01-01/2014-01-01",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Level 1.5 Almucantar Inversion Products Phase Functions"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/0D23ALHMHHT5",
             "citation": "Dalia B. Kirschbaum, Thomas A. Stanley, NASA GSFC. Dalia B. Kirschbaum, Thomas A. Stanley, NASA GSFC. Global_Landslide_Nowcast. Version 1.1. Global Landslide Nowcasts from LHASA L4  1 day 1 km x 1 km version 1.1 (Global_Landslide_Nowcast) at GES DISC. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/0D23ALHMHHT5. https://disc.gsfc.nasa.gov/datacollection/Global_Landslide_Nowcast_1.1.html. Digital Science Data.",
-            "issued": "2020-06-01",
-            "temporal": "2000-06-14T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-06-01",
-            "references": [
-                "https://doi.org/10.1002/2017EF000715",
-                "https://doi.org/10.5194/nhess-20-3413-2020"
-            ],
-            "keyword": [
-                "human dimensions",
-                "natural hazards",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Binita KC",
                 "hasEmail": "mailto:binita.kc@nasa.gov"
             },
+            "creator": "Dalia B. Kirschbaum, Thomas A. Stanley, NASA GSFC",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2036912694-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The Landslide Hazard Analysis for Situational Awareness (LHASA) model identifies locations with high potential for landslide occurrence at a daily temporal resolution.  LHASA combines satellite\u2010based precipitation estimates with a landslide susceptibility map derived from information on slope, geology, road networks, fault zones, and forest loss. When rainfall is considered to be extreme and susceptibility values are moderate to very high, a \u201cnowcast\u201d is issued to indicate the times and places where landslides are more probable.  Although the model could be run every half hour, this archive contains a daily record derived from a retrospective model run and spatial coverage is from 60\u00b0N to 60\u00b0S .",
-            "editor": "Dalia B. Kirschbaum, Thomas A. Stanley, NASA GSFC",
-            "series-name": "Global_Landslide_Nowcast",
-            "creator": "Dalia B. Kirschbaum, Thomas A. Stanley, NASA GSFC",
-            "title": "Global Landslide Nowcast from LHASA L4  1 day 1 km x 1 km version 1.1 (Global_Landslide_Nowcast) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/Global_Landslide_Nowcast_1.1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F0D23ALHMHHT5",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F0D23ALHMHHT5",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -111599,31 +111573,31 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/Global_Landslide_Nowcast_1.1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.\n",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.\n",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/Global_Landslide_Nowcast_1.1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Landslide/Global_Landslide_Nowcast.1.1/",
-                    "description": "Access the data via HTTPS.\n",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.\n",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Landslide/Global_Landslide_Nowcast.1.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Landslide/Global_Landslide_Nowcast.1.1/doc/README.Global_Landslide_Nowcast.pdf",
-                    "description": "README Document\n\n",
                     "@type": "dcat:Distribution",
+                    "description": "README Document\n\n",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Landslide/Global_Landslide_Nowcast.1.1/doc/README.Global_Landslide_Nowcast.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://landslides.nasa.gov/",
-                    "description": "Introduction to NASA landslides research.\n",
                     "@type": "dcat:Distribution",
+                    "description": "Introduction to NASA landslides research.\n",
+                    "downloadURL": "https://landslides.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
@@ -111633,47 +111607,53 @@
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "editor": "Dalia B. Kirschbaum, Thomas A. Stanley, NASA GSFC",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/Global_Landslide_Nowcast_1.1.png",
+            "identifier": "C2036912694-GES_DISC",
+            "issued": "2020-06-01",
+            "keyword": [
+                "human dimensions",
+                "natural hazards",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/0D23ALHMHHT5",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-06-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1002/2017EF000715",
+                "https://doi.org/10.5194/nhess-20-3413-2020"
+            ],
+            "series-name": "Global_Landslide_Nowcast",
             "spatial": "-180.0 -60.0 180.0 60.0",
+            "temporal": "2000-06-14T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Landslide Project",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Landslide Nowcast from LHASA L4  1 day 1 km x 1 km version 1.1 (Global_Landslide_Nowcast) at GES DISC"
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
-            "identifier": "NASA-634",
             "description": "Data Dictionary and Index Files",
-            "title": "PDS Data Dictionary (1r76)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -111681,428 +111661,426 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-634",
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
+            "title": "PDS Data Dictionary (1r76)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3008-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2011-07-13T23:57:08.000 to 2011-07-14T01:46:37.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3008-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars express",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3008-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3008-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2011-07-13T23:57:08.000 to 2011-07-14T01:46:37.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3008 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3008 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-FC2-5-CERESHAMODTMSPG-V1.0",
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
+            "description": "Abstract ======== This data set contains the Ceres digital terrain model based on the Dawn High Altitude Mapping orbit (HAMO) Framing Camera 2 (FC2) images and derived by using the stereo photo-grametric (SPG) method. The HAMO DTM covers approximately 98% of the Ceres surface (few permanently shadowed areas near the poles required interpolation). The a DTM has a lateral spacing of ~136.7 m/pixel (60 pixel/degree) and a vertical accuracy of about 10 m.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-fc2-5-cereshamodtmspg-v1.0_3yz6-rs9j",
+            "issued": "2021-05-21",
+            "keyword": [
+                "1 ceres",
+                "dawn mission to vesta and ceres"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-FC2-5-CERESHAMODTMSPG-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-fc2-5-cereshamodtmspg-v1.0_3yz6-rs9j",
-            "description": "Abstract ======== This data set contains the Ceres digital terrain model based on the Dawn High Altitude Mapping orbit (HAMO) Framing Camera 2 (FC2) images and derived by using the stereo photo-grametric (SPG) method. The HAMO DTM covers approximately 98% of the Ceres surface (few permanently shadowed areas near the poles required interpolation). The a DTM has a lateral spacing of ~136.7 m/pixel (60 pixel/degree) and a vertical accuracy of about 10 m.",
-            "title": "DAWN FC2 DERIVED CERES HAMO DTM SPG V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "DAWN FC2 DERIVED CERES HAMO DTM SPG V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5270/EN1-a1rc3jf",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "European Space Agency. 2021-10-20. Reduced Resolution Geophysical Product for Ocean, Land and Atmosphere. Version 4. MODAPS at GSFC. https://doi.org/10.5270/EN1-a1rc3jf.",
-            "issued": "2018-05-22",
-            "temporal": "2002-04-29T00:00:00Z/2012-04-08T12:00:45Z",
-            "@type": "dcat:Dataset",
-            "modified": "2012-04-08",
-            "keyword": [
-                "clouds",
-                "surface radiative properties",
-                "atmosphere",
-                "landscape",
-                "earth science",
-                "ocean optics",
-                "land surface",
-                "oceans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "MODAPS USER SERVICES",
                 "hasEmail": "mailto:MODAPSUSO@lists.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
-            "identifier": "C2151227530-LAADS",
-            "description": "The Medium Resolution Imaging Spectrometer (MERIS) is one of 10 sensors deployed in March of 2002 on board the polar-orbiting Envisat-1 environmental research satellite by the European Space Agency (ESA). The MERIS instrument is a moderate-resolution wide field-of-view push-broom imaging spectroradiometer capable of sensing in the 390 nm to 1040 nm spectral range. Being a programmable instrument, it had the unique capability of selectively adjusting the width and location of its 15 bands through ground command. The instrument has a 68.5-degree field of view and a swath width of 1150 meters, providing a global coverage every 3 days at 300 m resolution.  Communication with the Envisat-1 satellite was lost suddenly on the 8th of April, 2012, just weeks after celebrating its 10th year in orbit. All attempts to re-establish contact were unsuccessful, and the end of the mission was declared on May 9th, 2012.\r\n\r\nThe 4th reprocessing cycle, in 2020, has produced both the full-resolution and reduced-resolution L1 and L2 MERIS products. EN1_MDSI_MER_RR__2P is the short-name for the MERIS Level-2 reduced resolution, geophysical product for ocean, land, and atmosphere. This Level-2 product comes in a netCDF4 package that contains both instrument and science measurements, and a Manifest file that provides metadata information describing the product. Each Level-2 product contains 64 measurement files that break down thus: 13 files containing water-leaving reflectance, 13 files containing land surface reflectance and 13 files containing the TOA reflectance (for all bands except those dedicated to measuring atmospheric gas - M11 and M15), and several files containing additional measurements on ocean, land, and atmospheric parameters and annotation.",
-            "release-place": "MODAPS at GSFC",
             "creator": "European Space Agency",
-            "title": "Reduced Resolution Geophysical Product for Ocean, Land and Atmosphere",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Medium Resolution Imaging Spectrometer (MERIS) is one of 10 sensors deployed in March of 2002 on board the polar-orbiting Envisat-1 environmental research satellite by the European Space Agency (ESA). The MERIS instrument is a moderate-resolution wide field-of-view push-broom imaging spectroradiometer capable of sensing in the 390 nm to 1040 nm spectral range. Being a programmable instrument, it had the unique capability of selectively adjusting the width and location of its 15 bands through ground command. The instrument has a 68.5-degree field of view and a swath width of 1150 meters, providing a global coverage every 3 days at 300 m resolution.  Communication with the Envisat-1 satellite was lost suddenly on the 8th of April, 2012, just weeks after celebrating its 10th year in orbit. All attempts to re-establish contact were unsuccessful, and the end of the mission was declared on May 9th, 2012.\r\n\r\nThe 4th reprocessing cycle, in 2020, has produced both the full-resolution and reduced-resolution L1 and L2 MERIS products. EN1_MDSI_MER_RR__2P is the short-name for the MERIS Level-2 reduced resolution, geophysical product for ocean, land, and atmosphere. This Level-2 product comes in a netCDF4 package that contains both instrument and science measurements, and a Manifest file that provides metadata information describing the product. Each Level-2 product contains 64 measurement files that break down thus: 13 files containing water-leaving reflectance, 13 files containing land surface reflectance and 13 files containing the TOA reflectance (for all bands except those dedicated to measuring atmospheric gas - M11 and M15), and several files containing additional measurements on ocean, land, and atmospheric parameters and annotation.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5270%2FEN1-a1rc3jf",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5270%2FEN1-a1rc3jf",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/EN1_MDSI_MER_RR__2P--489",
-                    "description": "Search and order MERIS product from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order MERIS product from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/EN1_MDSI_MER_RR__2P--489",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earth.esa.int/eogateway/search?skipDetection=true&text=&category=Document+library&filter=Envisat%2CMERIS",
-                    "description": "MERIS Product Handbook/ATBD",
                     "@type": "dcat:Distribution",
+                    "description": "MERIS Product Handbook/ATBD",
+                    "downloadURL": "https://earth.esa.int/eogateway/search?skipDetection=true&text=&category=Document+library&filter=Envisat%2CMERIS",
+                    "mediaType": "text/html",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/489/EN1_MDSI_MER_RR__2P/",
-                    "description": "Product direct download from LAADS archive",
                     "@type": "dcat:Distribution",
+                    "description": "Product direct download from LAADS archive",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/489/EN1_MDSI_MER_RR__2P/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 }
             ],
+            "identifier": "C2151227530-LAADS",
+            "issued": "2018-05-22",
+            "keyword": [
+                "clouds",
+                "surface radiative properties",
+                "atmosphere",
+                "landscape",
+                "earth science",
+                "ocean optics",
+                "land surface",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5270/EN1-a1rc3jf",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2012-04-08",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-04-29T00:00:00Z/2012-04-08T12:00:45Z",
             "theme": [
                 "MULTI-TASTE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Reduced Resolution Geophysical Product for Ocean, Land and Atmosphere"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/209/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2010-09-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "nasa",
-                "ames",
-                "dashlink"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Deniz Gencaga",
                 "hasEmail": "mailto:dgencaga@gmail.com"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_209",
             "description": "Understanding the origins of life has been one of the greatest dreams throughout history. It is now known that star-forming regions contain complex organic molecules, known as Polycyclic Aromatic Hydrocarbons (PAHs), each of which has particular infrared spectral characteristics. By understanding which PAH species are found in specific star-forming regions, we can better understand the biochemistry that takes place in interstellar clouds. Identifying and classifying PAHs is not an easy task: we can only observe a single superposition of PAH spectra at any given astrophysical site, with the PAH species perhaps numbering in the hundreds or even thousands. This is a challenging source separation problem since we have only one observation composed of numerous mixed sources. However, it is made easier with the help of a library of hundreds of PAH spectra. In order to separate PAH molecules from their mixture, we need to identify the specific species and their unique concentrations that would provide the given mixture. We develop a Bayesian approach for this problem where sources are separated from their mixture by Metropolis Hastings algorithm. Separated PAH concentrations are provided with their error bars, illustrating the uncertainties involved in the estimation process. The approach is demonstrated on synthetic spectral mixtures using spectral resolutions from the Infrared Space Observatory (ISO). Performance of the method is tested for different noise levels.",
-            "title": "Characterization of Interstellar Organic Molecules",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/MaxEnt_2008_Gencaga_etal.pdf",
-                    "description": "Characterization of Interstellar Organic Molecules",
                     "@type": "dcat:Distribution",
+                    "description": "Characterization of Interstellar Organic Molecules",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/MaxEnt_2008_Gencaga_etal.pdf",
+                    "mediaType": "application/pdf",
                     "title": "MaxEnt_2008_Gencaga_etal.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_209",
+            "issued": "2010-09-22",
+            "keyword": [
+                "nasa",
+                "ames",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/209/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Characterization of Interstellar Organic Molecules"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MIRO-3-ESC1-67P-V2.0",
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
+            "description": "This data set contains Spectroscopic and Continuum, level 3 data, in the form of table files, taken during the ROSETTA COMET ESCORT 1 phase of the Rosetta mission to comet 67P/CHURYUMOV-GERASIMENKO by the MIRO instrument.  It supercedes dataset RO-C-MIRO-3-ESC1-67P-V1.0. The updates include a new calibration algorithm and modified documentation.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-miro-3-esc1-67p-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MIRO-3-ESC1-67P-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-miro-3-esc1-67p-v2.0",
-            "description": "This data set contains Spectroscopic and Continuum, level 3 data, in the form of table files, taken during the ROSETTA COMET ESCORT 1 phase of the Rosetta mission to comet 67P/CHURYUMOV-GERASIMENKO by the MIRO instrument.  It supercedes dataset RO-C-MIRO-3-ESC1-67P-V1.0. The updates include a new calibration algorithm and modified documentation.",
-            "title": "ROSETTA-ORBITER 67P MIRO 3 ESC1 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P MIRO 3 ESC1 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-ASPERA3-3-RDR-ELS-EXT6-V1.0",
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
+            "description": "This data set contains calibrated Mars Express ASPERA-3 Electron Spectrometer (ELS) data for the sixth mission extension (January 1, 2017 - Dec. 31, 2018).  These data are provided in units of Differential Number Flux (DNF): cnts/(cm**2-sr-sec-eV)",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-aspera3-3-rdr-els-ext6-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars express"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-ASPERA3-3-RDR-ELS-EXT6-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-aspera3-3-rdr-els-ext6-v1.0",
-            "description": "This data set contains calibrated Mars Express ASPERA-3 Electron Spectrometer (ELS) data for the sixth mission extension (January 1, 2017 - Dec. 31, 2018).  These data are provided in units of Differential Number Flux (DNF): cnts/(cm**2-sr-sec-eV)",
-            "title": "MARS EXPRESS ASPERA-3 CAL RDR ELECTRON SPECTROMTR EXT6 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS ASPERA-3 CAL RDR ELECTRON SPECTROMTR EXT6 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASTER/AST_L1AE.003",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA/METI/AIST/Japan Spacesystems and U.S./Japan ASTER Science Team. 2001-04-30. AST_L1AE.003. Expedited ASTER Level 1A Data Set - Reconstructed, unprocessed instrument data. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes DAAC. https://doi.org/10.5067/ASTER/AST_L1AE.003. https://doi.org/10.5067/ASTER/AST_L1AE.003. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2002-03-14",
-            "temporal": "2000-03-04T20:34:04Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-09-14",
-            "keyword": [
-                "infrared wavelengths",
-                "earth science",
-                "national geospatial data asset",
-                "ngda",
-                "visible wavelengths",
-                "spectral/engineering"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:lpdaac@usgs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
-            "identifier": "C179460405-LPDAAC_ECS",
-            "description": "The Advanced Spaceborne Thermal Emission and Reflection Radiometer (ASTER) Expedited Level 1A Reconstructed Unprocessed Instrument Data (AST_L1AE) product contains reconstructed, unprocessed instrument digital data derived from the acquired telemetry streams of the telescopes: Visible and Near Infrared (VNIR), Shortwave Infrared (SWIR), and Thermal Infrared (TIR). This data product is similar to the (AST_L1A) (http://doi.org/10.5067/ASTER/AST_L1A.003) with a few notable exceptions. These include:\r\n* The AST_L1AE is available for download within 48 hours of acquisition in support of field calibration and validation efforts, in addition to emergency response for natural disasters where the quick turn-around time from acquisition to availability would prove beneficial in initial damage or impact assessments.\r\n* The registration quality of the AST_L1AE is likely to be lower than the AST_L1A, and may vary from scene to scene.\r\n* The AST_L1AE data product does not contain the VNIR 3B (aft-viewing) Band.\r\n* This dataset does not have short-term calibration for the Thermal Infrared (TIR) sensor.\r\n* The AST_L1AE data product is only available for download 30 days after acquisition. It is then removed and reprocessed into an AST_L1A product.",
-            "series-name": "AST_L1AE.003",
             "creator": "NASA/METI/AIST/Japan Spacesystems and U.S./Japan ASTER Science Team",
-            "title": "ASTER Expedited L1A Reconstructed Unprocessed Instrument Data V003",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Advanced Spaceborne Thermal Emission and Reflection Radiometer (ASTER) Expedited Level 1A Reconstructed Unprocessed Instrument Data (AST_L1AE) product contains reconstructed, unprocessed instrument digital data derived from the acquired telemetry streams of the telescopes: Visible and Near Infrared (VNIR), Shortwave Infrared (SWIR), and Thermal Infrared (TIR). This data product is similar to the (AST_L1A) (http://doi.org/10.5067/ASTER/AST_L1A.003) with a few notable exceptions. These include:\r\n* The AST_L1AE is available for download within 48 hours of acquisition in support of field calibration and validation efforts, in addition to emergency response for natural disasters where the quick turn-around time from acquisition to availability would prove beneficial in initial damage or impact assessments.\r\n* The registration quality of the AST_L1AE is likely to be lower than the AST_L1A, and may vary from scene to scene.\r\n* The AST_L1AE data product does not contain the VNIR 3B (aft-viewing) Band.\r\n* This dataset does not have short-term calibration for the Thermal Infrared (TIR) sensor.\r\n* The AST_L1AE data product is only available for download 30 days after acquisition. It is then removed and reprocessed into an AST_L1A product.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASTER%2FAST_L1AE.003",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASTER%2FAST_L1AE.003",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASTER/AST_L1AE.003",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ASTER/AST_L1AE.003",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/ASTT/AST_L1AE.003/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/ASTT/AST_L1AE.003/",
+                    "mediaType": "text/html",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C179460405-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C179460405-LPDAAC_ECS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://asterweb.jpl.nasa.gov/data_products.asp",
-                    "description": "The ASTER home page is maintained through NASA's Jet Propulsion Laboratory and documents various aspects of the ASTER mission. http://asterweb.jpl.nasa.gov/ ",
                     "@type": "dcat:Distribution",
+                    "description": "The ASTER home page is maintained through NASA's Jet Propulsion Laboratory and documents various aspects of the ASTER mission. http://asterweb.jpl.nasa.gov/ ",
+                    "downloadURL": "http://asterweb.jpl.nasa.gov/data_products.asp",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/70/AST_L1_ATBD.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/70/AST_L1_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://asterweb.jpl.nasa.gov/content/03_data/04_Documents/ASTERHigherLevelUserGuideVer2May01.pdf",
-                    "description": "ASTER Higher-Level Product User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "ASTER Higher-Level Product User Guide",
+                    "downloadURL": "http://asterweb.jpl.nasa.gov/content/03_data/04_Documents/ASTERHigherLevelUserGuideVer2May01.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/175/ASTER_L1_Product_Specifications.pdf",
-                    "description": "The ASTER Level-1T Product Specification provides a description of the data file.",
                     "@type": "dcat:Distribution",
+                    "description": "The ASTER Level-1T Product Specification provides a description of the data file.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/175/ASTER_L1_Product_Specifications.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C179460405-LPDAAC_ECS",
+            "issued": "2002-03-14",
+            "keyword": [
+                "infrared wavelengths",
+                "earth science",
+                "national geospatial data asset",
+                "ngda",
+                "visible wavelengths",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASTER/AST_L1AE.003",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-09-14",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "series-name": "AST_L1AE.003",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-03-04T20:34:04Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Terra",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ASTER Expedited L1A Reconstructed Unprocessed Instrument Data V003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5270/S5P-3p6lnwd",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Copernicus Sentinel data processed by ESA, Koninklijk Nederlands Meteorologisch Instituut (KNMI)/Netherlands Institute for Space Research (SRON). 2019-08-19. S5P_L2__CH4____HiR. Version 1. Sentinel-5P TROPOMI Methane CH4 1-Orbit L2 5.5km x 7km. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5270/S5P-3p6lnwd. https://disc.gsfc.nasa.gov/datacollection/S5P_L2__CH4____HiR_1.html. Digital Science Data.",
-            "issued": "2017-05-05",
-            "temporal": "2019-08-06T02:41:41Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-05-05",
-            "keyword": [
-                "atmospheric chemistry",
-                "atmosphere",
-                "earth science"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jochen Landgraf",
                 "hasEmail": "mailto:j.landgraf@sron.nl"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1627516288-GES_DISC",
-            "description": "Starting from August 6th in 2019, Sentinel-5P TROPOMI along-track high spatial resolution (~5.5km at nadir) has been implemented.\nFor data before August 6th of 2019, please check S5P_L2__CH4____1 data collection.\n\nThe Copernicus Sentinel-5 Precursor (Sentinel-5P or S5P) satellite mission is one of the European Space Agency's (ESA) new mission family - Sentinels, and it is a joint initiative between the Kingdom of the Netherlands and the ESA. The sole payload on Sentinel-5P is the TROPOspheric Monitoring Instrument (TROPOMI), which is a nadir-viewing 108 degree Field-of-View push-broom grating hyperspectral spectrometer, covering the wavelength of ultraviolet-visible (UV-VIS, 270nm to 495nm), near infrared (NIR, 675nm to 775nm), and shortwave infrared (SWIR, 2305nm-2385nm). Sentinel-5P is the first of the Atmospheric Composition Sentinels and is expected to provide measurements of ozone, NO2, SO2, CH4, CO, formaldehyde, aerosols and cloud at high spatial, temporal and spectral resolutions.\n\nThe retrieval algorithm for Sentinel-5P TROPOMI methane product is a physics based method that uses the Oxygen-A band (760 nm) and absorption bands in shortwave infrared spectrum. In Sentinel-5P/TROPOMI methane algorithm, the atmosphere forward model simulates the absorbing gas (oxygen, methane, water vapor, and carbon monoxide) optical properties, as well as aerosol optical properties with size distribution, refractive index, and number concentration. The inversion is performed based on the forward calculation, the measurement, and the prior information. Cloud filtering is critical in methane retrieval, S5P methane algorithm applies re-gridded Visible Infrared Imaging Radiometer Suite (VIIRS) cloud mask data. Additional cloud filters based on S5P/TROPOMI measurements and the FRESCO apparent surface pressure will be applied when VIIRS cloud data are not available. Other current data filters in the retrieval algorithm include land-only pixels (excluding mountainous areas), spectrum intensity, solar zenith angle and instrument zenith angle. \n\nThe S5P/TROPOMI methane retrieval is for non-time-critical (NTC) data stream only, and its main outputs include the column averaged dry air mixing ratio of methane, the random error, and the biased corrected dry air methane fraction data based on the retrieved surface albedo. \n\nStarting from orbit #12432 on March 7th of 2020, the S-NPP auxiliary cloud data source used in the methane product data processing has been transitioned from the VIIRS Cloud Mask (VCM) into the Enterprise Cloud Mask (ECM).\n\nThe data are stored in an enhanced netCDF-4 format.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "S5P_L2__CH4____HiR",
             "creator": "Copernicus Sentinel data processed by ESA, Koninklijk Nederlands Meteorologisch Instituut (KNMI)/Netherlands Institute for Space Research (SRON)",
-            "title": "Sentinel-5P TROPOMI Methane CH4 1-Orbit L2 5.5km x 7km V1 (S5P_L2__CH4____HiR) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/S5P_OFFL_L2__CH4____HiR_1.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Starting from August 6th in 2019, Sentinel-5P TROPOMI along-track high spatial resolution (~5.5km at nadir) has been implemented.\nFor data before August 6th of 2019, please check S5P_L2__CH4____1 data collection.\n\nThe Copernicus Sentinel-5 Precursor (Sentinel-5P or S5P) satellite mission is one of the European Space Agency's (ESA) new mission family - Sentinels, and it is a joint initiative between the Kingdom of the Netherlands and the ESA. The sole payload on Sentinel-5P is the TROPOspheric Monitoring Instrument (TROPOMI), which is a nadir-viewing 108 degree Field-of-View push-broom grating hyperspectral spectrometer, covering the wavelength of ultraviolet-visible (UV-VIS, 270nm to 495nm), near infrared (NIR, 675nm to 775nm), and shortwave infrared (SWIR, 2305nm-2385nm). Sentinel-5P is the first of the Atmospheric Composition Sentinels and is expected to provide measurements of ozone, NO2, SO2, CH4, CO, formaldehyde, aerosols and cloud at high spatial, temporal and spectral resolutions.\n\nThe retrieval algorithm for Sentinel-5P TROPOMI methane product is a physics based method that uses the Oxygen-A band (760 nm) and absorption bands in shortwave infrared spectrum. In Sentinel-5P/TROPOMI methane algorithm, the atmosphere forward model simulates the absorbing gas (oxygen, methane, water vapor, and carbon monoxide) optical properties, as well as aerosol optical properties with size distribution, refractive index, and number concentration. The inversion is performed based on the forward calculation, the measurement, and the prior information. Cloud filtering is critical in methane retrieval, S5P methane algorithm applies re-gridded Visible Infrared Imaging Radiometer Suite (VIIRS) cloud mask data. Additional cloud filters based on S5P/TROPOMI measurements and the FRESCO apparent surface pressure will be applied when VIIRS cloud data are not available. Other current data filters in the retrieval algorithm include land-only pixels (excluding mountainous areas), spectrum intensity, solar zenith angle and instrument zenith angle. \n\nThe S5P/TROPOMI methane retrieval is for non-time-critical (NTC) data stream only, and its main outputs include the column averaged dry air mixing ratio of methane, the random error, and the biased corrected dry air methane fraction data based on the retrieved surface albedo. \n\nStarting from orbit #12432 on March 7th of 2020, the S-NPP auxiliary cloud data source used in the methane product data processing has been transitioned from the VIIRS Cloud Mask (VCM) into the Enterprise Cloud Mask (ECM).\n\nThe data are stored in an enhanced netCDF-4 format.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5270%2FS5P-3p6lnwd",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5270%2FS5P-3p6lnwd",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -112112,90 +112090,121 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/S5P_L2__CH4____HiR_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/S5P_L2__CH4____HiR_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/opendap/S5P_TROPOMI_Level2/S5P_L2__CH4____HiR.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/opendap/S5P_TROPOMI_Level2/S5P_L2__CH4____HiR.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/data/S5P_TROPOMI_Level2/S5P_L2__CH4____HiR.1",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/data/S5P_TROPOMI_Level2/S5P_L2__CH4____HiR.1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sentinel.esa.int/documents/247904/3541451/Sentinel-5P-Methane-Product-Readme-File",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://sentinel.esa.int/documents/247904/3541451/Sentinel-5P-Methane-Product-Readme-File",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=S5P_L2__CH4____HiR_1",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=S5P_L2__CH4____HiR_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sentinel.esa.int/documents/247904/2476257/Sentinel-5P-TROPOMI-ATBD-Methane-retrieval",
-                    "description": "Algorithm Theoretical Basis Document",
                     "@type": "dcat:Distribution",
+                    "description": "Algorithm Theoretical Basis Document",
+                    "downloadURL": "https://sentinel.esa.int/documents/247904/2476257/Sentinel-5P-TROPOMI-ATBD-Methane-retrieval",
+                    "mediaType": "text/html",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sentinel.esa.int/documents/247904/2474726/Sentinel-5P-Level-2-Product-User-Manual-Methane",
-                    "description": "Product User Manual Document",
                     "@type": "dcat:Distribution",
+                    "description": "Product User Manual Document",
+                    "downloadURL": "https://sentinel.esa.int/documents/247904/2474726/Sentinel-5P-Level-2-Product-User-Manual-Methane",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sentinel.esa.int/web/sentinel/missions/sentinel-5p",
-                    "description": "ESA Copernicus Sentinel 5P Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "ESA Copernicus Sentinel 5P Home Page",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/S5P_OFFL_L2__CH4____HiR_1.png",
+            "identifier": "C1627516288-GES_DISC",
+            "issued": "2017-05-05",
+            "keyword": [
+                "atmospheric chemistry",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5270/S5P-3p6lnwd",
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
+            "series-name": "S5P_L2__CH4____HiR",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2019-08-06T02:41:41Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Sentinel-5P",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sentinel-5P TROPOMI Methane CH4 1-Orbit L2 5.5km x 7km V1 (S5P_L2__CH4____HiR) at GES DISC"
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
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Christopher Rumsey",
+                "hasEmail": "mailto:c.l.rumsey@nasa.gov"
+            },
+            "description": "This grouping contains more recent compressible-flow cases.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://turbmodels.larc.nasa.gov/Bradshaw/r1-7/nagano.tar.gz",
+                    "mediaType": "application/x-gzip"
+                }
             ],
+            "identifier": "NASA-847__8",
+            "issued": "2018-06-25",
             "keyword": [
                 "compressible",
                 "turbulence",
@@ -112204,158 +112213,122 @@
                 "cases",
                 "flow"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Christopher Rumsey",
-                "hasEmail": "mailto:c.l.rumsey@nasa.gov"
-            },
+            "landingPage": "http://turbmodels.larc.nasa.gov/bradshaw.html",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:023"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-847__8",
-            "description": "This grouping contains more recent compressible-flow cases.",
-            "title": "Collaborative Testing of Turbulence Models: Other Flow Cases",
-            "programCode": [
-                "026:023"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://turbmodels.larc.nasa.gov/Bradshaw/r1-7/nagano.tar.gz",
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
+            "title": "Collaborative Testing of Turbulence Models: Other Flow Cases"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/60QSXDPEL5DP",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Soil Moisture Active Passive (SMAP) L4 Soil Moisture Ancillary LDAS Parameters Files V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/60QSXDPEL5DP.",
-            "issued": "2015-03-31",
-            "temporal": "2015-01-31T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-06-30",
-            "keyword": [
-                "land surface",
-                "microwave",
-                "earth science",
-                "soils",
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
-            "identifier": "C1539063295-NSIDC_ECS",
             "description": "This ancillary SMAP product contains three dynamic Land Data Assimilation Systems (LDAS) data sets. These data sets include Brightness Temperature (TB) scaling parameters; catchment model parameters such as topographic statistics, soil texture, and soil hydraulic parameters; and LDAS L-band microwave radiative transfer model parameters.",
-            "title": "Soil Moisture Active Passive (SMAP) L4 Soil Moisture Ancillary LDAS Parameters Files V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F60QSXDPEL5DP",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F60QSXDPEL5DP",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_ANC/SMAP_L4_SM_ANC_PARAM.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_ANC/SMAP_L4_SM_ANC_PARAM.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SMAP_L4_SM_ANC_PARAM+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SMAP_L4_SM_ANC_PARAM+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/60QSXDPEL5DP",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/60QSXDPEL5DP",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/60QSXDPEL5DP",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/60QSXDPEL5DP",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1539063295-NSIDC_ECS",
+            "issued": "2015-03-31",
+            "keyword": [
+                "land surface",
+                "microwave",
+                "earth science",
+                "soils",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/60QSXDPEL5DP",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-06-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -86.4 180.0 86.4",
+            "temporal": "2015-01-31T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Soil Moisture Active Passive (SMAP) L4 Soil Moisture Ancillary LDAS Parameters Files V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/Aura/OMI/DATA2008",
             "citation": "Pepijn Veefkind. 2012-01-20. OMCLDO2G. Version 003. OMI/Aura Cloud Pressure and Fraction (O2-O2 Absorption) Daily L2 Global Gridded 0.25 degree x 0.25 degree V3. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/OMI/DATA2008. https://disc.gsfc.nasa.gov/datacollection/OMCLDO2G_003.html. Digital Science Data.",
-            "issued": "2004-10-01",
-            "temporal": "2004-10-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2012-01-20",
-            "references": [
-                "https://doi.org/10.1109/TGRS.2006.869987",
-                "https://doi.org/10.1109/TGRS.2006.872935",
-                "https://doi.org/10.1117/12.627013"
-            ],
-            "keyword": [
-                "atmosphere",
-                "clouds",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JENNIFER WEI",
                 "hasEmail": "mailto:jennifer.c.wei@nasa.gov"
             },
+            "creator": "Pepijn Veefkind",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1266136098-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "This Level-2G daily global gridded product OMCLDO2G is based on the pixel level OMI Level-2 CLDO2 product OMCLDO2. This level-2G global cloud product (OMCLDO2G) is based on the spectral fitting of O2-O2 absorption band at 477 nm using DOAS technique. This product contains cloud pressure, cloud fraction, slant column O2-O2 and Ozone, Ring coefficients, uncertainties in derived parameters, terrain and geolocation information, solar and satellite viewing angles, and quality flags. The short name for this Level-2 OMI cloud product is OMCLDO2G and the lead scientist for this product and for OMCLDO2 (the data source of OMCLDO2G) is KNMI scientist Dr. Pepijn Veefkind. OMCLDO2G data product is a special Level-2 Global Gridded Product where pixel level data (OMCLDO2) are binned into 0.25x0.25 degree global grids. It contains the OMCLDO2 data for all L2 scenes that have observation time between UTC times of 00:00:00 and 23:59:59.9999. All data pixels that fall in a grid are saved 'Without Averaging'. Scientists can apply a data filtering scheme of their choice and create new gridded products.\n\nThe OMCLDO2G product files are stored in the version 5 Hierarchical Data Format (HDF-EOS5). Each daily data file contains data from the day lit portion of the orbits (~14 orbits) and is roughly 85 MB in size.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OMCLDO2G",
-            "creator": "Pepijn Veefkind",
-            "title": "OMI/Aura Cloud Pressure and Fraction (O2-O2 Absorption) Daily L2 Global Gridded 0.25 degree x 0.25 degree V3 (OMCLDO2G) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMCLDO2G_003.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FOMI%2FDATA2008",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FOMI%2FDATA2008",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -112365,73 +112338,73 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMCLDO2G_003.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMCLDO2G_003.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/Aura_OMI_Level2G/OMCLDO2G.003/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/Aura_OMI_Level2G/OMCLDO2G.003/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMCLDO2G_003",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMCLDO2G_003",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level2G/OMCLDO2G.003/doc/README.OMCLDO2G.txt",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level2G/OMCLDO2G.003/doc/README.OMCLDO2G.txt",
+                    "mediaType": "text/html",
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
-                    "downloadURL": "http://docserver.gesdisc.eosdis.nasa.gov/public/project/OMI/OMCLDO2G.fs",
-                    "description": "File Specification Document",
                     "@type": "dcat:Distribution",
+                    "description": "File Specification Document",
+                    "downloadURL": "http://docserver.gesdisc.eosdis.nasa.gov/public/project/OMI/OMCLDO2G.fs",
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
-                    "downloadURL": "http://projects.knmi.nl/omi/research/news/newsWrap.php?language=only_enhttps%3A%2F%2Fwww.knmi.nl%2FomitimeFrame%3Dlatesthttps%3A%2F%2Fwww.knmi.nl%2Fomichoise%3Dpage",
-                    "description": "OMI KNMI Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "OMI KNMI Home Page",
+                    "downloadURL": "http://projects.knmi.nl/omi/research/news/newsWrap.php?language=only_enhttps%3A%2F%2Fwww.knmi.nl%2FomitimeFrame%3Dlatesthttps%3A%2F%2Fwww.knmi.nl%2Fomichoise%3Dpage",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithm/ATBD-OMI-03.pdf",
-                    "description": "OMI Algorithm Theoretical Basis Documents",
                     "@type": "dcat:Distribution",
+                    "description": "OMI Algorithm Theoretical Basis Documents",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithm/ATBD-OMI-03.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_OMI_Level2G/OMCLDO2G.003/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_OMI_Level2G/OMCLDO2G.003/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
@@ -112447,420 +112420,449 @@
                     "title": "View this dataset's publications"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMCLDO2G_003.png",
+            "identifier": "C1266136098-GES_DISC",
+            "issued": "2004-10-01",
+            "keyword": [
+                "atmosphere",
+                "clouds",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/OMI/DATA2008",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2012-01-20",
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
+            "series-name": "OMCLDO2G",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2004-10-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OMI/Aura Cloud Pressure and Fraction (O2-O2 Absorption) Daily L2 Global Gridded 0.25 degree x 0.25 degree V3 (OMCLDO2G) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/TRACE-A/TraceGas_AircraftInSitu_DC8_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2024-03-11. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/TRACE-A/TraceGas_AircraftInSitu_DC8_Data_1.",
-            "issued": "1992-09-01",
-            "temporal": "1990-03-13T00:00:00Z/1992-11-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "1992-10-27",
-            "keyword": [
-                "aerosols",
-                "atmosphere",
-                "atmospheric chemistry",
-                "earth science"
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
-            "identifier": "C2813461507-LARC_CLOUD",
             "description": "TRACE-A_TraceGas_AircraftInSitu_DC8_Data is the in-situ trace gas data collected onboard the DC-8 aircraft during the Transport and Atmospheric Chemistry near the Equator - Atlantic (TRACE-A) suborbital campaign. Data from the Two Photon - Laser Induced Fluorescence (TP-LIF) and Differential Absorption of CO, CH4, N2O Measurements (DACOM) instruments are featured in this collection. Data collection for this product is complete.\r\n\r\nThe TRACE-A mission was a part of NASA\u2019s Global Tropospheric Experiment (GTE) \u2013 an assemblage of missions conducted from 1983-2001 with various research goals and objectives.\u202fTRACE-A was conducted in the Atlantic from September 21 to October 24, 1992. TRACE-A had the objective of determining the cause and source of the high concentrations of ozone that accumulated over the Atlantic Ocean between southern Africa and South America from August to October.\u202fNASA partnered with the Brazilian Space Agency (INPE) to accomplish this goal.\u202f \r\n\r\nThe NASA DC-8 aircraft\u202fand\u202fozonesondes\u202fwere\u202futilized during TRACE-A to collect the necessary data. The DC-8 was equipped with 19 instruments. A few\u202finstruments on the DC-8 include the Differential Absorption Lidar (DIAL),\u202fthe Laser-Induced Fluorescence, the O3-NO Ethylene/Forward Scattering Spectrometer, the Modified\u202fLicor, and the DACOM IR Laser Spectrometer. The DIAL was responsible for a variety of measurements, which include Nadir IR aerosols, Nadir UV aerosols, Zenith IR aerosols, Zenith VS aerosols, ozone,\u202fand ozone column. The Laser-Induced Fluorescence instrument\u202fcollected measurements on\u202fNxOy\u202fin the atmosphere. Measurements of ozone were recorded by the O3-NO Ethylene/Forward Scattering Spectrometer while the Modified\u202fLicor\u202frecorded CO2. Finally, the DACOM IR Laser Spectrometer gathered an assortment of data points, including CO, O3, N2O, CH4, and CO2.\u202fOzonesondes\u202fplayed a role in data collection for TRACE-A along with the DC-8 aircraft. The sondes were dropped from the DC-8 aircraft in order to gather data on ozone, temperature, and atmospheric pressure.",
-            "title": "TRACE-A DC-8 In-Situ Trace Gas Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FTRACE-A%2FTraceGas_AircraftInSitu_DC8_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FTRACE-A%2FTraceGas_AircraftInSitu_DC8_Data_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-gte.larc.nasa.gov/trace/tra_hmpg.htm",
-                    "description": "TRACE-A Summary",
                     "@type": "dcat:Distribution",
+                    "description": "TRACE-A Summary",
+                    "downloadURL": "https://www-gte.larc.nasa.gov/trace/tra_hmpg.htm",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-gte.larc.nasa.gov/gte_hmpg.htm#table",
-                    "description": "GTE Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "GTE Home Page",
+                    "downloadURL": "https://www-gte.larc.nasa.gov/gte_hmpg.htm#table",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/gte/guide/gte_fmt.pdf",
-                    "description": "GTE Data Format",
                     "@type": "dcat:Distribution",
+                    "description": "GTE Data Format",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/gte/guide/gte_fmt.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/epdf/10.1029/96JD00123",
-                    "description": "NASA GTE TRACE A Experiment (September-October 1992): Overview",
                     "@type": "dcat:Distribution",
+                    "description": "NASA GTE TRACE A Experiment (September-October 1992): Overview",
+                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/epdf/10.1029/96JD00123",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/TRACE-A/TraceGas_AircraftInSitu_DC8_Data_1",
-                    "description": "DOI Data Set Landing Page for TRACE-A_TraceGas_AircraftInSitu_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI Data Set Landing Page for TRACE-A_TraceGas_AircraftInSitu_DC8_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/TRACE-A/TraceGas_AircraftInSitu_DC8_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2813461507-LARC_CLOUD",
-                    "description": "Earthdata Search for TRACE-A_TraceGas_AircraftInSitu_DC8_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TRACE-A_TraceGas_AircraftInSitu_DC8_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2813461507-LARC_CLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "identifier": "C2813461507-LARC_CLOUD",
+            "issued": "1992-09-01",
+            "keyword": [
+                "aerosols",
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/TRACE-A/TraceGas_AircraftInSitu_DC8_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1992-10-27",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-180.0 -59.98 58.68 43.575",
+            "temporal": "1990-03-13T00:00:00Z/1992-11-01T00:00:00Z",
             "theme": [
                 "TRACE-A",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TRACE-A DC-8 In-Situ Trace Gas Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-L-PPR-2-EDR-MOON1-V1.0",
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
-                "galileo",
-                "moon"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains the R_EDR data\nfor the Galileo Orbiter PPR instrument for the period corresponding\nto the Earth-1 encounter observations in November-December 1990.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-l-ppr-2-edr-moon1-v1.0_3zn6-fvvb",
+            "issued": "2021-05-21",
+            "keyword": [
+                "galileo",
+                "moon"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-L-PPR-2-EDR-MOON1-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-l-ppr-2-edr-moon1-v1.0_3zn6-fvvb",
-            "description": "This data set contains the R_EDR data\nfor the Galileo Orbiter PPR instrument for the period corresponding\nto the Earth-1 encounter observations in November-December 1990.",
-            "title": "GLL PPR EARTH-1 ENCOUNTER EDR",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GLL PPR EARTH-1 ENCOUNTER EDR"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1999-11-15. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/FIRE/0101.",
-            "issued": "1999-11-04",
-            "temporal": "1991-11-13T00:00:00Z/1991-11-29T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-13",
-            "keyword": [
-                "clouds",
-                "atmosphere",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "TANEIL UTTAL",
                 "hasEmail": "mailto:tau@etl.noaa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1000001165-LARC_ASDC",
             "description": "The First ISCCP Regional Experiments have been designed to improve data products and cloud/radiation parameterizations used in general circulation models (GCMs). Specifically, the goals of FIRE are (1) to seek the basic understanding of the interaction of physical processes in determining life cycles of cirrus and marine stratocumulus systems and the radiative properties of these clouds during their life cycles and (2) to investigate the interrelationships between ISCCP data, GCM parameterizations, and higher space and time resolution cloud data. To-date, four intensive field-observation periods were planned and executed: a cirrus IFO (October 13 - November 2, 1986); a marine stratocumulus IFO off the southwestern coast of California (June 29 - July 20, 1987); a second cirrus IFO in southeastern Kansas (November 13 - December 7, 1991); and a second marine stratocumulus IFO in the eastern North Atlantic Ocean (June 1 - June 28, 1992). Each mission combined coordinated satellite, airborne, and surface observations with modeling studies to investigate the cloud properties and physical processes of the cloud systems.The National Oceanic and Atmospheric Administration (NOAA) Environmental Technology Laboratory (ETL) Doppler radar was used during the Fire Cirrus II experiment in Coffeyville, Kansas to document the structural, kinematic, microphysical and turbulent properties of climatically important cirrus cloud systems. Data were collected from November 13, 1991 through November 29, 1991.",
-            "title": "First ISCCP Regional Experiment (FIRE) Cirrus Phase II Environmental & Technology Laboratory (ETL) Doppler Radar Images (FIRE_CI2_ETL_RADAR)",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001165-LARC_ASDC",
-                    "description": "Earthdata Search for FIRE_CI2_ETL_RADAR_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FIRE_CI2_ETL_RADAR_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001165-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_CI2_ETL_RADAR/contents.html",
-                    "description": "OPeNDAP data access for FIRE_CI2_ETL_RADAR_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for FIRE_CI2_ETL_RADAR_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_CI2_ETL_RADAR/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ci2_etl_radar_dataset.pdf",
-                    "description": "FIRE Cirrus 2 Environmental Technology Laboratory (ETL) Doppler Radar Images Langley DAAC Data Set Document",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE Cirrus 2 Environmental Technology Laboratory (ETL) Doppler Radar Images Langley DAAC Data Set Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ci2_etl_radar_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ci2_etl_radar_info1.txt",
-                    "description": "FIR CI2 ETL Radar Image Info Readme",
                     "@type": "dcat:Distribution",
+                    "description": "FIR CI2 ETL Radar Image Info Readme",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ci2_etl_radar_info1.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/postscript",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ci2_etl_radar.ps",
-                    "description": "FIRE Cirrus 2 - Direct File Download (.ps) Readme",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE Cirrus 2 - Direct File Download (.ps) Readme",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ci2_etl_radar.ps",
+                    "mediaType": "application/postscript",
                     "title": "View this dataset's read me document"
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
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0101",
-                    "description": "DOI data set landing page for FIRE_CI2_ETL_RADAR_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIRE_CI2_ETL_RADAR_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0101",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_CI2_ETL_RADAR/",
-                    "description": "ASDC Direct Data Download for FIRE_CI2_ETL_RADAR_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIRE_CI2_ETL_RADAR_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_CI2_ETL_RADAR/",
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
+            "identifier": "C1000001165-LARC_ASDC",
+            "issued": "1999-11-04",
+            "keyword": [
+                "clouds",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0101",
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
+            "temporal": "1991-11-13T00:00:00Z/1991-11-29T23:59:59.999Z",
             "theme": [
                 "FIRE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "First ISCCP Regional Experiment (FIRE) Cirrus Phase II Environmental & Technology Laboratory (ETL) Doppler Radar Images (FIRE_CI2_ETL_RADAR)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/217/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2010-09-22",
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
-            "identifier": "DASHLINK_217",
             "description": "**Abstract:**\r\n\r\nBuilding health management is an important part in running an efficient and cost-effective building. Many problems in a building\u2019s system can go undetected for long periods of time, leading to expensive repairs or wasted resources. This project aims to help detect and diagnose the building\u2018s health with data driven methods throughout the day. Orca and IMS are two state of the art algorithms that observe an array of building health sensors and provide feedback on the overall system\u2019s health as well as localize the problem to one, or possibly two, components. With this level of feedback the hope is to quickly identify problems and provide appropriate maintenance while reducing the number of complaints and service calls.\r\n\r\n \r\n\r\n**Introduction:**\r\n\r\n\r\nTo prepare these technologies for the new installation, the proposed methods are being tested on a current system that behaves similarly to the future green building. Building 241 was determined to best resemble the proposed building 232 and therefore was chosen for this study.\r\nBuilding 241 is currently outfitted with 34 sensors that monitor the heating & cooling temperatures for the air and water systems as well as other various subsystem states. The daily sensor recordings were logged and sent to the IDU group for analysis. The period of analysis was focused from July 1st through August 10th 2009.\r\n \r\n\r\n**Methodology:**\r\n\r\n\r\nThe two algorithms used for analysis were Orca and IMS. Both methods look for anomalies using a distanced based scoring approach.\r\nOrca has the ability to use a single data set and find outliers within that data set. This tactic was applied to each day.  After scoring  each time sample throughout a given day the Orca score profiles were compared by computing the correlation against all other days. Days with high overall correlations were considered normal however days with lower overall correlations were more anomalous.  IMS, on the other hand, needs a normal  set of data to build a model, which can be applied to a set of test data to asses how anomaly the particular data set is.\r\nThe typical days  identified by Orca were used as the reference/training set for IMS, while all the other days were passed through IMS resulting in an anomaly score profile for each day. The mean of the IMS score profile was then calculated for each day to produce a summary IMS score. These summary scores were ranked and the top outliers were  identified (see Figure 1).  Once the anomalies were identified the contributing parameters were then ranked by the algorithm.\r\n\r\n \r\n\r\n**Analysis:**\r\n\r\n\r\nThe contributing parameters identified by IMS were localized to the return air temperature duct system.\r\n\r\n-7/03/09 (Figure 2 & 3) AHU-1 Return Air Temperature (RAT) Calculated Average Return Air Temperature\r\n-7/19/09 (Figure 3 & 4) AHU-2 Return Air Temperature (RAT) Calculated Average Return Air Temperature\r\n\r\n\r\nIMS identified significantly higher temperatures compared to other days during the month of July and August.\r\n \r\n\r\n**Conclusion:**\r\n\r\n\r\nThe proposed algorithms Orca and IMS have shown that they were able to pick up significant anomalies in the building system as well as diagnose the anomaly by identifying the sensor values that were anomalous.  In the future these methods can be used on live streaming data and produce a real time anomaly score to help building maintenance with detection and diagnosis of problems.",
-            "title": "Integrated Building Health Management",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Figure_1.jpg",
-                    "description": "Figure_1.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Figure_1.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Figure_1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Figure_1.jpg"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Figure_2.jpg",
-                    "description": "Figure_2.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Figure_2.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Figure_2.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Figure_2.jpg"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Figure_3.jpg",
-                    "description": "Figure_3.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Figure_3.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Figure_3.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Figure_3.jpg"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Figure_4.jpg",
-                    "description": "Figure_4.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Figure_4.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Figure_4.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Figure_4.jpg"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_217",
+            "issued": "2010-09-22",
+            "keyword": [
+                "ames",
+                "nasa",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/217/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Integrated Building Health Management"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Abopps2014&version=1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This bundle collects all the observational data and documentation generated as part of the first  Balloon Observation Platform for Planetary Science (BOPPS) flight to return planetary science data.",
+            "identifier": "urn:nasa:pds:bopps2014_3zsv-77ya",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "bopps",
                 "c/2014 e2 (jacques)",
@@ -112868,878 +112870,878 @@
                 "c/2012 k1 (panstarrs)",
                 "(1) ceres"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Abopps2014&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:bopps2014_3zsv-77ya",
-            "description": "This bundle collects all the observational data and documentation generated as part of the first  Balloon Observation Platform for Planetary Science (BOPPS) flight to return planetary science data.",
-            "title": "Balloon Observation Platform for Planetary Science (BOPPS) 2014 Observations",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Balloon Observation Platform for Planetary Science (BOPPS) 2014 Observations"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-UVS-3-RDR-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains reformatted records derived from data returned by the Voyager Ultraviolet Spectrometer Subsystem on board Voyager 2 during the Saturn encounter phase of the Voyager mission. Original instrument data were merged with ancillary data from footprint SEDR files provided by the Voyager Project at the Jet Propulsion Laboratory. The final product files are formatted as PDS binary tables.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-uvs-3-rdr-v1.0_3zvq-j3am",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "saturn",
                 "voyager",
                 "comet sl9/jupiter collision"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-UVS-3-RDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-uvs-3-rdr-v1.0_3zvq-j3am",
-            "description": "This data set contains reformatted records derived from data returned by the Voyager Ultraviolet Spectrometer Subsystem on board Voyager 2 during the Saturn encounter phase of the Voyager mission. Original instrument data were merged with ancillary data from footprint SEDR files provided by the Voyager Project at the Jet Propulsion Laboratory. The final product files are formatted as PDS binary tables.",
-            "title": "VG2 SATURN ULTRAVIOLET SPECTROMETER SUBSYSTEM 3 RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG2 SATURN ULTRAVIOLET SPECTROMETER SUBSYSTEM 3 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/174",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hall, F. G., K. F. Huemmrich, D. E. Strebel, S. J. Goetz, J. E. Nickeson, and K. D. Woods. 1996. NWS Daily Climatology Data: 1987 (SNF). [National Weather Service Daily Climatology Data: 1987 (Superior National Forest)]. Data set. Available on-line [http://www.daac.ornl.gov] from Oak Ridge National Laboratory Distributed Active Archive Center, Oak Ridge, Tennessee, U.S.A. Based on F. G. Hall, K. F. Huemmrich, D. E. Strebel, S. J. Goetz, J. E. Nickeson, and K. D. Woods, Biophysical, Morphological, Canopy Optical Property, and Productivity Data from the Superior National Forest, NASA Technical Memorandum 104568, National Aeronautics and Space Administration, Goddard Space Flight Center, Greenbelt, Maryland, U.S.A., 1992. doi:10.3334/ORNLDAAC/174",
-            "issued": "2024-03-01",
-            "temporal": "1987-01-01T00:00:00Z/1987-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-04",
-            "keyword": [
-                "earth science",
-                "atmospheric temperature",
-                "atmospheric radiation",
-                "atmospheric water vapor",
-                "atmosphere",
-                "precipitation"
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
-            "identifier": "C2884978442-ORNL_CLOUD",
             "description": "Daily min, max, average temperature (F), precipitation (water equivalent in inches), and daily insolation (Langleys) for the Superior National Forest area as collected by NWS and U. of Minnesota",
-            "graphic-preview-description": "Browse Image",
-            "title": "NWS Daily Climatology Data: 1987 (SNF)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/snf_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F174",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F174",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/snf/SNF_MET_1987/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/snf/SNF_MET_1987/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/SNF/guides/nws_daily_climate_1987.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/SNF/guides/nws_daily_climate_1987.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/174",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/174",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1987/comp/met_1987.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1987/comp/met_1987.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1987/comp/met_1987.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1987/comp/met_1987.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1987/comp/nws_daily_climate_1987.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1987/comp/nws_daily_climate_1987.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1987/comp/nws_daily_climate_1987.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1987/comp/nws_daily_climate_1987.txt",
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
+            "identifier": "C2884978442-ORNL_CLOUD",
+            "issued": "2024-03-01",
+            "keyword": [
+                "earth science",
+                "atmospheric temperature",
+                "atmospheric radiation",
+                "atmospheric water vapor",
+                "atmosphere",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/174",
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
+            "temporal": "1987-01-01T00:00:00Z/1987-12-31T23:59:59Z",
             "theme": [
                 "SNF",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NWS Daily Climatology Data: 1987 (SNF)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2145",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hook, S.J., J.S. Myers, K.J. Thome, M. Fitzgerald, A.B. Kahle,  Airborne Sensor Facility NASA Ames Research Center, and T.J. Schmugge. 2022. MASTER: Airborne Science, California-New Mexico, May, 2001, V2. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2145",
-            "issued": "2023-02-23",
-            "temporal": "2001-05-11T00:34:58Z/2001-05-12T18:05:15Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-13",
-            "keyword": [
-                "spectral/engineering",
-                "infrared wavelengths",
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
-            "identifier": "C2731792800-ORNL_CLOUD",
             "description": "This dataset includes Level 1B (L1B) data products from the MODIS/ASTER Airborne Simulator (MASTER) instrument. The spectral data were collected during two flights aboard a DOE B-200 aircraft over California and New Mexico, U.S., on 2001-05-11 to 2001-05-12. This deployment was coordinated by the U.S. Department of Energy's Remote Sensing Laboratory (RSL) located at Nellis Air Force Base near Las Vegas, Nevada. Data products include L1B georeferenced multispectral imagery of calibrated radiance in 50 bands covering wavelengths of 0.460 to 12.879 micrometers at approximately 10-meter spatial resolution. The L1B file format is HDF-4. In addition, the dataset includes flight paths, spectral band information, instrument configuration, ancillary notes, and summary information for each flight, and browse images derived from each L1B data file.",
-            "graphic-preview-description": "Single-band images and a RGB composite image from flight track 1 acquired on 11 May 2001 over Las Animas Creek, south-southeast of San Jose, California, U.S. Source: MASTERL1B_0100302_01_20010511_0034_0036_V01.jpg",
-            "title": "MASTER: Airborne Science, California-New Mexico, May, 2001, V2",
-            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_May_2001_V2_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2145",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2145",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/master/MASTER_RSL_May_2001_V2/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/master/MASTER_RSL_May_2001_V2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_May_2001_V2.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_May_2001_V2.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2145",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2145",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_RSL_May_2001_V2/comp/MASTER_RSL_May_2001_V2.pdf",
-                    "description": "MASTER: Airborne Science, California-New Mexico, May, 2001, V2: MASTER_RSL_May_2001_V2.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "MASTER: Airborne Science, California-New Mexico, May, 2001, V2: MASTER_RSL_May_2001_V2.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_RSL_May_2001_V2/comp/MASTER_RSL_May_2001_V2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_May_2001_V2_Fig1.jpg",
-                    "description": "Single-band images and a RGB composite image from flight track 1 acquired on 11 May 2001 over Las Animas Creek, south-southeast of San Jose, California, U.S. Source: MASTERL1B_0100302_01_20010511_0034_0036_V01.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Single-band images and a RGB composite image from flight track 1 acquired on 11 May 2001 over Las Animas Creek, south-southeast of San Jose, California, U.S. Source: MASTERL1B_0100302_01_20010511_0034_0036_V01.jpg",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_May_2001_V2_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Single-band images and a RGB composite image from flight track 1 acquired on 11 May 2001 over Las Animas Creek, south-southeast of San Jose, California, U.S. Source: MASTERL1B_0100302_01_20010511_0034_0036_V01.jpg",
+            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_May_2001_V2_Fig1.jpg",
+            "identifier": "C2731792800-ORNL_CLOUD",
+            "issued": "2023-02-23",
+            "keyword": [
+                "spectral/engineering",
+                "infrared wavelengths",
+                "earth science",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2145",
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
             "spatial": "-121.73 32.47 -106.57 37.23",
+            "temporal": "2001-05-11T00:34:58Z/2001-05-12T18:05:15Z",
             "theme": [
                 "MASTER",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MASTER: Airborne Science, California-New Mexico, May, 2001, V2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-X-VIR-2-EDR-VIS-CRUISE-SPECTRA-V1.0",
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
+            "description": "This data set contains the digital       numbers (DN) contained in the telemetry (TM) packages of the VIR-VIS    instrument on board of the spacecraft DAWN. The data are from the       cruise phase from launch to Vesta (Sep 2009-May 2011), and Vesta        to Ceres (Sep 2012-Dec 2014).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-x-vir-2-edr-vis-cruise-spectra-v1.0_422z-savt",
+            "issued": "2018-06-26",
+            "keyword": [
+                "dawn mission to vesta and ceres"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-X-VIR-2-EDR-VIS-CRUISE-SPECTRA-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-x-vir-2-edr-vis-cruise-spectra-v1.0_422z-savt",
-            "description": "This data set contains the digital       numbers (DN) contained in the telemetry (TM) packages of the VIR-VIS    instrument on board of the spacecraft DAWN. The data are from the       cruise phase from launch to Vesta (Sep 2009-May 2011), and Vesta        to Ceres (Sep 2012-Dec 2014).",
-            "title": "DAWN VIR RAW (EDR) CRUISE CHECKOUT/CALIB VISIBLE SPECTRA V1.",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "DAWN VIR RAW (EDR) CRUISE CHECKOUT/CALIB VISIBLE SPECTRA V1."
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/713",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Piketh, S.J., T. Elias, and D.C. Stein. 2004. SAFARI 2000 JRA Aerocommander Trace Gas, Aerosol, and CCN Data, Dry Season 2000. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/713",
-            "issued": "2023-10-18",
-            "temporal": "2000-08-15T00:00:00Z/2000-09-07T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-24",
-            "keyword": [
-                "atmospheric temperature",
-                "earth science",
-                "atmospheric water vapor",
-                "atmospheric pressure",
-                "atmospheric chemistry",
-                "atmosphere",
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
-            "identifier": "C2788386640-ORNL_CLOUD",
             "description": "As part of the 3rd Intensive Campaign of SAFARI 2000, the South African Weather Bureau Aerocommander, JRA, flew 19 missions, for a total of 28 separate flights conducted between August 15th and September 7th, 2000.  JRA worked closely with the other Aerocommander, JRA, and was dedicated to the measurement of trace gas and aerosol properties.  A suite of trace analyzers (for O3, SO2, CO and NO), laser aerosol probes and atmospheric probes were present for all flights.  Other instruments and sampling units present for some of the flights included, a nephelometer (Elias), CO flasks (Novelli) for MOPITT validation purposes, and VOC canisters for the collection and characterization of volatile organic compounds present over various land surface types.",
-            "graphic-preview-description": "Browse Image",
-            "title": "SAFARI 2000 JRA Aerocommander Trace Gas, Aerosol, and CCN Data, Dry Season 2000",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/safari_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F713",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F713",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/atmospheric/SAWB_JRA/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/atmospheric/SAWB_JRA/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/S2K/guides/s2k_JRA_Flights.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/S2K/guides/s2k_JRA_Flights.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/713",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/713",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/atmospheric/SAWB_JRA/comp/jra_jrb_trace_gas_companion.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/atmospheric/SAWB_JRA/comp/jra_jrb_trace_gas_companion.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/atmospheric/SAWB_JRA/comp/s2k_JRA_Flights.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/atmospheric/SAWB_JRA/comp/s2k_JRA_Flights.pdf",
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
+            "identifier": "C2788386640-ORNL_CLOUD",
+            "issued": "2023-10-18",
+            "keyword": [
+                "atmospheric temperature",
+                "earth science",
+                "atmospheric water vapor",
+                "atmospheric pressure",
+                "atmospheric chemistry",
+                "atmosphere",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/713",
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
             "spatial": "22.16 -30.19 33.16 -17.83",
+            "temporal": "2000-08-15T00:00:00Z/2000-09-07T23:59:59Z",
             "theme": [
                 "SAFARI 2000",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAFARI 2000 JRA Aerocommander Trace Gas, Aerosol, and CCN Data, Dry Season 2000"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/CLDMSK_L2_VIIRS_NOAA21.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA VIIRS Atmosphere SIPS. 2024-09-20. VIIRS/NOAA21 Cloud Mask and Spectral Test Results 6-Min L2 Swath 750m. Version 1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/VIIRS/CLDMSK_L2_VIIRS_NOAA21.001. https://doi.org/10.5067/VIIRS/CLDMSK_L2_VIIRS_NOAA21.001.",
-            "issued": "2023-02-10",
-            "temporal": "2023-02-10T00:00:00Z/2024-12-09T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-17",
-            "keyword": [
-                "clouds",
-                "earth science",
-                "atmosphere",
-                "spectral/engineering",
-                "visible wavelengths",
-                "infrared wavelengths"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:sips.support@ssec.wisc.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/HBSL/BISB/MODAPS"
-            },
-            "identifier": "C3206162112-LAADS",
-            "description": "The National Oceanic and Atmospheric Administration (NOAA-21) Visible Infrared Imaging Radiometer Suite (VIIRS) NASA Level-2 (L2) Cloud Mask (VIIRS/NOAA21 Cloud Mask and Spectral Test Results 6-Min L2 Swath 750m) product is one of four continuity products designed to sustain the long-term records of both Moderate Resolution Imaging Spectroradiometer (MODIS) and VIIRS heritages. CLDMSK_L2_VIIRS_NOAA21 is the short-name for the NOAA-21 VIIRS incarnation of the Cloud Mask continuity product derived from the MODIS-VIIRS cloud mask (MVCM) algorithm, which itself is based on the MODIS (MOD35) algorithm.  The MVCM describes a continuity algorithm that is central to both MODIS data (from Terra and Aqua missions) and VIIRS data (from Suomi National Polar-orbiting Partnership (SNPP) and Joint Polar Satellite System missions).  Please bear in mind that the term MVCM does not appear as an attribute within the product\u2019s metadata.  Implemented to consistently handle MODIS and VIIRS inputs, the NOAA-21 VIIRS collection-1 products use calibration-adjusted NASA VIIRS L1B as inputs.  The nominal spatial resolution of the NOAA-21 VIIRS L2 Cloud mask is 750 meters. The L2 netCDF product is acquired and processed every 6 minutes.\r\n\r\nFor more information consult Product Page at: \r\nhttps://cimss.ssec.wisc.edu/MVCM/",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "NASA VIIRS Atmosphere SIPS",
-            "title": "VIIRS/NOAA21 Cloud Mask and Spectral Test Results 6-Min L2 Swath 750m",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The National Oceanic and Atmospheric Administration (NOAA-21) Visible Infrared Imaging Radiometer Suite (VIIRS) NASA Level-2 (L2) Cloud Mask (VIIRS/NOAA21 Cloud Mask and Spectral Test Results 6-Min L2 Swath 750m) product is one of four continuity products designed to sustain the long-term records of both Moderate Resolution Imaging Spectroradiometer (MODIS) and VIIRS heritages. CLDMSK_L2_VIIRS_NOAA21 is the short-name for the NOAA-21 VIIRS incarnation of the Cloud Mask continuity product derived from the MODIS-VIIRS cloud mask (MVCM) algorithm, which itself is based on the MODIS (MOD35) algorithm.  The MVCM describes a continuity algorithm that is central to both MODIS data (from Terra and Aqua missions) and VIIRS data (from Suomi National Polar-orbiting Partnership (SNPP) and Joint Polar Satellite System missions).  Please bear in mind that the term MVCM does not appear as an attribute within the product\u2019s metadata.  Implemented to consistently handle MODIS and VIIRS inputs, the NOAA-21 VIIRS collection-1 products use calibration-adjusted NASA VIIRS L1B as inputs.  The nominal spatial resolution of the NOAA-21 VIIRS L2 Cloud mask is 750 meters. The L2 netCDF product is acquired and processed every 6 minutes.\r\n\r\nFor more information consult Product Page at: \r\nhttps://cimss.ssec.wisc.edu/MVCM/",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FCLDMSK_L2_VIIRS_NOAA21.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FCLDMSK_L2_VIIRS_NOAA21.001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/CLDMSK_L2_VIIRS_NOAA21.001",
-                    "description": "Data product's landing page",
                     "@type": "dcat:Distribution",
+                    "description": "Data product's landing page",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/CLDMSK_L2_VIIRS_NOAA21.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/1/CLDMSK_L2_VIIRS_NOAA21--5110",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/1/CLDMSK_L2_VIIRS_NOAA21--5110",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/5110/CLDMSK_L2_VIIRS_NOAA21/contents.html",
-                    "description": "Direct access to CLDMSK_L2_VIIRS_NOAA21 OPeNDAP data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to CLDMSK_L2_VIIRS_NOAA21 OPeNDAP data set.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/5110/CLDMSK_L2_VIIRS_NOAA21/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://atmosphere-imager.gsfc.nasa.gov/sites/default/files/ModAtmo/MVCM_User_Guide_01Oct2020.pdf",
-                    "description": "Product User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Product User's Guide",
+                    "downloadURL": "https://atmosphere-imager.gsfc.nasa.gov/sites/default/files/ModAtmo/MVCM_User_Guide_01Oct2020.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "identifier": "C3206162112-LAADS",
+            "issued": "2023-02-10",
+            "keyword": [
+                "clouds",
+                "earth science",
+                "atmosphere",
+                "spectral/engineering",
+                "visible wavelengths",
+                "infrared wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/CLDMSK_L2_VIIRS_NOAA21.001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-10-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/HBSL/BISB/MODAPS"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2023-02-10T00:00:00Z/2024-12-09T00:00:00Z",
             "theme": [
                 "NOAA - SPACE WEATHER PROGRAM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NOAA21 Cloud Mask and Spectral Test Results 6-Min L2 Swath 750m"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/D7IROA0Q6JEQ",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMEX02 Passive and Active L and S band System (PALS) Data, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/D7IROA0Q6JEQ.",
-            "issued": "2002-06-25",
-            "temporal": "2002-06-25T00:00:00Z/2002-07-08T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2002-07-08",
-            "keyword": [
-                "radar",
-                "spectral/engineering",
-                "microwave",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Eni Njoku",
                 "hasEmail": "mailto:eni.g.njoku@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1386204049-NSIDCV0",
             "description": "This data set contains calibrated sensor measurements acquired by the Passive and Active L- and S-band (PALS) airborne microwave sensor during the Soil Moisture Experiment 2002 (SMEX02).",
-            "title": "SMEX02 Passive and Active L and S band System (PALS) Data, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FD7IROA0Q6JEQ",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FD7IROA0Q6JEQ",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX02/aircraft_remote_sensing/PALS/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX02/aircraft_remote_sensing/PALS/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX02/aircraft_remote_sensing/PALS/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX02/aircraft_remote_sensing/PALS/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/D7IROA0Q6JEQ",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/D7IROA0Q6JEQ",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/D7IROA0Q6JEQ",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/D7IROA0Q6JEQ",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386204049-NSIDCV0",
+            "issued": "2002-06-25",
+            "keyword": [
+                "radar",
+                "spectral/engineering",
+                "microwave",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/D7IROA0Q6JEQ",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2002-07-08",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-93.775 41.9213 -93.4013 41.9952",
+            "temporal": "2002-06-25T00:00:00Z/2002-07-08T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMEX02 Passive and Active L and S band System (PALS) Data, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NOAA-21/VIIRS/L3M/KD/2022",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/NOAA-21/VIIRS/L3M/KD/2022.",
-            "issued": "2023-04-04",
-            "temporal": "2022-11-10T00:00:00Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-04",
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
-            "identifier": "C2652675353-OB_DAAC",
             "description": "The Visible and Infrared Imager/Radiometer Suite (VIIRS) is a multi-disciplinary instrument that is being flown on the Joint Polar Satellite System (JPSS) series of spacecraft, including the Suomi National Polar-orbiting Partnership (S-NPP) that launched in October 2011.  JPSS is a multi-platform, multi-agency program that consolidates the polar orbiting spacecraft of NASA and the National Oceanic and Atmospheric Administration (NOAA).  S-NPP is the initial spacecraft in this series, and VIIRS is the successor to MODIS for Earth science data product generation.  VIIRS has 22 spectral bands ranging from 412 nm to 12 nm.  There are 16 moderate-resolution bands (750m at nadir), 5 image-resolution bands (375m), and one day-night band (DNB).",
-            "title": "NOAA-21 VIIRS Global Mapped Diffuse Attenuation Coefficient for Downwelling Irradiance (KD) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNOAA-21%2FVIIRS%2FL3M%2FKD%2F2022",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNOAA-21%2FVIIRS%2FL3M%2FKD%2F2022",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NOAA-21/VIIRS/L3M/KD/2022",
-                    "description": "VIIRS-NOAA-21 L3M Diffuse Attenuation Coefficient for Downwelling Irradiance (KD) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS-NOAA-21 L3M Diffuse Attenuation Coefficient for Downwelling Irradiance (KD) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NOAA-21/VIIRS/L3M/KD/2022",
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
+            "identifier": "C2652675353-OB_DAAC",
+            "issued": "2023-04-04",
+            "keyword": [
+                "ocean optics",
+                "earth science",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/NOAA-21/VIIRS/L3M/KD/2022",
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
+            "title": "NOAA-21 VIIRS Global Mapped Diffuse Attenuation Coefficient for Downwelling Irradiance (KD) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/YO583L7ZOLOO",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SnowEx20-21 QSI Lidar DEM 0.5m UTM Grid V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/YO583L7ZOLOO.",
-            "issued": "2021-09-16",
-            "temporal": "2021-09-16T00:00:00Z/2021-09-21T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-09-21",
-            "keyword": [
-                "topography",
-                "land surface",
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
-            "identifier": "C2435982480-NSIDC_ECS",
             "description": "This data set is part of the SnowEx 2021 campaign and provides bare Earth digital elevation models (DEM) acquired by a scanning lidar system at a 0.5 m spatial resolution, and derived from point cloud digital terrain models. DEMs are available for September 2021 and from multiple areas in Colorado, Idaho, and Utah. These data were produced alongside <a href=\"https://doi.org/10.5067/8RBIUIPEUJ7Z\">Vegetation Height</a> and <a href=\"https://doi.org/10.5067/VBUN16K365DG\">Snow Depth</a> data sets.",
-            "title": "SnowEx20-21 QSI Lidar DEM 0.5m UTM Grid V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FYO583L7ZOLOO",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FYO583L7ZOLOO",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_QSI_DEM.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_QSI_DEM.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_QSI_DEM/versions/1",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_QSI_DEM/versions/1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX20_QSI_DEM+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX20_QSI_DEM+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/YO583L7ZOLOO",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/YO583L7ZOLOO",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/YO583L7ZOLOO",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/YO583L7ZOLOO",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2435982480-NSIDC_ECS",
+            "issued": "2021-09-16",
+            "keyword": [
+                "topography",
+                "land surface",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/YO583L7ZOLOO",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-09-21",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-117.0661 43.0343 -114.8547 44.3658",
+            "temporal": "2021-09-16T00:00:00Z/2021-09-21T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SnowEx20-21 QSI Lidar DEM 0.5m UTM Grid V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aphx_ra&version=1.1",
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
+            "description": "The Phoenix Robotic Arm derived and test data set migrated from PDS3",
+            "identifier": "urn:nasa:pds:phx_ra_428d-zucs",
+            "issued": "2021-05-21",
+            "keyword": [
+                "phoenix",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aphx_ra&version=1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:phx_ra_428d-zucs",
-            "description": "The Phoenix Robotic Arm derived and test data set migrated from PDS3",
-            "title": "Phoenix Robotic Arm Data Set",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Phoenix Robotic Arm Data Set"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0829-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-06-06T09:29:05.000 to 2015-06-06T15:05:08.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0829-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0829-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0829-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-06-06T09:29:05.000 to 2015-06-06T15:05:08.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0829 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0829 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A%2FCAL-ALICE-2-AST2-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains CODMAC level 2 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the Lutetia flyby mission phase, which took place between 2010-06-07 and 2010-09-10.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-cal-alice-2-ast2-v1.0_42ci-i4fk",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "21 lutetia",
                 "calibration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A%2FCAL-ALICE-2-AST2-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-cal-alice-2-ast2-v1.0_42ci-i4fk",
-            "description": "This data set contains CODMAC level 2 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the Lutetia flyby mission phase, which took place between 2010-06-07 and 2010-09-10.",
-            "title": "ROSETTA-ORBITER LUTETIA/CAL ALICE 2 AST2 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER LUTETIA/CAL ALICE 2 AST2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL-RPCMIP-3-CVP2-V1.0",
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
+            "description": "This archive contains data from the RPC-MIP instrument onboard ROSETTA Orbiter acquired during the COMMISSIONING 2 mission phase. It also contains documentation which describes the RPC-MIP experiment. The data archived in this data set conform to the Planetary Data System Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-rpcmip-3-cvp2-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "calibration"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL-RPCMIP-3-CVP2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-rpcmip-3-cvp2-v1.0",
-            "description": "This archive contains data from the RPC-MIP instrument onboard ROSETTA Orbiter acquired during the COMMISSIONING 2 mission phase. It also contains documentation which describes the RPC-MIP experiment. The data archived in this data set conform to the Planetary Data System Standards, Version 3.6.",
-            "title": "ROSETTA-ORBITER CAL RPCMIP 3 CVP2 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CAL RPCMIP 3 CVP2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-ROSINA-2-CR5-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set present engineering data of the COPS, DFMS and RTOF ROSINA sensors during the active checkout 12, the Lander panel test and Lutetia rehearsal test - Cruise 5 phase. Version 2.0 contains significant corrections to the V1.0 data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rosina-2-cr5-v2.0_42e2-wtzk",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "earth",
@@ -113748,182 +113750,182 @@
                 "21 lutetia",
                 "unknown"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-ROSINA-2-CR5-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rosina-2-cr5-v2.0_42e2-wtzk",
-            "description": "This data set present engineering data of the COPS, DFMS and RTOF ROSINA sensors during the active checkout 12, the Lander panel test and Lutetia rehearsal test - Cruise 5 phase. Version 2.0 contains significant corrections to the V1.0 data set.",
-            "title": "ROSETTA-ORBITER CHECK ROSINA 2 CR5 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECK ROSINA 2 CR5 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/MOQOVNHNERGG",
             "citation": "AIRS project. 2019-12-15. AIRS2SUP_NRT. Version 7.0. Aqua/AIRS L2 Near Real Time (NRT) Support Retrieval (AIRS-only) V7.0. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/MOQOVNHNERGG. https://disc.gsfc.nasa.gov/datacollection/AIRS2SUP_NRT_7.0.html. Digital Science Data.",
-            "issued": "2024-07-06",
-            "temporal": "2002-08-30T00:00:00Z/2024-08-12T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-07",
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
-                "ocean temperature",
-                "surface thermal properties",
-                "surface radiative properties",
-                "precipitation",
-                "oceans",
-                "land surface",
-                "earth science",
-                "clouds",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "atmospheric radiation",
-                "atmospheric pressure",
-                "atmospheric chemistry",
-                "atmosphere",
-                "altitude",
-                "air quality",
-                "aerosols"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "LENA IREDELL",
                 "hasEmail": "mailto:lena.iredell@nasa.gov"
             },
+            "creator": "AIRS project",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1701805636-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The Atmospheric Infrared Sounder (AIRS) Level 2 Near Real Time (NRT) Support Retrieval (AIRS-only) product (AIRS2SUP_NRT_7.0) differs from the routine product (AIRS2SUP_7.0) in four ways to meet the three hour latency requirements of the Land Atmosphere NRT Capability Earth Observing System (LANCE): (1) The NRT granules are produced without previous or subsequent granules if those granules are not available within 5 minutes, (2) the predictive ephemeris/attitude data are used rather than the definitive ephemeris/attitude, (3) if the forecast surface pressure is unavailable, a surface climatology is used, and (4) no ice cloud properties retrievals are performed. The consequences of these differences are described in the AIRS Near Real Time (NRT) data products document. The Atmospheric Infrared Sounder (AIRS) is a grating spectrometer (R = 1200) aboard the second Earth Observing System (EOS) polar-orbiting platform, EOS Aqua. In combination with the Advanced Microwave Sounding Unit (AMSU) and the Humidity Sounder for Brazil (HSB), AIRS constitutes an innovative atmospheric sounding group of visible, infrared, and microwave sensors. This product is product produced using AIRS IR only because the radiometric noise in several AMSU channels started to increase significantly (since June 2007). The Support Product includes higher vertical resolution profiles of the quantities found in the Standard Product, plus intermediate outputs (e.g., microwave-only retrieval), research products such as the abundance of trace gases, and detailed quality assessment information. The Support Product profiles contain 100 levels between 1100 and .016 mb; this higher resolution simplifies the generation of radiances using forward models, though the vertical information content is no greater than that in the Standard Product profiles. The intended users of the Support Product are researchers interested in generating forward radiance or in examining research products, and the AIRS algorithm development team. The Support Product is generated at all locations as Standard Products. \n\nAn AIRS granule has been set as 6 minutes of data, 30 footprints cross track by 45 scanlines. There are 240 granules per day, with an orbit repeat cycle of approximately 16 day.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "AIRS2SUP_NRT",
-            "creator": "AIRS project",
-            "graphic-preview-description": "Sample plot of AIRS Level 2 Support Retrieval (AIRS-only) H2O Column Density Profile and Cloud Fraction.",
-            "title": "Aqua/AIRS L2 Near Real Time (NRT) Support Retrieval (AIRS-only) V7.0 at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRS2SUP_7.0.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMOQOVNHNERGG",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMOQOVNHNERGG",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRS2SUP_7.0.png",
-                    "description": "Sample plot of AIRS Level 2 Support Retrieval (AIRS-only) H2O Column Density Profile and Cloud Fraction.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample plot of AIRS Level 2 Support Retrieval (AIRS-only) H2O Column Density Profile and Cloud Fraction.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRS2SUP_7.0.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRS2SUP_NRT_7.0.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRS2SUP_NRT_7.0.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://discnrt1.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_NRT/AIRS2SUP_NRT.7.0/",
-                    "description": "Access the data via HTTPS. User registration is required. Register for a username and password at https://urs.eosdis.nasa.gov/users/new",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS. User registration is required. Register for a username and password at https://urs.eosdis.nasa.gov/users/new",
+                    "downloadURL": "https://discnrt1.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_NRT/AIRS2SUP_NRT.7.0/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://discnrt1.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_NRT/AIRS2RET_NRT.7.0",
-                    "description": "AIRS Near Real Time data products.",
                     "@type": "dcat:Distribution",
+                    "description": "AIRS Near Real Time data products.",
+                    "downloadURL": "https://discnrt1.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_NRT/AIRS2RET_NRT.7.0",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRS2SUP_NRT+7.0",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRS2SUP_NRT+7.0",
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
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/AIRS/Overview_of_the_AIRS_Mission.pdf",
-                    "description": "Overview of the AIRS Mission: Instruments, Processing Algorithms, Products, and Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Overview of the AIRS Mission: Instruments, Processing Algorithms, Products, and Documentation",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/AIRS/Overview_of_the_AIRS_Mission.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/AIRS/V7_L2_Product_User_Guide.pdf",
-                    "description": "AIRS/AMSU/HSB Version 7 Level 2 Product User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "AIRS/AMSU/HSB Version 7 Level 2 Product User Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/AIRS/V7_L2_Product_User_Guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "graphic-preview-description": "Sample plot of AIRS Level 2 Support Retrieval (AIRS-only) H2O Column Density Profile and Cloud Fraction.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRS2SUP_7.0.png",
+            "identifier": "C1701805636-GES_DISC",
+            "issued": "2024-07-06",
+            "keyword": [
+                "ocean temperature",
+                "surface thermal properties",
+                "surface radiative properties",
+                "precipitation",
+                "oceans",
+                "land surface",
+                "earth science",
+                "clouds",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "atmospheric radiation",
+                "atmospheric pressure",
+                "atmospheric chemistry",
+                "atmosphere",
+                "altitude",
+                "air quality",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.5067/MOQOVNHNERGG",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-08-07",
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
+            "series-name": "AIRS2SUP_NRT",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-08-30T00:00:00Z/2024-08-12T00:00:00Z",
             "theme": [
                 "Aqua",
                 "LANCE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aqua/AIRS L2 Near Real Time (NRT) Support Retrieval (AIRS-only) V7.0 at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-E%2FJ%2FS%2FSW-MIMI-2-INCA-UNCALIB-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The Cassini Magnetospheric Imaging Instrument(MIMI) Imaging Neutral Camera (INCA) uncalibrated data set includes all data collected from the MIMI Data Processing Unit during the mission. The original data has been decommutated and decoded by software at the Applied Physics Laboratory (APL) and has been then further ordered and filtered by software at Fundamental Technologies, LLC. The data is provided in an uncalibrated form in conjunction with a PDS MIMI calibration volume COMIMI_0000 which provides specific algorithms for the derivation of calibrated data. This data set includes uncalibrated values of counts in the form of rates and of rate images for the INCA sensor for all times during the mission including the Earth flyby, the Jupiter flyby, interplanetary cruise, and the entire Saturn tour. Data are presented in a set of tables which are of variable length and use a comma to separate various fields. This data set is intended to be the most comprehensive and complete data set included in the Cassini MIMI INCA archive. A browse data set is included with Key Parameter data that is calibrated using the algorithms provided in the Calibration volume. In addition, a series of images are provided with the KP browse data that displays the KP data which can lead the user to the particular times of interest. This data set should be among the first used by a user of any of the MIMI INCA archive as it will lead one to information required to search for more detailed or highly specialized features in the original data.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-e-j-s-sw-mimi-2-inca-uncalib-v1.0_42et-yz8v",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "saturn",
                 "solar wind",
@@ -113931,99 +113933,75 @@
                 "jupiter",
                 "earth"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-E%2FJ%2FS%2FSW-MIMI-2-INCA-UNCALIB-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-e-j-s-sw-mimi-2-inca-uncalib-v1.0_42et-yz8v",
-            "description": "The Cassini Magnetospheric Imaging Instrument(MIMI) Imaging Neutral Camera (INCA) uncalibrated data set includes all data collected from the MIMI Data Processing Unit during the mission. The original data has been decommutated and decoded by software at the Applied Physics Laboratory (APL) and has been then further ordered and filtered by software at Fundamental Technologies, LLC. The data is provided in an uncalibrated form in conjunction with a PDS MIMI calibration volume COMIMI_0000 which provides specific algorithms for the derivation of calibrated data. This data set includes uncalibrated values of counts in the form of rates and of rate images for the INCA sensor for all times during the mission including the Earth flyby, the Jupiter flyby, interplanetary cruise, and the entire Saturn tour. Data are presented in a set of tables which are of variable length and use a comma to separate various fields. This data set is intended to be the most comprehensive and complete data set included in the Cassini MIMI INCA archive. A browse data set is included with Key Parameter data that is calibrated using the algorithms provided in the Calibration volume. In addition, a series of images are provided with the KP browse data that displays the KP data which can lead the user to the particular times of interest. This data set should be among the first used by a user of any of the MIMI INCA archive as it will lead one to information required to search for more detailed or highly specialized features in the original data.",
-            "title": "CASSINI E/J/S/SW MIMI INCA SENSOR UNCALIBRATED DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI E/J/S/SW MIMI INCA SENSOR UNCALIBRATED DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0313-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-09-23T16:39:55.000 to 2014-09-24T00:03:48.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0313-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0313-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0313-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-09-23T16:39:55.000 to 2014-09-24T00:03:48.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0313 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0313 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1685783951-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "OCO-2 Science Team/Michael Gunson, Annmarie Eldering. 2020-03-17. OCO2_Eph. Version 10. OCO-2 Level 0 spacecraft ephemerides V10. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/OCO2_Eph_10.html. Digital Science Data.",
-            "issued": "2020-01-17",
-            "temporal": "2019-11-30T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-17",
-            "keyword": [
-                "spectral/engineering",
-                "platform characteristics",
-                "earth science"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JENNIFER WEI, PH. D",
                 "hasEmail": "mailto:jennifer.c.wei@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1685783951-GES_DISC",
-            "description": "Version 10 is the current version of the data set. Older versions will no longer be available and are superseded by Version 10.\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers . Each band has 1016 spectral elements.This product contains the position and velocity of the spacecraft for each orbit. It is generated using the following input data:+ APID 20 telemetry+ Orbit Boundary File.It is essential in generating the Geolocations of the science data.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OCO2_Eph",
             "creator": "OCO-2 Science Team/Michael Gunson, Annmarie Eldering",
-            "title": "OCO-2 Level 0 spacecraft ephemerides V10 (OCO2_Eph) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Version 10 is the current version of the data set. Older versions will no longer be available and are superseded by Version 10.\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers . Each band has 1016 spectral elements.This product contains the position and velocity of the spacecraft for each orbit. It is generated using the following input data:+ APID 20 telemetry+ Orbit Boundary File.It is essential in generating the Geolocations of the science data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -114032,133 +114010,133 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_Eph_10.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_Eph_10.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO2_Eph",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO2_Eph",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_Eph.10/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_Eph.10/contents.html",
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
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_Eph.10/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_Eph.10/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/SDOS_SIS_Ephem.V5.pdf",
-                    "description": "Software Interface Specification",
                     "@type": "dcat:Distribution",
+                    "description": "Software Interface Specification",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/SDOS_SIS_Ephem.V5.pdf",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_logo.jpg",
+            "identifier": "C1685783951-GES_DISC",
+            "issued": "2020-01-17",
+            "keyword": [
+                "spectral/engineering",
+                "platform characteristics",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1685783951-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-01-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "OCO2_Eph",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2019-11-30T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "OCO-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OCO-2 Level 0 spacecraft ephemerides V10 (OCO2_Eph) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://nasa3d.arc.nasa.gov/detail/freedom-c2",
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
-                "freedom 7",
-                "vehicles",
-                "spacecraft",
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
-            "identifier": "NASA-345",
             "description": "Polygons: 163880 Vertices: 94635",
-            "title": "NASA 3D Models: Freedom 7",
-            "programCode": [
-                "026:045",
-                "026:046"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -114166,23 +114144,47 @@
                     "mediaType": "image/x-3ds"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-345",
+            "issued": "2018-06-25",
+            "keyword": [
+                "freedom 7",
+                "vehicles",
+                "spacecraft",
+                "3d model"
+            ],
+            "landingPage": "http://nasa3d.arc.nasa.gov/detail/freedom-c2",
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
+            "title": "NASA 3D Models: Freedom 7"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Agbo.ast.fieber-beyer.spectra&version=1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The data set contains observations       obtained with the NASA IRTF SpeX instrument covering the 0.7 to 2.5    micron near-infrared portion of the spectrum.  The data set archives   reduced, calibrated spectra which were obtained and used in Sherry     Fieber-Beyer's Ph.D. dissertation at the                               University of North Dakota and archives reduced, calibrated spectra    subsequent 2010. The research focused on asteroids in a zone centered  on the 3:1 resonance. These spectra were used to mineralogically       characterize asteroids in this zone in an attempt to identify their    meteorite analogs.",
+            "identifier": "urn:nasa:pds:gbo.ast.fieber-beyer.spectra",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "(1772) gagarin",
                 "none",
@@ -114239,76 +114241,76 @@
                 "(1036) ganymed",
                 "(1018) arnolda"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Agbo.ast.fieber-beyer.spectra&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:gbo.ast.fieber-beyer.spectra",
-            "description": "The data set contains observations       obtained with the NASA IRTF SpeX instrument covering the 0.7 to 2.5    micron near-infrared portion of the spectrum.  The data set archives   reduced, calibrated spectra which were obtained and used in Sherry     Fieber-Beyer's Ph.D. dissertation at the                               University of North Dakota and archives reduced, calibrated spectra    subsequent 2010. The research focused on asteroids in a zone centered  on the 3:1 resonance. These spectra were used to mineralogically       characterize asteroids in this zone in an attempt to identify their    meteorite analogs.",
-            "title": "FIEBER-BEYER IRTF MAINBELT ASTEROID SPECTRA",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "FIEBER-BEYER IRTF MAINBELT ASTEROID SPECTRA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VO1%2FVO2-M-IRTM-5-BINNED%2FCLOUDS-V1.0",
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
-                "viking",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set, derived from the Viking Orbiter Infrared Thermal Mapper (IRTM) data set, has been binned in both space and time. It consists of two complementary portions, water ice cloud observations and surface observations. For details on the IRTM instrument and data set, refer to [KIEFFER_ETAL_1977].",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vo1-vo2-m-irtm-5-binned-clouds-v1.0_42j3-2w7j",
+            "issued": "2021-05-21",
+            "keyword": [
+                "viking",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VO1%2FVO2-M-IRTM-5-BINNED%2FCLOUDS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vo1-vo2-m-irtm-5-binned-clouds-v1.0_42j3-2w7j",
-            "description": "This data set, derived from the Viking Orbiter Infrared Thermal Mapper (IRTM) data set, has been binned in both space and time. It consists of two complementary portions, water ice cloud observations and surface observations. For details on the IRTM instrument and data set, refer to [KIEFFER_ETAL_1977].",
-            "title": "VO1/VO2 MARS IRTM BINNED DATA AND DERIVED CLOUDS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VO1/VO2 MARS IRTM BINNED DATA AND DERIVED CLOUDS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-ESC1-67PCHURYUMOV-M11-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 1 mission phase, covering the period from 2014-12-19T23:25:00.000 to 2015-01-13T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-esc1-67pchuryumov-m11-v3.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "bias",
                 "dark",
@@ -114317,484 +114319,457 @@
                 "vega",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-ESC1-67PCHURYUMOV-M11-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-esc1-67pchuryumov-m11-v3.0",
-            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 1 mission phase, covering the period from 2014-12-19T23:25:00.000 to 2015-01-13T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 2 ESC1-MTP011 EDR V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 2 ESC1-MTP011 EDR V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/105",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Norman, J. N. 1994. Soil CO2 Flux Data (FIFE). Data set. Available on-line [http://www.daac.ornl.gov] from Oak Ridge National Laboratory Distributed Active Archive Center, Oak Ridge, Tennessee, U.S.A. Also published in D. E. Strebel, D. R. Landis, K. F. Huemmrich, and B. W. Meeson (eds.), Collected Data of the First ISLSCP Field Experiment, Vol. 1: Surface Observations and Non-Image Data Sets. CD-ROM. National Aeronautics and Space Administration, Goddard Space Flight Center, Greenbelt, Maryland, U.S.A. (available from http://www.daac.ornl.gov). doi:10.3334/ORNLDAAC/105",
-            "issued": "2024-05-06",
-            "temporal": "1989-07-24T00:00:00Z/1989-08-12T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-07",
-            "keyword": [
-                "soils",
-                "vegetation",
-                "earth science",
-                "atmospheric temperature",
-                "atmospheric chemistry",
-                "ecological dynamics",
-                "biosphere",
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
-            "identifier": "C2980612093-ORNL_CLOUD",
             "description": "Soil surface CO2 flux data collected by John Norman",
-            "graphic-preview-description": "Browse Image",
-            "title": "Soil CO2 Flux Data (FIFE)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/fife_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F105",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F105",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_biology_soil_co2/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_biology_soil_co2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/Soil_CO2_Flux_Data.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/Soil_CO2_Flux_Data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/105",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/105",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_biology_soil_co2/comp/soil_co2.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_biology_soil_co2/comp/soil_co2.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_biology_soil_co2/comp/soil_co2.tdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_biology_soil_co2/comp/soil_co2.tdf",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_biology_soil_co2/comp/Soil_CO2_Flux_Data.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_biology_soil_co2/comp/Soil_CO2_Flux_Data.pdf",
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
+            "identifier": "C2980612093-ORNL_CLOUD",
+            "issued": "2024-05-06",
+            "keyword": [
+                "soils",
+                "vegetation",
+                "earth science",
+                "atmospheric temperature",
+                "atmospheric chemistry",
+                "ecological dynamics",
+                "biosphere",
+                "land surface",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/105",
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
             "spatial": "-96.55 38.98 -96.54 39.09",
+            "temporal": "1989-07-24T00:00:00Z/1989-08-12T23:59:59Z",
             "theme": [
                 "FIFE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Soil CO2 Flux Data (FIFE)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TERRA/CERES/SSF1DEGDAY_L3.004",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2015-08-19. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/TERRA/CERES/SSF1DEGDAY_L3.004.",
-            "issued": "2015-02-23",
-            "temporal": "2000-03-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-13",
-            "keyword": [
-                "atmospheric winds",
-                "clouds",
-                "earth science",
-                "atmosphere",
-                "atmospheric pressure",
-                "aerosols",
-                "atmospheric radiation",
-                "atmospheric temperature",
-                "atmospheric water vapor"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DAVID DOELLING",
                 "hasEmail": "mailto:ceres-help@lists.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1000000601-LARC_ASDC",
             "description": "CER_SSF1deg-Day_Terra-MODIS_Edition4A is the Clouds and the Earth's Radiant Energy System (CERES) Time-Interpolated Top of Atmosphere (TOA) Fluxes, Clouds and Aerosols Daily Terra Edition 4A data product, which was collected using the CERES-Flight Model (FM1) and FM2 instruments on the Terra platform. Data collection for this product is in progress.\r\n\r\nCERES Single Scanner Footprint one degree (SSF1deg) Day provides daily averages of regional constant meteorology temporally interpolated TOA fluxes, clouds derived from a co-located imager and aerosols on a 1-degree latitude and longitude grid. This is a single satellite product that uses the primary CERES instrument in cross-track mode. TOA fluxes are provided for clear-sky and all-sky conditions for longwave (LW), shortwave (SW), and window (WN) wavelength bands. The incoming solar daily irradiance is from the SOlar Radiation and Climate Experiment (SORCE) and Total Solar Irradiance (TSI). The cloud properties are averaged for both day and night (24-hour) and day-only time periods. Cloud properties are stratified into 4 atmospheric layers (surface-700 hPa, 700 hPa - 500 hPa, 500 hPa - 300 hPa, 300 hPa - 100 hPa) and a total of all layers. The aerosols are averaged instantaneous values from the co-located imager. \r\n\r\nCERES is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions are a follow-on to the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument, protoflight model (PFM), was launched on November 27, 1997 as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the Earth Observing System (EOS) flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board Earth Observing System (EOS) Aqua on May 4, 2002. The CERES FM5 instrument was launched on board the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The newest CERES instrument (FM6) was launched on board the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite, now called NOAA-20, on November 18, 2017.",
-            "title": "CERES Time-Interpolated TOA Fluxes, Clouds and Aerosols Daily Terra Edition4A",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FCERES%2FSSF1DEGDAY_L3.004",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FCERES%2FSSF1DEGDAY_L3.004",
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
-                    "downloadURL": "https://doi.org/10.5067/TERRA/CERES/SSF1DEGDAY_L3.004",
-                    "description": "DOI data set landing page for CER_SSF1deg-Day_Terra-MODIS_Edition4A",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CER_SSF1deg-Day_Terra-MODIS_Edition4A",
+                    "downloadURL": "https://doi.org/10.5067/TERRA/CERES/SSF1DEGDAY_L3.004",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000601-LARC_ASDC",
-                    "description": "Earthdata Search for CER_SSF1deg-Day_Terra-MODIS_Edition4A (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CER_SSF1deg-Day_Terra-MODIS_Edition4A (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000601-LARC_ASDC",
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
-                    "downloadURL": "https://ceres.larc.nasa.gov/documents/DPC/DPC_current/pdfs/DPC_SSF-Ed4_R5V1.pdf",
-                    "description": "Data Products Catalog CERES SSF-Ed4 R5V1",
                     "@type": "dcat:Distribution",
+                    "description": "Data Products Catalog CERES SSF-Ed4 R5V1",
+                    "downloadURL": "https://ceres.larc.nasa.gov/documents/DPC/DPC_current/pdfs/DPC_SSF-Ed4_R5V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_SSF1deg_Ed4A_DQS.pdf",
-                    "description": "Quality Summary: CERES_SSF1deg-Hour/Day/Month_Ed4A (3/13/2018)",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Summary: CERES_SSF1deg-Hour/Day/Month_Ed4A (3/13/2018)",
+                    "downloadURL": "https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_SSF1deg_Ed4A_DQS.pdf",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/DPC_SSF_R4V1.pdf",
-                    "description": "CERES Data Products Catalog R4V110/1/2004 Single Scanner Footprint TOA/Surface Fluxes and Clouds (SSF)",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Data Products Catalog R4V110/1/2004 Single Scanner Footprint TOA/Surface Fluxes and Clouds (SSF)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/DPC_SSF_R4V1.pdf",
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
-                    "mediaType": "application/postscript",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/cer_ssf_trmm-pfm-virs_subset-edition1_read_packageSSF_DPC_010008.ps",
-                    "description": "Read Me - CERES Data Products Catalog R3V2, October 2000, section 2.5 Single Scanner Footprint TOA/Surface Fluxes and Clouds (SSF)",
                     "@type": "dcat:Distribution",
+                    "description": "Read Me - CERES Data Products Catalog R3V2, October 2000, section 2.5 Single Scanner Footprint TOA/Surface Fluxes and Clouds (SSF)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/cer_ssf_trmm-pfm-virs_subset-edition1_read_packageSSF_DPC_010008.ps",
+                    "mediaType": "application/postscript",
                     "title": "View this dataset's read me document"
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
-                    "downloadURL": "https://ceres.larc.nasa.gov/data/#ssf1deg-level-3",
-                    "description": "CERES Data Page",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Data Page",
+                    "downloadURL": "https://ceres.larc.nasa.gov/data/#ssf1deg-level-3",
+                    "mediaType": "text/html",
                     "title": "Subset this dataset using a web based subsetter"
                 },
                 {
@@ -114804,76 +114779,115 @@
                     "title": "Download this dataset through the CERES Ordering Tool"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/SSF1deg-Day/Terra-MODIS_Edition4A/",
-                    "description": "ASDC Direct Data Download for CER_SSF1deg-Day_Terra-MODIS_Edition4A",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CER_SSF1deg-Day_Terra-MODIS_Edition4A",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/SSF1deg-Day/Terra-MODIS_Edition4A/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/SSF1deg-Day/Terra-MODIS_Edition4A/contents.html",
-                    "description": "OPeNDAP data access for CER_SSF1deg-Day_Terra-MODIS_Edition4A",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CER_SSF1deg-Day_Terra-MODIS_Edition4A",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/SSF1deg-Day/Terra-MODIS_Edition4A/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1000000601-LARC_ASDC",
+            "issued": "2015-02-23",
+            "keyword": [
+                "atmospheric winds",
+                "clouds",
+                "earth science",
+                "atmosphere",
+                "atmospheric pressure",
+                "aerosols",
+                "atmospheric radiation",
+                "atmospheric temperature",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://doi.org/10.5067/TERRA/CERES/SSF1DEGDAY_L3.004",
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
+            "temporal": "2000-03-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "CERES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CERES Time-Interpolated TOA Fluxes, Clouds and Aerosols Daily Terra Edition4A"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-VIRTIS-2-ESC4-MTP024-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This release contains the digital numbers (DN) contained in the telemetry (TM) packages of the VIRTIS instrument on board of the spacecraft Rosetta. This volume contains data at the vicinity of comet 67P, from the ESCORT 4 MTP024 phase, which occurred from 2015-12-16 to 2016-01-13",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-virtis-2-esc4-mtp024-v1.0",
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
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-VIRTIS-2-ESC4-MTP024-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-virtis-2-esc4-mtp024-v1.0",
-            "description": "This release contains the digital numbers (DN) contained in the telemetry (TM) packages of the VIRTIS instrument on board of the spacecraft Rosetta. This volume contains data at the vicinity of comet 67P, from the ESCORT 4 MTP024 phase, which occurred from 2015-12-16 to 2016-01-13",
-            "title": "ROSETTA-ORBITER 67P VIRTIS 2 ESCORT 4 MTP024 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P VIRTIS 2 ESCORT 4 MTP024 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/42qh-6g7v",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Articular and sterno-costal cartilages were isolated from skeletally-mature mice flown for 30 days on the BION-M1 mission. Samples were characterized histologically for proteoglycan loss and at the gene expression levels using Affymetrix gene arrays.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-232",
+                    "mediaType": "text/html",
+                    "title": "The response of murine cartilages to 30 days of microgravity"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-232_42qh-6g7v",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "spaceflight",
                 "labeling",
@@ -114885,1280 +114899,1280 @@
                 "rna extraction",
                 "nucleic acid hybridization"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/42qh-6g7v",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-232_42qh-6g7v",
-            "description": "Articular and sterno-costal cartilages were isolated from skeletally-mature mice flown for 30 days on the BION-M1 mission. Samples were characterized histologically for proteoglycan loss and at the gene expression levels using Affymetrix gene arrays.",
-            "title": "The response of murine cartilages to 30 days of microgravity",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-232",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "The response of murine cartilages to 30 days of microgravity"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "The response of murine cartilages to 30 days of microgravity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-TEGA-4-EGSRDR-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-tega-4-egsrdr-v1.0_42rf-xkg4",
+            "issued": "2021-05-21",
+            "keyword": [
+                "phoenix",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-TEGA-4-EGSRDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-tega-4-egsrdr-v1.0_42rf-xkg4",
-            "description": "Calibrated or converted engineering, housekeeping and scientific data collected from the Thermal Evolved Gas Analyzer (TEGA) aboard the 2007 Mars Phoenix Lander.",
-            "title": "PHX MARS THERMAL EVOLVED GAS ANALYZER 4 EGSRDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "PHX MARS THERMAL EVOLVED GAS ANALYZER 4 EGSRDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/PZ3NJ5RXRH10",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MEaSUREs Phase-Based Antarctica Ice Velocity Map V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/PZ3NJ5RXRH10.",
-            "issued": "1996-01-01",
-            "temporal": "1996-01-01T00:00:00Z/2018-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-12-31",
-            "keyword": [
-                "cryosphere",
-                "earth science",
-                "snow/ice"
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
-            "identifier": "C1699753973-NSIDC_ECS",
             "description": "This data set, as part of the NASA Making Earth System Data Records for Use in Research Environments (MEaSUREs) Program, combines interferometric phases from multiple satellite interferometric synthetic-aperture radar systems to derive the first comprehensive phase-based map of Antarctic ice velocity. The precision in ice speed and flow direction over 80% of Antarctica is better than prior mappings based on feature and speckle tracking by a factor of 10. Phase-derived velocity mostly covers the years between 2007 and 2018, while tracking-derived velocity (for regions along the coasts) is mostly found in the years from 2013 to 2017. Additional data acquired between 1996 and 2018 were used as needed to maximize coverage.\n\nSee <a href=\"https://nsidc.org/data/measures/aiv\">Antarctic Ice Sheet Velocity and Mapping Data</a> for related data.",
-            "title": "MEaSUREs Phase-Based Antarctica Ice Velocity Map V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FPZ3NJ5RXRH10",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FPZ3NJ5RXRH10",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MEASURES/NSIDC-0754.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MEASURES/NSIDC-0754.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1699753973-NSIDC_ECS&q=nsidc-0754&m=-67.1%21-95.78%210%212%210%210%2C2&tl=1576701501%214%21%21",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1699753973-NSIDC_ECS&q=nsidc-0754&m=-67.1%21-95.78%210%212%210%210%2C2&tl=1576701501%214%21%21",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0754/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0754/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/PZ3NJ5RXRH10",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/PZ3NJ5RXRH10",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/PZ3NJ5RXRH10",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/PZ3NJ5RXRH10",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1699753973-NSIDC_ECS",
+            "issued": "1996-01-01",
+            "keyword": [
+                "cryosphere",
+                "earth science",
+                "snow/ice"
+            ],
+            "landingPage": "https://doi.org/10.5067/PZ3NJ5RXRH10",
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
             "spatial": "-180.0 -90.0 180.0 -60.0",
+            "temporal": "1996-01-01T00:00:00Z/2018-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MEaSUREs Phase-Based Antarctica Ice Velocity Map V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LP-L-MAG-4-LUNAR-FIELD-TS-V1.0",
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
-                "lunar prospector"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "LP magnetometer (MAG) Level 2 Data (CODMAC Level 4).\nSelected and filtered time series data at 5 second intervals.\nApproximate measurements of the lunar crustal magnetic field with\nexternal (solar wind and magnetospheric) fields removed or minimized.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lp-l-mag-4-lunar-field-ts-v1.0_42ss-x9dp",
+            "issued": "2021-05-21",
+            "keyword": [
+                "moon",
+                "lunar prospector"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LP-L-MAG-4-LUNAR-FIELD-TS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lp-l-mag-4-lunar-field-ts-v1.0_42ss-x9dp",
-            "description": "LP magnetometer (MAG) Level 2 Data (CODMAC Level 4).\nSelected and filtered time series data at 5 second intervals.\nApproximate measurements of the lunar crustal magnetic field with\nexternal (solar wind and magnetospheric) fields removed or minimized.",
-            "title": "LP Moon MAG Level 4 Lunar Magnetic Field Time Series V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "LP Moon MAG Level 4 Lunar Magnetic Field Time Series V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MIRO-3-ESC3-67P-V3.0",
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
+            "description": "This data set contains Spectroscopic and Continuum, level 3 data, in the form of table files, taken during the ROSETTA COMET ESCORT 3 phase of the Rosetta mission to comet 67P/CHURYUMOV-GERASIMENKO by the MIRO instrument.  It supercedes data sets with a lower version number. The updates include a new calibration algorithm and modified documentation.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-miro-3-esc3-67p-v3.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MIRO-3-ESC3-67P-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-miro-3-esc3-67p-v3.0",
-            "description": "This data set contains Spectroscopic and Continuum, level 3 data, in the form of table files, taken during the ROSETTA COMET ESCORT 3 phase of the Rosetta mission to comet 67P/CHURYUMOV-GERASIMENKO by the MIRO instrument.  It supercedes data sets with a lower version number. The updates include a new calibration algorithm and modified documentation.",
-            "title": "ROSETTA-ORBITER 67P MIRO 3 ESC3 V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P MIRO 3 ESC3 V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/158/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2010-09-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "ames",
-                "nasa",
-                "dashlink"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ashok Srivastava",
                 "hasEmail": "mailto:ashok.n.srivastava@gmail.com"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_158",
             "description": "The detection of clouds within a satellite image is essential for retrieving surface geophysical parameters from optical and thermal imagery. Even a small percentage of cloud cover within a radiometer pixel can adversely affect the determination of surface variables such as albedo and temperature. Thus, onboard processing of satellite data requires reliable automated cloud detection algorithms that are applicable to a wide range of surface types. Unfortunately cloud-detection, particularly over snow- and ice-covered surfaces, is a problem that plagues the field of remote sensing because of the lack of spectral contrast.\r\nThis paper discusses preliminary results based on kernel methods for unsupervised discovery of snow, ice, clouds, and other geophysical processes based on data from the MODIS instrument and discusses implementation in computationally constrained environments such as those found on satellites.",
-            "title": "Onboard Detection of Snow, Ice, Clouds, and Other Processes",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/Srivastava_ICML_2003.pdf",
-                    "description": "Paper",
                     "@type": "dcat:Distribution",
+                    "description": "Paper",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/Srivastava_ICML_2003.pdf",
+                    "mediaType": "application/pdf",
                     "title": "Srivastava_ICML_2003.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_158",
+            "issued": "2010-09-22",
+            "keyword": [
+                "ames",
+                "nasa",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/158/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Onboard Detection of Snow, Ice, Clouds, and Other Processes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1046-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-09-28T09:40:20.000 to 2015-09-28T15:10:25.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1046-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1046-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1046-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-09-28T09:40:20.000 to 2015-09-28T15:10:25.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1046 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1046 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/OLYMPEX/XPOL/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hudak, David , Peter  Rodriguez, Vlado  Stojanovic, Sudesh  Boodoo, Norman  Donaldson and Robert  Reed.2018. GPM Ground Validation CAX1 Radar ODIM format OLYMPEX [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/OLYMPEX/XPOL/DATA101",
-            "issued": "2018-02-14",
-            "temporal": "2015-11-14T23:10:04Z/2016-04-01T13:09:08Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
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
-            "identifier": "C1983295899-GHRC_DAAC",
             "description": "The GPM Ground Validation CAX1 Radar ODIM format OLYMPEX dataset consists of radar parameters, such as Radar reflectivity, Doppler velocity, Doppler width, Differential reflectivity, Differential phase, Differential phase shift, Correlation coefficient, and Signal Quality Index, provided on a 0.4 to 1.0 km spatial resolution within the OLYMPEX field campaign study region in state of Washington. These data were obtained for the GPM Ground Validation OLYMPEX field campaign by the SELEX Meteor 60DX10 Compact Weather (CAX1) radar. The CAX1 radar was located at the southern tip of Vancouver Island on the Canadian Forces Base (CFB) Esquimalt Albert Head (AHD) military training area.  These data are available in ODIM HDF-5 format, and have corresponding browse imagery in PNG format, from November 14, 2015 through April 1, 2016.",
-            "graphic-preview-description": "Browse images illustrate the nature and coverage of the data",
-            "title": "GPM Ground Validation CAX1 Radar ODIM format OLYMPEX V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/cax1_xah_odim/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FOLYMPEX%2FXPOL%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FOLYMPEX%2FXPOL%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
```

