# Change History for nasa.json (Part 103)

### Changes from 31606f9 to dd2190f (Part 92/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cal-alice-3-prl-v1.0_j9rw-akhi",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
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
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FCAL-ALICE-3-PRL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cal-alice-3-prl-v1.0_j9rw-akhi",
-            "description": "This data set contains CODMAC level 3 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the comet 67P/Churyumov-Gerasimenko prelanding mission phase, which took place between 2014-01-21 and 2014-11-18.",
-            "title": "ROSETTA-ORBITER 67P/CAL ALICE 3 PRL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P/CAL ALICE 3 PRL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/j9sx-cjqx",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "temporal": "1992-01-01/2002-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "purdue",
-                "apps",
-                "climate",
-                "hydrology"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Michael Goodman",
                 "hasEmail": "mailto:Michael.Goodman@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-0000048",
+            "describedBy": "http://ghrc.nsstc.nasa.gov/glossary.html",
             "description": "The GHRC is the data management and user services arm of the Global Hydrology and Climate Center. It encompasses the data and information management, supporting product generation, archival, and distribution of research quality and operational datasets for a variety of data types, including lightning, passive microwave, radar and others.",
-            "title": "Global Hydrology Research Center",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -961809,211 +961791,205 @@
                     "mediaType": "text/html"
                 }
             ],
+            "identifier": "NASA-0000048",
+            "issued": "2018-06-25",
+            "keyword": [
+                "purdue",
+                "apps",
+                "climate",
+                "hydrology"
+            ],
+            "landingPage": "https://data.nasa.gov/d/j9sx-cjqx",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
             "spatial": "global",
