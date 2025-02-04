# Change History for nasa.json (Part 83)

### Changes from 31606f9 to dd2190f (Part 72/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/AIRS/3.7_ScienceDataProductValidation/V5_CalVal_Status_Summary.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
@@ -749793,28 +749770,53 @@
                     "title": "View this dataset's algorithm theoretical basis document"
                 }
             ],
+            "graphic-preview-description": "Sample image of AIRABRAD",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRABRAD_NRT_005.jpeg",
+            "identifier": "C1233769000-GES_DISC",
+            "issued": "2024-11-17",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "microwave"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1233769000-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-11-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "AIRABRAD_NRT",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2015-12-15T00:00:00Z/2024-11-25T00:00:00Z",
             "theme": [
                 "Aqua",
                 "LANCE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AIRS/Aqua L1B Near Real Time (NRT) AMSU (A1/A2) geolocated and calibrated brightness temperatures V005 (AIRABRAD_NRT) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-VIRTIS-2-AST2-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This release contains the digital numbers (DN) contained in the telemetry (TM) packages of the VIRTIS instrument on board of the spacecraft Rosetta. This volume contains data from the Lutetia Fly-by phase, which occurred on 25-04/10-07/2010.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-virtis-2-ast2-v1.0_fbnd-zyjm",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "21 lutetia",
                 "moon",
@@ -749825,118 +749827,130 @@
                 "arcturus",
                 "4 vesta"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-VIRTIS-2-AST2-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-virtis-2-ast2-v1.0_fbnd-zyjm",
-            "description": "This release contains the digital numbers (DN) contained in the telemetry (TM) packages of the VIRTIS instrument on board of the spacecraft Rosetta. This volume contains data from the Lutetia Fly-by phase, which occurred on 25-04/10-07/2010.",
-            "title": "ROSETTA-ORBITER LUTETIA VIRTIS 2 AST2 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER LUTETIA VIRTIS 2 AST2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/1W3HSQ5D3VKP",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "High Mountain Asia Langtang Shortwave Downward Irradiance V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/1W3HSQ5D3VKP.",
-            "issued": "2017-10-21",
-            "temporal": "2017-10-21T00:00:00Z/2018-11-25T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-11-25",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "atmospheric radiation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Si-Chee Tsay",
                 "hasEmail": "mailto:si-chee.tsay@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1633818834-NSIDC_ECS",
             "description": "This data set contains thermal-dome-corrected downward shortwave irradiance at the bottom of atmosphere, measured by the Shared Mobile Atmospheric Research and Teaching Radar (SMART-R) and collected by the International Centre for Integrated Mountain Development (ICIMOD).",
-            "title": "High Mountain Asia Langtang Shortwave Downward Irradiance V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F1W3HSQ5D3VKP",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F1W3HSQ5D3VKP",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/HMA/HMA_SDI.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/HMA/HMA_SDI.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1633818834-NSIDC_ECS&m=4.66534423828125%2185.550537109375%213%211%210%210%2C2&tl=1552860036%214%21%21&ac=true",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1633818834-NSIDC_ECS&m=4.66534423828125%2185.550537109375%213%211%210%210%2C2&tl=1552860036%214%21%21&ac=true",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/HMA_SDI/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/HMA_SDI/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/1W3HSQ5D3VKP",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/1W3HSQ5D3VKP",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/1W3HSQ5D3VKP",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/1W3HSQ5D3VKP",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1633818834-NSIDC_ECS",
+            "issued": "2017-10-21",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://doi.org/10.5067/1W3HSQ5D3VKP",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-11-25",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "85.566 28.211 85.566 28.211",
+            "temporal": "2017-10-21T00:00:00Z/2018-11-25T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "High Mountain Asia Langtang Shortwave Downward Irradiance V001"
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
+                    "description": "FY11 NASA Strategic Plan",
+                    "downloadURL": "http://www.nasa.gov/pdf/516579main_NASA2011StrategicPlan.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "NASA FY11 Budget Strategic Plan"
+                }
+            ],
+            "identifier": "OCIO-Fitara-71",
             "issued": "2010-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "finance",
                 "strategic",
@@ -749945,621 +749959,609 @@
                 "budget",
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
-            "identifier": "OCIO-Fitara-71",
-            "description": "NASA Financial Budget Documents, Strategic Plans and Performance Reports for fiscal year 2011.",
-            "title": "NASA Financial Budget Documents, Strategic Plans and Performance Reports 2011: NASA Strategy Plan",
-            "programCode": [
-                "026:046"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.nasa.gov/pdf/516579main_NASA2011StrategicPlan.pdf",
-                    "description": "FY11 NASA Strategic Plan",
-                    "@type": "dcat:Distribution",
-                    "title": "NASA FY11 Budget Strategic Plan"
-                }
-            ],
-            "accrualPeriodicity": "R/P1Y",
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "NASA Financial Budget Documents, Strategic Plans and Performance Reports 2011: NASA Strategy Plan"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=JNO-E%2FJ%2FSS-WAV-3-CDR-SRVFULL-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The Juno Waves calibrated full resolution survey data set includes all low rate science electric spectral densities from 50Hz to 41MHz and magnetic spectral densities from 50Hz to 20kHz with complete sweeps at 30, 10 and 1 second intervals depending on the instrument mode.  This is a complete full resolution data set containing all low rate science data received from Waves from launch until the end of mission including initial checkout, the Earth flyby, the Jupiter orbits and all cruise data. Data are acquired from the Waves Low Frequency Receiver (LFR) and High Frequency Receiver (HFR) and are processed into spectra on board. These data are presented as ASCII text spreadsheets for ease of use. This data set is intended to be the most comprehensive and complete data set included in the Juno Waves archive.  Pre-rendered spectrograms generated from these data are included as well to lead the user to the particular data file(s) of interest.  This data set should be among the first used of any in the Waves archive as it will lead one to the information required to locate more detailed products.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.jno-e-j-ss-wav-3-cdr-srvfull-v1.0_fbqk-mv5p",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "jupiter",
                 "solar system",
                 "juno",
                 "earth"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=JNO-E%2FJ%2FSS-WAV-3-CDR-SRVFULL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.jno-e-j-ss-wav-3-cdr-srvfull-v1.0_fbqk-mv5p",
-            "description": "The Juno Waves calibrated full resolution survey data set includes all low rate science electric spectral densities from 50Hz to 41MHz and magnetic spectral densities from 50Hz to 20kHz with complete sweeps at 30, 10 and 1 second intervals depending on the instrument mode.  This is a complete full resolution data set containing all low rate science data received from Waves from launch until the end of mission including initial checkout, the Earth flyby, the Jupiter orbits and all cruise data. Data are acquired from the Waves Low Frequency Receiver (LFR) and High Frequency Receiver (HFR) and are processed into spectra on board. These data are presented as ASCII text spreadsheets for ease of use. This data set is intended to be the most comprehensive and complete data set included in the Juno Waves archive.  Pre-rendered spectrograms generated from these data are included as well to lead the user to the particular data file(s) of interest.  This data set should be among the first used of any in the Waves archive as it will lead one to the information required to locate more detailed products.",
-            "title": "JUNO E/J/SS WAVES CALIBRATED SURVEY FULL RESOLUTION V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "JUNO E/J/SS WAVES CALIBRATED SURVEY FULL RESOLUTION V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/YSR6IA5057XX",
             "citation": "Global Modeling and Assimilation Office (GMAO). 2015-06-30. M2TMNPUDT. Version 5.12.4. MERRA-2 tavgM_3d_udt_Np: 3d,Monthly mean,Time-Averaged,Pressure-Level,Assimilation,Wind Tendencies V5.12.4. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/YSR6IA5057XX. https://disc.gsfc.nasa.gov/datacollection/M2TMNPUDT_5.12.4.html. Digital Science Data.",
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
-                "atmosphere",
-                "atmospheric winds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DANA OSTRENGA",
                 "hasEmail": "mailto:dana.ostrenga@nasa.gov"
             },
+            "creator": "Global Modeling and Assimilation Office (GMAO)",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1276812944-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "M2TMNPUDT (or  tavgM_3d_udt_Np) is a 3-dimensional monthly mean data collection in Modern-Era Retrospective analysis for Research and Applications version 2 (MERRA-2).  This collection consists of assimilations of wind tendencies on 42 pressure levels, such as total eastward (or northward) wind analysis tendency,  tendency of eastward (or northward) wind due to dynamics,  and tendency of eastward (or northward) wind due to turbulence. The information on the pressure levels can be found in the section 4.2 of the MERRA-2 File Specification document.   The collection also includes variance of certain parameters.\n\nMERRA-2 is the latest version of global atmospheric reanalysis for the satellite era produced by NASA Global Modeling and Assimilation Office (GMAO) using the Goddard Earth Observing System Model (GEOS) version 5.12.4.  The dataset covers the period of 1980-present with the latency of ~3 weeks after the end of a month. \n\nData Reprocessing:  Please check \u201cRecords of MERRA-2 Data Reprocessing and Service Changes\u201d linked from the \u201cDocumentation\u201d tab on this page.  Note that a reprocessed data filename is different from the original file.\n\nMERRA-2 Mailing List: Sign up to receive information on reprocessing of data, changing of tools and services, as well as data announcements from GMAO. Contact the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov) to be added to the list.\n\nQuestions: If you have a question, please read \"MERRA-2 File Specification Document\",  \u201cMERRA-2 Data Access \u2013 Quick Start Guide\u201d, and FAQs linked from the \u201dDocumentation\u201d tab on this page.  If that does not answer your question, you may email the question on data access to the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov), or the question on science to the MERRA-2 science team (merra-questions@lists.nasa.gov).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "M2TMNPUDT",
-            "creator": "Global Modeling and Assimilation Office (GMAO)",
-            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
-            "title": "MERRA-2 tavgM_3d_udt_Np: 3d,Monthly mean,Time-Averaged,Pressure-Level,Assimilation,Wind Tendencies 0.625 x 0.5 degree V5.12.4 (M2TMNPUDT) at GES DISC",
-            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=M2TMNPUDT",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FYSR6IA5057XX",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FYSR6IA5057XX",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2TMNPUDT_5.12.4.png",
-                    "description": "M2TMNPUDT variable",
                     "@type": "dcat:Distribution",
+                    "description": "M2TMNPUDT variable",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2TMNPUDT_5.12.4.png",
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
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2TMNPUDT_5.12.4.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2TMNPUDT_5.12.4.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2_MONTHLY/M2TMNPUDT.5.12.4/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2_MONTHLY/M2TMNPUDT.5.12.4/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=M2TMNPUDT",
-                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
                     "@type": "dcat:Distribution",
+                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=M2TMNPUDT",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through GIOVANNI"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2TMNPUDT",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2TMNPUDT",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/dods/M2TMNPUDT.info",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/dods/M2TMNPUDT.info",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/opendap/MERRA2_MONTHLY/M2TMNPUDT.5.12.4/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/opendap/MERRA2_MONTHLY/M2TMNPUDT.5.12.4/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_MONTHLY_aggregation//M2TMNPUDT.5.12.4/catalog.html",
-                    "description": "Time aggregated THREDDS Data Server (TDS) ",
                     "@type": "dcat:Distribution",