-            "describedBy": "http://ghrc.nsstc.nasa.gov/glossary.html",
-            "accrualPeriodicity": "irregular"
+            "temporal": "1992-01-01/2002-01-01",
+            "title": "Global Hydrology Research Center"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1201",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Stackhouse, P.W., S.K. Gupta, F.G. Hall, G.J. Collatz, B.W. Meeson, S.O. Los, E.Brown De Colstoun, and D.R. Landis. 2013. ISLSCP II Surface Radiation Budget (SRB) Radiation Data. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1201",
-            "issued": "2023-10-15",
-            "temporal": "1986-01-01T00:00:00Z/1995-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-18",
-            "keyword": [
-                "earth science",
-                "clouds",
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
-            "identifier": "C2785335036-ORNL_CLOUD",
             "description": "This data set contains global Surface Radiation Budget (SRB) and a few top-of-atmosphere (TOA) radiation budget parameters on a 1-degree x 1-degree spatial resolution. These parameters are provided as monthly, monthly-3 hourly (i.e. monthly average for a particular 3 hourly period) and 3-hourly averages. All monthly parameters include files with a monthly mean value, a monthly standard deviation, and monthly minimum and maximum values. The surface and TOA Shortwave (SW) radiative parameters were computed with the Pinker and Laszlo (1992) radiation model. The Longwave (LW) SRB parameters were derived with the Gupta et al. (1992) model. Meteorological inputs for all processing were taken from the Goddard Earth Observing System version 1 (GEOS-1) reanalysis data sets (Schubert et al., 1993) from the Data Assimilation Office (DAO), at NASA Goddard Space Flight Center (GSFC). Required cloud parameters were derived at NASA Langley Research Center (LaRC) from International Satellite Cloud Climatology Project (ISCCP) DX data using the algorithms developed at the NASA Goddard Institute for Space Studies (GISS) (Rossow et al., 1996). Surface albedos are derived internally in the Pinker and Laszlo SW model. There are 30 compressed data files (*.zip) with this data set. When the *.zip files are expanded, there are 114,912 3-hourly files, 42,064 diurnal files, and 6,254 monthly files.",
-            "graphic-preview-description": "Browse Image",
-            "title": "ISLSCP II Surface Radiation Budget (SRB) Radiation Data",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/islscp_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1201",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1201",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/islscp_ii/radiation_clouds/srb_radiation_1deg/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/islscp_ii/radiation_clouds/srb_radiation_1deg/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ISLSCP_II/guides/srb_radiation_1deg.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ISLSCP_II/guides/srb_radiation_1deg.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1201",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1201",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/radiation_clouds/srb_radiation_1deg/comp/0_srb_radiation_readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/radiation_clouds/srb_radiation_1deg/comp/0_srb_radiation_readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/radiation_clouds/srb_radiation_1deg/comp/1_srb_radiation_clouds_doc.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/radiation_clouds/srb_radiation_1deg/comp/1_srb_radiation_clouds_doc.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/radiation_clouds/srb_radiation_1deg/comp/srb_radiation_1deg.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/radiation_clouds/srb_radiation_1deg/comp/srb_radiation_1deg.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/radiation_clouds/srb_radiation_1deg/comp/srb_radiation_datafile_information.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/radiation_clouds/srb_radiation_1deg/comp/srb_radiation_datafile_information.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/islscp_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/islscp_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/islscp_logo_square.png",
+            "identifier": "C2785335036-ORNL_CLOUD",
+            "issued": "2023-10-15",
+            "keyword": [
+                "earth science",
+                "clouds",
+                "atmospheric radiation",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1201",
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
+            "title": "ISLSCP II Surface Radiation Budget (SRB) Radiation Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GPM/ATMS/NPP/GPROFCLIM/2A/07",
             "citation": "GPM Science Team. 2022-05-09. GPM_2AGPROFNPPATMS_CLIM. GPM ATMS on SUOMI-NPP (GPROF) Radiometer Precipitation Profiling L2 1.5 hours 16 km V07 . Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/ATMS/NPP/GPROFCLIM/2A/07. https://disc.gsfc.nasa.gov/datacollection/GPM_2AGPROFNPPATMS_CLIM_07.html. Digital Science Data.",
-            "issued": "2022-05-09",
-            "temporal": "2011-11-08T00:00:00Z/2023-02-28T00:00:00Z",
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
                 "fn": "GEORGE HUFFMAN",
                 "hasEmail": "mailto:George.J.Huffman@nasa.gov"
             },
+            "creator": "GPM Science Team",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2264134428-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Version 07 is the current version of the data set. Older versions are no longer available and have been superseded by Version 07. \n\nThe \"CLIM\"  products differ from their \"regular\" counterparts (without the \"CLIM\" in the name) by the ancillary data they use. They are Climate-Reference products, which requires homogeneous ancillary data over the climate time series.  Hence, the ECMWF-Interim (European Centre for Medium-Range Weather Forecasts, 2-3 months lag behind the regular production) reanalysis is used as ancillary data to derive surface and atmospheric conditions required by the GPROF algorithm for the \"CLIM\" output. The GPROF databases are also adjusted accordingly for these climate-referenced retrievals.\n\nThe 2AGPROF (Goddard Profiling) algorithm retrieves consistent precipitation and related science fields from the following GMI and partner passive microwave sensors:\n+ TMI (TRMM)\n+ GMI, (GPM)\n+ SSMI (DMSP F15), SSMIS (DMSP F16, F17, F18, F19)\n+ AMSR2 (GCOM-W1)\n+ MHS (NOAA 18,19)\n+ MHS (METOP A,B)\n+ ATMS (NPP)\n+ SAPHIR (MT1)\n\nThis provides the bulk of the 3-hour coverage achieved by GPM. For each sensor, there are nearrealtime (NRT) products, standard products, and climate products. These differ only in the amount of data that are available within 3 hours, 48 hours, and 3 months of collection, as well as the ancillary data used. The NRT product uses GANAL forecast fields. Standard products use the GANAL analysis product, while the climate product uses ECMWF reanalysis in order to allow for consistent data records with earlier missions. These earlier data may be archived separately. The main strength of the product is the large sampling provided.\n\nThe GPM radiometer algorithms are Bayesian-type algorithms. These algorithms search an apriori database of potential rain profiles and retrieve a weighted average of these entries based upon the proximity of the observed brightness temperature (Tb) to the simulated Tb corresponding to each rain profile. By using the same a-priori database of rain profiles, with appropriate simulated Tb for each constellation sensor, the Bayesian method is completely parametric and thus well suited for GPM's constellation approach. The a-priori information will be supplied by the combined algorithm supplied by GPM's core satellite as soon after launch as feasible. Databases for V0 of the algorithm had to be constructed from various sources as described in the ATBD. The solution provides a mean rain rate as well as the vertical structure of cloud and precipitation hydrometeors and their uncertainty.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "GPM_2AGPROFNPPATMS_CLIM",
-            "creator": "GPM Science Team",
-            "title": "GPM ATMS on SUOMI-NPP (GPROF) Radiometer Precipitation Profiling L2 1.5 hours 16 km V07 (GPM_2AGPROFNPPATMS_CLIM) at GES DISC",
-            "graphic-preview-description": "Surface Precipitation Rate from  NPP/ATMS",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_2AGPROFNPPATMS_CLIM_07.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FATMS%2FNPP%2FGPROFCLIM%2F2A%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FATMS%2FNPP%2FGPROFCLIM%2F2A%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_2AGPROFNPPATMS_CLIM_07.png",
-                    "description": "Surface Precipitation Rate from  NPP/ATMS",
                     "@type": "dcat:Distribution",
+                    "description": "Surface Precipitation Rate from  NPP/ATMS",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_2AGPROFNPPATMS_CLIM_07.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_2AGPROFNPPATMS_CLIM_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_2AGPROFNPPATMS_CLIM_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L2/GPM_2AGPROFNPPATMS_CLIM.07/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L2/GPM_2AGPROFNPPATMS_CLIM.07/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L2/GPM_2AGPROFNPPATMS_CLIM.07/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L2/GPM_2AGPROFNPPATMS_CLIM.07/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_2AGPROFNPPATMS_CLIM_07",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_2AGPROFNPPATMS_CLIM_07",
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
@@ -962023,694 +961999,697 @@
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
-                    "downloadURL": "https://www.star.nesdis.noaa.gov/mirs/snppatms.php",
-                    "description": "Instrument Description",
                     "@type": "dcat:Distribution",
+                    "description": "Instrument Description",
+                    "downloadURL": "https://www.star.nesdis.noaa.gov/mirs/snppatms.php",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Surface Precipitation Rate from  NPP/ATMS",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_2AGPROFNPPATMS_CLIM_07.png",
+            "identifier": "C2264134428-GES_DISC",
+            "issued": "2022-05-09",
+            "keyword": [
+                "atmospheric water vapor",
+                "atmosphere",
+                "precipitation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/ATMS/NPP/GPROFCLIM/2A/07",
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
+            "series-name": "GPM_2AGPROFNPPATMS_CLIM",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-11-08T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "GPM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM ATMS on SUOMI-NPP (GPROF) Radiometer Precipitation Profiling L2 1.5 hours 16 km V07 (GPM_2AGPROFNPPATMS_CLIM) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/HXARUSIEQ4KM",
             "citation": "Kevin W. Bowman. 2021-03-08. TRPSDL2COCRSWCF. Version 1. TROPESS CrIS-SNPP L2 Carbon Monoxide for West Coast Fires, Standard Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/HXARUSIEQ4KM. https://disc.gsfc.nasa.gov/datacollection/TRPSDL2COCRSWCF_1.html. Digital Science Data.",
-            "issued": "2021-01-22",
-            "temporal": "2020-08-02T00:00:00Z/2020-10-26T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-22",
-            "references": [
-                "https://doi.org/10.1126/sciadv.abf7460",
-                "https://doi.org/10.1029/2006JD007663",
-                "https://doi.org/10.1029/2007JD008803",
-                "https://doi.org/10.5194/amt-9-2567-2016",
-                "https://doi.org/10.1016/j.rse.2020.112275",
-                "https://doi.org/10.5194/acp-13-837-2013"
-            ],
-            "keyword": [
-                "atmosphere",
-                "atmospheric chemistry",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "KEVIN BOWMAN",
                 "hasEmail": "mailto:kevin.w.bowman@jpl.nasa.gov"
             },
+            "creator": "Kevin W. Bowman",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1980429431-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS CrIS-SNPP L2 Carbon Monoxide for West Coast Fires, Standard Product contains the vertical distribution of the retrieved atmospheric state of carbon monoxide (CO), formal uncertainties, and diagnostic information measured by the CrIS instrument on the Suomi-NPP satellite. This product focuses on the CONUS region (20N-60N; 150W-40W) for the time period from 2020-08-01 to 2020-10-31, during the outbreak of U.S. West Coast wildfires. The NASA TRopospheric Ozone and Precursors from Earth System Sounding (TROPESS) project, uses an optimal estimation algorithm, known as the MUlti-SpEctra, MUlti-SpEcies, Multi-SEnsors (MUSES).\n\nThe data files are written in the netCDF version 4 file format, and each file contains one day of data. The data have a spatial resolution of 14 km (CrIS nadir FOV), and are reported at 14 vertical levels from the surface to 0.1 hPa. The principal investigator for the TROPESS project is Kevin W. Bowman.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSDL2COCRSWCF",
-            "creator": "Kevin W. Bowman",
-            "graphic-preview-description": "TROPESS CrIS/SNPP CO (West Coast Fires, Special Product) at 383 hPa on 12 September 2020.",
-            "title": "TROPESS CrIS-SNPP L2 Carbon Monoxide for West Coast Fires, Standard Product V1 (TRPSDL2COCRSWCF) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2COCRSWCF_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FHXARUSIEQ4KM",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FHXARUSIEQ4KM",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2COCRSWCF_Sample.png",
-                    "description": "TROPESS CrIS/SNPP CO (West Coast Fires, Special Product) at 383 hPa on 12 September 2020.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS CrIS/SNPP CO (West Coast Fires, Special Product) at 383 hPa on 12 September 2020.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2COCRSWCF_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2COCRSWCF_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2COCRSWCF_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Special/TRPSDL2COCRSWCF.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Special/TRPSDL2COCRSWCF.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2COCRSWCF_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2COCRSWCF_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Special/TRPSDL2COCRSWCF.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Special/TRPSDL2COCRSWCF.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Special/TRPSDL2COCRSWCF.1/doc/TROPESS_West_Coast_Fires_README_2-23-21.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Special/TRPSDL2COCRSWCF.1/doc/TROPESS_West_Coast_Fires_README_2-23-21.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/User_Guides/TROPESS-AIRS-CrIS_CO_L2_Product_User_Guide_v1_2-22-21.pdf",
-                    "description": "User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "User's Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/User_Guides/TROPESS-AIRS-CrIS_CO_L2_Product_User_Guide_v1_2-22-21.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
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
+            "graphic-preview-description": "TROPESS CrIS/SNPP CO (West Coast Fires, Special Product) at 383 hPa on 12 September 2020.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2COCRSWCF_Sample.png",
+            "identifier": "C1980429431-GES_DISC",
+            "issued": "2021-01-22",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/HXARUSIEQ4KM",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-01-22",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1126/sciadv.abf7460",
+                "https://doi.org/10.1029/2006JD007663",
+                "https://doi.org/10.1029/2007JD008803",
+                "https://doi.org/10.5194/amt-9-2567-2016",
+                "https://doi.org/10.1016/j.rse.2020.112275",
+                "https://doi.org/10.5194/acp-13-837-2013"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "TRPSDL2COCRSWCF",
             "spatial": "-150.0 20.0 -40.0 60.0",
+            "temporal": "2020-08-02T00:00:00Z/2020-10-26T23:59:59.999Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS CrIS-SNPP L2 Carbon Monoxide for West Coast Fires, Standard Product V1 (TRPSDL2COCRSWCF) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-A-SSI-3-IDA-CALIMAGES-V1.0",
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
-                "243 ida",
-                "galileo"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set includes Galileo Orbiter   SSI radiometrically calibrated images of the asteroid 243 Ida, created using ISIS software and assuming nadir pointing. This is an original   delivery of radiometrically calibrated files, not an update to         existing files. All images archived include the asteroid within the    image frame. Calibration was performed in 2013-2014.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-a-ssi-3-ida-calimages-v1.0_j9zj-zxgw",
+            "issued": "2018-06-26",
+            "keyword": [
+                "243 ida",
+                "galileo"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-A-SSI-3-IDA-CALIMAGES-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-a-ssi-3-ida-calimages-v1.0_j9zj-zxgw",
-            "description": "This data set includes Galileo Orbiter   SSI radiometrically calibrated images of the asteroid 243 Ida, created using ISIS software and assuming nadir pointing. This is an original   delivery of radiometrically calibrated files, not an update to         existing files. All images archived include the asteroid within the    image frame. Calibration was performed in 2013-2014.",
-            "title": "GALILEO SSI/IDA RADIOMETRICALLY         \n        CALIBRATED IMAGES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GALILEO SSI/IDA RADIOMETRICALLY         \n        CALIBRATED IMAGES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1615905764-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, OB.DAAC.",
-            "issued": "2019-06-23",
-            "temporal": "2002-07-04T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-10-01",
-            "keyword": [
-                "oceans",
-                "ocean temperature",
-                "ngda",
-                "national geospatial data asset",
-                "earth science"
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
-            "identifier": "C1615905764-OB_DAAC",
             "description": "MODIS (or Moderate Resolution Imaging Spectroradiometer) is a key instrument aboard the Terra (EOS AM) and Aqua (EOS PM) satellites. Terra's orbit around the Earth is timed so that it passes from north to south across the equator in the morning, while Aqua passes south to north over the equator in the afternoon. Terra MODIS and Aqua MODIS are viewing the entire Earth's surface every 1 to 2 days, acquiring data in 36 spectral bands, or groups of wavelengths (see MODIS Technical Specifications). These data will improve our understanding of global dynamics and processes occurring on the land, in the oceans, and in the lower atmosphere. MODIS is playing a vital role in the development of validated, global, interactive Earth system models able to predict global change accurately enough to assist policy makers in making sound decisions concerning the protection of our environment.",
-            "title": "Aqua MODIS Regional 4\u00b5m Nighttime Sea Surface Temperature (SST4) Data, version R2019.0",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/AQUA/MODIS/L2/SST4/R2019.0",
-                    "description": "MODIS-Aqua L2 4\u00b5m Nighttime Sea Surface Temperature (SST4) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS-Aqua L2 4\u00b5m Nighttime Sea Surface Temperature (SST4) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/AQUA/MODIS/L2/SST4/R2019.0",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1615905764-OB_DAAC",
+            "issued": "2019-06-23",
+            "keyword": [
+                "oceans",
+                "ocean temperature",
+                "ngda",
+                "national geospatial data asset",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1615905764-OB_DAAC.html",
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
+            "title": "Aqua MODIS Regional 4\u00b5m Nighttime Sea Surface Temperature (SST4) Data, version R2019.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1111",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Masarie, K.A., F.G. Hall, G.J. Collatz, B.W. Meeson, S.O. Los, E.Brown De Colstoun, and D.R. Landis. 2012. ISLSCP II Globalview: Atmospheric CO2 Concentrations. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1111",
-            "issued": "2023-10-15",
-            "temporal": "1979-01-01T00:00:00Z/2001-01-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-18",
-            "keyword": [
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
-            "identifier": "C2785323218-ORNL_CLOUD",
             "description": "The GlobalView Carbon Dioxide (CO2) data product contains synchronized and smoothed time series of atmospheric CO2 concentrations at selected sites that were created using the data extension and integration techniques described by Masarie and Tans, (1995). The information needed to derive this time series is also in this data set, along with extensive documentation. The longest period of coverage is from 1979 to 2001 with some sites having longer or shorter temporal coverage. Note that the GlobalView CO2 data products are derived from measurements but contain no actual data. To facilitate heterogeneous CO2 data use in carbon cycle modeling studies, the measurements have been processed (smoothed, interpolated, and extrapolated) resulting in extended records that are evenly incremented in time. There are 92 files with this data set which includes 89 *.zip data files. The other three files include 2  files with site information, one comma-delimited ASCII file (.csv), and one .dat file, and one .dat file which is a single reference marine boundary layer matrix file which contains CO2 mixing ratios as a function of time and sine of latitude and is a by-product of the data extension procedure.",
-            "graphic-preview-description": "Browse Image",
-            "title": "ISLSCP II Globalview: Atmospheric CO2 Concentrations",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/islscp_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1111",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1111",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/islscp_ii/carbon/globalview_co2_point/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/islscp_ii/carbon/globalview_co2_point/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ISLSCP_II/guides/globalview_co2_point.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ISLSCP_II/guides/globalview_co2_point.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1111",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1111",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/carbon/globalview_co2_point/comp/0_globalview_co2_readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/carbon/globalview_co2_point/comp/0_globalview_co2_readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/carbon/globalview_co2_point/comp/1_globalview_co2_doc.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/carbon/globalview_co2_point/comp/1_globalview_co2_doc.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/carbon/globalview_co2_point/comp/2_gv_co2_2003_doc.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/carbon/globalview_co2_point/comp/2_gv_co2_2003_doc.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/carbon/globalview_co2_point/comp/globalview_co2_point.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/carbon/globalview_co2_point/comp/globalview_co2_point.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/islscp_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/islscp_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/islscp_logo_square.png",
+            "identifier": "C2785323218-ORNL_CLOUD",
+            "issued": "2023-10-15",
+            "keyword": [
+                "earth science",
+                "atmospheric chemistry",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1111",
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
+            "temporal": "1979-01-01T00:00:00Z/2001-01-31T23:59:59Z",
             "theme": [
                 "ISLSCP II",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISLSCP II Globalview: Atmospheric CO2 Concentrations"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VL1%2FVL2-M-MET-3-P-V1.0",
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
+            "description": "This data set contains the martian surface atmospheric pressure readings obtained through much of the duration of the Viking Lander 1 and 2 missions (data are included for Viking Lander 1 sols 0 - 2245 and Viking Lander 2 sols 0 - 1050). The data are derived from the ambient pressure sensor carried onboard the Landers and values are presented on a point by point basis. The sampling rate was variable throughout the mission maximum sampling rate was one measurement per second, but ranged up to 65 minutes for Lander 1 and 105 minutes for Lander 2. For further background information on the Viking Meteorology Instrument System (VMIS) and results from this experiment, see CHAMBERLAIN_ETAL1976, HESS_ETAL_1976A, HESS_ETAL_1976B, and HESS_ETAL_1977. For discussions of analyses of experiment data, see also TILLMAN_1977, HESS_ETAL_1980, and TILLMAN_1988. An earlier version of this data set is archived at the NSSDC (NSSDC ID 75-075C-07D and 75-083C-07D).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vl1-vl2-m-met-3-p-v1.0_ja2u-iniy",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "viking"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VL1%2FVL2-M-MET-3-P-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vl1-vl2-m-met-3-p-v1.0_ja2u-iniy",
-            "description": "This data set contains the martian surface atmospheric pressure readings obtained through much of the duration of the Viking Lander 1 and 2 missions (data are included for Viking Lander 1 sols 0 - 2245 and Viking Lander 2 sols 0 - 1050). The data are derived from the ambient pressure sensor carried onboard the Landers and values are presented on a point by point basis. The sampling rate was variable throughout the mission maximum sampling rate was one measurement per second, but ranged up to 65 minutes for Lander 1 and 105 minutes for Lander 2. For further background information on the Viking Meteorology Instrument System (VMIS) and results from this experiment, see CHAMBERLAIN_ETAL1976, HESS_ETAL_1976A, HESS_ETAL_1976B, and HESS_ETAL_1977. For discussions of analyses of experiment data, see also TILLMAN_1977, HESS_ETAL_1980, and TILLMAN_1988. An earlier version of this data set is archived at the NSSDC (NSSDC ID 75-075C-07D and 75-083C-07D).",
-            "title": "VL1/VL2 MARS METEOROLOGY DATA CALIBRATED DATA PRESSURE V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VL1/VL2 MARS METEOROLOGY DATA CALIBRATED DATA PRESSURE V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1063-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-09-28T03:06:40.000 to 2015-09-28T09:23:25.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1063-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1063-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1063-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-09-28T03:06:40.000 to 2015-09-28T09:23:25.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1063 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1063 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/PRESW-NPJ10",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Menemenlis, D., Hill, C., Henze, C. E., Wang, J., & Fenty, I.. 2021-02-10. Northwest Pacific Pre-SWOT Level-4 Hourly MITgcm LLC4320 Native Grid 2km Oceanographic Dataset Version 1.0. Version 1.0. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/PRESW-NPJ10. Menemenlis, D., Hill, C., Henze, C. E., Wang, J., & Fenty, I. 2021. Northwest Pacific Pre-SWOT Level-4 Hourly MITgcm LLC4320 Native Grid 2km Oceanographic Dataset Version 1.0. PO.DAAC, CA, USA. Dataset accessed[YYYY-MM-DD] at https://doi.org/10.5067/PRESW-NPJ10.",
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
-                "ocean heat budget",
-                "ocean circulation",
-                "oceans",
-                "earth science",
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
-            "identifier": "C2006849488-POCLOUD",
-            "description": "This dataset provides a regional multivariate oceanographic state estimate from a global ocean numerical simulation with a focus on the Northwest Pacific Ocean region. The global ocean simulation is based on the MIT general circulation model (MITgcm) with Lat-Lon-Cap grid (LLC) layout and 1/48-degree (2km at equator) nominal horizontal resolution. This simulation is often referred to as LLC4320 in the community and existing publications. The simulation has 90 vertical levels, with about 1-m vertical resolution at the surface and 30 m down to 500 m, for optimized resolution of the upper-ocean processes. The model has zero parameterized horizontal diffusivity. In the vertical direction, the K-Profile Parameterization (KPP) is used for boundary layer turbulent mixing. It is spun up progressively from the lower resolution MITgcm simulation from the Estimating the Circulation & Climate of the Ocean (ECCO), and forced by the 6-hourly ERA-Interim atmosphere reanalysis ( https://www.ecmwf.int/en/forecasts/datasets/reanalysis-datasets/era-interim ). A synthetic surface pressure field consisting of the 16 most dominant tidal constituents is used to dynamically mimic the tidal forcing. The dataset provides hourly oceanographic variables at native grid. Three-dimensional variables include temperature, salinity, and velocity. Two-dimensional variables include sea level anomaly, ocean mixed layer thickness, bottom pressure anomaly, net freshwater flux, net heat flux, shortwave radiative flux, net salt flux, and ocean surface stress.",
-            "release-place": "PO.DAAC",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Menemenlis, D., Hill, C., Henze, C. E., Wang, J., & Fenty, I.",
-            "title": "Northwest Pacific Pre-SWOT Level-4 Hourly MITgcm LLC4320 Native Grid 2km Oceanographic Dataset Version 1.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MITgcm_LLC4320_Pre-SWOT_JPL_L4_NWPacific_v1.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset provides a regional multivariate oceanographic state estimate from a global ocean numerical simulation with a focus on the Northwest Pacific Ocean region. The global ocean simulation is based on the MIT general circulation model (MITgcm) with Lat-Lon-Cap grid (LLC) layout and 1/48-degree (2km at equator) nominal horizontal resolution. This simulation is often referred to as LLC4320 in the community and existing publications. The simulation has 90 vertical levels, with about 1-m vertical resolution at the surface and 30 m down to 500 m, for optimized resolution of the upper-ocean processes. The model has zero parameterized horizontal diffusivity. In the vertical direction, the K-Profile Parameterization (KPP) is used for boundary layer turbulent mixing. It is spun up progressively from the lower resolution MITgcm simulation from the Estimating the Circulation & Climate of the Ocean (ECCO), and forced by the 6-hourly ERA-Interim atmosphere reanalysis ( https://www.ecmwf.int/en/forecasts/datasets/reanalysis-datasets/era-interim ). A synthetic surface pressure field consisting of the 16 most dominant tidal constituents is used to dynamically mimic the tidal forcing. The dataset provides hourly oceanographic variables at native grid. Three-dimensional variables include temperature, salinity, and velocity. Two-dimensional variables include sea level anomaly, ocean mixed layer thickness, bottom pressure anomaly, net freshwater flux, net heat flux, shortwave radiative flux, net salt flux, and ocean surface stress.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FPRESW-NPJ10",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FPRESW-NPJ10",
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
-                    "downloadURL": "https://doi.org/10.5067/PRESW-NPJ10",
-                    "description": "Access the dataset landing page for the collection",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page for the collection",
+                    "downloadURL": "https://doi.org/10.5067/PRESW-NPJ10",
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MITgcm_LLC4320_Pre-SWOT_JPL_L4_NWPacific_v1.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MITgcm_LLC4320_Pre-SWOT_JPL_L4_NWPacific_v1.0.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2006849488-POCLOUD",
-                    "description": "Browse and download granules over HTTPS using the virtual directories",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2006849488-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MITgcm_LLC4320_Pre-SWOT_JPL_L4_NWPacific_v1.0.jpg",
+            "identifier": "C2006849488-POCLOUD",
+            "issued": "2021-01-20",
+            "keyword": [
+                "salinity/density",
+                "ocean heat budget",
+                "ocean circulation",
+                "oceans",
+                "earth science",
+                "ocean temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/PRESW-NPJ10",
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
             "spatial": "132.9062 19.00565 136.8854 22.99216",
+            "temporal": "2011-09-13T00:00:00Z/2012-11-15T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Northwest Pacific Pre-SWOT Level-4 Hourly MITgcm LLC4320 Native Grid 2km Oceanographic Dataset Version 1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/CLDPROP_L2_VIIRS_SNPP.011",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA VIIRS Atmosphere SIPS. 2019-11-15. VIIRS/SNPP Cloud Properties 6-min L2 Swath 750m. Version 1.1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/VIIRS/CLDPROP_L2_VIIRS_SNPP.011. https://doi.org/10.5067/VIIRS/CLDPROP_L2_VIIRS_SNPP.011.",
-            "issued": "2019-08-01",
-            "temporal": "2012-03-01T00:00:00Z/2024-06-24T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-17",
-            "references": [
-                "https://doi.org/10.5067/VIIRS/CLDPROP_L2_VIIRS_SNPP.011"
-            ],
-            "keyword": [
-                "infrared wavelengths",
-                "visible wavelengths",
-                "spectral/engineering",
-                "clouds",
-                "earth science",
-                "atmosphere"
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
-            "identifier": "C1643492740-LAADS",
-            "description": "The VIIRS/SNPP Cloud Properties 6-min L2 Swath 750m product is designed to facilitate continuity in cloud properties between the MODIS (Moderate Resolution Imaging Spectroradiometer) on the Aqua and Terra platforms and the series of VIIRS (Visible Infrared Imaging Radiometer Suite) instruments, beginning with the Suomi NPP spacecraft. The VIIRS Cloud Properties product consists of cloud optical and physical parameters. These parameters are derived using observations in visible through infrared spectral channels. VIIRS infrared channel radiances are primarily used to derive cloud top temperature, cloud top height, effective emissivity, an infrared cloud phase product (ice vs. water, opaque vs. non-opaque) and cloud fraction under both daytime and nighttime conditions. The VIIRS solar reflectance channels are primarily used to derive cloud optical thickness, particle effective radius, water path, and to inform the phase used in the optical retrievals. The VIIRS Cloud Properties product is a Level-2 product generated at 750 m (at nadir) spatial resolution.\r\n\r\nThe current version-1.1 of the Level-2 CLDPROP product collection is corrected to address an issue with the cloud optical properties\u2019 thermodynamic phase that caused erroneous liquid water cloud phase results.",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "NASA VIIRS Atmosphere SIPS",
-            "title": "VIIRS/SNPP Cloud Properties 6-min L2 Swath 750m",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The VIIRS/SNPP Cloud Properties 6-min L2 Swath 750m product is designed to facilitate continuity in cloud properties between the MODIS (Moderate Resolution Imaging Spectroradiometer) on the Aqua and Terra platforms and the series of VIIRS (Visible Infrared Imaging Radiometer Suite) instruments, beginning with the Suomi NPP spacecraft. The VIIRS Cloud Properties product consists of cloud optical and physical parameters. These parameters are derived using observations in visible through infrared spectral channels. VIIRS infrared channel radiances are primarily used to derive cloud top temperature, cloud top height, effective emissivity, an infrared cloud phase product (ice vs. water, opaque vs. non-opaque) and cloud fraction under both daytime and nighttime conditions. The VIIRS solar reflectance channels are primarily used to derive cloud optical thickness, particle effective radius, water path, and to inform the phase used in the optical retrievals. The VIIRS Cloud Properties product is a Level-2 product generated at 750 m (at nadir) spatial resolution.\r\n\r\nThe current version-1.1 of the Level-2 CLDPROP product collection is corrected to address an issue with the cloud optical properties\u2019 thermodynamic phase that caused erroneous liquid water cloud phase results.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FCLDPROP_L2_VIIRS_SNPP.011",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FCLDPROP_L2_VIIRS_SNPP.011",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/CLDPROP_L2_VIIRS_SNPP--5111",
-                    "description": "Search and order VIIRS/SNPP Level 2 Cloud Properties product from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order VIIRS/SNPP Level 2 Cloud Properties product from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/CLDPROP_L2_VIIRS_SNPP--5111",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/5111/CLDPROP_L2_VIIRS_SNPP/",
-                    "description": "Link to LAADS archive for CLDPROP_L2_VIIRS_SNPP data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Link to LAADS archive for CLDPROP_L2_VIIRS_SNPP data set.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/5111/CLDPROP_L2_VIIRS_SNPP/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/5111/CLDPROP_L2_VIIRS_SNPP/contents.html",
-                    "description": "Direct link to Collection's OPeNDAP directory",
                     "@type": "dcat:Distribution",
+                    "description": "Direct link to Collection's OPeNDAP directory",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/5111/CLDPROP_L2_VIIRS_SNPP/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/CLDPROP_L2_VIIRS_SNPP.011",
-                    "description": "Product DOI landing page",
                     "@type": "dcat:Distribution",
+                    "description": "Product DOI landing page",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/CLDPROP_L2_VIIRS_SNPP.011",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://atmosphere-imager.gsfc.nasa.gov/sites/default/files/ModAtmo/EOSSNPPCloudOpticalPropertyContinuityProductUserGuidev1.pdf",
-                    "description": "VIIRS Cloud Properties User\u2019s Guide",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS Cloud Properties User\u2019s Guide",
+                    "downloadURL": "https://atmosphere-imager.gsfc.nasa.gov/sites/default/files/ModAtmo/EOSSNPPCloudOpticalPropertyContinuityProductUserGuidev1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "identifier": "C1643492740-LAADS",
+            "issued": "2019-08-01",
+            "keyword": [
+                "infrared wavelengths",
+                "visible wavelengths",
+                "spectral/engineering",
+                "clouds",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/CLDPROP_L2_VIIRS_SNPP.011",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-06-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/HBSL/BISB/MODAPS"
+            },
+            "references": [
+                "https://doi.org/10.5067/VIIRS/CLDPROP_L2_VIIRS_SNPP.011"
+            ],
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-03-01T00:00:00Z/2024-06-24T00:00:00Z",
             "theme": [
                 "Suomi-NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/SNPP Cloud Properties 6-min L2 Swath 750m"
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
-                "tool",
-                "software",
-                "product",
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
-            "identifier": "NASA-473",
             "description": "PDS Software Release Product Tools (3.3.0)",
-            "title": "PDS Software Release Product Tools (3.3.0)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -962718,87 +962697,71 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-473",
+            "issued": "2018-06-25",
+            "keyword": [
+                "tool",
+                "software",
+                "product",
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
+            "title": "PDS Software Release Product Tools (3.3.0)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/656",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Olson, R.J., C.J. Emerson, and M.K. Nungesser. 2017. Geoecology: County-Level Environmental Data for the United States, 1941-1981. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/656",
-            "issued": "2017-08-17",
-            "temporal": "1941-01-01T00:00:00Z/1981-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-05",
-            "keyword": [
-                "earth science",
-                "human dimensions",
-                "agricultural plant science",
-                "solid earth",
-                "climate indicators",
-                "air quality",
-                "atmospheric/ocean indicators",
-                "atmosphere",
-                "soils",
-                "ecological dynamics",
-                "vegetation",
-                "population",
-                "land use/land cover",
-                "land surface",
-                "rocks/minerals/crystals",
-                "economic resources",
-                "agriculture",
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
-            "identifier": "C2761762895-ORNL_CLOUD",
             "description": "The Geoecology database is a compilation of environmental data for the period 1941 to 1981. The Geoecology database contains selected data on terrain and soils, water resources, forestry, vegetation, agriculture, land use, wildlife, air quality, climate, natural areas, and endangered species. Data on selected human population characteristics are also included to complement the environmental files. Data represent the conterminous United States at the county level. These historical data are provided as a source of 1970s baseline environmental conditions for the United States.",
-            "graphic-preview-description": "Browse Image",
-            "title": "Geoecology: County-Level Environmental Data for the United States, 1941-1981",
-            "graphic-preview-file": "https://daac.ornl.gov/VEGETATION/guides/geoecology_R1_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F656",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F656",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/geoecology_R1/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/geoecology_R1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/geoecology_R1.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/geoecology_R1.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/656",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/656",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
@@ -962844,553 +962807,592 @@
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/geoecology_R1_Fig1.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/geoecology_R1_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/VEGETATION/guides/geoecology_R1_Fig1.png",
+            "identifier": "C2761762895-ORNL_CLOUD",
+            "issued": "2017-08-17",
+            "keyword": [
+                "earth science",
+                "human dimensions",
+                "agricultural plant science",
+                "solid earth",
+                "climate indicators",
+                "air quality",
+                "atmospheric/ocean indicators",
+                "atmosphere",
+                "soils",
+                "ecological dynamics",
+                "vegetation",
+                "population",
+                "land use/land cover",
+                "land surface",
+                "rocks/minerals/crystals",
+                "economic resources",
+                "agriculture",
+                "biosphere",
+                "ecosystems"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/656",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-09-05",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-124.76 24.5 -66.95 49.38",
+            "temporal": "1941-01-01T00:00:00Z/1981-12-31T23:59:59Z",
             "theme": [
                 "Vegetation",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Geoecology: County-Level Environmental Data for the United States, 1941-1981"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCIES-3-EXT1-V1.0",
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
+            "description": "This dataset contains CALIBRATED DATA of the Rosetta RPCIES instrument taken during the Rosetta Extension 1 phase (EXT1). The target of this phase was comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). Included are the data taken between 01 Jan 2016 and 05 Apr 2016.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcies-3-ext1-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCIES-3-EXT1-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcies-3-ext1-v1.0",
-            "description": "This dataset contains CALIBRATED DATA of the Rosetta RPCIES instrument taken during the Rosetta Extension 1 phase (EXT1). The target of this phase was comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). Included are the data taken between 01 Jan 2016 and 05 Apr 2016.",
-            "title": "ROSETTA-ORBITER 67P RPCIES 3 EXT1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCIES 3 EXT1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3338-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-08-23T03:33:30.000 to 2012-08-23T06:12:49.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3338-v1.0_jaaa-9swb",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars express"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3338-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3338-v1.0_jaaa-9swb",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-08-23T03:33:30.000 to 2012-08-23T06:12:49.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3338 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3338 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-C-ROLIS-3-SDL-V1.0",
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
+            "description": "This archive contains calibrated images from the ROLIS instrument onboard ROSETTA Lander, acquired during the SDL phase. The primary target is the comet 67P/CHURYUMOV-GERASIMENKO. It also contains documentation which describes the ROLIS experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-c-rolis-3-sdl-v1.0_jac3-2ygk",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-C-ROLIS-3-SDL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-c-rolis-3-sdl-v1.0_jac3-2ygk",
-            "description": "This archive contains calibrated images from the ROLIS instrument onboard ROSETTA Lander, acquired during the SDL phase. The primary target is the comet 67P/CHURYUMOV-GERASIMENKO. It also contains documentation which describes the ROLIS experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER 67P ROLIS 3 SDL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-LANDER 67P ROLIS 3 SDL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-C-HRII-2-EPOXI-ISON-V1.0",
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
-                "c/ison (2012 s1)",
-                "epoxi"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains raw, 1.05- to 4.8-micron spectral images of comet C/ISON (2012 S1) acquired by the High Resolution Infrared Spectrometer on 16-17 February 2013 during the Cruise 3 phase of the EPOXI mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-c-hrii-2-epoxi-ison-v1.0_jaca-f8b5",
+            "issued": "2018-06-26",
+            "keyword": [
+                "c/ison (2012 s1)",
+                "epoxi"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-C-HRII-2-EPOXI-ISON-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-c-hrii-2-epoxi-ison-v1.0_jaca-f8b5",
-            "description": "This dataset contains raw, 1.05- to 4.8-micron spectral images of comet C/ISON (2012 S1) acquired by the High Resolution Infrared Spectrometer on 16-17 February 2013 during the Cruise 3 phase of the EPOXI mission.",
-            "title": "EPOXI C/ISON (2012 S1) - HRII RAW SPECTRA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "EPOXI C/ISON (2012 S1) - HRII RAW SPECTRA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GHAM2-2PR82",
             "citation": "Remote Sensing Systems. 2023-01-26. GHRSST Level 2P Global Subskin Sea Surface Temperature from the Advanced Microwave Scanning Radiometer 2 on the GCOM-W satellite. Version 8.2. AMSR2 geolocated L2 swath SST data set. Santa Rosa, CA, USA. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/GHAM2-2PR82. http://www.remss.com.",
-            "issued": "2017-09-18",
-            "temporal": "2012-07-02T19:00:44Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-09-18",
-            "references": [
-                "https://doi.org/10.1109/IGARSS.2005.1526780"
-            ],
-            "keyword": [
-                "oceans",
-                "earth science",
-                "ocean temperature"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
             },
-            "identifier": "C2596983413-POCLOUD",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "description": "This product provides a \u201cFinal\u201d (Refined) Level-2 Sea Surface Temperature (SST) (currently identified by \"v8.2\" within the file name) for the Group for High Resolution Sea Surface Temperature (GHRSST) Project, which is derived from the Advanced Microwave Scanning Radiometer 2 (AMSR2) by Remote Sensing Systems (RSS, or REMSS). AMSR2 was launched on 18 May 2012, onboard the Global Change Observation Mission - Water (GCOM-W) satellite developed by the Japan Aerospace Exploration Agency (JAXA). The GCOM-W mission aims to establish the global and long-term observation system to collect data, which is needed to understand mechanisms of climate and water cycle variations, and demonstrate its utilization. AMSR2 onboard the first generation of the GCOM-W satellite will continue Aqua/AMSR-E observations of water vapor, cloud liquid water, precipitation, SST, sea surface wind speed, sea ice concentration, snow depth, and soil moisture. AMSR2 is a remote sensing instrument for measuring weak microwave emission from the surface and the atmosphere of the Earth. The antenna of AMSR2 rotates once per 1.5 seconds and obtains data over a 1450 km swath. This conical scan mechanism enables AMSR2 to acquire a set of daytime and nighttime data with more than 99% coverage of the Earth every 2 days. The \u201cFinal\u201d SSTs are processed when RSS receives the atmospheric model National Center for Environmental Prediction (NCEP) Final Analysis (FNL) Operational Global Analysis. The NCEP wind directions are particularly useful for retrieving more accurate SSTs and wind speeds. The v8.2 supersedes the previous v8a dataset which can be found at https://www.doi.org/10.5067/GHAM2-2PR8A.",
-            "release-place": "Santa Rosa, CA, USA",
-            "series-name": "GHRSST Level 2P Global Subskin Sea Surface Temperature from the Advanced Microwave Scanning Radiometer 2 on the GCOM-W satellite",
             "creator": "Remote Sensing Systems",
-            "title": "GHRSST Level 2P Global Subskin Sea Surface Temperature version 8.2 (v8.2) from the Advanced Microwave Scanning Radiometer 2 (AMSR2) by REMSS",
-            "graphic-preview-description": "Thumbnail",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AMSR2-REMSS-L2P-v8.2.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This product provides a \u201cFinal\u201d (Refined) Level-2 Sea Surface Temperature (SST) (currently identified by \"v8.2\" within the file name) for the Group for High Resolution Sea Surface Temperature (GHRSST) Project, which is derived from the Advanced Microwave Scanning Radiometer 2 (AMSR2) by Remote Sensing Systems (RSS, or REMSS). AMSR2 was launched on 18 May 2012, onboard the Global Change Observation Mission - Water (GCOM-W) satellite developed by the Japan Aerospace Exploration Agency (JAXA). The GCOM-W mission aims to establish the global and long-term observation system to collect data, which is needed to understand mechanisms of climate and water cycle variations, and demonstrate its utilization. AMSR2 onboard the first generation of the GCOM-W satellite will continue Aqua/AMSR-E observations of water vapor, cloud liquid water, precipitation, SST, sea surface wind speed, sea ice concentration, snow depth, and soil moisture. AMSR2 is a remote sensing instrument for measuring weak microwave emission from the surface and the atmosphere of the Earth. The antenna of AMSR2 rotates once per 1.5 seconds and obtains data over a 1450 km swath. This conical scan mechanism enables AMSR2 to acquire a set of daytime and nighttime data with more than 99% coverage of the Earth every 2 days. The \u201cFinal\u201d SSTs are processed when RSS receives the atmospheric model National Center for Environmental Prediction (NCEP) Final Analysis (FNL) Operational Global Analysis. The NCEP wind directions are particularly useful for retrieving more accurate SSTs and wind speeds. The v8.2 supersedes the previous v8a dataset which can be found at https://www.doi.org/10.5067/GHAM2-2PR8A.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHAM2-2PR82",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHAM2-2PR82",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://suzaku.eorc.jaxa.jp/GCOM_W/w_amsr2/whats_amsr2.html",
-                    "description": "Full details of the AMSR2",
                     "@type": "dcat:Distribution",
+                    "description": "Full details of the AMSR2",
+                    "downloadURL": "http://suzaku.eorc.jaxa.jp/GCOM_W/w_amsr2/whats_amsr2.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/SeaSurfaceTemperature",
-                    "description": "Sea Surface Temperature measurement description.",
                     "@type": "dcat:Distribution",
+                    "description": "Sea Surface Temperature measurement description.",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/SeaSurfaceTemperature",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AMSR2-REMSS-L2P-v8.2.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AMSR2-REMSS-L2P-v8.2.jpg",
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
-                    "downloadURL": "https://www.remss.com/missions/amsr/",
-                    "description": "AMSR2 SSTs: algorithm description, browsing of data, and ftp of data",
                     "@type": "dcat:Distribution",
+                    "description": "AMSR2 SSTs: algorithm description, browsing of data, and ftp of data",
+                    "downloadURL": "https://www.remss.com/missions/amsr/",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2596983413-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2596983413-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2596983413-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2596983413-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AMSR2-REMSS-L2P-v8.2.jpg",
+            "identifier": "C2596983413-POCLOUD",
+            "issued": "2017-09-18",
+            "keyword": [
+                "oceans",
+                "earth science",
+                "ocean temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/GHAM2-2PR82",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-09-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.1109/IGARSS.2005.1526780"
+            ],
+            "release-place": "Santa Rosa, CA, USA",
+            "series-name": "GHRSST Level 2P Global Subskin Sea Surface Temperature from the Advanced Microwave Scanning Radiometer 2 on the GCOM-W satellite",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-07-02T19:00:44Z/2023-02-28T00:00:00Z",
             "theme": [
                 "GHRSST",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GHRSST Level 2P Global Subskin Sea Surface Temperature version 8.2 (v8.2) from the Advanced Microwave Scanning Radiometer 2 (AMSR2) by REMSS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1000000580-LARC_ASDC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC.",
-            "issued": "2009-03-03",
-            "temporal": "2006-02-01T00:00:00Z/2006-05-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-04-25",
-            "keyword": [
-                "nasa"
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
-            "identifier": "C1000000580-LARC_ASDC",
             "description": "INTEX-B Satellite data.",
-            "title": "INTEXB_SATELLITE",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1000000580-LARC_ASDC.html",
-                    "description": "View this dataset on the CMR (Common Metadata Repository)",
                     "@type": "dcat:Distribution",
+                    "description": "View this dataset on the CMR (Common Metadata Repository)",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1000000580-LARC_ASDC.html",
+                    "mediaType": "text/html",
                     "title": "CMR"
                 }
             ],
+            "identifier": "C1000000580-LARC_ASDC",
+            "issued": "2009-03-03",
+            "keyword": [
+                "nasa"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1000000580-LARC_ASDC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-04-25",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
+            "temporal": "2006-02-01T00:00:00Z/2006-05-31T23:59:59Z",
             "theme": [
                 "INTEXB",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "INTEXB_SATELLITE"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H43B5X3R",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for Hazards and Risk Research - CHRR - Columbia University, Center for International Earth Science Information Network - CIESIN - Columbia University, and International Bank for Reconstruction and Development - The World Bank. 2005-12-31. Global Volcano Proportional Economic Loss Risk Deciles. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, Center for Hazards and Risk Research (CHRR)/Columbia University. https://doi.org/10.7927/H43B5X3R. https://doi.org/10.7927/H43B5X3R.",
-            "issued": "2005-12-31",
-            "temporal": "2000-01-01T00:00:00Z/2000-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2005-12-31",
-            "references": [
-                "https://doi.org/10.7927/H4BR8Q45",
-                "https://doi.org/10.7927/H4ZK5DMF",
-                "https://doi.org/10.7927/H4736NT2"
-            ],
-            "keyword": [
-                "human dimensions",
-                "earth science",
-                "socioeconomics",
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
-            "identifier": "C179001794-SEDAC",
-            "description": "Global Volcano Proportional Economic Loss Risk Deciles is a 2.5 minute grid of volcano hazard economic loss as proportions of Gross Domestic Product (GDP) per analytical Unit. Estimates of GDP at risk are based on regional economic loss rates derived from historical records of the Emergency Events Database (EM-DAT). Loss rates are weighted by the hazard's frequency and distribution. The methodology of Sachs et al. (2003) is followed to determine baseline estimates of GDP per grid cell. To better reflect the confidence surrounding the data and procedures, the range of proportionalities is classified into deciles, 10 class of an approximately equal number of grid cells of increasing risk. This data set is the result of collaboration among the Columbia University Center for Hazards and Risk Research (CHRR), International Bank for Reconstruction and Development/The World Bank, and Columbia University Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Center for Hazards and Risk Research - CHRR - Columbia University, Center for International Earth Science Information Network - CIESIN - Columbia University, and International Bank for Reconstruction and Development - The World Bank",
-            "title": "Global Volcano Proportional Economic Loss Risk Deciles",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/ndh-volcano-proportional-economic-loss-risk-deciles/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Global Volcano Proportional Economic Loss Risk Deciles is a 2.5 minute grid of volcano hazard economic loss as proportions of Gross Domestic Product (GDP) per analytical Unit. Estimates of GDP at risk are based on regional economic loss rates derived from historical records of the Emergency Events Database (EM-DAT). Loss rates are weighted by the hazard's frequency and distribution. The methodology of Sachs et al. (2003) is followed to determine baseline estimates of GDP per grid cell. To better reflect the confidence surrounding the data and procedures, the range of proportionalities is classified into deciles, 10 class of an approximately equal number of grid cells of increasing risk. This data set is the result of collaboration among the Columbia University Center for Hazards and Risk Research (CHRR), International Bank for Reconstruction and Development/The World Bank, and Columbia University Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH43B5X3R",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH43B5X3R",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/ndh/ndh-volcano-proportional-economic-loss-risk-deciles/volcano-proportional-economic-loss-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/ndh/ndh-volcano-proportional-economic-loss-risk-deciles/volcano-proportional-economic-loss-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-volcano-proportional-economic-loss-risk-deciles/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-volcano-proportional-economic-loss-risk-deciles/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-volcano-proportional-economic-loss-risk-deciles/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-volcano-proportional-economic-loss-risk-deciles/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-volcano-proportional-economic-loss-risk-deciles/maps/services",
-                    "description": "Web Map Service Page",
                     "@type": "dcat:Distribution",
+                    "description": "Web Map Service Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-volcano-proportional-economic-loss-risk-deciles/maps/services",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-volcano-proportional-economic-loss-risk-deciles",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-volcano-proportional-economic-loss-risk-deciles",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/ndh-volcano-proportional-economic-loss-risk-deciles/maps",
+            "identifier": "C179001794-SEDAC",
+            "issued": "2005-12-31",
+            "keyword": [
+                "human dimensions",
+                "earth science",
+                "socioeconomics",
+                "natural hazards"
+            ],
+            "landingPage": "https://doi.org/10.7927/H43B5X3R",
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
+                "https://doi.org/10.7927/H4BR8Q45",
+                "https://doi.org/10.7927/H4ZK5DMF",
+                "https://doi.org/10.7927/H4736NT2"
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
+            "title": "Global Volcano Proportional Economic Loss Risk Deciles"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0287-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-09-11T06:32:02.000 to 2014-09-11T17:07:34.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0287-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0287-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0287-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-09-11T06:32:02.000 to 2014-09-11T17:07:34.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0287 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0287 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/117/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2010-09-10",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "nasa",
-                "ames",
-                "dashlink"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DAWN MCINTOSH",
                 "hasEmail": "mailto:dawn.m.mcintosh@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_117",
             "description": "The Mariana source code has been open sourced.  Download the tar file Mariana.tgz below.  I would love feedback.\r\n\r\n \r\n\r\nMariana is an auto-classifier algorithm that efficiently optimizes hyperparameters for Support Vector Machines.\r\n\r\nMariana is an algorithm that efficiently optimizes the hyperparameters for Support Vector Machines for regression and classification.  It currently uses Simulated Annealing for optimization but can be extended to use a variety of stochastic optimization techniques including, Markov Chain Monte Carlo, Sequential Monte Carlo, and Genetic Algorithms. Mariana can be applied to the text portion of reports, determining the likely categories that each report falls into, and calculating a confidence for each classification. Mariana\u00b9s innovation is it automates the search for the optimum hyperparameters.  It does so by randomly selecting a set of hyperparameters.  Next it builds a model from the training data and tests the model's performance using the validation set.  That performance is compared to previous performances, and if the current set of hyperparameters are better than the previous one, then it records the hyperparameters.  This process is repeated until there are no noticeable improvements in performance or at a predefined stopping point.",
-            "title": "Mariana",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/algorithm/Mariana_2.tgz",
-                    "description": "Mariana Source Code. Updated 8/12/08",
                     "@type": "dcat:Distribution",
+                    "description": "Mariana Source Code. Updated 8/12/08",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/algorithm/Mariana_2.tgz",
+                    "mediaType": "application/x-gzip",
                     "title": "Mariana_2.tgz"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/algorithm/Mariana_v0.8a.zip",
-                    "description": "Mariana Source Code. Updated 01/14/10",
                     "@type": "dcat:Distribution",
+                    "description": "Mariana Source Code. Updated 01/14/10",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/algorithm/Mariana_v0.8a.zip",
+                    "mediaType": "application/zip",
                     "title": "Mariana_v0.8a.zip"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/algorithm/Mariana_v0.8a_par.tgz",
-                    "description": "Mariana Source Code. Updated 01/14/10",
                     "@type": "dcat:Distribution",
+                    "description": "Mariana Source Code. Updated 01/14/10",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/algorithm/Mariana_v0.8a_par.tgz",
+                    "mediaType": "application/x-gzip",
                     "title": "Mariana_v0.8a_par.tgz"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/algorithm/Mariana_v0.8b_par.tgz",
-                    "description": "Mariana Source Code. Updated 4/6/10",
                     "@type": "dcat:Distribution",
+                    "description": "Mariana Source Code. Updated 4/6/10",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/algorithm/Mariana_v0.8b_par.tgz",
+                    "mediaType": "application/x-gzip",
                     "title": "Mariana_v0.8b_par.tgz"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/algorithm/Mariana_v0.8c_par.zip",
-                    "description": "Mariana Source Code. Updated 6/22/2010",
                     "@type": "dcat:Distribution",
+                    "description": "Mariana Source Code. Updated 6/22/2010",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/algorithm/Mariana_v0.8c_par.zip",
+                    "mediaType": "application/zip",
                     "title": "Mariana_v0.8c_par.zip"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_117",
+            "issued": "2010-09-10",
+            "keyword": [
+                "nasa",
+                "ames",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/117/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Mariana"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-E%2FV%2FH-MASCS-2-VIRS-EDR-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Abstract ======== This data set consists of the MESSENGER MASCS VIRS uncalibrated observations, also known as EDRs. The MASCS VIRS experiment is a fixed concave grating spectrograph with a beam splitter that simultaneously disperses the spectrum onto two photodiode arrays. There are two VIRS EDR data products, one for each array, which result in coverage of the wavelength ranges of the visible (VIS) and near infrared (NIR).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-e-v-h-mascs-2-virs-edr-v1.0_jaeu-a324",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "calibration",
                 "mercury",
@@ -963398,394 +963400,374 @@
                 "venus",
                 "earth"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-E%2FV%2FH-MASCS-2-VIRS-EDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-e-v-h-mascs-2-virs-edr-v1.0_jaeu-a324",
-            "description": "Abstract ======== This data set consists of the MESSENGER MASCS VIRS uncalibrated observations, also known as EDRs. The MASCS VIRS experiment is a fixed concave grating spectrograph with a beam splitter that simultaneously disperses the spectrum onto two photodiode arrays. There are two VIRS EDR data products, one for each array, which result in coverage of the wavelength ranges of the visible (VIS) and near infrared (NIR).",
-            "title": "MESSENGER E/V/H MASCS 2 VIRS UNCALIBRATED DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MESSENGER E/V/H MASCS 2 VIRS UNCALIBRATED DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-SS-MAG-4-SUMM-CRUISE-IRC-V1.0",
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
+            "description": "This data set contains data acquired by the Galileo Magnetometer during the Interplanetary Cruise to Jupiter. The data are at varying resolution depending on the averaging constant applied by the instrument. These data have been fully processed to remove instrument response function characteristics. The data are provided in physical units (nanoTesla) and in 2 coordinate systems. This set of data files contains data in Inertial Rotor Coordinates (IRC= despun spacecraft).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-ss-mag-4-summ-cruise-irc-v1.0_jaf4-qe3z",
+            "issued": "2021-05-21",
+            "keyword": [
+                "galileo"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-SS-MAG-4-SUMM-CRUISE-IRC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-ss-mag-4-summ-cruise-irc-v1.0_jaf4-qe3z",
-            "description": "This data set contains data acquired by the Galileo Magnetometer during the Interplanetary Cruise to Jupiter. The data are at varying resolution depending on the averaging constant applied by the instrument. These data have been fully processed to remove instrument response function characteristics. The data are provided in physical units (nanoTesla) and in 2 coordinate systems. This set of data files contains data in Inertial Rotor Coordinates (IRC= despun spacecraft).",
-            "title": "GALILEO MAGNETOMETER CRUISE DATA (IRC COORDINATES)",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GALILEO MAGNETOMETER CRUISE DATA (IRC COORDINATES)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2325",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Kahiu, N., N.P. Hanan, and J.Y. Anchang. 2024. MODIS-derived Aggregate, Woody and Herbaceous Leaf Area Index for Africa, 2002-2022. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2325",
-            "issued": "2024-04-24",
-            "temporal": "2002-07-05T00:00:00Z/2022-07-29T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-28",
-            "keyword": [
-                "earth science",
-                "national geospatial data asset",
-                "ngda",
-                "vegetation",
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
-            "identifier": "C2954717391-ORNL_CLOUD",
             "description": "This dataset provides leaf area index (LAI) estimates for Sub-Saharan Africa for woody, herbaceous, and aggregate vegetation types.  The estimates were derived from Moderate Resolution Imaging Spectroradiometer (MODIS) Level 4 and the native MODIS LAI product (MCD15A2H Version 6.1), which provides LAI measurements every 8 days at 500-m pixel size. Data from the MCD15A2H product were processed further to generate three layers including: a smoothed and gap filled LAI layer referred to as aggregate leaf area index and two additional layers processed to separate woody LAI (tree and shrubs) and herbaceous LAI (grass and forbs). The data include 31 MODIS 10-degree tiles and cover 2002 to 2022. The data are provided in NetCDF format.",
-            "graphic-preview-description": "Overall mean leaf area index (LAI) for woody vegetation in sub-Saharan Africa for 2003 to 2021.",
-            "title": "MODIS-derived Aggregate, Woody and Herbaceous Leaf Area Index for Africa, 2002-2022",
-            "graphic-preview-file": "https://daac.ornl.gov/VEGETATION/guides/LAI_Africa_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2325",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2325",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/LAI_Africa/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/LAI_Africa/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/LAI_Africa.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/LAI_Africa.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2325",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2325",
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
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/LAI_Africa/comp/LAI_Africa.pdf",
-                    "description": "MODIS-derived Aggregate, Woody and Herbaceous Leaf Area Index for Africa, 2002-2022: LAI_Africa.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS-derived Aggregate, Woody and Herbaceous Leaf Area Index for Africa, 2002-2022: LAI_Africa.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/LAI_Africa/comp/LAI_Africa.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/LAI_Africa_Fig1.jpg",
-                    "description": "Overall mean leaf area index (LAI) for woody vegetation in sub-Saharan Africa for 2003 to 2021.",
                     "@type": "dcat:Distribution",
+                    "description": "Overall mean leaf area index (LAI) for woody vegetation in sub-Saharan Africa for 2003 to 2021.",
+                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/LAI_Africa_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Overall mean leaf area index (LAI) for woody vegetation in sub-Saharan Africa for 2003 to 2021.",
+            "graphic-preview-file": "https://daac.ornl.gov/VEGETATION/guides/LAI_Africa_Fig1.jpg",
+            "identifier": "C2954717391-ORNL_CLOUD",
+            "issued": "2024-04-24",
+            "keyword": [
+                "earth science",
+                "national geospatial data asset",
+                "ngda",
+                "vegetation",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2325",
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
             "spatial": "-21.28 -40.02 63.86 20.02",
+            "temporal": "2002-07-05T00:00:00Z/2022-07-29T23:59:59Z",
             "theme": [
                 "Vegetation",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS-derived Aggregate, Woody and Herbaceous Leaf Area Index for Africa, 2002-2022"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/IMPACTS/NEXRAD/DATA109",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Brodzik, Stacy .2022. KDOX NEXRAD IMPACTS [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/IMPACTS/NEXRAD/DATA109",
-            "issued": "2022-03-23",
-            "temporal": "2020-01-01T00:06:51Z/2020-03-01T00:00:37Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "radar",
-                "spectral/engineering",
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
-            "identifier": "C2020897888-GHRC_DAAC",
             "description": "The KDOX NEXRAD IMPACTS dataset consists of Next Generation Weather Radar (NEXRAD) Level II surveillance data that were collected at 31 NEXRAD sites from January 1 to March 1, 2020 during the Investigation of Microphysics and Precipitation for Atlantic Coast-Threatening Snowstorms  (IMPACTS) field campaign. IMPACTS was a three-year sequence of winter season deployments conducted to study snowstorms over the U.S Atlantic Coast. The campaign aimed to (1) Provide observations critical to understanding the mechanisms of snowband formation, organization, and evolution; (2) Examine how the microphysical characteristics and likely growth mechanisms of snow particles vary across snowbands; and (3) Improve snowfall remote sensing interpretation and modeling to significantly advance prediction capabilities. There are currently 160 Weather Surveillance Radar-1988 Doppler (WSR-88D) or NEXRAD sites throughout the United States and abroad. This Level II dataset contains meteorological and dual-polarization base data quantities including: radar reflectivity, radial velocity, spectrum width, differential reflectivity, differential phase, and cross correlation ratio. The IMPACTS NEXRAD Level II data files are available in netCDF-4 format. It should be noted that this dataset will be updated in subsequent years of the IMPACTS campaign.",
-            "title": "KDOX NEXRAD IMPACTS V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FNEXRAD%2FDATA109",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FNEXRAD%2FDATA109",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=kdoximpacts",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=kdoximpacts",
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
-                    "downloadURL": "http://www.ofcm.gov/publications/fmh/FMH11/2016FMH11PTA.pdf",
-                    "description": "Federal Meteorological Handbook No. 11 Part A: System Concepts, Responsibilities, and Procedures",
                     "@type": "dcat:Distribution",
+                    "description": "Federal Meteorological Handbook No. 11 Part A: System Concepts, Responsibilities, and Procedures",
+                    "downloadURL": "http://www.ofcm.gov/publications/fmh/FMH11/2016FMH11PTA.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.ofcm.gov/publications/fmh/FMH11/fmh11partC.pdf",
-                    "description": "Federal Meteorological Handbook No. 11 Part C: WSR-88D Products and Algorithms",
                     "@type": "dcat:Distribution",
+                    "description": "Federal Meteorological Handbook No. 11 Part C: WSR-88D Products and Algorithms",
+                    "downloadURL": "http://www.ofcm.gov/publications/fmh/FMH11/fmh11partC.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/NEXRAD/KDOX/doc/nexrad_datasets.pdf",
-                    "description": "NEXRAD IMPACTS User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "NEXRAD IMPACTS User Guide",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/NEXRAD/KDOX/doc/nexrad_datasets.pdf",
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
+            "identifier": "C2020897888-GHRC_DAAC",
+            "issued": "2022-03-23",
+            "keyword": [
+                "radar",
+                "spectral/engineering",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/IMPACTS/NEXRAD/DATA109",
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
             "spatial": "-80.7442 34.6956 -70.136 42.9556",
+            "temporal": "2020-01-01T00:06:51Z/2020-03-01T00:00:37Z",
             "theme": [
                 "IMPACTS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "KDOX NEXRAD IMPACTS V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ODY-M-THM-5-VISALB-V2.0",
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
-                "2001 mars odyssey"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The THEMIS VIS-RDR data set contains the spatially registered, visible albedo images derived from the projected radiance (VIS-GEO) products. Each image header includes basic parameters describing the observation and image specific details of the processing.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ody-m-thm-5-visalb-v2.0_jajj-n2y2",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "2001 mars odyssey"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ODY-M-THM-5-VISALB-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ody-m-thm-5-visalb-v2.0_jajj-n2y2",
-            "description": "The THEMIS VIS-RDR data set contains the spatially registered, visible albedo images derived from the projected radiance (VIS-GEO) products. Each image header includes basic parameters describing the observation and image specific details of the processing.",
-            "title": "ODYSSEY THEMIS VIS ALB V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ODYSSEY THEMIS VIS ALB V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/jam2-g5sm",
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
-            "identifier": "NASA-0000038__5",
+            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
             "description": "Planetary nomenclature, like terrestrial nomenclature, is used to uniquely identify a feature on the surface of a planet or satellite so that the feature can be easily located, described, and discussed. This gazetteer contains detailed information about all names of topographic and albedo features on planets and satellites (and some planetary ring and ring-gap systems) that the International Astronomical Union (IAU) has named and approved from its founding in 1919 through the present time.",
-            "title": "Gazetteer of Planetary Nomenclature",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -963793,772 +963775,768 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
-            "accrualPeriodicity": "irregular"
+            "identifier": "NASA-0000038__5",
+            "issued": "2018-06-25",
+            "keyword": [
+                "wise",
+                "geography",
+                "nen",
+                "space science"
+            ],
+            "landingPage": "https://data.nasa.gov/d/jam2-g5sm",
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
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/775/",
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
-            "identifier": "DASHLINK_775",
             "description": "Power electronics are widely used in critical roles in modern day aircrafts and hence their health management is of great interest. An important part of prognostics and health management of these devices is understand- ing the effect of high-stress events such as lightning and how they affect their aging. In this paper we present our study and analysis of lightning injection experiments with power MOSFETs in their ON state. We show the different kind of damages that can be caused by such events and analyze their effects on device performance parameters. In addition, we present a simple yet effec- tive modeling technique that can model the degradation in these devices. Such models will play a valuable role in understanding the behavior of these damaged devices when operated under normal conditions later and sub- sequently in prognosis of their remaining useful life.We present our results on the performance of this modeling and the scope within which they can be utilized for ac- curate estimation of device damage.",
-            "title": "Towards Modeling the Effects of Lightning Injection on Power MOSFETs",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2010_PHM_Lightning.pdf",
-                    "description": "2010_PHM_Lightning.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "2010_PHM_Lightning.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2010_PHM_Lightning.pdf",
+                    "mediaType": "application/pdf",
                     "title": "2010_PHM_Lightning.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_775",
+            "issued": "2013-06-19",
+            "keyword": [
+                "nasa",
+                "dashlink",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/775/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Towards Modeling the Effects of Lightning Injection on Power MOSFETs"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3346-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-07-10T16:41:35.000 to 2012-07-15T12:01:59.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3346-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars express",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3346-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3346-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-07-10T16:41:35.000 to 2012-07-15T12:01:59.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3346 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3346 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-MAG-4-RDR-L1COORDS-1.92SEC-V1.1",
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
+            "description": "This data set includes Voyager 2 Saturn encounter magnetometer data from the Low Field Magnetometer (LFM) resampled at a 1.92 second sample rate from the 60 msec instrument sampling rate. Data coverage begins in the solar wind and continues until at least the first magnetopause crossing. The data are given in Kronographic (L1) coordinates. The data set is composed of the following columns: 1) time - UT of the sample in the format yyyy-mm-ddThh:mm:ss.sssZ, 2) spacecraft clock values (m65536:mod60:fds_line), 3) mag_id - magnetometer id (1 = LFM, 2 = HFM), 4) Br - radial (Saturn to spacecraft) B-field component, 5) Btheta - North/South (L1) B-field component (positive southward), 6) Bphi - azimuthal (L1) B-field component (positive eastward), 7) Bmag - magnitude of the averaged magnetic field components, 8) avg_Bmag - average of the magnetic field magnitudes, 9) delta - magnetic latitude = arcsin(Btheta/Bmag), 10) lambda - longitude = 180. - atan(Bphi/-Br), 11-13) rms_br, rms_bt, and rms_bn - rms vectors, 14) npts - number of points in average.  All magnetic field observations are measured in nanoTesla. All of the magnetic field data are calibrated (see the instrument calibration description for more details).  These data are provided in a Saturn centered spherical system (L1), based on the Saturn Longitude System (Voyager Measurements of the Rotation Period of Saturn's Magnetic Field, Desch and Kaiser, JGR, 8, 253, 1981).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-mag-4-rdr-l1coords-1.92sec-v1.1_jaqf-ners",
+            "issued": "2021-05-21",
+            "keyword": [
+                "voyager",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-MAG-4-RDR-L1COORDS-1.92SEC-V1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-mag-4-rdr-l1coords-1.92sec-v1.1_jaqf-ners",
-            "description": "This data set includes Voyager 2 Saturn encounter magnetometer data from the Low Field Magnetometer (LFM) resampled at a 1.92 second sample rate from the 60 msec instrument sampling rate. Data coverage begins in the solar wind and continues until at least the first magnetopause crossing. The data are given in Kronographic (L1) coordinates. The data set is composed of the following columns: 1) time - UT of the sample in the format yyyy-mm-ddThh:mm:ss.sssZ, 2) spacecraft clock values (m65536:mod60:fds_line), 3) mag_id - magnetometer id (1 = LFM, 2 = HFM), 4) Br - radial (Saturn to spacecraft) B-field component, 5) Btheta - North/South (L1) B-field component (positive southward), 6) Bphi - azimuthal (L1) B-field component (positive eastward), 7) Bmag - magnitude of the averaged magnetic field components, 8) avg_Bmag - average of the magnetic field magnitudes, 9) delta - magnetic latitude = arcsin(Btheta/Bmag), 10) lambda - longitude = 180. - atan(Bphi/-Br), 11-13) rms_br, rms_bt, and rms_bn - rms vectors, 14) npts - number of points in average.  All magnetic field observations are measured in nanoTesla. All of the magnetic field data are calibrated (see the instrument calibration description for more details).  These data are provided in a Saturn centered spherical system (L1), based on the Saturn Longitude System (Voyager Measurements of the Rotation Period of Saturn's Magnetic Field, Desch and Kaiser, JGR, 8, 253, 1981).",
-            "title": "VG2 SAT MAG RESAMPLED KRONOGRAPHIC (L1)\n                                      COORDS 1.92SEC V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG2 SAT MAG RESAMPLED KRONOGRAPHIC (L1)\n                                      COORDS 1.92SEC V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/IMPACTS/MRR2/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Minder, Justin R., E.  Potter and W. Massey Bartolini.2022. UAlbany Micro Rain Radar 2 (MRR-2) IMPACTS [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/IMPACTS/MRR2/DATA101",
-            "issued": "2022-08-02",
-            "temporal": "2020-01-30T00:01:00Z/2022-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "keyword": [
-                "spectral/engineering",
-                "atmospheric water vapor",
-                "atmosphere",
-                "earth science",
-                "precipitation",
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
-            "identifier": "C2382050573-GHRC_DAAC",
             "description": "The UAlbany Micro Rain Radar 2 (MRR-2) IMPACTS dataset consists of reflectivity, Doppler velocity, signal-to-noise ratio, spectral width, droplet size, Liquid Water Content, melting layer, drop size distribution, rain attenuation, rain rate, and radial velocity data collected during the Investigation of Microphysics and Precipitation for Atlantic Coast-Threatening Snowstorms (IMPACTS) field campaign. IMPACTS was a three-year sequence of winter season deployments conducted to study snowstorms over the U.S Atlantic Coast (2020-2023). The campaign aimed to (1) Provide observations critical to understanding the mechanisms of snowband formation, organization, and evolution; (2) Examine how the microphysical characteristics and likely growth mechanisms of snow particles vary across snowbands; and (3) Improve snowfall remote sensing interpretation and modeling to significantly advance prediction capabilities. The MRR-2 instrument was used to collect data for this dataset. The dataset files are available from January 30, 2020 through March 1, 2022 in netCDF-3 and netCDF-4 format.",
-            "title": "UAlbany Micro Rain Radar 2 (MRR-2) IMPACTS V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FMRR2%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FMRR2%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/portal/ghrc/search?q=ualbmrr2impacts&ghrccloud%2Fdata%2F=",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/portal/ghrc/search?q=ualbmrr2impacts&ghrccloud%2Fdata%2F=",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://metek.de/wpcontent/uploads/2014/05/Datasheet_MRR-2.pdf",
-                    "description": "Micro Rain Radar MRR2 Data Sheet",
                     "@type": "dcat:Distribution",
+                    "description": "Micro Rain Radar MRR2 Data Sheet",
+                    "downloadURL": "https://metek.de/wpcontent/uploads/2014/05/Datasheet_MRR-2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://metek.de/product/mrr-2/",
-                    "description": "Micro Rain Radar MRR | MRR2 Information",
                     "@type": "dcat:Distribution",
+                    "description": "Micro Rain Radar MRR | MRR2 Information",
+                    "downloadURL": "https://metek.de/product/mrr-2/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www.stormt.iag.usp.br/pub/MRR/Metek/Manuals/MRR-Manual_20120301.pdf",
-                    "description": "Micro Rain Radar MRR2 User Manual",
                     "@type": "dcat:Distribution",
+                    "description": "Micro Rain Radar MRR2 User Manual",
+                    "downloadURL": "https://www.stormt.iag.usp.br/pub/MRR/Metek/Manuals/MRR-Manual_20120301.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www.stormt.iag.usp.br/pub/MRR/Metek/Manuals/MRR-physical-basics_20120313.pdf",
-                    "description": "Micro Rain Radar MRR Physical Basics",
                     "@type": "dcat:Distribution",
+                    "description": "Micro Rain Radar MRR Physical Basics",
+                    "downloadURL": "https://www.stormt.iag.usp.br/pub/MRR/Metek/Manuals/MRR-physical-basics_20120313.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/impacts/content/IMPACTS",
-                    "description": "NASA IMPACTS ESPO Information",
                     "@type": "dcat:Distribution",
+                    "description": "NASA IMPACTS ESPO Information",
+                    "downloadURL": "https://espo.nasa.gov/impacts/content/IMPACTS",
+                    "mediaType": "text/html",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/UALB_MRR2/doc/ualbmrr2impacts_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/UALB_MRR2/doc/ualbmrr2impacts_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5194/amt-5-2661-2012",
-                    "description": "Improved Micro Rain Radar snow measurements using Doppler spectra post-processing",
                     "@type": "dcat:Distribution",
+                    "description": "Improved Micro Rain Radar snow measurements using Doppler spectra post-processing",
+                    "downloadURL": "https://doi.org/10.5194/amt-5-2661-2012",
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
-                    "downloadURL": "https://github.com/maahn/IMProToo",
-                    "description": "IMProToo Improved Mrr Processing Tool",
                     "@type": "dcat:Distribution",
+                    "description": "IMProToo Improved Mrr Processing Tool",
+                    "downloadURL": "https://github.com/maahn/IMProToo",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/impacts",
-                    "description": "IMPACTS Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "IMPACTS Project Home Page",
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
+            "identifier": "C2382050573-GHRC_DAAC",
+            "issued": "2022-08-02",
+            "keyword": [
+                "spectral/engineering",
+                "atmospheric water vapor",
+                "atmosphere",
+                "earth science",
+                "precipitation",
+                "radar"
+            ],
+            "landingPage": "https://doi.org/10.5067/IMPACTS/MRR2/DATA101",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/MSFC/GHRC"
+            },
             "spatial": "-73.8324 42.6804 -73.8139 42.6863",
+            "temporal": "2020-01-30T00:01:00Z/2022-03-01T00:00:00Z",
             "theme": [
                 "IMPACTS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "UAlbany Micro Rain Radar 2 (MRR-2) IMPACTS V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-RSS-1-EDR-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The Mars Exploration Rover 2 (MER2) Radio Science (RS) data archive contains raw radio tracking data collected during the surface lifetime of the MER2 Rover. The data contain potentially valuable information on the rotation dynamics of Mars, extending the previous data available from the Viking and Mars Pathfinder landers.  For more information on the earlier investigations see [FOLKNERETAL1997A].",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-rss-1-edr-v1.0_jasu-ijdq",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "mars",
                 "mars exploration rover"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-RSS-1-EDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-rss-1-edr-v1.0_jasu-ijdq",
-            "description": "The Mars Exploration Rover 2 (MER2) Radio Science (RS) data archive contains raw radio tracking data collected during the surface lifetime of the MER2 Rover. The data contain potentially valuable information on the rotation dynamics of Mars, extending the previous data available from the Viking and Mars Pathfinder landers.  For more information on the earlier investigations see [FOLKNERETAL1997A].",
-            "title": "MARS EXPLORATION ROVER 2\n                                     RADIO SCIENCE SUBSYSTEM EDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPLORATION ROVER 2\n                                     RADIO SCIENCE SUBSYSTEM EDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/IKZNCN3J05SP",
             "citation": "Miyazaki, Kazuyuki. 2024-01-08. TRPSCRQ2H2D. Version 1. TROPESS Chemical Reanalysis Surface Specific Humidity 2-Hourly 2-dimensional Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/IKZNCN3J05SP. https://disc.gsfc.nasa.gov/datacollection/TRPSCRQ2H2D_1.html. Digital Science Data.",
-            "issued": "2023-01-09",
-            "temporal": "2005-01-01T00:00:00Z/2021-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-02-17",
-            "references": [
-                "https://doi.org/10.5194/essd-12-2223-2020"
-            ],
-            "keyword": [
-                "atmospheric water vapor",
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
-            "identifier": "C2816184435-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS Chemical Reanalysis Surface Specific Humidity 2-Hourly 2-dimensional Product contains surface specific humidity values, a meteorological field. The data are part of the Tropospheric Chemical Reanalysis v2 (TCR-2) for the period 2005-2021. TCR-2 uses JPL's Multi-mOdel Multi-cOnstituent Chemical (MOMO-Chem) data assimilation framework that simultaneously optimizes both concentrations and emissions of multiple species from multiple satellite sensors.\n\nThe data files are written in the netCDF version 4 file format, and each file contains a year of data at 2-hourly resolution, and a spatial resolution of 1.125 x 1.125 degrees. The principal investigator for the TCR-2 data is Miyazaki, Kazuyuki.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSCRQ2H2D",
-            "creator": "Miyazaki, Kazuyuki",
-            "graphic-preview-description": "TCR-2 01 April 2005.",
-            "title": "TROPESS Chemical Reanalysis Surface Specific Humidity 2-Hourly 2-dimensional Product V1 (TRPSCRQ2H2D) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRQ2H2D_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIKZNCN3J05SP",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIKZNCN3J05SP",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRQ2H2D_Sample.png",
-                    "description": "TCR-2 01 April 2005.",
                     "@type": "dcat:Distribution",
+                    "description": "TCR-2 01 April 2005.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRQ2H2D_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSCRQ2H2D_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSCRQ2H2D_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_2HR_METFIELDS/TRPSCRQ2H2D.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_2HR_METFIELDS/TRPSCRQ2H2D.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSCRQ2H2D_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSCRQ2H2D_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TCR2_2HR_METFIELDS/TRPSCRQ2H2D.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TCR2_2HR_METFIELDS/TRPSCRQ2H2D.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_2HR_METFIELDS/TRPSCRQ2H2D.1/doc/TROPESS_ChemReanalysis_Forward_Stream_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_2HR_METFIELDS/TRPSCRQ2H2D.1/doc/TROPESS_ChemReanalysis_Forward_Stream_README.pdf",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRQ2H2D_Sample.png",
+            "identifier": "C2816184435-GES_DISC",
+            "issued": "2023-01-09",
+            "keyword": [
+                "atmospheric water vapor",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/IKZNCN3J05SP",
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
+            "series-name": "TRPSCRQ2H2D",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2005-01-01T00:00:00Z/2021-12-31T23:59:59.999Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS Chemical Reanalysis Surface Specific Humidity 2-Hourly 2-dimensional Product V1 (TRPSCRQ2H2D) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-ESC3-67PCHURYUMOV-M19-V1.0",
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
+            "description": "This data set contains raw EDR images acquired by the OSIRIS Narrow Angle\nCamera during the escort phase of the Rosetta mission at the comet 67P,\ncovering the period from 2015-07-28 to 2015-08-25.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-esc3-67pchuryumov-m19-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-ESC3-67PCHURYUMOV-M19-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-esc3-67pchuryumov-m19-v1.0",
-            "description": "This data set contains raw EDR images acquired by the OSIRIS Narrow Angle\nCamera during the escort phase of the Rosetta mission at the comet 67P,\ncovering the period from 2015-07-28 to 2015-08-25.",
-            "title": "ROSETTA-ORBITER COMET ESCORT OSINAC 2 EDR MTP 019 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMET ESCORT OSINAC 2 EDR MTP 019 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2CH4N_L2.007",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2017-10-17. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AURA/TES/TL2CH4N_L2.007. https://asdc.larc.nasa.gov/project/TES.",
-            "issued": "2015-08-27",
-            "temporal": "2004-08-22T00:00:00Z/2018-01-22T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "clouds",
-                "atmospheric temperature",
-                "atmospheric chemistry",
-                "air quality"
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
-            "identifier": "C1331182627-LARC",
             "description": "TL2CH4N_7 is the Tropospheric Emission Spectrometer (TES)/Aura Level 2 Methane Nadir Version 7 data product. TES was an instrument aboard NASA's Aura satellite and was launched from California on July 15, 2004. Data collection for TES is complete. TES Level 2 data contain retrieved species (or temperature) profiles at the observation targets and the estimated errors. The geolocation, quality, and other data (e.g., surface characteristics for nadir observations) were also provided. L2 modeled spectra were evaluated using radiative transfer modeling algorithms. The process, referred to as retrieval, compared observed spectra to the modeled spectra and iteratively updated the atmospheric parameters. L2 standard product files included information for one molecular species (or temperature) for an entire global survey or special observation run. A global survey consisted of a maximum of 16 consecutive orbits.\r\rNadir observations, which point directly to the surface of the Earth, are different from limb observations, which are pointed at various off-nadir angles into the atmosphere. Nadir and limb observations were added to separate L2 files, and a single ancillary file was composed of data that are common to both nadir and limb files. A Nadir sequence within the TES Global Survey was a fixed number of observations within an orbit for a Global Survey. Prior to April 24, 2005, it consisted of two low resolution scans over the same ground locations. After April 24, 2005, Global Survey data consisted of three low resolution scans. The Nadir standard product consists of four files, where each file is composed of the Global Survey Nadir observations from one of four focal planes for a single orbit, i.e. 72 orbit sequences. The Global Survey Nadir observations only used a single set of filter mix. \r\rA Global Survey consisted of observations along 16 consecutive orbits at the start of a two day cycle, over which 3,200 retrievals were performed. Each observation was the input for retrievals of species Volume Mixing Ratios (VMRs), temperature profiles, surface temperature, and other data parameters with associated pressure levels, precision, total error, vertical resolution, total column density, and other diagnostic quantities. Each TES Level 2 standard product reported information in a swath format conforming to the HDF-EOS Aura File Format Guidelines. Each Swath object was bounded by the number of observations in a global survey and a predefined set of pressure levels representing slices through the atmosphere. Each standard product could have had a variable number of observations depending upon the Global Survey configuration and whether averaging was employed. Also, missing or bad retrievals were not reported. Further, observations were occasionally scheduled on non-global survey days. In general they were measurements made for validation purposes or with highly focused science objectives. Those non-global survey measurements were referred to as \u201cspecial observations\u201d\r\rThe organization of data within the Swath object was based on a superset of the Upper Atmosphere Research Satellite (UARS) pressure levels used to report concentrations of trace atmospheric gases. The reporting grid was the same pressure grid used for modeling. There were 67 reporting levels from 1211.53 hPa, which allowed for very high surface pressure conditions, to 0.1 hPa, about 65 km. In addition, the products reported values directly at the surface when possible or at the observed cloud top level. Thus in the Standard Product files, each observation could potentially contain estimates for the concentration of a particular molecule at 67 different pressure levels within the atmosphere. However, for most retrieved profiles, the highest pressure levels were not observed due to a surface at lower pressure or cloud obscuration. For pressure levels corresponding to altitudes below the cloud top or surface, where measurements were not possible, a fill value was applied.\r\rTo",
-            "title": "TES/Aura L2 Methane Nadir V007",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2CH4N_L2.007",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2CH4N_L2.007",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1331182627-LARC",
-                    "description": "Earthdata Search for TL2CH4N_7 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TL2CH4N_7 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1331182627-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2CH4N_L2.007",
-                    "description": "DOI data set landing page for TL2CH4N_7",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TL2CH4N_7",
+                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2CH4N_L2.007",
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
-                    "mediaType": "application/x-tar",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/read_software/TES_L2_ReadSoftware.tar",
-                    "description": "TES Level 2 Read Software Package - Direct File Download (.tar)",
                     "@type": "dcat:Distribution",
+                    "description": "TES Level 2 Read Software Package - Direct File Download (.tar)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/read_software/TES_L2_ReadSoftware.tar",
+                    "mediaType": "application/x-tar",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/TES_Validation_Report_v7_Final.pdf",
-                    "description": "Earth Observing System (EOS) Tropospheric Emission Spectrometer (TES) Data Validation Report (Version F08_11 data) - Version 7.0",
                     "@type": "dcat:Distribution",
+                    "description": "Earth Observing System (EOS) Tropospheric Emission Spectrometer (TES) Data Validation Report (Version F08_11 data) - Version 7.0",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/TES_Validation_Report_v7_Final.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/README_L2_ReadSoftware.txt",
-                    "description": "Basic IDL Tools for extraction information from TES L2 HDF Product files",
                     "@type": "dcat:Distribution",
+                    "description": "Basic IDL Tools for extraction information from TES L2 HDF Product files",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/README_L2_ReadSoftware.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/public/cgi-bin/DUE/tes_L2Limb.cgi",
-                    "description": "Report of TES Level 2 Limb Products Available from the ASDC",
                     "@type": "dcat:Distribution",
+                    "description": "Report of TES Level 2 Limb Products Available from the ASDC",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/public/cgi-bin/DUE/tes_L2Limb.cgi",
+                    "mediaType": "text/html",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/TESDataUsersGuideV7_0_Sep_27_2018_FV-2.pdf",
-                    "description": "Earth Observing System (EOS) Tropospheric Emission Spectrometer (TES) Level 2 (L2) Data User\u2019s Guide (Up to & including Version 7 data) - Version 7.0",
                     "@type": "dcat:Distribution",
+                    "description": "Earth Observing System (EOS) Tropospheric Emission Spectrometer (TES) Level 2 (L2) Data User\u2019s Guide (Up to & including Version 7 data) - Version 7.0",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/TESDataUsersGuideV7_0_Sep_27_2018_FV-2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/level_2_std.pdf",
-                    "description": "TES Level 2 Versioning - Level 2 Standard and Special Observation Products",
                     "@type": "dcat:Distribution",
+                    "description": "TES Level 2 Versioning - Level 2 Standard and Special Observation Products",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/level_2_std.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's processing history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://aura.gsfc.nasa.gov/",
-                    "description": "AURA Instrument Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "AURA Instrument Home Page",
+                    "downloadURL": "https://aura.gsfc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gs614-avdc1-pz.gsfc.nasa.gov/Overview/",
-                    "description": "EOS Aura Science Team Meeting AGENDA, August 27 - August 29, 2019 Pasadena, CA, USA",
                     "@type": "dcat:Distribution",
+                    "description": "EOS Aura Science Team Meeting AGENDA, August 27 - August 29, 2019 Pasadena, CA, USA",
+                    "downloadURL": "https://gs614-avdc1-pz.gsfc.nasa.gov/Overview/",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1251/NASA_SOP_2006_On_the_trail_of_global_pollution_drift.pdf",
-                    "description": "Earth Observing System Data and Information System (EOSDIS) Article: On the trail of global pollution drift",
                     "@type": "dcat:Distribution",
+                    "description": "Earth Observing System Data and Information System (EOSDIS) Article: On the trail of global pollution drift",
+                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1251/NASA_SOP_2006_On_the_trail_of_global_pollution_drift.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/ASDC_TES_Overview_2015.pdf",
-                    "description": "Overview of TES Data at the ASDC - 2015",
                     "@type": "dcat:Distribution",
+                    "description": "Overview of TES Data at the ASDC - 2015",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/ASDC_TES_Overview_2015.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tes.jpl.nasa.gov/data/processing-calendar/",
-                    "description": "TES Data Processing Calendar",
                     "@type": "dcat:Distribution",
+                    "description": "TES Data Processing Calendar",
+                    "downloadURL": "https://tes.jpl.nasa.gov/data/processing-calendar/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's processing history"
                 },
                 {
-                    "mediaType": "application/vnd.ms-powerpoint",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/TES_STM_2013_Data_User_Session-2.ppt",
-                    "description": "2013 TES Data User Session Presentation - Direct File Download (.ppt)",
                     "@type": "dcat:Distribution",
+                    "description": "2013 TES Data User Session Presentation - Direct File Download (.ppt)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/TES_STM_2013_Data_User_Session-2.ppt",
+                    "mediaType": "application/vnd.ms-powerpoint",
                     "title": "View the primary investigator's documentation for this dataset"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2CH4N.007/",
-                    "description": "ASDC Direct Data Download for TL2CH4N.007",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for TL2CH4N.007",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2CH4N.007/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2CH4N.007/contents.html",
-                    "description": "OPeNDAP data access for TL2CH4N.007",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for TL2CH4N.007",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2CH4N.007/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
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
-                    "downloadURL": "https://portal.hdfgroup.org/display/support",
-                    "description": "HDF Support Portal",
                     "@type": "dcat:Distribution",
+                    "description": "HDF Support Portal",
+                    "downloadURL": "https://portal.hdfgroup.org/display/support",
+                    "mediaType": "text/html",
                     "title": "Access this dataset's users feedback page"
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
+            "identifier": "C1331182627-LARC",
+            "issued": "2015-08-27",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "clouds",
+                "atmospheric temperature",
+                "atmospheric chemistry",
+                "air quality"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2CH4N_L2.007",
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
+            "title": "TES/Aura L2 Methane Nadir V007"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MEASURES/AER/DATA203",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Omar Torres et al.. 2018-10-10. OMIAuraAER. Version 01. OMI/Aura Near UV Aerosol Index, Optical Depth and Single Scattering Albedo 1-Orbit L2 13x24km. NASA Goddard Space Flight Center. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/MEASURES/AER/DATA203. https://disc.gsfc.nasa.gov/datacollection/OMIAuraAER_1.html. Digital Science Data.",
-            "issued": "2018-01-25",
-            "temporal": "2004-10-01T00:03:05Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-09-06",
-            "keyword": [
-                "earth science",
-                "aerosols",
-                "atmosphere"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "OMAR TORRES, PH. D",
                 "hasEmail": "mailto:omar.o.torres@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1460503190-GES_DISC",
-            "description": "As part of the NASA's Making Earth System Data Records for Use in Research Environments (MEaSUREs) program, this projects describes a multi-decadal Fundamental Climate Data Record (FCDR) of calibrated radiances as well as an Earth System Data Record (ESDR) of aerosol properties over the continents derived from a 32-year record of satellite near-UV observations by three sensors.  \n\nThe OMI/Aura Near UV (version 1) Aerosol Index, Optical Depth and Single Scattering Albedo data product consists of aerosol absorption optical depth, aerosol optical depth, aerosol single scattering albedo, cloud fraction, cloud optical depth, refractive index, radiance, reflectivity and residue at approximately 13x24km. This product also contains ancillary data for ocean corrected surface albedo and terrain pressure.\n\nThese Level-2 data are stored in the Hierarchical Data Format 5 (HDF5) and are available from the Goddard Earth Sciences (GES) Data and Information Services Center (DISC).",
-            "release-place": "NASA Goddard Space Flight Center",
-            "series-name": "OMIAuraAER",
             "creator": "Omar Torres et al.",
-            "title": "OMI/Aura Near UV Aerosol Index, Optical Depth and Single Scattering Albedo 1-Orbit L2 13x24km",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMIAuraAER_001.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "As part of the NASA's Making Earth System Data Records for Use in Research Environments (MEaSUREs) program, this projects describes a multi-decadal Fundamental Climate Data Record (FCDR) of calibrated radiances as well as an Earth System Data Record (ESDR) of aerosol properties over the continents derived from a 32-year record of satellite near-UV observations by three sensors.  \n\nThe OMI/Aura Near UV (version 1) Aerosol Index, Optical Depth and Single Scattering Albedo data product consists of aerosol absorption optical depth, aerosol optical depth, aerosol single scattering albedo, cloud fraction, cloud optical depth, refractive index, radiance, reflectivity and residue at approximately 13x24km. This product also contains ancillary data for ocean corrected surface albedo and terrain pressure.\n\nThese Level-2 data are stored in the Hierarchical Data Format 5 (HDF5) and are available from the Goddard Earth Sciences (GES) Data and Information Services Center (DISC).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FAER%2FDATA203",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FAER%2FDATA203",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -964568,68 +964546,102 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMIAuraAER_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMIAuraAER_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/AER/OMIAuraAER.1/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/AER/OMIAuraAER.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/AER/OMIAuraAER.1/doc/README.MEaSUREs_Aerosols.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/AER/OMIAuraAER.1/doc/README.MEaSUREs_Aerosols.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthdata.nasa.gov/community/community-data-system-programs/measures-projects",
-                    "description": "MEaSUREs Project Homepage",
                     "@type": "dcat:Distribution",
+                    "description": "MEaSUREs Project Homepage",
+                    "downloadURL": "https://earthdata.nasa.gov/community/community-data-system-programs/measures-projects",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMIAuraAER_1",
-                    "description": "Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMIAuraAER_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/AER/OMIAuraAER.1",
-                    "description": "OPeNDAP Service",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP Service",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/AER/OMIAuraAER.1",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMIAuraAER_001.png",
+            "identifier": "C1460503190-GES_DISC",
+            "issued": "2018-01-25",
+            "keyword": [
+                "earth science",
+                "aerosols",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/AER/DATA203",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-09-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "NASA Goddard Space Flight Center",
+            "series-name": "OMIAuraAER",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2004-10-01T00:03:05Z/2022-01-17T00:00:00Z",
             "theme": [
                 "MEaSUREs",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OMI/Aura Near UV Aerosol Index, Optical Depth and Single Scattering Albedo 1-Orbit L2 13x24km"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1243133445-ASF.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, ASF.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "undefined",
+                "hasEmail": "mailto:uso@asf.alaska.edu"
+            },
+            "description": "SMAP Level 1B Sigma Naught Low Res Product Version 3",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Vertex, the ASF search and download interface",
+                    "downloadURL": "https://vertex.daac.asf.alaska.edu/",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                }
+            ],
+            "identifier": "C1243133445-ASF",
             "issued": "2015-07-31",
-            "temporal": "2015-02-12T16:02:58Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-05-07",
             "keyword": [
                 "platform characteristics",
                 "earth remote sensing instruments",
@@ -964642,80 +964654,46 @@
                 "earth science",
                 "imaging radars"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:uso@asf.alaska.edu"
-            },
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1243133445-ASF.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2016-05-07",
+            "programCode": [
+                "026:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "ASF"
             },
-            "identifier": "C1243133445-ASF",
-            "description": "SMAP Level 1B Sigma Naught Low Res Product Version 3",
-            "title": "SMAP_L1B_SIGMA_NAUGHT_LOW_RES_V003",
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
+            "temporal": "2015-02-12T16:02:58Z/2022-01-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMAP_L1B_SIGMA_NAUGHT_LOW_RES_V003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TCTE/TIM/DATA307",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Kopp, G.. 2020-03-10. TCTE3TSI6. Version 004. TCTE Level 3 Total Solar Irradiance 6-Hour Means V004. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/TCTE/TIM/DATA307. https://disc.gsfc.nasa.gov/datacollection/TCTE3TSI6_004.html. Digital Science Data.",
-            "issued": "2020-03-06",
-            "temporal": "2013-12-13T00:00:00Z/2019-05-15T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-03-06",
-            "keyword": [
-                "solar activity",
-                "earth science",
-                "sun-earth interactions"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "GREG KOPP",
                 "hasEmail": "mailto:Greg.Kopp@lasp.colorado.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1704861146-GES_DISC",
-            "description": "TCTE3TSI6 Version 004 is the final version of this data product, and supersedes all previous versions.\n\nThe Total Solar Irradiance (TSI) Calibration Transfer Experiment (TCTE) data set TCTE3TSI6 contains 6-hour averaged total solar irradiance (a.k.a solar constant) data collected by the Total Irradiance Monitor (TIM) instrument covering the full wavelength spectrum. The data are normalized to one astronomical unit (1 AU).\n\nThe TCTE/TIM instrument measures the Total Solar Irradiance (TSI), monitoring changes in incident sunlight to the Earth's atmosphere using an ambient temperature active cavity radiometer to a designed absolute accuracy of 350 parts per million (ppm, 1 ppm=0.0001% at 1-sigma), and a precision and long-term relative accuracy of 10 ppm per year. Due to the small size of these data and to maximize ease of use to end-users, each delivered TSI product contains science results for the entire mission in an ASCII column formatted file.\n\nEarly in the mission, between Dec 2013 and May 2014, TCTE acquired daily measurements to establish good overlap with the SORCE TIM. From May 2014 to Dec 2014, the TCTE measurements were reduced to weekly, which greatly subsample the true solar variability, and thus have little value for solar research. Beginning in Jan 2015, daily obervations were resumed. The mission ended June 30, 2019.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TCTE3TSI6",
             "creator": "Kopp, G.",
-            "title": "TCTE Level 3 Total Solar Irradiance 6-Hour Means V004 (TCTE3TSI6) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TCTE3TSI6_004.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "TCTE3TSI6 Version 004 is the final version of this data product, and supersedes all previous versions.\n\nThe Total Solar Irradiance (TSI) Calibration Transfer Experiment (TCTE) data set TCTE3TSI6 contains 6-hour averaged total solar irradiance (a.k.a solar constant) data collected by the Total Irradiance Monitor (TIM) instrument covering the full wavelength spectrum. The data are normalized to one astronomical unit (1 AU).\n\nThe TCTE/TIM instrument measures the Total Solar Irradiance (TSI), monitoring changes in incident sunlight to the Earth's atmosphere using an ambient temperature active cavity radiometer to a designed absolute accuracy of 350 parts per million (ppm, 1 ppm=0.0001% at 1-sigma), and a precision and long-term relative accuracy of 10 ppm per year. Due to the small size of these data and to maximize ease of use to end-users, each delivered TSI product contains science results for the entire mission in an ASCII column formatted file.\n\nEarly in the mission, between Dec 2013 and May 2014, TCTE acquired daily measurements to establish good overlap with the SORCE TIM. From May 2014 to Dec 2014, the TCTE measurements were reduced to weekly, which greatly subsample the true solar variability, and thus have little value for solar research. Beginning in Jan 2015, daily obervations were resumed. The mission ended June 30, 2019.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTCTE%2FTIM%2FDATA307",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTCTE%2FTIM%2FDATA307",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -964725,1158 +964703,1157 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/TCTE_Level3/TCTE3TSI6.004/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/TCTE_Level3/TCTE3TSI6.004/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TCTE3TSI6_004",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TCTE3TSI6_004",
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
-                    "downloadURL": "http://lasp.colorado.edu/home/tcte/",
-                    "description": "TCTE Project Home Page.",
                     "@type": "dcat:Distribution",
+                    "description": "TCTE Project Home Page.",
+                    "downloadURL": "http://lasp.colorado.edu/home/tcte/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://lasp.colorado.edu/home/tcte/data/tcte-tim-data-products-release-notes/",
-                    "description": "TIM Release Notes",
                     "@type": "dcat:Distribution",
+                    "description": "TIM Release Notes",
+                    "downloadURL": "http://lasp.colorado.edu/home/tcte/data/tcte-tim-data-products-release-notes/",
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
-                    "downloadURL": "http://lasp.colorado.edu/home/tcte/data/#references",
-                    "description": "List of publications.",
                     "@type": "dcat:Distribution",
+                    "description": "List of publications.",
+                    "downloadURL": "http://lasp.colorado.edu/home/tcte/data/#references",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TCTE3TSI6_004.png",
+            "identifier": "C1704861146-GES_DISC",
+            "issued": "2020-03-06",
+            "keyword": [
+                "solar activity",
+                "earth science",
+                "sun-earth interactions"
+            ],
+            "landingPage": "https://doi.org/10.5067/TCTE/TIM/DATA307",
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
+            "series-name": "TCTE3TSI6",
+            "temporal": "2013-12-13T00:00:00Z/2019-05-15T23:59:59.999Z",
             "theme": [
                 "TCTE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TCTE Level 3 Total Solar Irradiance 6-Hour Means V004 (TCTE3TSI6) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/231/",
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
-            "identifier": "DASHLINK_231",
             "description": "DISTRIBUTED ANOMALY DETECTION USING SATELLITE DATA FROM\r\nMULTIPLE MODALITIES\r\n\r\nKANISHKA BHADURI*, KAMALIKA DAS**, AND PETR VOTAVA***\r\n\r\nAbstract. There has been a tremendous increase in the volume of Earth Science data over the\r\nlast decade from modern satellites, in-situ sensors and different climate models. All these datasets\r\nneed to be co-analyzed for finding interesting patterns or for searching for extremes or outliers.\r\nInformation extraction from such rich data sources using advanced data mining methodologies is\r\na challenging task not only due to the massive volume of data, but also because these datasets\r\nate physically stored at different geographical locations. Moving these petabytes of data over the\r\nnetwork to a single location may waste a lot of bandwidth, and can take days to finish. To solve this\r\nproblem, in this paper, we present a novel algorithm which can identify outliers in the global data\r\nwithout moving all the data to one location. The algorithm is highly accurate (close to 99%) and\r\nrequires centralizing less than 5% of the entire dataset. We demonstrate the performance of the\r\nalgorithm using data obtained from the NASA MODerate-resolution Imaging Spectroradiometer\r\n(MODIS) satellite images.",
-            "title": "DISTRIBUTED ANOMALY DETECTION USING SATELLITE DATA FROM MULTIPLE MODALITIES",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/Paper_9_.pdf",
-                    "description": "DISTRIBUTED ANOMALY DETECTION USING SATELLITE DATA FROM MULTIPLE MODALITIES",
                     "@type": "dcat:Distribution",
+                    "description": "DISTRIBUTED ANOMALY DETECTION USING SATELLITE DATA FROM MULTIPLE MODALITIES",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/Paper_9_.pdf",
+                    "mediaType": "application/pdf",
                     "title": "Paper 9 .pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_231",
+            "issued": "2010-10-13",
+            "keyword": [
+                "ames",
+                "nasa",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/231/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "DISTRIBUTED ANOMALY DETECTION USING SATELLITE DATA FROM MULTIPLE MODALITIES"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMIP-3-ESC3-V1.0",
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
+            "description": "This archive contains data from the RPC-MIP instrument onboard ROSETTA Orbiter, acquired during the comet escort part 3 phase. The primary target was comet 67P/C-G. It also contains documentation which describes the MIP experiment.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmip-3-esc3-v1.0_jb7s-nbcv",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMIP-3-ESC3-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmip-3-esc3-v1.0_jb7s-nbcv",
-            "description": "This archive contains data from the RPC-MIP instrument onboard ROSETTA Orbiter, acquired during the comet escort part 3 phase. The primary target was comet 67P/C-G. It also contains documentation which describes the MIP experiment.",
-            "title": "ROSETTA-ORBITER 67P RPCMIP 3 ESC3 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCMIP 3 ESC3 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/KPF561IJYQSZ",
             "citation": "Miyazaki, Kazuyuki. 2024-02-06. TRPSCRENOXAM2D. Version 1. TROPESS Chemical Reanalysis Surface Anthropogenic NOx emissions Monthly 2-dimensional Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/KPF561IJYQSZ. https://disc.gsfc.nasa.gov/datacollection/TRPSCRENOXAM2D_1.html. Digital Science Data.",
-            "issued": "2023-01-09",
-            "temporal": "2005-01-01T00:00:00Z/2024-02-12T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-09",
-            "references": [
-                "https://doi.org/10.1126/sciadv.abf7460"
-            ],
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric chemistry"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "KAZUYUKI MIYAZAKI",
                 "hasEmail": "mailto:kazuyuki.miyazaki@jpl.nasa.gov"
             },
+            "creator": "Miyazaki, Kazuyuki",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2837624964-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS Chemical Reanalysis Surface Anthropogenic NOx emissions Monthly 2-dimensional Product contains nitrogen oxides (NO and NO2) emissions from anthropogenic sources. The data are part of the Tropospheric Chemical Reanalysis v2 (TCR-2) for the period 2005-2021. TCR-2 uses JPL's Multi-mOdel Multi-cOnstituent Chemical (MOMO-Chem) data assimilation framework that simultaneously optimizes both concentrations and emissions of multiple species from multiple satellite sensors.\n\nThe data files are written in the netCDF version 4 file format, and each file contains a year of data at monthly resolution, and a spatial resolution of 1.125 x 1.125 degrees. The principal investigator for the TCR-2 data is Miyazaki, Kazuyuki.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSCRENOXAM2D",
-            "creator": "Miyazaki, Kazuyuki",
-            "graphic-preview-description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
-            "title": "TROPESS Chemical Reanalysis Surface Anthropogenic NOx emissions Monthly 2-dimensional Product V1 (TRPSCRENOXAM2D) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRENOXAM2D_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FKPF561IJYQSZ",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FKPF561IJYQSZ",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRENOXAM2D_Sample.png",
-                    "description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRENOXAM2D_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSCRENOXAM2D_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSCRENOXAM2D_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_MON_VERTCONCS/TRPSCRENOXAM2D.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_MON_VERTCONCS/TRPSCRENOXAM2D.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSCRENOXAM2D_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSCRENOXAM2D_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TCR2_MON_VERTCONCS/TRPSCRENOXAM2D.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TCR2_MON_VERTCONCS/TRPSCRENOXAM2D.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_MON_VERTCONCS/TRPSCRENOXAM2D.1/doc/TROPESS_ChemReanalysis_Forward_Stream_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_MON_VERTCONCS/TRPSCRENOXAM2D.1/doc/TROPESS_ChemReanalysis_Forward_Stream_README.pdf",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRENOXAM2D_Sample.png",
+            "identifier": "C2837624964-GES_DISC",
+            "issued": "2023-01-09",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/KPF561IJYQSZ",
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
+            "series-name": "TRPSCRENOXAM2D",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2005-01-01T00:00:00Z/2024-02-12T00:00:00Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS Chemical Reanalysis Surface Anthropogenic NOx emissions Monthly 2-dimensional Product V1 (TRPSCRENOXAM2D) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-POS-4-SUMM-HGCOORDS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-pos-4-summ-hgcoords-v1.0_jb9n-46ut",
+            "issued": "2018-06-26",
+            "keyword": [
+                "voyager",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-POS-4-SUMM-HGCOORDS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-pos-4-summ-hgcoords-v1.0_jb9n-46ut",
-            "description": "not applicable",
-            "title": "VG2 SAT EPHEMERIS HELIOGRAPHIC COORDS BROWSE V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG2 SAT EPHEMERIS HELIOGRAPHIC COORDS BROWSE V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/216",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Nye, P.H., and D.J. Greenland. 2013. NPP Tropical Forest: Kade, Ghana, 1957-1972, R1. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/216",
-            "issued": "2023-08-17",
-            "temporal": "1945-01-01T00:00:00Z/1997-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-17",
-            "keyword": [
-                "vegetation",
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
-            "identifier": "C2752610968-ORNL_CLOUD",
             "description": "This data set contains one NPP data file and two climate data files (ASCII .txt format). The NPP file contains above- and below- ground biomass, litterfall, standing litter crop, and nutrient content data for a moist semi-deciduous secondary tropical forest at the Kade Agricultural Research Station (6.15 N 0.92 W), Ghana, spanning several collections periods between 1957 and 1972. Climate data come from weather stations at Kade near the study site (1958-1997) and at Kumasi near Kade (1945-1990).The Kade study site is typical of an old secondary forest which has probably not been cultivated or harvested since around 1915-1925. Tree basal area measured in 1957 was quite high at 33.7 m2/ha; measurements in 1968 of a plot a few hundred meters away gave 30.6 m2/ha.Detailed above- and below-ground biomass data are provided from a single clear-felling made in 1957. Nutrient content for lianas, leaves and twigs, branches, large wood, standing dead wood, stumps, litter, and roots is also provided. Total live + dead biomass was 36,102 g/m2, of which 5,414 g/m2 (15%) was below-ground live biomass and 23,568 g/m2 was above-ground live biomass. Monthly litterfall is available for 26 months (1970-72).Total annual NPP was estimated in the late 1950s at about 2,400 g/m2/year based on litterfall of 1,054 g/m2/year plus rough estimates of timber fall (1,070-1,121 g/m2/year) and root production (258 g/m2/year). In the 1970s, NPP was recalculated at 2,200-2,500 g/m2/year based on additional measurements of litter, wood fall, and decomposition.",
-            "graphic-preview-description": "Browse Image",
-            "title": "NPP Tropical Forest: Kade, Ghana, 1957-1972, R1",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/npp_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F216",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F216",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/npp/tropical_forest/NPP_KDE/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/npp/tropical_forest/NPP_KDE/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_KDE.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_KDE.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/216",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/216",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/tropical_forest/NPP_KDE/comp/NPP_KDE.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/tropical_forest/NPP_KDE/comp/NPP_KDE.pdf",
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
+            "identifier": "C2752610968-ORNL_CLOUD",
+            "issued": "2023-08-17",
+            "keyword": [
+                "vegetation",
+                "ecological dynamics",
+                "earth science",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/216",
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
             "spatial": "6.15 -0.92",
+            "temporal": "1945-01-01T00:00:00Z/1997-12-31T23:59:59Z",
             "theme": [
                 "NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NPP Tropical Forest: Kade, Ghana, 1957-1972, R1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FCAL-ALICE-4-PRL-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains CODMAC level 4 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the comet 67P/Churyumov-Gerasimenko prelanding mission phase, which took place between 2014-01-21 and 2014-11-18.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cal-alice-4-prl-v1.0_jbdr-7rbd",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "international rosetta mission",
                 "calibration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FCAL-ALICE-4-PRL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cal-alice-4-prl-v1.0_jbdr-7rbd",
-            "description": "This data set contains CODMAC level 4 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the comet 67P/Churyumov-Gerasimenko prelanding mission phase, which took place between 2014-01-21 and 2014-11-18.",
-            "title": "ROSETTA-ORBITER 67P/CAL ALICE 4 PRL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P/CAL ALICE 4 PRL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-PANCAM-3-RADCAL-RDR-V2.0",
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
+            "description": "Mars Exploration Rover 2 Pancam Radiometrically Calibrated Reduced Data Record",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-pancam-3-radcal-rdr-v2.0_jbe4-yvn7",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars exploration rover",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-PANCAM-3-RADCAL-RDR-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-pancam-3-radcal-rdr-v2.0_jbe4-yvn7",
-            "description": "Mars Exploration Rover 2 Pancam Radiometrically Calibrated Reduced Data Record",
-            "title": "MER 2 MARS PANCAM RADIOMETRICALLY\n                                   CALIBRATED RDR V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MER 2 MARS PANCAM RADIOMETRICALLY\n                                   CALIBRATED RDR V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MEASURES/DMSP-F14/SSMI/DATA304",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wentz, Frank J, Kyle Hilburn and Deborah K Smith.2012. RSS SSM/I OCEAN PRODUCT GRIDS MONTHLY AVERAGE FROM DMSP F14 NETCDF [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/MEASURES/DMSP-F14/SSMI/DATA304",
-            "issued": "2012-08-08",
-            "temporal": "1997-05-01T00:00:00Z/2008-08-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "atmospheric winds",
-                "precipitation",
-                "ocean winds",
-                "oceans",
-                "earth science",
-                "atmosphere",
-                "clouds",
-                "atmospheric water vapor"
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
-            "identifier": "C1979932834-GHRC_DAAC",
             "description": "The RSS SSM/I Ocean Product Grids Monthly Average from DMSP F14 netCDF dataset is part of the collection of Special Sensor Microwave/Imager (SSM/I) and Special Sensor Microwave Imager Sounder (SSMIS) data products produced as part of NASA's MEaSUREs Program. Remote Sensing Systems generates SSM/I and SSMIS binary data products using a unified, physically based algorithm to simultaneously retrieve ocean wind speed, water vapor, cloud water, and rain rate. The SSMIS data have been carefully intercalibrated to the brightness temperature level of the previous SSM/I and therefore extend this important time series of ocean winds, vapor, cloud and rain values. This algorithm is a product of 20 years of refinements, improvements, and verifications. The Global Hydrology Resource Center has reformatted the binary data into a netCDF data product for each temporal group for each satellite. The netCDF SSMI/SSMIS collection will be available for F14 for a monthly average.",
-            "graphic-preview-description": "N/A",
-            "title": "RSS SSM/I OCEAN PRODUCT GRIDS MONTHLY AVERAGE FROM DMSP F14 NETCDF V7",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f14/monthly/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FDMSP-F14%2FSSMI%2FDATA304",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FDMSP-F14%2FSSMI%2FDATA304",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=rssmif14m",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=rssmif14m",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f14/monthly/browse/2002/f14_ssmi_200212v7_WV.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f14/monthly/browse/2002/f14_ssmi_200212v7_WV.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f14/monthly/browse/2002/f14_ssmi_200212v7_RR.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f14/monthly/browse/2002/f14_ssmi_200212v7_RR.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f14/monthly/browse/2002/f14_ssmi_200212v7_WS.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f14/monthly/browse/2002/f14_ssmi_200212v7_WS.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f14/monthly/browse/2002/f14_ssmi_200212v7_CW.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f14/monthly/browse/2002/f14_ssmi_200212v7_CW.png",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ssmi_netcdf/rain.pdf",
-                    "description": "SSM/I Rain Retrievals Within an Unified All-Weather Ocean Algorithm",
                     "@type": "dcat:Distribution",
+                    "description": "SSM/I Rain Retrievals Within an Unified All-Weather Ocean Algorithm",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ssmi_netcdf/rain.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/opendap/ssmi/f14/monthly/",
-                    "description": "OPeNDAP server dataset access",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP server dataset access",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/opendap/ssmi/f14/monthly/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ssmi_netcdf/2012_Wentz_011012_Version-7_SSMI_Calibration.pdf",
-                    "description": "SSM/I Version-7 Calibration Report",
                     "@type": "dcat:Distribution",
+                    "description": "SSM/I Version-7 Calibration Report",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ssmi_netcdf/2012_Wentz_011012_Version-7_SSMI_Calibration.pdf",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f14/monthly/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f14/monthly/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f14/monthly/browse/",
+            "identifier": "C1979932834-GHRC_DAAC",
+            "issued": "2012-08-08",
+            "keyword": [
+                "atmospheric winds",
+                "precipitation",
+                "ocean winds",
+                "oceans",
+                "earth science",
+                "atmosphere",
+                "clouds",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/DMSP-F14/SSMI/DATA304",
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
+            "temporal": "1997-05-01T00:00:00Z/2008-08-31T23:59:59Z",
             "theme": [
                 "DISCOVER",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "RSS SSM/I OCEAN PRODUCT GRIDS MONTHLY AVERAGE FROM DMSP F14 NETCDF V7"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/CYGNS-L1C10",
             "citation": "CYGNSS. 2020-05-22. CYGNSS Level 1 Climate Data Record. Version 1.0. CYGNSS Level 1 Climate Data Record Version 1.0. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/CYGNS-L1C10. https://cygnss.engin.umich.edu/. CYGNSS, PO.DAAC, 2020-05-22, CYGNSS Level 1 Climate Data Record Version 1.0, http://clasp-research.engin.umich.edu/missions/cygnss/.",
-            "issued": "2020-04-01",
-            "temporal": "2017-03-18T00:00:00Z/2021-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-04-01",
-            "references": [
-                "https://doi.org/10.1109/JSTARS.2018.2832981"
-            ],
-            "keyword": [
-                "earth science",
-                "radar",
-                "spectral/engineering"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
             },
-            "identifier": "C1996881862-POCLOUD",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "description": "This Level 1 (L1) dataset contains the Version 1.0 Climate Data Record (CDR) of the geo-located Delay Doppler Maps (DDMs) calibrated into Power Received (Watts) and Bistatic Radar Cross Section (BRCS) expressed in units of m2 from the Delay Doppler Mapping Instrument aboard the CYGNSS satellite constellation. Other useful scientific and engineering measurement parameters include the DDM of Normalized Bistatic Radar Cross Section (NBRCS), the Delay Doppler Map Average (DDMA) of the NBRCS near the specular reflection point, and the Leading Edge Slope (LES) of the integrated delay waveform. The L1 dataset contains a number of other engineering and science measurement parameters, including sets of quality flags/indicators, error estimates, and bias estimates as well as a variety of orbital, spacecraft/sensor health, timekeeping, and geolocation parameters. At most, 8 netCDF data files (each file corresponding to a unique spacecraft in the CYGNSS constellation) are provided each day; under nominal conditions, there are typically 6-8 spacecraft retrieving data each day, but this can be maximized to 8 spacecraft under special circumstances in which higher than normal retrieval frequency is needed (i.e., during tropical storms and or hurricanes). Latency is approximately 2 months, depending on the availability of the MERRA wind speed reanalysis. The Version 1.0 CDR represents the first climate-quality release and is a collection of reanalysis products derived from the v2.1 Level 1 data. Calibration accuracy and long term stability are improved relative to the SDR v2.1 using a new trackwise correction algorithm which constrains the average value of the L1 data using MERRA-2 reanalysis wind speeds. Details of the algorithm are provide in the Trackwise Corrected CDR Algorithm Theoretical Basis Document. The CDR exhibits improved calibration accuracy and stability over v2.1. Trackwise correction is applied to the two primary CYGNSS L1 science data products  the normalized bistatic radar cross section (NBRCS) and the leading edge slope of the Doppler-integrated delay waveform (LES). The correction compensates for variations in the transmit power level of the GPS signals measured by the CYGNSS bistatic radar receivers. By comparison, the v2.1 SDR L1 algorithm assumes a constant GPS transmit power, and variations in it can be misinterpreted as variations in the L1 data and in subsequent L2 science data products derived from them. The GPS constellation consists of several different satellite models (a.k.a. block types) and the level of transmit power variation differs between them. The more recent Block IIF models (which account for ~37% of the GPS constellation) have significantly larger variations than the older models and, for this reason, they have been screened out and not used to produce v2.1 L2 or L3 science data products. Trackwise correction eliminates the need for this screening so CDR L2 and L3 data products now include Block IIF samples. It should be noted that the trackwise correction algorithm cannot be successfully applied to all v2.1 SDR L1 data, so there is also some loss of samples that were present in v2.1. Overall, there is a significant increase in sampling and improvement in spatial coverage with the CDR products.",
-            "release-place": "PO.DAAC",
-            "series-name": "CYGNSS Level 1 Climate Data Record",
             "creator": "CYGNSS",
-            "title": "CYGNSS Level 1 Climate Data Record Version 1.0",
-            "graphic-preview-description": "Thumbnail",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_L1_CDR_V1.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This Level 1 (L1) dataset contains the Version 1.0 Climate Data Record (CDR) of the geo-located Delay Doppler Maps (DDMs) calibrated into Power Received (Watts) and Bistatic Radar Cross Section (BRCS) expressed in units of m2 from the Delay Doppler Mapping Instrument aboard the CYGNSS satellite constellation. Other useful scientific and engineering measurement parameters include the DDM of Normalized Bistatic Radar Cross Section (NBRCS), the Delay Doppler Map Average (DDMA) of the NBRCS near the specular reflection point, and the Leading Edge Slope (LES) of the integrated delay waveform. The L1 dataset contains a number of other engineering and science measurement parameters, including sets of quality flags/indicators, error estimates, and bias estimates as well as a variety of orbital, spacecraft/sensor health, timekeeping, and geolocation parameters. At most, 8 netCDF data files (each file corresponding to a unique spacecraft in the CYGNSS constellation) are provided each day; under nominal conditions, there are typically 6-8 spacecraft retrieving data each day, but this can be maximized to 8 spacecraft under special circumstances in which higher than normal retrieval frequency is needed (i.e., during tropical storms and or hurricanes). Latency is approximately 2 months, depending on the availability of the MERRA wind speed reanalysis. The Version 1.0 CDR represents the first climate-quality release and is a collection of reanalysis products derived from the v2.1 Level 1 data. Calibration accuracy and long term stability are improved relative to the SDR v2.1 using a new trackwise correction algorithm which constrains the average value of the L1 data using MERRA-2 reanalysis wind speeds. Details of the algorithm are provide in the Trackwise Corrected CDR Algorithm Theoretical Basis Document. The CDR exhibits improved calibration accuracy and stability over v2.1. Trackwise correction is applied to the two primary CYGNSS L1 science data products  the normalized bistatic radar cross section (NBRCS) and the leading edge slope of the Doppler-integrated delay waveform (LES). The correction compensates for variations in the transmit power level of the GPS signals measured by the CYGNSS bistatic radar receivers. By comparison, the v2.1 SDR L1 algorithm assumes a constant GPS transmit power, and variations in it can be misinterpreted as variations in the L1 data and in subsequent L2 science data products derived from them. The GPS constellation consists of several different satellite models (a.k.a. block types) and the level of transmit power variation differs between them. The more recent Block IIF models (which account for ~37% of the GPS constellation) have significantly larger variations than the older models and, for this reason, they have been screened out and not used to produce v2.1 L2 or L3 science data products. Trackwise correction eliminates the need for this screening so CDR L2 and L3 data products now include Block IIF samples. It should be noted that the trackwise correction algorithm cannot be successfully applied to all v2.1 SDR L1 data, so there is also some loss of samples that were present in v2.1. Overall, there is a significant increase in sampling and improvement in spatial coverage with the CDR products.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCYGNS-L1C10",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCYGNS-L1C10",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/148-0389-1_ATBD_Trackwise_Corrected_CDR.pdf",
-                    "description": "Algorithm Theoretical Basis Document (ATBD) for the CYGNSS Climate Data Record (CDR)",
                     "@type": "dcat:Distribution",
+                    "description": "Algorithm Theoretical Basis Document (ATBD) for the CYGNSS Climate Data Record (CDR)",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/148-0389-1_ATBD_Trackwise_Corrected_CDR.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/forum/viewtopic.php?f=16&t=1261",
-                    "description": "Forum Post Capturing Changes to CYGNSS Sampling Rate",
                     "@type": "dcat:Distribution",
+                    "description": "Forum Post Capturing Changes to CYGNSS Sampling Rate",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/forum/viewtopic.php?f=16&t=1261",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product history"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_L1_CDR_V1.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_L1_CDR_V1.0.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/148-0137_ATBD_L1B_DDMCalibration_Rev2_Aug2018_release.pdf",
-                    "description": "Algorithm Theoretical Basis Document (ATBD) for Level 1B DDM Calibration, S. Gleason, CYGNSS Project Document 148-0137, Rev 2, 20 Aug. 2018.",
                     "@type": "dcat:Distribution",
+                    "description": "Algorithm Theoretical Basis Document (ATBD) for Level 1B DDM Calibration, S. Gleason, CYGNSS Project Document 148-0137, Rev 2, 20 Aug. 2018.",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/148-0137_ATBD_L1B_DDMCalibration_Rev2_Aug2018_release.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://cygnss.engin.umich.edu/wp-content/uploads/sites/534/2021/06/CYGNSS_Handbook_April2016.pdf",
-                    "description": "Deriving Surface Winds from Tropical Cyclones",
                     "@type": "dcat:Distribution",
+                    "description": "Deriving Surface Winds from Tropical Cyclones",
+                    "downloadURL": "https://cygnss.engin.umich.edu/wp-content/uploads/sites/534/2021/06/CYGNSS_Handbook_April2016.pdf",
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
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/148-0386-1_L1_v1.0_CDR_netCDF_Data_Dictionary.xlsx",
-                    "description": "Level 1 netCDF Data Dictionary",
                     "@type": "dcat:Distribution",
+                    "description": "Level 1 netCDF Data Dictionary",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/148-0386-1_L1_v1.0_CDR_netCDF_Data_Dictionary.xlsx",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/148-0136_ATBD_L1A_DDMCalibration_Rev2_Aug2018_release.pdf",
-                    "description": "Algorithm Theoretical Basis Document (ATBD) for Level 1A DDM Calibration, S. Gleason, CYGNSS Project Document 148-0136, Rev 2, 20 Aug. 2018.",
                     "@type": "dcat:Distribution",
+                    "description": "Algorithm Theoretical Basis Document (ATBD) for Level 1A DDM Calibration, S. Gleason, CYGNSS Project Document 148-0136, Rev 2, 20 Aug. 2018.",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/148-0136_ATBD_L1A_DDMCalibration_Rev2_Aug2018_release.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1109/TGRS.2015.2502245",
-                    "description": "Gleason, S., Ruf, C., Clarizia, M. P., & O'Brien, A. (2016). Calibration and Unwrapping of the Normalized Scattering Cross Section for the Cyclone Global Navigation Satellite System (CYGNSS). IEEE Trans. Geosci. Remote Sens., https://doi.org/10.1109/TGRS.2015.2502245.",
                     "@type": "dcat:Distribution",
+                    "description": "Gleason, S., Ruf, C., Clarizia, M. P., & O'Brien, A. (2016). Calibration and Unwrapping of the Normalized Scattering Cross Section for the Cyclone Global Navigation Satellite System (CYGNSS). IEEE Trans. Geosci. Remote Sens., https://doi.org/10.1109/TGRS.2015.2502245.",
+                    "downloadURL": "https://doi.org/10.1109/TGRS.2015.2502245",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/BAMS-D-14-00218.1",
-                    "description": "Ruf, C., Atlas, R., Chang, P., Clarizia, M., Garrison, J., Gleason, S., Katzberg, S., Jelenak, Z., Johnson, J., Majumdar, S., O'Brien, A., Posselt, D., Ridley, A., Rose, R., & Zavorotny, V. (2015). New Ocean Winds Satellite Mission to Probe Hurricanes and Tropical Convection. Bull. Amer. Meteor. Soc., https://doi.org/10.1175/BAMS-D-14-00218.1.",
                     "@type": "dcat:Distribution",
+                    "description": "Ruf, C., Atlas, R., Chang, P., Clarizia, M., Garrison, J., Gleason, S., Katzberg, S., Jelenak, Z., Johnson, J., Majumdar, S., O'Brien, A., Posselt, D., Ridley, A., Rose, R., & Zavorotny, V. (2015). New Ocean Winds Satellite Mission to Probe Hurricanes and Tropical Convection. Bull. Amer. Meteor. Soc., https://doi.org/10.1175/BAMS-D-14-00218.1.",
+                    "downloadURL": "https://doi.org/10.1175/BAMS-D-14-00218.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1996881862-POCLOUD/",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1996881862-POCLOUD/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1996881862-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1996881862-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_1.txt",
-                    "description": "Attitude Tables Updated Monthly",
                     "@type": "dcat:Distribution",
+                    "description": "Attitude Tables Updated Monthly",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_1.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_2.txt",
-                    "description": "Attitude Tables Updated Monthly",
                     "@type": "dcat:Distribution",
+                    "description": "Attitude Tables Updated Monthly",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_2.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_3.txt",
-                    "description": "Attitude Tables Updated Monthly",
                     "@type": "dcat:Distribution",
+                    "description": "Attitude Tables Updated Monthly",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_3.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_4.txt",
-                    "description": "Attitude Tables Updated Monthly",
                     "@type": "dcat:Distribution",
+                    "description": "Attitude Tables Updated Monthly",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_4.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_5.txt",
-                    "description": "Attitude Tables Updated Monthly",
                     "@type": "dcat:Distribution",
+                    "description": "Attitude Tables Updated Monthly",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_5.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_6.txt",
-                    "description": "Attitude Tables Updated Monthly",
                     "@type": "dcat:Distribution",
+                    "description": "Attitude Tables Updated Monthly",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_6.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_7.txt",
-                    "description": "Attitude Tables Updated Monthly",
                     "@type": "dcat:Distribution",
+                    "description": "Attitude Tables Updated Monthly",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_7.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_8.txt",
-                    "description": "Attitude Tables Updated Monthly",
                     "@type": "dcat:Distribution",
+                    "description": "Attitude Tables Updated Monthly",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_8.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_L1_CDR_V1.0.jpg",
+            "identifier": "C1996881862-POCLOUD",
+            "issued": "2020-04-01",
+            "keyword": [
+                "earth science",
+                "radar",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/CYGNS-L1C10",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-04-01",
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
+            "series-name": "CYGNSS Level 1 Climate Data Record",
             "spatial": "-180.0 -40.0 180.0 40.0",
+            "temporal": "2017-03-18T00:00:00Z/2021-03-01T00:00:00Z",
             "theme": [
                 "CYGNSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CYGNSS Level 1 Climate Data Record Version 1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0446-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-11-20T01:37:40.000 to 2014-11-20T13:30:25.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0446-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0446-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0446-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-11-20T01:37:40.000 to 2014-11-20T13:30:25.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0446 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0446 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3318-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-08-03T08:46:29.000 to 2012-08-03T11:25:02.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3318-v1.0_jbh9-79sd",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars express"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3318-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3318-v1.0_jbh9-79sd",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-08-03T08:46:29.000 to 2012-08-03T11:25:02.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3318 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3318 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCIES-5-ESC1-V1.0",
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
+            "description": "This dataset contains DERIVED DATA of the Rosetta RPCIES instrument taken during the comet escort 1 phase (ESC1). The target of this phase was comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). Included are the data taken between 06 Apr 2016 and 30 Jun 2016.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcies-5-esc1-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCIES-5-ESC1-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcies-5-esc1-v1.0",
-            "description": "This dataset contains DERIVED DATA of the Rosetta RPCIES instrument taken during the comet escort 1 phase (ESC1). The target of this phase was comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). Included are the data taken between 06 Apr 2016 and 30 Jun 2016.",
-            "title": "ROSETTA-ORBITER 67P RPCIES 5 ESC1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCIES 5 ESC1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2331332372-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC.",
-            "issued": "2019-06-23",
-            "temporal": "2002-07-04T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-10-01",
-            "keyword": [
-                "national geospatial data asset",
-                "ngda",
-                "earth science",
-                "ocean chemistry",
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
-            "identifier": "C2331332372-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "Aqua MODIS Global Mapped Particulate Organic Carbon (POC) - Near Real Time (NRT) Data, version R2022.0",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/AQUA/MODIS/L3M/POC/2022",
-                    "description": "MODIS-Aqua L3M Particulate Organic Carbon (POC) - Near Real Time (NRT) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS-Aqua L3M Particulate Organic Carbon (POC) - Near Real Time (NRT) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/AQUA/MODIS/L3M/POC/2022",
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
+            "identifier": "C2331332372-OB_DAAC",
+            "issued": "2019-06-23",
+            "keyword": [
+                "national geospatial data asset",
+                "ngda",
+                "earth science",
+                "ocean chemistry",
+                "oceans"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2331332372-OB_DAAC.html",
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
+            "title": "Aqua MODIS Global Mapped Particulate Organic Carbon (POC) - Near Real Time (NRT) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-C-SESAME-2-SDL-V1.0",
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
+            "description": "This archive contains edited data (CODMAC level 2) from the SESAME instrument onboard ROSETTA Lander, acquired during the SDL phase. It also contains documentation which describes the SESAME experiment. The primary target is the comet 67P/CHURYUMOV-GERASIMENKO. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-c-sesame-2-sdl-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-C-SESAME-2-SDL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-c-sesame-2-sdl-v1.0",
-            "description": "This archive contains edited data (CODMAC level 2) from the SESAME instrument onboard ROSETTA Lander, acquired during the SDL phase. It also contains documentation which describes the SESAME experiment. The primary target is the comet 67P/CHURYUMOV-GERASIMENKO. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER 67P SESAME 2 SDL\n                            V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-LANDER 67P SESAME 2 SDL\n                            V1.0"
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
+            "description": "The Cassini Magnetospheric Imaging Instrument(MIMI) Imaging Neutral Camera (INCA) uncalibrated data set includes all data collected from the MIMI Data Processing Unit during the mission.  The original data has been decommutated and decoded by software at the Applied Physics Laboratory (APL) and has been then further ordered and filtered by software at Fundamental Technologies, LLC. The data is provided in an uncalibrated form in conjunction with a PDS MIMI calibration volume COMIMI_0000 which provides specific algorithms for the derivation of calibrated data. This data set includes uncalibrated values of counts in the form of rates and of rate images for the INCA sensor for all times during the mission including the Earth flyby, the Jupiter flyby, interplanetary cruise, and the entire Saturn tour.  Data are presented in a set of tables which are of variable length and use a comma to separate various fields.  This data set is intended to be the most comprehensive and complete data set included in the Cassini MIMI INCA archive.  A browse data set is included with Key Parameter data that is calibrated using the algorithms provided in the Calibration volume. In addition, a series of images are provided with the KP browse data that displays the KP data which can lead the user to the particular times of interest. This data set should be among the first used by a user of any of the MIMI INCA archive as it will lead one to information required to search for more detailed or highly specialized features in the original data.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-e-j-s-sw-mimi-2-inca-uncalib-v1.0_jbnq-6aee",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "earth",
                 "cassini-huygens",
                 "jupiter",
                 "saturn"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-E%2FJ%2FS%2FSW-MIMI-2-INCA-UNCALIB-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-e-j-s-sw-mimi-2-inca-uncalib-v1.0_jbnq-6aee",
-            "description": "The Cassini Magnetospheric Imaging Instrument(MIMI) Imaging Neutral Camera (INCA) uncalibrated data set includes all data collected from the MIMI Data Processing Unit during the mission.  The original data has been decommutated and decoded by software at the Applied Physics Laboratory (APL) and has been then further ordered and filtered by software at Fundamental Technologies, LLC. The data is provided in an uncalibrated form in conjunction with a PDS MIMI calibration volume COMIMI_0000 which provides specific algorithms for the derivation of calibrated data. This data set includes uncalibrated values of counts in the form of rates and of rate images for the INCA sensor for all times during the mission including the Earth flyby, the Jupiter flyby, interplanetary cruise, and the entire Saturn tour.  Data are presented in a set of tables which are of variable length and use a comma to separate various fields.  This data set is intended to be the most comprehensive and complete data set included in the Cassini MIMI INCA archive.  A browse data set is included with Key Parameter data that is calibrated using the algorithms provided in the Calibration volume. In addition, a series of images are provided with the KP browse data that displays the KP data which can lead the user to the particular times of interest. This data set should be among the first used by a user of any of the MIMI INCA archive as it will lead one to information required to search for more detailed or highly specialized features in the original data.",
-            "title": "CASSINI E/J/S/SW MIMI INCA SENSOR UNCALIBRATED DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI E/J/S/SW MIMI INCA SENSOR UNCALIBRATED DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/SCAR_B/0001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1999-10-15. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/SCAR_B/0001. http://eosweb.larc.nasa.gov/project/scarb/scarb_table.",
-            "issued": "1999-10-15",
-            "temporal": "1995-08-17T00:00:00Z/1995-09-20T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-03",
-            "keyword": [
-                "clouds",
-                "earth science",
-                "precipitation",
-                "atmospheric chemistry",
-                "atmosphere",
-                "air quality",
-                "aerosols"
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
-            "identifier": "C1337195067-LARC_ASDC",
             "description": "SCAR_B_UWC131A data are Smoke/Sulfates, Clouds and Radiation Experiment in Brazil data from instruments on board the University of Washington C131A aircraft in Native format.Smoke/Sulfates, Clouds and Radiation - Brazil (SCAR-B) data include physical and chemical components of the Earth's surface, the atmosphere and the radiation field collected in Brazil with an emphasis in biomass burning.The objectives for the SCAR mission are: to advance our knowledge of how the physical, chemical and radiative processes in our atmosphere are affected by sulfate aerosol and smoke from biomass burning; to improve our expertise at remotely sensing smoke, water vapor, clouds, vegetation and fires; and to assess the effects of deforestation and biomass burning on tropical landscapes.From 17 August to 20 September 1995, the University of Washington's (UW) Cloud and Aerosol Research Group, with its Convair C-131A research aircraft, participated in an intensive field study of smoke emissions from various types of biomass burning over a large area of Brazil. This included 29 flights to collect measurements and photographs.",
-            "title": "Sulfates, Clouds and Radiation Brazil (SCAR-B) University of Washington C131A Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FSCAR_B%2F0001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FSCAR_B%2F0001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -965928,25 +965905,59 @@
                     "title": "View this dataset's data citation policy"
                 }
             ],
+            "identifier": "C1337195067-LARC_ASDC",
+            "issued": "1999-10-15",
+            "keyword": [
+                "clouds",
+                "earth science",
+                "precipitation",
+                "atmospheric chemistry",
+                "atmosphere",
+                "air quality",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/SCAR_B/0001",
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
             "spatial": "-64.75 -16.85 -47.53 -2.42",
+            "temporal": "1995-08-17T00:00:00Z/1995-09-20T23:59:59Z",
             "theme": [
                 "SCAR-B",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sulfates, Clouds and Radiation Brazil (SCAR-B) University of Washington C131A Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/jbr9-q8ae",
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
+                    "downloadURL": "http://prime.jsc.nasa.gov/earthplus/Dennis/DennisCoordinates.doc",
+                    "mediaType": "application/msword"
+                }
+            ],
+            "identifier": "NASA-0000033__4",
             "issued": "2018-06-25",
-            "temporal": "2004-01-01/2005-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "atmospheric science data center",
                 "power",
@@ -965956,960 +965967,951 @@
                 "radiometry",
                 "hdf5"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Robert O. Shelton",
-                "hasEmail": "mailto:Robert.o.Shelton@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/jbr9-q8ae",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000033__4",
-            "description": "Earth+ makes NASA satellite photos and data accessible to blind students.",
-            "title": "Earth+",
-            "programCode": [
-                "026:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://prime.jsc.nasa.gov/earthplus/Dennis/DennisCoordinates.doc",
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-SA-COMPIL-3-SATPOL-V1.0",
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
-                "satellite"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This compilation of polarimetry of planetary satellites has been compiled from the published literature and from unpublished results by Zaitsev, Rosenbush, and Kiselev. Geometric observational circumstances, calculated using the JPL Horizons ephemeris system, are also included. This version of the compilation is dated April 15, 2012.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-sa-compil-3-satpol-v1.0_jbrt-qwds",
+            "issued": "2018-06-26",
+            "keyword": [
+                "support archives",
+                "satellite"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-SA-COMPIL-3-SATPOL-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-sa-compil-3-satpol-v1.0_jbrt-qwds",
-            "description": "This compilation of polarimetry of planetary satellites has been compiled from the published literature and from unpublished results by Zaitsev, Rosenbush, and Kiselev. Geometric observational circumstances, calculated using the JPL Horizons ephemeris system, are also included. This version of the compilation is dated April 15, 2012.",
-            "title": "POLARIMETRY OF PLANETARY SATELLITES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "POLARIMETRY OF PLANETARY SATELLITES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/204",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Williamson, P., and J. Pitman. 2014. NPP Grassland: Beacon Hill, U.K., 1972-1993, R1. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/204",
-            "issued": "2023-08-17",
-            "temporal": "1969-01-01T00:00:00Z/1993-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-17",
-            "keyword": [
-                "earth science",
-                "ecological dynamics",
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
-            "identifier": "C2752551426-ORNL_CLOUD",
             "description": "This data set contains two ASCII text files, one providing productivity measurements for a chalk grassland on Beacon Hill, West Sussex, U.K. (50.92 N, -0.85 W) and the other containing climate data from a weather station at the former King's College London, Rogate Field Centre, 6 km distant (51.01 N, -0.85 W). Measurements of above-ground live biomass and total dead matter were made by harvesting 0.25 m2 quadrats in the 20 x 20-m study area at eight to ten week intervals from March 1972 to April 1973. Precipitation amount and minimum/maximum temperature were recorded from 1969 through 1993.Above-ground net primary production (ANPP) was estimated by several methods: 332 g/m2/year (annual increase in living biomass, sum of species); 355 g/m2/year (peak or maximum live biomass, plant dry matter weight); 773 g/m2/year (maximum live + dead biomass); 310 g/m2/year (annual increase in living biomass carbon by summing positive increments in biomass); and 691 g/m2/year (annual net production accounting for leaf turnover). The carbon content of ANPP (accounting for leaf turnover) was estimated to be 310 gC/m2/year using a conversion factor of 0.45. Below-ground production was not measured.Revision Notes: Only the documentation for this data set has been modified. The data files have been checked for accuracy and are identical to those originally published in 1998.",
-            "graphic-preview-description": "Browse Image",
-            "title": "NPP Grassland: Beacon Hill, U.K., 1972-1993, R1",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/npp_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F204",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F204",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/npp/grassland/NPP_BCN/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/npp/grassland/NPP_BCN/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_BCN.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_BCN.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/204",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/204",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/grassland/NPP_BCN/comp/NPP_BCN.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/grassland/NPP_BCN/comp/NPP_BCN.pdf",
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
+            "identifier": "C2752551426-ORNL_CLOUD",
+            "issued": "2023-08-17",
+            "keyword": [
+                "earth science",
+                "ecological dynamics",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/204",
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
             "spatial": "50.92 -0.85",
+            "temporal": "1969-01-01T00:00:00Z/1993-12-31T23:59:59Z",
             "theme": [
                 "NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NPP Grassland: Beacon Hill, U.K., 1972-1993, R1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/FIREXAQ_jValue_AircraftInSitu_DC8_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2020-07-27. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/FIREXAQ_jValue_AircraftInSitu_DC8_Data_1.",
-            "issued": "2020-04-07",
-            "temporal": "2019-07-22T00:00:00Z/2019-09-05T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-15",
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
-            "identifier": "C1917874744-LARC_ASDC",
             "description": "FIREXAQ_jValue_AircraftInSitu_DC8_Data are in-situ photolysis rate (J-value) measurements conducted onboard the DC8 aircraft during FIREX-AQ. This product features data from the CAFS instrument. Data collection for this product is complete.\r\n\r\nCompleted during summer 2019, FIREX-AQ utilized a combination of instrumented airplanes, satellites, and ground-based instrumentation. Detailed fire plume sampling was carried out by the NASA DC-8 aircraft, which had a comprehensive instrument payload capable of measuring over 200 trace gas species, as well as aerosol microphysical, optical, and chemical properties. The DC-8 aircraft completed 23 science flights, including 15 flights from Boise, Idaho and 8 flights from Salina, Kansas. NASA\u2019s ER-2 completed 11 flights, partially in support of the FIREX-AQ effort. The ER-2 payload was made up of 8 satellite analog instruments and provided critical fire information, including fire temperature, fire plume heights, and vegetation/soil albedo information. NOAA provided the NOAA-CHEM Twin Otter and the NOAA-MET Twin Otter aircraft to measure chemical processing in the lofted plumes of Western wildfires. The NOAA-CHEM Twin Otter focused on nighttime plume chemistry, from which data is archived at the NASA Atmospheric Science Data Center (ASDC). The NOAA-MET Twin Otter collected measurements of air movements at fire boundaries with the goal of understanding the local weather impacts of fires and the movement patterns of fires. NOAA-MET Twin Otter data will be archived at the ASDC in the future. Additionally, a ground-based station in McCall, Idaho and several mobile laboratories provided in-situ measurements of aerosol microphysical and optical properties, aerosol chemical compositions, and trace gas species. \r\n\r\nThe Fire Influence on Regional to Global Environments and Air Quality (FIREX-AQ) campaign was a NOAA/NASA interagency intensive study of North American fires to gain an understanding on the integrated impact of the fire emissions on the tropospheric chemistry and composition and to assess the satellite\u2019s capability for detecting fires and estimating fire emissions. The overarching goal of FIREX-AQ was to provide measurements of trace gas and aerosol emissions for wildfires and prescribed fires in great detail, relate them to fuel and fire conditions at the point of emission, characterize the conditions relating to plume rise, and follow plumes downwind to understand chemical transformation and air quality impacts.",
-            "title": "FIREX-AQ DC-8 In-Situ J Value Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FFIREXAQ_jValue_AircraftInSitu_DC8_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FFIREXAQ_jValue_AircraftInSitu_DC8_Data_1",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1917874744-LARC_ASDC",
-                    "description": "Earthdata Search for Product_Short_Name (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for Product_Short_Name (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1917874744-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/FIREXAQ_jValue_AircraftInSitu_DC8_Data_1",
-                    "description": "DOI data set landing page for FIREXAQ_jValue_AircraftInSitu_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIREXAQ_jValue_AircraftInSitu_DC8_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/FIREXAQ_jValue_AircraftInSitu_DC8_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
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
                     "title": "View information related to this dataset"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIREX-AQ/jValue_AircraftInSitu_DC8_Data_1/",
-                    "description": "ASDC Direct Data Download for FIREXAQ_jValue_AircraftInSitu_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIREXAQ_jValue_AircraftInSitu_DC8_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIREX-AQ/jValue_AircraftInSitu_DC8_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1917874744-LARC_ASDC",
+            "issued": "2020-04-07",
+            "keyword": [
+                "atmospheric chemistry",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/FIREXAQ_jValue_AircraftInSitu_DC8_Data_1",
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
+            "temporal": "2019-07-22T00:00:00Z/2019-09-05T23:59:59.999Z",
             "theme": [
                 "FIREX-AQ",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FIREX-AQ DC-8 In-Situ J Value Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSIWAC-4-CR4A-CHKOUT-STR-REFL-V1.0",
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
-                "jupiter"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units  (normalized and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the CRUISE 4-1 mission phase, covering the period  from 2008-01-28T00:00:00.000 to 2008-08-03T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. This version V1.0 is the first version of this dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osiwac-4-cr4a-chkout-str-refl-v1.0_jbts-pr35",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "jupiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSIWAC-4-CR4A-CHKOUT-STR-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osiwac-4-cr4a-chkout-str-refl-v1.0_jbts-pr35",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units  (normalized and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the CRUISE 4-1 mission phase, covering the period  from 2008-01-28T00:00:00.000 to 2008-08-03T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. This version V1.0 is the first version of this dataset.",
-            "title": "ROSETTA-ORBITER CHECKOUT OSIWAC 4 CR4A RDR-STR-REFL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECKOUT OSIWAC 4 CR4A RDR-STR-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SPUR2-NBFLT",
             "bureauCode": [
                 "026:00"
             ],
-            "citation": "Andrey Shcherbina. 2019-10-24. SPURS-2 Neutrally buoyant float data for the E. Tropical Pacific field campaign. Version 1.0. SPURS-2 Field Campaign Neutrally Buoyant Float Data Products. APL, University of Washington, 1013 NE 40th St, Seattle, WA 98105, USA. Archived by National Aeronautics and Space Administration, U.S. Government, SPURS Data Management PI, Fred Bingham. https://doi.org/10.5067/SPUR2-NBFLT. http://podaac.jpl.nasa.gov/SPURS. Andrey Shcherbina, SPURS Data Management PI, Fred Bingham, 2019-10-24, SPURS-2 Neutrally buoyant float data for the E. Tropical Pacific field campaign, http://podaac.jpl.nasa.gov/SPURS.",
-            "issued": "2019-08-14",
-            "temporal": "2016-08-26T17:43:36Z/2016-12-29T08:04:45Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-08-14",
-            "keyword": [
-                "ocean temperature",
-                "salinity/density",
-                "oceans",
-                "earth science"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "identifier": "C2491772336-POCLOUD",
-            "description": "The SPURS (Salinity Processes in the Upper Ocean Regional Study) project is a NASA-funded oceanographic process study and associated field program that aim to elucidate key mechanisms responsible for near-surface salinity variations in the oceans. The project is comprised of two field campaigns and a series of cruises in regions of the Atlantic and Pacific Oceans exhibiting salinity extremes. SPURS employs a suite of state-of-the-art in-situ sampling technologies that, combined with remotely sensed salinity fields from the Aquarius/SAC-D, SMAP and SMOS satellites, provide a detailed characterization of salinity structure over a continuum of spatio-temporal scales. The SPURS-2 campaign involved two month-long cruises by the R/V Revelle in August 2016 and October 2017 combined with complementary sampling on a more continuous basis over this period by the schooner Lady Amber. Focused around a central mooring located near 10N,125W, the objective of SPURS-2 was to study the dynamics of the rainfall-dominated surface ocean at the western edge of the eastern Pacific fresh pool subject to high seasonal variability and strong zonal flows associated with the North Equatorial Current and Countercurrent. Neutrally buoyant floats (also known as Mixed Layer Floats - MLF) drift and move through the water column providing continuous CTD temperature and salinity profiles and GPS surface position location data. One float was deployed in SPURS-2 during the first Revelle cruise in August 2016 and recovered in December 2016 after 3.5 months about 1800 km east of the central mooring.  The MLF data are provided in netCDF file format with standards compliant metadata.",
-            "release-place": "APL, University of Washington, 1013 NE 40th St, Seattle, WA 98105, USA",
-            "series-name": "SPURS-2 Neutrally buoyant float data for the E. Tropical Pacific field campaign",
-            "graphic-preview-description": "Thumbnail",
-            "creator": "Andrey Shcherbina",
-            "title": "SPURS-2 Neutrally buoyant float data for the E. Tropical Pacific field campaign",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_FLOAT_NEUTRALLYBUOYANT.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "citation": "Andrey Shcherbina. 2019-10-24. SPURS-2 Neutrally buoyant float data for the E. Tropical Pacific field campaign. Version 1.0. SPURS-2 Field Campaign Neutrally Buoyant Float Data Products. APL, University of Washington, 1013 NE 40th St, Seattle, WA 98105, USA. Archived by National Aeronautics and Space Administration, U.S. Government, SPURS Data Management PI, Fred Bingham. https://doi.org/10.5067/SPUR2-NBFLT. http://podaac.jpl.nasa.gov/SPURS. Andrey Shcherbina, SPURS Data Management PI, Fred Bingham, 2019-10-24, SPURS-2 Neutrally buoyant float data for the E. Tropical Pacific field campaign, http://podaac.jpl.nasa.gov/SPURS.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "undefined",
+                "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
+            },
+            "creator": "Andrey Shcherbina",
+            "description": "The SPURS (Salinity Processes in the Upper Ocean Regional Study) project is a NASA-funded oceanographic process study and associated field program that aim to elucidate key mechanisms responsible for near-surface salinity variations in the oceans. The project is comprised of two field campaigns and a series of cruises in regions of the Atlantic and Pacific Oceans exhibiting salinity extremes. SPURS employs a suite of state-of-the-art in-situ sampling technologies that, combined with remotely sensed salinity fields from the Aquarius/SAC-D, SMAP and SMOS satellites, provide a detailed characterization of salinity structure over a continuum of spatio-temporal scales. The SPURS-2 campaign involved two month-long cruises by the R/V Revelle in August 2016 and October 2017 combined with complementary sampling on a more continuous basis over this period by the schooner Lady Amber. Focused around a central mooring located near 10N,125W, the objective of SPURS-2 was to study the dynamics of the rainfall-dominated surface ocean at the western edge of the eastern Pacific fresh pool subject to high seasonal variability and strong zonal flows associated with the North Equatorial Current and Countercurrent. Neutrally buoyant floats (also known as Mixed Layer Floats - MLF) drift and move through the water column providing continuous CTD temperature and salinity profiles and GPS surface position location data. One float was deployed in SPURS-2 during the first Revelle cruise in August 2016 and recovered in December 2016 after 3.5 months about 1800 km east of the central mooring.  The MLF data are provided in netCDF file format with standards compliant metadata.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSPUR2-NBFLT",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSPUR2-NBFLT",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_FLOAT_NEUTRALLYBUOYANT.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_FLOAT_NEUTRALLYBUOYANT.jpg",
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
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs2/docs/DataDocumentation/ReadmeCFT_2016.pdf",
-                    "description": "Data Submission Report, Instrument Calibration Report, etc",
                     "@type": "dcat:Distribution",
+                    "description": "Data Submission Report, Instrument Calibration Report, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs2/docs/DataDocumentation/ReadmeCFT_2016.pdf",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772336-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772336-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772336-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772336-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_FLOAT_NEUTRALLYBUOYANT.jpg",
+            "identifier": "C2491772336-POCLOUD",
+            "issued": "2019-08-14",
+            "keyword": [
+                "ocean temperature",
+                "salinity/density",
+                "oceans",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SPUR2-NBFLT",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-08-14",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "APL, University of Washington, 1013 NE 40th St, Seattle, WA 98105, USA",
+            "series-name": "SPURS-2 Neutrally buoyant float data for the E. Tropical Pacific field campaign",
             "spatial": "-125.015 7.855 -108.951 11.891",
+            "temporal": "2016-08-26T17:43:36Z/2016-12-29T08:04:45Z",
             "theme": [
                 "SPURS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SPURS-2 Neutrally buoyant float data for the E. Tropical Pacific field campaign"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1559",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Loboda, T.V., J.V. Hall, and A. Baer. 2017. ABoVE: Wildfire Date of Burning within Fire Scars across Alaska and Canada, 2001-2019. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1559",
-            "issued": "2021-01-14",
-            "temporal": "2001-01-01T00:00:00Z/2019-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "natural hazards",
-                "ecological dynamics",
-                "earth science",
-                "biosphere",
-                "ngda",
-                "national geospatial data asset",
-                "human dimensions"
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
-            "identifier": "C2162122340-ORNL_CLOUD",
             "description": "This dataset provides estimates of wildfire progression represented by date of burning (DoB) within fire scars across Alaska and Canada for the period 2001-2019. Burn scar locations were obtained from two datasets: the Alaskan Interagency Coordination Center (AICC) and the Natural Resources Canada (NRC) databases. All scars within these databases were used in this study. The estimated DoB was derived using an algorithm for identifying the first fire occurrence from the Moderate Resolution Imaging Spectroradiometer (MODIS) active fire detection product (MCD14ML, Collection 6) and to subsequently determine all dates of burning within fire scars. The DoB data are provided as polygons and map the daily progression of a fire within each burn scar. As a result, there is one polygon for each DoB detected within an identified burn scar boundary. The MODIS active fire points associated with the burn scar data are also provided. Data for the period 2001-2015 were first published in 2017 and data for the period 2016-2019 were added in January 2021.",
-            "graphic-preview-description": "Date of Burning (DoB) estimated for areas within each fire scar (inset) across Alaska and Canada. Red areas show fire scar locations across central Canada (detail) in 2015.",
-            "title": "ABoVE: Wildfire Date of Burning within Fire Scars across Alaska and Canada, 2001-2019",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Wildfires_Date_of_Burning_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1559",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1559",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/Wildfires_Date_of_Burning/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/Wildfires_Date_of_Burning/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Wildfires_Date_of_Burning.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Wildfires_Date_of_Burning.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1559",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1559",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Wildfires_Date_of_Burning/comp/Wildfires_Date_of_Burning.pdf",
-                    "description": "ABoVE: Wildfire Date of Burning within Fire Scars across Alaska and Canada, 2001-2019: Wildfires_Date_of_Burning.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Wildfire Date of Burning within Fire Scars across Alaska and Canada, 2001-2019: Wildfires_Date_of_Burning.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Wildfires_Date_of_Burning/comp/Wildfires_Date_of_Burning.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Wildfires_Date_of_Burning_Fig1.png",
-                    "description": "Date of Burning (DoB) estimated for areas within each fire scar (inset) across Alaska and Canada. Red areas show fire scar locations across central Canada (detail) in 2015.",
                     "@type": "dcat:Distribution",
+                    "description": "Date of Burning (DoB) estimated for areas within each fire scar (inset) across Alaska and Canada. Red areas show fire scar locations across central Canada (detail) in 2015.",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Wildfires_Date_of_Burning_Fig1.png",
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
+            "graphic-preview-description": "Date of Burning (DoB) estimated for areas within each fire scar (inset) across Alaska and Canada. Red areas show fire scar locations across central Canada (detail) in 2015.",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Wildfires_Date_of_Burning_Fig1.png",
+            "identifier": "C2162122340-ORNL_CLOUD",
+            "issued": "2021-01-14",
+            "keyword": [
+                "natural hazards",
+                "ecological dynamics",
+                "earth science",
+                "biosphere",
+                "ngda",
+                "national geospatial data asset",
+                "human dimensions"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1559",
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
             "spatial": "-178.84 41.75 -53.83 70.16",
+            "temporal": "2001-01-01T00:00:00Z/2019-12-31T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE: Wildfire Date of Burning within Fire Scars across Alaska and Canada, 2001-2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/219",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Kira, T., N. Manokaran, and S. Appanah. 2013. NPP Tropical Forest: Pasoh, Malaysia, 1971-1973, R1. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/219",
-            "issued": "2023-08-17",
-            "temporal": "1891-01-01T00:00:00Z/1990-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-17",
-            "keyword": [
-                "biosphere",
-                "earth science",
-                "ecological dynamics",
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
-            "identifier": "C2752738171-ORNL_CLOUD",
             "description": "This data set contains four ASCII data files (.txt format), one providing net primary production (NPP) component data and three providing climate data. The NPP studies were conducted in a lowland tropical rainforest in the Pasoh Forest Reserve, Malaysia (2.98 N 102.31 E) from 1971 through 1973. Precipitation and temperature data are available from weather stations located about 25 km from the study sites.",
-            "graphic-preview-description": "Browse Image",
-            "title": "NPP Tropical Forest: Pasoh, Malaysia, 1971-1973, R1",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/npp_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F219",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F219",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/npp/tropical_forest/NPP_PSH/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/npp/tropical_forest/NPP_PSH/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_PSH.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_PSH.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/219",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/219",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/tropical_forest/NPP_PSH/comp/NPP_PSH.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/tropical_forest/NPP_PSH/comp/NPP_PSH.pdf",
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
+            "identifier": "C2752738171-ORNL_CLOUD",
+            "issued": "2023-08-17",
+            "keyword": [
+                "biosphere",
+                "earth science",
+                "ecological dynamics",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/219",
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
             "spatial": "2.98 102.31",
+            "temporal": "1891-01-01T00:00:00Z/1990-12-31T23:59:59Z",
             "theme": [
                 "NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NPP Tropical Forest: Pasoh, Malaysia, 1971-1973, R1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO_L3T_SEB.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Simon Hook, Gregory Halverson. 2024-05-03. ECOSTRESS Tiled Surface Energy Balance Instantaneous L3 Global 70 m V002. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/ECOSTRESS/ECO_L3T_SEB.002. https://doi.org/10.5067/ECOSTRESS/ECO_L3T_SEB.002. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2024-05-03",
-            "temporal": "2018-07-09T00:00:00Z/2025-01-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-23",
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
-            "identifier": "C2074852168-LPCLOUD",
-            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found in Figure 2 on the ECOSTRESS website (https://ecostress.jpl.nasa.gov/science).\n\nThe ECOSTRESS Tiled Surface Energy Balance Instantaneous L3 Global 70 m (ECO_L3T_SEB) Version 2 data product provides estimated incoming surface radiation (Rg) and net radiation (Rn) aligned with each daytime ECOSTRESS overpass. The Rg was generated using the Forest Light Environmental Simulator (FLiES) radiative transfer model implemented in an artificial neural network using Cloud Optical Thickness (COT) and Aerosol Optical Thickness (AOT) from Goddard Earth Observing System Version 5 (GEOS-5) Forward Processing (FP) along with albedo from ECOSTRESS Tiled Ancillary NDVI and Albedo Level 2 Global 70 m (ECO_L2T_STARS (https://doi.org/10.5067/ECOSTRESS/ECO_L2T_STARS.002)) Version 2 as variables. The Rg output from the FLiES model was bias corrected to Rg from GEOS-FP. The Rn is an output from the Breathing Earth System Simulator (BESS) algorithm. This data product is tiled using a modified version of the Military Grid Reference System (MGRS (https://hls.gsfc.nasa.gov/products-description/tiling-system/)), which divides Universal Transverse Mercator (UTM) zones into square tiles that are 109.8 km by 109.8 km with a 70 meter (m) spatial resolution.\n\nThe ECO_L3T_SEB Version 2 data product is provided in Cloud Optimized GeoTIFF (COG) format with each data layer distributed as a separate COG. This product contains four layers including Rg, Rn, cloud mask, and water mask.\n\nKnown Issues\n\n-\tData acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly, temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented, and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4, and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\n\n-\tData acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\n\n-\tData acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.\n\n-\tMissing Cloud Layer Alert: All users of ECOSTRESS Tiled and Gridded L3 Soil Moisture and Surface Energy Balance v002 products (ECO_L3T_SM, ECO_L3G_SM, ECO_L3T_SEB and ECO_L3G_SEB) should be aware that the \u2018cloud mask\u2019 layer may be unavailable for a select number of granules for the year 2023. Users are encouraged to get that information from the corresponding Level 2 Standard Cloud Mask products (",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "Simon Hook, Gregory Halverson",
-            "title": "ECOSTRESS Tiled Surface Energy Balance Instantaneous L3 Global 70 m V002",
-            "graphic-preview-file": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/ECO_L3T_SEB.002/ECOv002_L3T_SEB_34189_030_35KPQ_20240717T120259_0712_01/ECOv002_L3T_SEB_34189_030_35KPQ_20240717T120259_0712_01.png",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found in Figure 2 on the ECOSTRESS website (https://ecostress.jpl.nasa.gov/science).\n\nThe ECOSTRESS Tiled Surface Energy Balance Instantaneous L3 Global 70 m (ECO_L3T_SEB) Version 2 data product provides estimated incoming surface radiation (Rg) and net radiation (Rn) aligned with each daytime ECOSTRESS overpass. The Rg was generated using the Forest Light Environmental Simulator (FLiES) radiative transfer model implemented in an artificial neural network using Cloud Optical Thickness (COT) and Aerosol Optical Thickness (AOT) from Goddard Earth Observing System Version 5 (GEOS-5) Forward Processing (FP) along with albedo from ECOSTRESS Tiled Ancillary NDVI and Albedo Level 2 Global 70 m (ECO_L2T_STARS (https://doi.org/10.5067/ECOSTRESS/ECO_L2T_STARS.002)) Version 2 as variables. The Rg output from the FLiES model was bias corrected to Rg from GEOS-FP. The Rn is an output from the Breathing Earth System Simulator (BESS) algorithm. This data product is tiled using a modified version of the Military Grid Reference System (MGRS (https://hls.gsfc.nasa.gov/products-description/tiling-system/)), which divides Universal Transverse Mercator (UTM) zones into square tiles that are 109.8 km by 109.8 km with a 70 meter (m) spatial resolution.\n\nThe ECO_L3T_SEB Version 2 data product is provided in Cloud Optimized GeoTIFF (COG) format with each data layer distributed as a separate COG. This product contains four layers including Rg, Rn, cloud mask, and water mask.\n\nKnown Issues\n\n-\tData acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly, temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented, and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4, and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\n\n-\tData acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\n\n-\tData acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.\n\n-\tMissing Cloud Layer Alert: All users of ECOSTRESS Tiled and Gridded L3 Soil Moisture and Surface Energy Balance v002 products (ECO_L3T_SM, ECO_L3G_SM, ECO_L3T_SEB and ECO_L3G_SEB) should be aware that the \u2018cloud mask\u2019 layer may be unavailable for a select number of granules for the year 2023. Users are encouraged to get that information from the corresponding Level 2 Standard Cloud Mask products (",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECOSTRESS%2FECO_L3T_SEB.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECOSTRESS%2FECO_L3T_SEB.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-geotiff",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2074852168-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2074852168-LPCLOUD",
+                    "mediaType": "application/x-geotiff",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO_L3T_SEB.002",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO_L3T_SEB.002",
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
-                    "downloadURL": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/ECO_L3T_SEB.002/ECOv002_L3T_SEB_34189_030_35KPQ_20240717T120259_0712_01/ECOv002_L3T_SEB_34189_030_35KPQ_20240717T120259_0712_01.png",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/ECO_L3T_SEB.002/ECOv002_L3T_SEB_34189_030_35KPQ_20240717T120259_0712_01/ECOv002_L3T_SEB_34189_030_35KPQ_20240717T120259_0712_01.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://appeears.earthdatacloud.nasa.gov/",
-                    "description": "The Application for Extracting and Exploring Analysis Ready Samples (AppEEARS) offers a simple and efficient way to perform data access and transformation processes.",
                     "@type": "dcat:Distribution",
+                    "description": "The Application for Extracting and Exploring Analysis Ready Samples (AppEEARS) offers a simple and efficient way to perform data access and transformation processes.",
+                    "downloadURL": "https://appeears.earthdatacloud.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through APPEEARS"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/ECO_L3T_SEB.002/ECOv002_L3T_SEB_34189_030_35KPQ_20240717T120259_0712_01/ECOv002_L3T_SEB_34189_030_35KPQ_20240717T120259_0712_01.png",
+            "identifier": "C2074852168-LPCLOUD",
+            "issued": "2024-05-03",
+            "keyword": [
+                "surface thermal properties",
+                "earth science",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO_L3T_SEB.002",
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
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-07-09T00:00:00Z/2025-01-27T00:00:00Z",
             "theme": [
                 "ECOSTRESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ECOSTRESS Tiled Surface Energy Balance Instantaneous L3 Global 70 m V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-VMC-3-RDR-EXT7-V1.0",
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
+            "description": "N/A",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-vmc-3-rdr-ext7-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars express",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-VMC-3-RDR-EXT7-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-vmc-3-rdr-ext7-v1.0",
-            "description": "N/A",
-            "title": "MEX MARS VMC CALIBRATED DATA EXT7\n  V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MEX MARS VMC CALIBRATED DATA EXT7\n  V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0007",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2003-06-04. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/FIRE/0007.",
-            "issued": "2003-06-04",
-            "temporal": "1998-05-02T00:00:00Z/1998-05-25T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-02",
-            "keyword": [
-                "atmospheric temperature",
-                "atmosphere",
-                "earth science",
-                "atmospheric pressure",
-                "atmospheric winds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRANK LAFONTAINE",
                 "hasEmail": "mailto:frank.j.lafontaine@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1000000923-LARC_ASDC",
             "description": "The First ISCCP Regional Experiments have been designed to improve data products and cloud/radiation parameterizations used in general circulation models (GCMs). Specifically, the goals of FIRE are (1) to improve basic understanding of the interaction of physical processes in determining life cycles of cirrus and marine stratocumulus systems and the radiative properties of these clouds during their life cycles and (2) to investigate the interrelationships between the ISCCP data, GCM parameterizations, and higher space and time resolution cloud data.First ISCCP Regional Experiment - Arctic Cloud Experiment Utrecht University Tethered Balloon.",
-            "title": "First ISCCP Regional Experiment - Arctic Cloud Experiment Utrecht University Tethered Balloon",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0007",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0007",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000923-LARC_ASDC",
-                    "description": "Earthdata Search for FIRE_ACE_UTRECHT_BALLOON_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FIRE_ACE_UTRECHT_BALLOON_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000923-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0007",
-                    "description": "DOI data set landing page for FIRE_ACE_UTRECHT_BALLOON_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIRE_ACE_UTRECHT_BALLOON_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0007",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_ACE_UTRECHT_BALLOON/",
-                    "description": "ASDC Direct Data Download for FIRE_ACE_UTRECHT_BALLOON_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIRE_ACE_UTRECHT_BALLOON_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_ACE_UTRECHT_BALLOON/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_ACE_UTRECHT_BALLOON/contents.html",
-                    "description": "OPeNDAP data access for FIRE_ACE_UTRECHT_BALLOON_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for FIRE_ACE_UTRECHT_BALLOON_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_ACE_UTRECHT_BALLOON/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1000000923-LARC_ASDC",
+            "issued": "2003-06-04",
+            "keyword": [
+                "atmospheric temperature",
+                "atmosphere",
+                "earth science",
+                "atmospheric pressure",
+                "atmospheric winds"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0007",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>75.98 -167.16 75.98 -164.84 76.4 -164.84 76.4 -167.16 75.98 -167.16</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1998-05-02T00:00:00Z/1998-05-25T23:59:59.999Z",
             "theme": [
                 "FIRE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "First ISCCP Regional Experiment - Arctic Cloud Experiment Utrecht University Tethered Balloon"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-PRL-67PCHURYUMOV-M04-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Narrow Angle Camera during the PRELANDING phase of the Rosetta mission, covering the period from 2014-06-04T10:50:00.000 to 2014-07-02T08:34:59.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-prl-67pchuryumov-m04-v1.0_jchk-z4ah",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "beta cen",
                 "fomalhaut",
@@ -966920,39 +966922,39 @@
                 "alpha sco",
                 "beta car"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-PRL-67PCHURYUMOV-M04-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-prl-67pchuryumov-m04-v1.0_jchk-z4ah",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Narrow Angle Camera during the PRELANDING phase of the Rosetta mission, covering the period from 2014-06-04T10:50:00.000 to 2014-07-02T08:34:59.000.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 PRL-MTP004 RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 PRL-MTP004 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-L-APO3.5M_AGILE-2-EDR-LCROSS-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This archive contains observations of the 2009-10-09 impact of the LCROSS spacecraft on the moon by the AGILE instrument on the Apache Point Observatory 3.5m telescope. The archive consists of FITS images of the event and calibration data. This is one of several data sets of Earth-based observations of the impact.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-l-apo3.5m_agile-2-edr-lcross-v1.0_jchn-xg3t",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "bias",
                 "uranus",
@@ -966966,596 +966968,576 @@
                 "68 psc",
                 "1 aurigae"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-L-APO3.5M_AGILE-2-EDR-LCROSS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-l-apo3.5m_agile-2-edr-lcross-v1.0_jchn-xg3t",
-            "description": "This archive contains observations of the 2009-10-09 impact of the LCROSS spacecraft on the moon by the AGILE instrument on the Apache Point Observatory 3.5m telescope. The archive consists of FITS images of the event and calibration data. This is one of several data sets of Earth-based observations of the impact.",
-            "title": "APACHE POINT OBSERVATORY 3.5M AGILE OBSERVATIONS OF LCROSS",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "APACHE POINT OBSERVATORY 3.5M AGILE OBSERVATIONS OF LCROSS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1261-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-15T20:34:05.000 to 2015-12-16T00:16:34.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1261-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1261-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1261-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-15T20:34:05.000 to 2015-12-16T00:16:34.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1261 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1261 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/805",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Thornton, P.E., S.W. Running, and E.R. Hunt. 2005. Biome-BGC: Terrestrial Ecosystem Process Model, Version 4.1.1. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/805",
-            "issued": "2024-04-26",
-            "temporal": "2000-07-05T00:00:00Z/2000-07-05T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-26",
-            "keyword": [
-                "soils",
-                "biosphere",
-                "earth science",
-                "land surface",
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
-            "identifier": "C2954635280-ORNL_CLOUD",
             "description": "Biome-BGC is a computer program that estimates fluxes and storage of energy, water, carbon, and nitrogen for the vegetation and soil components of terrestrial ecosystems. The primary model purpose is to study global and regional interactions between climate, disturbance, and biogeochemical cycles. Biome-BGC represents physical and biological processes that control fluxes of energy and mass. These processes include new leaf growth and old leaf litterfall, sunlight interception by leaves and penetration to the ground, precipitation routing to leaves and soil, snow accumulation and melting, drainage and runoff of soil water, evaporation of water from soil and wet leaves, transpiration of soil water through leaf stomata, photosynthetic fixation of carbon from CO2 in the air, uptake of nitrogen from the soil, distribution of carbon and nitrogen to growing plant parts, decomposition of fresh plant litter and old soil organic matter, plant mortality, and fire. The model uses a daily time-step, meaning that each flux is estimated for a one-day period. Between days, the program updates its memory of the mass stored in different components of the vegetation, litter, and soil. Weather is the most important control on vegetation processes. Flux estimates in Biome-BGC depend strongly on daily weather conditions. Model behavior over time depends on climate--the history of these weather conditions. A companion file with more information about Biome-BGC and its components is available. Biome-BGC, Version 4.1.1, was developed and is maintained by the  Numerical Terradynamic Simulation Group, School of Forestry, the University of Montana, Missoula, Montana, U.S.A.  Additional information can be found on their web site at: http://www.ntsg.umt.edu/.",
-            "graphic-preview-description": "Browse Image",
-            "title": "Biome-BGC: Terrestrial Ecosystem Process Model, Version 4.1.1",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/model-archive_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F805",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F805",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/model_archive/BIOME_BGC_4_1_1/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/model_archive/BIOME_BGC_4_1_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/MODELS/guides/biome-bgc_guide.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/MODELS/guides/biome-bgc_guide.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/805",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/805",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/model_archive/BIOME_BGC_4_1_1/comp/bgc_users_guide_411.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/model_archive/BIOME_BGC_4_1_1/comp/bgc_users_guide_411.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/model_archive/BIOME_BGC_4_1_1/comp/biome-bgc_guide.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/model_archive/BIOME_BGC_4_1_1/comp/biome-bgc_guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/model_archive/BIOME_BGC_4_1_1/comp/BiomeBGC_v411_release.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/model_archive/BIOME_BGC_4_1_1/comp/BiomeBGC_v411_release.pdf",
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
+            "identifier": "C2954635280-ORNL_CLOUD",
+            "issued": "2024-04-26",
+            "keyword": [
+                "soils",
+                "biosphere",
+                "earth science",
+                "land surface",
+                "ecological dynamics"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/805",
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
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-07-05T00:00:00Z/2000-07-05T23:59:59Z",
             "theme": [
                 "Model Archive",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Biome-BGC: Terrestrial Ecosystem Process Model, Version 4.1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQUA/CERES/CRS_AQUA-FM3_L2.002B/C",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2008-09-26. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AQUA/CERES/CRS_AQUA-FM3_L2.002B/C.",
-            "issued": "2014-01-09",
-            "temporal": "2006-05-01T00:00:00Z/2007-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-03-11",
-            "keyword": [
-                "atmosphere",
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "aerosols",
-                "atmospheric radiation",
-                "earth science",
-                "clouds",
-                "atmospheric winds"
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
-            "identifier": "C4331631-LARC_ASDC",
             "description": "CER_CRS_Aqua-FM3-MODIS_Edition2c is the Clouds and the Earth's Radiant Energy System (CERES) Clouds and Radiative Swath (CRS) Aqua-Flight Model 3 (FM3) Moderate-Resolution Imaging Spectroradiometer (MODIS) Edition2C data product, which was collected using the CERES-FM3 instrument on the Aqua platform. Data collection for this product is complete. Note that more recent (2006) CRS Ed2C fields for untuned SW (upper left for all-sky globe and lower right for clear-sky ocean) show a bit more bias than does an average of the earlier (2002-2005) Clouds and Radiative Swath (CRS) Ed2B. CRS Ed2C (Ed2B) biases are evaluated with respect to SSF Ed2C (Ed2B) observations, and those Single Scanner Footprint (SSF) observations do not include recent \"Rev1\" adjustments to observations.\r\n\r\nThe CRS product contains one hour of instantaneous Clouds and the Earth's Radiant Energy System (CERES) data for a single scanner instrument. The CRS contains all of the CERES SSF product data. For each CERES footprint on the SSF, the CRS also contains vertical flux profiles evaluated at four levels in the atmosphere: the surface, 500-, 70-, and 1-hPa. The CRS fluxes and cloud parameters are adjusted for consistency with a radiative transfer model and adjusted fluxes are evaluated at the four atmospheric levels for both clear-sky and total-sky.\r\n\r\nCERES is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions are a follow-on to the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument, protoflight model (PFM), was launched on November 27, 1997 as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the Earth Observing System (EOS) flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board Earth Observing System (EOS) Aqua on May 4, 2002. The CERES FM5 instrument was launched on board the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The newest CERES instrument (FM6) was launched on board the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite, now called NOAA-20, on November 18, 2017.",
-            "title": "CERES Clouds and Radiative Swath Aqua FM3 MODIS Edition2C",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQUA%2FCERES%2FCRS_AQUA-FM3_L2.002B%2FC",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQUA%2FCERES%2FCRS_AQUA-FM3_L2.002B%2FC",
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
-                    "downloadURL": "https://doi.org/10.5067/AQUA/CERES/CRS_AQUA-FM3_L2.002B/C",
-                    "description": "DOI data set landing page for CER_CRS_Aqua-FM3-MODIS_Edition2B/C",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CER_CRS_Aqua-FM3-MODIS_Edition2B/C",
+                    "downloadURL": "https://doi.org/10.5067/AQUA/CERES/CRS_AQUA-FM3_L2.002B/C",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C4331631-LARC_ASDC",
-                    "description": "Earthdata Search for CER_CRS_Aqua-FM3-MODIS_Edition2C (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CER_CRS_Aqua-FM3-MODIS_Edition2C (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C4331631-LARC_ASDC",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/guide/cer_crs.pdf",
-                    "description": "Clouds and the Earth's Radiant Energy System(CERES) Clouds and Radiation Swath (CRS) Data Set Abstract",
                     "@type": "dcat:Distribution",
+                    "description": "Clouds and the Earth's Radiant Energy System(CERES) Clouds and Radiation Swath (CRS) Data Set Abstract",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/guide/cer_crs.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/quality_summaries/CER_CRS_Aqua_Edition2C.pdf",
-                    "description": "Quality Summary: CERES Aqua Edition 2C CRS",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Summary: CERES Aqua Edition 2C CRS",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/quality_summaries/CER_CRS_Aqua_Edition2C.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/DPC_CRS_R5V1.pdf",
-                    "description": "CERES Data Products Catalog R5V1 3/26/2010 Clouds and Radiative Swath (CRS)",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Data Products Catalog R5V1 3/26/2010 Clouds and Radiative Swath (CRS)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/DPC_CRS_R5V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's production history"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/CWG.TELCON.9.01.pdf",
-                    "description": "CERES Cloud Working Group Teleconference ",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Cloud Working Group Teleconference ",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/CWG.TELCON.9.01.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/aqua_rev.pdf",
-                    "description": "CERES Aqua Revision 1 Table ",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Aqua Revision 1 Table ",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/aqua_rev.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/terra_rev.pdf",
-                    "description": "CERES Terra Revision 1 Table",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Terra Revision 1 Table",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/terra_rev.pdf",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/CRS/Aqua-FM3-MODIS_Edition2C/",
-                    "description": "ASDC Direct Data Download for CER_CRS_Aqua-FM3-MODIS_Edition2C",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CER_CRS_Aqua-FM3-MODIS_Edition2C",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/CRS/Aqua-FM3-MODIS_Edition2C/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/CRS/Aqua-FM3-MODIS_Edition2C/contents.html",
-                    "description": "OPeNDAP data access for CER_CRS_Aqua-FM3-MODIS_Edition2C",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CER_CRS_Aqua-FM3-MODIS_Edition2C",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/CRS/Aqua-FM3-MODIS_Edition2C/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C4331631-LARC_ASDC",
+            "issued": "2014-01-09",
+            "keyword": [
+                "atmosphere",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "aerosols",
+                "atmospheric radiation",
+                "earth science",
+                "clouds",
+                "atmospheric winds"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQUA/CERES/CRS_AQUA-FM3_L2.002B/C",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-03-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2006-05-01T00:00:00Z/2007-12-31T23:59:59.999Z",
             "theme": [
                 "CERES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CERES Clouds and Radiative Swath Aqua FM3 MODIS Edition2C"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMAG-3-ESC4-CALIBRATED-V6.0",
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
+            "description": "This dataset contains CALIBRATED (CODMAC LEVEL 3) DATA of the COMET\nESCORT 4 Phase (ESC4)from  October 21, 2015  until January 12, 2016\nof the ROSETTA orbiter magnetometer RPCMAG. Observations are done in\nthe vicinity of comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1).\nThe current version of the dataset is V6.0, the first one\nbeing archived.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmag-3-esc4-calibrated-v6.0_jckd-h3ub",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMAG-3-ESC4-CALIBRATED-V6.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmag-3-esc4-calibrated-v6.0_jckd-h3ub",
-            "description": "This dataset contains CALIBRATED (CODMAC LEVEL 3) DATA of the COMET\nESCORT 4 Phase (ESC4)from  October 21, 2015  until January 12, 2016\nof the ROSETTA orbiter magnetometer RPCMAG. Observations are done in\nthe vicinity of comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1).\nThe current version of the dataset is V6.0, the first one\nbeing archived.",
-            "title": "ROSETTA-ORBITER 67P RPCMAG 3 ESC4 CALIBRATED V6.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCMAG 3 ESC4 CALIBRATED V6.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/jckf-c4dh",
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
-                "wise",
-                "space science",
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
-            "identifier": "NASA-0000038__47",
+            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
             "description": "Planetary nomenclature, like terrestrial nomenclature, is used to uniquely identify a feature on the surface of a planet or satellite so that the feature can be easily located, described, and discussed. This gazetteer contains detailed information about all names of topographic and albedo features on planets and satellites (and some planetary ring and ring-gap systems) that the International Astronomical Union (IAU) has named and approved from its founding in 1919 through the present time.",
-            "title": "Gazetteer of Planetary Nomenclature",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -967563,252 +967545,248 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
-            "accrualPeriodicity": "irregular"
+            "identifier": "NASA-0000038__47",
+            "issued": "2018-06-25",
+            "keyword": [
+                "nen",
+                "wise",
+                "space science",
+                "geography"
+            ],
+            "landingPage": "https://data.nasa.gov/d/jckf-c4dh",
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
-            "landingPage": "https://doi.org/10.5067/CAMEX-4/HYGROMETER/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Herman, Robert L.2002. CAMEX-4 JPL LASER HYGROMETER [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/CAMEX-4/HYGROMETER/DATA101",
-            "issued": "2002-07-12",
-            "temporal": "2001-08-18T18:04:15Z/2001-09-25T03:02:27Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-18",
-            "keyword": [
-                "atmospheric water vapor",
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
-            "identifier": "C1979096272-GHRC_DAAC",
             "description": "The CAMEX-4 JPL Laser Hygrometer dataset contains water vapor volume and mixing ratio concentractions collected during the CAMEX-4 campaign to study tropical cyclones. The Laser Hygrometer measures in situ water vapor content using a tuneable laser emitting at 1.37 microns. Absorption at that wavelength is a function of water vapor content, thus measuring the amount of absorption in an open path beyond the aircraft boundary layer, a value of water vapor pressure is made. The maximum sampling rate is 8 Hz, but the instrument is normally configured through the software for a 1Hz sampling rate.",
-            "title": "CAMEX-4 JPL LASER HYGROMETER V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAMEX-4%2FHYGROMETER%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAMEX-4%2FHYGROMETER%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=c4djlh",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=c4djlh",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/camex4/c4djlh/c4djlh_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/camex4/c4djlh/c4djlh_dataset.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/camex4/c4djlh/TUTORIAL.pdf",
-                    "description": "Format Specification for Data Exchange V1.3 June 18, 1998",
                     "@type": "dcat:Distribution",
+                    "description": "Format Specification for Data Exchange V1.3 June 18, 1998",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/camex4/c4djlh/TUTORIAL.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/camex4/c4djlh/jlh_summary.pdf",
-                    "description": "The JPL Laser Hygrometer in CAMEX-4",
                     "@type": "dcat:Distribution",
+                    "description": "The JPL Laser Hygrometer in CAMEX-4",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/camex4/c4djlh/jlh_summary.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/camex4/c4djlh/JLHfactsheet.doc",
-                    "description": "CAMEX-4 JPL Laser Hygrometer (JLH) Experiment Operations",
                     "@type": "dcat:Distribution",
+                    "description": "CAMEX-4 JPL Laser Hygrometer (JLH) Experiment Operations",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/camex4/c4djlh/JLHfactsheet.doc",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/about-ghrc/citing-ghrc-daac-data",
-                    "description": "Instructions for citing GHRC data",
                     "@type": "dcat:Distribution",
+                    "description": "Instructions for citing GHRC data",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/about-ghrc/citing-ghrc-daac-data",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1979096272-GHRC_DAAC",
+            "issued": "2002-07-12",
+            "keyword": [
+                "atmospheric water vapor",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/CAMEX-4/HYGROMETER/DATA101",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-05-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/MSFC/GHRC"
+            },
             "spatial": "-88.215 16.5317 -58.635 39.71",
+            "temporal": "2001-08-18T18:04:15Z/2001-09-25T03:02:27Z",
             "theme": [
                 "CAMEX-4",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CAMEX-4 JPL LASER HYGROMETER V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-5-ESC1-DERIV2-V1.0",
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
+            "description": "This data set contains DERIVED\ndata from Rosetta RPC-LAP, acquired during the COMET ESCORT 1 mission\nphase where the primary target was the comet 67P/CHURYUMOV-GERASIMENKO 1\n(1969 R1). It contains high-level data products in physical units, such\nas electron density, electron temperature, spacecraft potential, and\ndownsampled time series of current and voltage measurements.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-5-esc1-deriv2-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-5-ESC1-DERIV2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-5-esc1-deriv2-v1.0",
-            "description": "This data set contains DERIVED\ndata from Rosetta RPC-LAP, acquired during the COMET ESCORT 1 mission\nphase where the primary target was the comet 67P/CHURYUMOV-GERASIMENKO 1\n(1969 R1). It contains high-level data products in physical units, such\nas electron density, electron temperature, spacecraft potential, and\ndownsampled time series of current and voltage measurements.",
-            "title": "ROSETTA-ORBITER 67P RPCLAP 5\nESC1 DERIV2 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCLAP 5\nESC1 DERIV2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-DERIVED-LIGHTCURVE-V8.0",
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
+            "description": "This is a compilation of published rotational parameters derived from lightcurve data for asteroids, through March 2006.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-derived-lightcurve-v8.0_jcpp-bew7",
+            "issued": "2021-05-21",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-DERIVED-LIGHTCURVE-V8.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-derived-lightcurve-v8.0_jcpp-bew7",
-            "description": "This is a compilation of published rotational parameters derived from lightcurve data for asteroids, through March 2006.",
-            "title": "ASTEROID LIGHTCURVE DERIVED DATA V8.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ASTEROID LIGHTCURVE DERIVED DATA V8.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-U-PWS-2-RDR-SA-4SEC-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set consists of 4-second edited, wave electric field intensities from the Voyager 2 Plasma Wave Receiver spectrum analyzer obtained in the vicinity of the Uranian magnetosphere. For each 4-second interval, a field strength is determined for each of the 16 spectrum analyzer channels whose center frequencies range from 10 Hertz to 56.2 kiloHertz and which are logarithmically spaced in frequency, four channels per decade. The time associated with each set of intensities (16 channels) is the time of the beginning of the scan. During data gaps where complete 4-second spectra are missing, no entries exist in the file, that is, the gaps are not zero-filled or tagged in any other way. When one or more channels are missing within a scan, the missing measurements are zero-filled. Data are edited but not calibrated. The data numbers in this data set can be plotted in raw form for event searches and simple trend analysis since they are roughly proportional to the log of the electric field strength. Calibration procedures and tables are provided for use with this data set described below.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-u-pws-2-rdr-sa-4sec-v1.0_jcpq-um6h",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "voyager",
                 "uranus",
                 "comet sl9/jupiter collision"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-U-PWS-2-RDR-SA-4SEC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-u-pws-2-rdr-sa-4sec-v1.0_jcpq-um6h",
-            "description": "This data set consists of 4-second edited, wave electric field intensities from the Voyager 2 Plasma Wave Receiver spectrum analyzer obtained in the vicinity of the Uranian magnetosphere. For each 4-second interval, a field strength is determined for each of the 16 spectrum analyzer channels whose center frequencies range from 10 Hertz to 56.2 kiloHertz and which are logarithmically spaced in frequency, four channels per decade. The time associated with each set of intensities (16 channels) is the time of the beginning of the scan. During data gaps where complete 4-second spectra are missing, no entries exist in the file, that is, the gaps are not zero-filled or tagged in any other way. When one or more channels are missing within a scan, the missing measurements are zero-filled. Data are edited but not calibrated. The data numbers in this data set can be plotted in raw form for event searches and simple trend analysis since they are roughly proportional to the log of the electric field strength. Calibration procedures and tables are provided for use with this data set described below.",
-            "title": "VG2 URA PWS EDITED RDR UNCALIB SPECTRUM ANALYZER 4SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG2 URA PWS EDITED RDR UNCALIB SPECTRUM ANALYZER 4SEC V1.0"
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
-                "turbulence",
-                "cases",
-                "models",
-                "flow"
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
-            "identifier": "NASA-844__24",
             "description": "This grouping contains the incompressible-flow cases from the 1980-81 Data Library.",
-            "title": "Collaborative Testing of Turbulence Models: Incompressible Flow Cases from 1980-81 Data Library",
-            "programCode": [
-                "026:023"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -967816,45 +967794,45 @@
                     "mediaType": "application/txt"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-844__24",
+            "issued": "2018-06-25",
+            "keyword": [
+                "incompressible",
+                "turbulence",
+                "cases",
+                "models",
+                "flow"
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
-                "models",
-                "cases",
-                "incompressible",
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
-            "identifier": "NASA-842__27",
             "description": "This grouping contains the incompressible-flow cases from the 1980-81 Data Library.",
-            "title": "Collaborative Testing of Turbulence Models: Incompressible Flow Cases from 1980-81 Data Library",
-            "programCode": [
-                "026:023"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -967862,530 +967840,528 @@
                     "mediaType": "application/txt"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-842__27",
+            "issued": "2018-06-25",
+            "keyword": [
+                "flow",
+                "models",
+                "cases",
+                "incompressible",
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
+            "title": "Collaborative Testing of Turbulence Models: Incompressible Flow Cases from 1980-81 Data Library"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D59.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler\r\n. 2019-11-07. VNP43D59. Version 001. VIIRS/NPP BRDF/Albedo BSA at Solar Noon Band M7 Daily L3 Global 30ArcSec CMG V001\r\n. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VNP43D59.001. https://doi.org/10.5067/VIIRS/VNP43D59.001. Digital Science Data. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
-            "issued": "2019-11-07",
-            "temporal": "2012-01-19T00:00:00Z/2024-05-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-11-07",
-            "keyword": [
-                "earth science",
-                "surface radiative properties",
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
-            "identifier": "C1607335247-LPDAAC_ECS",
-            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Black-Sky Albedo for Band M7 (VNP43D59) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. \r\n\r\nVNP43D54 through VNP43D79 are the albedo products of the VNP43D BRDF/Albedo product suite. Black-sky albedo (BSA) and white-sky albedo (WSA) values are provided for the nine VIIRS moderate resolution bands (M1 through M5, M7, M8, M10, and M11) along with the visible, near-infrared (NIR), and shortwave bands included in the VNP43MA3 (https://doi.org/10.5067/VIIRS/VNP43MA3.001) product. In addition to the bands included in VNP43MA3, this product suite includes albedo values for the VIIRS Day/Night Band (DNB). The black-sky albedo (directional hemispherical reflectance) is defined as albedo in the absence of a diffuse component and is a function of solar zenith angle. White-sky albedo (bihemispherical reflectance) is defined as albedo in the absence of a direct component when the diffuse component is isotropic. Details regarding methodology are available on the VNP43MA3 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D59 is the BSA for VIIRS band M7 (0.865 \u03bcm).",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "VNP43D59",
             "creator": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler",
-            "title": "VIIRS/NPP BRDF/Albedo BSA at Solar Noon Band M7 Daily L3 Global 30ArcSec CMG V001",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Black-Sky Albedo for Band M7 (VNP43D59) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. \r\n\r\nVNP43D54 through VNP43D79 are the albedo products of the VNP43D BRDF/Albedo product suite. Black-sky albedo (BSA) and white-sky albedo (WSA) values are provided for the nine VIIRS moderate resolution bands (M1 through M5, M7, M8, M10, and M11) along with the visible, near-infrared (NIR), and shortwave bands included in the VNP43MA3 (https://doi.org/10.5067/VIIRS/VNP43MA3.001) product. In addition to the bands included in VNP43MA3, this product suite includes albedo values for the VIIRS Day/Night Band (DNB). The black-sky albedo (directional hemispherical reflectance) is defined as albedo in the absence of a diffuse component and is a function of solar zenith angle. White-sky albedo (bihemispherical reflectance) is defined as albedo in the absence of a direct component when the diffuse component is isotropic. Details regarding methodology are available on the VNP43MA3 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D59 is the BSA for VIIRS band M7 (0.865 \u03bcm).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D59.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D59.001",
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
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D59.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D59.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/xhdf5",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D59.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D59.001/",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607335247-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607335247-LPDAAC_ECS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D59.001/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D59.001/contents.html",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D59",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D59",
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
+            "identifier": "C1607335247-LPDAAC_ECS",
+            "issued": "2019-11-07",
+            "keyword": [
+                "earth science",
+                "surface radiative properties",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D59.001",
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
+            "series-name": "VNP43D59",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-19T00:00:00Z/2024-05-27T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP BRDF/Albedo BSA at Solar Noon Band M7 Daily L3 Global 30ArcSec CMG V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/4XXOGX0OOW1S",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMAP L3 Radiometer Global Daily 36 km EASE-Grid Soil Moisture V009. Version 009. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/4XXOGX0OOW1S.",
-            "issued": "2015-03-31",
-            "temporal": "2015-03-31T00:00:00Z/2025-01-13T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-08",
-            "keyword": [
-                "land surface",
-                "spectral/engineering",
-                "earth science",
-                "soils",
-                "microwave"
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
-            "identifier": "C2938664585-NSIDC_CPRD",
             "description": "This Level-3 (L3) soil moisture product provides a composite of daily estimates of global land surface conditions retrieved by the Soil Moisture Active Passive (SMAP) passive microwave radiometer. SMAP L-band soil moisture data are resampled to a global, cylindrical 36 km Equal-Area Scalable Earth Grid, Version 2.0 (EASE-Grid 2.0).",
-            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
-            "title": "SMAP L3 Radiometer Global Daily 36 km EASE-Grid Soil Moisture V009",
-            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?v=-193,-69,134,83&l=SMAP_L3_Passive_Brightness_Temp_V,SMAP_L3_Passive_Day_Soil_Moisture,SMAP_L3_Passive_Night_Soil_Moisture,SMAP_L3_Passive_Brightness_Temp_H,Coastlines_15m,MODIS_Terra_CorrectedReflectance_TrueColor&t=2015-03-31",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F4XXOGX0OOW1S",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F4XXOGX0OOW1S",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SPL3SMP+V009",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SPL3SMP+V009",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2938664585-NSIDC_CPRD",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2938664585-NSIDC_CPRD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://worldview.earthdata.nasa.gov/?v=-193%2C-69%2C134%2C83&l=SMAP_L3_Passive_Brightness_Temp_V%2CSMAP_L3_Passive_Day_Soil_Moisture%2CSMAP_L3_Passive_Night_Soil_Moisture%2CSMAP_L3_Passive_Brightness_Temp_H%2CCoastlines_15m%2CMODIS_Terra_CorrectedReflectance_TrueColor&t=2015-03-31",
-                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
                     "@type": "dcat:Distribution",
+                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+                    "downloadURL": "https://worldview.earthdata.nasa.gov/?v=-193%2C-69%2C134%2C83&l=SMAP_L3_Passive_Brightness_Temp_V%2CSMAP_L3_Passive_Day_Soil_Moisture%2CSMAP_L3_Passive_Night_Soil_Moisture%2CSMAP_L3_Passive_Brightness_Temp_H%2CCoastlines_15m%2CMODIS_Terra_CorrectedReflectance_TrueColor&t=2015-03-31",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through WORLDVIEW"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/4XXOGX0OOW1S",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/4XXOGX0OOW1S",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/4XXOGX0OOW1S",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/4XXOGX0OOW1S",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?v=-193,-69,134,83&l=SMAP_L3_Passive_Brightness_Temp_V,SMAP_L3_Passive_Day_Soil_Moisture,SMAP_L3_Passive_Night_Soil_Moisture,SMAP_L3_Passive_Brightness_Temp_H,Coastlines_15m,MODIS_Terra_CorrectedReflectance_TrueColor&t=2015-03-31",
+            "identifier": "C2938664585-NSIDC_CPRD",
+            "issued": "2015-03-31",
+            "keyword": [
+                "land surface",
+                "spectral/engineering",
+                "earth science",
+                "soils",
+                "microwave"
+            ],
+            "landingPage": "https://doi.org/10.5067/4XXOGX0OOW1S",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-08",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -85.044 180.0 85.044",
+            "temporal": "2015-03-31T00:00:00Z/2025-01-13T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMAP L3 Radiometer Global Daily 36 km EASE-Grid Soil Moisture V009"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQR50-3RRCS",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA Aquarius project. 2017-12-07. Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image 28-Day Running Mean Data. Version 5.0. Aquarius Sea Surface Salinity Products. Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC OBPG. https://doi.org/10.5067/AQR50-3RRCS. http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius. NASA Aquarius project, NASA/GSFC OBPG, 2017-12-07, Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image 28-Day Running Mean Data V5.0, http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius.",
-            "issued": "2017-10-21",
-            "temporal": "2011-08-25T01:55:23Z/2015-06-07T12:45:21Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-07",
-            "keyword": [
-                "oceans",
-                "ocean temperature",
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
-            "identifier": "C2491742792-POCLOUD",
-            "description": "Aquarius Level 3 ancillary sea surface temperature (SST) standard mapped image data are the ancillary SST data used in the Aquarius calibration for salinity retrieval.  They are simply the daily SSTs from the Reynolds National Climatic Data Center (NCDC) 0.25 degree dataset, gridded and averaged using the Aquarius processing L2-L3 processing scheme to the same 1 degree spatial resolution and daily, 7 day, monthly, 7-Day, and annual time intervals as Aquarius L3 standard salinity and wind speed products.  This particular data set is the 28-Day running mean, ancillary sea surface temperature product associated with version 5.0  of the Aquarius data set, which is the official end of mission public data release from the AQUARIUS/SAC-D mission.",
-            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA",
-            "series-name": "Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image 28-Day Running Mean Data",
-            "graphic-preview-description": "Thumbnail",
             "creator": "NASA Aquarius project",
-            "title": "Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image 28-Day Running Mean Data V5.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_ANCILLARY_SST_SMI_28DAY-RUNNINGMEAN_V5.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Aquarius Level 3 ancillary sea surface temperature (SST) standard mapped image data are the ancillary SST data used in the Aquarius calibration for salinity retrieval.  They are simply the daily SSTs from the Reynolds National Climatic Data Center (NCDC) 0.25 degree dataset, gridded and averaged using the Aquarius processing L2-L3 processing scheme to the same 1 degree spatial resolution and daily, 7 day, monthly, 7-Day, and annual time intervals as Aquarius L3 standard salinity and wind speed products.  This particular data set is the 28-Day running mean, ancillary sea surface temperature product associated with version 5.0  of the Aquarius data set, which is the official end of mission public data release from the AQUARIUS/SAC-D mission.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3RRCS",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3RRCS",
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
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_ANCILLARY_SST_SMI_28DAY-RUNNINGMEAN_V5.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_ANCILLARY_SST_SMI_28DAY-RUNNINGMEAN_V5.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491742792-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491742792-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491742792-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491742792-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_ANCILLARY_SST_SMI_28DAY-RUNNINGMEAN_V5.jpg",
+            "identifier": "C2491742792-POCLOUD",
+            "issued": "2017-10-21",
+            "keyword": [
+                "oceans",
+                "ocean temperature",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQR50-3RRCS",
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
+            "series-name": "Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image 28-Day Running Mean Data",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T01:55:23Z/2015-06-07T12:45:21Z",
             "theme": [
                 "AQUARIUS SAC-D",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image 28-Day Running Mean Data V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1273652205-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Flynn, Lawrence E., et al.. 2004-06-01. SBUV2N09O3. Version 008. SBUV2/NOAA-9 Level 2 Daily Ozone Profile and Total Column from CD-ROM V008. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/SBUV2N09O3_008.html. Digital Science Data.",
-            "issued": "1985-02-02",
-            "temporal": "1985-02-02T00:00:00Z/1998-02-19T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1998-02-19",
-            "keyword": [
-                "aerosols",
-                "earth science",
-                "atmospheric radiation",
-                "atmosphere",
-                "atmospheric chemistry"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "LARRY FLYNN, PH. D",
                 "hasEmail": "mailto:Lawrence.E.Flynn@noaa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1273652205-GES_DISC",
-            "description": "The version 8 SBUV/2 NOAA-9 ozone data were first released at the 2004 Quadrennial Ozone Symposium on DVD. The DVD contained all of the SBUV/2 data from NOAA-9, NOAA-11 and NOAA-16 satellites as well as SBUV data from the Nimbus-7 satellite. The DVD is no longer available, however all the data are available on-line from the NASA GES DISC. The NOAA-9 SBUV/2 v8 data are available in two time periods from 1985-02-02 to 1989-12-31 (ascending orbits) and again from 1992-01-01 to 1998-02-19 (descending orbits) due to the drift of the NOAA-9 satellite. The instrument spatial resolution is 180 km x 180 km footprint at nadir. The ozone profiles are made at 21 pressure levels between 1000 and 0.1 hPa. Each data file contains a days worth of ozone measurements, and is written in an ASCII text format.\n\nThe SBUV/2 is a scanning double monochromator and a cloud cover radiometer (CCR) designed to measure ultraviolet (UV) spectral intensities. In its primary mode of operation, the monochromator measures solar radiation backscattered by the atmosphere in 12 discrete wavelength bands in the near-UV, ranging from 252.0 to 339.8 nanometers, each with a bandpass of 1.1 nm. The total-ozone algorithm uses the four longest wavelength bands (312.5, 317.5, 331.2 and 339.8 nm), whereas the profiling algorithm uses the shorter wavelengths. The cloud cover radiometer operates at 379 nm (i.e., outside the ozone absorption band) with a 3.0 nm bandpass and was designed to measure the reflectivity of the surface in the IFOV. The SBUV/2 also makes periodic measurements of the solar flux by deploying a diffuser plate into the FOV to reflect sunlight into the measurement.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "SBUV2N09O3",
             "creator": "Flynn, Lawrence E., et al.",
-            "title": "SBUV2/NOAA-9 Level 2 Daily Ozone Profile and Total Column from CD-ROM V008 (SBUV2N09O3) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SBUV2N09O3_008.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The version 8 SBUV/2 NOAA-9 ozone data were first released at the 2004 Quadrennial Ozone Symposium on DVD. The DVD contained all of the SBUV/2 data from NOAA-9, NOAA-11 and NOAA-16 satellites as well as SBUV data from the Nimbus-7 satellite. The DVD is no longer available, however all the data are available on-line from the NASA GES DISC. The NOAA-9 SBUV/2 v8 data are available in two time periods from 1985-02-02 to 1989-12-31 (ascending orbits) and again from 1992-01-01 to 1998-02-19 (descending orbits) due to the drift of the NOAA-9 satellite. The instrument spatial resolution is 180 km x 180 km footprint at nadir. The ozone profiles are made at 21 pressure levels between 1000 and 0.1 hPa. Each data file contains a days worth of ozone measurements, and is written in an ASCII text format.\n\nThe SBUV/2 is a scanning double monochromator and a cloud cover radiometer (CCR) designed to measure ultraviolet (UV) spectral intensities. In its primary mode of operation, the monochromator measures solar radiation backscattered by the atmosphere in 12 discrete wavelength bands in the near-UV, ranging from 252.0 to 339.8 nanometers, each with a bandpass of 1.1 nm. The total-ozone algorithm uses the four longest wavelength bands (312.5, 317.5, 331.2 and 339.8 nm), whereas the profiling algorithm uses the shorter wavelengths. The cloud cover radiometer operates at 379 nm (i.e., outside the ozone absorption band) with a 3.0 nm bandpass and was designed to measure the reflectivity of the surface in the IFOV. The SBUV/2 also makes periodic measurements of the solar flux by deploying a diffuser plate into the FOV to reflect sunlight into the measurement.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -968394,449 +968370,455 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SBUV2N09O3_008.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SBUV2N09O3_008.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/NOAA_SBUV2_Level2/SBUV2N09O3.008/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/NOAA_SBUV2_Level2/SBUV2N09O3.008/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SBUV2N09O3",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SBUV2N09O3",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.star.nesdis.noaa.gov/smcd/spb/ozone/",
-                    "description": "NOAA NESDIS SBUV/2 web site",
                     "@type": "dcat:Distribution",
+                    "description": "NOAA NESDIS SBUV/2 web site",
+                    "downloadURL": "https://www.star.nesdis.noaa.gov/smcd/spb/ozone/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SBUV2N09O3_008.png",
+            "identifier": "C1273652205-GES_DISC",
+            "issued": "1985-02-02",
+            "keyword": [
+                "aerosols",
+                "earth science",
+                "atmospheric radiation",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1273652205-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1998-02-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "SBUV2N09O3",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1985-02-02T00:00:00Z/1998-02-19T23:59:59.999Z",
             "theme": [
                 "POES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SBUV2/NOAA-9 Level 2 Daily Ozone Profile and Total Column from CD-ROM V008 (SBUV2N09O3) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/913",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Selva, E.C., E.G. Couto, M.S. Johnson, and J. Lehmann. 2009. LBA-ECO ND-11 Organic Carbon Watershed Exports, Mato Grosso, Brazil: 2003-2004. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/913",
-            "issued": "2023-10-03",
-            "temporal": "2003-09-15T00:00:00Z/2004-09-13T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-04",
-            "keyword": [
-                "terrestrial hydrosphere",
-                "water quality/water chemistry",
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
-            "identifier": "C2777410780-ORNL_CLOUD",
             "description": "This data set contains stream water exports of coarse particulate organic matter (CPOM) and coarse particulate organic carbon (CPOC) during 2003-2004 from four forested headwater streams near Juruena, Mato Grosso, Brazil (Selva et al. (2007) and Johnson et al. (2006) . Data are reported in a single comma-separated ASCII  file as watershed exports in mass units, carbon content, and watershed exports per watershed area over the reported sampling intervals.Resolving the carbon balance in the Amazonian forest depends on an improved quantification of production and losses of particulate C from forested landscapes via stream export. The export of coarse organic particulate matter (>2 mm) was quantified for one year in four small watersheds (1-2 ha) under native forest in southern Amazonia near Juruena, Mato Grosso, Brazil. Stream-water exports of particulate C were positively correlated with stream flow, increasing in the rainiest months. The export of particulate C in stream flow was found to be a small (less than 1%) percentage of the amount of litterfall produced.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO ND-11 Organic Carbon Watershed Exports, Mato Grosso, Brazil: 2003-2004",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F913",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F913",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/nutrient_dynamics/ND11_Carbon_Export_CPOM/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/nutrient_dynamics/ND11_Carbon_Export_CPOM/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/ND11_Carbon_Export_CPOM.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/ND11_Carbon_Export_CPOM.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/913",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/913",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/nutrient_dynamics/ND11_Carbon_Export_CPOM/comp/ND11_Carbon_Export_CPOM.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/nutrient_dynamics/ND11_Carbon_Export_CPOM/comp/ND11_Carbon_Export_CPOM.pdf",
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
-            "spatial": "-10.42 -58.76",
-            "theme": [
-                "LBA-ECO",
-                "geospatial"
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
+            "identifier": "C2777410780-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "terrestrial hydrosphere",
+                "water quality/water chemistry",
+                "earth science"
             ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/913",
             "language": [
                 "en-US"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1060-V1.0",
-            "bureauCode": [
-                "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
+            "modified": "2023-10-04",
+            "programCode": [
+                "026:001"
             ],
-            "keyword": [
-                "67p/churyumov-gerasimenko 1 (1969 r1)",
-                "international rosetta mission"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
+            "spatial": "-10.42 -58.76",
+            "temporal": "2003-09-15T00:00:00Z/2004-09-13T23:59:59Z",
+            "theme": [
+                "LBA-ECO",
+                "geospatial"
+            ],
+            "title": "LBA-ECO ND-11 Organic Carbon Watershed Exports, Mato Grosso, Brazil: 2003-2004"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "026:00"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-09-26T21:05:10.000 to 2015-09-27T05:25:05.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1060-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1060-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1060-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-09-26T21:05:10.000 to 2015-09-27T05:25:05.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1060 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1060 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGN-V-RDRS-5-MIDR-C3-V1.0",
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
-                "venus",
-                "magellan"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains the Magellan Compressed Thrice Mosaicked Image Data Records (C3-MIDRs) which consists of mosaics generated by computing 3x3 pixel arithmetic moving averages from the C2-MIDRs. Each C3-MIDR is in a sinusoidal equal area projection and has an origin at 0 degrees latitude, with the central meridian defined as the longitude bisecting the mosaic. Each C1-MIDR has 7168 lines (aligned with latitudes) and 8192 samples, arranged as 56 1024 x 1024 files on CD-ROM. C3-MIDRs, with their 2.025 km pixel widths, are designed to cover the planet at reasonably high resolution and high signal to noise ratio. The 1024 x 1024 files have a VICAR2 format, with embedded VICAR2 labels. The data have been placed on CD-ROMs with documentation, detached Planetary Data System labels, and summary tabular information.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgn-v-rdrs-5-midr-c3-v1.0_jcy8-4mb7",
+            "issued": "2018-06-26",
+            "keyword": [
+                "venus",
+                "magellan"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGN-V-RDRS-5-MIDR-C3-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgn-v-rdrs-5-midr-c3-v1.0_jcy8-4mb7",
-            "description": "This data set contains the Magellan Compressed Thrice Mosaicked Image Data Records (C3-MIDRs) which consists of mosaics generated by computing 3x3 pixel arithmetic moving averages from the C2-MIDRs. Each C3-MIDR is in a sinusoidal equal area projection and has an origin at 0 degrees latitude, with the central meridian defined as the longitude bisecting the mosaic. Each C1-MIDR has 7168 lines (aligned with latitudes) and 8192 samples, arranged as 56 1024 x 1024 files on CD-ROM. C3-MIDRs, with their 2.025 km pixel widths, are designed to cover the planet at reasonably high resolution and high signal to noise ratio. The 1024 x 1024 files have a VICAR2 format, with embedded VICAR2 labels. The data have been placed on CD-ROMs with documentation, detached Planetary Data System labels, and summary tabular information.",
-            "title": "MGN V RADAR SYSTEM DERIVED MIDR COMPRESSED THRICE V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MGN V RADAR SYSTEM DERIVED MIDR COMPRESSED THRICE V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/LAMONT_SCS/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/LAMONT_SCS/DATA001.",
-            "issued": "2016-06-04",
-            "temporal": "2016-06-04T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "salinity/density",
-                "ocean chemistry",
-                "oceans",
-                "ocean temperature",
-                "ocean optics",
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
-            "identifier": "C1633360425-OB_DAAC",
             "description": "Measurements from the South China Sea (SCS) made by researchers at Columbia University's Lamont-Doherty Earth Observatory (LDEO).",
-            "title": "Lamont-Doherty Earth Observatory measurements from the South China Sea (SCS)",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FLAMONT_SCS%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FLAMONT_SCS%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/LAMONT_SCS/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/LAMONT_SCS/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360425-OB_DAAC",
+            "issued": "2016-06-04",
+            "keyword": [
+                "salinity/density",
+                "ocean chemistry",
+                "oceans",
+                "ocean temperature",
+                "ocean optics",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/LAMONT_SCS/DATA001",
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
+            "temporal": "2016-06-04T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Lamont-Doherty Earth Observatory measurements from the South China Sea (SCS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SWOT-LAKESP-2.0",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Surface Water Ocean Topography (SWOT). 2024-02-01. SWOT Level 2 Lake Single-Pass Vector Unassigned Data Product. Version 2.0. SWOT Level 2 Lake Single-Pass Vector Unassigned Data Product, Version 2.0. Jet Propulsion Laboratory. Archived by National Aeronautics and Space Administration, U.S. Government, JPL NASA. https://doi.org/10.5067/SWOT-LAKESP-2.0. https://swot.jpl.nasa.gov/.",
-            "issued": "2022-07-20",
-            "temporal": "2022-12-16T00:00:00Z/2024-03-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-07-20",
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
-            "identifier": "C2799438254-POCLOUD",
-            "description": "The SWOT Level 2 Lake Single-Pass Vector Unassigned Data Product from the Surface Water Ocean Topography (SWOT) mission provides water surface elevation, area, storage change derived from the high rate (HR) data stream from the Ka-band Radar Interferometer (KaRIn). SWOT launched on December 16, 2022 from Vandenberg Air Force Base in California into a 1-day repeat orbit for the \"calibration\" or \"fast-sampling\" phase of the mission, which completed in early July 2023. After the calibration phase, SWOT entered a 21-day repeat orbit in August 2023 to start the \"science\" phase of the mission, which is expected to continue through 2025. <br> Water surface elevation, area, and storage change are provided in three feature datasets covering the full swath for each continent-pass: 1) an observation-oriented feature dataset of lakes identified in the prior lake database (PLD), 2) a feature dataset of lakes identified in the PLD, and 3) a feature dataset containing unassigned features (i.e., not identified in PLD nor prior river database (PRD)). These data are generally produced for inland and coastal hydrology surfaces, as controlled by the reloadable KaRIn HR mask. The dataset is distributed in ESRI Shapefile format. <br> This collection is a sub-collection of its parent: https://podaac.jpl.nasa.gov/dataset/SWOT_L2_HR_LakeSP_2.0 It contains feature datasets of unassigned water features that were not identified in the PLD or PRD.",
-            "release-place": "Jet Propulsion Laboratory",
-            "series-name": "SWOT Level 2 Lake Single-Pass Vector Unassigned Data Product",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Surface Water Ocean Topography (SWOT)",
-            "title": "SWOT Level 2 Lake Single-Pass Vector Unassigned Data Product, Version 2.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_HR_LakeSP_2.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The SWOT Level 2 Lake Single-Pass Vector Unassigned Data Product from the Surface Water Ocean Topography (SWOT) mission provides water surface elevation, area, storage change derived from the high rate (HR) data stream from the Ka-band Radar Interferometer (KaRIn). SWOT launched on December 16, 2022 from Vandenberg Air Force Base in California into a 1-day repeat orbit for the \"calibration\" or \"fast-sampling\" phase of the mission, which completed in early July 2023. After the calibration phase, SWOT entered a 21-day repeat orbit in August 2023 to start the \"science\" phase of the mission, which is expected to continue through 2025. <br> Water surface elevation, area, and storage change are provided in three feature datasets covering the full swath for each continent-pass: 1) an observation-oriented feature dataset of lakes identified in the prior lake database (PLD), 2) a feature dataset of lakes identified in the PLD, and 3) a feature dataset containing unassigned features (i.e., not identified in PLD nor prior river database (PRD)). These data are generally produced for inland and coastal hydrology surfaces, as controlled by the reloadable KaRIn HR mask. The dataset is distributed in ESRI Shapefile format. <br> This collection is a sub-collection of its parent: https://podaac.jpl.nasa.gov/dataset/SWOT_L2_HR_LakeSP_2.0 It contains feature datasets of unassigned water features that were not identified in the PLD or PRD.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSWOT-LAKESP-2.0",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSWOT-LAKESP-2.0",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2799438254-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2799438254-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2799438254-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2799438254-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_HR_LakeSP_2.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_HR_LakeSP_2.0.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/swot_mission_docs/pdd/SWOT-TN-CDM-0673-CNES_Product_Description_L2_HR_LakeSP_20231208_RevB_signed.pdf",
-                    "description": "Product Description Document (PDD)",
                     "@type": "dcat:Distribution",
+                    "description": "Product Description Document (PDD)",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/swot_mission_docs/pdd/SWOT-TN-CDM-0673-CNES_Product_Description_L2_HR_LakeSP_20231208_RevB_signed.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/swot_mission_docs/atbd/SWOT-NT-CDM-1753-CNES_ATBD_LakeSP_20230726_Initial_w-sigs.pdf",
-                    "description": "Algorithm Theoretical Basis Document (ATBD)",
                     "@type": "dcat:Distribution",
+                    "description": "Algorithm Theoretical Basis Document (ATBD)",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/swot_mission_docs/atbd/SWOT-NT-CDM-1753-CNES_ATBD_LakeSP_20230726_Initial_w-sigs.pdf",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2799438254-POCLOUD&pg%5B0%5D%5Bid%5D=*PIC0*",
-                    "description": "Search Granules from Forward Processing (PIC0)",
                     "@type": "dcat:Distribution",
+                    "description": "Search Granules from Forward Processing (PIC0)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2799438254-POCLOUD&pg%5B0%5D%5Bid%5D=*PIC0*",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2799438254-POCLOUD&pg%5B0%5D%5Bid%5D=*PGC0*",
-                    "description": "Search Granules from Bulk Reprocessing (PGC0)",
                     "@type": "dcat:Distribution",
+                    "description": "Search Granules from Bulk Reprocessing (PGC0)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2799438254-POCLOUD&pg%5B0%5D%5Bid%5D=*PGC0*",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_HR_LakeSP_2.0.jpg",
+            "identifier": "C2799438254-POCLOUD",
+            "issued": "2022-07-20",
+            "keyword": [
+                "terrestrial hydrosphere",
+                "surface water",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SWOT-LAKESP-2.0",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-07-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "Jet Propulsion Laboratory",
+            "series-name": "SWOT Level 2 Lake Single-Pass Vector Unassigned Data Product",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2022-12-16T00:00:00Z/2024-03-27T00:00:00Z",
             "theme": [
                 "SWOT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SWOT Level 2 Lake Single-Pass Vector Unassigned Data Product, Version 2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/jd5f-rvnx",
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
-                "space science",
-                "wise",
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
-            "identifier": "NASA-0000038__71",
+            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
             "description": "Planetary nomenclature, like terrestrial nomenclature, is used to uniquely identify a feature on the surface of a planet or satellite so that the feature can be easily located, described, and discussed. This gazetteer contains detailed information about all names of topographic and albedo features on planets and satellites (and some planetary ring and ring-gap systems) that the International Astronomical Union (IAU) has named and approved from its founding in 1919 through the present time.",
-            "title": "Gazetteer of Planetary Nomenclature",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -968844,21 +968826,49 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
-            "accrualPeriodicity": "irregular"
+            "identifier": "NASA-0000038__71",
+            "issued": "2018-06-25",
+            "keyword": [
+                "nen",
+                "space science",
+                "wise",
+                "geography"
+            ],
+            "landingPage": "https://data.nasa.gov/d/jd5f-rvnx",
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
-            "landingPage": "https://github.com/nasa/concept-tagging-api",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2020-06-15",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "references": [
-                "https://github.com/nasa/concept-tagging-api"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Anthony Buonomo",
+                "hasEmail": "mailto:anthony.r.buonomo@nasa.gov"
+            },
+            "description": "Keyword models for a subset of the NASA Thesaurus (https://www.sti.nasa.gov/nasa-thesaurus/). These models were trained on the NASA Technical Reports Server (NTRS). These models can be used with the concept-tagging-api flask server (https://github.com/nasa/concept-tagging-api) to run a keyword predicting service.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "10/23/2019",
+                    "downloadURL": "https://data.nasa.gov/docs/datasets/public/concept_tagging_models/10_23_2019.zip",
+                    "mediaType": "application/zip",
+                    "title": "Concept Tagging Models"
+                }
             ],
+            "identifier": "https://data.nasa.gov/api/views/jd6d-mr3p",
+            "issued": "2020-06-15",
             "keyword": [
                 "keyword tagging",
                 "information retrieval",
@@ -968869,401 +968879,393 @@
                 "metadata management",
                 "machine-learning"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Anthony Buonomo",
-                "hasEmail": "mailto:anthony.r.buonomo@nasa.gov"
-            },
+            "landingPage": "https://github.com/nasa/concept-tagging-api",
+            "modified": "2023-01-31",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "NASA"
             },
-            "identifier": "https://data.nasa.gov/api/views/jd6d-mr3p",
-            "description": "Keyword models for a subset of the NASA Thesaurus (https://www.sti.nasa.gov/nasa-thesaurus/). These models were trained on the NASA Technical Reports Server (NTRS). These models can be used with the concept-tagging-api flask server (https://github.com/nasa/concept-tagging-api) to run a keyword predicting service.",
-            "title": "STI Tagging Models",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.nasa.gov/docs/datasets/public/concept_tagging_models/10_23_2019.zip",
-                    "description": "10/23/2019",
-                    "@type": "dcat:Distribution",
-                    "title": "Concept Tagging Models"
-                }
+            "references": [
+                "https://github.com/nasa/concept-tagging-api"
             ],
             "theme": [
                 "Software"
-            ]
+            ],
+            "title": "STI Tagging Models"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-PRL-67PCHURYUMOV-M05-V2.0",
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
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-07-02T08:35:00.000 to 2014-08-01T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-prl-67pchuryumov-m05-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-PRL-67PCHURYUMOV-M05-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-prl-67pchuryumov-m05-v2.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-07-02T08:35:00.000 to 2014-08-01T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 PRL-MTP005 RDR V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 PRL-MTP005 RDR V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2019",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hook, S.J., J.S. Myers, K.J. Thome, M. Fitzgerald, A.B. Kahle,  Airborne Sensor Facility NASA Ames Research Center, G. McFarquhar, and S.E. Platnick. 2022. MASTER: Cloud And Land Surface Interaction Campaign, California-Oklahoma, 2007. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2019",
-            "issued": "2023-06-29",
-            "temporal": "2007-09-20T17:20:20Z/2007-09-21T21:01:05Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-13",
-            "keyword": [
-                "infrared wavelengths",
-                "visible wavelengths",
-                "surface thermal properties",
-                "surface radiative properties",
-                "spectral/engineering",
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
-            "identifier": "C2731719877-ORNL_CLOUD",
             "description": "This dataset includes Level 1B (L1B) and Level 2 (L2) data products from the MODIS/ASTER Airborne Simulator (MASTER) instrument. The spectral data were collected during two flights aboard a NASA ER-2 aircraft over California, Arizona, New Mexico, Texas, and Oklahoma, U.S., from 2007-09-20 to 2007-09-21. This data collection supported the Cloud And Land Surface Interaction Campaign (CLASIC), a cross-disciplinary interagency research effort to study cumulus convection as an important component in the atmospheric radiation budget and hydrologic cycle of the Southern Great Plains (SGP). Data products include L1B georeferenced multispectral imagery of calibrated radiance in 50 bands covering wavelengths of 0.460 to 12.879 micrometers at approximately 50-meter spatial resolution. Derived L2 data products are emissivity in 5 bands in thermal infrared range (8.58 to 12.13 micrometers) and land surface temperature. The L1B file format is HDF-4, and L2 products are provided in ENVI and KMZ formats. In addition, the dataset includes flight paths, spectral band information, instrument configuration, ancillary notes, and summary information for each flight, and browse images derived from each L1B data file.",
-            "graphic-preview-description": "Single-band images and a RGB composite image from flight track 20 acquired on 21 September 2007 over western Arizona, U.S. Source: MASTERL1B_0793800_20_20070921_2058_2101_V02.jpg",
-            "title": "MASTER: Cloud And Land Surface Interaction Campaign, California-Oklahoma, 2007",
-            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_CLASIC_2007_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2019",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2019",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/master/MASTER_CLASIC_2007/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/master/MASTER_CLASIC_2007/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_CLASIC_2007.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_CLASIC_2007.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2019",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2019",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_CLASIC_2007/comp/MASTER_CLASIC_2007.pdf",
-                    "description": "MASTER: Cloud And Land Surface Interaction Campaign, California-Oklahoma, 2007: MASTER_CLASIC_2007.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "MASTER: Cloud And Land Surface Interaction Campaign, California-Oklahoma, 2007: MASTER_CLASIC_2007.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_CLASIC_2007/comp/MASTER_CLASIC_2007.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_CLASIC_2007_Fig1.jpg",
-                    "description": "Single-band images and a RGB composite image from flight track 20 acquired on 21 September 2007 over western Arizona, U.S. Source: MASTERL1B_0793800_20_20070921_2058_2101_V02.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Single-band images and a RGB composite image from flight track 20 acquired on 21 September 2007 over western Arizona, U.S. Source: MASTERL1B_0793800_20_20070921_2058_2101_V02.jpg",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_CLASIC_2007_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Single-band images and a RGB composite image from flight track 20 acquired on 21 September 2007 over western Arizona, U.S. Source: MASTERL1B_0793800_20_20070921_2058_2101_V02.jpg",
+            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_CLASIC_2007_Fig1.jpg",
+            "identifier": "C2731719877-ORNL_CLOUD",
+            "issued": "2023-06-29",
+            "keyword": [
+                "infrared wavelengths",
+                "visible wavelengths",
+                "surface thermal properties",
+                "surface radiative properties",
+                "spectral/engineering",
+                "land surface",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2019",
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
             "spatial": "-120.94 34.39 -95.44 40.98",
+            "temporal": "2007-09-20T17:20:20Z/2007-09-21T21:01:05Z",
             "theme": [
                 "MASTER",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MASTER: Cloud And Land Surface Interaction Campaign, California-Oklahoma, 2007"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=JNO-J-JIRAM-2-EDR-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This dataset contains the                scientific telemetry produced by the JIRAM                 instrument after editing for duplicated and                corrupted packets, together with geometric                 information computed on ground to locate                   observations in space and time.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.jno-j-jiram-2-edr-v1.0_jd9q-wxbh",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "callisto",
                 "io",
                 "juno",
                 "jupiter"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=JNO-J-JIRAM-2-EDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.jno-j-jiram-2-edr-v1.0_jd9q-wxbh",
-            "description": "This dataset contains the                scientific telemetry produced by the JIRAM                 instrument after editing for duplicated and                corrupted packets, together with geometric                 information computed on ground to locate                   observations in space and time.",
-            "title": "JUNO JUPITER JIRAM EXPERIMENT           \n               DATA RECORD V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "JUNO JUPITER JIRAM EXPERIMENT           \n               DATA RECORD V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4N014G5",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "International Union for Conservation of Nature - IUCN, and Center for International Earth Science Information Network - CIESIN - Columbia University. 2015-12-31. Gridded Species Distribution: Global Mammal Richness Grids, 2015 Release. Version 2015.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H4N014G5. https://doi.org/10.7927/H4N014G5.",
-            "issued": "2015-12-31",
-            "temporal": "2013-01-01T00:00:00Z/2013-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-12-31",
-            "references": [
-                "https://doi.org/10.7927/H4RR1W66"
-            ],
-            "keyword": [
-                "biological classification",
-                "earth science",
-                "animals/vertebrates"
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
-            "identifier": "C1399957348-SEDAC",
-            "description": "The 2015 Release of the Global Mammal Richness Grids data set of the Gridded Species Distribution collection are aggregations of the presence grids data for the entire class, individual  families, and International Union for the Conservation of Nature (IUCN) Red List status categories.  The data are available in 30 arc-second (~1 km) resolutions. The grid cell values represent the number of species in a particular class, family or IUCN threatened category. The input vector layers are based on the IUCN Red List and the grids are compiled by the Columbia University Center for International Earth Science Information Network (CIESIN). The data from IUCN were downloaded in April 2013.",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "International Union for Conservation of Nature - IUCN, and Center for International Earth Science Information Network - CIESIN - Columbia University",
-            "title": "Gridded Species Distribution: Global Mammal Richness Grids, 2015 Release",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/species-global-mammal-richness-2015/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The 2015 Release of the Global Mammal Richness Grids data set of the Gridded Species Distribution collection are aggregations of the presence grids data for the entire class, individual  families, and International Union for the Conservation of Nature (IUCN) Red List status categories.  The data are available in 30 arc-second (~1 km) resolutions. The grid cell values represent the number of species in a particular class, family or IUCN threatened category. The input vector layers are based on the IUCN Red List and the grids are compiled by the Columbia University Center for International Earth Science Information Network (CIESIN). The data from IUCN were downloaded in April 2013.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4N014G5",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4N014G5",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/species/species-global-mammal-richness-2015/species-global-mammal-richness-2015-all-species-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/species/species-global-mammal-richness-2015/species-global-mammal-richness-2015-all-species-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/species-global-mammal-richness-2015/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/species-global-mammal-richness-2015/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/species-global-mammal-richness-2015/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/species-global-mammal-richness-2015/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/species-global-mammal-richness-2015/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/species-global-mammal-richness-2015/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/species-global-mammal-richness-2015",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/species-global-mammal-richness-2015",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/species-global-mammal-richness-2015/maps",
+            "identifier": "C1399957348-SEDAC",
+            "issued": "2015-12-31",
+            "keyword": [
+                "biological classification",
+                "earth science",
+                "animals/vertebrates"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4N014G5",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H4RR1W66"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2013-01-01T00:00:00Z/2013-12-31T00:00:00Z",
             "theme": [
                 "SPECIES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Gridded Species Distribution: Global Mammal Richness Grids, 2015 Release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2135",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Nghiem, J., G. Salter, and M.P. Lamb. 2023. Delta-X: Bed and Suspended Sediment Grain Size, MRD, LA, USA, 2021, Version 2. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2135",
-            "issued": "2023-02-23",
-            "temporal": "2021-03-24T17:22:00Z/2021-08-25T17:08:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "land surface",
-                "biosphere",
-                "earth science",
-                "geomorphic landforms/processes",
-                "terrestrial hydrosphere",
-                "surface water",
-                "ecosystems",
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
-            "identifier": "C2619216342-ORNL_CLOUD",
             "description": "This dataset provides sediment concentration and grain size distribution measurements from suspended and bed sediment samples collected in the Atchafalaya and Terrebonne River Basins as part of the Delta-X Spring campaign between March 24 to April 2, 2021 and Delta-X Fall campaign between August 17-25, 2021. During the field campaign, samples were collected in the main distributary channels and the interior of Mike Island in the Wax Lake Delta, Louisiana and at site CRMS0421 inside the Terrebonne River Basin. Sediment samples were collected from a boat using a Van Dorn sampler (for suspended sediment samples) or a Ponar bed sampler (for bed samples). Suspended sediment samples were collected from a boat drifting at approximately the same velocity as the water flow. One sample was collected per drift. Bed samples were collected in a similar fashion. Data includes measurements of sediment grain size, total sediment concentration, as well as water temperature, velocity, salinity, and depth. This Version 2 includes the initial release of Fall 2021 data and an update to the Version 1 (Spring 2021) data file in which an error in the data was resolved.",
-            "graphic-preview-description": "Figure 1: Suspended and bed sediment sampling locations in the Wax Lake Delta, Louisiana. Clusters of measurements are grouped together into single points on this map. Map excludes measurements made far upstream of the Wax Lake Delta or in the Terrebonne River Basin.",
-            "title": "Delta-X: Bed and Suspended Sediment Grain Size, MRD, LA, USA, 2021, Version 2",
-            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Sediment_Grain_Size_V2_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2135",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2135",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/deltax/DeltaX_Sediment_Grain_Size_V2/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/deltax/DeltaX_Sediment_Grain_Size_V2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Sediment_Grain_Size_V2.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Sediment_Grain_Size_V2.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2135",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2135",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/DeltaX_Sediment_Grain_Size_V2/comp/DeltaX_Sediment_Grain_Size_V2.pdf",
-                    "description": "Delta-X: Bed and Suspended Sediment Grain Size, MRD, LA, USA, 2021, Version 2: DeltaX_Sediment_Grain_Size_V2.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Delta-X: Bed and Suspended Sediment Grain Size, MRD, LA, USA, 2021, Version 2: DeltaX_Sediment_Grain_Size_V2.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/DeltaX_Sediment_Grain_Size_V2/comp/DeltaX_Sediment_Grain_Size_V2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Sediment_Grain_Size_V2_Fig1.png",
-                    "description": "Figure 1: Suspended and bed sediment sampling locations in the Wax Lake Delta, Louisiana. Clusters of measurements are grouped together into single points on this map. Map excludes measurements made far upstream of the Wax Lake Delta or in the Terrebonne River Basin.",
                     "@type": "dcat:Distribution",
+                    "description": "Figure 1: Suspended and bed sediment sampling locations in the Wax Lake Delta, Louisiana. Clusters of measurements are grouped together into single points on this map. Map excludes measurements made far upstream of the Wax Lake Delta or in the Terrebonne River Basin.",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Sediment_Grain_Size_V2_Fig1.png",
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
+            "graphic-preview-description": "Figure 1: Suspended and bed sediment sampling locations in the Wax Lake Delta, Louisiana. Clusters of measurements are grouped together into single points on this map. Map excludes measurements made far upstream of the Wax Lake Delta or in the Terrebonne River Basin.",
+            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Sediment_Grain_Size_V2_Fig1.png",
+            "identifier": "C2619216342-ORNL_CLOUD",
+            "issued": "2023-02-23",
+            "keyword": [
+                "land surface",
+                "biosphere",
+                "earth science",
+                "geomorphic landforms/processes",
+                "terrestrial hydrosphere",
+                "surface water",
+                "ecosystems",
+                "water quality/water chemistry"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2135",
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
             "spatial": "-91.45 29.17 -90.82 29.7",
+            "temporal": "2021-03-24T17:22:00Z/2021-08-25T17:08:00Z",
             "theme": [
                 "Delta-X",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Delta-X: Bed and Suspended Sediment Grain Size, MRD, LA, USA, 2021, Version 2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=SOHO-C-LASCO-4-COMETIMAGES-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images of Kreutz sungrazing comets that were obtained by the SOHO spacecraft from 1996-2005. Images have been processed by subtracting a bias, correcting for vignetting, and normalizing by the exposure time. A median of four neighboring images is then subtracted to remove the background. The resulting image has units of DN/sec. A 41x41 pixel array centered on the comet has been extracted for archiving. Future updates will contain Kreutz comets discovered since 2005, comets from the other sungrazing families (Marsden, Meyer, and Kracht), and other comets observed by SOHO.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.soho-c-lasco-4-cometimages-v1.0_jdeg-nbue",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "c/soho (2003 l3)",
                 "c/soho (2004 k11)",
@@ -970181,134 +970183,110 @@
                 "c/soho (2001 v3)",
                 "c/soho (2001 w4)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=SOHO-C-LASCO-4-COMETIMAGES-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.soho-c-lasco-4-cometimages-v1.0_jdeg-nbue",
-            "description": "This data set contains images of Kreutz sungrazing comets that were obtained by the SOHO spacecraft from 1996-2005. Images have been processed by subtracting a bias, correcting for vignetting, and normalizing by the exposure time. A median of four neighboring images is then subtracted to remove the background. The resulting image has units of DN/sec. A 41x41 pixel array centered on the comet has been extracted for archiving. Future updates will contain Kreutz comets discovered since 2005, comets from the other sungrazing families (Marsden, Meyer, and Kracht), and other comets observed by SOHO.",
-            "title": "SOHO LASCO COMET IMAGES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "SOHO LASCO COMET IMAGES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-C-HRIV-3-NAV-9P-ENCOUNTER-V1.0",
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
-                "9p/tempel 1 (1867 g1)",
-                "deep impact"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains calibrated images of comet 9P/Tempel 1 acquired by the Deep Impact High Resolution Instrument Visible CCD during the encounter phase of the mission. These observations were used for optical and autonomous navigation (NAV) of the flyby spacecraft as well as for scientific investigations. These data were collected on 3-4 July 2005.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-c-hriv-3-nav-9p-encounter-v1.0_jdf5-bb7v",
+            "issued": "2018-06-26",
+            "keyword": [
+                "9p/tempel 1 (1867 g1)",
+                "deep impact"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-C-HRIV-3-NAV-9P-ENCOUNTER-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-c-hriv-3-nav-9p-encounter-v1.0_jdf5-bb7v",
-            "description": "This data set contains calibrated images of comet 9P/Tempel 1 acquired by the Deep Impact High Resolution Instrument Visible CCD during the encounter phase of the mission. These observations were used for optical and autonomous navigation (NAV) of the flyby spacecraft as well as for scientific investigations. These data were collected on 3-4 July 2005.",
-            "title": "DEEP IMPACT 9P/TEMPEL ENCOUNTER - REDUCED HRIV NAV IMGS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "DEEP IMPACT 9P/TEMPEL ENCOUNTER - REDUCED HRIV NAV IMGS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=A16C-L-XRFS-2-SURFACE-XRAY-COUNTS-V1.0",
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
-                "apollo 16"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains two tables of time-ordered, raw event count rates acquired by the Apollo 16 X-Ray Fluorescence Spectrometer from 20 April to 24 April 1972 during lunar orbit.  The tables include counts for all channels of the three proportional counters (unfiltered, magnesium filter, aluminum filter) and the solar monitor.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.a16c-l-xrfs-2-surface-xray-counts-v1.0_jdf6-5ref",
+            "issued": "2021-05-21",
+            "keyword": [
+                "moon",
+                "apollo 16"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=A16C-L-XRFS-2-SURFACE-XRAY-COUNTS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.a16c-l-xrfs-2-surface-xray-counts-v1.0_jdf6-5ref",
-            "description": "This dataset contains two tables of time-ordered, raw event count rates acquired by the Apollo 16 X-Ray Fluorescence Spectrometer from 20 April to 24 April 1972 during lunar orbit.  The tables include counts for all channels of the three proportional counters (unfiltered, magnesium filter, aluminum filter) and the solar monitor.",
-            "title": "APOLLO 16 XRFS LUNAR SURFACE X-RAY\n      COUNTS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "APOLLO 16 XRFS LUNAR SURFACE X-RAY\n      COUNTS V1.0"
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
-                "radio science",
-                "spice",
-                "grs",
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
-            "identifier": "NASA-512",
             "description": "GRS, RADIO SCIENCE (Releases 115-117), SPICE, THEMIS",
-            "title": "PDS Odyssey Data Release 39",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -970316,105 +970294,111 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-512",
+            "issued": "2018-06-25",
+            "keyword": [
+                "pds",
+                "radio science",
+                "spice",
+                "grs",
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
+            "title": "PDS Odyssey Data Release 39"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VJ103IMG_NRT.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "VCST Team. 2019-04-08. VIIRS/JPSS1  Imagery Resolution Terrain Corrected Geolocation 6-Min L1 Swath 375m NRT. Version 2. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, LANCEMODIS. https://doi.org/10.5067/VIIRS/VJ103IMG_NRT.002. https://dx.doi.org/10.5067/VIIRS/VJ103IMG_NRT.002.",
-            "issued": "2019-04-08",
-            "temporal": "2019-04-08T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-04-04",
-            "keyword": [
-                "spectral/engineering",
-                "infrared wavelengths",
-                "earth science",
-                "visible wavelengths"
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
-            "identifier": "C1604644159-LANCEMODIS",
-            "description": "The Near Real Time (NRT) VIIRS/JPSS1 Imagery Resolution Terrain Corrected Geolocation 6-Min L1 Swath 375m (VJ103IMG_NRT) product includes the geolocation fields that are calculated for each VIIRS imagery resolution band (I-band) Line of sight (LOS) for all orbits at the nominal resolution of 375 m. The locations and ancillary information correspond to the intersection of the centers of each Field of View (FOV) from 32 detectors in an ideal I-band on the Earth's surface. A digital terrain model is used to model the Earth's surface. The main inputs are the spacecraft attitude and orbit ephemeris data, the instrument telemetry and the digital elevation model. The geolocation fields contained within the VNP03IMG_NRT Geolocation files include geodetic latitude, longitude, surface height above the geoid, solar zenith and azimuth angles, satellite zenith and azimuth angles, and a land/water mask for each 375m sample. Additional information is included in the header to enable the calculation of the approximate location of the center of the detectors for any of the VIIRS bands. This product is used as input by a large number of subsequent VIIRS Imagery Resolution products, particularly those produced by the Land team.",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "VCST Team",
-            "title": "VIIRS/JPSS1 Imagery Resolution Terrain Corrected Geolocation 6-Min L1 Swath 375m NRT",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Near Real Time (NRT) VIIRS/JPSS1 Imagery Resolution Terrain Corrected Geolocation 6-Min L1 Swath 375m (VJ103IMG_NRT) product includes the geolocation fields that are calculated for each VIIRS imagery resolution band (I-band) Line of sight (LOS) for all orbits at the nominal resolution of 375 m. The locations and ancillary information correspond to the intersection of the centers of each Field of View (FOV) from 32 detectors in an ideal I-band on the Earth's surface. A digital terrain model is used to model the Earth's surface. The main inputs are the spacecraft attitude and orbit ephemeris data, the instrument telemetry and the digital elevation model. The geolocation fields contained within the VNP03IMG_NRT Geolocation files include geodetic latitude, longitude, surface height above the geoid, solar zenith and azimuth angles, satellite zenith and azimuth angles, and a land/water mask for each 375m sample. Additional information is included in the header to enable the calculation of the approximate location of the center of the detectors for any of the VIIRS bands. This product is used as input by a large number of subsequent VIIRS Imagery Resolution products, particularly those produced by the Land team.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ103IMG_NRT.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ103IMG_NRT.002",
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
                     "title": "Download this dataset through MODAPS"
                 }
             ],
+            "identifier": "C1604644159-LANCEMODIS",
+            "issued": "2019-04-08",
+            "keyword": [
+                "spectral/engineering",
+                "infrared wavelengths",
+                "earth science",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VJ103IMG_NRT.002",
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
+            "title": "VIIRS/JPSS1 Imagery Resolution Terrain Corrected Geolocation 6-Min L1 Swath 375m NRT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://data.nasa.gov/d/jdkf-j3pt",
-            "issued": "2015-04-12",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "spaceapps"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NASA Public Data",
                 "hasEmail": "mailto:no-reply@data.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.nasa.gov"
-            },
-            "identifier": "https://data.nasa.gov/api/views/jdkf-j3pt",
             "description": "This is a monitor using data from Swift/BAT, MAXI and Fermi/GBM instruments. \r\nClick on the table header to change the sorting behaviour. \r\nColor code for the probability: (rising flux , no change, decreasing flux)\r\nThe average flux is calculated as the average of the last 3 days of data, without taking the errors into account. The fermi flux is not given in mCrab. \r\nPlease note that the accuracy of the probabilities is limited by the accuracy of the data used.\r\nRelease of Friday, the 17th of October 2014\r\n\r\nLast updated at 14:04:07 UT\r\n\r\nCreated as an ESAC trainee project by Eva Laplace. \r\nSupervisors: Peter Kretschmar, Emilio Salazar and Miguel Arregui. \r\nContact: peter.kretschmar@esa.int",
-            "title": "BeXRB Monitor Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -970422,703 +970406,698 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.nasa.gov/api/views/jdkf-j3pt/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.nasa.gov/api/views/jdkf-j3pt/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.nasa.gov/api/views/jdkf-j3pt/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.nasa.gov/api/views/jdkf-j3pt/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.nasa.gov/api/views/jdkf-j3pt/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.nasa.gov/api/views/jdkf-j3pt/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.nasa.gov/api/views/jdkf-j3pt/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.nasa.gov/api/views/jdkf-j3pt/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.nasa.gov/api/views/jdkf-j3pt/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "https://data.nasa.gov/api/views/jdkf-j3pt",
+            "issued": "2015-04-12",
+            "keyword": [
+                "spaceapps"
+            ],
+            "landingPage": "https://data.nasa.gov/d/jdkf-j3pt",
+            "modified": "2023-01-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.nasa.gov"
+            },
+            "title": "BeXRB Monitor Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP21A1D.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Glynn Hulley, Simon Hook. 2023-06-29. VIIRS/NPP Land Surface Temperature/Emissivity Daily L3 Global 1km SIN Grid Day V002. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VNP21A1D.002. https://doi.org/10.5067/VIIRS/VNP21A1D.002. This data set was provided by the NASA/NOAA NPP Project..",
-            "issued": "2023-06-29",
-            "temporal": "2012-01-17T00:00:00Z/2024-06-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-29",
-            "keyword": [
-                "land surface",
-                "surface radiative properties",
-                "earth science",
-                "surface thermal properties"
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
-            "identifier": "C2545314555-LPCLOUD",
-            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Land Surface Temperature and Emissivity (LST&E) Day Version 2 product (VNP21A1D) is compiled daily from daytime Level 2 Gridded (L2G) intermediate products.  \r\n\r\nThe L2G process maps the daily (VNP21) (https://doi.org/10.5067/VIIRS/VNP21.002) swath granules onto a sinusoidal MODIS grid and stores all observations overlapping a gridded cell for a given day. The VNP21A1 algorithm sorts through all these observations for each cell and estimates the final LST value as an average from all cloud-free observations that have good LST accuracies. The daytime average is weighted by the observation coverage for that cell. Only observations having observation coverage more than a certain threshold (15%) are considered for this averaging. The 1 kilometer dataset is derived through resampling the native 750 meter VIIRS resolution in the input product.\r\n\r\nThe VNP21A1D product is developed synergistically with the Moderate Resolution Imaging Spectroradiometer (MODIS) LST&E Version 6.1 product (MOD21A1D) (https://doi.org/10.5067/MODIS/MOD21A1D.061)) using the same input atmospheric products and algorithmic approach. The overall objective for NASA VIIRS products is to ensure the algorithms and products are compatible with the MODIS Terra and Aqua algorithms to promote the continuity of the Earth Observation System (EOS) mission. Additional details regarding the method used to create this Level 3 (L3) product are available in the Algorithm Theoretical Basis Document (ATBD) (https://lpdaac.usgs.gov/documents/1332/VNP21_ATBD_V1.pdf). VIIRS LST&E products are available 2 months after acquisition due to latency of data inputs.\r\n\r\nThe VNP21A1D product contains seven Science Datasets (SDS): LST, quality control, emissivity for bands M14, M15, and M16, view zenith angle, and time of observation. A low-resolution browse image for LST is also available for each VNP21A1D granule.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "Glynn Hulley, Simon Hook",
-            "title": "VIIRS/NPP Land Surface Temperature/Emissivity Daily L3 Global 1km SIN Grid Day V002",
-            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/datasets/C2545314555-LPCLOUD?h=85&w=85",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Land Surface Temperature and Emissivity (LST&E) Day Version 2 product (VNP21A1D) is compiled daily from daytime Level 2 Gridded (L2G) intermediate products.  \r\n\r\nThe L2G process maps the daily (VNP21) (https://doi.org/10.5067/VIIRS/VNP21.002) swath granules onto a sinusoidal MODIS grid and stores all observations overlapping a gridded cell for a given day. The VNP21A1 algorithm sorts through all these observations for each cell and estimates the final LST value as an average from all cloud-free observations that have good LST accuracies. The daytime average is weighted by the observation coverage for that cell. Only observations having observation coverage more than a certain threshold (15%) are considered for this averaging. The 1 kilometer dataset is derived through resampling the native 750 meter VIIRS resolution in the input product.\r\n\r\nThe VNP21A1D product is developed synergistically with the Moderate Resolution Imaging Spectroradiometer (MODIS) LST&E Version 6.1 product (MOD21A1D) (https://doi.org/10.5067/MODIS/MOD21A1D.061)) using the same input atmospheric products and algorithmic approach. The overall objective for NASA VIIRS products is to ensure the algorithms and products are compatible with the MODIS Terra and Aqua algorithms to promote the continuity of the Earth Observation System (EOS) mission. Additional details regarding the method used to create this Level 3 (L3) product are available in the Algorithm Theoretical Basis Document (ATBD) (https://lpdaac.usgs.gov/documents/1332/VNP21_ATBD_V1.pdf). VIIRS LST&E products are available 2 months after acquisition due to latency of data inputs.\r\n\r\nThe VNP21A1D product contains seven Science Datasets (SDS): LST, quality control, emissivity for bands M14, M15, and M16, view zenith angle, and time of observation. A low-resolution browse image for LST is also available for each VNP21A1D granule.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP21A1D.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP21A1D.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2545314555-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2545314555-LPCLOUD",
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
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP21A1D.002",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP21A1D.002",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/datasets/C2545314555-LPCLOUD?h=85&w=85",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/datasets/C2545314555-LPCLOUD?h=85&w=85",
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
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/2/VNP21A1D",
-                    "description": "The File Specification provides a description of the product file including scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/2/VNP21A1D",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
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
+            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/datasets/C2545314555-LPCLOUD?h=85&w=85",
+            "identifier": "C2545314555-LPCLOUD",
+            "issued": "2023-06-29",
+            "keyword": [
+                "land surface",
+                "surface radiative properties",
+                "earth science",
+                "surface thermal properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP21A1D.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-06-29",
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
+            "title": "VIIRS/NPP Land Surface Temperature/Emissivity Daily L3 Global 1km SIN Grid Day V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2340494022-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC.",
-            "issued": "2022-09-14",
-            "temporal": "2012-01-02T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-14",
-            "keyword": [
-                "earth science",
-                "ocean optics",
-                "oceans",
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
-            "identifier": "C2340494022-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "Suomi-NPP VIIRS Global Binned Chlorophyll (CHL) - NRT Data, version R2022.0",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/SNPP/VIIRS/L3B/CHL/2022",
-                    "description": "VIIRS-Suomi-NPP L3B Chlorophyll (CHL) - NRT Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS-Suomi-NPP L3B Chlorophyll (CHL) - NRT Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/SNPP/VIIRS/L3B/CHL/2022",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2340494022-OB_DAAC",
+            "issued": "2022-09-14",
+            "keyword": [
+                "earth science",
+                "ocean optics",
+                "oceans",
+                "ocean chemistry"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2340494022-OB_DAAC.html",
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
+            "title": "Suomi-NPP VIIRS Global Binned Chlorophyll (CHL) - NRT Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ISS/CATS/L2O_D-M7.2-V3-01_05kmPro",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2018-10-31. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ISS/CATS/L2O_D-M7.2-V3-01_05kmPro. https://asdc.larc.nasa.gov/project/CATS-ISS.",
-            "issued": "2018-08-13",
-            "temporal": "2015-03-25T00:00:00Z/2017-10-29T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-08-13",
-            "keyword": [
-                "atmosphere",
-                "aerosols",
-                "earth science",
-                "clouds"
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
-            "identifier": "C1599922061-LARC_ASDC",
             "description": "CATS-ISS_L2O_D-M7.2-V3-01_05kmPro is the Cloud-Aerosol Transport System (CATS) International Space Station (ISS) Level 2 Operational Day Mode 7.2 Version 3-01 5 km Profile data product. This collection spans from March 25, 2015 to October 29, 2017. CATS, which was launched on January 10, 2015, was a lidar remote sensing instrument that provided range-resolved profile measurements of atmospheric aerosols and clouds from the ISS. CATS was intended to operate on-orbit for up to three years. CATS provides vertical profiles at three wavelengths, orbiting between ~230 and ~270 miles above the Earth's surface at a 51-degree inclination with nearly a three-day repeat cycle. For the first time, scientists were able to study diurnal (day-to-night) changes in cloud and aerosol effects from space by observing the same spot on Earth at different times each day. CATS Level 2 Layer data products contain geophysical parameters and are derived from Level 1 data, at 60m vertical and 5km horizontal resolution.",
-            "graphic-preview-description": "CATS Browse and Granule Availability",
-            "title": "CATS-ISS Level 2 Operational Day Mode 7.2 Version 3-01 5 km Profile",
-            "graphic-preview-file": "https://cats.gsfc.nasa.gov/data/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FISS%2FCATS%2FL2O_D-M7.2-V3-01_05kmPro",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FISS%2FCATS%2FL2O_D-M7.2-V3-01_05kmPro",
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
-                    "downloadURL": "https://doi.org/10.5067/ISS/CATS/L2O_D-M7.2-V3-01_05kmPro",
-                    "description": "DOI data set landing page for CATS-ISS_L2O_D-M7.2-V3-01_05kmPro_V3-01",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CATS-ISS_L2O_D-M7.2-V3-01_05kmPro_V3-01",
+                    "downloadURL": "https://doi.org/10.5067/ISS/CATS/L2O_D-M7.2-V3-01_05kmPro",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1599922061-LARC_ASDC",
-                    "description": "Earthdata Search for CATS-ISS_L2O_D-M7.2-V3-01_05kmPro_V3-01 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CATS-ISS_L2O_D-M7.2-V3-01_05kmPro_V3-01 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1599922061-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CATS/L2O_D-M7.2-V3-01_05kmPro/contents.html",
-                    "description": "OPeNDAP data access for CATS-ISS_L2O_D-M7.2-V3-01_05kmPro_V3-01",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CATS-ISS_L2O_D-M7.2-V3-01_05kmPro_V3-01",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CATS/L2O_D-M7.2-V3-01_05kmPro/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CATS/L2O_D-M7.2-V3-01_05kmPro/",
-                    "description": "ASDC Direct Data Download for CATS-ISS_L2O_D-M7.2-V3-01_05kmPro_V3-01",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CATS-ISS_L2O_D-M7.2-V3-01_05kmPro_V3-01",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CATS/L2O_D-M7.2-V3-01_05kmPro/",
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
+            "identifier": "C1599922061-LARC_ASDC",
+            "issued": "2018-08-13",
+            "keyword": [
+                "atmosphere",
+                "aerosols",
+                "earth science",
+                "clouds"
+            ],
+            "landingPage": "https://doi.org/10.5067/ISS/CATS/L2O_D-M7.2-V3-01_05kmPro",
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
+            "title": "CATS-ISS Level 2 Operational Day Mode 7.2 Version 3-01 5 km Profile"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GNSS/GNSS_IGSIONOVTEC_001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "International GNSS Service, GNSS Weekly Ionosphere Total Electron Content Grid Validation Product, Greenbelt, MD, USA: NASA Crustal Dynamics Data Information System (CDDIS), Accessed [[enter user data access date]] at doi:10.5067/GNSS/gnss_igsionovtec_001",
-            "issued": "1998-01-01",
-            "temporal": "1998-01-01T00:00:00Z/2025-01-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-21",
-            "keyword": [
-                "earth science",
-                "geodetics",
-                "gravity/gravitational field",
-                "solid earth",
-                "tectonics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:support-cddis@nasa.ogv"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "CDDIS"
-            },
-            "identifier": "C1511780832-CDDIS",
             "description": "This derived product set consists of Global Navigation Satellite System Ionosphere Vertical Total Electron Content (VTEC) comparison product (daily files) from the NASA Crustal Dynamics Data Information System (CDDIS). GNSS provide autonomous geo-spatial positioning with global coverage. GNSS data sets from ground receivers at the CDDIS consist primarily of the data from the U.S. Global Positioning System (GPS) and the Russian GLObal NAvigation Satellite System (GLONASS). Since 2011, the CDDIS GNSS archive includes data from other GNSS (Europe\u2019s Galileo, China\u2019s Beidou, Japan\u2019s Quasi-Zenith Satellite System/QZSS, the Indian Regional Navigation Satellite System/IRNSS, and worldwide Satellite Based Augmentation Systems/SBASs), which are similar to the U.S. GPS in terms of the satellite constellation, orbits, and signal structure. GNSS observations from a global network can be utilized for atmospheric measurements. Analysis Centers (ACs) of the International GNSS Service (IGS) retrieve GNSS data on regular schedules to produce independently computed VTEC maps. The IGS Ionosphere Analysis Center Coordinator (ACC) uses these individual AC solutions to generate the official IGS VTEC maps. The validation products are used to compare the IGS and AC solutions of generated VTEC maps. There are three types of ionosphere product evaluation/validation products: 1) the upcwWWWW.YYv.Z files provide an evaluation of the final weekly combination solution of VTEC maps with the individual analysis center contributions; 2) the gpsgDDD0.YYi.Z files are provided by the Center for Orbit Determinate (CODE) at the Astronomical Institute at the University of Bern (AIUB) Switzerland; these files contain GPS broadcast ionosphere model for day YYDDD; and 3) the ckmgDDD0.YYi.Z products are computed by CODE using their Klobuchar model, best fitting CODE\u2019s final ionosphere solution, also available from the CDDIS.",
-            "title": "Global Navigation Satellite System (GNSS) Ionosphere Vertical Total Electron Content (VTEC) Validation Product from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGNSS_IGSIONOVTEC_001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGNSS_IGSIONOVTEC_001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/archive/gnss/products",
-                    "description": "URL for retrieval of GNSS derived products through https",
                     "@type": "dcat:Distribution",
+                    "description": "URL for retrieval of GNSS derived products through https",
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
-                    "downloadURL": "http://doi.org/10.5067/GNSS/GNSS_IGSIONOVTEC_001",
-                    "description": "URL for more information about GNSS derived products",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about GNSS derived products",
+                    "downloadURL": "http://doi.org/10.5067/GNSS/GNSS_IGSIONOVTEC_001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1511780832-CDDIS",
+            "issued": "1998-01-01",
+            "keyword": [
+                "earth science",
+                "geodetics",
+                "gravity/gravitational field",
+                "solid earth",
+                "tectonics"
+            ],
+            "landingPage": "https://doi.org/10.5067/GNSS/GNSS_IGSIONOVTEC_001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-21",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "CDDIS"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1998-01-01T00:00:00Z/2025-01-27T00:00:00Z",
             "theme": [
                 "IGS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Navigation Satellite System (GNSS) Ionosphere Vertical Total Electron Content (VTEC) Validation Product from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/je2j-67g7",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "keyword": [
-                "library construction",
-                "nucleic acid extraction",
-                "nucleic acid sequencing",
-                "treatment protocol",
-                "microgravity simulation"
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
-            "identifier": "nasa_genelab_GLDS-215_je2j-67g7",
             "description": "Previous spaceflight experiments using Bacillus subtilis have reported altered transcriptome profiles during spaceflight compared to matching ground samples. This study tried to replicate those transcriptome changes using High Aspect Ratio Vessels (HARVs). B. subtilis spores were grown in HARVs using the same protocol and growth conditions as the BRIC-21 spaceflight mission. RNA was extracted from the HARV samples and sequenced for differential expression analysis. HARV differentially expressed genes were then compared to the genes identified as differentially expressed in the BRIC-21 mission to access the accuracy of HARVs as a model for spaceflight experiments.",
-            "title": "HARV replication of the BRIC-21 Bacillus subtilis spaceflight samples",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-215",
-                    "description": "GeneLab Study Page",
                     "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-215",
+                    "mediaType": "text/html",
                     "title": "HARV replication of the BRIC-21 Bacillus subtilis spaceflight samples"
                 }
             ],
+            "identifier": "nasa_genelab_GLDS-215_je2j-67g7",
+            "issued": "2021-05-21",
+            "keyword": [
+                "library construction",
+                "nucleic acid extraction",
+                "nucleic acid sequencing",
+                "treatment protocol",
+                "microgravity simulation"
+            ],
+            "landingPage": "https://data.nasa.gov/d/je2j-67g7",
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
+            "title": "HARV replication of the BRIC-21 Bacillus subtilis spaceflight samples"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VEGA1-C-TVS-3-RDR-HALLEY-PROCESSED-V1.0",
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
-                "vega 1"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The TVS data from KFKI came in various stages. The initial submission from KFKI was completely replaced in the fall 1992. At that time, additional processed data with aspect and range corrections were included. The original filenaming scheme was preserved except for changing the leading filename character and expressing the aspect ratio as 'a'.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vega1-c-tvs-3-rdr-halley-processed-v1.0_je2j-znnu",
+            "issued": "2018-06-26",
+            "keyword": [
+                "halley",
+                "vega 1"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VEGA1-C-TVS-3-RDR-HALLEY-PROCESSED-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vega1-c-tvs-3-rdr-halley-processed-v1.0_je2j-znnu",
-            "description": "The TVS data from KFKI came in various stages. The initial submission from KFKI was completely replaced in the fall 1992. At that time, additional processed data with aspect and range corrections were included. The original filenaming scheme was preserved except for changing the leading filename character and expressing the aspect ratio as 'a'.",
-            "title": "VEGA1 TV SYSTEM IMAGES PROCESSED BY KFKI V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VEGA1 TV SYSTEM IMAGES PROCESSED BY KFKI V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/MODTM-8D4N9",
             "citation": "NASA OBPG. 2020-01-15. MODIS Terra Level 3 SST MID-IR 8 day 4km Nighttime. Version 2019.0. MODIS Terra Global Level 3 Mapped SST. OBPG, Goddard Space Flight Center  Greenbelt, MD,US. Archived by National Aeronautics and Space Administration, U.S. Government, OBPG. https://doi.org/10.5067/MODTM-8D4N9. https://podaac-tools.jpl.nasa.gov/drive/files/allData/modis/L3/docs/modis_sst.html. NASA OBPG, OBPG, 2020-01-15, MODIS Terra Level 3 SST MID-IR 8 day 4km Nighttime V2019.0, https://podaac-tools.jpl.nasa.gov/drive/files/allData/modis/L3/docs/modis_sst.html.",
-            "issued": "2019-12-14",
-            "temporal": "2000-02-24T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-12-14",
-            "references": [
-                "https://doi.org/10.1016/j.rse.2015.04.023",
-                "https://doi.org/10.1175/JTECH-D-18-0103.1"
-            ],
-            "keyword": [
-                "ngda",
-                "oceans",
-                "national geospatial data asset",
-                "ocean temperature",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:cmr-support@earthdata.nasa.gov"
             },
-            "identifier": "C2036882246-POCLOUD",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "description": "Day and night spatially gridded (L3) global NASA skin sea surface temperature (SST) products from the Moderate-resolution Imaging Spectroradiometer (MODIS) onboard the Terra satellite.  Average daily, weekly (8 day), monthly and annual skin SST products are available at both 4.63 and 9.26 km spatial resolution. Terra was launched by NASA on December 18, 1999, into a sun synchronous, polar orbit with a daylight descending node at 10:30 am, to study the global dynamics of the Earth atmosphere, land and oceans. The MODIS captures data in 36 spectral bands at a variety of spatial resolutions. Two SST products can be present in these files. The first is a skin SST produced for both day and night observations, derived from the long wave IR 11 and 12 micron  wavelength channels, using a modified nonlinear SST algorithm intended to provide continuity with SST derived from heritage and current NASA sensors. At night, a second SST product is produced using the mid-infrared 3.95 and 4.05 micron  channels which are unique to MODIS; the SST derived from these measurements is identified as SST4. The SST4 product has lower uncertainty, but due to sun glint can only be produced at night. To generate the L3 products the L2 pixels are binned into an integerized sinusoidal area grid (ISEAG) and mapped into an equidistant cylindrical (also known as Platte Carre) projection.  Additional projection detailed can be found at https://oceancolor.gsfc.nasa.gov/docs/format/ The NASA MODIS L3 SST data products are generated by the NASA Ocean Biology Processing Group (OBPG) Peter Minnett and his team at the Rosenstiel School of Marine and Atmospheric Science (RSMAS) are responsible for sea surface temperature algorithm development, error statistics and quality flagging. JPL acquires and distributes MODIS ocean L3 SST data from the OBPG as the official Physical Oceanography Data Archive (PO.DAAC) for SST. The R2019 superseded the previous v2014.1 datasets which can be found at https://doi.org/10.5067/MODTM-8D4N4",
-            "release-place": "OBPG, Goddard Space Flight Center  Greenbelt, MD,US",
-            "series-name": "MODIS Terra Level 3 SST MID-IR 8 day 4km Nighttime",
             "creator": "NASA OBPG",
-            "title": "MODIS Terra Level 3 SST MID-IR 8 day 4km Nighttime V2019.0",
-            "graphic-preview-description": "Thumbnail",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MODIS_TERRA_L3_SST_MID-IR_8DAY_4KM_NIGHTTIME_V2019.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Day and night spatially gridded (L3) global NASA skin sea surface temperature (SST) products from the Moderate-resolution Imaging Spectroradiometer (MODIS) onboard the Terra satellite.  Average daily, weekly (8 day), monthly and annual skin SST products are available at both 4.63 and 9.26 km spatial resolution. Terra was launched by NASA on December 18, 1999, into a sun synchronous, polar orbit with a daylight descending node at 10:30 am, to study the global dynamics of the Earth atmosphere, land and oceans. The MODIS captures data in 36 spectral bands at a variety of spatial resolutions. Two SST products can be present in these files. The first is a skin SST produced for both day and night observations, derived from the long wave IR 11 and 12 micron  wavelength channels, using a modified nonlinear SST algorithm intended to provide continuity with SST derived from heritage and current NASA sensors. At night, a second SST product is produced using the mid-infrared 3.95 and 4.05 micron  channels which are unique to MODIS; the SST derived from these measurements is identified as SST4. The SST4 product has lower uncertainty, but due to sun glint can only be produced at night. To generate the L3 products the L2 pixels are binned into an integerized sinusoidal area grid (ISEAG) and mapped into an equidistant cylindrical (also known as Platte Carre) projection.  Additional projection detailed can be found at https://oceancolor.gsfc.nasa.gov/docs/format/ The NASA MODIS L3 SST data products are generated by the NASA Ocean Biology Processing Group (OBPG) Peter Minnett and his team at the Rosenstiel School of Marine and Atmospheric Science (RSMAS) are responsible for sea surface temperature algorithm development, error statistics and quality flagging. JPL acquires and distributes MODIS ocean L3 SST data from the OBPG as the official Physical Oceanography Data Archive (PO.DAAC) for SST. The R2019 superseded the previous v2014.1 datasets which can be found at https://doi.org/10.5067/MODTM-8D4N4",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODTM-8D4N9",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODTM-8D4N9",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MODIS_TERRA_L3_SST_MID-IR_8DAY_4KM_NIGHTTIME_V2019.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MODIS_TERRA_L3_SST_MID-IR_8DAY_4KM_NIGHTTIME_V2019.0.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2036882246-POCLOUD",
-                    "description": "Browse and download granules over HTTPS using the virtual directories",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2036882246-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2036882246-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2036882246-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MODIS_TERRA_L3_SST_MID-IR_8DAY_4KM_NIGHTTIME_V2019.0.jpg",
+            "identifier": "C2036882246-POCLOUD",
+            "issued": "2019-12-14",
+            "keyword": [
+                "ngda",
+                "oceans",
+                "national geospatial data asset",
+                "ocean temperature",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODTM-8D4N9",
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
+            "series-name": "MODIS Terra Level 3 SST MID-IR 8 day 4km Nighttime",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-02-24T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "EOS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS Terra Level 3 SST MID-IR 8 day 4km Nighttime V2019.0"
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
-                "sharing",
-                "knowledge",
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
-            "identifier": "NASA-860__11",
             "description": "Academy of Program/Project & Engineering Leadership's ASK Magazine archive.",
-            "title": "Academy of Program/Project & Engineering Leadership ASK Magazine Past Issues",
-            "programCode": [
-                "026:045"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -971126,234 +971105,229 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/P3M",
+            "identifier": "NASA-860__11",
+            "issued": "2018-06-25",
+            "keyword": [
+                "appel",
+                "sharing",
+                "knowledge",
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-C-COMPIL-5-COMET-NUC-PROPERTIES-V2.0",
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
-                "comet",
-                "support archives"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-c-compil-5-comet-nuc-properties-v2.0_je3e-n9qf",
+            "issued": "2021-05-21",
+            "keyword": [
+                "comet",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-C-COMPIL-5-COMET-NUC-PROPERTIES-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-c-compil-5-comet-nuc-properties-v2.0_je3e-n9qf",
-            "description": "not applicable",
-            "title": "PROPERTIES OF COMET NUCLEI",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "PROPERTIES OF COMET NUCLEI"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-D-UDDS-5-DUST-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains the data from the Ulysses dust detector system (UDDS) from start of mission through the end of mission, 1990-2007. (As the dust detector was turned off after Nov. 30, 2007, this is the last date for which UDDS data is recorded.) Included are the dust impact data, noise data, laboratory calibration data, and location and orientation of the spacecraft and instrument.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-d-udds-5-dust-v3.0_je4m-jbrq",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "calibration",
                 "dust",
                 "ulysses"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-D-UDDS-5-DUST-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-d-udds-5-dust-v3.0_je4m-jbrq",
-            "description": "This data set contains the data from the Ulysses dust detector system (UDDS) from start of mission through the end of mission, 1990-2007. (As the dust detector was turned off after Nov. 30, 2007, this is the last date for which UDDS data is recorded.) Included are the dust impact data, noise data, laboratory calibration data, and location and orientation of the spacecraft and instrument.",
-            "title": "ULYSSES DUST DETECTION SYSTEM V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ULYSSES DUST DETECTION SYSTEM V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-ENGR7-V1.0",
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
+            "description": "The Cassini Radio Science Enceladus Gravity Science Experiment (ENGR7) Raw Data Archive is a time-ordered collection of radio science raw data acquired on November 29 and 30, 2010, during he Cassini Extended Mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-engr7-v1.0_je54-yfca",
+            "issued": "2018-06-26",
+            "keyword": [
+                "titan",
+                "cassini-huygens"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-ENGR7-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-engr7-v1.0_je54-yfca",
-            "description": "The Cassini Radio Science Enceladus Gravity Science Experiment (ENGR7) Raw Data Archive is a time-ordered collection of radio science raw data acquired on November 29 and 30, 2010, during he Cassini Extended Mission.",
-            "title": "CASSINI RSS RAW DATA SET - ENGR7 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI RSS RAW DATA SET - ENGR7 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-PRL-67PCHURYUMOV-M04-V1.0",
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
+            "description": "This data set contains images acquired between 2014-06-04 and 2014-06-18 by\nthe OSIRIS Narrow Angle Camera during the prelanding phase of the Rosetta\nmission at the comet 67P",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-prl-67pchuryumov-m04-v1.0_je5z-vfkz",
+            "issued": "2018-06-26",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-PRL-67PCHURYUMOV-M04-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-prl-67pchuryumov-m04-v1.0_je5z-vfkz",
-            "description": "This data set contains images acquired between 2014-06-04 and 2014-06-18 by\nthe OSIRIS Narrow Angle Camera during the prelanding phase of the Rosetta\nmission at the comet 67P",
-            "title": "ROSETTA-ORBITER COMET PRELANDING OSINAC 2 EDR data",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER COMET PRELANDING OSINAC 2 EDR data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC1-67P-M10-REFLECT-V1.0",
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
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 1 mission phase, covering the period from 2014-11-21T23:25:00.000 to 2014-12-19T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc1-67p-m10-reflect-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC1-67P-M10-REFLECT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc1-67p-m10-reflect-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 1 mission phase, covering the period from 2014-11-21T23:25:00.000 to 2014-12-19T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC1-MTP010 RDR-REFLECT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC1-MTP010 RDR-REFLECT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1282032614-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Tropical Rainfall Measuring Mission (TRMM). 2011-07-01. TRMM_3B31. TRMM TMI/PR Combined Precipitation L3 1 month 0.5 degree x 0.5 degree V7. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/TRMM_3B31_7.html.",
-            "issued": "2011-07-01",
-            "temporal": "1997-12-01T00:00:00Z/2015-03-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-04-20",
-            "references": [
-                "https://doi.org/10.2151/jmsj1965.75.4_799"
-            ],
-            "keyword": [
-                "earth science",
-                "precipitation",
-                "atmosphere",
-                "clouds"
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
-            "identifier": "C1282032614-GES_DISC",
-            "description": "This is a combined rainfall product. 3B31 uses the high quality retrievals done for the narrow swath in 2B31 to calibrate the wide swath retrievals generated in 2A12. For each 0.5 degree box and each vertical layer, an adjustment ratio is calculated for the swath overlap region for one month. Only TMI pixels with 2A12 pixelStatus equal to zero are included in monthly averages, which effectively removes sea ice.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "TRMM_3B31",
             "creator": "Tropical Rainfall Measuring Mission (TRMM)",
-            "title": "TRMM TMI/PR Combined Precipitation L3 1 month 0.5 degree x 0.5 degree V7 (TRMM_3B31) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TRMM_3B31_7.png",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This is a combined rainfall product. 3B31 uses the high quality retrievals done for the narrow swath in 2B31 to calibrate the wide swath retrievals generated in 2A12. For each 0.5 degree box and each vertical layer, an adjustment ratio is calculated for the swath overlap region for one month. Only TMI pixels with 2A12 pixelStatus equal to zero are included in monthly averages, which effectively removes sea ice.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -971362,130 +971336,137 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRMM_3B31_7.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRMM_3B31_7.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L3/TRMM_3B31.7",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L3/TRMM_3B31.7",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/dods/TRMM_3B31_7.info",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/dods/TRMM_3B31_7.info",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/opendap/TRMM_L3/TRMM_3B31.7/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/opendap/TRMM_L3/TRMM_3B31.7/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/thredds/catalog/aggregation/TRMM_3B31.7/catalog.html",
-                    "description": "Access the data via the THREDDS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the THREDDS.",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/thredds/catalog/aggregation/TRMM_3B31.7/catalog.html",
+                    "mediaType": "text/html",
                     "title": "Use THREDDS DATA to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRMM_3B31",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRMM_3B31",
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
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L3/TRMM_3B31/doc/README.TRMM_V7.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L3/TRMM_3B31/doc/README.TRMM_V7.pdf",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TRMM_3B31_7.png",
+            "identifier": "C1282032614-GES_DISC",
+            "issued": "2011-07-01",
+            "keyword": [
+                "earth science",
+                "precipitation",
+                "atmosphere",
+                "clouds"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1282032614-GES_DISC.html",
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
+            "references": [
+                "https://doi.org/10.2151/jmsj1965.75.4_799"
+            ],
+            "release-place": "Greenbelt, MD",
+            "series-name": "TRMM_3B31",
             "spatial": "-180.0 -40.0 180.0 40.0",
+            "temporal": "1997-12-01T00:00:00Z/2015-03-31T23:59:59.999Z",
             "theme": [
                 "TRMM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TRMM TMI/PR Combined Precipitation L3 1 month 0.5 degree x 0.5 degree V7 (TRMM_3B31) at GES DISC"
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
-            "identifier": "NASA-722",
             "description": "RSS",
-            "title": "PDS Odyssey Radio Science Data (81)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -971493,446 +971474,443 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-722",
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
+            "title": "PDS Odyssey Radio Science Data (81)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ACES/FIELDMILL/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Blakeslee, Richard J..2004. ACES ELECTRIC FIELD MILL [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/ACES/FIELDMILL/DATA101",
-            "issued": "2004-05-04",
-            "temporal": "2002-07-10T00:00:00Z/2002-08-30T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-20",
-            "keyword": [
-                "earth science",
-                "atmospheric electricity",
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
-            "identifier": "C1977847178-GHRC_DAAC",
             "description": "The ALTUS Cloud Electrification Study (ACES) was based at the Naval Air Facility Key West in Florida.  During August 2002, ACES researchers conducted overflights of thunderstorms over the southwestern corner of Florida. For the first time in NASA research, an uninhabited aerial vehicle (UAV) named ALTUS was used to collect cloud electrification data. Carrying field mills, optical sensors, electric field sensors and other instruments, ALTUS allowed scientists to collect cloud electrification data for the first time from above the storm, from it's birth through dissipation. This experiment allowed scientists to achieve the dual goals of gathering weather data safely and testing new aircraft technology. This dataset consists of data from Electric Field Mills, which yield information about the atmospheric electrical fields above the instruments.",
-            "title": "ACES ELECTRIC FIELD MILL V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FACES%2FFIELDMILL%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FACES%2FFIELDMILL%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=aces1efm",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=aces1efm",
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
+            "identifier": "C1977847178-GHRC_DAAC",
+            "issued": "2004-05-04",
+            "keyword": [
+                "earth science",
+                "atmospheric electricity",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ACES/FIELDMILL/DATA101",
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
             "spatial": "-85.0 23.0 -81.0 26.0",
+            "temporal": "2002-07-10T00:00:00Z/2002-08-30T23:59:59Z",
             "theme": [
                 "ACES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ACES ELECTRIC FIELD MILL V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-SS-RPCICA-2-CR4B-RAW-V2.0",
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
+            "description": "This dataset contains RAW DATA from the RPCICA instrument on\nmission ROSETTA during Cruise phase 4B. Data of the solar wind was obtained.\nData set version 2 replaces a previously delivered data set.\nImportant changes are the ordering of the energy levels which now\ngo from low to high and that the quality flag in the labels is\nupdated.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-ss-rpcica-2-cr4b-raw-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "solar wind"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-SS-RPCICA-2-CR4B-RAW-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-ss-rpcica-2-cr4b-raw-v2.0",
-            "description": "This dataset contains RAW DATA from the RPCICA instrument on\nmission ROSETTA during Cruise phase 4B. Data of the solar wind was obtained.\nData set version 2 replaces a previously delivered data set.\nImportant changes are the ordering of the energy levels which now\ngo from low to high and that the quality flag in the labels is\nupdated.",
-            "title": "ROSETTA-ORBITER SW RPCICA 2 CR4B UNCALIBRATED V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER SW RPCICA 2 CR4B UNCALIBRATED V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1345119267-GES_DISC.html",
             "citation": "AIRS Science Team/Joao Teixeira. 2016-10-15. AIRS2CCF_NRT. Version 006. AIRS/Aqua L2 Near Real Time (NRT) Cloud-Cleared Infrared Radiances (AIRS-only) V006. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/AIRS2CCF_NRT_006.html. Digital Science Data.",
-            "issued": "2024-07-03",
-            "temporal": "2016-10-15T00:00:00Z/2024-08-12T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-07",
-            "references": [
-                "https://doi.org/10.1109/TGRS.2002.808236",
-                "https://doi.org/10.1117/1.JRS.8.084994"
-            ],
-            "keyword": [
-                "earth science",
-                "infrared wavelengths",
-                "spectral/engineering"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ED ESFANDIARI",
                 "hasEmail": "mailto:asghar.e.esfandiari@nasa.gov"
             },
+            "creator": "AIRS Science Team/Joao Teixeira",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1345119267-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The Atmospheric Infrared Sounder (AIRS) Level 2 Near Real Time (NRT) Cloud-Cleared Infrared Radiances (AIRS-only) product (AIRS2CCF_NRT_006) differs from the routine product (AIRS2CCF_006) in four ways to meet the three hour latency requirements of the Land Atmosphere NRT Capability Earth Observing System (LANCE): (1) The NRT granules are produced without previous or subsequent granules if those granules are not available within 5 minutes, (2) the predictive ephemeris/attitude data are used rather than the definitive ephemeris/attitude, (3) if the forecast surface pressure is unavailable, a surface climatology is used, and (4) no ice cloud properties retrievals are performed. The consequences of these differences are described in the AIRS Near Real Time (NRT) data products document. The Atmospheric Infrared Sounder (AIRS) is a grating spectrometer (R = 1200) aboard the second Earth Observing System (EOS) polar-orbiting platform, EOS Aqua. In combination with the Advanced Microwave Sounding Unit (AMSU) and the Humidity Sounder for Brazil (HSB), AIRS constitutes an innovative atmospheric sounding group of visible, infrared, and microwave sensors. This product is produced using AIRS IR only because the radiometric noise in AMSU channel 4 started to increase significantly (since June 2007). Cloud-Cleared Radiances contain calibrated, geolocated channel-by-channel AIRS infrared radiances (milliWatts/m2/cm-1/steradian) that would have been observed within each AMSU footprint if there were no clouds in the FOV and produced along with the AIRS Standard Product, as they are the radiances used to retrieve the Standard Product. Nevertheless, they are an order of magnitude larger in data volume than the remainder of the Standard Products and, many Standard Product users are expected to have little interest in the Cloud Cleared Radiance. For these reasons they are a separate output file. The AIRS2CCF_NRT_006 products are stored in files (often referred to as \"granules\") that contain 6 minutes of data, 30 footprints across track by 45 lines along track.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "AIRS2CCF_NRT",
-            "creator": "AIRS Science Team/Joao Teixeira",
-            "graphic-preview-description": "Sample data of the \"AIRS/Aqua Level 2 Cloud-Cleared Infrared (IR) Radiances Product\".",
-            "title": "AIRS/Aqua L2 Near Real Time (NRT) Cloud-Cleared Infrared Radiances (AIRS-only) V006 (AIRS2CCF_NRT) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRS2CCF_NRT_006.jpeg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRS2CCF_NRT_006.jpeg",
-                    "description": "Sample data of the \"AIRS/Aqua Level 2 Cloud-Cleared Infrared (IR) Radiances Product\".",
                     "@type": "dcat:Distribution",
+                    "description": "Sample data of the \"AIRS/Aqua Level 2 Cloud-Cleared Infrared (IR) Radiances Product\".",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRS2CCF_NRT_006.jpeg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRS2CCF_NRT_006.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRS2CCF_NRT_006.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://discnrt1.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_NRT/AIRS2CCF_NRT.006/",
-                    "description": "Access the data via HTTPS. User registration is required. Register for a username and password at https://urs.eosdis.nasa.gov/users/new",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS. User registration is required. Register for a username and password at https://urs.eosdis.nasa.gov/users/new",
+                    "downloadURL": "https://discnrt1.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_NRT/AIRS2CCF_NRT.006/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://discnrt1.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_NRT/AIRS2CCF_NRT.006/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://discnrt1.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_NRT/AIRS2CCF_NRT.006/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRS2CCF_NRT+005",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRS2CCF_NRT+005",
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/nrt/data-holdings/airs-nrt-products",
-                    "description": "AIRS Near Real Time (NRT) information",
                     "@type": "dcat:Distribution",
+                    "description": "AIRS Near Real Time (NRT) information",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/nrt/data-holdings/airs-nrt-products",
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
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/AIRS/3.3_ScienceDataProductDocumentation/3.3.5_ProductQuality/nrt_memo_v6.pdf",
-                    "description": "Memo on NRT vs Standard Product",
                     "@type": "dcat:Distribution",
+                    "description": "Memo on NRT vs Standard Product",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/AIRS/3.3_ScienceDataProductDocumentation/3.3.5_ProductQuality/nrt_memo_v6.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
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
+            "graphic-preview-description": "Sample data of the \"AIRS/Aqua Level 2 Cloud-Cleared Infrared (IR) Radiances Product\".",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRS2CCF_NRT_006.jpeg",
+            "identifier": "C1345119267-GES_DISC",
+            "issued": "2024-07-03",
+            "keyword": [
+                "earth science",
+                "infrared wavelengths",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1345119267-GES_DISC.html",
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
+                "https://doi.org/10.1109/TGRS.2002.808236",
+                "https://doi.org/10.1117/1.JRS.8.084994"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "AIRS2CCF_NRT",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2016-10-15T00:00:00Z/2024-08-12T00:00:00Z",
             "theme": [
                 "Aqua",
                 "LANCE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AIRS/Aqua L2 Near Real Time (NRT) Cloud-Cleared Infrared Radiances (AIRS-only) V006 (AIRS2CCF_NRT) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-SPEC-2-DIDR-GZ-V1.0",
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
+            "description": "In preparation for the concerted international study of Comet Halley, the IHW conducted a trial run with observations of Comet Crommelin, largely during February and March of 1984.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-spec-2-didr-gz-v1.0_jeb4-frz4",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international halley watch",
+                "halley"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-SPEC-2-DIDR-GZ-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-spec-2-didr-gz-v1.0_jeb4-frz4",
-            "description": "In preparation for the concerted international study of Comet Halley, the IHW conducted a trial run with observations of Comet Crommelin, largely during February and March of 1984.",
-            "title": "IHW COMET SPEC EDITED DIGITALIZED IMAGE DATA RECORD GZ V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "IHW COMET SPEC EDITED DIGITALIZED IMAGE DATA RECORD GZ V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ESO-J-IRSPEC-3-RDR-SL9-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "At the ESO La Silla site is a direct imaging facility (DIFA) at the A Nasmyth focus of the NTT, in front of the image derotator which feeds the IRSPEC infrared spectrograph. Two remotely-controlled 45-degree mirrors can be inserted in the light beam to deviate the telescope beam either to a CCD camera (SUSI) or to an infrared array.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.eso-j-irspec-3-rdr-sl9-v1.0_jefs-ivfn",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "ground based atmospheric observations",
                 "comet sl9/jupiter collision",
                 "jupiter",
                 "sl9"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ESO-J-IRSPEC-3-RDR-SL9-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.eso-j-irspec-3-rdr-sl9-v1.0_jefs-ivfn",
-            "description": "At the ESO La Silla site is a direct imaging facility (DIFA) at the A Nasmyth focus of the NTT, in front of the image derotator which feeds the IRSPEC infrared spectrograph. Two remotely-controlled 45-degree mirrors can be inserted in the light beam to deviate the telescope beam either to a CCD camera (SUSI) or to an infrared array.",
-            "title": "ESO NTT IRSPEC IMAGE DATA FROM SL9 IMPACTS WITH JUPITER V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ESO NTT IRSPEC IMAGE DATA FROM SL9 IMPACTS WITH JUPITER V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1219-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-28T07:23:15.000 to 2015-11-28T16:30:24.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1219-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1219-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1219-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-28T07:23:15.000 to 2015-11-28T16:30:24.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1219 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1219 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-LEISA-2-LAUNCH-V1.0",
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
-                "calibration",
-                "new horizons"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Raw data taken by the New Horizons Linear Etalon Imaging Spectral Array instrument during the post-launch checkout mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-leisa-2-launch-v1.0_jeic-prt5",
+            "issued": "2018-06-26",
+            "keyword": [
+                "calibration",
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-LEISA-2-LAUNCH-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-leisa-2-launch-v1.0_jeic-prt5",
-            "description": "This data set contains Raw data taken by the New Horizons Linear Etalon Imaging Spectral Array instrument during the post-launch checkout mission phase.",
-            "title": "NEW HORIZONS LEISA POST-LAUNCH CHECKOUT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS LEISA POST-LAUNCH CHECKOUT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1273652151-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Donald F. Heath, et al.. 1985-12-11. BUVN4L3ZMT. Version 005. BUV/Nimbus-4 Level 3 Ozone Zonal Means V005. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/BUVN4L3ZMT_005.html. Digital Science Data.",
-            "issued": "2015-12-10",
-            "temporal": "1970-04-11T00:00:00Z/1977-05-06T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-12-10",
-            "keyword": [
-                "atmospheric chemistry",
-                "atmosphere",
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
-            "identifier": "C1273652151-GES_DISC",
-            "description": "The Nimbus-4 BUV Level 3 Ozone Zonal Means collection or ZMT contains total ozone, reflectivities, and ozone mixing ratios averaged in 10 degree latitude zones centered from  80 to -80 degrees. Mixing ratios are given at 19 levels: 0.3, 0.4, 0.5, 0.7, 1, 1.5, 2, 3, 4, 5, 7, 10, 15, 20, 30, 40, 50, 70 and 100 mbar. In addition to the means, files also include the standard deviation, minimum and maximum values, as well as sample size.\n\nThe data were originally created on IBM 360 machines and archived on magnetic tapes. The data have been restored from the tapes and are now archived on disk in their original IBM binary file format. Each file contains monthly, weekly and daily zonal means, as well as quarterly means if it is the last month of the quarter. The files consist of data records each with one-hundred-eighty 4-byte words. Monthly, weekly, daily and quarterly means are distinguished by the seventh 4-byte word in the records. A typical file is about 380 kB in size.\n\nThe BUV instrument was operational from April 10, 1970 until May 6, 1977. In July 1972 the Nimbus-4 solar power array partially failed such that BUV operations were curtailed. Thus data collected in the later years was increasingly sparse, particularly in the equatorial region.\n\nThis product was previously available from the NSSDC as the Zonal Means File (ZMT) with the identifier ESAC-00039 (old ID 70-025A-05O).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "BUVN4L3ZMT",
             "creator": "Donald F. Heath, et al.",
-            "title": "BUV/Nimbus-4 Level 3 Ozone Zonal Means V005 (BUVN4L3ZMT) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/BUVN4L3ZMT_005.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The Nimbus-4 BUV Level 3 Ozone Zonal Means collection or ZMT contains total ozone, reflectivities, and ozone mixing ratios averaged in 10 degree latitude zones centered from  80 to -80 degrees. Mixing ratios are given at 19 levels: 0.3, 0.4, 0.5, 0.7, 1, 1.5, 2, 3, 4, 5, 7, 10, 15, 20, 30, 40, 50, 70 and 100 mbar. In addition to the means, files also include the standard deviation, minimum and maximum values, as well as sample size.\n\nThe data were originally created on IBM 360 machines and archived on magnetic tapes. The data have been restored from the tapes and are now archived on disk in their original IBM binary file format. Each file contains monthly, weekly and daily zonal means, as well as quarterly means if it is the last month of the quarter. The files consist of data records each with one-hundred-eighty 4-byte words. Monthly, weekly, daily and quarterly means are distinguished by the seventh 4-byte word in the records. A typical file is about 380 kB in size.\n\nThe BUV instrument was operational from April 10, 1970 until May 6, 1977. In July 1972 the Nimbus-4 solar power array partially failed such that BUV operations were curtailed. Thus data collected in the later years was increasingly sparse, particularly in the equatorial region.\n\nThis product was previously available from the NSSDC as the Zonal Means File (ZMT) with the identifier ESAC-00039 (old ID 70-025A-05O).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -971941,445 +971919,481 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/BUVN4L3ZMT_005.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/BUVN4L3ZMT_005.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus4_BUV_Level3/BUVN4L3ZMT.005/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus4_BUV_Level3/BUVN4L3ZMT.005/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=BUVN4L3ZMT",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=BUVN4L3ZMT",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus4_BUV_Level3/BUVN4L3ZMT.005/doc/README.BUVN4L3ZMT.005.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus4_BUV_Level3/BUVN4L3ZMT.005/doc/README.BUVN4L3ZMT.005.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/N4_BUV_UsersGuide_19780013751.pdf",
-                    "description": "Nimbus 4 BUV User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Nimbus 4 BUV User's Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/N4_BUV_UsersGuide_19780013751.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
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
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/N4_BUV_Inventory.xlsx",
-                    "description": "N4 BUV Inventory",
                     "@type": "dcat:Distribution",
+                    "description": "N4 BUV Inventory",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/N4_BUV_Inventory.xlsx",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/BUVN4L3ZMT_005.png",
+            "identifier": "C1273652151-GES_DISC",
+            "issued": "2015-12-10",
+            "keyword": [
+                "atmospheric chemistry",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1273652151-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-12-10",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "BUVN4L3ZMT",
             "spatial": "-180.0 -80.0 180.0 80.0",
+            "temporal": "1970-04-11T00:00:00Z/1977-05-06T23:59:59.999Z",
             "theme": [
                 "Nimbus",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BUV/Nimbus-4 Level 3 Ozone Zonal Means V005 (BUVN4L3ZMT) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L2_05kmCPro-Standard-V4-21",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2018-10-17. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L2_05kmCPro-Standard-V4-21.",
-            "issued": "2018-09-06",
-            "temporal": "2020-07-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-09-06",
-            "keyword": [
-                "lidar",
-                "spectral/engineering",
-                "earth science",
-                "atmosphere",
-                "aerosols"
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
-            "identifier": "C1978623870-LARC_ASDC",
             "description": "CAL_LID_L2_05kmCPro-Standard-V4-21 is the Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) Lidar Level 2 Cloud Profile, Version 4-21 data product. Data for this product was collected using the CALIPSO Cloud-Aerosol Lidar with Orthogonal Polarization (CALIOP) instrument. The version of this product was changed from 4-20 to 4-21 to account for a change in the operating system of the CALIPSO production cluster.\r\n\r\nCALIPSO was launched on April 28, 2006 to study the impact of clouds and aerosols on the Earth's radiation budget and climate. It flies in the international A-Train constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments, CALIOP, Imaging Infrared Radiometer (IIR), and Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES.",
-            "title": "CALIPSO Lidar Level 2 Cloud Profile, V4-21",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCALIOP%2FCALIPSO%2FCAL_LID_L2_05kmCPro-Standard-V4-21",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCALIOP%2FCALIPSO%2FCAL_LID_L2_05kmCPro-Standard-V4-21",
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
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/qs/cal_lid_l2_all_v4-20.php",
-                    "description": "Data Quality Summary for the CALIPSO Version 4.20 and V4.21 Lidar Level 2 Data Products",
                     "@type": "dcat:Distribution",
+                    "description": "Data Quality Summary for the CALIPSO Version 4.20 and V4.21 Lidar Level 2 Data Products",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/qs/cal_lid_l2_all_v4-20.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product quality assessment"
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
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/publications.php",
-                    "description": "CALIPSO - List of publications",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO - List of publications",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/publications.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
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
-                    "downloadURL": "https://calipso.cnes.fr/fr",
-                    "description": "French (CNES) CALIPSO Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "French (CNES) CALIPSO Home Page",
+                    "downloadURL": "https://calipso.cnes.fr/fr",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/products/CALIPSO_DPC_Rev4x92.pdf",
-                    "description": "CALIPSO - Data Management System - Data Products Catalog - Release 2.4",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO - Data Management System - Data Products Catalog - Release 2.4",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/products/CALIPSO_DPC_Rev4x92.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1978623870-LARC_ASDC",
-                    "description": "Earthdata Search for CAL_LID_L2_05kmCPro-Standard-V4-21_V4-21  (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CAL_LID_L2_05kmCPro-Standard-V4-21_V4-21  (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1978623870-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L2_05kmCPro-Standard-V4-21",
-                    "description": "DOI data set landing page for CAL_LID_L2_05kmCPro-Standard-V4-21_V4-21",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CAL_LID_L2_05kmCPro-Standard-V4-21_V4-21",
+                    "downloadURL": "https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L2_05kmCPro-Standard-V4-21",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CALIPSO/LID_L2_05kmCPro-Standard-V4-21/",
-                    "description": "ASDC Direct Data Download for CAL_LID_L2_05kmCPro-Standard-V4-21_V4-21",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CAL_LID_L2_05kmCPro-Standard-V4-21_V4-21",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CALIPSO/LID_L2_05kmCPro-Standard-V4-21/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CALIPSO/LID_L2_05kmCPro-Standard-V4-21/contents.html",
-                    "description": "OPeNDAP data access for CAL_LID_L2_05kmCPro-Standard-V4-21_V4-21",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CAL_LID_L2_05kmCPro-Standard-V4-21_V4-21",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CALIPSO/LID_L2_05kmCPro-Standard-V4-21/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1978623870-LARC_ASDC",
+            "issued": "2018-09-06",
+            "keyword": [
+                "lidar",
+                "spectral/engineering",
+                "earth science",
+                "atmosphere",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L2_05kmCPro-Standard-V4-21",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-09-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2020-07-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "CALIPSO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CALIPSO Lidar Level 2 Cloud Profile, V4-21"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/APSWI5NK3PKJ",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NSCAT Twice-Daily SIR-Enhanced EASE-Grid 2.0 Radar Backscatter V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center. https://doi.org/10.5067/APSWI5NK3PKJ.",
-            "issued": "1996-09-14",
-            "temporal": "1996-09-14T00:00:00Z/1997-06-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1997-06-29",
-            "keyword": [
-                "earth science",
-                "spectral/engineering",
-                "radar"
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
-            "identifier": "C3068826019-NSIDC_ECS",
             "description": "This data set provides twice-daily enhanced-resolution radar backscatter images from 14 GHz NASA Scatterometer (NSCAT) observations by applying the Scatterometer Image Reconstruction with Filtering (SIRF) algorithm. The algorithm incorporates a median filter and a simplified spatial response function. Multiple passes of the spacecraft are combined to produce a higher spatial resolution and fill in coverage gaps between the individual measurement footprints, which are not contiguous and have six-sided shapes. Overlapping imaging periods start each day and extend through 4- and 8-day periods. Data are gridded to Northern Hemisphere, Southern Hemisphere, and Temperate EASE-Grid 2.0 projections at 3.125 km and 25 km resolutions.",
-            "title": "NSCAT Twice-Daily SIR-Enhanced EASE-Grid 2.0 Radar Backscatter V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAPSWI5NK3PKJ",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAPSWI5NK3PKJ",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP/NSIDC-0786.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP/NSIDC-0786.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=NSIDC-0786+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=NSIDC-0786+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0786/versions/001",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0786/versions/001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/APSWI5NK3PKJ",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/APSWI5NK3PKJ",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/APSWI5NK3PKJ",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/APSWI5NK3PKJ",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C3068826019-NSIDC_ECS",
+            "issued": "1996-09-14",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "radar"
+            ],
+            "landingPage": "https://doi.org/10.5067/APSWI5NK3PKJ",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1997-06-29",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1996-09-14T00:00:00Z/1997-06-30T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NSCAT Twice-Daily SIR-Enhanced EASE-Grid 2.0 Radar Backscatter V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Texas_Ozonesondes_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2022-08-22. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Texas_Ozonesondes_Data_1.",
-            "issued": "2021-08-20",
-            "temporal": "2013-08-29T00:00:00Z/2013-10-09T23:59:59.999Z",
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
-            "identifier": "C2417020026-LARC_ASDC",
             "description": "DISCOVERAQ_Texas_Ozonesondes_Data contains data collected via ozonesonde launches at the Moody Tower and Smith Point ground sites during the Texas (Houston) deployment of NASA's DISCOVER-AQ field study. This data product contains data for only the Texas deployment, and data collection is complete.\r\n\r\nUnderstanding the factors that contribute to near surface pollution is difficult using only satellite-based observations. The incorporation of surface-level measurements from aircraft and ground-based platforms provides the crucial information necessary to validate and expand upon the use of satellites in understanding near surface pollution. Deriving Information on Surface conditions from Column and Vertically Resolved Observations Relevant to Air Quality (DISCOVER-AQ) was a four-year campaign conducted in collaboration between NASA Langley Research Center, NASA Goddard Space Flight Center, NASA Ames Research Center, and multiple universities to improve the use of satellites to monitor air quality for public health and environmental benefit. Through targeted airborne and ground-based observations, DISCOVER-AQ enabled more effective use of current and future satellites to diagnose ground level conditions influencing air quality.\r\n\r\nDISCOVER-AQ employed two NASA aircraft, the P-3B and King Air, with the P-3B completing in-situ spiral profiling of the atmosphere (aerosol properties, meteorological variables, and trace gas species). The King Air conducted both passive and active remote sensing of the atmospheric column extending below the aircraft to the surface. Data from an existing network of surface air quality monitors, AERONET sun photometers, Pandora UV/vis spectrometers and model simulations were also collected. Further, DISCOVER-AQ employed many surface monitoring sites, with measurements being made on the ground, in conjunction with the aircraft. The B200 and P-3B conducted flights in Baltimore-Washington, D.C. in 2011, Houston, TX in 2013, San Joaquin Valley, CA in 2013, and Denver, CO in 2014. These regions were targeted due to being in violation of the National Ambient Air Quality Standards (NAAQS).\r\n\r\nThe first objective of DISCOVER-AQ was to determine and investigate correlations between surface measurements and satellite column observations for the trace gases ozone (O3), nitrogen dioxide (NO2), and formaldehyde (CH2O) to understand how satellite column observations can diagnose surface conditions. DISCOVER-AQ also had the objective of using surface-level measurements to understand how satellites measure diurnal variability and to understand what factors control diurnal variability. Lastly, DISCOVER-AQ aimed to explore horizontal scales of variability, such as regions with steep gradients and urban plumes.",
-            "title": "DISCOVER-AQ Texas Deployment Ozonesonde Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDISCOVERAQ_Texas_Ozonesondes_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDISCOVERAQ_Texas_Ozonesondes_Data_1",
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
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Texas_Ozonesondes_Data_1",
-                    "description": "DOI for DISCOVERAQ_Texas_Ozonesondes_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for DISCOVERAQ_Texas_Ozonesondes_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Texas_Ozonesondes_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2417020026-LARC_ASDC",
-                    "description": "Earthdata Search client for DISCOVERAQ_Texas_Ozonesondes_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search client for DISCOVERAQ_Texas_Ozonesondes_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2417020026-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/DISCOVER-AQ/Texas_Ozonesondes_Data_1/",
-                    "description": "ASDC Direct Data Download for DISCOVERAQ_Texas_Ozonesondes_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for DISCOVERAQ_Texas_Ozonesondes_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/DISCOVER-AQ/Texas_Ozonesondes_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2417020026-LARC_ASDC",
+            "issued": "2021-08-20",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Texas_Ozonesondes_Data_1",
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
+            "temporal": "2013-08-29T00:00:00Z/2013-10-09T23:59:59.999Z",
             "theme": [
                 "DISCOVER-AQ",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "DISCOVER-AQ Texas Deployment Ozonesonde Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/jers-v5ph",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Technology demonstration of a nanopore sequencer operating aboard the ISS in comparison with the same sequencer on the ground.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-84",
+                    "mediaType": "text/html",
+                    "title": "Biomolecule Sequencer"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-84_jers-v5ph",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "nucleic acid extraction",
                 "nucleic acid sequencing",
@@ -972388,298 +972402,286 @@
                 "library construction",
                 "microgravity"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/jers-v5ph",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-84_jers-v5ph",
-            "description": "Technology demonstration of a nanopore sequencer operating aboard the ISS in comparison with the same sequencer on the ground.",
-            "title": "Biomolecule Sequencer",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-84",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Biomolecule Sequencer"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Biomolecule Sequencer"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MOD16A2.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Steven Running, Qiaozhen Mu, Maosheng Zhao. 2021-03-15. MODIS/Terra Net Evapotranspiration 8-Day L4 Global 500m SIN Grid V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MOD16A2.061. https://doi.org/10.5067/MODIS/MOD16A2.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-03-15",
-            "temporal": "2021-01-01T00:00:00Z/2024-05-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-03-15",
-            "keyword": [
-                "ngda",
-                "atmosphere",
-                "earth science",
-                "atmospheric water vapor",
-                "national geospatial data asset",
-                "precipitation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Steve Running",
                 "hasEmail": "mailto:swr@ntsg.umt.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
-            "identifier": "C2343113232-LPCLOUD",
-            "description": "The MOD16A2 Version 6.1 Evapotranspiration/Latent Heat Flux product is an 8-day composite dataset produced at 500 meter (m) pixel resolution. The algorithm used for the MOD16 data product collection is based on the logic of the Penman-Monteith equation, which includes inputs of daily meteorological reanalysis data along with Moderate Resolution Imaging Spectroradiometer (MODIS) remotely sensed data products such as vegetation property dynamics, albedo, and land cover. \r\n\r\nProvided in the MOD16A2 product are layers for composited Evapotranspiration (ET), Latent Heat Flux (LE), Potential ET (PET) and Potential LE (PLE) along with a quality control layer. Two low resolution browse images, ET and LE, are also available for each MOD16A2 granule.\r\n\r\nThe pixel values for the two Evapotranspiration layers (ET and PET) are the sum of all eight days within the composite period and the pixel values for the two Latent Heat layers (LE and PLE) are the average of all eight days within the composite period. Note that the last acquisition period of each year is a 5 or 6-day composite period, depending on the year.\r\n\r\nValidation at stage 1 (https://landweb.modaps.eosdis.nasa.gov/cgi-bin/QA_WWW/newPage.cgi?fileName=maturity) has been achieved for MODIS Evapotranspiration products.\r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).\r\n* The product uses Climatology LAI/FPAR as back up to the operational LAI/FPAR.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "Steven Running, Qiaozhen Mu, Maosheng Zhao",
-            "title": "MODIS/Terra Net Evapotranspiration 8-Day L4 Global 500m SIN Grid V061",
-            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2370959723-LPCLOUD?h=85&w=85",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MOD16A2 Version 6.1 Evapotranspiration/Latent Heat Flux product is an 8-day composite dataset produced at 500 meter (m) pixel resolution. The algorithm used for the MOD16 data product collection is based on the logic of the Penman-Monteith equation, which includes inputs of daily meteorological reanalysis data along with Moderate Resolution Imaging Spectroradiometer (MODIS) remotely sensed data products such as vegetation property dynamics, albedo, and land cover. \r\n\r\nProvided in the MOD16A2 product are layers for composited Evapotranspiration (ET), Latent Heat Flux (LE), Potential ET (PET) and Potential LE (PLE) along with a quality control layer. Two low resolution browse images, ET and LE, are also available for each MOD16A2 granule.\r\n\r\nThe pixel values for the two Evapotranspiration layers (ET and PET) are the sum of all eight days within the composite period and the pixel values for the two Latent Heat layers (LE and PLE) are the average of all eight days within the composite period. Note that the last acquisition period of each year is a 5 or 6-day composite period, depending on the year.\r\n\r\nValidation at stage 1 (https://landweb.modaps.eosdis.nasa.gov/cgi-bin/QA_WWW/newPage.cgi?fileName=maturity) has been achieved for MODIS Evapotranspiration products.\r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).\r\n* The product uses Climatology LAI/FPAR as back up to the operational LAI/FPAR.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD16A2.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD16A2.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOLT/MOD16A2.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOLT/MOD16A2.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2343113232-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2343113232-LPCLOUD",
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
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD16A2.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD16A2.061",
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
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/931/MOD16_User_Guide_V61.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/931/MOD16_User_Guide_V61.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/93/MOD16_ATBD.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/93/MOD16_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MOD16A2",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MOD16A2",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/MODLAND_val.html",
-                    "description": "Validation at stage 3 has been achieved for the MODIS Evapotranspiration data products.",
                     "@type": "dcat:Distribution",
+                    "description": "Validation at stage 3 has been achieved for the MODIS Evapotranspiration data products.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/MODLAND_val.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD16",
-                    "description": "Further details regarding MODIS land product validation for the MOD16 data products are available from the MODIS Land Team Validation site.",
                     "@type": "dcat:Distribution",
+                    "description": "Further details regarding MODIS land product validation for the MOD16 data products are available from the MODIS Land Team Validation site.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD16",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP128/MOLT/MOD16A2.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP128/MOLT/MOD16A2.061/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2370959723-LPCLOUD?h=85&w=85",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2370959723-LPCLOUD?h=85&w=85",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2370959723-LPCLOUD?h=85&w=85",
+            "identifier": "C2343113232-LPCLOUD",
+            "issued": "2021-03-15",
+            "keyword": [
+                "ngda",
+                "atmosphere",
+                "earth science",
+                "atmospheric water vapor",
+                "national geospatial data asset",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MOD16A2.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-03-15",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2021-01-01T00:00:00Z/2024-05-27T00:00:00Z",
             "theme": [
                 "Terra",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Terra Net Evapotranspiration 8-Day L4 Global 500m SIN Grid V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-IRFTAB-2-RDR-GZ-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-irftab-2-rdr-gz-v1.0_jet4-sg2b",
+            "issued": "2021-05-21",
+            "keyword": [
+                "halley",
+                "international halley watch"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-IRFTAB-2-RDR-GZ-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-irftab-2-rdr-gz-v1.0_jet4-sg2b",
-            "description": "In preparation for the concerted international study of Comet Halley, the IHW conducted a trial run with observations of Comet Crommelin, largely during February and March of 1984.",
-            "title": "IHW COMET IRFTAB EDITED REDUCED DATA RECORD GZ V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "IHW COMET IRFTAB EDITED REDUCED DATA RECORD GZ V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1286-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-25T22:25:50.000 to 2015-12-26T01:11:05.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1286-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1286-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1286-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-25T22:25:50.000 to 2015-12-26T01:11:05.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1286 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1286 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0778-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-05-15T12:25:35.000 to 2015-05-15T15:16:47.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0778-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0778-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0778-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-05-15T12:25:35.000 to 2015-05-15T15:16:47.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0778 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0778 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-ALICE-2-JUPITER-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Raw data taken by the New Horizons Alice UV Spectrograph instrument during the Jupiter encounter mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-alice-2-jupiter-v2.0_jevq-6ymp",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "calibration",
                 "callisto",
@@ -972690,149 +972692,117 @@
                 "jupiter",
                 "new horizons"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-ALICE-2-JUPITER-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-alice-2-jupiter-v2.0_jevq-6ymp",
-            "description": "This data set contains Raw data taken by the New Horizons Alice UV Spectrograph instrument during the Jupiter encounter mission phase.",
-            "title": "NEW HORIZONS ALICE JUPITER ENCOUNTER V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS ALICE JUPITER ENCOUNTER V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-VARGBDET-5-NESVORNYFAM-V2.0",
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
+            "description": "This data set contains asteroid dynamical family memberships for 64 families calculated from analytic proper elements, and 79 families calculated from synthetic proper elements, including high-inclination families. These families were calculated by David Nesvorny using his code based on the Hierarchical Clustering Method (HCM) described in Zappala et al. (1990, 1994). The input analytic proper elements for 401,408 numbered and unnumbered asteroids were calculated by Milani and Knezevic. The input synthetic proper elements for 302,212 numbered asteroids were calculated by Knezevic.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-vargbdet-5-nesvornyfam-v2.0_jexf-m2zr",
+            "issued": "2018-06-26",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-VARGBDET-5-NESVORNYFAM-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-vargbdet-5-nesvornyfam-v2.0_jexf-m2zr",
-            "description": "This data set contains asteroid dynamical family memberships for 64 families calculated from analytic proper elements, and 79 families calculated from synthetic proper elements, including high-inclination families. These families were calculated by David Nesvorny using his code based on the Hierarchical Clustering Method (HCM) described in Zappala et al. (1990, 1994). The input analytic proper elements for 401,408 numbered and unnumbered asteroids were calculated by Milani and Knezevic. The input synthetic proper elements for 302,212 numbered asteroids were calculated by Knezevic.",
-            "title": "NESVORNY HCM ASTEROID FAMILIES V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NESVORNY HCM ASTEROID FAMILIES V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1057-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-09-25T09:44:50.000 to 2015-09-25T17:32:29.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1057-v1.0_jey7-dr6v",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1057-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1057-v1.0_jey7-dr6v",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-09-25T09:44:50.000 to 2015-09-25T17:32:29.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1057 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1057 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/Aura/OMI/DATA3001",
             "citation": "Pawan K. Bhartia. 2012-03-25. OMTO3d. Version 003. OMI/Aura TOMS-Like Ozone, Aerosol Index, Cloud Radiance Fraction L3 1 day 1 degree x 1 degree V3. NASA Goddard Space Flight Center. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/OMI/DATA3001. https://disc.gsfc.nasa.gov/datacollection/OMTO3d_003.html. Digital Science Data.",
-            "issued": "2004-10-01",
-            "temporal": "2004-10-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2012-04-20",
-            "references": [
-                "https://doi.org/10.1109/TGRS.2006.869987",
-                "https://doi.org/10.1109/TGRS.2006.872935",
-                "https://doi.org/10.1117/12.627013"
-            ],
-            "keyword": [
-                "atmosphere",
-                "atmospheric radiation",
-                "aerosols",
-                "atmospheric chemistry",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JENNIFER WEI",
                 "hasEmail": "mailto:jennifer.c.wei@nasa.gov"
             },
+            "creator": "Pawan K. Bhartia",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1266136070-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The OMI science team produces this Level-3 daily global TOMS-Like Total Column Ozone gridded product OMTO3d (1 deg Lat/Lon grids). The OMTO3d product is produced by gridding and averaging only good quality level-2 total column ozone orbital swath data (OMTO3, based on the enhanced TOMS version-8 algorithm) on the 1x1 degree global grids.\n\nThe OMTO3d files are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5). Each file contains daily data from approximately 15 orbits. The maximum file size for the OMTO3d data product is about 0.65 Mbytes.",
-            "release-place": "NASA Goddard Space Flight Center",
-            "series-name": "OMTO3d",
-            "creator": "Pawan K. Bhartia",
-            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
-            "title": "OMI/Aura TOMS-Like Ozone, Aerosol Index, Cloud Radiance Fraction L3 1 day 1 degree x 1 degree V3 (OMTO3d) at GES DISC",
-            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=OMTO3d",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FOMI%2FDATA3001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FOMI%2FDATA3001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -972842,73 +972812,73 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMTO3d_003.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMTO3d_003.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level3/OMTO3d.003/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level3/OMTO3d.003/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=OMTO3d",
-                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
                     "@type": "dcat:Distribution",
+                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=OMTO3d",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through GIOVANNI"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMTO3d_003",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMTO3d_003",
+                    "mediaType": "text/html",
```