+                    "description": "Time aggregated THREDDS Data Server (TDS) ",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_MONTHLY_aggregation//M2TMNPUDT.5.12.4/catalog.html",
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
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2_MONTHLY/M2TMNPUDT.5.12.4/doc/MERRA2.README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2_MONTHLY/M2TMNPUDT.5.12.4/doc/MERRA2.README.pdf",
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
+            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=M2TMNPUDT",
+            "identifier": "C1276812944-GES_DISC",
+            "issued": "2007-06-14",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric winds"
+            ],
+            "landingPage": "https://doi.org/10.5067/YSR6IA5057XX",
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
+            "series-name": "M2TMNPUDT",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1980-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "MERRA-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MERRA-2 tavgM_3d_udt_Np: 3d,Monthly mean,Time-Averaged,Pressure-Level,Assimilation,Wind Tendencies 0.625 x 0.5 degree V5.12.4 (M2TMNPUDT) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-2-ESC1-MTP010-V1.0",
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
+            "description": "This data set contains count rates (1/s) as measured by the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, along with their standard deviations.  The primary target is comet 67P/Churyumov-Gerasimenko. These are CODMAC Level 2 Experiment Data Record data, and provide a measure of the radiation in the spacecraft environment during the Medium Term Plan 10 period of the ESCORT 1 mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-2-esc1-mtp010-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-2-ESC1-MTP010-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-2-esc1-mtp010-v1.0",
-            "description": "This data set contains count rates (1/s) as measured by the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, along with their standard deviations.  The primary target is comet 67P/Churyumov-Gerasimenko. These are CODMAC Level 2 Experiment Data Record data, and provide a measure of the radiation in the spacecraft environment during the Medium Term Plan 10 period of the ESCORT 1 mission phase.",
-            "title": "ROSETTA-ORBITER 67P SREM 2 ESCORT 1\n    MTP010 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P SREM 2 ESCORT 1\n    MTP010 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-RSS-1-SAGR18-V1.0",
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
-                "saturn",
-                "cassini-huygens"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Cassini Radio Science Saturn Gravity and Ring Occultation experiments (SAGR18) Raw Data Archive is a time-ordered collection of radio science raw data acquired on  May 8, 15, 21, June 9, and 22, 2017, during the Cassini Extended Extended Mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-rss-1-sagr18-v1.0_fbti-uiv4",
+            "issued": "2018-09-05",
+            "keyword": [
+                "saturn",
+                "cassini-huygens"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-RSS-1-SAGR18-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-rss-1-sagr18-v1.0_fbti-uiv4",
-            "description": "The Cassini Radio Science Saturn Gravity and Ring Occultation experiments (SAGR18) Raw Data Archive is a time-ordered collection of radio science raw data acquired on  May 8, 15, 21, June 9, and 22, 2017, during the Cassini Extended Extended Mission.",
-            "title": "CASSINI RSS RAW DATA SET - SAGR18 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI RSS RAW DATA SET - SAGR18 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VJ121A1N.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Glynn Hulley, Simon Hook. 2023-06-29. VIIRS/JPSS1 Land Surface Temperature/Emissivity Daily L3 Global 1km SIN Grid Night V002. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VJ121A1N.002. https://doi.org/10.5067/VIIRS/VJ121A1N.002. This data set was provided by the NASA/NOAA NPP Project. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
-            "issued": "2023-06-29",
-            "temporal": "2018-01-01T00:00:00Z/2024-06-03T00:00:00Z",
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
-            "identifier": "C2545310892-LPCLOUD",
-            "description": "The NOAA-20 Visible Infrared Imaging Radiometer Suite (VIIRS) Land Surface Temperature and Emissivity (LST&E) Night Version 2 product (VJ121A1N) is compiled daily from nighttime Level 2 Gridded (L2G) intermediate products.  \r\n\r\nThe L2G process maps the daily (VJ121) (https://doi.org/10.5067/VIIRS/VJ121.002) swath granules onto a sinusoidal MODIS grid and stores all observations overlapping a gridded cell for a given night. The VJ121A1 algorithm sorts through all these observations for each cell and estimates the final LST value as an average from all cloud-free observations that have good LST accuracies. The nighttime average is weighted by the observation coverage for that cell. Only observations having observation coverage more than a certain threshold (15%) are considered for this averaging. The 1 kilometer dataset is derived through resampling the native 750 meter VIIRS resolution in the input product.\r\n\r\nThe VJ121A1N product is developed synergistically with the Moderate Resolution Imaging Spectroradiometer (MODIS) LST&E Version 6.1 product (MOD21A1N) (https://doi.org/10.5067/MODIS/MOD21A1N.061) using the same input atmospheric products and algorithmic approach. The overall objective for NASA VIIRS products is to ensure the algorithms and products are compatible with the MODIS Terra and Aqua algorithms to promote the continuity of the Earth Observation System (EOS) mission. Additional details regarding the method used to create this Level 3 (L3) product are available in the Algorithm Theoretical Basis Document (ATBD) (https://lpdaac.usgs.gov/documents/1332/VNP21_ATBD_V1.pdf).\r\n\r\nThe VJ121A1N product contains seven Science Datasets (SDS): LST, quality control, emissivity for bands M14, M15, and M16, view zenith angle, and time of observation. A low-resolution browse image for LST is also available for each VJ121A1N granule.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "Glynn Hulley, Simon Hook",
-            "title": "VIIRS/JPSS1 Land Surface Temperature/Emissivity Daily L3 Global 1km SIN Grid Night V002",
-            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2725293125-LPCLOUD?h=85&w=85",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The NOAA-20 Visible Infrared Imaging Radiometer Suite (VIIRS) Land Surface Temperature and Emissivity (LST&E) Night Version 2 product (VJ121A1N) is compiled daily from nighttime Level 2 Gridded (L2G) intermediate products.  \r\n\r\nThe L2G process maps the daily (VJ121) (https://doi.org/10.5067/VIIRS/VJ121.002) swath granules onto a sinusoidal MODIS grid and stores all observations overlapping a gridded cell for a given night. The VJ121A1 algorithm sorts through all these observations for each cell and estimates the final LST value as an average from all cloud-free observations that have good LST accuracies. The nighttime average is weighted by the observation coverage for that cell. Only observations having observation coverage more than a certain threshold (15%) are considered for this averaging. The 1 kilometer dataset is derived through resampling the native 750 meter VIIRS resolution in the input product.\r\n\r\nThe VJ121A1N product is developed synergistically with the Moderate Resolution Imaging Spectroradiometer (MODIS) LST&E Version 6.1 product (MOD21A1N) (https://doi.org/10.5067/MODIS/MOD21A1N.061) using the same input atmospheric products and algorithmic approach. The overall objective for NASA VIIRS products is to ensure the algorithms and products are compatible with the MODIS Terra and Aqua algorithms to promote the continuity of the Earth Observation System (EOS) mission. Additional details regarding the method used to create this Level 3 (L3) product are available in the Algorithm Theoretical Basis Document (ATBD) (https://lpdaac.usgs.gov/documents/1332/VNP21_ATBD_V1.pdf).\r\n\r\nThe VJ121A1N product contains seven Science Datasets (SDS): LST, quality control, emissivity for bands M14, M15, and M16, view zenith angle, and time of observation. A low-resolution browse image for LST is also available for each VJ121A1N granule.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ121A1N.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ121A1N.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2545310892-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2545310892-LPCLOUD",
+                    "mediaType": "text/html",
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
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VJ121A1N.002",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VJ121A1N.002",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2725293125-LPCLOUD?h=85&w=85",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2725293125-LPCLOUD?h=85&w=85",
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
+            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2725293125-LPCLOUD?h=85&w=85",
+            "identifier": "C2545310892-LPCLOUD",
+            "issued": "2023-06-29",
+            "keyword": [
+                "land surface",
+                "surface radiative properties",
+                "earth science",
+                "surface thermal properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VJ121A1N.002",
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
+            "temporal": "2018-01-01T00:00:00Z/2024-06-03T00:00:00Z",
             "theme": [
                 "JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/JPSS1 Land Surface Temperature/Emissivity Daily L3 Global 1km SIN Grid Night V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CAMEX-4/NAV/DATA103",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Yarbrough, Sky  and Gloria  Fields.2002. CAMEX-4 ER-2 NAVIGATION DATA [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/CAMEX-4/NAV/DATA103",
-            "issued": "2002-02-08",
-            "temporal": "2001-08-18T17:31:49Z/2001-09-25T01:19:11Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-23",
-            "keyword": [
-                "atmospheric winds",
-                "atmosphere",
-                "atmospheric temperature",
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
-            "identifier": "C1979099479-GHRC_DAAC",
             "description": "The CAMEX-4 ER-2 Navigation data files contain information recorded by on board navigation and data collection systems. In addition to typical navigation data (e.g. date, time, lat/lon and altitude) these files contain outside meteorological parameters such as wind speed and direction and temperature. These ascii text files was recorded every second for the length of the sortie. Additionally, graphical representations of these measured parameters are shown in .gif files.",
-            "graphic-preview-description": "N/A",
-            "title": "CAMEX-4 ER-2 NAVIGATION DATA V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex4/NAV_ER-2/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAMEX-4%2FNAV%2FDATA103",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAMEX-4%2FNAV%2FDATA103",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=c4enav",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=c4enav",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex4/NAV_ER-2/browse/c4enav_2001-131_par_2.gif",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex4/NAV_ER-2/browse/c4enav_2001-131_par_2.gif",
+                    "mediaType": "image/gif",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/camex4/c4enav/c4enav_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/camex4/c4enav/c4enav_dataset.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex4/NAV_ER-2/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex4/NAV_ER-2/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex4/NAV_ER-2/browse/",
+            "identifier": "C1979099479-GHRC_DAAC",
+            "issued": "2002-02-08",
+            "keyword": [
+                "atmospheric winds",
+                "atmosphere",
+                "atmospheric temperature",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/CAMEX-4/NAV/DATA103",
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
             "spatial": "-88.4781 16.5617 -63.4356 39.4583",
+            "temporal": "2001-08-18T17:31:49Z/2001-09-25T01:19:11Z",
             "theme": [
                 "CAMEX-4",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CAMEX-4 ER-2 NAVIGATION DATA V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aast_lightcurve_derived_parameters&version=1.0",
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
-                "none",
-                "multiple asteroids"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This is a compilation of published       rotational parameters derived from lightcurve data for asteroids,      based on the Warner et al. (2009) Asteroid Lightcurve Database.  This  is the version as of February 3, 2017.  In addition to reported        rotational parameters by individual papers, there is a summary file    with the values adopted by Harris, Warner, and Pravec as the most      likely correct values for each asteroid.  The data set also contains   files listing known binary asteroids, asteroid spin axes, and          'tumbling' asteroids.",
+            "identifier": "urn:nasa:pds:ast_lightcurve_derived_parameters_fc2n-gpcf",
+            "issued": "2021-05-21",
+            "keyword": [
+                "none",
+                "multiple asteroids"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aast_lightcurve_derived_parameters&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:ast_lightcurve_derived_parameters_fc2n-gpcf",
-            "description": "This is a compilation of published       rotational parameters derived from lightcurve data for asteroids,      based on the Warner et al. (2009) Asteroid Lightcurve Database.  This  is the version as of February 3, 2017.  In addition to reported        rotational parameters by individual papers, there is a summary file    with the values adopted by Harris, Warner, and Pravec as the most      likely correct values for each asteroid.  The data set also contains   files listing known binary asteroids, asteroid spin axes, and          'tumbling' asteroids.",
-            "title": "ASTEROID LIGHTCURVE DERIVED DATA",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ASTEROID LIGHTCURVE DERIVED DATA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-VIRTIS-3-ESC2-MTP015-V2.0",
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
+            "description": "This release contains the calibrated data of the VIRTIS instrument on board of the spacecraft Rosetta. This volume contains data from the ESCORT 2 MTP015 phase, which occurred from 2015-04-08 to 2015-05-06 when at the vicinity of comet 67P. This data set V2.0 supersedes V1.0. It includes major updates on the data and documentation.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-virtis-3-esc2-mtp015-v2.0_fc34-24m8",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-VIRTIS-3-ESC2-MTP015-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-virtis-3-esc2-mtp015-v2.0_fc34-24m8",
-            "description": "This release contains the calibrated data of the VIRTIS instrument on board of the spacecraft Rosetta. This volume contains data from the ESCORT 2 MTP015 phase, which occurred from 2015-04-08 to 2015-05-06 when at the vicinity of comet 67P. This data set V2.0 supersedes V1.0. It includes major updates on the data and documentation.",
-            "title": "ROSETTA-ORBITER 67P VIRTIS 3 ESCORT 2 MTP015 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P VIRTIS 3 ESCORT 2 MTP015 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-MIRO-3-CVP-COMMISSIONING-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Spectroscopic and Continuum data, in the form of table files, taken during the Commissioning phase of the Rosetta mission by the MIRO instrument. These data have been calibrated to antenna temperatures.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-miro-3-cvp-commissioning-v1.0_fc34-4abz",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "m42",
@@ -750569,393 +750571,405 @@
                 "c/linear (2002 t7)",
                 "earth"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-MIRO-3-CVP-COMMISSIONING-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-miro-3-cvp-commissioning-v1.0_fc34-4abz",
-            "description": "This data set contains Spectroscopic and Continuum data, in the form of table files, taken during the Commissioning phase of the Rosetta mission by the MIRO instrument. These data have been calibrated to antenna temperatures.",
-            "title": "ROSETTA-ORBITER CHECK MIRO 3 CVP COMMISSIONING V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECK MIRO 3 CVP COMMISSIONING V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/MC3E/2DVD/DATA301",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Petersen, Walter A, Ali  Tokay, Patrick N Gatlin and Matthew T. Wingo.2012. GPM GROUND VALIDATION TWO-DIMENSIONAL VIDEO DISDROMETER (2DVD) MC3E [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/MC3E/2DVD/DATA301",
-            "issued": "2012-02-24",
-            "temporal": "2011-04-21T16:22:00Z/2011-06-06T17:13:25Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-09",
-            "keyword": [
-                "atmosphere",
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
-            "identifier": "C1979123780-GHRC_DAAC",
             "description": "The GPM Ground Validation Two-Dimensional Video Disdrometer (2DVD) MC3E dataset was collected during the  Midlatitude Continental Convective Clouds Experiment (MC3E), which provides data on raindrop size and precipitation drop size distribution. The MC3E took place in central Oklahoma during the April-June 2011 period. The experiment was a collaborative effort between the U.S. Department of Energy (DOE) Atmospheric Radiation Measurement (ARM) Climate Research Facility and the National Aeronautics and Space Administration's (NASA) Global Precipitation Measurement (GPM) mission Ground Validation (GV) program. The field campaign leveraged the unprecedented observing infrastructure currently available in the central United States, combined with an extensive sounding array, remote sensing and in situ aircraft observations, NASA GPM ground validation remote sensors, and new ARM instrumentation purchased with American Recovery and Reinvestment Act funding. The overarching goal was to provide the most complete characterization of convective cloud systems, precipitation, and the environment that has ever been obtained, providing constraints for model cumulus parameterizations and space-based rainfall retrieval algorithms over land that had never before been available.",
-            "title": "GPM GROUND VALIDATION TWO-DIMENSIONAL VIDEO DISDROMETER (2DVD) MC3E V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FMC3E%2F2DVD%2FDATA301",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FMC3E%2F2DVD%2FDATA301",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpm2dmc3e",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpm2dmc3e",
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
-                    "downloadURL": "http://pmm.nasa.gov/GPM",
-                    "description": "GPM Mission Concept",
                     "@type": "dcat:Distribution",
+                    "description": "GPM Mission Concept",
+                    "downloadURL": "http://pmm.nasa.gov/GPM",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/gpmgv/2dvd/gpm_2dvd_campaign_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/gpmgv/2dvd/gpm_2dvd_campaign_dataset.html",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/micro-articles/instrument-2dvd-disdrometer",
-                    "description": "Instrument: 2DVD Disdrometer Micro Article",
                     "@type": "dcat:Distribution",
+                    "description": "Instrument: 2DVD Disdrometer Micro Article",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/micro-articles/instrument-2dvd-disdrometer",
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
+            "identifier": "C1979123780-GHRC_DAAC",
+            "issued": "2012-02-24",
+            "keyword": [
+                "atmosphere",
+                "precipitation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/MC3E/2DVD/DATA301",
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
             "spatial": "-97.5323 36.5784 -97.4447 36.6334",
+            "temporal": "2011-04-21T16:22:00Z/2011-06-06T17:13:25Z",
             "theme": [
                 "MC3E",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM GROUND VALIDATION TWO-DIMENSIONAL VIDEO DISDROMETER (2DVD) MC3E V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1272-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-20T17:47:35.000 to 2015-12-21T01:18:04.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1272-v1.0_fc46-r6ga",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1272-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1272-v1.0_fc46-r6ga",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-20T17:47:35.000 to 2015-12-21T01:18:04.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1272 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1272 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-APD-POLARIMETRY-V8.0",
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
+            "description": "The Asteroid Polarimetric Database (APD) is a collection of asteroid polarimetry results compiled by D.F. Lupishko of Karazin Kharkiv National University, Ukraine. It is intended to include most asteroid polarimetry available through Feb. 10, 2014.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-apd-polarimetry-v8.0_fc5n-mbx6",
+            "issued": "2021-05-21",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-APD-POLARIMETRY-V8.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-apd-polarimetry-v8.0_fc5n-mbx6",
-            "description": "The Asteroid Polarimetric Database (APD) is a collection of asteroid polarimetry results compiled by D.F. Lupishko of Karazin Kharkiv National University, Ukraine. It is intended to include most asteroid polarimetry available through Feb. 10, 2014.",
-            "title": "ASTEROID POLARIMETRIC DATABASE V8.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ASTEROID POLARIMETRIC DATABASE V8.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL3QRD_L3.005",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Component Global Radiance Product for a quarter (seasonal);See ProductionDateTime for Published date.",
-            "issued": "2003-12-03",
-            "temporal": "1999-12-18T00:00:00Z/2022-01-17T00:00:00Z",
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
-            "identifier": "C43677732-LARC",
             "description": "This file contains the MISR Level 3 Component Global Radiance Product covering a quarter (seasonal)",
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "title": "MISR Level 3 Component Global Radiance Product covering a quarter (seasonal) V005",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL3QRD_L3.005",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL3QRD_L3.005",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 }
             ],
+            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
+            "identifier": "C43677732-LARC",
+            "issued": "2003-12-03",
+            "keyword": [
+                "nasa"
+            ],
+            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL3QRD_L3.005",
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
+            "temporal": "1999-12-18T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR Level 3 Component Global Radiance Product covering a quarter (seasonal) V005"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43MA2.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler\r\n. 2018-11-17. VNP43MA2. Version 001. VIIRS/NPP BRDF/Albedo Quality Daily L3 Global 1km SIN Grid V001\r\n. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VNP43MA2.001 . https://doi.org/10.5067/VIIRS/VNP43MA2.001. Digital Science Data. This data set was provided by the NASA/NOAA NPP Project. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
-            "issued": "2018-11-17",
-            "temporal": "2012-01-17T00:00:00Z/2024-06-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-11-17",
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
-            "identifier": "C1412449612-LPDAAC_ECS",
-            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Quality (VNP43MA2) Version 1 product provides BRDF and Albedo quality at 1 kilometer (km) resolution. The VNP43MA2 product is produced daily using 16 days of VIIRS data and is weighted temporally to the ninth day, which is reflected in the file name. The VNP43MA2 product gives information regarding band quality and days of valid observation within a 16-day period for nine VIIRS moderate resolution bands and three broadbands. The VNP43 data products are designed to promote the continuity of NASA\u2019s Moderate Resolution Imaging Spectroradiometer (MODIS) BRDF/Albedo data product suite. \r\n\r\nThe VNP43 algorithm uses the RossThick/Li-Sparse-Reciprocal (RTLSR) semi-empirical kernel-driven BRDF model, with the three kernel weights from (VNP43MA1) \r\n(https://doi.org/10.5067/VIIRS/VNP43MA1.001) to reconstruct surface anisotropic effects, correcting the directional reflectance to a common view geometry (VNP43MA4) (https://doi.org/10.5067/VIIRS/VNP43MA4.001), while also computing integrated black-sky albedo (BSA) at local solar noon and white-sky albedo (WSA) (VNP43MA3) (https://doi.org/10.5067/VIIRS/VNP43MA3.001). Researchers can use the BRDF model parameters with a simple polynomial, to obtain black-sky albedo at any solar illumination angle. Likewise, both the BSA and WSA Science Dataset (SDS) layers can be used with a simple polynomial, to manually estimate instantaneous actual albedo (blue-sky albedo). Additional details regarding the methodology are available in the Algorithm Theoretical Basis Document (ATBD) (https://lpdaac.usgs.gov/documents/194/VNP43_ATBD_V1.pdf).\r\n\r\nThe VNP43MA2 data product provides a total of 23 SDS layers including: BRDF/Albedo band quality and days of valid observation within a 16-day period for VIIRS moderate resolution bands: M1-M5, M7-M8, and M10-M11, as well as land water type class flag, snow BRDF albedo class flag, local solar noon, albedo uncertainty and the platform name.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "VNP43MA2",
             "creator": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler",
-            "title": "VIIRS/NPP BRDF/Albedo Quality Daily L3 Global 1km SIN Grid V001",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Quality (VNP43MA2) Version 1 product provides BRDF and Albedo quality at 1 kilometer (km) resolution. The VNP43MA2 product is produced daily using 16 days of VIIRS data and is weighted temporally to the ninth day, which is reflected in the file name. The VNP43MA2 product gives information regarding band quality and days of valid observation within a 16-day period for nine VIIRS moderate resolution bands and three broadbands. The VNP43 data products are designed to promote the continuity of NASA\u2019s Moderate Resolution Imaging Spectroradiometer (MODIS) BRDF/Albedo data product suite. \r\n\r\nThe VNP43 algorithm uses the RossThick/Li-Sparse-Reciprocal (RTLSR) semi-empirical kernel-driven BRDF model, with the three kernel weights from (VNP43MA1) \r\n(https://doi.org/10.5067/VIIRS/VNP43MA1.001) to reconstruct surface anisotropic effects, correcting the directional reflectance to a common view geometry (VNP43MA4) (https://doi.org/10.5067/VIIRS/VNP43MA4.001), while also computing integrated black-sky albedo (BSA) at local solar noon and white-sky albedo (WSA) (VNP43MA3) (https://doi.org/10.5067/VIIRS/VNP43MA3.001). Researchers can use the BRDF model parameters with a simple polynomial, to obtain black-sky albedo at any solar illumination angle. Likewise, both the BSA and WSA Science Dataset (SDS) layers can be used with a simple polynomial, to manually estimate instantaneous actual albedo (blue-sky albedo). Additional details regarding the methodology are available in the Algorithm Theoretical Basis Document (ATBD) (https://lpdaac.usgs.gov/documents/194/VNP43_ATBD_V1.pdf).\r\n\r\nThe VNP43MA2 data product provides a total of 23 SDS layers including: BRDF/Albedo band quality and days of valid observation within a 16-day period for VIIRS moderate resolution bands: M1-M5, M7-M8, and M10-M11, as well as land water type class flag, snow BRDF albedo class flag, local solar noon, albedo uncertainty and the platform name.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43MA2.001+",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43MA2.001+",
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
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43MA2.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43MA2.001",
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
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43MA2.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43MA2.001/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1412449612-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1412449612-LPDAAC_ECS",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.umb.edu/spectralmass/viirs-user-guide/vnp43ia2-and-vnp43ma2-brdf-albedo-quality-product/",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://www.umb.edu/spectralmass/viirs-user-guide/vnp43ia2-and-vnp43ma2-brdf-albedo-quality-product/",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43MA2",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43MA2",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP104/VIIRS/VNP43MA2.001/contents.html",
-                    "description": "OPeNDAP provides direct access to data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP provides direct access to data via HTTPS.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP104/VIIRS/VNP43MA2.001/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
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
+            "identifier": "C1412449612-LPDAAC_ECS",
+            "issued": "2018-11-17",
+            "keyword": [
+                "surface radiative properties",
+                "land surface",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43MA2.001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-11-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
+            "series-name": "VNP43MA2",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-17T00:00:00Z/2024-06-03T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP BRDF/Albedo Quality Daily L3 Global 1km SIN Grid V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/fc9e-f5eq",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Certain mouse strains such as CBA C3H and RFM have high incidence of radiation-induced acute myeloid leukemia (AML). The data in this series wer generated by using spleen DNA from CBA mice which were irraidated with either gamma-rays or heavy ion (HZE) particles. Spleen DNA with radiation-induced AML was compared with DNA from normal CBA mice. Comparison of spleen DNA from CBA mice with radiation-induced AML vs genomic DNA from normal CBA mice",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-94",
+                    "mediaType": "text/html",
+                    "title": "DNA copy number analysis from mice with radiation-induced acute myeloid leukemia"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-94_fc9e-f5eq",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "nucleic_acid_extraction",
                 "p-gse37233-1",
@@ -750973,301 +750987,265 @@
                 "p-gse37233-6",
                 "p-gse37233-7"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/fc9e-f5eq",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-94_fc9e-f5eq",
-            "description": "Certain mouse strains such as CBA C3H and RFM have high incidence of radiation-induced acute myeloid leukemia (AML). The data in this series wer generated by using spleen DNA from CBA mice which were irraidated with either gamma-rays or heavy ion (HZE) particles. Spleen DNA with radiation-induced AML was compared with DNA from normal CBA mice. Comparison of spleen DNA from CBA mice with radiation-induced AML vs genomic DNA from normal CBA mice",
-            "title": "DNA copy number analysis from mice with radiation-induced acute myeloid leukemia",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-94",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "DNA copy number analysis from mice with radiation-induced acute myeloid leukemia"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "DNA copy number analysis from mice with radiation-induced acute myeloid leukemia"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NR1VABD1ZDTQ",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "IceBridge Photon Counting Lidar L1B Subset Geolocated Photon Elevations V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/NR1VABD1ZDTQ.",
-            "issued": "2010-11-25",
-            "temporal": "2010-11-25T00:00:00Z/2012-12-11T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2012-12-11",
-            "keyword": [
-                "cryosphere",
-                "glaciers/ice sheets",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Donald Blankenship",
                 "hasEmail": "mailto:blank@ig.utexas.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1000000542-NSIDC_ECS",
             "description": "This data set contains nadir photon counting data captured over Antarctica using the Sigma Space photon counting lidar. Position and orientation data are included. The data were collected by scientists working on the International Collaborative Exploration of the Cryosphere through Airborne Profiling (ICECAP) project, which was funded by the National Science Foundation (NSF), the Antarctic Climate and Ecosystems Collaborative Research Center, and the Natural Environment Research Council (NERC) with additional support from NASA Operation IceBridge.",
-            "title": "IceBridge Photon Counting Lidar L1B Subset Geolocated Photon Elevations V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNR1VABD1ZDTQ",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNR1VABD1ZDTQ",
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
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/ILSNP1B.001",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/ILSNP1B.001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000542-NSIDC_ECS&m=-62.25404112259866%21138.40451829948873%210%212%210%210%2C2&tl=1513802945%214%21%21&q=ILSNP1B",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000542-NSIDC_ECS&m=-62.25404112259866%21138.40451829948873%210%212%210%210%2C2&tl=1513802945%214%21%21&q=ILSNP1B",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/ILSNP1B/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/ILSNP1B/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/NR1VABD1ZDTQ",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/NR1VABD1ZDTQ",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/NR1VABD1ZDTQ",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/NR1VABD1ZDTQ",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1000000542-NSIDC_ECS",
+            "issued": "2010-11-25",
+            "keyword": [
+                "cryosphere",
+                "glaciers/ice sheets",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/NR1VABD1ZDTQ",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2012-12-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 -53.0",
+            "temporal": "2010-11-25T00:00:00Z/2012-12-11T23:59:59.999Z",
             "theme": [
                 "2010_AN_UTIG",
                 "2011_AN_UTIG",
                 "2012_AN_UTIG",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "IceBridge Photon Counting Lidar L1B Subset Geolocated Photon Elevations V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1898",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wagner, N.L., C.A. Brock, C.J. Williamson, A. Kupc, K.D. Froyd, and D.M. Murphy. 2021. ATom: Aerosol Extinction and Absorption Measurements from SOAP Instrument, 2018. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1898",
-            "issued": "2021-12-20",
-            "temporal": "2018-04-24T00:00:00Z/2018-05-21T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "atmospheric radiation",
-                "earth science",
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
-            "identifier": "C2677187997-ORNL_CLOUD",
             "description": "This dataset contains one-second aerosol extinction and absorption measurements from the Spectrometers for Optical Aerosol Properties (SOAP) instrument aboard the NASA DC-8 aircraft during the ATom-4 campaign that occurred in 2018. SOAP is a compact, low maintenance instrument that measures aerosol extinction and absorption at 532 nm. Aerosol extinction is measured by cavity ringdown spectroscopy and aerosol absorption by photoacoustic spectroscopy. Extinction is measured with sufficient precision and accuracy for the remote atmosphere. The absorption measurements are valid only in strongly absorbing cases, such as in dilute plumes from wildfire smoke. The absorption and extinction of visible light by aerosol particles is a major component of the earth's radiation budget, strongly affecting climate. Highly absorbing particles directly heat the atmosphere, while particles that scatter light tend to cool the atmosphere. Extinction is the sum of absorption and scattering; in most cases scattering represents >90% of extinction, with absorption making up the remainder. These aerosol-radiation interactions also alter air temperature and the rates of photochemical reactions.",
-            "graphic-preview-description": "(a) Aerosol extinction calculated using Mie theory from composition-resolved size distributions plotted as a function of measured extinction from the SOAP cavity ring-down spectrometer during the ATom-4 campaign, showing representative error bars. (b) Calculated aerosol absorption and measured absorption from the SOAP photoacoustic spectrometer for cases when absorption >2 *10-6 m-1 (2x the detection limit).",
-            "title": "ATom: Aerosol Extinction and Absorption Measurements from SOAP Instrument, 2018",
-            "graphic-preview-file": "https://daac.ornl.gov/ATOM/guides/ATom_SOAP_Instrument_Data_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1898",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1898",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/atom/ATom_SOAP_Instrument_Data/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/atom/ATom_SOAP_Instrument_Data/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_SOAP_Instrument_Data.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_SOAP_Instrument_Data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1898",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1898",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_SOAP_Instrument_Data/comp/ATom_SOAP_Instrument_Data.pdf",
-                    "description": "ATom: Aerosol Extinction and Absorption Measurements from SOAP Instrument, 2018: ATom_SOAP_Instrument_Data.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ATom: Aerosol Extinction and Absorption Measurements from SOAP Instrument, 2018: ATom_SOAP_Instrument_Data.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_SOAP_Instrument_Data/comp/ATom_SOAP_Instrument_Data.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_SOAP_Instrument_Data_Fig1.png",
-                    "description": "(a) Aerosol extinction calculated using Mie theory from composition-resolved size distributions plotted as a function of measured extinction from the SOAP cavity ring-down spectrometer during the ATom-4 campaign, showing representative error bars. (b) Calculated aerosol absorption and measured absorption from the SOAP photoacoustic spectrometer for cases when absorption >2 *10-6 m-1 (2x the detection limit).",
                     "@type": "dcat:Distribution",
+                    "description": "(a) Aerosol extinction calculated using Mie theory from composition-resolved size distributions plotted as a function of measured extinction from the SOAP cavity ring-down spectrometer during the ATom-4 campaign, showing representative error bars. (b) Calculated aerosol absorption and measured absorption from the SOAP photoacoustic spectrometer for cases when absorption >2 *10-6 m-1 (2x the detection limit).",
+                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_SOAP_Instrument_Data_Fig1.png",
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
+            "graphic-preview-description": "(a) Aerosol extinction calculated using Mie theory from composition-resolved size distributions plotted as a function of measured extinction from the SOAP cavity ring-down spectrometer during the ATom-4 campaign, showing representative error bars. (b) Calculated aerosol absorption and measured absorption from the SOAP photoacoustic spectrometer for cases when absorption >2 *10-6 m-1 (2x the detection limit).",
+            "graphic-preview-file": "https://daac.ornl.gov/ATOM/guides/ATom_SOAP_Instrument_Data_Fig1.png",
+            "identifier": "C2677187997-ORNL_CLOUD",
+            "issued": "2021-12-20",
+            "keyword": [
+                "atmospheric radiation",
+                "earth science",
+                "atmosphere",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1898",
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
+            "temporal": "2018-04-24T00:00:00Z/2018-05-21T23:59:59Z",
             "theme": [
                 "ATom",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ATom: Aerosol Extinction and Absorption Measurements from SOAP Instrument, 2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-MAG-4-RDR-L1COORDS-1.92SEC-V1.1",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-mag-4-rdr-l1coords-1.92sec-v1.1_fcd4-uftv",
+            "issued": "2018-06-26",
+            "keyword": [
+                "voyager",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-MAG-4-RDR-L1COORDS-1.92SEC-V1.1",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-mag-4-rdr-l1coords-1.92sec-v1.1_fcd4-uftv",
-            "description": "not applicable",
-            "title": "VG2 SAT MAG RESAMPLED KRONOGRAPHIC (L1) COORDS 1.92SEC V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG2 SAT MAG RESAMPLED KRONOGRAPHIC (L1) COORDS 1.92SEC V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/HIRDLS/DATA309",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Gille, John and Gray, Lesley J.. 2013-08-19. H3ZFCNO2. Version 007. HIRDLS/Aura Level 3 Nitrogen Dioxide (NO2) 1deg Lat Zonal Fourier Coefficients V007. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/HIRDLS/DATA309. https://disc.gsfc.nasa.gov/datacollection/H3ZFCNO2_007.html. Digital Science Data.",
-            "issued": "2013-05-31",
-            "temporal": "2005-01-22T00:00:00Z/2008-03-17T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2013-05-06",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric chemistry"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JOHN GILLE",
                 "hasEmail": "mailto:gille@ucar.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1251101003-GES_DISC",
-            "description": "The \"HIRDLS/Aura Level 3 Nitrogen Dioxide (NO2) Zonal Fourier Coefficients\" version 7 data product (H3ZFCNO2) contains the entire mission (~3 years) of HIRDLS data expressed as zonal Fourier coefficients in 1 degree latitude bands from -64 to 80 degrees at 121 pressure levels. The coefficients are computed from the HIRDLS Level 2 profiles with a Kalman filter approach using both forward and backward passes in time. Expressed as the mean and up to 7 sine and cosine coefficients (4 waves for ascending and descending, 7 waves for combined), these coefficients may be used to compute values at any longitude. The data are provided on a pressure grid with 24 levels per decade, corresponding to about 1 km vertical resolution. The useful vertical range of the data is 100 to 5.1 hPa. The precision values are given by the root-mean square of the differences between the estimated fields and the input data.\n\nThe data are stored in the version 5 Hierarchical Data Format for the Earth Observing System (HDF-EOS5), which is an extension of the HDF5 format. Each file contains a zonal object with data for the entire mission with separate data fields for ascending (daytime), descending (nighttime), and combined orbit node.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "H3ZFCNO2",
             "creator": "Gille, John and Gray, Lesley J.",
-            "title": "HIRDLS/Aura Level 3 Nitrogen Dioxide (NO2) 1deg Lat Zonal Fourier Coefficients V007 (H3ZFCNO2) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/H3ZFCNO2_007.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The \"HIRDLS/Aura Level 3 Nitrogen Dioxide (NO2) Zonal Fourier Coefficients\" version 7 data product (H3ZFCNO2) contains the entire mission (~3 years) of HIRDLS data expressed as zonal Fourier coefficients in 1 degree latitude bands from -64 to 80 degrees at 121 pressure levels. The coefficients are computed from the HIRDLS Level 2 profiles with a Kalman filter approach using both forward and backward passes in time. Expressed as the mean and up to 7 sine and cosine coefficients (4 waves for ascending and descending, 7 waves for combined), these coefficients may be used to compute values at any longitude. The data are provided on a pressure grid with 24 levels per decade, corresponding to about 1 km vertical resolution. The useful vertical range of the data is 100 to 5.1 hPa. The precision values are given by the root-mean square of the differences between the estimated fields and the input data.\n\nThe data are stored in the version 5 Hierarchical Data Format for the Earth Observing System (HDF-EOS5), which is an extension of the HDF5 format. Each file contains a zonal object with data for the entire mission with separate data fields for ascending (daytime), descending (nighttime), and combined orbit node.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FHIRDLS%2FDATA309",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FHIRDLS%2FDATA309",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -751277,102 +751255,138 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/H3ZFCNO2_007.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/H3ZFCNO2_007.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_HIRDLS_Level3/H3ZFCNO2.007/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_HIRDLS_Level3/H3ZFCNO2.007/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_HIRDLS_Level3/H3ZFCNO2.007/HIRDLS-Aura_L3ZFCNO2_v07-00-20-c01_2005d022-2008d077.he5.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_HIRDLS_Level3/H3ZFCNO2.007/HIRDLS-Aura_L3ZFCNO2_v07-00-20-c01_2005d022-2008d077.he5.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=H3ZFCNO2_007",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=H3ZFCNO2_007",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/HIRDLS/3.3_Product_Documentation/3.3.5_Product_Quality/HIRDLS-DQD_V7.pdf",
-                    "description": "README and Data Quality document",
                     "@type": "dcat:Distribution",
+                    "description": "README and Data Quality document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/HIRDLS/3.3_Product_Documentation/3.3.5_Product_Quality/HIRDLS-DQD_V7.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/HIRDLS/3.3_Product_Documentation/3.3.6_Product_Application/All_HIRDLS_Papers_26June2013.pdf",
-                    "description": "List of publications.",
                     "@type": "dcat:Distribution",
+                    "description": "List of publications.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/HIRDLS/3.3_Product_Documentation/3.3.6_Product_Application/All_HIRDLS_Papers_26June2013.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/H3ZFCNO2_007.png",
+            "identifier": "C1251101003-GES_DISC",
+            "issued": "2013-05-31",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/HIRDLS/DATA309",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2013-05-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "H3ZFCNO2",
             "spatial": "-180.0 -64.0 180.0 80.0",
+            "temporal": "2005-01-22T00:00:00Z/2008-03-17T23:59:59.999Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "HIRDLS/Aura Level 3 Nitrogen Dioxide (NO2) 1deg Lat Zonal Fourier Coefficients V007 (H3ZFCNO2) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-TNO-PHOT-V2.0",
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
+            "description": "Published colors of Trans-Neptunian objects through December 2001.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-tno-phot-v2.0_fcek-8b2m",
+            "issued": "2018-06-26",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-TNO-PHOT-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-tno-phot-v2.0_fcek-8b2m",
-            "description": "Published colors of Trans-Neptunian objects through December 2001.",
-            "title": "TRANS-NEPTUNIAN OBJECT PHOTOMETRY V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "TRANS-NEPTUNIAN OBJECT PHOTOMETRY V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/fch4-8qvj",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Transcriptional profiling of human lymphoblastoid TK6 cells comparing mock irradiaed cells resuspended in fresh untreated RPMI 1640 medium with cells resuspended in medium activated by exposure to 2.5 Gy HZE (1 GeV/amu iron ions accelerated at the NASA Space Research Laboratory (NSRL) of Brookhaven National Laboratory). Two-condition experiment mock irradiated vs. cells exposed to activated medium. 3 biological replicates were independently grown and harvested during three different runs at the NSRL. One replicate per array.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-9",
+                    "mediaType": "text/html",
+                    "title": "Response of human lymphoblastoid cells to activated medium"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-9_fch4-8qvj",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "grow",
                 "labeling",
@@ -751392,66 +751406,33 @@
                 "p-gse16519-8",
                 "bioassay_data_transformation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/fch4-8qvj",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-9_fch4-8qvj",
-            "description": "Transcriptional profiling of human lymphoblastoid TK6 cells comparing mock irradiaed cells resuspended in fresh untreated RPMI 1640 medium with cells resuspended in medium activated by exposure to 2.5 Gy HZE (1 GeV/amu iron ions accelerated at the NASA Space Research Laboratory (NSRL) of Brookhaven National Laboratory). Two-condition experiment mock irradiated vs. cells exposed to activated medium. 3 biological replicates were independently grown and harvested during three different runs at the NSRL. One replicate per array.",
-            "title": "Response of human lymphoblastoid cells to activated medium",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-9",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Response of human lymphoblastoid cells to activated medium"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Response of human lymphoblastoid cells to activated medium"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://scanpath.arc.nasa.gov/quip/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2015-01-07",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "quip",
-                "quick",
-                "graphics",
-                "image processing",
-                "scientific computing"
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
-            "identifier": "OCIO-Fitara-135",
             "description": "QuIP (QUick Image Processing) is an interpreter for image processing, graphics, psychophysical experimentation and general scientific computing.",
-            "title": "ARC Code TI: QuIP",
-            "programCode": [
-                "026:046"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -751459,20 +751440,53 @@
                     "mediaType": "application/x-tar"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "OCIO-Fitara-135",
+            "issued": "2015-01-07",
+            "keyword": [
+                "quip",
+                "quick",
+                "graphics",
+                "image processing",
+                "scientific computing"
+            ],
+            "landingPage": "http://scanpath.arc.nasa.gov/quip/",
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
+            "title": "ARC Code TI: QuIP"
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
+            "description": "NASA Financial Budget Documents, Strategic Plans and Performance Reports for fiscal year 2012.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "FY12 NASA Budget Overview",
+                    "downloadURL": "http://www.nasa.gov/pdf/516674main_NASAFY12_Budget_Estimates-Overview-508.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "NASA FY12 Budget Overview"
+                }
+            ],
+            "identifier": "OCIO-Fitara-68",
             "issued": "2011-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "plan",
                 "performance",
@@ -751481,95 +751495,60 @@
                 "budget",
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
-            "identifier": "OCIO-Fitara-68",
-            "description": "NASA Financial Budget Documents, Strategic Plans and Performance Reports for fiscal year 2012.",
-            "title": "NASA Financial Budget Documents, Strategic Plans and Performance Reports 2012: NASA Budget Overview",
-            "programCode": [
-                "026:046"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.nasa.gov/pdf/516674main_NASAFY12_Budget_Estimates-Overview-508.pdf",
-                    "description": "FY12 NASA Budget Overview",
-                    "@type": "dcat:Distribution",
-                    "title": "NASA FY12 Budget Overview"
-                }
-            ],
-            "accrualPeriodicity": "R/P1Y",
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "NASA Financial Budget Documents, Strategic Plans and Performance Reports 2012: NASA Budget Overview"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/244",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Vickers, D., A. Kowalski, L. Mahrt, and K. Kotwica. 1999. BOREAS AFM-11 Aircraft Flux Analysis Reports. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/244",
-            "issued": "2017-09-27",
-            "temporal": "1994-01-01T00:00:00Z/1996-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-01",
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
-            "identifier": "C2759282019-ORNL_CLOUD",
             "description": "Reports from the BOREAS AFM-11 team regarding quality control and sampling analysis of data collected by other AFM personnel using the Electra, LongEZ, and Twin Otter aircraft.   These reports are stored in Adobe Acrobat (.PDF) format.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS AFM-11 Aircraft Flux Analysis Reports",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F244",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F244",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/AFM/afm11afr/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/AFM/afm11afr/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/AFM11_README.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/AFM11_README.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/244",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/244",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
@@ -751585,31 +751564,64 @@
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
+            "identifier": "C2759282019-ORNL_CLOUD",
+            "issued": "2017-09-27",
+            "keyword": [
+                "atmospheric chemistry",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/244",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-09-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-111.0 40.0 -89.0 60.0",
+            "temporal": "1994-01-01T00:00:00Z/1996-12-31T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS AFM-11 Aircraft Flux Analysis Reports"
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
+            "description": "This catalog of LAT sources above 10 GeV reports the locations, spectra, and variability properties of the 514 sources significantly detected in this range during the first three years of the Fermi mission. Many of these sources are already included in the 2FGL catalog, although in that catalog their characterization is dominated by the much larger numbers of gamma rays detected in the energy range 0.1 to 10 GeV.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://fermi.gsfc.nasa.gov/ssc/data/access/lat/1FHL/photthresh_P7v6clean_3years_10GeV.fits",
+                    "mediaType": "image/fits"
+                }
+            ],
+            "identifier": "NASA-0000220__3",
             "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "bursts",
                 "acd",
@@ -751627,200 +751639,166 @@
                 "compton",
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
-            "identifier": "NASA-0000220__3",
-            "description": "This catalog of LAT sources above 10 GeV reports the locations, spectra, and variability properties of the 514 sources significantly detected in this range during the first three years of the Fermi mission. Many of these sources are already included in the 2FGL catalog, although in that catalog their characterization is dominated by the much larger numbers of gamma rays detected in the energy range 0.1 to 10 GeV.",
-            "title": "First Fermi-LAT Catalog of Sources above 10 GeV (1FHL)",
-            "programCode": [
-                "026:014"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://fermi.gsfc.nasa.gov/ssc/data/access/lat/1FHL/photthresh_P7v6clean_3years_10GeV.fits",
-                    "mediaType": "image/fits"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "First Fermi-LAT Catalog of Sources above 10 GeV (1FHL)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Maryland_Aerosol_AircraftInSitu_P3B_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2022-03-21. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Maryland_Aerosol_AircraftInSitu_P3B_Data_1.",
-            "issued": "2021-06-10",
-            "temporal": "2011-06-26T00:00:00Z/2011-07-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-21",
-            "keyword": [
-                "atmosphere",
-                "aerosols",
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
-            "identifier": "C2241805125-LARC_ASDC",
             "description": "DISCOVERAQ_Maryland_Aerosol_AircraftInSitu_P3B_Data contains in situ aerosol data collected onboard NASA's P-3B aircraft during the Maryland (Baltimore-Washington) deployment of NASA's DISCOVER-AQ field study. Instruments utilized to collect data found in this data product include the PSAP, APS, CPC, Nephelometer, LAS, PILS, SMPS, SP2 and UHSAS. This data product contains data for only the Maryland deployment and data collection is complete.\r\n\r\nUnderstanding the factors that contribute to near surface pollution is difficult using only satellite-based observations. The incorporation of surface-level measurements from aircraft and ground-based platforms provides the crucial information necessary to validate and expand upon the use of satellites in understanding near surface pollution. Deriving Information on Surface conditions from Column and Vertically Resolved Observations Relevant to Air Quality (DISCOVER-AQ) was a four-year campaign conducted in collaboration between NASA Langley Research Center, NASA Goddard Space Flight Center, NASA Ames Research Center, and multiple universities to improve the use of satellites to monitor air quality for public health and environmental benefit. Through targeted airborne and ground-based observations, DISCOVER-AQ enabled more effective use of current and future satellites to diagnose ground level conditions influencing air quality.\r\n\r\nDISCOVER-AQ employed two NASA aircraft, the P-3B and King Air, with the P-3B completing in-situ spiral profiling of the atmosphere (aerosol properties, meteorological variables, and trace gas species). The King Air conducted both passive and active remote sensing of the atmospheric column extending below the aircraft to the surface. Data from an existing network of surface air quality monitors, AERONET sun photometers, Pandora UV/vis spectrometers and model simulations were also collected. Further, DISCOVER-AQ employed many surface monitoring sites, with measurements being made on the ground, in conjunction with the aircraft. The B200 and P-3B conducted flights in Baltimore-Washington, D.C. in 2011, Houston, TX in 2013, San Joaquin Valley, CA in 2013, and Denver, CO in 2014. These regions were targeted due to being in violation of the National Ambient Air Quality Standards (NAAQS).\r\n\r\nThe first objective of DISCOVER-AQ was to determine and investigate correlations between surface measurements and satellite column observations for the trace gases ozone (O3), nitrogen dioxide (NO2), and formaldehyde (CH2O) to understand how satellite column observations can diagnose surface conditions. DISCOVER-AQ also had the objective of using surface-level measurements to understand how satellites measure diurnal variability and to understand what factors control diurnal variability. Lastly, DISCOVER-AQ aimed to explore horizontal scales of variability, such as regions with steep gradients and urban plumes.",
-            "title": "DISCOVER-AQ Maryland Deployment P-3B Aircraft In Situ Aerosol Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDISCOVERAQ_Maryland_Aerosol_AircraftInSitu_P3B_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDISCOVERAQ_Maryland_Aerosol_AircraftInSitu_P3B_Data_1",
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
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Maryland_Aerosol_AircraftInSitu_P3B_Data_1",
-                    "description": "DOI Data Set Landing Page for DISCOVERAQ_Maryland_Aerosol_AircraftInSitu_P3B_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI Data Set Landing Page for DISCOVERAQ_Maryland_Aerosol_AircraftInSitu_P3B_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Maryland_Aerosol_AircraftInSitu_P3B_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2241805125-LARC_ASDC",
-                    "description": "Earthdata Search for DISCOVERAQ_Maryland_Aerosol_AircraftInSitu_P3B_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for DISCOVERAQ_Maryland_Aerosol_AircraftInSitu_P3B_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2241805125-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/DISCOVER-AQ/Maryland_Aerosol_AircraftInSitu_P3B_Data_1/",
-                    "description": "ASDC Direct Data Download for DISCOVERAQ_Maryland_Aerosol_AircraftInSitu_P3B_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for DISCOVERAQ_Maryland_Aerosol_AircraftInSitu_P3B_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/DISCOVER-AQ/Maryland_Aerosol_AircraftInSitu_P3B_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2241805125-LARC_ASDC",
+            "issued": "2021-06-10",
+            "keyword": [
+                "atmosphere",
+                "aerosols",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Maryland_Aerosol_AircraftInSitu_P3B_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-03-21",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>30.0 -85.0 30.0 -70.0 45.0 -70.0 45.0 -85.0 30.0 -85.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2011-06-26T00:00:00Z/2011-07-31T23:59:59.999Z",
             "theme": [
                 "DISCOVER-AQ",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "DISCOVER-AQ Maryland Deployment P-3B Aircraft In Situ Aerosol Data"
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
-                "compressible",
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
-            "identifier": "NASA-843__18",
             "description": "This grouping contains the compressible-flow cases from the 1980-81 Data Library.",
-            "title": "Collaborative Testing of Turbulence Models: Compressible Flow Cases from 1980-81 Data Library",
-            "programCode": [
-                "026:023"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -751828,108 +751806,102 @@
                     "mediaType": "application/txt"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-843__18",
+            "issued": "2018-06-25",
+            "keyword": [
+                "flow",
+                "turbulence",
+                "cases",
+                "compressible",
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
+            "title": "Collaborative Testing of Turbulence Models: Compressible Flow Cases from 1980-81 Data Library"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GPM/ATMS/NOAA20/1C/07",
             "citation": "Wesley Berg. 2022-05-09. GPM_1CNOAA20ATMS. GPM ATMS on NOAA-20 Common Calibrated Brightness Temperatures L1C 1.5 hours 17 km V07. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/ATMS/NOAA20/1C/07. https://disc.gsfc.nasa.gov/datacollection/GPM_1CNOAA20ATMS_07.html. Digital Science Data.",
-            "issued": "2022-05-01",
-            "temporal": "2017-11-29T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-01",
-            "references": [
-                "https://doi.org/10.1175/JTECH-D-16-0100.1",
-                "https://doi.org/10.3390/rs10081306"
-            ],
-            "keyword": [
-                "earth science",
-                "precipitation",
-                "atmosphere",
-                "atmospheric water vapor"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "WESLEY BERG",
                 "hasEmail": "mailto:berg@atmos.colostate.edu"
             },
+            "creator": "Wesley Berg",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2264133522-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Version 07 is the current version of the data set. Older versions will no longer be available and have been superseded by Version 07.\n\n1CATMS contains common calibrated brightness temperature from the ATMS passive microwave instrument flown on the Suomi NPP satellite and JPSS satellites. ATMS is approximatly a combination of the AMSU-A channels and the MHS channels, to the total of 22 channels. ATMS rotates 3 scans per 8 seconds. 1CATMS contains 4 swaths, one for each band K, A(Ka), W, and G.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "GPM_1CNOAA20ATMS",
-            "creator": "Wesley Berg",
-            "graphic-preview-description": "Common Calibrated Brightness Temperature from GPM ATMS on NOAA-20 (GPM_1CNOAA20ATMS)",
-            "title": "GPM ATMS on NOAA-20 Common Calibrated Brightness Temperatures L1C 1.5 hours 17 km V07 (GPM_1CNOAA20ATMS) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_1CNOAA20ATMS.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FATMS%2FNOAA20%2F1C%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FATMS%2FNOAA20%2F1C%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_1CNOAA20ATMS.png",
-                    "description": "Common Calibrated Brightness Temperature from GPM ATMS on NOAA-20 (GPM_1CNOAA20ATMS)",
                     "@type": "dcat:Distribution",
+                    "description": "Common Calibrated Brightness Temperature from GPM ATMS on NOAA-20 (GPM_1CNOAA20ATMS)",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_1CNOAA20ATMS.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_1CNOAA20ATMS_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_1CNOAA20ATMS_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L1C/GPM_1CNOAA20ATMS.07/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L1C/GPM_1CNOAA20ATMS.07/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L1C/GPM_1CNOAA20ATMS.07/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L1C/GPM_1CNOAA20ATMS.07/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_1CNOAA20ATMS_07",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_1CNOAA20ATMS_07",
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
@@ -751939,269 +751911,273 @@
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
-                    "downloadURL": "https://www.star.nesdis.noaa.gov/mirs/snppatms.php",
-                    "description": "Instrument Description from NOAA",
                     "@type": "dcat:Distribution",
+                    "description": "Instrument Description from NOAA",
+                    "downloadURL": "https://www.star.nesdis.noaa.gov/mirs/snppatms.php",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Common Calibrated Brightness Temperature from GPM ATMS on NOAA-20 (GPM_1CNOAA20ATMS)",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_1CNOAA20ATMS.png",
+            "identifier": "C2264133522-GES_DISC",
+            "issued": "2022-05-01",
+            "keyword": [
+                "earth science",
+                "precipitation",
+                "atmosphere",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/ATMS/NOAA20/1C/07",
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
+            "series-name": "GPM_1CNOAA20ATMS",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2017-11-29T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "GPM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM ATMS on NOAA-20 Common Calibrated Brightness Temperatures L1C 1.5 hours 17 km V07 (GPM_1CNOAA20ATMS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/PRESW-YOJ10",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Menemenlis, D., Hill, C., Henze, C. E., Wang, J., & Fenty, I.. 2021-02-10. Yongala Pre-SWOT Level-4 Hourly MITgcm LLC4320 Native Grid 2km Oceanographic Dataset Version 1.0. Version 1.0. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/PRESW-YOJ10. Menemenlis, D., Hill, C., Henze, C. E., Wang, J., & Fenty, I. 2021. Yongala Pre-SWOT Level-4 Hourly MITgcm LLC4320 Native Grid 2km Oceanographic Dataset Version 1.0. PO.DAAC, CA, USA. Dataset accessed[YYYY-MM-DD] at https://doi.org/10.5067/PRESW-ASJ10.",
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
-                "earth science",
-                "oceans",
-                "ocean heat budget",
-                "ocean circulation",
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
-            "identifier": "C2258633956-POCLOUD",
-            "description": "This dataset provides a regional multivariate oceanographic state estimate from a global ocean numerical simulation with a focus on the Yongala region. The global ocean simulation is based on the MIT general circulation model (MITgcm) with Lat-Lon-Cap grid (LLC) layout and 1/48-degree (2km at equator) nominal horizontal resolution. This simulation is often referred to as LLC4320 in the community and existing publications. The simulation has 90 vertical levels, with about 1-m vertical resolution at the surface and 30 m down to 500 m, for optimized resolution of the upper-ocean processes. The model has zero parameterized horizontal diffusivity. In the vertical direction, the K-Profile Parameterization (KPP) is used for boundary layer turbulent mixing. It is spun up progressively from the lower resolution MITgcm simulation from the Estimating the Circulation & Climate of the Ocean (ECCO), and forced by the 6-hourly ERA-Interim atmosphere reanalysis ( https://www.ecmwf.int/en/forecasts/datasets/reanalysis-datasets/era-interim ). A synthetic surface pressure field consisting of the 16 most dominant tidal constituents is used to dynamically mimic the tidal forcing. The dataset provides hourly oceanographic variables at native grid. Three-dimensional variables include temperature, salinity, and velocity. Two-dimensional variables include sea level anomaly, ocean mixed layer thickness, bottom pressure anomaly, net freshwater flux, net heat flux, shortwave radiative flux, net salt flux, and ocean surface stress.",
-            "release-place": "PO.DAAC",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Menemenlis, D., Hill, C., Henze, C. E., Wang, J., & Fenty, I.",
-            "title": "Yongala Pre-SWOT Level-4 Hourly MITgcm LLC4320 Native Grid 2km Oceanographic Dataset Version 1.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MITgcm_LLC4320_Pre-SWOT_JPL_L4_Yongala_v1.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset provides a regional multivariate oceanographic state estimate from a global ocean numerical simulation with a focus on the Yongala region. The global ocean simulation is based on the MIT general circulation model (MITgcm) with Lat-Lon-Cap grid (LLC) layout and 1/48-degree (2km at equator) nominal horizontal resolution. This simulation is often referred to as LLC4320 in the community and existing publications. The simulation has 90 vertical levels, with about 1-m vertical resolution at the surface and 30 m down to 500 m, for optimized resolution of the upper-ocean processes. The model has zero parameterized horizontal diffusivity. In the vertical direction, the K-Profile Parameterization (KPP) is used for boundary layer turbulent mixing. It is spun up progressively from the lower resolution MITgcm simulation from the Estimating the Circulation & Climate of the Ocean (ECCO), and forced by the 6-hourly ERA-Interim atmosphere reanalysis ( https://www.ecmwf.int/en/forecasts/datasets/reanalysis-datasets/era-interim ). A synthetic surface pressure field consisting of the 16 most dominant tidal constituents is used to dynamically mimic the tidal forcing. The dataset provides hourly oceanographic variables at native grid. Three-dimensional variables include temperature, salinity, and velocity. Two-dimensional variables include sea level anomaly, ocean mixed layer thickness, bottom pressure anomaly, net freshwater flux, net heat flux, shortwave radiative flux, net salt flux, and ocean surface stress.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FPRESW-YOJ10",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FPRESW-YOJ10",
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
-                    "downloadURL": "https://doi.org/10.5067/PRESW-YOJ10",
-                    "description": "Access the dataset landing page for the collection",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page for the collection",
+                    "downloadURL": "https://doi.org/10.5067/PRESW-YOJ10",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MITgcm_LLC4320_Pre-SWOT_JPL_L4_Yongala_v1.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MITgcm_LLC4320_Pre-SWOT_JPL_L4_Yongala_v1.0.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2258633956-POCLOUD",
-                    "description": "Browse and download granules over HTTPS using the virtual directories service",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories service",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2258633956-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2258633956-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2258633956-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/SWOT/Pre-SWOT_LLC4320/preswot_llc4320_user_guide.pdf",
-                    "description": "PRE-SWOT NUMERICAL SIMULATION VERSION 1 USER GUIDE",
                     "@type": "dcat:Distribution",
+                    "description": "PRE-SWOT NUMERICAL SIMULATION VERSION 1 USER GUIDE",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/SWOT/Pre-SWOT_LLC4320/preswot_llc4320_user_guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/SWOT/Pre-SWOT_LLC4320/README",
-                    "description": "README file",
                     "@type": "dcat:Distribution",
+                    "description": "README file",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/SWOT/Pre-SWOT_LLC4320/README",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MITgcm_LLC4320_Pre-SWOT_JPL_L4_Yongala_v1.0.jpg",
+            "identifier": "C2258633956-POCLOUD",
+            "issued": "2021-01-20",
+            "keyword": [
+                "salinity/density",
+                "earth science",
+                "oceans",
+                "ocean heat budget",
+                "ocean circulation",
+                "ocean temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/PRESW-YOJ10",
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
             "spatial": "146.25 -20.5 150.25 -16.5",
+            "temporal": "2011-09-13T00:00:00Z/2012-11-15T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Yongala Pre-SWOT Level-4 Hourly MITgcm LLC4320 Native Grid 2km Oceanographic Dataset Version 1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GPM/SSMIS/F16/GPROF/2A/07",
             "citation": "GPM Science Team. 2022-05-09. GPM_2AGPROFF16SSMIS. Version 07. GPM SSMIS on F16 (GPROF) Radiometer Precipitation Profiling L2 1.5 hours 12 km V07. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/SSMIS/F16/GPROF/2A/07. https://disc.gsfc.nasa.gov/datacollection/GPM_2AGPROFF16SSMIS_07.html. Digital Science Data.",
-            "issued": "2022-05-09",
-            "temporal": "2014-01-31T00:00:00Z/2023-02-28T00:00:00Z",
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
-            "identifier": "C2264133638-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Version 07 is the current version of the data set. Older versions will no longer be available and have been superseded by Version 07.\n\nThe 2AGPROF (Goddard Profiling) algorithm retrieves consistent precipitation and related science fields from the following GMI and partner passive microwave sensors:\n+ TMI (TRMM)\n+ GMI, (GPM)\n+ SSMI (DMSP F15), SSMIS (DMSP F16, F17, F18, F19)\n+ AMSR2 (GCOM-W1)\n+ MHS (NOAA 18,19) \n+ MHS (METOP A,B)\n+ ATMS (NPP)\n+ SAPHIR (MT1)\n\nThis provides the bulk of the 3-hour coverage achieved by GPM. For each sensor, there are nearrealtime (NRT) products, standard products, and climate products. These differ only in the amount of data that are available within 3 hours, 48 hours, and 3 months of collection, as well as the ancillary data used. The NRT product uses GANAL forecast fields. Standard products use the GANAL analysis product, while the climate product uses ECMWF reanalysis in order to allow for consistent data records with earlier missions. These earlier data may be archived separately. The main strength of the product is the large sampling provided.\n\nThe GPM radiometer algorithms are Bayesian-type algorithms. These algorithms search an apriori database of potential rain profiles and retrieve a weighted average of these entries based upon the proximity of the observed brightness temperature (Tb) to the simulated Tb corresponding to each rain profile. By using the same a-priori database of rain profiles, with appropriate simulated Tb for each constellation sensor, the Bayesian method is completely parametric and thus well suited for GPM's constellation approach. The a-priori information will be supplied by the combined algorithm supplied by GPM's core satellite as soon after launch as feasible. Databases for V0 of the algorithm had to be constructed from various sources as described in the ATBD. The solution provides a mean rain rate as well as the vertical structure of cloud and precipitation hydrometeors and their uncertainty.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "GPM_2AGPROFF16SSMIS",
-            "creator": "GPM Science Team",
-            "title": "GPM SSMIS on F16 (GPROF) Radiometer Precipitation Profiling L2 1.5 hours 12 km V07 (GPM_2AGPROFF16SSMIS) at GES DISC",
-            "graphic-preview-description": "Surface Precipitation from F16 GPROF (GPM_2AGPROFF16SSMIS)",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_2AGPROFF16SSMIS_07.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FSSMIS%2FF16%2FGPROF%2F2A%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FSSMIS%2FF16%2FGPROF%2F2A%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_2AGPROFF16SSMIS_07.png",
-                    "description": "Surface Precipitation from F16 GPROF (GPM_2AGPROFF16SSMIS)",
                     "@type": "dcat:Distribution",
+                    "description": "Surface Precipitation from F16 GPROF (GPM_2AGPROFF16SSMIS)",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_2AGPROFF16SSMIS_07.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_2AGPROFF16SSMIS_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_2AGPROFF16SSMIS_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L2/GPM_2AGPROFF16SSMIS.07/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L2/GPM_2AGPROFF16SSMIS.07/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L2/GPM_2AGPROFF16SSMIS.07/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L2/GPM_2AGPROFF16SSMIS.07/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_2AGPROFF16SSMIS_07",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_2AGPROFF16SSMIS_07",
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
@@ -752211,214 +752187,240 @@
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
-                    "downloadURL": "https://www.star.nesdis.noaa.gov/mirs/ssmis.php",
-                    "description": "Instrument Description",
                     "@type": "dcat:Distribution",
+                    "description": "Instrument Description",
+                    "downloadURL": "https://www.star.nesdis.noaa.gov/mirs/ssmis.php",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Surface Precipitation from F16 GPROF (GPM_2AGPROFF16SSMIS)",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_2AGPROFF16SSMIS_07.png",
+            "identifier": "C2264133638-GES_DISC",
+            "issued": "2022-05-09",
+            "keyword": [
+                "atmospheric water vapor",
+                "atmosphere",
+                "precipitation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/SSMIS/F16/GPROF/2A/07",
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
+            "series-name": "GPM_2AGPROFF16SSMIS",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2014-01-31T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "GPM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM SSMIS on F16 (GPROF) Radiometer Precipitation Profiling L2 1.5 hours 12 km V07 (GPM_2AGPROFF16SSMIS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-EXT1-67P-M26-STR-REFL-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 1 mission phase, covering the period from 2016-02-09T23:25:00.000 to 2016-03-08T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-ext1-67p-m26-str-refl-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-EXT1-67P-M26-STR-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-ext1-67p-m26-str-refl-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 1 mission phase, covering the period from 2016-02-09T23:25:00.000 to 2016-03-08T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 EXT1-MTP026 RDR-STR-REFL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 EXT1-MTP026 RDR-STR-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4RB72JW",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "United States Department of Agriculture Extension Research Service - USDA/ERS, and Center for International Earth Science Information Network - CIESIN. 1996-05-31. China Dimensions Data Collection: Agricultural Statistics of the People's Republic of China: 1949-1990. Version 1.00. Saginaw, MI. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H4RB72JW. https://doi.org/10.7927/H4RB72JW.",
-            "issued": "1996-05-31",
-            "temporal": "1949-01-01T00:00:00Z/1990-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "1996-05-31",
-            "references": [
-                "https://doi.org/10.7927/H4QC01D2",
-                "https://doi.org/10.7927/H4C24TCF",
-                "https://doi.org/10.7927/H4GT5K3V",
-                "https://doi.org/10.7927/H4KK98PS",
-                "https://doi.org/10.7927/H4MK69T5",
-                "https://doi.org/10.7927/H4ZW1HVD",
-                "https://doi.org/10.7927/H47D2S2F",
-                "https://doi.org/10.7927/H43N21B3",
-                "https://doi.org/10.7927/H4V40S4D",
-                "https://doi.org/10.7927/H4FT8HZ2"
-            ],
-            "keyword": [
-                "economic resources",
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
-            "identifier": "C179001901-SEDAC",
-            "description": "The Agricultural Statistics of the People's Republic of China, 1949-1990 is an historical collection of agricultural statistical data compiled by China's State Statistical Bureau (SSB). The collection contains 297 variables covering social and economic indicators, commodities, price index, production, trade, and consumption. The data are provided at the national level (1949-1990) and the provincial level (1979-1990). This data set is produced in collaboration with the United States Department of Agriculture (USDA), SSB, and the Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "Saginaw, MI",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "United States Department of Agriculture Extension Research Service - USDA/ERS, and Center for International Earth Science Information Network - CIESIN",
-            "title": "China Dimensions Data Collection: Agricultural Statistics of the People's Republic of China: 1949-1990",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/cddc/cddc-china-agricultural-stats-1949-1990/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Agricultural Statistics of the People's Republic of China, 1949-1990 is an historical collection of agricultural statistical data compiled by China's State Statistical Bureau (SSB). The collection contains 297 variables covering social and economic indicators, commodities, price index, production, trade, and consumption. The data are provided at the national level (1949-1990) and the provincial level (1979-1990). This data set is produced in collaboration with the United States Department of Agriculture (USDA), SSB, and the Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4RB72JW",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4RB72JW",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/cddc/cddc-china-agricultural-stats-1949-1990/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/cddc/cddc-china-agricultural-stats-1949-1990/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/cddc-china-agricultural-stats-1949-1990/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/cddc-china-agricultural-stats-1949-1990/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/cddc-china-agricultural-stats-1949-1990/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/cddc-china-agricultural-stats-1949-1990/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/cddc-china-agricultural-stats-1949-1990",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/cddc-china-agricultural-stats-1949-1990",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/cddc/cddc-china-agricultural-stats-1949-1990/sedac-logo.jpg",
+            "identifier": "C179001901-SEDAC",
+            "issued": "1996-05-31",
+            "keyword": [
+                "economic resources",
+                "human dimensions",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4RB72JW",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1996-05-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H4QC01D2",
+                "https://doi.org/10.7927/H4C24TCF",
+                "https://doi.org/10.7927/H4GT5K3V",
+                "https://doi.org/10.7927/H4KK98PS",
+                "https://doi.org/10.7927/H4MK69T5",
+                "https://doi.org/10.7927/H4ZW1HVD",
+                "https://doi.org/10.7927/H47D2S2F",
+                "https://doi.org/10.7927/H43N21B3",
+                "https://doi.org/10.7927/H4V40S4D",
+                "https://doi.org/10.7927/H4FT8HZ2"
+            ],
+            "release-place": "Saginaw, MI",
             "spatial": "73.0 18.0 135.0 54.0",
+            "temporal": "1949-01-01T00:00:00Z/1990-12-31T00:00:00Z",
             "theme": [
                 "CDDC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "China Dimensions Data Collection: Agricultural Statistics of the People's Republic of China: 1949-1990"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-PWS-4-SUMM-SA-48SEC-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-pws-4-summ-sa-48sec-v1.0_fd22-5kvy",
+            "issued": "2018-06-26",
+            "keyword": [
+                "voyager",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-PWS-4-SUMM-SA-48SEC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-pws-4-summ-sa-48sec-v1.0_fd22-5kvy",
-            "description": "not applicable",
-            "title": "VG2 SAT PWS RESAMPLED SPECTRAL ANALYZER 48SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG2 SAT PWS RESAMPLED SPECTRAL ANALYZER 48SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-ROSINA-2-AST1-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set present engineering data of the COPS and DFMS ROSINA sensors during the Steins flyby phase. There were no RTOF measurements",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-rosina-2-ast1-v1.0_fd48-3y4r",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "unknown",
@@ -752427,240 +752429,220 @@
                 "earth",
                 "2867 steins"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-ROSINA-2-AST1-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-rosina-2-ast1-v1.0_fd48-3y4r",
-            "description": "This data set present engineering data of the COPS and DFMS ROSINA sensors during the Steins flyby phase. There were no RTOF measurements",
-            "title": "ROSETTA-ORBITER STEINS ROSINA 2 ENGINEERING V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER STEINS ROSINA 2 ENGINEERING V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/BNL/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/BNL/DATA001.",
-            "issued": "1998-04-02",
-            "temporal": "1998-04-02T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean temperature",
-                "oceans",
-                "ocean optics",
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
-            "identifier": "C1633360163-OB_DAAC",
             "description": "Measurements made near the Bahamas during 1998 by the Brookhaven National Laboratory (BNL).",
-            "title": "Brookhaven National Laboratory (BNL) measurements near the Bahamas in 1998",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FBNL%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FBNL%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/BNL/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/BNL/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360163-OB_DAAC",
+            "issued": "1998-04-02",
+            "keyword": [
+                "ocean temperature",
+                "oceans",
+                "ocean optics",
+                "salinity/density",
+                "earth science",
+                "ocean chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/BNL/DATA001",
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
+            "temporal": "1998-04-02T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Brookhaven National Laboratory (BNL) measurements near the Bahamas in 1998"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-RPCMAG-4-EAR3-RESAMPLED-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This dataset contains RESAMPLED DATA of the 3rd Earth Swingby(EAR3). The closest approach (CA) took place on November 13, 2009 at 07:45. Additionally data from the Payload Chekcout PC10 are added.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-rpcmag-4-ear3-resampled-v3.0_fd4k-jcwg",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "unknown",
                 "earth"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-RPCMAG-4-EAR3-RESAMPLED-V3.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-rpcmag-4-ear3-resampled-v3.0_fd4k-jcwg",
-            "description": "This dataset contains RESAMPLED DATA of the 3rd Earth Swingby(EAR3). The closest approach (CA) took place on November 13, 2009 at 07:45. Additionally data from the Payload Chekcout PC10 are added.",
-            "title": "ROSETTA-ORBITER EARTH RPCMAG 4 EAR3 RESAMPLED V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER EARTH RPCMAG 4 EAR3 RESAMPLED V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H45718Z5",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for Hazards and Risk Research - CHRR - Columbia University, Center for International Earth Science Information Network - CIESIN - Columbia University, and International Bank for Reconstruction and Development - The World Bank. 2005-12-31. Global Multihazard Frequency and Distribution. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, Center for Hazards and Risk Research (CHRR)/Columbia University. https://doi.org/10.7927/H45718Z5. https://doi.org/10.7927/H45718Z5.",
-            "issued": "2005-12-31",
-            "temporal": "2000-01-01T00:00:00Z/2000-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2005-12-31",
-            "references": [
-                "https://doi.org/10.7927/H4S180F9",
-                "https://doi.org/10.7927/H41J97NM",
-                "https://doi.org/10.7927/H4WS8R5B"
-            ],
-            "keyword": [
-                "earth science",
-                "human dimensions",
-                "natural hazards",
-                "snow/ice",
-                "terrestrial hydrosphere"
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
-            "identifier": "C179001784-SEDAC",
-            "description": "The Global Multihazard Frequency and Distribution is a 2.5 minute grid presenting a simple multihazard index based solely on summated single-hazard decile values. The hazards of interest include cyclones, droughts, earthquakes, floods, landslides, and volcanoes. This data set is further enriched by the inclusion of data pertaining to population, Gross Domestic Product (GDP), and transportation infrastructure. This data set is the result of collaboration among the Columbia University Center for Hazards and Risk Research (CHRR), International Bank for Reconstruction and Development/The World Bank, and Columbia University Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Center for Hazards and Risk Research - CHRR - Columbia University, Center for International Earth Science Information Network - CIESIN - Columbia University, and International Bank for Reconstruction and Development - The World Bank",
-            "title": "Global Multihazard Frequency and Distribution",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/ndh-multihazard-frequency-distribution/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Global Multihazard Frequency and Distribution is a 2.5 minute grid presenting a simple multihazard index based solely on summated single-hazard decile values. The hazards of interest include cyclones, droughts, earthquakes, floods, landslides, and volcanoes. This data set is further enriched by the inclusion of data pertaining to population, Gross Domestic Product (GDP), and transportation infrastructure. This data set is the result of collaboration among the Columbia University Center for Hazards and Risk Research (CHRR), International Bank for Reconstruction and Development/The World Bank, and Columbia University Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH45718Z5",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH45718Z5",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/ndh/ndh-multihazard-frequency-distribution/multihazard-frequency-distribution-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/ndh/ndh-multihazard-frequency-distribution/multihazard-frequency-distribution-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-multihazard-frequency-distribution/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-multihazard-frequency-distribution/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-multihazard-frequency-distribution/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-multihazard-frequency-distribution/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-multihazard-frequency-distribution",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-multihazard-frequency-distribution",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/ndh-multihazard-frequency-distribution/maps",
+            "identifier": "C179001784-SEDAC",
+            "issued": "2005-12-31",
+            "keyword": [
+                "earth science",
+                "human dimensions",
+                "natural hazards",
+                "snow/ice",
+                "terrestrial hydrosphere"
+            ],
+            "landingPage": "https://doi.org/10.7927/H45718Z5",
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
+                "https://doi.org/10.7927/H41J97NM",
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
+            "title": "Global Multihazard Frequency and Distribution"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/fd7y-uk2r",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "temporal": "1977-01-01/1996-01-01",
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
                 "fn": "William Stefanov",
                 "hasEmail": "mailto:jsc-earthweb@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-0000037__13",
+            "describedBy": "http://www.lpi.usra.edu/resources/gc/gcreadme.html",
             "description": "Planetary nomenclature, like terrestrial nomenclature, is used to uniquely identify a feature on the surface of a planet or satellite so that the feature can be easily located, described, and discussed. This gazetteer contains detailed information about all names of topographic and albedo features on planets and satellites (and some planetary ring and ring-gap systems) that the International Astronomical Union (IAU) has named and approved from its founding in 1919 through the present time.",
-            "title": "Gateway to Astronaut Photography of Earth",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -752668,18 +752650,50 @@
                     "mediaType": "text/html"
                 }
             ],
-            "describedBy": "http://www.lpi.usra.edu/resources/gc/gcreadme.html",
-            "accrualPeriodicity": "irregular"
+            "identifier": "NASA-0000037__13",
+            "issued": "2018-06-25",
+            "keyword": [
+                "nen",
+                "wise",
+                "space science",
+                "geography"
+            ],
+            "landingPage": "https://data.nasa.gov/d/fd7y-uk2r",
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
-            "landingPage": "https://data.nasa.gov/d/fd88-7vtt",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "We investigated differentially regulated genes in human Jurkat T lymphocytic cells in 20s and 5min microgravity and in hypergravity and compared expression profiles to identify potential gravity-regulated genes and adaptation processes. This dataset is part of a series of three and the other two datasets are deposited in GLDS-172 and GLDS-189.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-188",
+                    "mediaType": "text/html",
+                    "title": "Dynamic gene expression response to altered gravity in human T cells (sounding rocket flight)"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-188_fd88-7vtt",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "labeling",
                 "altered gravity",
@@ -752692,632 +752706,593 @@
                 "rna extraction",
                 "nucleic acid hybridization"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/fd88-7vtt",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-188_fd88-7vtt",
-            "description": "We investigated differentially regulated genes in human Jurkat T lymphocytic cells in 20s and 5min microgravity and in hypergravity and compared expression profiles to identify potential gravity-regulated genes and adaptation processes. This dataset is part of a series of three and the other two datasets are deposited in GLDS-172 and GLDS-189.",
-            "title": "Dynamic gene expression response to altered gravity in human T cells (sounding rocket flight)",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-188",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Dynamic gene expression response to altered gravity in human T cells (sounding rocket flight)"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Dynamic gene expression response to altered gravity in human T cells (sounding rocket flight)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-J%2FC-HSCCD-3-RDR-SL9-V1.0",
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
-                "comet sl9/jupiter collision",
-                "jupiter"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "A global imaging campaign (GIC) was organized at sites during the impact of comet Shoemaker-levy 9 with Jupiter. These five sites were Queensland in Australia, the Cerro Tololo Interamerican Observatory, Lick Observatory, Mauna Kea Observatory and Reunion Island. All sites used a combination of high speed optical CCD systems with similar broad and narrow band filters.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-j-c-hsccd-3-rdr-sl9-v1.0_fd95-wdzs",
+            "issued": "2021-05-21",
+            "keyword": [
+                "comet sl9/jupiter collision",
+                "jupiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-J%2FC-HSCCD-3-RDR-SL9-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-j-c-hsccd-3-rdr-sl9-v1.0_fd95-wdzs",
-            "description": "A global imaging campaign (GIC) was organized at sites during the impact of comet Shoemaker-levy 9 with Jupiter. These five sites were Queensland in Australia, the Cerro Tololo Interamerican Observatory, Lick Observatory, Mauna Kea Observatory and Reunion Island. All sites used a combination of high speed optical CCD systems with similar broad and narrow band filters.",
-            "title": "IMAGING OF JUPITER ASSOCIATED WITH SL9 IMPACT FLASHES",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "IMAGING OF JUPITER ASSOCIATED WITH SL9 IMPACT FLASHES"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SEAC4RS_Analysis_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2021-09-07. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/SEAC4RS_Analysis_Data_1.",
-            "issued": "2021-08-20",
-            "temporal": "2013-07-30T00:00:00Z/2013-09-24T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-20",
-            "keyword": [
-                "atmosphere",
-                "weather events",
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
-            "identifier": "C2119341692-LARC_ASDC",
             "description": "SEAC4RS_Analysis_Data are ancillary analysis data utilized as part of the Studies of Emissions and Atmospheric Composition, Clouds and Climate Coupling by Regional Surveys (SEA4CRS) airborne field study. Data from GOES-EAST and GOES-WEST relating to overshooting tops are featured in this product. Data collection for this product is complete.\r\n\r\nStudies of Emissions and Atmospheric Composition, Clouds and Climate Coupling by Regional Surveys (SEAC4RS) airborne field study was conducted in August and September of 2013. The field operation was based in Houston, Texas. The primary SEAC4RS science objectives are: to determine how pollutant emissions are redistributed via deep convection throughout the troposphere; to determine the evolution of gases and aerosols in deep convective outflow and the implications for UT/LS chemistry; to identify the influences and feedbacks of aerosol particles from anthropogenic pollution and biomass burning on meteorology and climate through changes in the atmospheric heat budget (i.e., semi-direct effect) or through microphysical changes in clouds (i.e., indirect effects); and lastly, to serve as a calibration and validation test bed for future satellite instruments and missions.\r\n\r\nThe airborne observational data were collected from three aircraft platforms: the NASA DC-8, ER-2, and SPEC LearJet. Both the NASA DC-8 and ER-2 aircraft were instrumented for comprehensive in-situ and remote sensing measurements of the trace gas, aerosol properties, and cloud properties. In addition, radiative fluxes and meteorological parameters were also recorded. The NASA DC-8 was mostly responsible for tropospheric sampling, while the NASA ER-2 was operating in the lower stratospheric regime. The SPEC LearJet was dedicated to in-situ cloud characterizations. To accomplish the science objectives, the flight plans were designed to investigate the influence of biomass burning and pollution, their temporal evolution, and ultimately, impacts on meteorological processes which can, in turn, feedback on regional air quality. With respect to meteorological feedbacks, the opportunity to examine the impact of polluting aerosols on cloud properties and dynamics was of particular interest.",
-            "title": "SEAC4RS Analysis and Ancillary Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSEAC4RS_Analysis_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSEAC4RS_Analysis_Data_1",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://espo.nasa.gov/sites/default/files/documents/SEAC4RS_DraftPlan_20130409b_USA.pdf",
-                    "description": "SEAC4RS Draft Plan",
                     "@type": "dcat:Distribution",
+                    "description": "SEAC4RS Draft Plan",
+                    "downloadURL": "https://espo.nasa.gov/sites/default/files/documents/SEAC4RS_DraftPlan_20130409b_USA.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/dc3-seac4rs/docs/SEAC4RS_Data_Management_Plan.pdf",
-                    "description": "SEAC4RS/DC3 Data Management Plan",
                     "@type": "dcat:Distribution",
+                    "description": "SEAC4RS/DC3 Data Management Plan",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/dc3-seac4rs/docs/SEAC4RS_Data_Management_Plan.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/seac4rs",
-                    "description": "SEAC4RS Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "SEAC4RS Project Home Page",
+                    "downloadURL": "https://espo.nasa.gov/seac4rs",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/topics/earth/features/seac4rs_2013.html",
-                    "description": "SEAC4RS nasa.gov feature article",
                     "@type": "dcat:Distribution",
+                    "description": "SEAC4RS nasa.gov feature article",
+                    "downloadURL": "https://www.nasa.gov/topics/earth/features/seac4rs_2013.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2015JD024297",
-                    "description": "SEAC4RS Overview Paper",
                     "@type": "dcat:Distribution",
+                    "description": "SEAC4RS Overview Paper",
+                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2015JD024297",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/SEAC4RS_Analysis_Data_1",
-                    "description": "DOI data set landing page for SEAC4RS_Analysis_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for SEAC4RS_Analysis_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/SEAC4RS_Analysis_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2119341692-LARC_ASDC",
-                    "description": "Earthdata Search for SEAC4RS_Analysis_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for SEAC4RS_Analysis_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2119341692-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/SEAC4RS/Analysis_Data_1/",
-                    "description": "ASDC Direct Data Download for SEAC4RS_Analysis_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for SEAC4RS_Analysis_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/SEAC4RS/Analysis_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2119341692-LARC_ASDC",
+            "issued": "2021-08-20",
+            "keyword": [
+                "atmosphere",
+                "weather events",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SEAC4RS_Analysis_Data_1",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>18.0 -126.0 18.0 -79.0 52.0 -79.0 52.0 -126.0 18.0 -126.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2013-07-30T00:00:00Z/2013-09-24T23:59:59.999Z",
             "theme": [
                 "SEAC4RS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SEAC4RS Analysis and Ancillary Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567575-USGS_LTA.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, DOI/USGS/EROS.",
-            "issued": "2019-09-20",
-            "temporal": "1970-01-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-03-25",
-            "keyword": [
-                "surface radiative properties",
-                "land surface",
-                "earth science",
-                "topography"
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
-            "identifier": "C1220567575-USGS_LTA",
             "description": "Declassified satellite images provide an important worldwide record of land-surface change. With the success of the first release of classified satellite photography in 1995, images from U.S. military intelligence satellites KH-7 and KH-9 were declassified in accordance with Executive Order 12951 in 2002. The data were originally used for cartographic information and reconnaissance for U.S. intelligence agencies. Since the images could be of historical value for global change research and were no longer critical to national security, the collection was made available to the public.\n\nKeyhole (KH) satellite systems KH-7 and KH-9 acquired photographs of the Earth\u2019s surface with a telescopic camera system and transported the exposed film through the use of recovery capsules. The capsules or buckets were de-orbited and retrieved by aircraft while the capsules parachuted to earth. The exposed film was developed and the images were analyzed for a range of military applications.\n\nThe KH-7 surveillance system was a high resolution imaging system that was operational from July 1963 to June 1967. Approximately 18,000 black-and-white images and 230 color images are available from the 38 missions flown during this program. Key features for this program were larger area of coverage and improved ground resolution. The cameras acquired imagery in continuous lengthwise sweeps of the terrain. KH-7 images are 9 inches wide, vary in length from 4 inches to 500 feet long, and have a resolution of 2 to 4 feet.\n\nThe KH-9 mapping program was operational from March 1973 to October 1980 and was designed to support mapping requirements and exact positioning of geographical points for the military. This was accomplished by using image overlap for stereo coverage and by using a camera system with a reseau grid to correct image distortion. The KH-9 framing cameras produced 9 x 18 inch imagery at a resolution of 20-30 feet. Approximately 29,000 mapping images were acquired from 12 missions. \n\nThe original film sources are maintained by the National Archives and Records Administration (NARA). Duplicate film sources held in the USGS EROS Center archive are used to produce digital copies of the imagery.",
-            "title": "Declassified Satellite Imagery 2 (2002)",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://earthexplorer.usgs.gov",
-                    "description": "\n         EarthExplorer\n      ",
                     "@type": "dcat:Distribution",
+                    "description": "\n         EarthExplorer\n      ",
+                    "downloadURL": "http://earthexplorer.usgs.gov",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1220567575-USGS_LTA",
+            "issued": "2019-09-20",
+            "keyword": [
+                "surface radiative properties",
+                "land surface",
+                "earth science",
+                "topography"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567575-USGS_LTA.html",
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
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1970-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Declassified Satellite Imagery 2 (2002)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0191-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-09T08:54:50.000 to 2014-08-09T13:55:59.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0191-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0191-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0191-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-09T08:54:50.000 to 2014-08-09T13:55:59.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0191 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0191 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-C-MUPUS-3-SDL-V1.0",
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
+            "description": "This archive contains calibrated data from the MUPUS instrument onboard ROSETTA Lander, acquired during the SDL phase. The primary target is the comet 67P/CHURYUMOV-GERASIMENKO. It also contains documentation which describes the MUPUS experiment. The data archived in this data set conform to the Planetary Data System Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-c-mupus-3-sdl-v1.0_fde7-55be",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-C-MUPUS-3-SDL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-c-mupus-3-sdl-v1.0_fde7-55be",
-            "description": "This archive contains calibrated data from the MUPUS instrument onboard ROSETTA Lander, acquired during the SDL phase. The primary target is the comet 67P/CHURYUMOV-GERASIMENKO. It also contains documentation which describes the MUPUS experiment. The data archived in this data set conform to the Planetary Data System Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER 67P MUPUS 3 SDL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-LANDER 67P MUPUS 3 SDL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SUBORBITAL/ACEPOL2017/AircraftRemoteSensing_CPL_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2020-05-27. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/SUBORBITAL/ACEPOL2017/AircraftRemoteSensing_CPL_Data_1.",
-            "issued": "2020-03-27",
-            "temporal": "2017-10-19T00:00:00Z/2017-11-09T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-08",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "aerosols",
-                "clouds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kirk  Knobelspiesse",
                 "hasEmail": "mailto:kirk.d.knobelspiesse@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1758588308-LARC_ASDC",
             "description": "ACEPOL Cloud Physics Lidar (CPL) Remotely Sensed Data (ACEPOL_AircraftRemoteSensing_CPL_Data) are remotely sensed measurements collected by the Cloud Physics Lidar (CPL) onboard the ER-2 during ACEPOL. In order to improve our understanding of the effect of aerosols on climate and air quality, measurements of aerosol chemical composition, size distribution, height profile, and optical properties are of crucial importance. In terms of remotely sensed instrumentation, the most extensive set of aerosol properties can be obtained by combining passive multi-angle, multi-spectral measurements of intensity and polarization with active measurements performed by a High Spectral Resolution Lidar. During Fall 2017, the Aerosol Characterization from Polarimeter and Lidar (ACEPOL) campaign, jointly sponsored by NASA and the Netherlands Institute for Space Research (SRON), performed aerosol and cloud measurements over the United States from the NASA high altitude ER-2 aircraft. Six instruments were deployed on the aircraft. Four of these instruments were multi-angle polarimeters: the Airborne Hyper Angular Rainbow Polarimeter (AirHARP), the Airborne Multiangle SpectroPolarimetric Imager (AirMSPI), the Airborne Spectrometer for Planetary Exploration (SPEX Airborne) and the Research Scanning Polarimeter (RSP). The other two instruments were lidars: the High Spectral Resolution Lidar 2 (HSRL-2) and the Cloud Physics Lidar (CPL). The ACEPOL operation was based at NASA\u2019s Armstrong Flight Research Center in Palmdale California, which enabled observations of a wide variety of scene types, including urban, desert, forest, coastal ocean and agricultural areas, with clear, cloudy, polluted and pristine atmospheric conditions. The primary goal of ACEPOL was to assess the capabilities of the different polarimeters for retrieval of aerosol and cloud microphysical and optical parameters, as well as their capabilities to derive aerosol layer height (near-UV polarimetry, O2 A-band). ACEPOL also focused on the development and evaluation of aerosol retrieval algorithms that combine data from both active (lidar) and passive (polarimeter) instruments. ACEPOL data are appropriate for algorithm development and testing, instrument intercomparison, and investigations of active and passive instrument data fusion, which make them valuable resources for remote sensing communities as they prepare for the next generation of spaceborne MAP and lidar missions.",
-            "title": "ACEPOL Cloud Physics Lidar (CPL) Remotely Sensed Data Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSUBORBITAL%2FACEPOL2017%2FAircraftRemoteSensing_CPL_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSUBORBITAL%2FACEPOL2017%2FAircraftRemoteSensing_CPL_Data_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://airbornescience.nasa.gov/acepwg/content/ACE_Polarimeter_Working_Group_ACEPWG_ACEPOL_field_campaign",
-                    "description": "NASA Airborne Science Program Overview of ACEPWG ACEPOL/LIREX field campaign",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Airborne Science Program Overview of ACEPWG ACEPOL/LIREX field campaign",
+                    "downloadURL": "https://airbornescience.nasa.gov/acepwg/content/ACE_Polarimeter_Working_Group_ACEPWG_ACEPOL_field_campaign",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
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
-                    "downloadURL": "https://doi.org/10.5067/SUBORBITAL/ACEPOL2017/AircraftRemoteSensing_CPL_Data_1",
-                    "description": "DOI data set landing page for ACEPOL_AircraftRemoteSensing_CPL_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for ACEPOL_AircraftRemoteSensing_CPL_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/SUBORBITAL/ACEPOL2017/AircraftRemoteSensing_CPL_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1758588308-LARC_ASDC",
-                    "description": "Earthdata Search for ACEPOL_AircraftRemoteSensing_CPL_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for ACEPOL_AircraftRemoteSensing_CPL_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1758588308-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/acepol/index.html",
-                    "description": "NASA LaRC Airborne Science Data for Atmospheric Composition ACEPOL Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "NASA LaRC Airborne Science Data for Atmospheric Composition ACEPOL Home Page",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/acepol/index.html",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nwo.nl/en/projects/alw-go16-09/",
-                    "description": "Netherlands Organization for Scientific Research (NWO) ACEPOL Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "Netherlands Organization for Scientific Research (NWO) ACEPOL Home Page",
+                    "downloadURL": "https://www.nwo.nl/en/projects/alw-go16-09/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gmao.gsfc.nasa.gov/field_campaigns/ACEPOL/",
-                    "description": "Global Modeling and Assimilation Office (GMAO) ACEPOL Support Website",
                     "@type": "dcat:Distribution",
+                    "description": "Global Modeling and Assimilation Office (GMAO) ACEPOL Support Website",
+                    "downloadURL": "https://gmao.gsfc.nasa.gov/field_campaigns/ACEPOL/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/ACEPOL/2017",
-                    "description": "ACEPOL Data on the Sub-Orbital Order Tool (SOOT) Power User Interface (UI)",
                     "@type": "dcat:Distribution",
+                    "description": "ACEPOL Data on the Sub-Orbital Order Tool (SOOT) Power User Interface (UI)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/ACEPOL/2017",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through the Sub-Orbital Order Tool"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/ACEPOL/AircraftRemoteSensing_CPL_Data_1/",
-                    "description": "ASDC Direct Data Download for ACEPOL_AircraftRemoteSensing_CPL_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for ACEPOL_AircraftRemoteSensing_CPL_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/ACEPOL/AircraftRemoteSensing_CPL_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/ACEPOL/AircraftRemoteSensing_CPL_Data_1/contents.html",
-                    "description": "OPeNDAP data access for ACEPOL_AircraftRemoteSensing_CPL_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for ACEPOL_AircraftRemoteSensing_CPL_Data_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/ACEPOL/AircraftRemoteSensing_CPL_Data_1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1758588308-LARC_ASDC",
+            "issued": "2020-03-27",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "aerosols",
+                "clouds"
+            ],
+            "landingPage": "https://doi.org/10.5067/SUBORBITAL/ACEPOL2017/AircraftRemoteSensing_CPL_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-04-08",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>25.0 -130.0 25.0 -100.0 45.0 -100.0 45.0 -130.0 25.0 -130.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2017-10-19T00:00:00Z/2017-11-09T23:59:59.999Z",
             "theme": [
                 "ACEPOL",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ACEPOL Cloud Physics Lidar (CPL) Remotely Sensed Data Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NOAA-21/VIIRS/L3M/IOP/2022",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/NOAA-21/VIIRS/L3M/IOP/2022.",
-            "issued": "2023-04-04",
-            "temporal": "2022-11-10T00:00:00Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-04",
-            "keyword": [
-                "biosphere",
-                "ocean optics",
-                "oceans",
-                "ecosystems",
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
-            "identifier": "C2652675346-OB_DAAC",
             "description": "The Visible and Infrared Imager/Radiometer Suite (VIIRS) is a multi-disciplinary instrument that is being flown on the Joint Polar Satellite System (JPSS) series of spacecraft, including the Suomi National Polar-orbiting Partnership (S-NPP) that launched in October 2011.  JPSS is a multi-platform, multi-agency program that consolidates the polar orbiting spacecraft of NASA and the National Oceanic and Atmospheric Administration (NOAA).  S-NPP is the initial spacecraft in this series, and VIIRS is the successor to MODIS for Earth science data product generation.  VIIRS has 22 spectral bands ranging from 412 nm to 12 nm.  There are 16 moderate-resolution bands (750m at nadir), 5 image-resolution bands (375m), and one day-night band (DNB).",
-            "title": "NOAA-21 VIIRS Global Mapped Inherent Optical Properties (IOP) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNOAA-21%2FVIIRS%2FL3M%2FIOP%2F2022",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNOAA-21%2FVIIRS%2FL3M%2FIOP%2F2022",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NOAA-21/VIIRS/L3M/IOP/2022",
-                    "description": "VIIRS-NOAA-21 L3M Inherent Optical Properties (IOP) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS-NOAA-21 L3M Inherent Optical Properties (IOP) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NOAA-21/VIIRS/L3M/IOP/2022",
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
+            "identifier": "C2652675346-OB_DAAC",
+            "issued": "2023-04-04",
+            "keyword": [
+                "biosphere",
+                "ocean optics",
+                "oceans",
+                "ecosystems",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/NOAA-21/VIIRS/L3M/IOP/2022",
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
+            "title": "NOAA-21 VIIRS Global Mapped Inherent Optical Properties (IOP) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0474-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-12-05T04:26:35.000 to 2014-12-05T12:29:07.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0474-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0474-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0474-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-12-05T04:26:35.000 to 2014-12-05T12:29:07.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0474 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0474 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-SWAP-3-JUPITER-V1.0",
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
-                "solar wind"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Calibrated data taken by the New Horizons Solar Wind Around Pluto instrument during the Jupiter encounter mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-swap-3-jupiter-v1.0_fdki-pxgr",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons",
+                "solar wind"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-SWAP-3-JUPITER-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-swap-3-jupiter-v1.0_fdki-pxgr",
-            "description": "This data set contains Calibrated data taken by the New Horizons Solar Wind Around Pluto instrument during the Jupiter encounter mission phase.",
-            "title": "NEW HORIZONS SWAP JUPITER ENCOUNTER V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS SWAP JUPITER ENCOUNTER V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/40L92G8144IV",
             "citation": "Omar Torres. 2019-09-17. OMPS_NPP_NMMIEAI_L2. Version 2. OMPS-NPP L2 NM Aerosol Index swath orbital V2. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/40L92G8144IV. https://disc.gsfc.nasa.gov/datacollection/OMPS_NPP_NMMIEAI_L2_2.html. Digital Science Data.",
-            "issued": "2018-12-06",
-            "temporal": "2011-11-07T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-12-06",
-            "references": [
-                "https://doi.org/10.1029/98JD00900"
-            ],
-            "keyword": [
-                "aerosols",
-                "atmosphere",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "OMAR TORRES, PH. D",
                 "hasEmail": "mailto:omar.o.torres@nasa.gov"
             },
+            "creator": "Omar Torres",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1564538427-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The OMPS-NPP L2 NM Aerosol Index swath orbital product provides aerosol index values from the Ozone Mapping and Profiling Suite (OMPS) Nadir-Mapper (NM) instrument on the Suomi-NPP satellite. This is now the official NASA aerosol index product, replacing the aerosol index found in the OMPS-NPP L2 NM Total Ozone product. The aerosol index is derived from normalized radiances using 2 wavelength pairs at 340 and 378.5 nm. Additionally, this data product contains measurements of normalized radiances, reflectivity, cloud fraction, reflectivity, and other ancillary variables.\n\nEach granule contains data from the daylight portion of each orbit measured for a full day. Spatial coverage is global (-90 to  90 degrees latitude), and there are about 14.5 orbits per day, each has typically 400 swaths. The swath width of the NM is about 2800 km with 36 scenes, or pixels, with a footprint size of 50 km x 50 km at nadir.\n\nThe data are written using the Hierarchical Data Format Version 5 or HDF5.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OMPS_NPP_NMMIEAI_L2",
-            "creator": "Omar Torres",
-            "title": "OMPS-NPP L2 NM Aerosol Index swath orbital",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMPS_NPP_NMMIEAI_L2_2.jpeg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F40L92G8144IV",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F40L92G8144IV",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -753327,249 +753302,252 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMPS_NPP_NMMIEAI_L2_2.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMPS_NPP_NMMIEAI_L2_2.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://snpp-omps.gesdisc.eosdis.nasa.gov/data/SNPP_OMPS_Level2/OMPS_NPP_NMMIEAI_L2.2/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://snpp-omps.gesdisc.eosdis.nasa.gov/data/SNPP_OMPS_Level2/OMPS_NPP_NMMIEAI_L2.2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://snpp-omps.gesdisc.eosdis.nasa.gov/opendap/SNPP_OMPS_Level2/OMPS_NPP_NMMIEAI_L2.2/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://snpp-omps.gesdisc.eosdis.nasa.gov/opendap/SNPP_OMPS_Level2/OMPS_NPP_NMMIEAI_L2.2/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMPS_NPP_NMMIEAI_L2_2",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMPS_NPP_NMMIEAI_L2_2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://snpp-omps.gesdisc.eosdis.nasa.gov/data/SNPP_OMPS_Level2/OMPS_NPP_NMMIEAI_L2.2/doc/README.OMPS_NPP_NMMIEAI_L2.2.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://snpp-omps.gesdisc.eosdis.nasa.gov/data/SNPP_OMPS_Level2/OMPS_NPP_NMMIEAI_L2.2/doc/README.OMPS_NPP_NMMIEAI_L2.2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://jointmission.gsfc.nasa.gov/",
-                    "description": "Joint Polar Satellite System (JPSS) mission home page",
                     "@type": "dcat:Distribution",
+                    "description": "Joint Polar Satellite System (JPSS) mission home page",
+                    "downloadURL": "https://jointmission.gsfc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMPS_NPP_NMMIEAI_L2_2.jpeg",
+            "identifier": "C1564538427-GES_DISC",
+            "issued": "2018-12-06",
+            "keyword": [
+                "aerosols",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/40L92G8144IV",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-12-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1029/98JD00900"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "OMPS_NPP_NMMIEAI_L2",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-11-07T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OMPS-NPP L2 NM Aerosol Index swath orbital"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-EXT1-67P-M25-INFLDSTR-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the ROSETTA EXTENSION 1 mission phase, covering the period  from 2016-01-12T23:25:00.000 to 2016-02-09T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-ext1-67p-m25-infldstr-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-EXT1-67P-M25-INFLDSTR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-ext1-67p-m25-infldstr-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the ROSETTA EXTENSION 1 mission phase, covering the period  from 2016-01-12T23:25:00.000 to 2016-02-09T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 EXT1-MTP025 RDR-INFLDSTR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 EXT1-MTP025 RDR-INFLDSTR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/fdqq-aept",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brad Cenko",
+                "hasEmail": "mailto:brad.cenko@nasa.gov"
+            },
+            "describedBy": "http://128.32.15.133/kait/agn/README",
+            "description": "This web page shows the light curves of a total of 163 AGNs that are monitored by KAIT with average cadence of 3 days. These are unfiltered observations; in practice, they correspond roughly to the R band (see Li et al. 2003, PASP, 115, 844).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://128.32.15.133/kait/agn/",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000240",
             "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "fermi",
                 "kait",
                 "agn"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brad Cenko",
-                "hasEmail": "mailto:brad.cenko@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/fdqq-aept",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:006"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000240",
-            "description": "This web page shows the light curves of a total of 163 AGNs that are monitored by KAIT with average cadence of 3 days. These are unfiltered observations; in practice, they correspond roughly to the R band (see Li et al. 2003, PASP, 115, 844).",
-            "title": "KAIT Fermi AGN Light-Curve Reservoir",
-            "programCode": [
-                "026:006"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://128.32.15.133/kait/agn/",
-                    "mediaType": "text/html"
-                }
-            ],
-            "describedBy": "http://128.32.15.133/kait/agn/README",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Applied Science"
-            ]
+            ],
+            "title": "KAIT Fermi AGN Light-Curve Reservoir"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67P-M05-REFLECT-V1.0",
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
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-07-02T08:35:00.000 to 2014-08-01T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67p-m05-reflect-v1.0_fdr2-p495",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67P-M05-REFLECT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67p-m05-reflect-v1.0_fdr2-p495",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-07-02T08:35:00.000 to 2014-08-01T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP005 RDR-REFLECT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP005 RDR-REFLECT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/393/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2011-06-07",
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
-            "identifier": "DASHLINK_393",
             "description": "Prognostics is an emerging concept in condition based maintenance (CBM) of critical systems. Along with developing the fundamentals of being able to confidently predict Remaining Useful Life (RUL), the technology calls for fielded applications as it inches towards maturation. This requires a stringent performance evaluation so that the significance of the concept can be fully exploited. Currently, prognostics concepts lack standard definitions and suffer from ambiguous and inconsistent interpretations. This lack of standards is in part due to the varied end-user requirements for different applications, time scales, available information, domain dynamics, etc. to name a few issues. Instead, the research community has used a variety of metrics based largely on convenience with respect to their respective requirements. Very little attention has been focused on establishing a common ground to compare different efforts. This paper surveys the metrics that are already used for prognostics in a variety of domains including medicine, nuclear, automotive, aerospace, and electronics. It also considers other domains that involve prediction-related tasks, such as weather and finance.  Differences and similarities between these domains and health maintenance have been analyzed to help understand what performance evaluation methods may or may not be borrowed. Further, these metrics have been categorized in several ways that may be useful in deciding upon a suitable subset for a\r\nspecific application. Some important prognostic concepts have been defined using a notational framework that enables interpretation of different metrics coherently. Last, but not the \r\nleast, a list of metrics has been suggested to assess critical aspects of RUL predictions before they are fielded in real applications.",
-            "title": "Metrics for Evaluating Performance of Prognostics Techniques",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/force-download",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/PHM_2008_Metrics.pdf",
-                    "description": "PHM_2008_Metrics.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "PHM_2008_Metrics.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/PHM_2008_Metrics.pdf",
+                    "mediaType": "application/force-download",
                     "title": "PHM_2008_Metrics.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_393",
+            "issued": "2011-06-07",
+            "keyword": [
+                "nasa",
+                "dashlink",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/393/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Metrics for Evaluating Performance of Prognostics Techniques"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C3272764592-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "OCO Science Team/Michael Gunson, AnnmarieEldering. 2024-10-29. OCO3_L2_ABand. Version 11. OCO-3 Level 2 spatially ordered geolocated retrievals screened using the A-band Preprocessor, Forward Processing V11. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/OCO3_L2_ABand_11.html. Digital Science Data.",
-            "issued": "2021-05-31",
-            "temporal": "2019-08-06T00:00:00Z/2024-11-11T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-31",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "atmospheric chemistry"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "THOMAS HEARTY",
                 "hasEmail": "mailto:Thomas.J.Hearty@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C3272764592-GES_DISC",
-            "description": "Version 11 is the current version of the data set. Older versions will no longer be available and are superseded by Version 11.\n\nThe Orbiting Carbon Observatory -3 (OCO-3) was deployed to the International Space Station in May, 2019. It is technically a single instrument, almost identical to OCO-2.\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere.\n\nOCO-3 incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers. The three spectrometers have different characteristics and are calibrated independently. \n\nOxygen-A Band cloud screening algorithm is one of the primary cloud screening tools implemented in the operational OCO processing pipeline. The algorithm was introduced and applied to early GOSAT data  with further analysis performed on OCO-2 simulations.\n\nThe OCO ABO2 algorithm employs a fast Bayesian retrieval to estimate surface pressure and surface albedo from high resolution spectra of the molecular oxygen (O2) A-band, near 0.765 \u00b5m. The radiative transfer forward model (FM) assumes a clear-sky condition, i.e. Rayleigh scattering only, such that differences between the modeled and measured radiances are apparent when the measurement scene contains cloud or aerosol.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OCO3_L2_ABand",
             "creator": "OCO Science Team/Michael Gunson, AnnmarieEldering",
-            "title": "OCO-3 Level 2 spatially ordered geolocated retrievals screened using the A-band Preprocessor, Forward Processing V11 (OCO3_L2_ABand) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO3_logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Version 11 is the current version of the data set. Older versions will no longer be available and are superseded by Version 11.\n\nThe Orbiting Carbon Observatory -3 (OCO-3) was deployed to the International Space Station in May, 2019. It is technically a single instrument, almost identical to OCO-2.\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere.\n\nOCO-3 incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers. The three spectrometers have different characteristics and are calibrated independently. \n\nOxygen-A Band cloud screening algorithm is one of the primary cloud screening tools implemented in the operational OCO processing pipeline. The algorithm was introduced and applied to early GOSAT data  with further analysis performed on OCO-2 simulations.\n\nThe OCO ABO2 algorithm employs a fast Bayesian retrieval to estimate surface pressure and surface albedo from high resolution spectra of the molecular oxygen (O2) A-band, near 0.765 \u00b5m. The radiative transfer forward model (FM) assumes a clear-sky condition, i.e. Rayleigh scattering only, such that differences between the modeled and measured radiances are apparent when the measurement scene contains cloud or aerosol.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -753578,66 +753556,66 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO3_L2_ABand_11.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO3_L2_ABand_11.html",
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
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO3_DATA/OCO3_L2_ABand.11/",
-                    "description": "Access the data via HTTP",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO3_DATA/OCO3_L2_ABand.11/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO3_L2_ABand",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO3_L2_ABand",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO3_L2_ABand.11/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO3_L2_ABand.11/contents.html",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/README.OCO2.pdf",
-                    "description": "README document",
                     "@type": "dcat:Distribution",
+                    "description": "README document",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/SDOS_SIS_L2Fluorescence.V6.pdf",
-                    "description": "Software Interface Specification",
                     "@type": "dcat:Distribution",
+                    "description": "Software Interface Specification",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/SDOS_SIS_L2Fluorescence.V6.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
@@ -753647,408 +753625,432 @@
                     "title": "View this dataset's algorithm theoretical basis document"
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
+            "identifier": "C3272764592-GES_DISC",
+            "issued": "2021-05-31",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C3272764592-GES_DISC.html",
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
+            "series-name": "OCO3_L2_ABand",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2019-08-06T00:00:00Z/2024-11-11T00:00:00Z",
             "theme": [
                 "OCO-3",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OCO-3 Level 2 spatially ordered geolocated retrievals screened using the A-band Preprocessor, Forward Processing V11 (OCO3_L2_ABand) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/Not Applicable",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2018-12-06. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/Not Applicable. https://asdc.larc.nasa.gov/project/MISR.",
-            "issued": "1998-10-14",
-            "temporal": "2018-05-04T00:00:00Z/2024-03-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "infrared wavelengths",
-                "spectral/engineering",
-                "visible wavelengths",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DAVID, DR. DINER",
                 "hasEmail": "mailto:david.j.diner@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C179031533-LARC",
             "description": "MIL1A_2 is the Multi-angle Imaging SpectroRadiometer (MISR) Level 1A CCD Science data, all cameras version 2. It is the Reformatted Annotated Level 1A product for the CCD science data. The data numbers (DN) have been commuted from 12-bit numbers to 16-bit byte aligned half-words. The MISR CCD Science Instrument Data acquired from all nine of the MISR cameras for each of the four bands represent the raw MISR input data staged for MISR Science Instrument Data processing. There are nine file granules of this type, one corresponding to each of the nine MISR cameras. Each file granule contains four entire swaths of data, one swath for each of the four MISR bands associated with each MISR camera. The MISR instrument consists of nine pushbroom cameras which measure radiance in four spectral bands. Global coverage is achieved in nine days. The cameras are arranged with one camera pointing toward the nadir, four cameras pointing forward, and four cameras pointing aftward. It takes seven minutes for all nine cameras to view the same surface location. The view angles relative to the surface reference ellipsoid, are 0, 26.1, 45.6, 60.0, and 70.5 degrees. The spectral band shapes are nominally Gaussian, centered at 443, 555, 670, and 865 nm.",
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "title": "MISR Level 1A CCD Science data, all cameras V002",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=Not+Applicable",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=Not+Applicable",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/DPS_v50_RevS.pdf",
-                    "description": "Data Product Specification for MISR V4.2 Software Delivery Updates - Revision P, November 19, 2007",
                     "@type": "dcat:Distribution",
+                    "description": "Data Product Specification for MISR V4.2 Software Delivery Updates - Revision P, November 19, 2007",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/DPS_v50_RevS.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C179031533-LARC",
-                    "description": "Earthdata Search for MIL1A_2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for MIL1A_2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C179031533-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MISR/MIL1A.002/contents.html",
-                    "description": "OPeNDAP data access for MIL1A_2",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for MIL1A_2",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MISR/MIL1A.002/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/cgi-bin/DUE/ecs_pge_history_L1_PR.cgi",
-                    "description": "MISR Level 1 Production Report",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Level 1 Production Report",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/cgi-bin/DUE/ecs_pge_history_L1_PR.cgi",
+                    "mediaType": "text/html",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L1_Products.pdf",
-                    "description": "MISR Level 1 Products Quality Statement - August 29, 2007",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Level 1 Products Quality Statement - August 29, 2007",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L1_Products.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's data quality document"
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
-                    "downloadURL": "https://www.google.com/earth/",
-                    "description": "Google Earth",
                     "@type": "dcat:Distribution",
+                    "description": "Google Earth",
+                    "downloadURL": "https://www.google.com/earth/",
+                    "mediaType": "text/html",
                     "title": "Use this dataset in a web based map viewerf"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/MISR/MIL1A.002/",
-                    "description": "ASDC Direct Data Download for MIL1A_2",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for MIL1A_2",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/MISR/MIL1A.002/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/MISR/MIL1A_2",
-                    "description": "Data set landing page for MIL1A_2",
                     "@type": "dcat:Distribution",
+                    "description": "Data set landing page for MIL1A_2",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/MISR/MIL1A_2",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/quality_summaries/maturity_def.pdf",
-                    "description": "MISR Maturity Level Definitions",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Maturity Level Definitions",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/quality_summaries/maturity_def.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's processing history"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/pge1.html",
-                    "description": "ASDC List of MISR Level 1A CCD, 1B1, 1B2, and Browse Products",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC List of MISR Level 1A CCD, 1B1, 1B2, and Browse Products",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/pge1.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/file_descriptions.html",
-                    "description": "ASDC Overview of MISR File Naming and Versioning Conventions",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Overview of MISR File Naming and Versioning Conventions",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/file_descriptions.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/index.html",
-                    "description": "ASDC Overview of MISR Data Versioning Index",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Overview of MISR Data Versioning Index",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/index.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/misr_qual_stmts_current.html",
-                    "description": "MISR Quality Statements - September 30, 2014",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Quality Statements - September 30, 2014",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/misr_qual_stmts_current.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data quality document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/misr_qual_stmts_new.html",
-                    "description": "MISR Quality Statements - September 30, 2014",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Quality Statements - September 30, 2014",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/misr_qual_stmts_new.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data quality document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/dps/dps.html",
-                    "description": "Data Product Specification for MISR Data Products",
                     "@type": "dcat:Distribution",
+                    "description": "Data Product Specification for MISR Data Products",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/dps/dps.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/dps/specific_products.html",
-                    "description": "Data Product Specification for Specific Products MISR Data Products",
                     "@type": "dcat:Distribution",
+                    "description": "Data Product Specification for Specific Products MISR Data Products",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/dps/specific_products.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product usage"
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
-                    "downloadURL": "https://terra.nasa.gov/?section=60",
-                    "description": "TERRA Overview",
                     "@type": "dcat:Distribution",
+                    "description": "TERRA Overview",
+                    "downloadURL": "https://terra.nasa.gov/?section=60",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
                 }
             ],
+            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
+            "identifier": "C179031533-LARC",
+            "issued": "1998-10-14",
+            "keyword": [
+                "infrared wavelengths",
+                "spectral/engineering",
+                "visible wavelengths",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/Not Applicable",
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
+            "temporal": "2018-05-04T00:00:00Z/2024-03-27T00:00:00Z",
             "theme": [
                 "MISR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR Level 1A CCD Science data, all cameras V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-M-OSIWAC-4-MARS-MARSSWINGBY-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the MARS SWING-BY mission phase, covering the period  from 2006-07-29T00:00:00.000 to 2007-05-28T23:59:59.000. The prime target is planet Mars. This version V1.0 is the first version of this dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-m-osiwac-4-mars-marsswingby-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "vega",
                 "mars",
@@ -754060,219 +754062,189 @@
                 "deimos",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-M-OSIWAC-4-MARS-MARSSWINGBY-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-m-osiwac-4-mars-marsswingby-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the MARS SWING-BY mission phase, covering the period  from 2006-07-29T00:00:00.000 to 2007-05-28T23:59:59.000. The prime target is planet Mars. This version V1.0 is the first version of this dataset.",
-            "title": "ROSETTA-ORBITER MARS OSIWAC 4 MARS RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER MARS OSIWAC 4 MARS RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-PRL-67PCHURYUMOV-M09-V2.0",
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
+            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera during the PRELANDING phase of the Rosetta mission at the comet 67P, covering the period from 2014-10-24T10:00:00.000 to 2014-11-21T23:24:59.000. This version V2.0 supersedes previous deliveries of the same dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-prl-67pchuryumov-m09-v2.0_fdw8-76pk",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-PRL-67PCHURYUMOV-M09-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-prl-67pchuryumov-m09-v2.0_fdw8-76pk",
-            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera during the PRELANDING phase of the Rosetta mission at the comet 67P, covering the period from 2014-10-24T10:00:00.000 to 2014-11-21T23:24:59.000. This version V2.0 supersedes previous deliveries of the same dataset.",
-            "title": "ROSETTA-ORBITER PRELANDING OSIWAC 2 EDR MTP009 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER PRELANDING OSIWAC 2 EDR MTP009 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/378",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Bubier, J.L., P.M. Crill, R.K. Varner, and T.R. Moore. 1998. BOREAS TGB-01/TGB-03 CH4 Chamber Flux Data: NSA Fen. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/378",
-            "issued": "2023-11-22",
-            "temporal": "1994-05-09T00:00:00Z/1996-10-21T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-28",
-            "keyword": [
-                "earth science",
-                "atmospheric temperature",
-                "soils",
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
-            "identifier": "C2808131382-ORNL_CLOUD",
             "description": "Contains TGB-03 methane flux data for fens in the Northern Study Area.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS TGB-01/TGB-03 CH4 Chamber Flux Data: NSA Fen",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F378",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F378",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TGB/tgbfenfx/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TGB/tgbfenfx/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TGB01_TGB03_CH4_FenFlux.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TGB01_TGB03_CH4_FenFlux.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/378",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/378",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgbfenfx/comp/TGB01_TGB03_CH4_FenFlux.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgbfenfx/comp/TGB01_TGB03_CH4_FenFlux.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgbfenfx/comp/TGB01_TGB03_CH4_FenFlux.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgbfenfx/comp/TGB01_TGB03_CH4_FenFlux.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgbfenfx/comp/TGB01_TGB03_CH4_FenFlux.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgbfenfx/comp/TGB01_TGB03_CH4_FenFlux.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgbfenfx/comp/tgbfenfx.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgbfenfx/comp/tgbfenfx.def",
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
+            "identifier": "C2808131382-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "earth science",
+                "atmospheric temperature",
+                "soils",
+                "land surface",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/378",
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
             "spatial": "55.92 -98.42",
+            "temporal": "1994-05-09T00:00:00Z/1996-10-21T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS TGB-01/TGB-03 CH4 Chamber Flux Data: NSA Fen"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/CLAMS/0002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2004-11-03. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/CLAMS/0002. http://eosweb.larc.nasa.gov/project/clams/clams_table.",
-            "issued": "2004-11-03",
-            "temporal": "2001-07-10T00:00:00Z/2001-08-02T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-02",
-            "keyword": [
-                "clouds",
-                "atmospheric pressure",
-                "visible wavelengths",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "atmosphere",
-                "aerosols",
-                "spectral/engineering",
-                "atmospheric radiation",
-                "earth science",
-                "ocean optics",
-                "oceans"
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
-            "identifier": "C1567298630-LARC_ASDC",
             "description": "CLAMS_CV580_CAR data were collected during the Chesapeake Lighthouse and Aircraft Measurements for Satellites (CLAMS) experiment.The Cloud Absorption Radiometer (CAR) instrument is an airborne multi-wavelength scanning radiometer, designed to operate from a mounted position aboard various aircraft, including the nose cone of the University of Washington's Convair CV-580. Developed by Dr. Michael King at NASA Goddard Space Flight Center, the CAR instrument measures radiance for 190 degrees, and total view at 1 degree field of view resolution. Instrument functions include: * acquiring imagery of Earth surface and Cloud features* single scattering albedo determination of clouds* angular distribution measuring of scattered radiation* bidirectional reflectance measuring of various surface types",
-            "title": "CLAMS CV-580 Cloud Absorption Radiometer (CAR)",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FCLAMS%2F0002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FCLAMS%2F0002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -754324,119 +754296,125 @@
                     "title": "View this dataset's data citation policy"
                 }
             ],
+            "identifier": "C1567298630-LARC_ASDC",
+            "issued": "2004-11-03",
+            "keyword": [
+                "clouds",
+                "atmospheric pressure",
+                "visible wavelengths",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "atmosphere",
+                "aerosols",
+                "spectral/engineering",
+                "atmospheric radiation",
+                "earth science",
+                "ocean optics",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/CLAMS/0002",
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
             "spatial": "-76.52 36.35 -70.28 38.7",
+            "temporal": "2001-07-10T00:00:00Z/2001-08-02T23:59:59Z",
             "theme": [
                 "CLAMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CLAMS CV-580 Cloud Absorption Radiometer (CAR)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7265/yy5v-5y11",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Rock-Ice Feature Inventory for the Sierra Nevada, California, USA, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center. https://doi.org/10.7265/yy5v-5y11.",
-            "issued": "2019-09-20",
-            "temporal": "1970-01-01T00:00:00Z/2024-07-08T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-07",
-            "keyword": [
-                "earth science",
-                "cryosphere",
-                "land surface",
-                "frozen ground"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Constance Millar",
                 "hasEmail": "mailto:cmillar@fs.fed.us"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NSIDC"
-            },
-            "identifier": "C1386206913-NSIDCV0",
             "description": "The Sierra Nevada is a tectonic uplift mountain range with a gradual gain in elevation on the west side and a steep escarpment on the east.  Most of the mapped locations are east of the Sierran crest. The climate in the region is Mediterranean, with most of the precipitation in the winter months coming as snow at high elevations, but with some monsoonal precipitation in the summer, particularly in the southern end of the range.   There is a very steep gradient in decreasing precipitation eastward from the Sierran crest as a result of rain-shadow orographic effects from the predominately eastward-moving Pacific frontal storms.  PRISM-estimated (Daly et al. 1994) annual precipitation for the RIF locations ranged from 580 to 1880 mm; July precipitation from 5 to 33 mm.  Mean annual maximum temperatures ranged from 1.8 to 15.2 oC, January from -5.7 to 6.2 oC, and July from 11 to 26.3 oC.  Mean annual minima ranged from -8.1 to -0.4 oC, January from -15 to -7 oC, and July from 1.2 to 8.9 oC.  The highest temperatures and lowest precipitation were largely at relict Pleistocene rock glaciers, which tended to be farthest east of the Sierran crest and lower in elevation. We mapped over 430 RIFs, based on field surveys and grouped them into six classes based on morphology and location. These categories constitute a greater range of frozen-ground features than are commonly described in rock-glacier surveys.  Although granitic substrates dominate the Sierra Nevada, they do not in the eastern escarpment, so substrates in the RIF database are about equally divided between granitic and metamorphic.  Ages of rock glaciers ranged from current (active) to relict (late Pleistocene).  We interpreted the presence of outlet springs, basal lakes, suspended silt in outlet streams, and fringing phreatophytic vegetation, in addition to morphologic indications of current rock movement, as evidence for interstitial ice, either persistent or seasonal.\n\n<br>One comma-delimited ASCII file containing information for 430 rock-ice features is available.",
-            "title": "Rock-Ice Feature Inventory for the Sierra Nevada, California, USA, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2Fyy5v-5y11",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2Fyy5v-5y11",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/GGD652_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/GGD652_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/yy5v-5y11",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/yy5v-5y11",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/yy5v-5y11",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/yy5v-5y11",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386206913-NSIDCV0",
+            "issued": "2019-09-20",
+            "keyword": [
+                "earth science",
+                "cryosphere",
+                "land surface",
+                "frozen ground"
+            ],
+            "landingPage": "https://doi.org/10.7265/yy5v-5y11",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-07-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "-119.9 34.5 -118.2 38.8",
+            "temporal": "1970-01-01T00:00:00Z/2024-07-08T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Rock-Ice Feature Inventory for the Sierra Nevada, California, USA, Version 1"
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
-                "compressible",
-                "cases",
-                "models",
-                "turbulence",
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
-            "identifier": "NASA-843__15",
             "description": "This grouping contains the compressible-flow cases from the 1980-81 Data Library.",
-            "title": "Collaborative Testing of Turbulence Models: Compressible Flow Cases from 1980-81 Data Library",
-            "programCode": [
-                "026:023"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -754444,566 +754422,562 @@
                     "mediaType": "application/txt"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-843__15",
+            "issued": "2018-06-25",
+            "keyword": [
+                "compressible",
+                "cases",
+                "models",
+                "turbulence",
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
+            "title": "Collaborative Testing of Turbulence Models: Compressible Flow Cases from 1980-81 Data Library"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-5-EXT1-67P-M26-GEO-V1.0",
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
+            "description": "This CODMAC level 5 data set contains derived data products that include pixel-precise georeferencing information, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 1 mission phase, covering the period from 2016-02-09T23:25:00.000 to 2016-03-08T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-5-ext1-67p-m26-geo-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-5-EXT1-67P-M26-GEO-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-5-ext1-67p-m26-geo-v1.0",
-            "description": "This CODMAC level 5 data set contains derived data products that include pixel-precise georeferencing information, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 1 mission phase, covering the period from 2016-02-09T23:25:00.000 to 2016-03-08T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 5 EXT1-MTP026 DDR-GEO V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 5 EXT1-MTP026 DDR-GEO V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-A-PPR-2-EDR-IDA-V1.0",
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
+            "description": "ARCHIVE_STATUS, , DATA_SET_TERSE_DESC,This data set contains the R_EDR data for the Galileo Orbiter PPR instrument for the period corresponding to the Ida asteroid encounter observations in October 1993.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-a-ppr-2-edr-ida-v1.0_fe5a-ud2d",
+            "issued": "2018-06-26",
+            "keyword": [
+                "galileo",
+                "ida"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-A-PPR-2-EDR-IDA-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-a-ppr-2-edr-ida-v1.0_fe5a-ud2d",
-            "description": "ARCHIVE_STATUS, , DATA_SET_TERSE_DESC,This data set contains the R_EDR data for the Galileo Orbiter PPR instrument for the period corresponding to the Ida asteroid encounter observations in October 1993.",
-            "title": "GLL PPR IDA ENCOUNTER EDR",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GLL PPR IDA ENCOUNTER EDR"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-V-MAG-4-SUMM-VENUS-SUMMARY-V1.0",
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
-                "galileo"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Galileo Orbiter Magnetometer (MAG) calibrated averaged data from the Venus flyby in VSO coordinates. These data cover the interval 1990-02-09 03:07 to 1990-02-10 08:34.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-v-mag-4-summ-venus-summary-v1.0_fe6e-mcsz",
+            "issued": "2021-05-21",
+            "keyword": [
+                "venus",
+                "galileo"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-V-MAG-4-SUMM-VENUS-SUMMARY-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-v-mag-4-summ-venus-summary-v1.0_fe6e-mcsz",
-            "description": "Galileo Orbiter Magnetometer (MAG) calibrated averaged data from the Venus flyby in VSO coordinates. These data cover the interval 1990-02-09 03:07 to 1990-02-10 08:34.",
-            "title": "GALILEO ORBITER V MAG SUMM VENUS SUMMARY V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GALILEO ORBITER V MAG SUMM VENUS SUMMARY V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/445/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2011-07-28",
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
-            "identifier": "DASHLINK_445",
             "description": "Location of the HIRENASD Iges file",
-            "title": "Other files used on Website",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/hirenasd_AePW_DLR.igs",
-                    "description": "HIRENASD Iges File",
                     "@type": "dcat:Distribution",
+                    "description": "HIRENASD Iges File",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/hirenasd_AePW_DLR.igs",
+                    "mediaType": "application/octet-stream",
                     "title": "hirenasd_AePW_DLR.igs"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_445",
+            "issued": "2011-07-28",
+            "keyword": [
+                "ames",
+                "nasa",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/445/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Other files used on Website"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-5-ESC4-MTP022-V1.0",
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
+            "description": "This data set contains derived electron and proton flux energies in MeV from the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, which had the primary target of comet 67P/Churyumov-Gerasimenko. These are CODMAC Level 5 derived data, and measure the radiation in the spacecraft environment during the Medium Term Plan 22 period of the ESCORT 4 mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-5-esc4-mtp022-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-5-ESC4-MTP022-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-5-esc4-mtp022-v1.0",
-            "description": "This data set contains derived electron and proton flux energies in MeV from the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, which had the primary target of comet 67P/Churyumov-Gerasimenko. These are CODMAC Level 5 derived data, and measure the radiation in the spacecraft environment during the Medium Term Plan 22 period of the ESCORT 4 mission phase.",
-            "title": "ROSETTA-ORBITER 67P SREM 5 ESCORT 4\n    MTP022 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P SREM 5 ESCORT 4\n    MTP022 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0690-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-02T21:37:30.000 to 2015-04-03T05:58:06.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0690-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0690-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0690-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-02T21:37:30.000 to 2015-04-03T05:58:06.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0690 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0690 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TERRA/MOPITT/MOP02T_L2.008",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2000-03-03. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/TERRA/MOPITT/MOP02T_L2.008. https://asdc.larc.nasa.gov/project/MOPITT.",
-            "issued": "2018-10-26",
-            "temporal": "2000-03-03T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "atmospheric pressure",
-                "atmospheric chemistry"
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
-            "identifier": "C1575974115-LARC",
             "description": "MOP02T_8 is the Measurements Of Pollution In The Troposphere (MOPITT) Derived Carbon Monoxide (CO) (Thermal Infrared Radiances) version 8 product. It consists of geo-located, retrieved CO profiles and total column amounts for CO. Ancillary data concerning surface properties and cloud conditions at the locations of the retrieved parameters are also included. Each retrieval is accompanied by an estimated error. MOPITT was successfully launched into sun-synchronous polar orbit aboard Terra, NASA's first Earth Observing System spacecraft, on December 18, 1999. The MOPITT instrument was constructed by a consortium of Canadian companies and funded by the Space Science Division of the Canadian Space Agency. Data collection for this product was completed in March of 2020.",
-            "graphic-preview-description": "MOPITT Visualizations",
-            "title": "MOPITT Derived CO (Thermal Infrared Radiances) V008",
-            "graphic-preview-file": "https://www2.acom.ucar.edu/mopitt/visualization",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMOPITT%2FMOP02T_L2.008",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMOPITT%2FMOP02T_L2.008",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1575974115-LARC",
-                    "description": "Earthdata Search for MOP02T_8 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for MOP02T_8 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1575974115-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
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
-                    "downloadURL": "https://worldview.earthdata.nasa.gov/",
-                    "description": "NASA Worldview",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Worldview",
+                    "downloadURL": "https://worldview.earthdata.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through WORLDVIEW"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www2.acom.ucar.edu/sites/default/files/mopitt/v8_users_guide_201812.pdf",
-                    "description": "MOPITT Version 8 Product User's Guide - December 2018",
                     "@type": "dcat:Distribution",
+                    "description": "MOPITT Version 8 Product User's Guide - December 2018",
+                    "downloadURL": "https://www2.acom.ucar.edu/sites/default/files/mopitt/v8_users_guide_201812.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
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
-                    "downloadURL": "https://doi.org/10.5067/TERRA/MOPITT/MOP02T_L2.008",
-                    "description": "DOI data set landing page for MOP02T_8",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for MOP02T_8",
+                    "downloadURL": "https://doi.org/10.5067/TERRA/MOPITT/MOP02T_L2.008",
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
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MOPITT/MOP02T.008/contents.html",
-                    "description": "OPeNDAP data access for MOP02T_8",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for MOP02T_8",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MOPITT/MOP02T.008/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/MOPITT/MOP02T.008/",
-                    "description": "ASDC Direct Data Download for MOP02T_8",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for MOP02T_8",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/MOPITT/MOP02T.008/",
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
+            "identifier": "C1575974115-LARC",
+            "issued": "2018-10-26",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "atmospheric pressure",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/TERRA/MOPITT/MOP02T_L2.008",
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
+            "title": "MOPITT Derived CO (Thermal Infrared Radiances) V008"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SENTINEL5P/S5P_L1B_RA_BD2.1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Copernicus Sentinel data processed by ESA, Koninklijk Nederlands Meteorologisch Instituut (KNMI). 2018-08-23. S5P_L1B_RA_BD2. Version 1. Sentinel-5P TROPOMI L1B Radiance product band 2 (UV detector). Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/SENTINEL5P/S5P_L1B_RA_BD2.1. https://disc.gsfc.nasa.gov/datacollection/S5P_L1B_RA_BD2_1.html. Digital Science Data.",
-            "issued": "2014-12-09",
-            "temporal": "2018-04-30T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2014-12-09",
-            "keyword": [
-                "sensor characteristics",
-                "ultraviolet wavelengths",
-                "atmospheric radiation",
-                "atmosphere",
-                "earth science",
-                "spectral/engineering",
-                "platform characteristics"
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
-            "identifier": "C1442068497-GES_DISC",
-            "description": "Starting from August 6th in 2019, Sentinel-5P TROPOMI along-track high spatial resolution (~5.5km at nadir) has been implemented.\nFor data after August 6th of 2019, please check S5P_L1B_RA_BD2 data collection.\n\nThe Copernicus Sentinel-5 Precursor (Sentinel-5P or S5P) satellite mission is one of the European Space Agency's (ESA) new mission family - Sentinels, and it is a joint initiative between the Kingdom of the Netherlands and the ESA. The sole payload on Sentinel-5P is the TROPOspheric Monitoring Instrument (TROPOMI), which is a nadir-viewing 108 degree Field-of-View push-broom grating hyperspectral spectrometer, covering the wavelength of ultraviolet-visible (UV-VIS, 270nm to 495nm), near infrared (NIR, 675nm to 775nm), and shortwave infrared (SWIR, 2305nm-2385nm).\nTROPOMI Level-1B (L1B) product is generated by the Koninklijk Nederlands Meteoroligisch Instituut (KNMI) TROPOMI L01B processor from Level-0 input data and auxiliary data products with the netCDF-4 enhanced model. It provides users with radiance, irradiance, calibration and engineering products.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "S5P_L1B_RA_BD2",
             "creator": "Copernicus Sentinel data processed by ESA, Koninklijk Nederlands Meteorologisch Instituut (KNMI)",
-            "title": "Sentinel-5P TROPOMI Radiance product band 2 (UV detector) L1B V1 (S5P_L1B_RA_BD2) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/S5P_OFFL_L1B_RA_BD2_1.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Starting from August 6th in 2019, Sentinel-5P TROPOMI along-track high spatial resolution (~5.5km at nadir) has been implemented.\nFor data after August 6th of 2019, please check S5P_L1B_RA_BD2 data collection.\n\nThe Copernicus Sentinel-5 Precursor (Sentinel-5P or S5P) satellite mission is one of the European Space Agency's (ESA) new mission family - Sentinels, and it is a joint initiative between the Kingdom of the Netherlands and the ESA. The sole payload on Sentinel-5P is the TROPOspheric Monitoring Instrument (TROPOMI), which is a nadir-viewing 108 degree Field-of-View push-broom grating hyperspectral spectrometer, covering the wavelength of ultraviolet-visible (UV-VIS, 270nm to 495nm), near infrared (NIR, 675nm to 775nm), and shortwave infrared (SWIR, 2305nm-2385nm).\nTROPOMI Level-1B (L1B) product is generated by the Koninklijk Nederlands Meteoroligisch Instituut (KNMI) TROPOMI L01B processor from Level-0 input data and auxiliary data products with the netCDF-4 enhanced model. It provides users with radiance, irradiance, calibration and engineering products.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSENTINEL5P%2FS5P_L1B_RA_BD2.1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSENTINEL5P%2FS5P_L1B_RA_BD2.1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -755013,110 +754987,116 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/S5P_L1B_RA_BD2_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/S5P_L1B_RA_BD2_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/opendap/S5P_TROPOMI_Level1B/S5P_L1B_RA_BD2.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/opendap/S5P_TROPOMI_Level1B/S5P_L1B_RA_BD2.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/data/S5P_TROPOMI_Level1B/S5P_L1B_RA_BD2.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/data/S5P_TROPOMI_Level1B/S5P_L1B_RA_BD2.1/",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=S5P_L1B_RA_BD2_1",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=S5P_L1B_RA_BD2_1",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/S5P_OFFL_L1B_RA_BD2_1.png",
+            "identifier": "C1442068497-GES_DISC",
+            "issued": "2014-12-09",
+            "keyword": [
+                "sensor characteristics",
+                "ultraviolet wavelengths",
+                "atmospheric radiation",
+                "atmosphere",
+                "earth science",
+                "spectral/engineering",
+                "platform characteristics"
+            ],
+            "landingPage": "https://doi.org/10.5067/SENTINEL5P/S5P_L1B_RA_BD2.1",
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
+            "series-name": "S5P_L1B_RA_BD2",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-04-30T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Sentinel-5P",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sentinel-5P TROPOMI Radiance product band 2 (UV detector) L1B V1 (S5P_L1B_RA_BD2) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "http://www.opengeospatial.org/standards/wmts",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "maps",
-                "digital",
-                "imagery",
-                "wmts",
-                "tiles",
-                "scale"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ryan Boller",
                 "hasEmail": "mailto:ryan.a.boller@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-423",
             "description": "The WMTS implementation standard provides a standards-based solution for serviing digital maps using predefined image tiles.  Through the constructs of the specification, a WMTS service advertises imagery layers (e.g. imagery product) and defines the coordinate reference system, scale, and tiling grid available for access.",
-            "title": "GIBS Web Map Tile Service (WMTS)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -755124,429 +755104,430 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-423",
+            "issued": "2018-06-25",
+            "keyword": [
+                "maps",
+                "digital",
+                "imagery",
+                "wmts",
+                "tiles",
+                "scale"
+            ],
+            "landingPage": "http://www.opengeospatial.org/standards/wmts",
+            "modified": "2020-01-29",
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
+            "title": "GIBS Web Map Tile Service (WMTS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ISS/SAGEIII/SOLAR_HDF5_L1B-V5.2",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2017-03-17. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ISS/SAGEIII/SOLAR_HDF5_L1B-V5.2. https://asdc.larc.nasa.gov/project/SAGE%20III-ISS.",
-            "issued": "2018-08-22",
-            "temporal": "2017-06-07T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric chemistry",
-                "atmospheric radiation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dr. Flittner",
                 "hasEmail": "mailto:david.e.flittner@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2066317194-LARC",
             "description": "g3bt_52 is the Stratospheric Aerosol and Gas Experiment III (SAGE III) on the International Space Station (ISS) (SAGE III/ISS) Level 1B Lunar Event Species Profiles (HDF5) V052 data product. It contains pixel group transmission profiles for a single solar event. SAGE III was Launched on February 19, 2017 on a SpaceX Falcon 9 from Kennedy Space Center, SAGE III-ISS is the second instrument from the SAGE III project, externally mounted on the ISS. This ISS-based instrument uses a technique known as occultation, which involves looking at the light from the Sun or Moon as it passes through Earth's atmosphere at the edge, or limb, of the planet to provide long-term monitoring of ozone vertical profiles of the stratosphere and mesosphere. The data provided by SAGE III-ISS includes key components of atmospheric composition and their long-term variability, focusing on the study of aerosols, chlorine dioxide, clouds, nitrogen dioxide, nitrogen trioxide, pressure and temperature, and water vapor. SAGE data has historically been used by the World Meteorological Organization to inform their periodic assessments of ozone depletion. These new observations from the International Space Station will continue the SAGE team's contributions to ongoing scientific understanding of the Earth's atmosphere.",
-            "title": "SAGE III/ISS L1B Solar Event Transmission Data (HDF5) V052",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FISS%2FSAGEIII%2FSOLAR_HDF5_L1B-V5.2",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FISS%2FSAGEIII%2FSOLAR_HDF5_L1B-V5.2",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sage.nasa.gov/",
-                    "description": "SAGE project home page",
                     "@type": "dcat:Distribution",
+                    "description": "SAGE project home page",
+                    "downloadURL": "https://sage.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/guide/DPUG-G3B.docx",
-                    "description": "SAGE III/ISS Data Products User\u2019s Guide, April 2021",
                     "@type": "dcat:Distribution",
+                    "description": "SAGE III/ISS Data Products User\u2019s Guide, April 2021",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/guide/DPUG-G3B.docx",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/x-tar",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/read_software/sageiii_iss_readers.tar",
-                    "description": "SAGE III/ISS Data Read Software Package - Direct File Download (.tar)",
                     "@type": "dcat:Distribution",
+                    "description": "SAGE III/ISS Data Read Software Package - Direct File Download (.tar)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/read_software/sageiii_iss_readers.tar",
+                    "mediaType": "application/x-tar",
                     "title": "Downloadable software applications"
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
-                    "downloadURL": "https://doi.org/10.5067/ISS/SAGEIII/SOLAR_HDF5_L1B-V5.2",
-                    "description": "DOI data set landing page for g3bt_52",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for g3bt_52",
+                    "downloadURL": "https://doi.org/10.5067/ISS/SAGEIII/SOLAR_HDF5_L1B-V5.2",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/guide/Release_Notes_v5.2.docx",
-                    "description": "SAGE III/ISS Version 5.2 Release Notes",
                     "@type": "dcat:Distribution",
+                    "description": "SAGE III/ISS Version 5.2 Release Notes",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/guide/Release_Notes_v5.2.docx",
+                    "mediaType": "text/html",
                     "title": "View an important notice for this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/read_software/19529_SAGE_III_NOSA_1.3_License.pdf",
-                    "description": "NASA Open Source Agreement for Computer Software",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Open Source Agreement for Computer Software",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/read_software/19529_SAGE_III_NOSA_1.3_License.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2066317194-LARC",
-                    "description": "Earthdata Search for g3bt_52 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for g3bt_52 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2066317194-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/SAGE_III_ISS/g3bt.052/",
-                    "description": "ASDC Direct Data Download for g3bt_52",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for g3bt_52",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/SAGE_III_ISS/g3bt.052/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/SAGE%20III-ISS",
-                    "description": "ASDC Data and Information for SAGE III-ISS",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for SAGE III-ISS",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/SAGE%20III-ISS",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2066317194-LARC",
+            "issued": "2018-08-22",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://doi.org/10.5067/ISS/SAGEIII/SOLAR_HDF5_L1B-V5.2",
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
+            "temporal": "2017-06-07T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "SAGE III-ISS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAGE III/ISS L1B Solar Event Transmission Data (HDF5) V052"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2105",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Liston, G.E., A.K. Reinking, and N.T. Boleman. 2023. Daily SnowModel Outputs Covering the ABoVE Core Domain, 3-km Resolution, 1980-2020. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2105",
-            "issued": "2023-01-27",
-            "temporal": "1980-09-01T00:00:00Z/2020-08-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-17",
-            "keyword": [
-                "atmospheric water vapor",
-                "atmospheric winds",
-                "atmospheric temperature",
-                "atmosphere",
-                "cryosphere",
-                "earth science",
-                "precipitation",
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
-            "identifier": "C2600317177-ORNL_CLOUD",
             "description": "This dataset provides daily SnowModel simulation outputs on a 3-km grid for the period 1 September 1980 through 31 August 2020, covering the Core ABoVE Domain. The daily outputs include: air temperature (deg C), relative humidity (%), wind speed (m/s), wind direction (deg from True North), total precipitation (rain+snow) (m), rainfall (m), snowfall (m), snow melt (m), snow sublimation (m), runoff (m), surface temperature (deg C), bulk snowpack thermal resistance (K/W), snow depth (m), snow density (kg/m3), and snow-water-equivalent (SWE) depth (m). Model data inputs included land cover and topography, ground-based observations of snow, remote sensing observations of snow from satellites and aircraft, and meteorological forcing data from weather stations and reanalysis data. The SnowModel includes the processing modules MicroMet, Enbal, SnowDunes, SnowAssin, SnowPack, and SnowTran-3D. The data are provided in NetCDF format.",
-            "graphic-preview-description": "The topographic distribution and core domain boundary of the ABoVE study area (image is from Liston and Reinking, 2022).",
-            "title": "Daily SnowModel Outputs Covering the ABoVE Core Domain, 3-km Resolution, 1980-2020",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/ABoVE_SnowModel_Data_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2105",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2105",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/ABoVE_SnowModel_Data/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/ABoVE_SnowModel_Data/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ABoVE_SnowModel_Data.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ABoVE_SnowModel_Data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2105",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2105",
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
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/ABoVE_SnowModel_Data/comp/ABoVE_SnowModel_Data.pdf",
-                    "description": "Daily SnowModel Outputs Covering the ABoVE Core Domain, 3-km Resolution, 1980-2020: ABoVE_SnowModel_Data.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Daily SnowModel Outputs Covering the ABoVE Core Domain, 3-km Resolution, 1980-2020: ABoVE_SnowModel_Data.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/ABoVE_SnowModel_Data/comp/ABoVE_SnowModel_Data.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/ABoVE_SnowModel_Data/comp/SnowModel_Summary_ABoVE_Core_Domain_3km.pdf",
-                    "description": "Daily SnowModel Outputs Covering the ABoVE Core Domain, 3-km Resolution, 1980-2020: SnowModel_Summary_ABoVE_Core_Domain_3km.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Daily SnowModel Outputs Covering the ABoVE Core Domain, 3-km Resolution, 1980-2020: SnowModel_Summary_ABoVE_Core_Domain_3km.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/ABoVE_SnowModel_Data/comp/SnowModel_Summary_ABoVE_Core_Domain_3km.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ABoVE_SnowModel_Data_Fig1.png",
-                    "description": "The topographic distribution and core domain boundary of the ABoVE study area (image is from Liston and Reinking, 2022).",
                     "@type": "dcat:Distribution",
+                    "description": "The topographic distribution and core domain boundary of the ABoVE study area (image is from Liston and Reinking, 2022).",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ABoVE_SnowModel_Data_Fig1.png",
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
+            "graphic-preview-description": "The topographic distribution and core domain boundary of the ABoVE study area (image is from Liston and Reinking, 2022).",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/ABoVE_SnowModel_Data_Fig1.png",
+            "identifier": "C2600317177-ORNL_CLOUD",
+            "issued": "2023-01-27",
+            "keyword": [
+                "atmospheric water vapor",
+                "atmospheric winds",
+                "atmospheric temperature",
+                "atmosphere",
+                "cryosphere",
+                "earth science",
+                "precipitation",
+                "snow/ice"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2105",
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
             "spatial": "-176.91 49.8 -84.33 75.84",
+            "temporal": "1980-09-01T00:00:00Z/2020-08-31T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Daily SnowModel Outputs Covering the ABoVE Core Domain, 3-km Resolution, 1980-2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DC3_MetNav_AircraftInSitu_DLR-Falcon_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2021-04-29. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/DC3_MetNav_AircraftInSitu_DLR-Falcon_Data_1.",
-            "issued": "2021-03-12",
-            "temporal": "2012-05-29T00:00:00Z/2012-06-14T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-04-29",
-            "keyword": [
-                "atmosphere",
-                "atmospheric temperature",
-                "atmospheric winds",
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
-            "identifier": "C2050607204-LARC_ASDC",
             "description": "DC3_MetNav_AircraftInSitu_DLR-Falcon_Data are meteorological and navigational data collected onboard the DLR Falcon aircraft during the Deep Convective Clouds and Chemistry (DC3) field campaign. Data collection for this product is complete.\r\n\r\nThe Deep Convective Clouds and Chemistry (DC3) field campaign sought to understand the dynamical, physical, and lightning processes of deep, mid-latitude continental convective clouds and to define the impact of these clouds on upper tropospheric composition and chemistry. DC3 was conducted from May to June 2012 with a base location of Salina, Kansas. Observations were conducted in northeastern Colorado, west Texas to central Oklahoma, and northern Alabama in order to provide a wide geographic sample of storm types and boundary layer compositions, as well as to sample convection.\r\nDC3 had two primary science objectives. The first was to investigate storm dynamics and physics, lightning and its production of nitrogen oxides, cloud hydrometeor effects on wet deposition of species, surface emission variability, and chemistry in anvil clouds. Observations related to this objective focused on the early stages of active convection. The second objective was to investigate changes in upper tropospheric chemistry and composition after active convection. Observations related to this objective focused on the 12-48 hours following convection. This objective also served to explore seasonal change of upper tropospheric chemistry.\r\nIn addition to using the NSF/NCAR Gulfstream-V (GV) aircraft, the NASA DC-8 was used during DC3 to provide in-situ measurements of the convective storm inflow and remotely-sensed measurements used for flight planning and column characterization. DC3 utilized ground-based radar networks spread across its observation area to measure the physical and kinematic characteristics of storms. Additional sampling strategies relied on lightning mapping arrays, radiosondes, and precipitation collection. Lastly, DC3 used data collected from various satellite instruments to achieve its goals, focusing on measurements from CALIOP onboard CALIPSO and CPL onboard CloudSat. In addition to providing an extensive set of data related to deep, mid-latitude continental convective clouds and analyzing their impacts on upper tropospheric composition and chemistry, DC3 improved models used to predict convective transport. DC3 improved knowledge of convection and chemistry, and provided information necessary to understanding the processes relating to ozone in the upper troposphere.",
-            "title": "DC3 In-Situ DLR Falcon Meteorological and Navigational Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDC3_MetNav_AircraftInSitu_DLR-Falcon_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDC3_MetNav_AircraftInSitu_DLR-Falcon_Data_1",
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
-                    "downloadURL": "https://www.eol.ucar.edu/field_projects/dc3",
-                    "description": "NCAR/UCAR EOL DC3 Project Page",
                     "@type": "dcat:Distribution",
+                    "description": "NCAR/UCAR EOL DC3 Project Page",
+                    "downloadURL": "https://www.eol.ucar.edu/field_projects/dc3",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/dc3-seac4rs/docs/SEAC4RS_Data_Management_Plan.pdf",
-                    "description": "DC3/SEAC4RS Data Management Plan",
                     "@type": "dcat:Distribution",
+                    "description": "DC3/SEAC4RS Data Management Plan",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/dc3-seac4rs/docs/SEAC4RS_Data_Management_Plan.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.eol.ucar.edu/projects/dc3/documents/SPO_DC3_revised.pdf",
-                    "description": "DC3 Scientific Program Overview",
                     "@type": "dcat:Distribution",
+                    "description": "DC3 Scientific Program Overview",
+                    "downloadURL": "https://archive.eol.ucar.edu/projects/dc3/documents/SPO_DC3_revised.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.eol.ucar.edu/projects/dc3/documents/EDO_DC3_revised.pdf",
-                    "description": "DC3 Experimental Design Overview ",
                     "@type": "dcat:Distribution",
+                    "description": "DC3 Experimental Design Overview ",
+                    "downloadURL": "https://archive.eol.ucar.edu/projects/dc3/documents/EDO_DC3_revised.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://journals.ametsoc.org/view/journals/bams/96/8/bams-d-13-00290.1.xml",
-                    "description": "DC3 Overview Paper",
                     "@type": "dcat:Distribution",
+                    "description": "DC3 Overview Paper",
+                    "downloadURL": "https://journals.ametsoc.org/view/journals/bams/96/8/bams-d-13-00290.1.xml",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www2.acom.ucar.edu/dc3",
-                    "description": "NCAR/UCAR ACOM DC3 Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "NCAR/UCAR ACOM DC3 Project Home Page",
+                    "downloadURL": "https://www2.acom.ucar.edu/dc3",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/78101/the-anatomy-of-a-thunderstorm/",
-                    "description": "NASA Earth Observatory \"The Anatomy of a Thunderstorm\" Article",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory \"The Anatomy of a Thunderstorm\" Article",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/78101/the-anatomy-of-a-thunderstorm/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/78497/when-wildfire-smoke-and-thunderstorms-collide/",
-                    "description": "NASA Earth Observatory \"When Wildfire, Smoke, and Thunderstorms Collide\" Article",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory \"When Wildfire, Smoke, and Thunderstorms Collide\" Article",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/78497/when-wildfire-smoke-and-thunderstorms-collide/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://dc3blog.wordpress.com/",
-                    "description": "DC3 Blog",
                     "@type": "dcat:Distribution",
+                    "description": "DC3 Blog",
+                    "downloadURL": "https://dc3blog.wordpress.com/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.eol.ucar.edu/project/DC3",
-                    "description": "NCAR/UCAR EOL Data Webpage",
                     "@type": "dcat:Distribution",
+                    "description": "NCAR/UCAR EOL Data Webpage",
+                    "downloadURL": "https://data.eol.ucar.edu/project/DC3",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/centers/dryden/status_reports/DC-8_status_05_21_12.html",
-                    "description": "NASA DC3 Status Report",
                     "@type": "dcat:Distribution",
+                    "description": "NASA DC3 Status Report",
+                    "downloadURL": "https://www.nasa.gov/centers/dryden/status_reports/DC-8_status_05_21_12.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2050607204-LARC_ASDC",
-                    "description": "Earthdata Search for DC3_MetNav_AircraftInSitu_DLR-Falcon_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for DC3_MetNav_AircraftInSitu_DLR-Falcon_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2050607204-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/DC3/MetNav_AircraftInSitu_DLR-Falcon_Data_1/",
-                    "description": "ASDC Direct Data Download for DC3_MetNav_AircraftInSitu_DLR-Falcon_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for DC3_MetNav_AircraftInSitu_DLR-Falcon_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/DC3/MetNav_AircraftInSitu_DLR-Falcon_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/DC3/MetNav_AircraftInSitu_DLR-Falcon_Data_1/",
-                    "description": "ASDC Direct Data Download for DC3_MetNav_AircraftInSitu_DLR-Falcon_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for DC3_MetNav_AircraftInSitu_DLR-Falcon_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/DC3/MetNav_AircraftInSitu_DLR-Falcon_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2050607204-LARC_ASDC",
+            "issued": "2021-03-12",
+            "keyword": [
+                "atmosphere",
+                "atmospheric temperature",
+                "atmospheric winds",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DC3_MetNav_AircraftInSitu_DLR-Falcon_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-04-29",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>25.0 -110.0 25.0 -90.0 45.0 -90.0 45.0 -110.0 25.0 -110.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2012-05-29T00:00:00Z/2012-06-14T23:59:59.999Z",
             "theme": [
                 "DC3",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "DC3 In-Situ DLR Falcon Meteorological and Navigational Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://lambda.gsfc.nasa.gov/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "cosmic microwave radiation",
-                "cosmology",
-                "cmb",
-                "lambda",
-                "heasarc"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "David T. Chuss",
                 "hasEmail": "mailto:david.t.chuss@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-0000066",
             "description": "The High Energy Astrophysics Science Archive Research Center (HEASARC) and the Legacy Archive for Microwave Background Data Analysis (LAMBDA) have merged into a single organization that will use the name HEASARC. The merged archive will continue to provide all of the services currently being offered by the two archives, while better serving users interested in studies requiring both high energy and microwave data. Users will notice few immediate changes, but we will gradually fully integrate all the services of the archives.",
-            "title": "LAMBDA - Legacy Archive for Microwave Background Data Analysis",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -755554,686 +755535,685 @@
                     "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "NASA-0000066",
+            "issued": "2018-06-25",
+            "keyword": [
+                "cosmic microwave radiation",
+                "cosmology",
+                "cmb",
+                "lambda",
+                "heasarc"
+            ],
+            "landingPage": "http://lambda.gsfc.nasa.gov/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "title": "LAMBDA - Legacy Archive for Microwave Background Data Analysis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-RADAR-V9.0",
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
+            "description": "This data set is a compilation of all groundbased asteroid radar detections. The collection is maintained and updated by Steven Ostro. It is updated annually.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-radar-v9.0_fehy-wipa",
+            "issued": "2018-06-26",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-RADAR-V9.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-radar-v9.0_fehy-wipa",
-            "description": "This data set is a compilation of all groundbased asteroid radar detections. The collection is maintained and updated by Steven Ostro. It is updated annually.",
-            "title": "ASTEROID RADAR V9.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ASTEROID RADAR V9.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1646",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Fayne, J.V., L.C. Smith, L.H. Pitcher, and T.M. Pavelsky. 2019. ABoVE: AirSWOT Ka-band Radar over Surface Waters of Alaska and Canada, 2017. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1646",
-            "issued": "2019-03-29",
-            "temporal": "2017-07-08T00:00:00Z/2017-08-17T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "spectral/engineering",
-                "earth science",
-                "land surface",
-                "radar",
-                "surface water",
-                "terrestrial hydrosphere",
-                "topography"
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
-            "identifier": "C2111827036-ORNL_CLOUD",
             "description": "AirSWOT is an airborne calibration and validation instrument for the upcoming Surface Water Topography Mission (SWOT) satellite. AirSWOT is capable of producing high resolution digital elevation models over land and water bodies. This dataset provides AirSWOT Ka-band (35.75 GHz) radar data products collected from an airborne platform over parts of Alaska and Canada during the period 2017-07-09 to 2017-08-17. Flights targeted specific surface water features, including rivers, lakes, ponds, and wetlands in the ABoVE domain. The radar data include six products: elevation (above the WGS84 ellipsoid), incidence angle, magnitude (backscatter), interferometric correlation (coherence), DHDPHI (incidence angle dependent height sensitivity), and error (estimated height random error, 1-sigma standard deviation). The flight lines were selected to span a full spectrum of permafrost conditions (permafrost-free to continuous permafrost, low to high ground ice content), ecosystems, climatic regions, topographic relief, and geological substrates across the ABoVE domain to investigate surface water responses to thawing permafrost and spatial and temporal variability in terrestrial water storage by measuring elevation and extent of surface waters. The data are provided in two forms: 1) the original output (outer-swath products only) at 3.6 m2 resolution in UTM coordinates from the AirSWOT processing group at the Jet Propulsion Laboratory (JPL), and 2) the ABoVE Projection at 3.6 m2 resolution, clipped to the ABoVE reference grid tiles using the C grid.",
-            "graphic-preview-description": "Example of AirSWOT radar products in ABoVE Projection at 3.6 m2 resolution, for a flight over the ABoVE C grid Ch065v034. Left: Shape for backscatter image. Middle: Magnitude image. Right: Elevation product image.",
-            "title": "ABoVE: AirSWOT Ka-band Radar over Surface Waters of Alaska and Canada, 2017",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/ABoVE_AirSWOT_Radar_Data_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1646",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1646",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/ABoVE_AirSWOT_Radar_Data/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/ABoVE_AirSWOT_Radar_Data/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ABoVE_AirSWOT_Radar_Data.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ABoVE_AirSWOT_Radar_Data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1646",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1646",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/ABoVE_AirSWOT_Radar_Data/comp/ABoVE_AirSWOT_Radar_Data.pdf",
-                    "description": "ABoVE: AirSWOT Ka-band Radar in the ABoVE Domain, 2017: ABoVE_AirSWOT_Radar_Data.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: AirSWOT Ka-band Radar in the ABoVE Domain, 2017: ABoVE_AirSWOT_Radar_Data.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/ABoVE_AirSWOT_Radar_Data/comp/ABoVE_AirSWOT_Radar_Data.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/vnd.google-earth.kmz",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/ABoVE_AirSWOT_Radar_Data/comp/AirSWOT_Radar_TileIndex.kmz",
-                    "description": "ABoVE: AirSWOT Ka-band Radar in the ABoVE Domain, 2017: AirSWOT_Radar_TileIndex.kmz",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: AirSWOT Ka-band Radar in the ABoVE Domain, 2017: AirSWOT_Radar_TileIndex.kmz",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/ABoVE_AirSWOT_Radar_Data/comp/AirSWOT_Radar_TileIndex.kmz",
+                    "mediaType": "application/vnd.google-earth.kmz",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ABoVE_AirSWOT_Radar_Data_Fig1.png",
-                    "description": "Example of AirSWOT radar products in ABoVE Projection at 3.6 m2 resolution, for a flight over the ABoVE C grid Ch065v034. Left: Shape for backscatter image. Middle: Magnitude image. Right: Elevation product image.",
                     "@type": "dcat:Distribution",
+                    "description": "Example of AirSWOT radar products in ABoVE Projection at 3.6 m2 resolution, for a flight over the ABoVE C grid Ch065v034. Left: Shape for backscatter image. Middle: Magnitude image. Right: Elevation product image.",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ABoVE_AirSWOT_Radar_Data_Fig1.png",
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
+            "graphic-preview-description": "Example of AirSWOT radar products in ABoVE Projection at 3.6 m2 resolution, for a flight over the ABoVE C grid Ch065v034. Left: Shape for backscatter image. Middle: Magnitude image. Right: Elevation product image.",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/ABoVE_AirSWOT_Radar_Data_Fig1.png",
+            "identifier": "C2111827036-ORNL_CLOUD",
+            "issued": "2019-03-29",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "land surface",
+                "radar",
+                "surface water",
+                "terrestrial hydrosphere",
+                "topography"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1646",
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
             "spatial": "-149.83 46.85 -98.63 70.49",
+            "temporal": "2017-07-08T00:00:00Z/2017-08-17T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE: AirSWOT Ka-band Radar over Surface Waters of Alaska and Canada, 2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/QPO9E5TPZ8OF",
             "citation": "Global Modeling and Assimilation Office (GMAO). 2015-06-30. M2TUNPTDT. Version 5.12.4. MERRA-2 tavgU_3d_tdt_Np: 3d,diurnal,Time-Averaged,Pressure-Level,Assimilation,Temperature Tendencies V5.12.4. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/QPO9E5TPZ8OF. https://disc.gsfc.nasa.gov/datacollection/M2TUNPTDT_5.12.4.html. Digital Science Data.",
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
-                "atmospheric temperature",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DANA OSTRENGA",
                 "hasEmail": "mailto:dana.ostrenga@nasa.gov"
             },
+            "creator": "Global Modeling and Assimilation Office (GMAO)",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1276812695-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "M2TUNPTDT (or  tavgU_3d_tdt_Np) is a 3-dimensional monthly diurnal means data collection in Modern-Era Retrospective analysis for Research and Applications version 2 (MERRA-2).  This collection consists of assimilations of air temperature tendencies on 42 pressure levels, such as total temperature analysis tendency, and tendency of air temperature due to  dynamics (or friction, moisture, radiation, and physics). The information on the pressure levels can be found in the section 4.2 of the MERRA-2 File Specification document.  This data collection is the monthly mean of data fields for each 3-hour and time-stamped at the central time starting from 01:30 UTC, e.g.: 01:30, 04:30, \u2026 , 22:30 UTC.\n\nMERRA-2 is the latest version of global atmospheric reanalysis for the satellite era produced by NASA Global Modeling and Assimilation Office (GMAO) using the Goddard Earth Observing System Model (GEOS) version 5.12.4.  The dataset covers the period of 1980-present with the latency of ~3 weeks after the end of a month. \n\nData Reprocessing:  Please check \u201cRecords of MERRA-2 Data Reprocessing and Service Changes\u201d linked from the \u201cDocumentation\u201d tab on this page.  Note that a reprocessed data filename is different from the original file.\n\nMERRA-2 Mailing List: Sign up to receive information on reprocessing of data, changing of tools and services, as well as data announcements from GMAO. Contact the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov) to be added to the list.\n\nQuestions: If you have a question, please read \"MERRA-2 File Specification Document\",  \u201cMERRA-2 Data Access \u2013 Quick Start Guide\u201d, and FAQs linked from the \u201dDocumentation\u201d tab on this page.  If that does not answer your question, you may email the question on data access to the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov), or the question on science to the MERRA-2 science team (merra-questions@lists.nasa.gov).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "M2TUNPTDT",
-            "creator": "Global Modeling and Assimilation Office (GMAO)",
-            "graphic-preview-description": "M2TUNPTDT variable",
-            "title": "MERRA-2 tavgU_3d_tdt_Np: 3d,diurnal,Time-Averaged,Pressure-Level,Assimilation,Temperature Tendencies 0.625 x 0.5 degree V5.12.4 (M2TUNPTDT) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2TUNPTDT_5.12.4.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FQPO9E5TPZ8OF",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FQPO9E5TPZ8OF",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2TUNPTDT_5.12.4.png",
-                    "description": "M2TUNPTDT variable",
                     "@type": "dcat:Distribution",
+                    "description": "M2TUNPTDT variable",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2TUNPTDT_5.12.4.png",
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
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2TUNPTDT_5.12.4.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2TUNPTDT_5.12.4.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2_DIURNAL/M2TUNPTDT.5.12.4/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2_DIURNAL/M2TUNPTDT.5.12.4/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2TUNPTDT",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2TUNPTDT",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/dods/M2TUNPTDT.info",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/dods/M2TUNPTDT.info",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/opendap/MERRA2_DIURNAL/M2TUNPTDT.5.12.4/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/opendap/MERRA2_DIURNAL/M2TUNPTDT.5.12.4/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_DIURNAL_aggregation//M2TUNPTDT.5.12.4/catalog.html",
-                    "description": "Time aggregated THREDDS Data Server (TDS) ",
                     "@type": "dcat:Distribution",
+                    "description": "Time aggregated THREDDS Data Server (TDS) ",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_DIURNAL_aggregation//M2TUNPTDT.5.12.4/catalog.html",
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
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2_DIURNAL/M2TUNPTDT.5.12.4/doc/MERRA2.README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2_DIURNAL/M2TUNPTDT.5.12.4/doc/MERRA2.README.pdf",
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
+            "graphic-preview-description": "M2TUNPTDT variable",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2TUNPTDT_5.12.4.png",
+            "identifier": "C1276812695-GES_DISC",
+            "issued": "2007-06-14",
+            "keyword": [
+                "earth science",
+                "atmospheric temperature",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/QPO9E5TPZ8OF",
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
+            "series-name": "M2TUNPTDT",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1980-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "MERRA-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MERRA-2 tavgU_3d_tdt_Np: 3d,diurnal,Time-Averaged,Pressure-Level,Assimilation,Temperature Tendencies 0.625 x 0.5 degree V5.12.4 (M2TUNPTDT) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-LECP-4-SUMM-SECTOR-15MIN-V1.1",
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
+            "description": "This data set consists of resampled data from the Low Energy Charged Particle (LECP) experiment on Voyager 2 while the spacecraft was in the vicinity of Jupiter. This instrument measures the intensities of in-situ charged particles (>26 keV electrons and >30 keV ions) with various levels of discrimination based on energy, mass species, and angular arrival direction. A subset of almost 100 LECP channels are included with this data set. The LECP data are globally calibrated to the extent possible (see below) and they are time averaged to about 15 minute time intervals with the exact beginning and ending times for those intervals matching the LECP instrumental cycle periods (the angular scanning periods). The data is in the form of 'rate' data which has not been converted  to the usual physical units. Data records for the version 1.1 data set provide all data for a given channel and time period (8 sectors, plus the average for all sectors) in a single record.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-lecp-4-summ-sector-15min-v1.1_femz-czip",
+            "issued": "2018-06-26",
+            "keyword": [
+                "jupiter",
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-LECP-4-SUMM-SECTOR-15MIN-V1.1",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-lecp-4-summ-sector-15min-v1.1_femz-czip",
-            "description": "This data set consists of resampled data from the Low Energy Charged Particle (LECP) experiment on Voyager 2 while the spacecraft was in the vicinity of Jupiter. This instrument measures the intensities of in-situ charged particles (>26 keV electrons and >30 keV ions) with various levels of discrimination based on energy, mass species, and angular arrival direction. A subset of almost 100 LECP channels are included with this data set. The LECP data are globally calibrated to the extent possible (see below) and they are time averaged to about 15 minute time intervals with the exact beginning and ending times for those intervals matching the LECP instrumental cycle periods (the angular scanning periods). The data is in the form of 'rate' data which has not been converted  to the usual physical units. Data records for the version 1.1 data set provide all data for a given channel and time period (8 sectors, plus the average for all sectors) in a single record.",
-            "title": "VG2 JUP LECP CALIBRATED RESAMPLED SECTORED 15MIN V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG2 JUP LECP CALIBRATED RESAMPLED SECTORED 15MIN V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-C-RSS-1-9P-ENCOUNTER-V1.0",
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
+            "description": "This data set contains raw radio science data from the Deep Impact flyby spacecraft, collected during the encounter with comet 9P/Tempel 1.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-c-rss-1-9p-encounter-v1.0_ferk-8mz7",
+            "issued": "2018-06-26",
+            "keyword": [
+                "9p/tempel 1 (1867 g1)",
+                "deep impact"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-C-RSS-1-9P-ENCOUNTER-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-c-rss-1-9p-encounter-v1.0_ferk-8mz7",
-            "description": "This data set contains raw radio science data from the Deep Impact flyby spacecraft, collected during the encounter with comet 9P/Tempel 1.",
-            "title": "DEEP IMPACT 9P/TEMPEL 1 ENCOUNTER - RADIO SCIENCE DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "DEEP IMPACT 9P/TEMPEL 1 ENCOUNTER - RADIO SCIENCE DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-PPMAG-3-RDR-CROMMELIN-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-ppmag-3-rdr-crommelin-v1.0_fete-ajw4",
+            "issued": "2021-05-21",
+            "keyword": [
+                "halley",
+                "international halley watch"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-PPMAG-3-RDR-CROMMELIN-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-ppmag-3-rdr-crommelin-v1.0_fete-ajw4",
-            "description": "In preparation for the concerted international study of Comet Halley, the IHW conducted a trial run with observations of Comet Crommelin, largely during February and March of 1984.",
-            "title": "IHW COMET PPMAG CALIB REDUCED DATA RECORD CROMMELIN V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "IHW COMET PPMAG CALIB REDUCED DATA RECORD CROMMELIN V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1118-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-21T10:20:25.000 to 2015-10-21T17:22:10.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1118-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1118-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1118-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-21T10:20:25.000 to 2015-10-21T17:22:10.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1118 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1118 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/HS3/AVAPS/DROPSONDE/DATA202",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hock, Terry , Kate  Young and Holger  Voemel.2017. HURRICANE AND SEVERE STORM SENTINEL (HS3) GLOBAL HAWK ADVANCED VERTICAL ATMOSPHERIC PROFILING SYSTEM (AVAPS) DROPSONDE SYSTEM V2 [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/HS3/AVAPS/DROPSONDE/DATA202",
-            "issued": "2017-05-17",
-            "temporal": "2012-09-07T02:20:55Z/2014-09-30T16:39:08Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-25",
-            "keyword": [
-                "weather events",
-                "atmospheric temperature",
-                "atmospheric pressure",
-                "atmosphere",
-                "atmospheric winds",
-                "atmospheric water vapor",
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
-            "identifier": "C1979860836-GHRC_DAAC",
             "description": "The Hurricane and Severe Storm Sentinel (HS3) Global Hawk Advanced Vertical Atmospheric Profiling System (AVAPS) Dropsonde System dataset was collected by the Advanced Vertical Atmospheric Profiling System (AVAPS), built by the National Center for Atmospheric Research (NCAR), which served as the dropsonde system for the Global Hawk aircraft during the HS3 campaign. Goals for HS3 included: assessing the relative roles of large-scale environment and storm-scale internal processes; and addressing the controversial role of the Saharan Air Layer (SAL) in tropical storm formation and intensification as well as the role of deep convection in the inner-core region of storms. AVAPS dropsondes provide in-situ, high-vertical resolution measurements of atmospheric variables including pressure, temperature, humidity, geographic location, and winds, providing a vertical profile of the atmospheric conditions. The raw instrument measurement precision is as follows: pressure +-1.0 hPa, temperature +-0.2 degrees C, wind +-1 ms-1, and humidity +-7 percent. The measured information was transmitted via Iridium or Ku-Band satellite to the ground station where the Global Telecommunications System (GTS) performed additional processing for research and operational purposes.",
-            "title": "HURRICANE AND SEVERE STORM SENTINEL (HS3) GLOBAL HAWK ADVANCED VERTICAL ATMOSPHERIC PROFILING SYSTEM (AVAPS) DROPSONDE SYSTEM V2",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FHS3%2FAVAPS%2FDROPSONDE%2FDATA202",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FHS3%2FAVAPS%2FDROPSONDE%2FDATA202",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=hs3avaps2",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=hs3avaps2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/missions/hs3/",
-                    "description": "NASA Hurricane and Severe Storm Sentinel mission",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Hurricane and Severe Storm Sentinel mission",
+                    "downloadURL": "https://espo.nasa.gov/missions/hs3/",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.eol.ucar.edu/observing_facilities/avaps-dropsonde-system",
-                    "description": "NCAR UCAR Earth Observing Laboratory (EOL) Avaps Dropsonde System",
                     "@type": "dcat:Distribution",
+                    "description": "NCAR UCAR Earth Observing Laboratory (EOL) Avaps Dropsonde System",
+                    "downloadURL": "https://www.eol.ucar.edu/observing_facilities/avaps-dropsonde-system",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/hs3/AVAPS/doc/HS3_AVAPS_Guide_V2.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/hs3/AVAPS/doc/HS3_AVAPS_Guide_V2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/hs3/AVAPS/doc/readme.V5.HS3-2013.GHdropsonde.pdf",
-                    "description": "Hurricane and Severe Storm Sentinel (HS3) 2013 Global Hawk Dropsonde Data Analysis Summary",
                     "@type": "dcat:Distribution",
+                    "description": "Hurricane and Severe Storm Sentinel (HS3) 2013 Global Hawk Dropsonde Data Analysis Summary",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/hs3/AVAPS/doc/readme.V5.HS3-2013.GHdropsonde.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/hs3/AVAPS/doc/readme.V3.HS3-2014.GHdropsonde.pdf",
-                    "description": "Hurricane and Severe Storm Sentinel (HS3) 2014 Global Hawk Dropsonde Data Analysis Summary",
                     "@type": "dcat:Distribution",
+                    "description": "Hurricane and Severe Storm Sentinel (HS3) 2014 Global Hawk Dropsonde Data Analysis Summary",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/hs3/AVAPS/doc/readme.V3.HS3-2014.GHdropsonde.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/hs3/AVAPS/doc/readme.V5.HS3-2012.GHdropsonde.pdf",
-                    "description": "Hurricane and Severe Storm Sentinel (HS3) 2012 Global Hawk Dropsonde Project Analysis Summary",
                     "@type": "dcat:Distribution",
+                    "description": "Hurricane and Severe Storm Sentinel (HS3) 2012 Global Hawk Dropsonde Project Analysis Summary",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/hs3/AVAPS/doc/readme.V5.HS3-2012.GHdropsonde.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/opendap/fieldCampaigns/hs3/AVAPS/data/",
-                    "description": "OPeNDAP server dataset access",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP server dataset access",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/opendap/fieldCampaigns/hs3/AVAPS/data/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/projects/HS3",
-                    "description": "The home page for the project or program which sponsored the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The home page for the project or program which sponsored the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/projects/HS3",
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
+            "identifier": "C1979860836-GHRC_DAAC",
+            "issued": "2017-05-17",
+            "keyword": [
+                "weather events",
+                "atmospheric temperature",
+                "atmospheric pressure",
+                "atmosphere",
+                "atmospheric winds",
+                "atmospheric water vapor",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/HS3/AVAPS/DROPSONDE/DATA202",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-05-25",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/MSFC/GHRC"
+            },
             "spatial": "-97.5988 7.9001 -19.0779 47.1646",
+            "temporal": "2012-09-07T02:20:55Z/2014-09-30T16:39:08Z",
             "theme": [
                 "HS3",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "HURRICANE AND SEVERE STORM SENTINEL (HS3) GLOBAL HAWK ADVANCED VERTICAL ATMOSPHERIC PROFILING SYSTEM (AVAPS) DROPSONDE SYSTEM V2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-EXT3-67PCHURYUMOV-M32-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 3 mission phase, covering the period from 2016-07-26T23:25:00.000 to 2016-08-09T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-ext3-67pchuryumov-m32-v3.0_ff3b-6p2j",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "international rosetta mission",
                 "vega",
                 "bias"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-EXT3-67PCHURYUMOV-M32-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-ext3-67pchuryumov-m32-v3.0_ff3b-6p2j",
-            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 3 mission phase, covering the period from 2016-07-26T23:25:00.000 to 2016-08-09T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 2 EXT3-MTP032 EDR V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 2 EXT3-MTP032 EDR V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-RSSL-3-EDR-HALLEY-V1.0",
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
+            "description": "NASA's International Halley Watch has created a Comet Halley Archive. The collection of data spans the full wavelength range as submitted by scientists to the IHW. The observations belong to one of the following Disciplines: Amateur, Astrometry, Infrared Studies, Large-Scale Phenomena, Meteor Studies, Near-Nucleus Studies, Photometry and Polarimetry, Radio Studies, and Spectroscopy and Spectrophotometry. The data collected by these nine disciplines were augmented by Spacecraft measurements. The data were submitted to IHW, but the evaluation and selection for the Archive has been the primary responsibility of the Discipline Specialist Teams for each network in cooperation with the Lead Center. The data from the Radio Studies Spectral Line Subnetwork contains 107 spectra of Halley, spanning dates 1985 November 09 through 1986 May 11.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-rssl-3-edr-halley-v1.0_ff4x-bmys",
+            "issued": "2018-06-26",
+            "keyword": [
+                "halley",
+                "international halley watch"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-RSSL-3-EDR-HALLEY-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-rssl-3-edr-halley-v1.0_ff4x-bmys",
-            "description": "NASA's International Halley Watch has created a Comet Halley Archive. The collection of data spans the full wavelength range as submitted by scientists to the IHW. The observations belong to one of the following Disciplines: Amateur, Astrometry, Infrared Studies, Large-Scale Phenomena, Meteor Studies, Near-Nucleus Studies, Photometry and Polarimetry, Radio Studies, and Spectroscopy and Spectrophotometry. The data collected by these nine disciplines were augmented by Spacecraft measurements. The data were submitted to IHW, but the evaluation and selection for the Archive has been the primary responsibility of the Discipline Specialist Teams for each network in cooperation with the Lead Center. The data from the Radio Studies Spectral Line Subnetwork contains 107 spectra of Halley, spanning dates 1985 November 09 through 1986 May 11.",
-            "title": "IHW COMET HALLEY RADIO SPECTRAL DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "IHW COMET HALLEY RADIO SPECTRAL DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/ff5v-kuh6",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2022-07-14",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-15",
-            "keyword": [
-                "ivhm",
-                "fan degradation",
-                "prognostics",
-                "degradation",
-                "phm"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Chris Teubert",
                 "hasEmail": "mailto:Christopher.a.teubert@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "PCoE"
-            },
-            "identifier": "https://data.nasa.gov/api/views/ff5v-kuh6",
             "description": "Data sets consists of multiple multivariate time series. Each data set is further divided into training and test subsets. Each time series is from a different engine i.e., the data can be considered to be from a fleet of engines of the same type. Each engine starts with different degrees of initial wear and manufacturing variation which is unknown to the user. This wear and variation is considered normal, i.e., it is not considered a fault condition. There are three operational settings that have a substantial effect on engine performance. These settings are also included in the data. The data is contaminated with sensor noise.\n\nThe engine is operating normally at the start of each time series, and develops a fault at some point during the series. In the training set, the fault grows in magnitude until system failure. In the test set, the time series ends some time prior to system failure. The objective of the competition is to predict the number of remaining operational cycles before failure in the test set, i.e., the number of operational cycles after the last cycle that the engine will continue to operate. Also provided a vector of true Remaining Useful Life (RUL) values for the test data.\n\nThe data are provided as a zip-compressed text file with 26 columns of numbers, separated by spaces. Each row is a snapshot of data taken during a single operational cycle, each column is a different variable. The columns correspond to:\n1)            unit number\n2)            time, in cycles\n3)            operational setting 1\n4)            operational setting 2\n5)            operational setting 3\n6)            sensor measurement  1\n7)            sensor measurement  2\n...\n26)          sensor measurement  26\n \nData Set: FD001\nTrain trjectories: 100\nTest trajectories: 100\nConditions: ONE (Sea Level)\nFault Modes: ONE (HPC Degradation)\n \nData Set: FD002\nTrain trjectories: 260\nTest trajectories: 259\nConditions: SIX\nFault Modes: ONE (HPC Degradation)\n\nData Set: FD003\nTrain trjectories: 100\nTest trajectories: 100\nConditions: ONE (Sea Level)\nFault Modes: TWO (HPC Degradation, Fan Degradation)\n\nData Set: FD004\nTrain trjectories: 248\nTest trajectories: 249\nConditions: SIX\nFault Modes: TWO (HPC Degradation, Fan Degradation)\n\nReference: A. Saxena, K. Goebel, D. Simon, and N. Eklund, \u2018Damage Propagation Modeling for Aircraft Engine Run-to-Failure Simulation\u2019, in the Proceedings of the 1st International Conference on Prognostics and Health Management (PHM08), Denver CO, Oct 2008.",
-            "title": "CMAPSS Jet Engine Simulated Data",
-            "programCode": [
-                "026:021"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -756241,285 +756221,307 @@
                     "mediaType": "application/zip"
                 }
             ],
+            "identifier": "https://data.nasa.gov/api/views/ff5v-kuh6",
+            "issued": "2022-07-14",
+            "keyword": [
+                "ivhm",
+                "fan degradation",
+                "prognostics",
+                "degradation",
+                "phm"
+            ],
+            "landingPage": "https://data.nasa.gov/d/ff5v-kuh6",
+            "modified": "2024-05-15",
+            "programCode": [
+                "026:021"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "PCoE"
+            },
             "theme": [
                 "Aerospace"
-            ]
+            ],
+            "title": "CMAPSS Jet Engine Simulated Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-SWAP-2-PLUTOCRUISE-V1.0",
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
+            "description": "This data set contains Raw data taken by the New Horizons Solar Wind Around Pluto instrument during the pluto cruise mission phase.  This is VERSION 1.0 of this data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-swap-2-plutocruise-v1.0_ff6u-m8yw",
+            "issued": "2018-06-26",
+            "keyword": [
+                "new horizons",
+                "solar wind"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-SWAP-2-PLUTOCRUISE-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-swap-2-plutocruise-v1.0_ff6u-m8yw",
-            "description": "This data set contains Raw data taken by the New Horizons Solar Wind Around Pluto instrument during the pluto cruise mission phase.  This is VERSION 1.0 of this data set.",
-            "title": "NEW HORIZONS\n      SWAP PLUTO CRUISE\n      RAW V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS\n      SWAP PLUTO CRUISE\n      RAW V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/9SQ1B3ZXP2C5",
             "citation": "Beaudoing, H. and M. Rodell, NASA/GSFC/HSL. 2019-11-19. GLDAS_NOAH025_M. Version 2.0. GLDAS Noah Land Surface Model L4 monthly 0.25 x 0.25 degree V2.0. Greenbelt, Maryland, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/9SQ1B3ZXP2C5. https://disc.gsfc.nasa.gov/datacollection/GLDAS_NOAH025_M_2.0.html. Digital Science Data.",
-            "issued": "2019-11-19",
-            "temporal": "1948-01-01T00:00:00Z/2014-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-11-19",
-            "references": [
-                "https://doi.org/10.1175/BAMS-85-3-381"
-            ],
-            "keyword": [
-                "land surface",
-                "atmosphere",
-                "atmospheric winds",
-                "atmospheric radiation",
-                "atmospheric pressure",
-                "terrestrial hydrosphere",
-                "atmospheric temperature",
-                "earth science",
-                "atmospheric water vapor",
-                "precipitation",
-                "snow/ice",
-                "surface water",
-                "soils",
-                "surface thermal properties"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "HUALAN RUI",
                 "hasEmail": "mailto:Hualan.Rui@nasa.gov"
             },
+            "creator": "Beaudoing, H. and M. Rodell, NASA/GSFC/HSL",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1233767569-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "NASA Global Land Data Assimilation System Version 2 (GLDAS-2) has three components: GLDAS-2.0, GLDAS-2.1, and GLDAS-2.2. GLDAS-2.0 is forced entirely with the Princeton meteorological forcing input data and provides a temporally consistent series from 1948 through 2014. GLDAS-2.1 is forced with a combination of model and observation data from 2000 to present. GLDAS-2.2 product suites use data assimilation (DA), whereas the GLDAS-2.0 and GLDAS-2.1 products are \"open-loop\" (i.e., no data assimilation). The choice of forcing data, as well as DA observation source, variable, and scheme, vary for different GLDAS-2.2 products.\n\nThis data product, GLDAS-2.0 0.25 degree monthly, was reprocessed and replaced its previous data product on November 19, 2019.  The data product was generated through temporal averaging of the reprocessed 3-hourly data, contains a series of land surface parameters simulated from the Noah Model 3.6, and currently covers from January 1948 to December 2014, but will be extended as the data becomes available.  The GLDAS-2.0 data are archived and distributed in netCDF format.\n\nThe GLDAS-2.0 model simulations were initialized on simulation date January 1, 1948, using soil moisture and other state fields from the LSM climatology for that day of the year. The simulations were forced by the global meteorological forcing data set from Princeton University (Sheffield et al., 2006). Each simulation uses the common GLDAS data sets for land water mask (MOD44W: Carroll et al., 2009) and elevation (GTOPO30) along with the model default land cover and soils datasets. Noah model uses the Modified IGBP MODIS 20-category vegetation classification and the soil texture based on the Hybrid STATSGO/FAO) datasets. The MODIS based land surface parameters are used in the current GLDAS-2.0 and GLDAS-2.1 products while the AVHRR base parameters were used in GLDAS-1 and previous GLDAS-2 products (prior to October 2012).  The land mask was modified to accommodate the river routing scheme included in the simulations in the fall 2019 update.  \n\nIn October 2020, all 3-hourly and monthly GLDAS-2 data were post-processed with the MOD44W MODIS land mask.  Previously, some grid boxes over inland water were considered as over land and, thus, had non-missing values.  The post-processing corrected this issue and masked out all model output data over inland water; the post-processing did not affect the meteorological forcing variables. More information can be found in the GLDAS-2 README.  The MOD44W MODIS land mask is available on the GLDAS Project site.\n\nIf you had downloaded the GLDAS data prior to November 2020, please download the data again to receive the post-processed data.",
-            "release-place": "Greenbelt, Maryland, USA",
-            "series-name": "GLDAS_NOAH025_M",
-            "creator": "Beaudoing, H. and M. Rodell, NASA/GSFC/HSL",
-            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
-            "title": "GLDAS Noah Land Surface Model L4 monthly 0.25 x 0.25 degree V2.0 (GLDAS_NOAH025_M) at GES DISC",
-            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=GLDAS_NOAH025_M_2_0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F9SQ1B3ZXP2C5",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F9SQ1B3ZXP2C5",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GLDAS_NOAH025_M_2.0.png",
-                    "description": "GLDAS-2.0 Noah monthly 0.25 Degree 0 - 10 cm soil moisture content [kg m-2] for Jan. 1948.",
                     "@type": "dcat:Distribution",
+                    "description": "GLDAS-2.0 Noah monthly 0.25 Degree 0 - 10 cm soil moisture content [kg m-2] for Jan. 1948.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GLDAS_NOAH025_M_2.0.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GLDAS_NOAH025_M_2.0.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GLDAS_NOAH025_M_2.0.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/GLDAS/GLDAS_NOAH025_M.2.0/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/GLDAS/GLDAS_NOAH025_M.2.0/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GLDAS_NOAH025_M_2.0",
-                    "description": "Use the Earthdata Search Client (EDSC) to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client (EDSC) to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GLDAS_NOAH025_M_2.0",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=GLDAS_NOAH025_M_2_0",
-                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
                     "@type": "dcat:Distribution",
+                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=GLDAS_NOAH025_M_2_0",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through GIOVANNI"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/opendap/hyrax/GLDAS/GLDAS_NOAH025_M.2.0/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/opendap/hyrax/GLDAS/GLDAS_NOAH025_M.2.0/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/dods/GLDAS_NOAH025_M.2.0/",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/dods/GLDAS_NOAH025_M.2.0/",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/GLDAS/GLDAS_NOAH025_M.2.0/doc/README_GLDAS2.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/GLDAS/GLDAS_NOAH025_M.2.0/doc/README_GLDAS2.pdf",
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
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/thredds/catalog/GLDAS_aggregation/GLDAS_NOAH025_M.2.0/catalog.html",
-                    "description": "Time aggregated THREDDS Data Server (TDS)",
                     "@type": "dcat:Distribution",
+                    "description": "Time aggregated THREDDS Data Server (TDS)",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/thredds/catalog/GLDAS_aggregation/GLDAS_NOAH025_M.2.0/catalog.html",
+                    "mediaType": "text/html",
                     "title": "Use THREDDS DATA to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=GLDAS_NOAH025_M_2_0",
+            "identifier": "C1233767569-GES_DISC",
+            "issued": "2019-11-19",
+            "keyword": [
+                "land surface",
+                "atmosphere",
+                "atmospheric winds",
+                "atmospheric radiation",
+                "atmospheric pressure",
+                "terrestrial hydrosphere",
+                "atmospheric temperature",
+                "earth science",
+                "atmospheric water vapor",
+                "precipitation",
+                "snow/ice",
+                "surface water",
+                "soils",
+                "surface thermal properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/9SQ1B3ZXP2C5",
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
+            "series-name": "GLDAS_NOAH025_M",
             "spatial": "-180.0 -60.0 180.0 90.0",
+            "temporal": "1948-01-01T00:00:00Z/2014-12-31T23:59:59.999Z",
             "theme": [
                 "GLDAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GLDAS Noah Land Surface Model L4 monthly 0.25 x 0.25 degree V2.0 (GLDAS_NOAH025_M) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DI%2FEAR-C-I0046-2-IRTF-NIRSPEC-TMPL1-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Near-IR spectra of Comet 9P/Tempel 1 were obtained with SpeX at the NASA IRTF during the period from June 24 through July 08, 2005 UT. These observations were taken as part of a campaign designed to support the science objectives of the Deep Impact spacecraft around the time of its encounter with Tempel 1 on July 4, 2005.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.di-ear-c-i0046-2-irtf-nirspec-tmpl1-v1.0_ff7f-pa55",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "support archives",
                 "9p/tempel 1 (1867 g1)",
                 "calibration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DI%2FEAR-C-I0046-2-IRTF-NIRSPEC-TMPL1-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.di-ear-c-i0046-2-irtf-nirspec-tmpl1-v1.0_ff7f-pa55",
-            "description": "Near-IR spectra of Comet 9P/Tempel 1 were obtained with SpeX at the NASA IRTF during the period from June 24 through July 08, 2005 UT. These observations were taken as part of a campaign designed to support the science objectives of the Deep Impact spacecraft around the time of its encounter with Tempel 1 on July 4, 2005.",
-            "title": "IRTF NEAR-IR SPECTROSCOPY OF COMET 9P-TEMPEL 1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "IRTF NEAR-IR SPECTROSCOPY OF COMET 9P-TEMPEL 1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DI%2FEAR-C-I0046-2-IRTF-NIRIMG-TMPL1-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Near-IR images of Comet 9P/Tempel 1 were obtained at the NASA IRTF during the period from June 24 through July 17, 2005 UT. These observations were taken as part of a campaign designed to support the science objectives of the Deep Impact spacecraft around the time of its encounter with Tempel 1. This data set contains all raw images, including those required for reduction and photometric calibration of the comet observations.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.di-ear-c-i0046-2-irtf-nirimg-tmpl1-v1.0_ff7i-rfnf",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "9p/tempel 1 (1867 g1)",
                 "calibration",
                 "support archives"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DI%2FEAR-C-I0046-2-IRTF-NIRIMG-TMPL1-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.di-ear-c-i0046-2-irtf-nirimg-tmpl1-v1.0_ff7i-rfnf",
-            "description": "Near-IR images of Comet 9P/Tempel 1 were obtained at the NASA IRTF during the period from June 24 through July 17, 2005 UT. These observations were taken as part of a campaign designed to support the science objectives of the Deep Impact spacecraft around the time of its encounter with Tempel 1. This data set contains all raw images, including those required for reduction and photometric calibration of the comet observations.",
-            "title": "IRTF NEAR-IR IMAGING OF COMET 9P-TEMPEL 1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "IRTF NEAR-IR IMAGING OF COMET 9P-TEMPEL 1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-UVIS-2-SPEC-V1.3",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Spectroscopy of Jupiter, Saturnian rings, atmospheres and satellites for determining chemical abundance, compositional albedo, aerosol profiling, ring reflected spectra and diffraction patterns.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-uvis-2-spec-v1.3_ffbk-78dp",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "phoebe",
                 "iapetus",
@@ -756555,35 +756557,47 @@
                 "pandora",
                 "prometheus"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-UVIS-2-SPEC-V1.3",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-uvis-2-spec-v1.3_ffbk-78dp",
-            "description": "Spectroscopy of Jupiter, Saturnian rings, atmospheres and satellites for determining chemical abundance, compositional albedo, aerosol profiling, ring reflected spectra and diffraction patterns.",
-            "title": "CASSINI ORBITER SATURN UVIS EDITED SPECTRA V1.3",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI ORBITER SATURN UVIS EDITED SPECTRA V1.3"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/ffbp-yzmd",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "The MARS500 project the longest ground-based space simulation ever provided us with a unique opportunity to trace the crew microbiota over 520 days of isolated confinement such as that faced by astronauts in real long-term interplanetary space flights and after returning to regular life for a total of 2 years.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-191",
+                    "mediaType": "text/html",
+                    "title": "Temporal dynamics of the gut microbiota in people sharing a confined environment a 520-day ground-based space simulation MARS500"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-191_ffbp-yzmd",
             "issued": "2018-09-05",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "nucleic acid sequencing",
                 "nucleic acid extraction",
@@ -756592,156 +756606,120 @@
                 "library construction",
                 "sampling time"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/ffbp-yzmd",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-191_ffbp-yzmd",
-            "description": "The MARS500 project the longest ground-based space simulation ever provided us with a unique opportunity to trace the crew microbiota over 520 days of isolated confinement such as that faced by astronauts in real long-term interplanetary space flights and after returning to regular life for a total of 2 years.",
-            "title": "Temporal dynamics of the gut microbiota in people sharing a confined environment a 520-day ground-based space simulation MARS500",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-191",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Temporal dynamics of the gut microbiota in people sharing a confined environment a 520-day ground-based space simulation MARS500"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Temporal dynamics of the gut microbiota in people sharing a confined environment a 520-day ground-based space simulation MARS500"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/8YTYSV6JGBK2",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMAP L2 Radar/Radiometer Half-Orbit 9 km EASE-Grid Soil Moisture V003. Version 003. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/8YTYSV6JGBK2.",
-            "issued": "2015-04-13",
-            "temporal": "2015-04-13T00:00:00Z/2015-07-07T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-07-07",
-            "keyword": [
-                "spectral/engineering",
-                "land surface",
-                "microwave",
-                "earth science",
-                "radar",
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
-            "identifier": "C2830464428-NSIDC_CPRD",
             "description": "This Level-2 (L2) soil moisture product provides estimates of global land surface conditions retrieved by both the Soil Moisture Active Passive (SMAP) radar and radiometer during 6:00 a.m. descending half-orbit passes. SMAP L-band backscatter and brightness temperatures are used to derive soil moisture data, which are then resampled to an Earth-fixed, global, cylindrical 9 km Equal-Area Scalable Earth Grid, Version 2.0 (EASE-Grid 2.0).",
-            "title": "SMAP L2 Radar/Radiometer Half-Orbit 9 km EASE-Grid Soil Moisture V003",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F8YTYSV6JGBK2",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F8YTYSV6JGBK2",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SPL2SMAP+V003",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SPL2SMAP+V003",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2830464428-NSIDC_CPRD",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2830464428-NSIDC_CPRD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/8YTYSV6JGBK2",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/8YTYSV6JGBK2",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/8YTYSV6JGBK2",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/8YTYSV6JGBK2",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2830464428-NSIDC_CPRD",
+            "issued": "2015-04-13",
+            "keyword": [
+                "spectral/engineering",
+                "land surface",
+                "microwave",
+                "earth science",
+                "radar",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.5067/8YTYSV6JGBK2",
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
             "spatial": "-180.0 -85.044 180.0 85.044",
+            "temporal": "2015-04-13T00:00:00Z/2015-07-07T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMAP L2 Radar/Radiometer Half-Orbit 9 km EASE-Grid Soil Moisture V003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/C663V8751REA",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Martin Snow. 2020-12-29. SOR3SOLD_HIGH. Version 018. SORCE SOLSTICE FUV and MUV Level 3 Solar Spectral Irradiance 0.1nm Res 24-Hour Means V018. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/C663V8751REA. https://disc.gsfc.nasa.gov/datacollection/SOR3SOLD_HIGH_018.html. Digital Science Data.",
-            "issued": "2020-12-21",
-            "temporal": "2003-03-05T00:00:00Z/2020-02-25T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-21",
-            "keyword": [
-                "earth science",
-                "solar activity",
-                "sun-earth interactions"
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
-            "identifier": "C1994107713-GES_DISC",
-            "description": "SORCE SOLSTICE FUV and MUV Level 3 Solar Spectral Irradiance 0.1nm Res 24-Hour Means data product (SOR3SOLD_HIGH) is constructed using measurements from the SOLSTICE FUV and MUV instrument, which is combined into merged daily solar spectra over the spectral range from 115 to 310 nm at a high spectral resolution of 0.1 nm. Irradiances are reported at a mean solar distance of 1 AU and zero relative line-of-sight velocity with respect to the Sun. The SOLSTICE absolute uncertainty better than 5%.\n\nThe SOR3SOLD_HIGH data are stored in netCDF files containing a full year of data. Each file contains variables with the date, Julian day, wavelength, irradiance value, irradiance uncertainty, and irradiance repeatability.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "SOR3SOLD_HIGH",
             "creator": "Martin Snow",
-            "title": "SORCE SOLSTICE FUV and MUV Level 3 Solar Spectral Irradiance 0.1nm Res 24-Hour Means V018 (SOR3SOLD_HIGH) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SORCE_Logo.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "SORCE SOLSTICE FUV and MUV Level 3 Solar Spectral Irradiance 0.1nm Res 24-Hour Means data product (SOR3SOLD_HIGH) is constructed using measurements from the SOLSTICE FUV and MUV instrument, which is combined into merged daily solar spectra over the spectral range from 115 to 310 nm at a high spectral resolution of 0.1 nm. Irradiances are reported at a mean solar distance of 1 AU and zero relative line-of-sight velocity with respect to the Sun. The SOLSTICE absolute uncertainty better than 5%.\n\nThe SOR3SOLD_HIGH data are stored in netCDF files containing a full year of data. Each file contains variables with the date, Julian day, wavelength, irradiance value, irradiance uncertainty, and irradiance repeatability.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FC663V8751REA",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FC663V8751REA",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -756751,253 +756729,289 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/SORCE_Level3/SOR3SOLD_HIGH.018/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/SORCE_Level3/SOR3SOLD_HIGH.018/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SOR3SOLD_HIGH_018",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SOR3SOLD_HIGH_018",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://lasp.colorado.edu/data/sorce/file_readers/read_netcdf.pro",
-                    "description": "SORCE netCDF IDL-based file reader.",
                     "@type": "dcat:Distribution",
+                    "description": "SORCE netCDF IDL-based file reader.",
+                    "downloadURL": "http://lasp.colorado.edu/data/sorce/file_readers/read_netcdf.pro",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SORCE_Logo.png",
+            "identifier": "C1994107713-GES_DISC",
+            "issued": "2020-12-21",
+            "keyword": [
+                "earth science",
+                "solar activity",
+                "sun-earth interactions"
+            ],
+            "landingPage": "https://doi.org/10.5067/C663V8751REA",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-12-21",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "SOR3SOLD_HIGH",
+            "temporal": "2003-03-05T00:00:00Z/2020-02-25T23:59:59.999Z",
             "theme": [
                 "SORCE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SORCE SOLSTICE FUV and MUV Level 3 Solar Spectral Irradiance 0.1nm Res 24-Hour Means V018 (SOR3SOLD_HIGH) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-SDC-3-PLUTOCRUISE-V2.0",
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
+            "description": "This data set contains Calibrated data taken by the New Horizons         Student Dust Counter                                                   instrument during the                                                    pluto cruise                                                           mission phase.  This is VERSION 2.0 of this data set.                    SDC collected science data intermittently during the hibernation         years following the Jupiter encounter, designated as the PLUTOCRUISE     phase.  There were also Annual Checkouts (ACOs), STIM calibrations,      Noise calibrations, and an anomaly in November, 2007.                    SDC's main science data collection periods were during hibernation.      During ACOs, science data are taken intermittently but the user must     be careful in analyzing these data since there is usually more           activity on the spacecraft during hibernation.  STIM and Noise refer     to scheduled calibrations and are done with a regular cadence of one     per year after the Jupiter encounter; they occurred sporadically in      the early years of the mission.                                          Note that some SDC data files have the same stop and start time and      a zero exposure time.  The reason for this is that the start and         stop time for SDC data files are the event times for the first and       last events in the files, so for files that contain a single event,      these two values are the same.                                           The changes in Version 2.0 were re-running of the ancillary data         in the data product, updated geometry from newer SPICE kernels,          minor editing of the documentation, catalogs, etc., and resolution       of liens from the December, 2014 review, plus those from the May,        2016 review of the Pluto Encounter data sets.                            New observations added with this version (V2.0) include ongoing          cruise observations from August, 2014 through January, 2015.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-sdc-3-plutocruise-v2.0_ffjb-zy5a",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons",
+                "dust"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-SDC-3-PLUTOCRUISE-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-sdc-3-plutocruise-v2.0_ffjb-zy5a",
-            "description": "This data set contains Calibrated data taken by the New Horizons         Student Dust Counter                                                   instrument during the                                                    pluto cruise                                                           mission phase.  This is VERSION 2.0 of this data set.                    SDC collected science data intermittently during the hibernation         years following the Jupiter encounter, designated as the PLUTOCRUISE     phase.  There were also Annual Checkouts (ACOs), STIM calibrations,      Noise calibrations, and an anomaly in November, 2007.                    SDC's main science data collection periods were during hibernation.      During ACOs, science data are taken intermittently but the user must     be careful in analyzing these data since there is usually more           activity on the spacecraft during hibernation.  STIM and Noise refer     to scheduled calibrations and are done with a regular cadence of one     per year after the Jupiter encounter; they occurred sporadically in      the early years of the mission.                                          Note that some SDC data files have the same stop and start time and      a zero exposure time.  The reason for this is that the start and         stop time for SDC data files are the event times for the first and       last events in the files, so for files that contain a single event,      these two values are the same.                                           The changes in Version 2.0 were re-running of the ancillary data         in the data product, updated geometry from newer SPICE kernels,          minor editing of the documentation, catalogs, etc., and resolution       of liens from the December, 2014 review, plus those from the May,        2016 review of the Pluto Encounter data sets.                            New observations added with this version (V2.0) include ongoing          cruise observations from August, 2014 through January, 2015.",
-            "title": "NEW HORIZONS                            \n      SDC PLUTO CRUISE                                                        \n      CALIBRATED V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS                            \n      SDC PLUTO CRUISE                                                        \n      CALIBRATED V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0949-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-08-08T03:33:40.000 to 2015-08-08T04:38:17.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0949-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0949-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0949-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-08-08T03:33:40.000 to 2015-08-08T04:38:17.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0949 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0949 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/TCSP/NAV/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Heymsfield, Gerald M.2019. TCSP ER-2 Navigation Data [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/TCSP/NAV/DATA101",
-            "issued": "2019-08-22",
-            "temporal": "2005-07-02T12:57:00Z/2005-07-27T11:46:12Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-23",
-            "keyword": [
-                "platform characteristics",
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
-            "identifier": "C1979949563-GHRC_DAAC",
             "description": "The TCSP ER-2 Navigation Data contains information recorded by the on-board navigation and data collection systems of the NASA ER-2 high-altitude research aircraft. In addition to typical navigation data (e.g., date, time, latitude/longitude, and altitude) it contains outside meteorological parameters such as wind speed, wind direction, and temperature. These data were collected during the Tropical Cloud Systems and Processes (TCSP) field campaign in July 2005, with flights based out of  Juan Santamaria Airport in San Jose, Costa Rica. The main goal of the campaign was to gain further insight into the structure and lifecycle of tropical weather systems. These navigation dataset files are available from July 2 through July 27, 2005 in ASCII and PDF formats.",
-            "graphic-preview-description": "N/A",
-            "title": "TCSP ER-2 Navigation Data V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/NAV_ER2/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FTCSP%2FNAV%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FTCSP%2FNAV%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=tcsper2nav",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=tcsper2nav",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www.nasa.gov/centers/dryden/pdf/90464main_ER2handbook.pdf",
-                    "description": "ER-2 Airborne Laboratory Experimenter Handbook",
                     "@type": "dcat:Distribution",
+                    "description": "ER-2 Airborne Laboratory Experimenter Handbook",
+                    "downloadURL": "https://www.nasa.gov/centers/dryden/pdf/90464main_ER2handbook.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/centers/armstrong/news/FactSheets/FS-046-DFRC.html",
-                    "description": "NASA Armstrong Fact Sheet: ER-2 High-Altitude Airborne Science Aircraft",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Armstrong Fact Sheet: ER-2 High-Altitude Airborne Science Aircraft",
+                    "downloadURL": "https://www.nasa.gov/centers/armstrong/news/FactSheets/FS-046-DFRC.html",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/NAV_ER2/doc/tcsper2nav_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/NAV_ER2/doc/tcsper2nav_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/BAMS-88-6-867",
-                    "description": "Nasa's Tropical Cloud Systems and Processes Experiment: Investigating Tropical Cyclogenesis and Hurricane Intensity Change",
                     "@type": "dcat:Distribution",
+                    "description": "Nasa's Tropical Cloud Systems and Processes Experiment: Investigating Tropical Cyclogenesis and Hurricane Intensity Change",
+                    "downloadURL": "https://doi.org/10.1175/BAMS-88-6-867",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/tcsp",
-                    "description": "TCSP Field Campaign Project Homepage",
                     "@type": "dcat:Distribution",
+                    "description": "TCSP Field Campaign Project Homepage",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/tcsp",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/NAV_ER2/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/NAV_ER2/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/NAV_ER2/browse/",
+            "identifier": "C1979949563-GHRC_DAAC",
+            "issued": "2019-08-22",
+            "keyword": [
+                "platform characteristics",
+                "spectral/engineering",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/TCSP/NAV/DATA101",
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
             "spatial": "-99.7368 4.68412 -65.9173 24.785",
+            "temporal": "2005-07-02T12:57:00Z/2005-07-27T11:46:12Z",
             "theme": [
                 "TCSP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TCSP ER-2 Navigation Data V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/ffpr-jrkt",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Microbes interact with humans in complex ways and understanding how they respond to the spaceflight environment is important to the success of future manned spaceflight missions. The BRIC-23 mission was designed to measure the response of Bacillus subtilis and Staphylococcus aureus to the spaceflight environment. This experiment aimed to produce high quality omics data from B. subtilis and S. aureus grown aboard the International Space Station (ISS) to allow comparison to matched ground controls. There were two primary objectives for this experiment: (1) Demonstrate all post-flight processes and operations required for successful completion of GeneLab Reference Missions conducted on ISS and (2) Generate high quality GeneLab Reference Mission omics data sets for two prokaryotic model organisms Bacillus subtilis and Staphylococcus aureus. Freezing Control Experiment: The BRIC hardware has significant thermal inertia thus the freezing rate of samples placed at -80 C is quite slow. This could affect RNA-sequencing proteomic and metabolic data sets. In an effort to understand how slow freezing could affect these data sets a control experiment was designed in which B. subtilis and S. aureus were grown in petri plates and either slow frozen to -80 C at a rate matching the BRIC-23 spaceflight samples or processed immediately to harvest RNA and protein. B.subtilis omics data is deposited in GLDS-138.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-145",
+                    "mediaType": "text/html",
+                    "title": "BRIC-23 GeneLab Process Verification Test: Staphylococcus aureus transcriptomic proteomic and metabolomic data"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-145_ffpr-jrkt",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "extraction",
                 "metabolomics mass spectrometry",
@@ -757020,442 +757034,404 @@
                 "nucleic acid extraction",
                 "nucleic acid sequencing"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/ffpr-jrkt",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-145_ffpr-jrkt",
-            "description": "Microbes interact with humans in complex ways and understanding how they respond to the spaceflight environment is important to the success of future manned spaceflight missions. The BRIC-23 mission was designed to measure the response of Bacillus subtilis and Staphylococcus aureus to the spaceflight environment. This experiment aimed to produce high quality omics data from B. subtilis and S. aureus grown aboard the International Space Station (ISS) to allow comparison to matched ground controls. There were two primary objectives for this experiment: (1) Demonstrate all post-flight processes and operations required for successful completion of GeneLab Reference Missions conducted on ISS and (2) Generate high quality GeneLab Reference Mission omics data sets for two prokaryotic model organisms Bacillus subtilis and Staphylococcus aureus. Freezing Control Experiment: The BRIC hardware has significant thermal inertia thus the freezing rate of samples placed at -80 C is quite slow. This could affect RNA-sequencing proteomic and metabolic data sets. In an effort to understand how slow freezing could affect these data sets a control experiment was designed in which B. subtilis and S. aureus were grown in petri plates and either slow frozen to -80 C at a rate matching the BRIC-23 spaceflight samples or processed immediately to harvest RNA and protein. B.subtilis omics data is deposited in GLDS-138.",
-            "title": "BRIC-23 GeneLab Process Verification Test: Staphylococcus aureus transcriptomic proteomic and metabolomic data",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-145",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "BRIC-23 GeneLab Process Verification Test: Staphylococcus aureus transcriptomic proteomic and metabolomic data"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "BRIC-23 GeneLab Process Verification Test: Staphylococcus aureus transcriptomic proteomic and metabolomic data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567235-USGS_LTA.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "U.S. Geological Survey. 2010-01-01. USGS Global Forest Observations Initiative (GFOI) Cameroon. Archived by National Aeronautics and Space Administration, U.S. Government, U.S. Geological Survey. http://lsiexplorer.cr.usgs.gov.",
-            "issued": "1972-10-31",
-            "temporal": "1972-10-31T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-03-25",
-            "keyword": [
-                "agriculture",
-                "biosphere",
-                "vegetation",
-                "terrestrial ecosystems",
-                "human dimensions",
-                "habitat conversion/fragmentation",
-                "forest science",
-                "earth science"
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
-            "identifier": "C1220567235-USGS_LTA",
-            "description": "The Global Forest Observations Initiative (GFOI) is an initiative of the inter-governmental Group on Earth Observations (GEO) that aims to:\n\nfoster the sustained availability of observations for national forest monitoring systems; support governments that are establishing national systems by providing a platform for coordinating observations, providing assistance and guidance on utilizing observations, developing accepted methods and protocols, and promoting ongoing research and development; and work with national governments that report into international forest assessments (such as the global Forest Resources Assessment (FRA) of the Food and Agriculture Organization, FAO) and the national greenhouse gas inventories reported to the UN Framework Convention on Climate Change (UNFCCC) using methods of the Intergovernmental Panel on Climate Change (IPCC).",
             "creator": "U.S. Geological Survey",
-            "title": "USGS Global Forest Observations Initiative (GFOI) Cameroon",
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
+            "identifier": "C1220567235-USGS_LTA",
+            "issued": "1972-10-31",
+            "keyword": [
+                "agriculture",
+                "biosphere",
+                "vegetation",
+                "terrestrial ecosystems",
+                "human dimensions",
+                "habitat conversion/fragmentation",
+                "forest science",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567235-USGS_LTA.html",
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
             "spatial": "6.31 0.46 17.86 14.17",
+            "temporal": "1972-10-31T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "CWIC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "USGS Global Forest Observations Initiative (GFOI) Cameroon"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/IFLOODS/GAUGES/DATA/101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Krajewski, Witold F.2017. GPM Ground Validation Iowa Flood Center (IFC) Rain Gauges IFloodS [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/IFLOODS/GAUGES/DATA/101",
-            "issued": "2017-08-08",
-            "temporal": "2013-04-28T00:00:00Z/2013-05-20T23:55:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-23",
-            "keyword": [
-                "atmospheric water vapor",
-                "atmosphere",
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
-            "identifier": "C1979697680-GHRC_DAAC",
             "description": "The GPM Ground Validation Iowa Flood Center (IFC) Rain Gauges IFloodS dataset was collected during the Iowa Flood Studies (IFloodS) field campaign from April 28, 2013 through May 20, 2013 near Shueyville City, Iowa. Four observation sites (15442, 15443, 15444, and 22390), each consisting of three tipping bucket rain gauges that collected 5-minute accumulations of precipitation data.  The main goal of IFloodS was to evaluate how well the GPM satellite rainfall data can be used for flood forecasting. Specifically, this meant collecting detailed measurements of precipitation at the Earth\u2019s surface using ground instruments and advanced weather radars while simultaneously collecting data from satellites passing overhead. These IFC Rain Gauge data are available in ASCII format, with corresponding browse images available in PNG format.",
-            "graphic-preview-description": "N/A",
-            "title": "GPM Ground Validation Iowa Flood Center (IFC) Rain Gauges IFloodS V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/disdrometers_and_gauges/rain_gauges_IFC/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FIFLOODS%2FGAUGES%2FDATA%2F101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FIFLOODS%2FGAUGES%2FDATA%2F101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmrgifcifld",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmrgifcifld",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/disdrometers_and_gauges/rain_gauges_IFC/browse/ifloods_IA_Shueyville_Site15442_Raindata_20130428_20130506.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/disdrometers_and_gauges/rain_gauges_IFC/browse/ifloods_IA_Shueyville_Site15442_Raindata_20130428_20130506.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://pmm.nasa.gov/sites/default/files/document_files/GPM%20Science%20Implementation%20Plan%20-%20April%202013.pdf",
-                    "description": "Global Precipitation Measurement (GPM) Science Implementation Plan",
                     "@type": "dcat:Distribution",
+                    "description": "Global Precipitation Measurement (GPM) Science Implementation Plan",
+                    "downloadURL": "https://pmm.nasa.gov/sites/default/files/document_files/GPM%20Science%20Implementation%20Plan%20-%20April%202013.pdf",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/disdrometers_and_gauges/rain_gauges_IFC/doc/gpmrgifcifld_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/disdrometers_and_gauges/rain_gauges_IFC/doc/gpmrgifcifld_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/disdrometers_and_gauges/rain_gauges_IFC/doc/IFLOODS_README_ET_cluster_WY.txt",
-                    "description": "Overall description of the data",
                     "@type": "dcat:Distribution",
+                    "description": "Overall description of the data",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/disdrometers_and_gauges/rain_gauges_IFC/doc/IFLOODS_README_ET_cluster_WY.txt",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/1520-0426(2003)20%3C752:LREITB%3E2.0.CO;2",
-                    "description": "Local random errors in tipping-bucket rain gauge measurements",
                     "@type": "dcat:Distribution",
+                    "description": "Local random errors in tipping-bucket rain gauge measurements",
+                    "downloadURL": "https://doi.org/10.1175/1520-0426(2003)20%3C752:LREITB%3E2.0.CO;2",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/2009JHM1137.1",
-                    "description": "Comparison of Rain Gauge Measurements in the Mid-Atlantic Region",
                     "@type": "dcat:Distribution",
+                    "description": "Comparison of Rain Gauge Measurements in the Mid-Atlantic Region",
+                    "downloadURL": "https://doi.org/10.1175/2009JHM1137.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/2009JAMC2264.1",
-                    "description": "Evaluation of TRMM ground-validation radar-rain errors using rain gauge measurements",
                     "@type": "dcat:Distribution",
+                    "description": "Evaluation of TRMM ground-validation radar-rain errors using rain gauge measurements",
+                    "downloadURL": "https://doi.org/10.1175/2009JAMC2264.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/disdrometers_and_gauges/rain_gauges_IFC/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/disdrometers_and_gauges/rain_gauges_IFC/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/disdrometers_and_gauges/rain_gauges_IFC/browse/",
+            "identifier": "C1979697680-GHRC_DAAC",
+            "issued": "2017-08-08",
+            "keyword": [
+                "atmospheric water vapor",
+                "atmosphere",
+                "precipitation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/IFLOODS/GAUGES/DATA/101",
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
             "spatial": "-91.6459 41.8548 -91.6348 41.8599",
+            "temporal": "2013-04-28T00:00:00Z/2013-05-20T23:55:00Z",
             "theme": [
                 "IFloodS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM Ground Validation Iowa Flood Center (IFC) Rain Gauges IFloodS V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-PLS-5-ELE-BR-96.0SEC",
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
+            "description": "THIS DATA SET CONTAINS THE THERMAL ELECTRON DENSITY AND TEMPERATURE IN THE PLS ENERGY RANGE (10-5950 EV) FROM VOYAGER 1 AT SATURN DERIVED BY FITTING THE LOW ENERGY ELECTRON COMPONENT WITH A MAXWELLIAN DISTRIBUTION, AND THE MOMENT DENSITY AND TEMPERATURE OF THE HOT ELECTRONS CALCULATED AFTER THE SIGNAL FROM THE THERMAL COMPONENT IS SUBTRACTED FROM THE ELECTRON SPECTRA. IT IS A SUBSET OF THE DATA SET VG1-S-PLS-5-ELE-FIT-96.0SEC WHICH SHOULD BE OBTAINED BEFORE THIS DATA IS USED. SPACECRAFT CHARGING MAY RESULT IN FACTOR OF 2-3 ERRORS IN THE THERMAL ELECTRON DENSITY. THE FIRST SIX COLUMNS ARE THE TIME TAG (YEAR, DAY, HOUR, MIN, SEC, MSEC), COLUMN 7 AND 8 ARE THE FIT DENSITY AND TEMPERATURE OF THE THERMAL ELECTRON COMPONENT, AND 9 AND 10 ARE THE MOMENT DENSITY AND TEMPERATURE OF THE SUPRATHERMAL ELECTRONS. EACH ROW HAS THE FORMAT (6I5,4E12.4). VALUES OF 1.E32 INDICATE THAT THE PARAMETER COULD NOT BE OBTAINED FROM THE DATA USING THE STANDARD ANALYSIS TECHNIQUE. ADDITIONAL INFORMATION ABOUT THIS DATASET AND THE INSTRUMENT WHICH PRODUCED IT CAN BE FOUND ELSEWHERE IN THIS CATALOG. AN OVERVIEW OF THE DATA IN THIS DATA SET CAN BE FOUND IN SITTLER ET AL. (1983) AND A COMPLETE INSTRUMENT DESCRIPTION CAN BE FOUND IN BRIDGE (1977).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-pls-5-ele-br-96.0sec_ffs9-zykp",
+            "issued": "2021-05-21",
+            "keyword": [
+                "saturn",
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-PLS-5-ELE-BR-96.0SEC",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-pls-5-ele-br-96.0sec_ffs9-zykp",
-            "description": "THIS DATA SET CONTAINS THE THERMAL ELECTRON DENSITY AND TEMPERATURE IN THE PLS ENERGY RANGE (10-5950 EV) FROM VOYAGER 1 AT SATURN DERIVED BY FITTING THE LOW ENERGY ELECTRON COMPONENT WITH A MAXWELLIAN DISTRIBUTION, AND THE MOMENT DENSITY AND TEMPERATURE OF THE HOT ELECTRONS CALCULATED AFTER THE SIGNAL FROM THE THERMAL COMPONENT IS SUBTRACTED FROM THE ELECTRON SPECTRA. IT IS A SUBSET OF THE DATA SET VG1-S-PLS-5-ELE-FIT-96.0SEC WHICH SHOULD BE OBTAINED BEFORE THIS DATA IS USED. SPACECRAFT CHARGING MAY RESULT IN FACTOR OF 2-3 ERRORS IN THE THERMAL ELECTRON DENSITY. THE FIRST SIX COLUMNS ARE THE TIME TAG (YEAR, DAY, HOUR, MIN, SEC, MSEC), COLUMN 7 AND 8 ARE THE FIT DENSITY AND TEMPERATURE OF THE THERMAL ELECTRON COMPONENT, AND 9 AND 10 ARE THE MOMENT DENSITY AND TEMPERATURE OF THE SUPRATHERMAL ELECTRONS. EACH ROW HAS THE FORMAT (6I5,4E12.4). VALUES OF 1.E32 INDICATE THAT THE PARAMETER COULD NOT BE OBTAINED FROM THE DATA USING THE STANDARD ANALYSIS TECHNIQUE. ADDITIONAL INFORMATION ABOUT THIS DATASET AND THE INSTRUMENT WHICH PRODUCED IT CAN BE FOUND ELSEWHERE IN THIS CATALOG. AN OVERVIEW OF THE DATA IN THIS DATA SET CAN BE FOUND IN SITTLER ET AL. (1983) AND A COMPLETE INSTRUMENT DESCRIPTION CAN BE FOUND IN BRIDGE (1977).",
-            "title": "VOYAGER 1 SATURN PLASMA DERIVED ELECTRON BROWSE 96 SEC",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VOYAGER 1 SATURN PLASMA DERIVED ELECTRON BROWSE 96 SEC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/594",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Roujean, J.-L, and R. Lacaze. 2001. BOREAS Follow-On DSP-08 POLDER Atmospherically Corrected Surface Parameters, SSA. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/594",
-            "issued": "2024-04-27",
-            "temporal": "1994-06-01T00:00:00Z/1994-07-22T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-28",
-            "keyword": [
-                "biosphere",
-                "earth science",
-                "atmospheric radiation",
-                "atmosphere",
-                "land surface",
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
-            "identifier": "C2956507865-ORNL_CLOUD",
             "description": "This data set contains maps of surface reflectance and vegetation parameters derived from imagery collected by the POLDER instrument over BOREAS conifer tower sites in the Southern Study Area (SSA) during 1994. The POLDER imagery provided in this data set was collected on June 1 and July 21, 1994, from the NASA C-130 aircraft platform.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS Follow-On DSP-08 POLDER Atmospherically Corrected Surface Parameters, SSA",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F594",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F594",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/DSP/BFO_dsp08_polder_surface_params/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/DSP/BFO_dsp08_polder_surface_params/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/FollowOn/guides/dsp08_polder_surf_para_doc.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/FollowOn/guides/dsp08_polder_surf_para_doc.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/594",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/594",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/DSP/BFO_dsp08_polder_surface_params/comp/0_readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/DSP/BFO_dsp08_polder_surface_params/comp/0_readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/DSP/BFO_dsp08_polder_surface_params/comp/0_site_list.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/DSP/BFO_dsp08_polder_surface_params/comp/0_site_list.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/DSP/BFO_dsp08_polder_surface_params/comp/dsp08_polder_surf_para_doc.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/DSP/BFO_dsp08_polder_surface_params/comp/dsp08_polder_surf_para_doc.pdf",
+                    "mediaType": "application/pdf",
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
+            "identifier": "C2956507865-ORNL_CLOUD",
+            "issued": "2024-04-27",
+            "keyword": [
+                "biosphere",
+                "earth science",
+                "atmospheric radiation",
+                "atmosphere",
+                "land surface",
+                "surface radiative properties",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/594",
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
             "spatial": "-111.0 48.0 -90.0 60.0",
+            "temporal": "1994-06-01T00:00:00Z/1994-07-22T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS Follow-On DSP-08 POLDER Atmospherically Corrected Surface Parameters, SSA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-C-PTOLEMY-2-FSS-V1.0",
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
+            "description": "This archive contains edited data from the PTOLEMY instrument onboard ROSETTA Lander, acquired during the FSS mission phase. The primary target is the comet 67P/CHURYUMOV-GERASIMENKO. It also contains documentation which describes the PTOLEMY experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-c-ptolemy-2-fss-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-C-PTOLEMY-2-FSS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-c-ptolemy-2-fss-v1.0",
-            "description": "This archive contains edited data from the PTOLEMY instrument onboard ROSETTA Lander, acquired during the FSS mission phase. The primary target is the comet 67P/CHURYUMOV-GERASIMENKO. It also contains documentation which describes the PTOLEMY experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER 67P PTOLEMY 2 FSS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-LANDER 67P PTOLEMY 2 FSS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2022-01-03",
-            "temporal": "2022-01-03T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "station",
-                "coordinates",
-                "coords",
-                "ephemeris",
-                "international",
-                "iss",
-                "space",
-                "trajectory",
-                "location",
-                "topo"
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
-            "identifier": "nasa-iss-data_2022-01-03_ffwr-gv9k",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2022-01-03",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -757578,363 +757554,401 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2022-01-03_ffwr-gv9k",
+            "issued": "2022-01-03",
+            "keyword": [
+                "station",
+                "coordinates",
+                "coords",
+                "ephemeris",
+                "international",
+                "iss",
+                "space",
+                "trajectory",
+                "location",
+                "topo"
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
+            "temporal": "2022-01-03T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2022-01-03"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/762/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-06-19",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "ames",
-                "nasa",
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
-            "identifier": "DASHLINK_762",
             "description": "Distributed architecture for prognostics is an essential step in prognostic research in order to enable feasible real-time system health management. Communication overhead is an important design problem for such systems. In this paper we focus on communication issues faced in the distributed implementation of an important class of algorithms for prognostics \u2013 particle filters. In spite of being computation and memory intensive, particle filters lend well to distributed implementation except for one significant step \u2013 resampling. We propose new resampling scheme called parameterized resampling that attempts to reduce communication between collaborating nodes in a distributed wireless sensor network. Analysis and comparison with relevant resampling schemes are also presented. A battery health management system is used as a target application.",
-            "title": "Communication Optimizations for a Wireless Distributed Prognostic Framework",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2009_IEEEAerospace_DistributedArchitecture.pdf",
-                    "description": "2009_IEEEAerospace_DistributedArchitecture.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "2009_IEEEAerospace_DistributedArchitecture.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2009_IEEEAerospace_DistributedArchitecture.pdf",
+                    "mediaType": "application/pdf",
                     "title": "2009_IEEEAerospace_DistributedArchitecture.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_762",
+            "issued": "2013-06-19",
+            "keyword": [
+                "ames",
+                "nasa",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/762/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Communication Optimizations for a Wireless Distributed Prognostic Framework"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-EXT1-67P-M26-INF-REFL-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the ROSETTA EXTENSION 1 mission phase, covering the period  from 2016-02-09T23:25:00.000 to 2016-03-08T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-ext1-67p-m26-inf-refl-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-EXT1-67P-M26-INF-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-ext1-67p-m26-inf-refl-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the ROSETTA EXTENSION 1 mission phase, covering the period  from 2016-02-09T23:25:00.000 to 2016-03-08T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 EXT1-MTP026 RDR-INF-REFL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 EXT1-MTP026 RDR-INF-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/247",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Myers, J.S. 1999. BOREAS Daedalus TMS Level-0 Imagery: Digital Counts in BIL Format. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/247",
-            "issued": "2024-04-30",
-            "temporal": "1994-09-16T00:00:00Z/1994-09-17T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
-            "keyword": [
-                "visible wavelengths",
-                "infrared wavelengths",
-                "land surface",
-                "spectral/engineering",
-                "surface radiative properties",
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
-            "identifier": "C2846959845-ORNL_CLOUD",
             "description": "The level-0 Daedalus TMS imagery, along with the other remotely sensed images, was collected to provide spatially extensive information about radiant energy over the primary BOREAS study areas.  This information includes detailed land cover and biophysical parameter maps such as fPAR and LAI.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS Daedalus TMS Level-0 Imagery: Digital Counts in BIL Format",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F247",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F247",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/STAFF/dtms0bil/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/STAFF/dtms0bil/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/DTMS_L0.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/DTMS_L0.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/247",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/247",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/dtms0bil/comp/dtms0bil.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/dtms0bil/comp/dtms0bil.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/dtms0bil/comp/DTMS_L0.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/dtms0bil/comp/DTMS_L0.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/dtms0bil/comp/DTMS_L0.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/dtms0bil/comp/DTMS_L0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/dtms0bil/comp/DTMS_L0.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/dtms0bil/comp/DTMS_L0.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/dtms0bil/comp/dtms_l0_image_inv.dat",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/dtms0bil/comp/dtms_l0_image_inv.dat",
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
+            "identifier": "C2846959845-ORNL_CLOUD",
+            "issued": "2024-04-30",
+            "keyword": [
+                "visible wavelengths",
+                "infrared wavelengths",
+                "land surface",
+                "spectral/engineering",
+                "surface radiative properties",
+                "vegetation",
+                "biosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/247",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-05-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-106.32 53.42 -97.23 56.25",
+            "temporal": "1994-09-16T00:00:00Z/1994-09-17T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS Daedalus TMS Level-0 Imagery: Digital Counts in BIL Format"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC4-67P-M23-STRLIGHT-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 4 mission phase, covering the period from 2015-11-17T23:25:00.000 to 2015-12-15T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc4-67p-m23-strlight-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "vega",
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "international rosetta mission",
                 "zeta cas"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC4-67P-M23-STRLIGHT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc4-67p-m23-strlight-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 4 mission phase, covering the period from 2015-11-17T23:25:00.000 to 2015-12-15T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC4-MTP023 RDR-STRLIGHT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC4-MTP023 RDR-STRLIGHT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-ASTNAMES-DISCOVERY-V12.0",
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
+            "description": "This data set includes names, designations, and discovery circumstances for the asteroids numbered as of April 20, 2008.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-astnames-discovery-v12.0_fg4u-ndgs",
+            "issued": "2018-06-26",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-ASTNAMES-DISCOVERY-V12.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-astnames-discovery-v12.0_fg4u-ndgs",
-            "description": "This data set includes names, designations, and discovery circumstances for the asteroids numbered as of April 20, 2008.",
-            "title": "ASTEROID NAMES AND DISCOVERY V12.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ASTEROID NAMES AND DISCOVERY V12.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206915-NSIDCV0.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Seasonal and annual dynamics of frozen ground, central highland of Iceland, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center.",
-            "issued": "1983-01-01",
-            "temporal": "1983-01-01T00:00:00Z/1991-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1991-12-31",
-            "keyword": [
-                "snow/ice",
-                "land surface",
-                "frozen ground",
-                "terrestrial hydrosphere",
-                "cryosphere",
-                "atmospheric temperature",
-                "earth science",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thora Thorhalsdottir",
                 "hasEmail": "mailto:theth@rhi.hi.is"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NSIDC"
-            },
-            "identifier": "C1386206915-NSIDCV0",
             "description": "This dataset documents a nine-year study to investigate the seasonal and annual dynamics of frozen ground and explore the relationship with environmental factors. The presence/absence of frozen ground and active layer thickness were recorded three times over the growing season (4-7 July, 1-4 August, and 20-24 August) at 51 permanent points in different plant communities and on 12 palsas (Thorhallsdottir 1996, p. 237).  Sample size is variable: 33 permanent measurement stations in 1983, 29 in 1984, 63 in 1985-1991. Active layer depth measurement sites averaged 51 over the span of the data set. Data include mean active layer depth (and standard error) in early July and early August (for palsas and with palsas excluded); monthly degree days above zero, precipitation, snow depth, and frost degree days (i.e., below zero.) Data are presented on the CAPS Version 1.0 CD-ROM, June 1998.",
-            "title": "Seasonal and annual dynamics of frozen ground, central highland of Iceland, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/GGD9_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/GGD9_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD9/versions/1",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://nsidc.org/data/GGD9/versions/1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD9/versions/1",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://nsidc.org/data/GGD9/versions/1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386206915-NSIDCV0",
+            "issued": "1983-01-01",
+            "keyword": [
+                "snow/ice",
+                "land surface",
+                "frozen ground",
+                "terrestrial hydrosphere",
+                "cryosphere",
+                "atmospheric temperature",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206915-NSIDCV0.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1991-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "-18.667 64.5 -18.667 64.5",
+            "temporal": "1983-01-01T00:00:00Z/1991-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Seasonal and annual dynamics of frozen ground, central highland of Iceland, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/fg6b-h7es",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Anticipating the risk for infectious disease during space exploration and habitation is a critical factor to ensure safety health and performance of the crewmembers. As a ubiquitous environmental organism that is occasionally part of the human flora Pseudomonas aeruginosa could pose a health hazard for the immuno-compromised astronauts. In order to gain insights in the behavior of P. aeruginosa in spaceflight conditions two spaceflight-analogue culture systems i.e. the rotating wall vessel (RWV) and the random position machine (RPM) were used. Microarray analysis of P. aeruginosa PAO1 grown in the low shear modeled microgravity (LSMMG) environment of the RWV compared to the normal gravity control (NG) revealed a regulatory role for AlgU (RpoE). Specifically P. aeruginosa cultured in LSMMG exhibited increased alginate production and up-regulation of AlgU-controlled transcripts including those encoding stress-related proteins. This study also shows the involvement of Hfq in the LSMMG response consistent with its previously identified role in the Salmonella LSMMG- and spaceflight response. Furthermore cultivation in LSMMG increased heat and oxidative stress resistance and caused a decrease in the culture oxygen transfer rate. Interestingly the global transcriptional response of P. aeruginosa grown in the RPM was similar to that in NG. The possible role of differences in fluid mixing between the RWV and RPM is discussed with the overall collective data favoring the RWV as the optimal model to study the LSMMG-response of suspended cells. This study represents a first step towards the identification of specific virulence mechanisms of P. aeruginosa activated in response to spaceflight-analogue conditions and could direct future research regarding the risk assessment and prevention of Pseudomonas infections for the crew in flight and the general public.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-14",
+                    "mediaType": "text/html",
+                    "title": "Response of Pseudomonas aeruginosa PAO1 to low shear modeled microgravity"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-14_fg6b-h7es",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "nucleic_acid_extraction",
                 "p-gse16970-1",
@@ -757956,114 +757970,73 @@
                 "microgravity simulation",
                 "bioassay_data_transformation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/fg6b-h7es",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-14_fg6b-h7es",
-            "description": "Anticipating the risk for infectious disease during space exploration and habitation is a critical factor to ensure safety health and performance of the crewmembers. As a ubiquitous environmental organism that is occasionally part of the human flora Pseudomonas aeruginosa could pose a health hazard for the immuno-compromised astronauts. In order to gain insights in the behavior of P. aeruginosa in spaceflight conditions two spaceflight-analogue culture systems i.e. the rotating wall vessel (RWV) and the random position machine (RPM) were used. Microarray analysis of P. aeruginosa PAO1 grown in the low shear modeled microgravity (LSMMG) environment of the RWV compared to the normal gravity control (NG) revealed a regulatory role for AlgU (RpoE). Specifically P. aeruginosa cultured in LSMMG exhibited increased alginate production and up-regulation of AlgU-controlled transcripts including those encoding stress-related proteins. This study also shows the involvement of Hfq in the LSMMG response consistent with its previously identified role in the Salmonella LSMMG- and spaceflight response. Furthermore cultivation in LSMMG increased heat and oxidative stress resistance and caused a decrease in the culture oxygen transfer rate. Interestingly the global transcriptional response of P. aeruginosa grown in the RPM was similar to that in NG. The possible role of differences in fluid mixing between the RWV and RPM is discussed with the overall collective data favoring the RWV as the optimal model to study the LSMMG-response of suspended cells. This study represents a first step towards the identification of specific virulence mechanisms of P. aeruginosa activated in response to spaceflight-analogue conditions and could direct future research regarding the risk assessment and prevention of Pseudomonas infections for the crew in flight and the general public.",
-            "title": "Response of Pseudomonas aeruginosa PAO1 to low shear modeled microgravity",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-14",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Response of Pseudomonas aeruginosa PAO1 to low shear modeled microgravity"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Response of Pseudomonas aeruginosa PAO1 to low shear modeled microgravity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1241-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-06T18:29:20.000 to 2015-12-07T03:57:31.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1241-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1241-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1241-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-06T18:29:20.000 to 2015-12-07T03:57:31.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1241 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1241 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "issue-identification": "MAC021S0",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1236350891-GES_DISC.html",
             "citation": "MODIS Science Team. GES DISC. 2006-10-01. MAC021S0. Version 002. MODIS/Aqua Calibrated Radiances 1km 5-Min 1B Narrow Swath Subset along CloudSat. Greenbelt, MD, USA. MAC021S0. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/MAC021S0_002.html. Digital Science Data.",
-            "issued": "2006-06-02",
-            "temporal": "2006-06-02T00:00:00Z/2018-03-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-03-01",
-            "keyword": [
-                "ngda",
-                "infrared wavelengths",
-                "spectral/engineering",
-                "earth science",
-                "visible wavelengths",
-                "national geospatial data asset"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANDREY SAVTCHENKO",
                 "hasEmail": "mailto:Andrey.Savtchenko@nasa.gov"
             },
+            "creator": "MODIS Science Team",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1236350891-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "This is the narrow-swath MODIS/Aqua subset along CloudSat field of view track.  The goal of the narrow-swath subset is to select and return MODIS data that are  within +-5 km across the CloudSat track.   I.e. the resultant MODIS subset swath is about 10 km cross-track.   Thus, MAC021S0 cross-track width is 11 pixels for radiances.  Geolocations in the original product, however, are subsampled at 5-km, and thus the cross-track width of the subset geolocations is 3 pixels.  Along-track, all MODIS pixels from the original product are preserved. \n      \nIn the standard product, the MODIS Level 1B data set contains calibrated and geolocated at-aperture radiances for 36 discrete bands located in the 0.4 to 14.4  micron region of electromagentic spectrum. These data are generated from the MODIS Level 1A scans of raw radiance and in the process converted to geophysical units of W/(m^2 um sr). In addition, the Earth Bi-directional Reflectance Distribution Function (BRDF) may be determined for the solar reflective bands (1-19, 26) through knowledge  of the solar irradiance (e.g., determined from MODIS solar diffuser  data, and from the target illumination geometry). Additional data are provided including quality flags, error estimates and calibration data.\n      \nVisible, shortwave infrared, and near infrared measurements are only made during the daytime, while radiances for the thermal infrared region (bands  20-25, 27-36) are measured continuously.\n      \n(The shortname for this product is MAC021S0).",
-            "editor": "GES DISC",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "MAC021S0",
-            "creator": "MODIS Science Team",
-            "title": "MODIS/Aqua Calibrated Radiances 1km 5-Min 1B Narrow Swath Subset along CloudSat V002 (MAC021S0) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/MAC021S0_002.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -758072,62 +758045,91 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/MAC021S0_002.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/MAC021S0_002.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://atrain.gesdisc.eosdis.nasa.gov/data/MAC/MAC021S0.002/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://atrain.gesdisc.eosdis.nasa.gov/data/MAC/MAC021S0.002/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
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
-                    "downloadURL": "https://modaps.nascom.nasa.gov/services/qa/science.html",
-                    "description": "Quality information of the original data.",
                     "@type": "dcat:Distribution",
+                    "description": "Quality information of the original data.",
+                    "downloadURL": "https://modaps.nascom.nasa.gov/services/qa/science.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "editor": "GES DISC",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/MAC021S0_002.png",
+            "identifier": "C1236350891-GES_DISC",
+            "issue-identification": "MAC021S0",
+            "issued": "2006-06-02",
+            "keyword": [
+                "ngda",
+                "infrared wavelengths",
+                "spectral/engineering",
+                "earth science",
+                "visible wavelengths",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1236350891-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-03-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "MAC021S0",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2006-06-02T00:00:00Z/2018-03-01T23:59:59.999Z",
             "theme": [
                 "ATDD",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Aqua Calibrated Radiances 1km 5-Min 1B Narrow Swath Subset along CloudSat V002 (MAC021S0) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-X-FC2-2-EDR-CRUISE-IMAGES-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Abstract                                                                   ========                                                                   Framing Camera 2 is one of two identical units flying on Dawn            spacecraft. This dataset includes the Experiment Data Record (EDR)       version of all available images acquired during the initial checkout and all cruise phases (Earth to Mars, Mars to Vesta and Vesta to Ceres).     In addition to the imagery, anciliary information is stored within the   image headers. Calibration files needed for further processing are       archived as a separate data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-x-fc2-2-edr-cruise-images-v1.0_fg7v-z9i3",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "1 ceres",
                 "epsilon geminorum",
@@ -758137,422 +758139,398 @@
                 "mars",
                 "hr 2290"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-X-FC2-2-EDR-CRUISE-IMAGES-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-x-fc2-2-edr-cruise-images-v1.0_fg7v-z9i3",
-            "description": "Abstract                                                                   ========                                                                   Framing Camera 2 is one of two identical units flying on Dawn            spacecraft. This dataset includes the Experiment Data Record (EDR)       version of all available images acquired during the initial checkout and all cruise phases (Earth to Mars, Mars to Vesta and Vesta to Ceres).     In addition to the imagery, anciliary information is stored within the   image headers. Calibration files needed for further processing are       archived as a separate data set.",
-            "title": "DAWN FC2 RAW (EDR) CRUISE               \n                                      CHECKOUT/CALIBRATION IMAGES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "DAWN FC2 RAW (EDR) CRUISE               \n                                      CHECKOUT/CALIBRATION IMAGES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NISTAR/DSCOVR/L1A.003",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/NISTAR/DSCOVR/L1A.003.",
-            "issued": "2020-04-08",
-            "temporal": "2017-01-31T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-04-08",
-            "keyword": [
-                "atmospheric radiation",
-                "sun-earth interactions",
-                "solar activity",
-                "earth science",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "STEVEN LORENTZ",
                 "hasEmail": "mailto:lorentz@l-1.biz"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1863115716-LARC_ASDC",
             "description": "DSCOVR_NISTAR_L1A is the Deep Space Climate Observatory (DSCOVR) National Institute of Standards & Technology Advanced Radiometer (NISTAR) Level 1A Radiance, Version 3 data product. \r\n\r\nNISTAR is a 4-band radiometer onboard NOAA\u2019s DSCOVR spacecraft located at the Earth-Sun Lagrange-1 (L-1) point, from which vantage it continuously measures the reflected and emitted radiances of the sunlit face of the Earth. These measurements provide an accurate energy balance measurement that improves our understanding of the Earth\u2019s radiation budget.\r\n\r\nNISTAR employs three electrical substitution radiometers and a photodiode to measure reflected sunlight and infrared emission from the Earth. NISTAR measures the absolute irradiance integrated over the entire sunlit face of Earth in four broadband channels minute-by-minute. NISTAR has a 1\u00ba field of view (FOV) that acts as one large pixel that encompasses the entire sunlit side of the Earth, and a 7\u00ba field of regard.\r\n\r\nThe four measurement bands and their uses are: \r\n\r\n1) Total Radiation \u2013 0.2 \u00b5m to 100 \u00b5m: total radiant power in the UV, visible, and infrared wavelengths emerging from Earth.\r\n2) Total Solar Reflected \u2013 0.2 \u00b5m to 4 \u00b5m: reflected solar radiance in UV, visible, and near infrared wavelengths from Earth.\r\n3) Near Infrared Solar Reflected \u2013 0.7 \u00b5m to 4 \u00b5m: reflected near infrared solar radiation from Earth.\r\n4) Photodiode \u2013 0.2 \u00b5m to 1.1 \u00b5m: tracks the stability of the filters, and to verify co-alignment of NISTAR and EPIC.\r\n\r\nThe Level 1A products have been converted to engineering units, but retain their one to one associations with the items in the raw telemetry from which they were derived. These data products are in HDF5 format.",
-            "title": "Deep Space Climate Observatory National Institute of Standards and Technology Advanced Radiometer Level 1A Radiance, Version 3",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNISTAR%2FDSCOVR%2FL1A.003",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNISTAR%2FDSCOVR%2FL1A.003",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/DSCOVR",
-                    "description": "ASDC Data and Information for DSCOVR",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for DSCOVR",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/DSCOVR",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/NISTAR/DSCOVR/L1A.003",
-                    "description": "DOI data set landing page for DSCOVR_NISTAR_L1A_3",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for DSCOVR_NISTAR_L1A_3",
+                    "downloadURL": "https://doi.org/10.5067/NISTAR/DSCOVR/L1A.003",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/dscovr/DSCOVR_NISTAR_Processing_V02.pdf",
-                    "description": "NISTAR Processing Description and Processing Algorithm Overview",
                     "@type": "dcat:Distribution",
+                    "description": "NISTAR Processing Description and Processing Algorithm Overview",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/dscovr/DSCOVR_NISTAR_Processing_V02.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the documentation for this dataset's algorithms"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/dscovr/DSCOVR_overview_2016-06-29.pdf",
-                    "description": "DSCOVR Earth Science Instrument Overview",
                     "@type": "dcat:Distribution",
+                    "description": "DSCOVR Earth Science Instrument Overview",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/dscovr/DSCOVR_overview_2016-06-29.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's requirements and design documentation"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/dscovr/DSCOVR_NISTAR_Users_Guide_V02.pdf",
-                    "description": "National Institute of Standards and Technology Advanced Radiometer (NISTAR) User\u2019s Guide - September 9, 2015 For the Flight Operations Team",
                     "@type": "dcat:Distribution",
+                    "description": "National Institute of Standards and Technology Advanced Radiometer (NISTAR) User\u2019s Guide - September 9, 2015 For the Flight Operations Team",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/dscovr/DSCOVR_NISTAR_Users_Guide_V02.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/image-feature/nasa-captures-epic-earth-image",
-                    "description": "NASA Captures \"EPIC\" Earth Image Article from July 20, 2015",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Captures \"EPIC\" Earth Image Article from July 20, 2015",
+                    "downloadURL": "https://www.nasa.gov/image-feature/nasa-captures-epic-earth-image",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://medium.com/@ObamaWhiteHouse/a-new-blue-marble-39c2fe1b5b3c?",
-                    "description": "A New Blue Marble By Scott Kelly, NASA Astronaut",
                     "@type": "dcat:Distribution",
+                    "description": "A New Blue Marble By Scott Kelly, NASA Astronaut",
+                    "downloadURL": "https://medium.com/@ObamaWhiteHouse/a-new-blue-marble-39c2fe1b5b3c?",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.discovermagazine.com/environment/a-spectacular-view-of-earth-unlike-any-seen-since-1972",
-                    "description": "Discover Article \"The U.S. Deep Space Climate Observatory just sent back its first view of our home world, and it\u2019s a beauty.\" By Robinson Meyer, July 20, 2015",
                     "@type": "dcat:Distribution",
+                    "description": "Discover Article \"The U.S. Deep Space Climate Observatory just sent back its first view of our home world, and it\u2019s a beauty.\" By Robinson Meyer, July 20, 2015",
+                    "downloadURL": "https://www.discovermagazine.com/environment/a-spectacular-view-of-earth-unlike-any-seen-since-1972",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://directory.eoportal.org/web/eoportal/satellite-missions/d/dscovr",
-                    "description": "Earth Observation Portal Page for DSCOVR Mission Information",
                     "@type": "dcat:Distribution",
+                    "description": "Earth Observation Portal Page for DSCOVR Mission Information",
+                    "downloadURL": "https://directory.eoportal.org/web/eoportal/satellite-missions/d/dscovr",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://twitter.com/NASAGoddard/status/676462280469553154",
-                    "description": "NASA Goddard Twitter Page",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Goddard Twitter Page",
+                    "downloadURL": "https://twitter.com/NASAGoddard/status/676462280469553154",
+                    "mediaType": "text/html",
                     "title": "Access this dataset's users feedback page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://blogs.nasa.gov/leadership/2015/07/20/dscovrs-first-light-on-the-future/",
-                    "description": "NASA Leadership Blog, DSCOVR\u2019s First Light on the Future by Buzz Aldrin",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Leadership Blog, DSCOVR\u2019s First Light on the Future by Buzz Aldrin",
+                    "downloadURL": "https://blogs.nasa.gov/leadership/2015/07/20/dscovrs-first-light-on-the-future/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/press-release/nasa-studies-high-clouds-saharan-dust-from-epic-view",
-                    "description": "NASA Studies High Clouds, Saharan Dust from EPIC View",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Studies High Clouds, Saharan Dust from EPIC View",
+                    "downloadURL": "https://www.nasa.gov/press-release/nasa-studies-high-clouds-saharan-dust-from-epic-view",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://dotearth.blogs.nytimes.com/2015/07/21/from-a-million-miles-away-a-new-nasa-blue-marble-view-of-earth",
-                    "description": "New York Times Blog \"From a Million Miles Away, a New NASA \u2018Blue Marble\u2019 View of Earth\" By Andrew C. Revkin",
                     "@type": "dcat:Distribution",
+                    "description": "New York Times Blog \"From a Million Miles Away, a New NASA \u2018Blue Marble\u2019 View of Earth\" By Andrew C. Revkin",
+                    "downloadURL": "https://dotearth.blogs.nytimes.com/2015/07/21/from-a-million-miles-away-a-new-nasa-blue-marble-view-of-earth",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.theatlantic.com/technology/archive/2015/07/our-new-and-daily-view-of-the-blue-marble/399011/",
-                    "description": "The Atlantic Article \"Al Gore Dreamed Up a Satellite\u2014and It Just Took Its First Picture of Earth: The U.S. Deep Space Climate Observatory just sent back its first view of our home world, and it\u2019s a beauty.\" By Robinson Meyer, July 20, 2015",
                     "@type": "dcat:Distribution",
+                    "description": "The Atlantic Article \"Al Gore Dreamed Up a Satellite\u2014and It Just Took Its First Picture of Earth: The U.S. Deep Space Climate Observatory just sent back its first view of our home world, and it\u2019s a beauty.\" By Robinson Meyer, July 20, 2015",
+                    "downloadURL": "https://www.theatlantic.com/technology/archive/2015/07/our-new-and-daily-view-of-the-blue-marble/399011/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/85273/plumes-from-africas-volcanic-duo",
-                    "description": "NASA Earth Observatory Article: Plumes From Africa's Volcanic Duo: Image of the Day -\u00a0Located near the equator in central Africa, the Nyamuragira and Nyiragongo volcanoes are often obscured from satellite view by clouds",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Plumes From Africa's Volcanic Duo: Image of the Day -\u00a0Located near the equator in central Africa, the Nyamuragira and Nyiragongo volcanoes are often obscured from satellite view by clouds",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/85273/plumes-from-africas-volcanic-duo",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/84542/the-legacy-of-nimbus",
-                    "description": "NASA Earth Observatory Article: The Legacy of Nimbus: Image of the Day -\u00a0No Longer Just for Astronauts",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: The Legacy of Nimbus: Image of the Day -\u00a0No Longer Just for Astronauts",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/84542/the-legacy-of-nimbus",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/81818/zaatari-refugee-camp-jordan",
-                    "description": "NASA Earth Observatory Article: Zaatari Refugee Camp, Jordan: Image of the Day",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Zaatari Refugee Camp, Jordan: Image of the Day",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/81818/zaatari-refugee-camp-jordan",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/blogs/earthmatters/2016/04/",
-                    "description": "NASA Earth Observatory Article: April : 2016 : Earth Matters : Blog\u00a0-\u00a0The images were acquired by the Earth Polychromatic Imaging Camera (EPIC) on the DSCOVR satellite",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: April : 2016 : Earth Matters : Blog\u00a0-\u00a0The images were acquired by the Earth Polychromatic Imaging Camera (EPIC) on the DSCOVR satellite",
+                    "downloadURL": "https://earthobservatory.nasa.gov/blogs/earthmatters/2016/04/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/40173/space-debris",
-                    "description": "NASA Earth Observatory Article: Space Debris: Image of the Day\u00a0-\u00a0Low and High Earth Orbital Debris Images",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Space Debris: Image of the Day\u00a0-\u00a0Low and High Earth Orbital Debris Images",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/40173/space-debris",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/blogs/earthmatters/2016/04/05/2016-tournament-earth-champion-the-dark-side-of-the-moon/",
-                    "description": "NASA Earth Observatory Article: 2016 Tournament Earth Champion: The Dark Side of the Moon\u00a0-\u00a0The images were acquired by the Earth Polychromatic Imaging Camera (EPIC) on the DSCOVR satellite",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: 2016 Tournament Earth Champion: The Dark Side of the Moon\u00a0-\u00a0The images were acquired by the Earth Polychromatic Imaging Camera (EPIC) on the DSCOVR satellite",
+                    "downloadURL": "https://earthobservatory.nasa.gov/blogs/earthmatters/2016/04/05/2016-tournament-earth-champion-the-dark-side-of-the-moon/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/features/IndonesianFires/page4.php",
-                    "description": "NASA Earth Observatory Article: Seeing Through the Smoky Pall: Observations from a Grim Indonesian Fire Season\u00a0-\u00a0The Earth Polychromatic Imaging Camera aboard the DSCOVR satellite acquired this view of smoke drifting over the region.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Seeing Through the Smoky Pall: Observations from a Grim Indonesian Fire Season\u00a0-\u00a0The Earth Polychromatic Imaging Camera aboard the DSCOVR satellite acquired this view of smoke drifting over the region.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/features/IndonesianFires/page4.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/87167/keeping-on-the-sunny-side-of-earth",
-                    "description": "NASA Earth Observatory Article: Keeping on the Sunny Side of Earth",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Keeping on the Sunny Side of Earth",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/87167/keeping-on-the-sunny-side-of-earth",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/86353/the-dark-side-and-the-bright-side",
-                    "description": "NASA Earth Observatory Article: The Dark Side and the Bright Side: Image of the Day\u00a0- A NASA camera aboard the Deep Space Climate Observatory (DSCOVR) has captured a unique view of the Moon as it passed between the spacecraft and Earth",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: The Dark Side and the Bright Side: Image of the Day\u00a0- A NASA camera aboard the Deep Space Climate Observatory (DSCOVR) has captured a unique view of the Moon as it passed between the spacecraft and Earth",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/86353/the-dark-side-and-the-bright-side",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/86257/an-epic-new-view-of-earth",
-                    "description": "NASA Earth Observatory Article: An EPIC New View of Earth: Image of the Day\u00a0-\u00a0From one million miles away, the DSCOVR satellite returned its first view of the entire sunlit side of Earth",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: An EPIC New View of Earth: Image of the Day\u00a0-\u00a0From one million miles away, the DSCOVR satellite returned its first view of the entire sunlit side of Earth",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/86257/an-epic-new-view-of-earth",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/85288/up-up-and-away-for-dscovr",
-                    "description": "NASA Earth Observatory Article: Up, Up, and Away for DSCOVR\u00a0-\u00a0The journey has been a long one for the Deep Space Climate Observatory (DSCOVR)",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Up, Up, and Away for DSCOVR\u00a0-\u00a0The journey has been a long one for the Deep Space Climate Observatory (DSCOVR)",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/85288/up-up-and-away-for-dscovr",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/87675/an-epic-eclipse",
-                    "description": "NASA Earth Observatory Article: An EPIC Eclipse: Natural Hazards\u00a0-\u00a0The Deep Space Climate Observatory (DSCOVR) was built to provide a distinct perspective on our planet.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: An EPIC Eclipse: Natural Hazards\u00a0-\u00a0The Deep Space Climate Observatory (DSCOVR) was built to provide a distinct perspective on our planet.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/87675/an-epic-eclipse",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nesdis.noaa.gov/content/dscovr-deep-space-climate-observatory",
-                    "description": "NOAA overview of DSCOVR: Deep Space Climate Observatory",
                     "@type": "dcat:Distribution",
+                    "description": "NOAA overview of DSCOVR: Deep Space Climate Observatory",
+                    "downloadURL": "https://www.nesdis.noaa.gov/content/dscovr-deep-space-climate-observatory",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncdc.noaa.gov/wct/",
-                    "description": "NOAA's Weather and Climate Toolkit",
                     "@type": "dcat:Distribution",
+                    "description": "NOAA's Weather and Climate Toolkit",
+                    "downloadURL": "https://www.ncdc.noaa.gov/wct/",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.noaa.gov/",
-                    "description": "NOAA - National Climatic Data Center (NCDC)",
                     "@type": "dcat:Distribution",
+                    "description": "NOAA - National Climatic Data Center (NCDC)",
+                    "downloadURL": "https://www.noaa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/dscovr/DSCOVR_NISTAR_Data_Quality_Report_V3.pdf",
-                    "description": "NISTAR Data Quality Report, May 17, 2019",
                     "@type": "dcat:Distribution",
+                    "description": "NISTAR Data Quality Report, May 17, 2019",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/dscovr/DSCOVR_NISTAR_Data_Quality_Report_V3.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/dscovr/DSCOVR_NISTAR_Data_Format_Control_Book_V3.pdf",
-                    "description": "NISTAR Data Format Control Book Specification April 1, 2019",
                     "@type": "dcat:Distribution",
+                    "description": "NISTAR Data Format Control Book Specification April 1, 2019",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/dscovr/DSCOVR_NISTAR_Data_Format_Control_Book_V3.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's processing history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.atmos-meas-tech.net/11/177/2018/amt-11-177-2018-discussion.html",
-                    "description": "Synoptic ozone, cloud reflectivity, and erythemal irradiance from sunrise to sunset for the whole earth as viewed by the DSCOVR spacecraft from the earth\u2013sun Lagrange 1 orbit Jay Herman et al.",
                     "@type": "dcat:Distribution",
+                    "description": "Synoptic ozone, cloud reflectivity, and erythemal irradiance from sunrise to sunset for the whole earth as viewed by the DSCOVR spacecraft from the earth\u2013sun Lagrange 1 orbit Jay Herman et al.",
+                    "downloadURL": "https://www.atmos-meas-tech.net/11/177/2018/amt-11-177-2018-discussion.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/dscovr/NISTAR_Data_Format_Control_Book_2016-07-01.pdf",
-                    "description": "NISTAR Data Format Control Book Specification June 23, 2016",
                     "@type": "dcat:Distribution",
+                    "description": "NISTAR Data Format Control Book Specification June 23, 2016",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/dscovr/NISTAR_Data_Format_Control_Book_2016-07-01.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's processing history"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/dscovr/NISTAR_Processing_V1-1_2016-07-11.pdf",
-                    "description": "NISTAR Processing Version 1 - Processing Description and Processing Algorithm Overview",
                     "@type": "dcat:Distribution",
+                    "description": "NISTAR Processing Version 1 - Processing Description and Processing Algorithm Overview",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/dscovr/NISTAR_Processing_V1-1_2016-07-11.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the documentation for this dataset's algorithms"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/dscovr/NISTAR_Quality_Report_V1-1_2016-07-11.pdf",
-                    "description": "NISTAR Quality Report -Version 1 June 28th, 2016",
                     "@type": "dcat:Distribution",
+                    "description": "NISTAR Quality Report -Version 1 June 28th, 2016",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/dscovr/NISTAR_Quality_Report_V1-1_2016-07-11.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's data quality document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1863115716-LARC_ASDC",
-                    "description": "Earthdata Search for DSCOVR_NISTAR_L1A_3 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for DSCOVR_NISTAR_L1A_3 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1863115716-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/DSCOVR/NISTAR_V3/L1A/",
-                    "description": "ASDC Direct Data Download for DSCOVR_NISTAR_L1A_3",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for DSCOVR_NISTAR_L1A_3",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/DSCOVR/NISTAR_V3/L1A/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/DSCOVR/NISTAR_V3/L1A/contents.html",
-                    "description": "OPeNDAP data access for DSCOVR_NISTAR_L1A_3",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for DSCOVR_NISTAR_L1A_3",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/DSCOVR/NISTAR_V3/L1A/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1863115716-LARC_ASDC",
+            "issued": "2020-04-08",
+            "keyword": [
+                "atmospheric radiation",
+                "sun-earth interactions",
+                "solar activity",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/NISTAR/DSCOVR/L1A.003",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-04-08",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2017-01-31T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "DSCOVR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Deep Space Climate Observatory National Institute of Standards and Technology Advanced Radiometer Level 1A Radiance, Version 3"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-MVIC-2-PLUTO-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Raw data taken by the New Horizons                Multispectral Visible Imaging Camera                                   instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 1.0 of this data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-mvic-2-pluto-v1.0_fgby-encs",
             "issued": "2018-09-05",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "nix",
                 "pluto",
                 "new horizons"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-MVIC-2-PLUTO-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-mvic-2-pluto-v1.0_fgby-encs",
-            "description": "This data set contains Raw data taken by the New Horizons                Multispectral Visible Imaging Camera                                   instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 1.0 of this data set.",
-            "title": "NEW HORIZONS                            \n      MVIC PLUTO ENCOUNTER                                                    \n      RAW V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS                            \n      MVIC PLUTO ENCOUNTER                                                    \n      RAW V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://nasa3d.arc.nasa.gov/detail/cassini-assy",
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
-                "vehicles",
-                "cassini",
-                "3d model",
-                "cassini-huygens mission",
-                "orbiter"
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
-            "identifier": "NASA-327",
             "description": "Includes orbiter from CAD models. Accurate (to a fault) except no thermal blanketing is shown (this would cover most of the central structure of the spacecraft). Polygons: 478358 Vertices: 237633",
-            "title": "NASA 3D Models: Cassini Assembly",
-            "programCode": [
-                "026:007"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -758560,48 +758538,46 @@
                     "mediaType": "image/x-3ds"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-327",
+            "issued": "2018-06-25",
+            "keyword": [
+                "vehicles",
+                "cassini",
+                "3d model",
+                "cassini-huygens mission",
+                "orbiter"
+            ],
+            "landingPage": "http://nasa3d.arc.nasa.gov/detail/cassini-assy",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:007"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "references": [
+                "http://www.nasa.gov/mission_pages/cassini/main/index.html"
+            ],
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "NASA 3D Models: Cassini Assembly"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-09-11",
-            "temporal": "2021-09-11T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "topo",
-                "coords",
-                "space",
-                "station",
-                "ephemeris",
-                "location",
-                "iss",
-                "coordinates",
-                "trajectory",
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
-            "identifier": "nasa-iss-data_2021-09-11_fgfn-sfmb",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2021-09-11",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -758724,839 +758700,865 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2021-09-11_fgfn-sfmb",
+            "issued": "2021-09-11",
+            "keyword": [
+                "topo",
+                "coords",
+                "space",
+                "station",
+                "ephemeris",
+                "location",
+                "iss",
+                "coordinates",
+                "trajectory",
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
+            "temporal": "2021-09-11T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2021-09-11"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-SDC-3-JUPITER-V3.0",
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
+            "description": "This data set contains Calibrated data taken by the New Horizons         Student Dust Counter                                                   instrument during the                                                    Jupiter encounter                                                      mission phase.  This is VERSION 3.0 of this data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-sdc-3-jupiter-v3.0_fggx-j8be",
+            "issued": "2021-05-21",
+            "keyword": [
+                "dust",
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-SDC-3-JUPITER-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-sdc-3-jupiter-v3.0_fggx-j8be",
-            "description": "This data set contains Calibrated data taken by the New Horizons         Student Dust Counter                                                   instrument during the                                                    Jupiter encounter                                                      mission phase.  This is VERSION 3.0 of this data set.",
-            "title": "NEW HORIZONS                            \n      SDC JUPITER ENCOUNTER                                                   \n      CALIBRATED V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS                            \n      SDC JUPITER ENCOUNTER                                                   \n      CALIBRATED V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MCDWD_L3_F1_NRT.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2021-03-15. MODIS/Aqua+Terra Global Flood Product L3 NRT 250m 1-day GeoTIFF. Version 6.1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, The Land, Atmosphere Near real-time Capability for EOS (LANCE). https://doi.org/10.5067/MODIS/MCDWD_L3_F1_NRT.061.",
-            "issued": "2021-03-01",
-            "temporal": "2021-03-15T00:00:00Z/2023-07-24T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-20",
-            "keyword": [
-                "terrestrial hydrosphere",
-                "national geospatial data asset",
-                "surface water",
-                "ngda",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dan Slayback",
                 "hasEmail": "mailto:floodmap@lists.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/EOS/ESDIS/LANCE MODIS"
-            },
-            "identifier": "C2018623526-LANCEMODIS",
             "description": "The MODIS/Aqua+Terra Global Flood Product L3 Near Real Time (NRT) 250m 1-day GeoTIFF (MCDWD_L3_F1_NRT) (beta) provides daily maps of flooding globally.  The Global Flood product is provided over 3 compositing periods (1-day, 2-day, and 3-day) to minimize the impact of clouds and more rigorously identify flood water (the best composite will depend on the cloudiness for a particular event).  The MCDWD_L3_F1_NRT is a 1-day product. \r\nThe beta version of the product will be updated. For more information, visit product page at:\r\nhttps://earthdata.nasa.gov/earth-observation-data/near-real-time/mcdwd-nrt",
-            "release-place": "MODAPS at NASA/GSFC",
-            "title": "MODIS/Aqua+Terra Global Flood Product L3 NRT 250m 1-day GeoTIFF",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCDWD_L3_F1_NRT.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCDWD_L3_F1_NRT.061",
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
-                    "downloadURL": "http://lance4.modaps.eosdis.nasa.gov/data_products/",
-                    "description": "Access Collection 6.1 data set from the MODAPS LANCE-MODIS page.",
                     "@type": "dcat:Distribution",
+                    "description": "Access Collection 6.1 data set from the MODAPS LANCE-MODIS page.",
+                    "downloadURL": "http://lance4.modaps.eosdis.nasa.gov/data_products/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through MODAPS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nrt4.modaps.eosdis.nasa.gov/archive/allData/61/MCDWD_L3_F1_NRT",
-                    "description": "Direct access to the download site and directory hosting the MCDWD_L3_F1_NRT C6.1 NRT data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to the download site and directory hosting the MCDWD_L3_F1_NRT C6.1 NRT data set.",
+                    "downloadURL": "https://nrt4.modaps.eosdis.nasa.gov/archive/allData/61/MCDWD_L3_F1_NRT",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through MODAPS"
                 }
             ],
+            "identifier": "C2018623526-LANCEMODIS",
+            "issued": "2021-03-01",
+            "keyword": [
+                "terrestrial hydrosphere",
+                "national geospatial data asset",
+                "surface water",
+                "ngda",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MCDWD_L3_F1_NRT.061",
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
+            "temporal": "2021-03-15T00:00:00Z/2023-07-24T00:00:00Z",
             "theme": [
                 "Aqua",
                 "Terra",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Aqua+Terra Global Flood Product L3 NRT 250m 1-day GeoTIFF"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-SPEC-2-EDR-GZ-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-spec-2-edr-gz-v1.0_fgk7-nyuc",
+            "issued": "2021-05-21",
+            "keyword": [
+                "halley",
+                "international halley watch"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-SPEC-2-EDR-GZ-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-spec-2-edr-gz-v1.0_fgk7-nyuc",
-            "description": "In preparation for the concerted international study of Comet Halley, the IHW conducted a trial run with observations of Comet Crommelin, largely during February and March of 1984.",
-            "title": "IHW COMET SPEC EDITED EXPERIMENT DATA RECORD GZ V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "IHW COMET SPEC EDITED EXPERIMENT DATA RECORD GZ V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/IMPACTS/NEXRAD/DATA122",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Brodzik, Stacy .2022. KLOT NEXRAD IMPACTS [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/IMPACTS/NEXRAD/DATA122",
-            "issued": "2022-03-23",
-            "temporal": "2020-01-01T00:10:38Z/2020-03-01T00:04:35Z",
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
-            "identifier": "C2012927437-GHRC_DAAC",
             "description": "The KLOT NEXRAD IMPACTS dataset consists of Next Generation Weather Radar (NEXRAD) Level II surveillance data that were collected at 31 NEXRAD sites from January 1 to March 1, 2020 during the Investigation of Microphysics and Precipitation for Atlantic Coast-Threatening Snowstorms  (IMPACTS) field campaign. IMPACTS was a three-year sequence of winter season deployments conducted to study snowstorms over the U.S Atlantic Coast. The campaign aimed to (1) Provide observations critical to understanding the mechanisms of snowband formation, organization, and evolution; (2) Examine how the microphysical characteristics and likely growth mechanisms of snow particles vary across snowbands; and (3) Improve snowfall remote sensing interpretation and modeling to significantly advance prediction capabilities. There are currently 160 Weather Surveillance Radar-1988 Doppler (WSR-88D) or NEXRAD sites throughout the United States and abroad. This Level II dataset contains meteorological and dual-polarization base data quantities including: radar reflectivity, radial velocity, spectrum width, differential reflectivity, differential phase, and cross correlation ratio. The IMPACTS NEXRAD Level II data files are available in netCDF-4 format. It should be noted that this dataset will be updated in subsequent years of the IMPACTS campaign.",
-            "title": "KLOT NEXRAD IMPACTS V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FNEXRAD%2FDATA122",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FNEXRAD%2FDATA122",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=klotimpacts",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=klotimpacts",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/NEXRAD/KLOT/doc/nexrad_datasets.pdf",
-                    "description": "NEXRAD IMPACTS User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "NEXRAD IMPACTS User Guide",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/NEXRAD/KLOT/doc/nexrad_datasets.pdf",
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
+            "identifier": "C2012927437-GHRC_DAAC",
+            "issued": "2022-03-23",
+            "keyword": [
+                "spectral/engineering",
+                "radar",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/IMPACTS/NEXRAD/DATA122",
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
             "spatial": "-93.612 37.474 -82.557 45.735",
+            "temporal": "2020-01-01T00:10:38Z/2020-03-01T00:04:35Z",
             "theme": [
                 "IMPACTS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "KLOT NEXRAD IMPACTS V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/OASIS_MOORINGS/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/OASIS_MOORINGS/DATA001.",
-            "issued": "1995-03-16",
-            "temporal": "1995-03-16T00:00:00Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean chemistry",
-                "earth science",
-                "ocean optics",
-                "oceans",
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
-            "identifier": "C1633360534-OB_DAAC",
             "description": "Measurements from the OASIS moorings at the mouth of the Monterey Bay in 1995.",
-            "title": "Ocean Acquisition System for Interdisciplinary Science (OASIS) moorings",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FOASIS_MOORINGS%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FOASIS_MOORINGS%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/OASIS_Moorings/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/OASIS_Moorings/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360534-OB_DAAC",
+            "issued": "1995-03-16",
+            "keyword": [
+                "ocean chemistry",
+                "earth science",
+                "ocean optics",
+                "oceans",
+                "ocean temperature",
+                "salinity/density"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/OASIS_MOORINGS/DATA001",
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
+            "temporal": "1995-03-16T00:00:00Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Ocean Acquisition System for Interdisciplinary Science (OASIS) moorings"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Anearmsi.shapebackplane&version=1.0",
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
-                "(433) eros",
-                "near earth asteroid rendezvous"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains data products for 93,397 images obtained by the Multi-Spectral Imager (MSI) of the Near  Earth Asteroid Rendezvous (NEAR) mission during the orbital phase at   asteroid 433 Eros. The data products include geometric and geophysical information for each pixel. The data products are in the form of       backplanes, stored in the FITS image format. There is one backplane    file for each MSI image. Each of the MSI backplane files is a 16-band  image cube. The bands of the cube contain the information detailed     below calculated for the center of each pixel:                         1: Pixel values (I/F) of the original FITS images delivered to the PDS by the NEAR team [Murchie et al., 2001], linearly resampled to rectify the image by squaring the pixels. The original image size is 537 x 244 pixels and the rectified size is 537 x 412 pixels.                     2: x coordinate (kilometers) of the intercept with the surface of the  asteroid in body-fixed reference frame                                 3: y coordinate (kilometers) of the intercept with the surface of the  asteroid in body-fixed reference frame                                 4: z coordinate (kilometers) of the intercept with the surface of the  asteroid in body-fixed reference frame                                 5: latitude (planetocentric, degrees)                                  6: longitude (degrees east)                                            7: radial distance (kilometers) from the asteroid center of figure     8: solar incidence angle (degrees)                                     9: emission angle (degrees)                                            10: solar phase angle (degrees)                                        11: horizontal pixel scale (kilometers)                                12: vertical pixel scale (kilometers)                                  13: average surface slope relative to gravity (degrees)                14: average elevation relative to gravity (meters)                     15: average gravitational acceleration (meters/[s^2])                  16: average gravitational potential (J/kg)",
+            "identifier": "urn:nasa:pds:nearmsi.shapebackplane_fgs2-u68q",
+            "issued": "2018-06-26",
+            "keyword": [
+                "(433) eros",
+                "near earth asteroid rendezvous"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Anearmsi.shapebackplane&version=1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:nearmsi.shapebackplane_fgs2-u68q",
-            "description": "This data set contains data products for 93,397 images obtained by the Multi-Spectral Imager (MSI) of the Near  Earth Asteroid Rendezvous (NEAR) mission during the orbital phase at   asteroid 433 Eros. The data products include geometric and geophysical information for each pixel. The data products are in the form of       backplanes, stored in the FITS image format. There is one backplane    file for each MSI image. Each of the MSI backplane files is a 16-band  image cube. The bands of the cube contain the information detailed     below calculated for the center of each pixel:                         1: Pixel values (I/F) of the original FITS images delivered to the PDS by the NEAR team [Murchie et al., 2001], linearly resampled to rectify the image by squaring the pixels. The original image size is 537 x 244 pixels and the rectified size is 537 x 412 pixels.                     2: x coordinate (kilometers) of the intercept with the surface of the  asteroid in body-fixed reference frame                                 3: y coordinate (kilometers) of the intercept with the surface of the  asteroid in body-fixed reference frame                                 4: z coordinate (kilometers) of the intercept with the surface of the  asteroid in body-fixed reference frame                                 5: latitude (planetocentric, degrees)                                  6: longitude (degrees east)                                            7: radial distance (kilometers) from the asteroid center of figure     8: solar incidence angle (degrees)                                     9: emission angle (degrees)                                            10: solar phase angle (degrees)                                        11: horizontal pixel scale (kilometers)                                12: vertical pixel scale (kilometers)                                  13: average surface slope relative to gravity (degrees)                14: average elevation relative to gravity (meters)                     15: average gravitational acceleration (meters/[s^2])                  16: average gravitational potential (J/kg)",
-            "title": "EROS MSI IMAGES WITH GEOMETRY BACKPLANES",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "EROS MSI IMAGES WITH GEOMETRY BACKPLANES"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CGVZ4V9AAY7X",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "AMSRIce03 Snow Depth Data, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/CGVZ4V9AAY7X.",
-            "issued": "2003-03-04",
-            "temporal": "2003-03-04T00:00:00Z/2003-03-19T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2003-03-19",
-            "keyword": [
-                "earth science",
-                "snow/ice",
-                "terrestrial hydrosphere",
-                "cryosphere"
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
-            "identifier": "C1386205135-NSIDCV0",
             "description": "Notice to Data Users: The documentation for this data set was provided solely by the Principal Investigator(s) and was not further developed, thoroughly reviewed, or edited by NSIDC. Thus, support for this data set may be limited.\n\nThis data set contains snow depth measurements collected over sea ice in the Barrow, Alaska area and at the Navy Ice Camp in the main pack ice of the Arctic Ocean as part of the joint in situ and aircraft AMSRIce03 campaign.",
-            "title": "AMSRIce03 Snow Depth Data, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCGVZ4V9AAY7X",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCGVZ4V9AAY7X",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/cryosphere/AMSRIce03/ground_data/snowdepth/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/cryosphere/AMSRIce03/ground_data/snowdepth/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/cryosphere/AMSRIce03/ground_data/snowdepth/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/cryosphere/AMSRIce03/ground_data/snowdepth/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/CGVZ4V9AAY7X",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/CGVZ4V9AAY7X",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/CGVZ4V9AAY7X",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/CGVZ4V9AAY7X",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386205135-NSIDCV0",
+            "issued": "2003-03-04",
+            "keyword": [
+                "earth science",
+                "snow/ice",
+                "terrestrial hydrosphere",
+                "cryosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/CGVZ4V9AAY7X",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2003-03-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-156.4 71.18 -156.15 71.28",
+            "temporal": "2003-03-04T00:00:00Z/2003-03-19T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AMSRIce03 Snow Depth Data, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/224",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Kittel, T.G.F., N.A. Rosenbloom, T.H. Painter, D.S. Schimel, H.H. Fisher, A. Grimsdell,  , C. Daly, and E.R. Hunt. 1998. VEMAP 1: U.S. Climate, 1961-1990. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/224",
-            "issued": "2024-04-22",
-            "temporal": "1961-01-01T00:00:00Z/1990-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-23",
-            "keyword": [
-                "earth science",
-                "precipitation",
-                "atmospheric radiation",
-                "atmosphere",
-                "atmospheric winds",
-                "atmospheric water vapor",
-                "atmospheric temperature"
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
-            "identifier": "C2946787569-ORNL_CLOUD",
             "description": "An integrated input data set for ecosystem and vegetation modeling for the conterminous United States: Climate",
-            "graphic-preview-description": "Browse Image",
-            "title": "VEMAP 1: U.S. Climate, 1961-1990",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/vemap_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F224",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F224",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/vemap/vemap-1_climate/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/vemap/vemap-1_climate/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/VEMAP/guides/climate.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/VEMAP/guides/climate.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/224",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/224",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-1_climate/comp/biread.f",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-1_climate/comp/biread.f",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-1_climate/comp/climate.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-1_climate/comp/climate.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-1_climate/comp/CORRECT.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-1_climate/comp/CORRECT.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-1_climate/comp/Phase_1_User_Guide.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-1_climate/comp/Phase_1_User_Guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-1_climate/comp/README.MON",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-1_climate/comp/README.MON",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-1_climate/comp/README.vem",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-1_climate/comp/README.vem",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-1_climate/comp/SVF_FORMAT",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-1_climate/comp/SVF_FORMAT",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-1_climate/comp/VEMAPDOC.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-1_climate/comp/VEMAPDOC.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/vemap_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/vemap_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/vemap_logo_square.png",
+            "identifier": "C2946787569-ORNL_CLOUD",
+            "issued": "2024-04-22",
+            "keyword": [
+                "earth science",
+                "precipitation",
+                "atmospheric radiation",
+                "atmosphere",
+                "atmospheric winds",
+                "atmospheric water vapor",
+                "atmospheric temperature"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/224",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-04-23",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-124.5 25.0 -67.0 49.0",
+            "temporal": "1961-01-01T00:00:00Z/1990-12-31T23:59:59Z",
             "theme": [
                 "VEMAP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VEMAP 1: U.S. Climate, 1961-1990"
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
-                "oceans",
-                "earth science",
-                "cryosphere",
-                "sea surface topography",
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
-            "identifier": "C1000000420-NSIDC_ECS",
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
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/GLAS/GLAH15.034/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/GLAS/GLAH15.034/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000420-NSIDC_ECS&m=-31.921875%210.84375%211%211%210%210%2C2&q=GLAH15",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000420-NSIDC_ECS&m=-31.921875%210.84375%211%211%210%210%2C2&q=GLAH15",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/GLAH15/versions/34/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/GLAH15/versions/34/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
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
+            "identifier": "C1000000420-NSIDC_ECS",
+            "issued": "2003-02-20",
+            "keyword": [
+                "oceans",
+                "earth science",
+                "cryosphere",
+                "sea surface topography",
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
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1264",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Xu, X., P.E. Thornton, and P. Potapov. 2014. A Compilation of Global Soil Microbial Biomass Carbon, Nitrogen, and Phosphorus Data. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1264",
-            "issued": "2015-01-12",
-            "temporal": "1977-11-16T00:00:00Z/2012-06-01T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "land surface",
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
-            "identifier": "C2216863966-ORNL_CLOUD",
             "description": "This data set provides the concentrations of soil microbial biomass carbon (C), nitrogen (N) and phosphorus (P), soil organic carbon, total nitrogen, and total phosphorus at biome and global scales. The data were compiled from a comprehensive survey of publications from the late 1970s to 2012 and include 3,422 data points from 315 papers. These data are from soil samples collected primarily at 0-15 cm depth with some from 0-30 cm. In addition, data were compiled for soil microbial biomass concentrations from soil profile samples to depths of 100 cm. Sampling site latitude and longitude were available for the majority of the samples that enabled assembling additional soil properties, site characteristics, vegetation distributions, biomes, and long-term climate data from several global sources of soil, land-cover, and climate data. These site attributes are included with the microbial biomass data. This data set contains two *.csv files of the soil microbial biomass C, N, P data. The first provides all compiled results emphasizing the full spatial extent of the data, while the second is a subset that provides only data from a series of profile samples emphasizing the vertical distribution of microbial biomass concentrations.There is a companion file, also in .csv format, of the references for the surveyed publications. A reference_number relates the data to the respective publication.The concentrations of soil microbial biomass, in combination with other soil databases, were used to estimate the global storage of soil microbial biomass C and N in 0-30 cm and 0-100 cm soil profiles. These storage estimates were combined with a spatial map of 12 major biomes (boreal forest, temperate coniferous forest, temperate broadleaf forest, tropical and subtropical forests, mixed forest, grassland, shrub, tundra, desert, natural wetland, cropland, and pasture) at 0.05-degree by 0.5-degree spatial resolution. The biome map and six estimates of C and N storage and C:N ration in soil microbial biomass are provided in a single netCDF format file.",
-            "graphic-preview-description": "Distribution of the data points used in this study.",
-            "title": "A Compilation of Global Soil Microbial Biomass Carbon, Nitrogen, and Phosphorus Data",
-            "graphic-preview-file": "https://daac.ornl.gov/SOILS/guides/fig_1_global_biomass.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1264",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1264",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/global_soil/Global_Microbial_Biomass_C_N_P/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/global_soil/Global_Microbial_Biomass_C_N_P/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/SOILS/guides/Global_Microbial_Biomass_C_N_P.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/SOILS/guides/Global_Microbial_Biomass_C_N_P.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1264",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1264",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/Global_Microbial_Biomass_C_N_P/comp/Global_Microbial_Biomass_C_N_P.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/Global_Microbial_Biomass_C_N_P/comp/Global_Microbial_Biomass_C_N_P.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/Global_Microbial_Biomass_C_N_P/comp/Soil_Microbial_Biomass_C_N_P_references.csv",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/Global_Microbial_Biomass_C_N_P/comp/Soil_Microbial_Biomass_C_N_P_references.csv",
+                    "mediaType": "text/csv",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/Global_Microbial_Biomass_C_N_P/comp/XuXF2013_GEB.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/Global_Microbial_Biomass_C_N_P/comp/XuXF2013_GEB.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/SOILS/guides/fig_1_global_biomass.png",
-                    "description": "Distribution of the data points used in this study.",
                     "@type": "dcat:Distribution",
+                    "description": "Distribution of the data points used in this study.",
+                    "downloadURL": "https://daac.ornl.gov/SOILS/guides/fig_1_global_biomass.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Distribution of the data points used in this study.",
+            "graphic-preview-file": "https://daac.ornl.gov/SOILS/guides/fig_1_global_biomass.png",
+            "identifier": "C2216863966-ORNL_CLOUD",
+            "issued": "2015-01-12",
+            "keyword": [
+                "land surface",
+                "soils",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1264",
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
             "spatial": "-180.0 -90.0 177.9 79.0",
+            "temporal": "1977-11-16T00:00:00Z/2012-06-01T23:59:59Z",
             "theme": [
                 "Soil",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "A Compilation of Global Soil Microbial Biomass Carbon, Nitrogen, and Phosphorus Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MULTI-SA-MULTI-6-STOOKEMAPS-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "These maps of small solar system bodies have been prepared by Philip Stooke of the University of Western Ontario. This data set includes 221 map sheets of five asteroids, five planetary satellites, and one comet, all prepared from spacecraft images.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.multi-sa-multi-6-stookemaps-v1.0_fh7d-6arn",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "433 eros",
                 "voyager",
@@ -759581,354 +759583,326 @@
                 "253 mathilde",
                 "81p/wild 2 (1978 a2)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MULTI-SA-MULTI-6-STOOKEMAPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.multi-sa-multi-6-stookemaps-v1.0_fh7d-6arn",
-            "description": "These maps of small solar system bodies have been prepared by Philip Stooke of the University of Western Ontario. This data set includes 221 map sheets of five asteroids, five planetary satellites, and one comet, all prepared from spacecraft images.",
-            "title": "STOOKE SMALL BODIES MAPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "STOOKE SMALL BODIES MAPS V1.0"
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-e-alice-4-ear3-v1.0_fh7e-avuy",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "moon",
                 "earth",
                 "calibration",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL%2FE-ALICE-4-EAR3-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-e-alice-4-ear3-v1.0_fh7e-avuy",
-            "description": "This data set contains CODMAC level 4 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the third earth flyby mission phase, which took place between 2009-09-14 and 2009-12-13.",
-            "title": "ROSETTA-ORBITER CAL/EARTH ALICE 4 EAR3 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER CAL/EARTH ALICE 4 EAR3 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/YAMX52BXFL10",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMAP Radiometer Twice-Daily rSIR-Enhanced EASE-Grid 2.0 Brightness Temperatures V002. Version 2. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/YAMX52BXFL10.",
-            "issued": "2015-03-31",
-            "temporal": "2015-03-31T00:00:00Z/2022-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-12-31",
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
-            "identifier": "C2103333573-NSIDC_ECS",
             "description": "This data set contains twice-daily, enhanced-resolution brightness temperature data derived from the SMAP radiometer. Data are available on the Northern Hemisphere, Southern Hemisphere, Temperate, and Mid-Latitude (sub-set of Global) EASE-Grid 2.0 projections and on the 3 km, 3.125 km, 9 km,  25 km, and 36 km resolution grids. This data set applies the same SIR technique used to derive brightness temperatures from the SMMR, AMSR-E, and SSM/I-SSMIS sensors and is a companion product for the MEaSUREs Calibrated Enhanced-Resolution Passive Microwave Daily EASE-Grid 2.0 Brightness Temperature ESDR data set (DOI: 10.5067/MEASURES/CRYOSPHERE/NSIDC-0630.001).",
-            "title": "SMAP Radiometer Twice-Daily rSIR-Enhanced EASE-Grid 2.0 Brightness Temperatures V002",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FYAMX52BXFL10",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FYAMX52BXFL10",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP/NSIDC-0738.002/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP/NSIDC-0738.002/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0738/versions/2/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0738/versions/2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=NSIDC-0738+V002",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=NSIDC-0738+V002",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/YAMX52BXFL10",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/YAMX52BXFL10",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/YAMX52BXFL10",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/YAMX52BXFL10",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2103333573-NSIDC_ECS",
+            "issued": "2015-03-31",
+            "keyword": [
+                "microwave",
+                "earth science",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/YAMX52BXFL10",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2015-03-31T00:00:00Z/2022-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMAP Radiometer Twice-Daily rSIR-Enhanced EASE-Grid 2.0 Brightness Temperatures V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1099",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Morton, D.C., R.S. Defries, Y.E. Shimabukuro, L.O. Anderson, E. Arai, F.D.B. Espirito-Santo, R.M. Freitas, and J.T. Morisette. 2012. LBA-ECO LC-22 Post-deforestation Land Use, Mato Grosso, Brazil: 2001-2005. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1099",
-            "issued": "2023-10-03",
-            "temporal": "2001-08-01T00:00:00Z/2005-07-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-10",
-            "keyword": [
-                "human dimensions",
-                "earth science",
-                "ngda",
-                "national geospatial data asset",
-                "habitat conversion/fragmentation"
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
-            "identifier": "C2780155131-ORNL_CLOUD",
             "description": "This data set provides (1) areal estimates of deforestation events (>25 ha) that were identified from 2001-2004 in Mato Grosso by the Brazilian Institute for Space Research (INPE) as part of the Program for the Estimation of Deforestation in the Brazilian Amazon (PRODES) and (2) the classification of the post-deforestation land use as either cropland, cattle pasture, or not in production (deforested areas that were never fully cleared or returned immediately to secondary forest) in the years after the large deforestation events from 2002-2005. Data are provided in ESRI shapefile format. There are five compressed (*.zip) data files with this data set. Each shapefile represents one year of post-deforestation land use. Land use in the years following deforestation was estimated using annual time series of MODIS NDVI (normalized difference vegetation index) and EVI (enhanced vegetation index). Metrics of vegetation phenology derived annual time series of MODIS NDVI and EVI data were analyzed using a decision-tree classifier to characterize the major cover type in each area of new deforestation. Post-deforestation land use for each large deforestation event was classified based on the classification of MODIS phenology metrics for all years following deforestation during 2002-2005.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO LC-22 Post-deforestation Land Use, Mato Grosso, Brazil: 2001-2005",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1099",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1099",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC22_Post_Deforestation_LULC/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC22_Post_Deforestation_LULC/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC22_Post_Deforestation_LULC.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC22_Post_Deforestation_LULC.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1099",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1099",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC22_Post_Deforestation_LULC/comp/LC22_Post_Deforestation_LULC.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC22_Post_Deforestation_LULC/comp/LC22_Post_Deforestation_LULC.pdf",
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
+            "identifier": "C2780155131-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "human dimensions",
+                "earth science",
+                "ngda",
+                "national geospatial data asset",
+                "habitat conversion/fragmentation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1099",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-10-10",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-61.01 -18.23 -50.1 -7.47",
+            "temporal": "2001-08-01T00:00:00Z/2005-07-31T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO LC-22 Post-deforestation Land Use, Mato Grosso, Brazil: 2001-2005"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-L-MRO24M_PHOTGJON-2-EDR-LCROSS-V1.0",
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
-                "lunar crater observation and sensing satellite"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This archive contains raw observations of the 2009-10-09 impact of the LCROSS spacecraft on the moon by the PHOTGJON instrument on the Magdalena Ridge Observatory 2.4m telescope. This dataset consists of frame-transfer CCD observations of the LCROSS impact site as well as unresolved images of the primary impactor in the final hours before impact.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-l-mro24m_photgjon-2-edr-lcross-v1.0_fh8f-wwxz",
+            "issued": "2018-06-26",
+            "keyword": [
+                "moon",
+                "lunar crater observation and sensing satellite"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-L-MRO24M_PHOTGJON-2-EDR-LCROSS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-l-mro24m_photgjon-2-edr-lcross-v1.0_fh8f-wwxz",
-            "description": "This archive contains raw observations of the 2009-10-09 impact of the LCROSS spacecraft on the moon by the PHOTGJON instrument on the Magdalena Ridge Observatory 2.4m telescope. This dataset consists of frame-transfer CCD observations of the LCROSS impact site as well as unresolved images of the primary impactor in the final hours before impact.",
-            "title": "MAGDALENA RIDGE OBSERVATORY 2.4M PHOTGJON LCROSS OBSERVATION",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MAGDALENA RIDGE OBSERVATORY 2.4M PHOTGJON LCROSS OBSERVATION"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0560-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-02-02T16:53:50.000 to 2015-02-02T22:45:14.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0560-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0560-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0560-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-02-02T16:53:50.000 to 2015-02-02T22:45:14.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0560 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0560 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Q28GFYJYFZ7H",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Scarpelli, Tia R.; Jacob, Daniel J.; Maasakkers, Joannes D.; Sulprizio, Melissa P.; Sheng, Jian-Xiong; Rose, Kelly; Romeo, Lucy; Worden, John R.; Janssens-Maenhout, Greet. 2021-10-08. GFEI_CH4. Version 1. Global Inventory of Methane Emissions from Fuel Exploitation. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Q28GFYJYFZ7H. https://disc.gsfc.nasa.gov/datacollection/GFEI_CH4_1.html.",
-            "issued": "2016-01-01",
-            "temporal": "2016-01-01T00:00:00Z/2016-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-12-31",
-            "references": [
-                "https://doi.org/10.5194/essd-12-563-2020",
-                "https://doi.org/10.7910/DVN/HH4EUM"
-            ],
-            "keyword": [
-                "atmosphere",
-                "atmospheric chemistry",
-                "earth science"
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
-            "identifier": "C2143386827-GES_DISC",
-            "description": "This is a global inventory of methane emissions from fuel exploitation (GFEI) created for the NASA Carbon Monitoring System (CMS). The emission sources represented in this dataset include fugitive emission sources from oil, gas, and coal exploitation following IPCC 2006 definitions and are estimated using bottom-up methods. The inventory emissions are based on individual country reports submitted in accordance with the United Nations Framework Convention on Climate Change (UNFCCC). For those countries that do not report, the emissions are estimated following IPCC 2006 methods. Emissions are allocated to infrastructure locations including mines, wells, pipelines, compressor stations, storage facilities, processing plants, and refineries.\n  The purpose of the inventory is to be used as a prior estimate of fuel exploitation emissions in inverse modeling of atmospheric methane observations. GFEI only includes fugitive methane emissions from oil, gas, and coal exploitation activities and does not include any combustion emissions as defined in IPCC 2006 category 1A.\n The CMS program is designed to make significant contributions in characterizing, quantifying, understanding, and predicting the evolution of global carbon sources and sinks through improved monitoring of carbon stocks and fluxes. The System uses NASA observations and modeling/analysis capabilities to establish the accuracy, quantitative uncertainties, and utility of products for supporting national and international policy, regulatory, and management activities. CMS data products are designed to inform near-term policy development and planning.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "GFEI_CH4",
             "creator": "Scarpelli, Tia R.; Jacob, Daniel J.; Maasakkers, Joannes D.; Sulprizio, Melissa P.; Sheng, Jian-Xiong; Rose, Kelly; Romeo, Lucy; Worden, John R.; Janssens-Maenhout, Greet",
-            "title": "Global Inventory of Methane Emissions from Fuel Exploitation V1 (GFEI_CH4)",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/CMS/GFEI_CH4_1.png",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This is a global inventory of methane emissions from fuel exploitation (GFEI) created for the NASA Carbon Monitoring System (CMS). The emission sources represented in this dataset include fugitive emission sources from oil, gas, and coal exploitation following IPCC 2006 definitions and are estimated using bottom-up methods. The inventory emissions are based on individual country reports submitted in accordance with the United Nations Framework Convention on Climate Change (UNFCCC). For those countries that do not report, the emissions are estimated following IPCC 2006 methods. Emissions are allocated to infrastructure locations including mines, wells, pipelines, compressor stations, storage facilities, processing plants, and refineries.\n  The purpose of the inventory is to be used as a prior estimate of fuel exploitation emissions in inverse modeling of atmospheric methane observations. GFEI only includes fugitive methane emissions from oil, gas, and coal exploitation activities and does not include any combustion emissions as defined in IPCC 2006 category 1A.\n The CMS program is designed to make significant contributions in characterizing, quantifying, understanding, and predicting the evolution of global carbon sources and sinks through improved monitoring of carbon stocks and fluxes. The System uses NASA observations and modeling/analysis capabilities to establish the accuracy, quantitative uncertainties, and utility of products for supporting national and international policy, regulatory, and management activities. CMS data products are designed to inform near-term policy development and planning.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FQ28GFYJYFZ7H",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FQ28GFYJYFZ7H",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -759938,797 +759912,804 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GFEI_CH4_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GFEI_CH4_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/GFEI_CH4.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/GFEI_CH4.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/GFEI_CH4.1/doc/README.GFEI_CH4_v1.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/GFEI_CH4.1/doc/README.GFEI_CH4_v1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/CMS/GFEI_CH4.1/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/CMS/GFEI_CH4.1/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GFEI_CH4",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GFEI_CH4",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/CMS/GFEI_CH4_1.png",
+            "identifier": "C2143386827-GES_DISC",
+            "issued": "2016-01-01",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Q28GFYJYFZ7H",
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
+                "https://doi.org/10.5194/essd-12-563-2020",
+                "https://doi.org/10.7910/DVN/HH4EUM"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "GFEI_CH4",
             "spatial": "-180.0 -90.0 -180.0 90.0",
+            "temporal": "2016-01-01T00:00:00Z/2016-12-31T23:59:59.999Z",
             "theme": [
                 "CMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Inventory of Methane Emissions from Fuel Exploitation V1 (GFEI_CH4)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-HAZCAM-4-LINEARIZED-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-hazcam-4-linearized-ops-v1.0_fhd3-9yay",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-HAZCAM-4-LINEARIZED-OPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-hazcam-4-linearized-ops-v1.0_fhd3-9yay",
-            "description": "NULL",
-            "title": "MER 2 MARS HAZARD AVOID CAMERA\n                                    LINEARIZED RDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MER 2 MARS HAZARD AVOID CAMERA\n                                    LINEARIZED RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/RSX12-L2A20",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "RapidScat Project. 2023-05-15. RapidScat Level 2A Surface Flagged Sigma-0 and Attenuations in 12.5Km Swath Grid. Version 2.0. RapidScat Level 2A Surface Flagged Sigma-0 and Attenuations in 12.5Km Swath Grid Version 2.0. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/RSX12-L2A20. https://d2pn8kiwq2w21t.cloudfront.net/documents/issrapidscat_factsheet.pdf. RapidScat Project, PO.DAAC, 2023-15-15, RapidScat Level 2A Surface Flagged Sigma-0 and Attenuations in 12.5Km Swath Grid Version 2.0, https://d2pn8kiwq2w21t.cloudfront.net/documents/issrapidscat_factsheet.pdf.",
-            "issued": "2016-09-28",
-            "temporal": "2014-10-03T00:00:00Z/2016-08-19T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-04-28",
-            "keyword": [
-                "spectral/engineering",
-                "radar",
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
-            "identifier": "C2633944131-POCLOUD",
-            "description": "This dataset contains the Version 2.0 ISS-RapidScat on Level 2A 12.5 km science data record, which provides surface-flagged sigma-0 in 12.5 km Wind Vector Cells processed using the pulse \"slice\" Sigma-0 data provided by the Level 1B dataset. Due to the circular scan of the RapidScat instrument the expected number of Sigma-0 cells per WVC is not constant. To minimize the L2A data volume, the Sigma-0 cell data are stored as \"lists\" for each WVC row, with each list indexed by a \"cell_index\" array to indicate the cross-track WVC membership of the data. Each cell is then checked for land or ice and flagged accordingly. Attenuation corrections for each Sigma-0 measurement are also provided. Data are provided in single-orbit files in HDF-4 format. Version 2.0 represents a complete historical re-processing of the L2A data record (see the technical note for Version 2.0 under Documentation). RapidScat is a Ku-band dual beam circular rotating scatterometer retaining much of the same hardware and functionality of QuikSCAT, with exception of the antenna sub-system and digital interface to the International Space Station (ISS) Columbus module, which is where RapidScat is mounted. The NASA mission is officially referred to as ISS-RapidScat. Unlike QuikSCAT, ISS-RapidScat is not in sun-synchronous orbit, and flies at roughly half the altitude with a low inclination angle that restricts data coverage to the tropics and mid-latitude regions; the extent of latitudinal coverage stretches from approximately 61 degrees North to 61 degrees South. Furthermore, there is no consistent local time of day retrieval. If you have any questions or concerns, please visit our Forum at https://podaac.jpl.nasa.gov/forum/.",
-            "release-place": "PO.DAAC",
-            "series-name": "RapidScat Level 2A Surface Flagged Sigma-0 and Attenuations in 12.5Km Swath Grid",
-            "graphic-preview-description": "Thumbnail",
             "creator": "RapidScat Project",
-            "title": "RapidScat Level 2A Surface Flagged Sigma-0 and Attenuations in 12.5km Swath Grid Version 2.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/RSCAT_L2A_12KM_V1.3.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset contains the Version 2.0 ISS-RapidScat on Level 2A 12.5 km science data record, which provides surface-flagged sigma-0 in 12.5 km Wind Vector Cells processed using the pulse \"slice\" Sigma-0 data provided by the Level 1B dataset. Due to the circular scan of the RapidScat instrument the expected number of Sigma-0 cells per WVC is not constant. To minimize the L2A data volume, the Sigma-0 cell data are stored as \"lists\" for each WVC row, with each list indexed by a \"cell_index\" array to indicate the cross-track WVC membership of the data. Each cell is then checked for land or ice and flagged accordingly. Attenuation corrections for each Sigma-0 measurement are also provided. Data are provided in single-orbit files in HDF-4 format. Version 2.0 represents a complete historical re-processing of the L2A data record (see the technical note for Version 2.0 under Documentation). RapidScat is a Ku-band dual beam circular rotating scatterometer retaining much of the same hardware and functionality of QuikSCAT, with exception of the antenna sub-system and digital interface to the International Space Station (ISS) Columbus module, which is where RapidScat is mounted. The NASA mission is officially referred to as ISS-RapidScat. Unlike QuikSCAT, ISS-RapidScat is not in sun-synchronous orbit, and flies at roughly half the altitude with a low inclination angle that restricts data coverage to the tropics and mid-latitude regions; the extent of latitudinal coverage stretches from approximately 61 degrees North to 61 degrees South. Furthermore, there is no consistent local time of day retrieval. If you have any questions or concerns, please visit our Forum at https://podaac.jpl.nasa.gov/forum/.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FRSX12-L2A20",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FRSX12-L2A20",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://manati.star.nesdis.noaa.gov/rscat_images/monitor/RapidScat_Scheduled_Outages.txt",
-                    "description": "Text file containing reverse chronological list of future scheduled outages and past outages. A start/stop date/time and description is provided for each outage. This list is maintained by NOAA/NESDIS to service near-real-time data users.",
                     "@type": "dcat:Distribution",
+                    "description": "Text file containing reverse chronological list of future scheduled outages and past outages. A start/stop date/time and description is provided for each outage. This list is maintained by NOAA/NESDIS to service near-real-time data users.",
+                    "downloadURL": "http://manati.star.nesdis.noaa.gov/rscat_images/monitor/RapidScat_Scheduled_Outages.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's documented anomalies"
                 },
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/rapidscat/open/L2A/docs/revtime.csv",
-                    "description": "ASCII CSV orbital revolution time tables with quality assurance information.",
                     "@type": "dcat:Distribution",
+                    "description": "ASCII CSV orbital revolution time tables with quality assurance information.",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/rapidscat/open/L2A/docs/revtime.csv",
+                    "mediaType": "text/csv",
                     "title": "View this dataset's documented anomalies"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://directory.eoportal.org/web/eoportal/satellite-missions/i/iss-rapidscat",
-                    "description": "Detailed background information on the ISS-RapidScat mission published by the eoPortal.",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed background information on the ISS-RapidScat mission published by the eoPortal.",
+                    "downloadURL": "https://directory.eoportal.org/web/eoportal/satellite-missions/i/iss-rapidscat",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://d2pn8kiwq2w21t.cloudfront.net/documents/issrapidscat_factsheet.pdf",
-                    "description": "Summary of Facts on the ISS-RapidScat Mission",
                     "@type": "dcat:Distribution",
+                    "description": "Summary of Facts on the ISS-RapidScat Mission",
+                    "downloadURL": "https://d2pn8kiwq2w21t.cloudfront.net/documents/issrapidscat_factsheet.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/RSCAT_L2A_12KM_V1.3.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/RSCAT_L2A_12KM_V1.3.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2633944131-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2633944131-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2633944131-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2633944131-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/rapidscat/open/L2A/docs/v2.0_technical_note.txt",
-                    "description": "Technical note for Version 2.0",
                     "@type": "dcat:Distribution",
+                    "description": "Technical note for Version 2.0",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/rapidscat/open/L2A/docs/v2.0_technical_note.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's processing history"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/RSCAT_L2A_12KM_V1.3.jpg",
+            "identifier": "C2633944131-POCLOUD",
+            "issued": "2016-09-28",
+            "keyword": [
+                "spectral/engineering",
+                "radar",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/RSX12-L2A20",
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
+            "release-place": "PO.DAAC",
+            "series-name": "RapidScat Level 2A Surface Flagged Sigma-0 and Attenuations in 12.5Km Swath Grid",
             "spatial": "-180.0 -61.0 180.0 61.0",
+            "temporal": "2014-10-03T00:00:00Z/2016-08-19T23:59:59.999Z",
             "theme": [
                 "ISS_RapidScat",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "RapidScat Level 2A Surface Flagged Sigma-0 and Attenuations in 12.5km Swath Grid Version 2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQR50-3WACS",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA Aquarius project. 2017-12-07. Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Annual Data. Version 5.0. Aquarius Sea Surface Salinity Products. Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC OBPG. https://doi.org/10.5067/AQR50-3WACS. http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius. NASA Aquarius project, NASA/GSFC OBPG, 2017-12-07, Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Annual Data V5.0, http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius.",
-            "issued": "2017-10-21",
-            "temporal": "2011-08-25T01:55:23Z/2015-06-07T12:45:21Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-07",
-            "keyword": [
-                "oceans",
-                "ocean winds",
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
-            "identifier": "C2491757171-POCLOUD",
-            "description": "Aquarius Level 3 ocean surface wind speed standard mapped image data contains gridded 1 degree spatial resolution wind speed data averaged over daily, 7 day, monthly, and seasonal time\nscales. This particular data set is the Annual wind speed product for version 5.0 of the Aquarius data set, which is the official end of mission public data release from the AQUARIUS/SAC-D mission. The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
-            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA",
-            "series-name": "Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Annual Data",
-            "graphic-preview-description": "Thumbnail",
             "creator": "NASA Aquarius project",
-            "title": "Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Annual Data V5.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_WIND_SPEED_SMI_ANNUAL_V5.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Aquarius Level 3 ocean surface wind speed standard mapped image data contains gridded 1 degree spatial resolution wind speed data averaged over daily, 7 day, monthly, and seasonal time\nscales. This particular data set is the Annual wind speed product for version 5.0 of the Aquarius data set, which is the official end of mission public data release from the AQUARIUS/SAC-D mission. The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3WACS",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3WACS",
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_WIND_SPEED_SMI_ANNUAL_V5.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_WIND_SPEED_SMI_ANNUAL_V5.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491757171-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491757171-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491757171-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491757171-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_WIND_SPEED_SMI_ANNUAL_V5.jpg",
+            "identifier": "C2491757171-POCLOUD",
+            "issued": "2017-10-21",
+            "keyword": [
+                "oceans",
+                "ocean winds",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQR50-3WACS",
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
+            "series-name": "Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Annual Data",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T01:55:23Z/2015-06-07T12:45:21Z",
             "theme": [
                 "AQUARIUS SAC-D",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Annual Data V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-RSS-5-CEGR-V3.0",
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
-                "1 ceres",
-                "dawn mission to vesta and ceres"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
```

