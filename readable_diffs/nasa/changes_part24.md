# Change History for nasa.json (Part 24)

### Changes from 31606f9 to dd2190f (Part 13/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
+            ],
+            "modified": "2017-04-14",
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
+                "https://doi.org/10.7927/H44B2Z74",
+                "https://doi.org/10.7927/H40K26HS",
+                "https://doi.org/10.7927/H4R20Z93",
+                "https://doi.org/10.7927/H4M906KR",
+                "https://doi.org/10.7927/H4GH9FVG",
+                "https://doi.org/10.7927/H4Z31WKF",
+                "https://doi.org/10.7927/H4GX48H5"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -58.0 180.0 85.0",
+            "temporal": "1990-07-01T00:00:00Z/2000-07-01T00:00:00Z",
             "theme": [
                 "GRUMP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Rural-Urban Mapping Project, Version 1 (GRUMPv1): Settlement Points, Revision 01"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0003",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2000-08-01. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/FIRE/0003.",
-            "issued": "2000-08-01",
-            "temporal": "1998-05-04T00:00:00Z/1998-07-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-02",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric radiation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRANCISCO VALERO",
                 "hasEmail": "mailto:fvalero@ucsd.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1000000940-LARC_ASDC",
             "description": "This data set consists of data provided by Scripps' Radiation Measurement System (RAMS) flown onboard the NCAR C-130 aircraft during the FIRE ACE field campaign.The First ISCCP Regional Experiments have been designed to improve data products and cloud/radiation parameterizations used in general circulation models (GCMs). Specifically, the goals of FIRE are (1) to improve basic understanding of the interaction of physical processes in determining life cycles of cirrus and marine stratocumulus systems and the radiative properties of these clouds during their life cycles and (2) to investigate the interrelationships between the ISCCP data, GCM parameterizations, and higher space and time resolution cloud data.",
-            "title": "First ISCCP Regional Experiment (FIRE) Arctic Cloud Experiment (ACE) Radiation Measurement System (RAMS)",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0003",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0003",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000940-LARC_ASDC",
-                    "description": "Earthdata Search for FIRE_ACE_C130_RAMS_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FIRE_ACE_C130_RAMS_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000940-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/read_fire_ace_c130_rams.pro",
-                    "description": "Readme to open and read FIRE-ACE RAMS tddr and bbr data files",
                     "@type": "dcat:Distribution",
+                    "description": "Readme to open and read FIRE-ACE RAMS tddr and bbr data files",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/read_fire_ace_c130_rams.pro",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/fire3_ace/ACEDOCS/data/c130_avhrr.pdf",
-                    "description": "C-130 Flight Tracks during FIRE- ACE, April - July 1998",
                     "@type": "dcat:Distribution",
+                    "description": "C-130 Flight Tracks during FIRE- ACE, April - July 1998",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/fire3_ace/ACEDOCS/data/c130_avhrr.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ace_c130_rams",
-                    "description": "FIRE_ACE_C130_RAMS Readme File",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE_ACE_C130_RAMS Readme File",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ace_c130_rams",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0003",
-                    "description": "DOI data set landing page for FIRE_ACE_C130_RAMS_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIRE_ACE_C130_RAMS_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0003",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_ACE_C130_RAMS/",
-                    "description": "ASDC Direct Data Download for FIRE_ACE_C130_RAMS_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIRE_ACE_C130_RAMS_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_ACE_C130_RAMS/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_ACE_C130_RAMS/contents.html",
-                    "description": "OPeNDAP data access for FIRE_ACE_C130_RAMS_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for FIRE_ACE_C130_RAMS_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_ACE_C130_RAMS/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1000000940-LARC_ASDC",
+            "issued": "2000-08-01",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0003",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>64.69 -169.12 64.69 -147.5 78.69 -147.5 78.69 -169.12 64.69 -169.12</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1998-05-04T00:00:00Z/1998-07-30T23:59:59.999Z",
             "theme": [
                 "FIRE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "First ISCCP Regional Experiment (FIRE) Arctic Cloud Experiment (ACE) Radiation Measurement System (RAMS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-ENGR1-V1.0",
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
-                "enceladus"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Cassini Radio Science Enceladus Gravity Experiment (ENGR1) Raw Data Archive is a time-ordered collection of radio science raw data acquired on February 16 and 17, 2005 during the Tour subphase of the Cassini mission",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-engr1-v1.0_488s-w433",
+            "issued": "2021-05-21",
+            "keyword": [
+                "cassini-huygens",
+                "enceladus"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-ENGR1-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-engr1-v1.0_488s-w433",
-            "description": "The Cassini Radio Science Enceladus Gravity Experiment (ENGR1) Raw Data Archive is a time-ordered collection of radio science raw data acquired on February 16 and 17, 2005 during the Tour subphase of the Cassini mission",
-            "title": "CASSINI RSS RAW DATA SET - ENGR1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI RSS RAW DATA SET - ENGR1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=HAY-A-NIRS-3-NIRSCAL-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set includes the 111,226 calibrated spectra of asteroid 25143 Itokawa returned by the Near-Infrared Spectrometer (NIRS) instrument of the Hayabusa mission. The data cover the Itokawa encounter phases of the mission, from Aug. 31 through November 24, 2005.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.hay-a-nirs-3-nirscal-v1.0_489e-w8uc",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "25143 itokawa",
                 "hayabusa",
                 "asteroid",
                 "calibration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=HAY-A-NIRS-3-NIRSCAL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.hay-a-nirs-3-nirscal-v1.0_489e-w8uc",
-            "description": "This data set includes the 111,226 calibrated spectra of asteroid 25143 Itokawa returned by the Near-Infrared Spectrometer (NIRS) instrument of the Hayabusa mission. The data cover the Itokawa encounter phases of the mission, from Aug. 31 through November 24, 2005.",
-            "title": "HAYABUSA NIRS CALIBRATED SPECTRA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "HAYABUSA NIRS CALIBRATED SPECTRA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-RADAR-V1.0",
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
+            "description": "This dataset is intended to include all asteroid radar detections. An entry for each detection reports radar cross-section and circular polarization, if known, as well as the year of observation and the reference in which the observations were reported. Observations which have not been published yet, or which have been reported only in an abstract, are included as an entry but with no data.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-radar-v1.0_489j-fnpc",
+            "issued": "2018-06-26",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-RADAR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-radar-v1.0_489j-fnpc",
-            "description": "This dataset is intended to include all asteroid radar detections. An entry for each detection reports radar cross-section and circular polarization, if known, as well as the year of observation and the reference in which the observations were reported. Observations which have not been published yet, or which have been reported only in an abstract, are included as an entry but with no data.",
-            "title": "ASTEROID RADAR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ASTEROID RADAR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-HAZCAM-5-SLOPE-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-hazcam-5-slope-ops-v1.0_48ar-xv9d",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars exploration rover",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-HAZCAM-5-SLOPE-OPS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-hazcam-5-slope-ops-v1.0_48ar-xv9d",
-            "description": "not applicable",
-            "title": "MER 1 MARS HAZARD AVOID CAMERA SLOPE RDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MER 1 MARS HAZARD AVOID CAMERA SLOPE RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67P-M09-STR-REFL-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units (normalized and thus without unit), acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-10-24T10:00:00.000 to 2014-11-21T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67p-m09-str-refl-v1.0_48at-6hra",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67P-M09-STR-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67p-m09-str-refl-v1.0_48at-6hra",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units (normalized and thus without unit), acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-10-24T10:00:00.000 to 2014-11-21T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP009 RDR-STR-REFL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP009 RDR-STR-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGN-V-RDRS-5-DIM-V1.0",
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
+            "description": "This data set contains the Magellan the FMAP, a full-resolution (75 meters/pixel) global mosaic, produced by the U.S. Geological Survey from Magellan F-BIDR data. The complete dataset consists of 340 quadrangles in Sinusoidal equal-area projection. Quadrangles extend approximately 12 degrees in latitude, except for those between 84 and 90 degrees North and South. Quadrangles near the equator extend 12 degrees in longitude longitudinal extent is increased to maintain a roughly constant number of samples.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgn-v-rdrs-5-dim-v1.0_48ck-p7j7",
+            "issued": "2021-05-21",
+            "keyword": [
+                "venus",
+                "magellan"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGN-V-RDRS-5-DIM-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgn-v-rdrs-5-dim-v1.0_48ck-p7j7",
-            "description": "This data set contains the Magellan the FMAP, a full-resolution (75 meters/pixel) global mosaic, produced by the U.S. Geological Survey from Magellan F-BIDR data. The complete dataset consists of 340 quadrangles in Sinusoidal equal-area projection. Quadrangles extend approximately 12 degrees in latitude, except for those between 84 and 90 degrees North and South. Quadrangles near the equator extend 12 degrees in longitude longitudinal extent is increased to maintain a roughly constant number of samples.",
-            "title": "MGN V RDRS DERIVED DIGITAL IMAGE MAP DATA RECORD V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MGN V RDRS DERIVED DIGITAL IMAGE MAP DATA RECORD V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1533",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Dashti, H., N.F. Glenn, L.P. Spaete, and N. Ilangakoon. 2018. Hyperspectral Imagery from AVIRIS-NG for Sites in ID and CA, USA, 2014 and 2015. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1533",
-            "issued": "2018-05-03",
-            "temporal": "2014-09-15T17:38:00Z/2015-06-13T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-15",
-            "keyword": [
-                "land surface",
-                "surface radiative properties",
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
-            "identifier": "C2765511853-ORNL_CLOUD",
             "description": "This dataset provides surface reflectance measured by the Airborne Visible/Infrared Imaging Spectrometer-Next Generation (AVIRIS-NG) instrument during flights over research sites in Idaho and California in 2014 and 2015. AVIRIS-NG measures reflected radiance at 5-nanometer (nm) intervals in the visible to shortwave infrared spectral range between 380 and 2510 nm. Measurements are radiometrically and geometrically calibrated and provided at 1-meter spatial resolution. The data include 72 flight lines covering long-term research sites in the Reynolds Creek Experimental Watershed in southwestern Idaho and Hollister in southeastern Idaho. Several flight lines from a site in the Inyo National Forest near Big Pine, California are included.",
-            "graphic-preview-description": "A portion of the quicklook image from flight line ang20150611t202652 over Reynolds Creek Experimental Watershed, southwestern Idaho on June 6, 2015. Center-pivot irrigation for agricultural land in the northeastern portion of the watershed. Flight altitude approximately 10,000 ft with clear weather.",
-            "title": "Hyperspectral Imagery from AVIRIS-NG for Sites in ID and CA, USA, 2014 and 2015",
-            "graphic-preview-file": "https://daac.ornl.gov/VEGETATION/guides/AVIRIS-NG_Data_Idaho_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1533",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1533",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/AVIRIS-NG_Data_Idaho/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/AVIRIS-NG_Data_Idaho/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/AVIRIS-NG_Data_Idaho.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/AVIRIS-NG_Data_Idaho.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1533",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1533",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/AVIRIS-NG_Data_Idaho/comp/AVIRIS-NG_Data_Idaho.pdf",
-                    "description": "Hyperspectral Imagery from AVIRIS-NG for sites in ID and CA, US, 2014 and 2015: AVIRIS-NG_Data_Idaho.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Hyperspectral Imagery from AVIRIS-NG for sites in ID and CA, US, 2014 and 2015: AVIRIS-NG_Data_Idaho.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/AVIRIS-NG_Data_Idaho/comp/AVIRIS-NG_Data_Idaho.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/AVIRIS-NG_Data_Idaho/comp/idaho_aviris_boundaries.zip",
-                    "description": "Hyperspectral Imagery from AVIRIS-NG for sites in ID and CA, US, 2014 and 2015: idaho_aviris_boundaries.zip",
                     "@type": "dcat:Distribution",
+                    "description": "Hyperspectral Imagery from AVIRIS-NG for sites in ID and CA, US, 2014 and 2015: idaho_aviris_boundaries.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/AVIRIS-NG_Data_Idaho/comp/idaho_aviris_boundaries.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/AVIRIS-NG_Data_Idaho/comp/idaho_aviris_quicklooks.zip",
-                    "description": "Hyperspectral Imagery from AVIRIS-NG for sites in ID and CA, US, 2014 and 2015: idaho_aviris_quicklooks.zip",
                     "@type": "dcat:Distribution",
+                    "description": "Hyperspectral Imagery from AVIRIS-NG for sites in ID and CA, US, 2014 and 2015: idaho_aviris_quicklooks.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/AVIRIS-NG_Data_Idaho/comp/idaho_aviris_quicklooks.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/AVIRIS-NG_Data_Idaho_Fig1.png",
-                    "description": "A portion of the quicklook image from flight line ang20150611t202652 over Reynolds Creek Experimental Watershed, southwestern Idaho on June 6, 2015. Center-pivot irrigation for agricultural land in the northeastern portion of the watershed. Flight altitude approximately 10,000 ft with clear weather.",
                     "@type": "dcat:Distribution",
+                    "description": "A portion of the quicklook image from flight line ang20150611t202652 over Reynolds Creek Experimental Watershed, southwestern Idaho on June 6, 2015. Center-pivot irrigation for agricultural land in the northeastern portion of the watershed. Flight altitude approximately 10,000 ft with clear weather.",
+                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/AVIRIS-NG_Data_Idaho_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "A portion of the quicklook image from flight line ang20150611t202652 over Reynolds Creek Experimental Watershed, southwestern Idaho on June 6, 2015. Center-pivot irrigation for agricultural land in the northeastern portion of the watershed. Flight altitude approximately 10,000 ft with clear weather.",
+            "graphic-preview-file": "https://daac.ornl.gov/VEGETATION/guides/AVIRIS-NG_Data_Idaho_Fig1.png",
+            "identifier": "C2765511853-ORNL_CLOUD",
+            "issued": "2018-05-03",
+            "keyword": [
+                "land surface",
+                "surface radiative properties",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1533",
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
             "spatial": "-118.41 36.57 -114.67 43.42",
+            "temporal": "2014-09-15T17:38:00Z/2015-06-13T23:59:59Z",
             "theme": [
                 "Vegetation",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Hyperspectral Imagery from AVIRIS-NG for Sites in ID and CA, USA, 2014 and 2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/TRACE-P/Aerosol_AircraftInSitu_DC8_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2024-09-06. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/TRACE-P/Aerosol_AircraftInSitu_DC8_Data_1.",
-            "issued": "2001-02-27",
-            "temporal": "1999-01-07T00:00:00Z/2002-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2001-04-10",
-            "keyword": [
-                "aerosols",
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
-            "identifier": "C2812939178-LARC_CLOUD",
             "description": "TRACE-P_Aerosol_AircraftInSitu_DC8_Data is the in-situ aerosol data collected onboard the DC-8 aircraft during the Transport and Chemical Evolution over the Pacific (TRACE-P) suborbital campaign. Data collection for this product is complete.\r\n\r\nThe NASA TRACE-P mission was a part of NASA\u2019s Global Tropospheric Experiment (GTE) \u2013 an assemblage of missions conducted from 1983-2001 with various research goals and objectives.\u202fTRACE-P was a multi-organizational campaign with NASA, the National Center for Atmospheric Research (NCAR), and several US universities.\u202fTRACE-P deployed\u202fits payloads in the Pacific between the months of March and April 2001 with the goal of studying the air chemistry emerging\u202ffrom Asia\u202fto the western Pacific.\u202fAlong with this, TRACE-P had the objective\u202fstudying\u202fthe chemical evolution of the air as it moved away from Asia.\u202f \r\n\r\nIn order to accomplish its goals, the NASA DC-8 aircraft and NASA P-3B aircraft were deployed, each equipped with various instrumentation.\u202fTRACE-P also relied on ground sites,\u202fand\u202fsatellites\u202fto collect data. The DC-8 aircraft was equipped with 19 instruments in total\u202fwhile the P-3B\u202fboasted\u202f21 total instruments.\u202fSome instruments on the DC-8 include the Nephelometer, the GCMS, the Nitric Oxide Chemiluminescence, the Differential Absorption Lidar (DIAL), and the Dual Channel Collectors and Fluorometers, HPLC. The Nephelometer was utilized to gather data on various\u202fwavelengths\u202fincluding\u202faerosol\u202fscattering\u202f(450, 550, 700nm), aerosol absorption (565nm), equivalent BC mass, and air density ratio. The GCMS was responsible for capturing a multitude of compounds in the atmosphere, some of which include CH4, CH3CHO, CH3Br, CH3Cl, CHBr3, and C2H6O.\u202fDIAL was used for a variety of measurements, some of which include aerosol wavelength dependence (1064/587nm), IR aerosol scattering ratio (1064nm),\u202ftropopause heights and ozone columns, visible aerosol scattering ratio, composite tropospheric ozone cross-sections, and visible aerosol depolarization. Finally, the Dual Channel Collectors and Fluorometers, HPLC collected data on H2O2, CH3OOH, and CH2O in the atmosphere.\u202fThe P-3B aircraft was equipped with various instruments for TRACE-P, some of which include\u202fthe MSA/CIMS, the Non-dispersive IR Spectrometer, the PILS-Ion Chromatograph, and the\u202fCondensation particle counter and Pulse Height Analysis (PHA). The\u202fMSA/CIMS measured OH, H2SO4, MSA, and HNO3. The Non-dispersive IR Spectrometer took measurements on CO2 in the atmosphere. The PILS-Ion Chromatograph recorded measurements of compounds and elements in the atmosphere, including sodium, calcium, potassium, magnesium, chloride, NH4, NO3, and SO4. Finally, the Condensation particle counter and PHA was used to gather data on total UCN, UCN 3-8nm, and UCN 3-4nm. Along with the aircrafts, ground stations measured air quality from China along with C2H2, C2H6, CO, and HCN.\u202fFinally, satellites imagery was used to collect a multitude of data, some of the uses were to observe the history of lightning flashes,\u202fSeaWiFS\u202fcloud imagery, 8-day exposure to TOMS aerosols, and\u202fSeaWiFS\u202faerosol optical thickness. The imagery was used to best aid in planning for the aircraft deployment.",
-            "title": "TRACE-P DC-8 In-Situ Aerosol Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FTRACE-P%2FAerosol_AircraftInSitu_DC8_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FTRACE-P%2FAerosol_AircraftInSitu_DC8_Data_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/tracep/tracep.htm",
-                    "description": "TRACE-P Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "TRACE-P Home Page",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/tracep/tracep.htm",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/tracep/WhitePaper.htm",
-                    "description": "TRACE-P White Paper",
                     "@type": "dcat:Distribution",
+                    "description": "TRACE-P White Paper",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/tracep/WhitePaper.htm",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/epdf/10.1029/2002JD003276",
-                    "description": "Transport and Chemical Evolution over the Pacific (TRACE-P)aircraft mission: Design, execution, and first results",
                     "@type": "dcat:Distribution",
+                    "description": "Transport and Chemical Evolution over the Pacific (TRACE-P)aircraft mission: Design, execution, and first results",
+                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/epdf/10.1029/2002JD003276",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2812939178-LARC_CLOUD",
-                    "description": "Earthdata Search for TRACE-P_Aerosol_AircraftInSitu_DC8_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TRACE-P_Aerosol_AircraftInSitu_DC8_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2812939178-LARC_CLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/TRACE-P/Aerosol_AircraftInSitu_DC8_Data_1",
-                    "description": "DOI data set landing page for TRACE-P_Aerosol_AircraftInSitu_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TRACE-P_Aerosol_AircraftInSitu_DC8_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/TRACE-P/Aerosol_AircraftInSitu_DC8_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2812939178-LARC_CLOUD",
+            "issued": "2001-02-27",
+            "keyword": [
+                "aerosols",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/TRACE-P/Aerosol_AircraftInSitu_DC8_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2001-04-10",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-180.0 6.89 180.0 45.7",
+            "temporal": "1999-01-07T00:00:00Z/2002-03-01T00:00:00Z",
             "theme": [
                 "TRACE-P",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TRACE-P DC-8 In-Situ Aerosol Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/614/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2012-08-29",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "nasa",
-                "dashlink",
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
-            "identifier": "DASHLINK_614",
             "description": "Slides presented at DXC'11 session of 22nd International Workshop on Principles of Diagnosis",
-            "title": "Third International Diagnostic Competition - DXC'11 Slides",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/unknown",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/DXC11_Slides_v1.pdf",
-                    "description": "DXC'11 Slides",
                     "@type": "dcat:Distribution",
+                    "description": "DXC'11 Slides",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/DXC11_Slides_v1.pdf",
+                    "mediaType": "application/unknown",
                     "title": "DXC11_Slides_v1.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_614",
+            "issued": "2012-08-29",
+            "keyword": [
+                "nasa",
+                "dashlink",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/614/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Third International Diagnostic Competition - DXC'11 Slides"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/7V38PNLVUNES",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "CLASIC07 In Situ Vegetation Data V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/7V38PNLVUNES.",
-            "issued": "2007-06-10",
-            "temporal": "2007-06-10T00:00:00Z/2007-07-03T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2007-07-03",
-            "keyword": [
-                "earth science",
-                "biosphere",
-                "vegetation"
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
-            "identifier": "C1000001425-NSIDC_ECS",
             "description": "This data set includes in situ vegetation data collected during the Cloud and Land Surface Interaction Campaign 2007 (CLASIC07) campaign. Sampling was designed to coincide with satellite overpasses, such as Landsat's Thematic Mapper (TM) 5 and the Moderate Resolution Imaging Spectroradiometer (MODIS) sensor on NASA's Terra satellite (MODIS/Terra), which can be then used to estimate vegetation water content on the regional scale.",
-            "title": "CLASIC07 In Situ Vegetation Data V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F7V38PNLVUNES",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F7V38PNLVUNES",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_VAL/CL07V.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_VAL/CL07V.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001425-NSIDC_ECS&m=25.751953125%21-97.716796875%214%211%210%210%2C2&q=CLASIC07&ok=CLASIC07",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001425-NSIDC_ECS&m=25.751953125%21-97.716796875%214%211%210%210%2C2&q=CLASIC07&ok=CLASIC07",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/CL07V/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/CL07V/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/7V38PNLVUNES",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/7V38PNLVUNES",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/7V38PNLVUNES",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/7V38PNLVUNES",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1000001425-NSIDC_ECS",
+            "issued": "2007-06-10",
+            "keyword": [
+                "earth science",
+                "biosphere",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.5067/7V38PNLVUNES",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2007-07-03",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-98.6 34.79 -97.95 35.21",
+            "temporal": "2007-06-10T00:00:00Z/2007-07-03T23:59:59.999Z",
             "theme": [
                 "CLASIC07",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CLASIC07 In Situ Vegetation Data V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-03-13",
-            "temporal": "2021-03-13T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "coords",
-                "coordinates",
-                "space",
-                "iss",
-                "location",
-                "topo",
-                "trajectory",
-                "international",
-                "ephemeris",
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
-            "identifier": "nasa-iss-data_2021-03-13",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2021-03-13",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -126161,1107 +126137,1133 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2021-03-13",
+            "issued": "2021-03-13",
+            "keyword": [
+                "coords",
+                "coordinates",
+                "space",
+                "iss",
+                "location",
+                "topo",
+                "trajectory",
+                "international",
+                "ephemeris",
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
+            "temporal": "2021-03-13T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2021-03-13"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.15770/EUM_SAF_OSI_NRT_2015",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "EUMETSAT/OSI SAF. 2019-04-10. GHRSST L3C OSISAF sub-skin SST v1.0 from GOES16 ABI in East position. Version 1.0. GHRSST L3C Hourly AMERICAS GOES16 sub-skin SST dataset. EUMETSAT Ocean and Sea Ice Satellite Application Facility, Lannion, France. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.15770/EUM_SAF_OSI_NRT_2015. https://osi-saf.eumetsat.int/. EUMETSAT/OSI SAF, EUMETSAT Ocean and Sea Ice Satellite Application Facility, Meteo-France/CMS, Lannion, France, 2019-04-10, GHRSST L3C OSISAF SSTskin dataset v1.0 from GOES16 ABI in East position (GDS V2), www.osi-saf.org.",
-            "issued": "2018-02-21",
-            "temporal": "2017-12-14T14:30:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-02-21",
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
-            "identifier": "C2036877806-POCLOUD",
-            "description": "The data is regional and part of the Group for High Resolution Sea Surface Temperature (GHRSST) Level 3 Collated (L3C) dataset covering the America Region based on retrievals from the Advanced Baseline Imager (ABI) on board the Geostationary Operational Environmental Satellite-16 (GOES-16). The European Organization for the Exploitation of Meteorological Satellites (EUMETSAT), Ocean and Sea Ice Satellite Application Facility (OSI SAF) is producing SST products in near real time from GOES-16 in the Eastern position. GOES-16 Imager level 1 data are acquired at M\u00e9t\u00e9o-France/Centre de M\u00e9t\u00e9orologie Spatiale (CMS) through the EUMETSAT/EUMETCast system. The GOES-16 ABI enables daytime SST calculations (whereas, previously, GOES East SST was restricted to nighttime conditions). The L3C SST is derived from a three-band (centered at 8.4, 10.3, and 12.3 um) algorithm. The ABI split-window configuration features three bands instead of the two found in heritage sensors (GOES-13). The 8.5-um is used in conjunction with the 10.3-um and 12.3-um bands for improved thin cirrus detection as well as for better atmospheric moisture correction in relatively dry atmospheres. Atmospheric profiles of water vapor and temperature from a numerical weather prediction model, together with a radiative transfer model, are used to correct the multispectral algorithm for regional and seasonal biases due to changing atmospheric conditions. Each 10-minute observation interval is processed at full satellite resolution. The operational products are then produced by remapping over a 0.05-degree regular grid (60S-60N and 135W-15W) SST fields obtained by aggregating the available10-minute SST data into hourly files-hour time, with priority being given to the value closest in time to the product nominal hour. The product format is compliant with the GHRSST Data Specification (GDS) version 2.",
-            "release-place": "EUMETSAT Ocean and Sea Ice Satellite Application Facility, Lannion, France",
-            "series-name": "GHRSST L3C OSISAF sub-skin SST v1.0 from GOES16 ABI in East position",
-            "graphic-preview-description": "Thumbnail",
             "creator": "EUMETSAT/OSI SAF",
-            "title": "GHRSST L3C hourly America Region sub-skin Sea Surface Temperature v1.0 from ABI on GOES16 produced by OSISAF",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GOES16-OSISAF-L3C-v1.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The data is regional and part of the Group for High Resolution Sea Surface Temperature (GHRSST) Level 3 Collated (L3C) dataset covering the America Region based on retrievals from the Advanced Baseline Imager (ABI) on board the Geostationary Operational Environmental Satellite-16 (GOES-16). The European Organization for the Exploitation of Meteorological Satellites (EUMETSAT), Ocean and Sea Ice Satellite Application Facility (OSI SAF) is producing SST products in near real time from GOES-16 in the Eastern position. GOES-16 Imager level 1 data are acquired at M\u00e9t\u00e9o-France/Centre de M\u00e9t\u00e9orologie Spatiale (CMS) through the EUMETSAT/EUMETCast system. The GOES-16 ABI enables daytime SST calculations (whereas, previously, GOES East SST was restricted to nighttime conditions). The L3C SST is derived from a three-band (centered at 8.4, 10.3, and 12.3 um) algorithm. The ABI split-window configuration features three bands instead of the two found in heritage sensors (GOES-13). The 8.5-um is used in conjunction with the 10.3-um and 12.3-um bands for improved thin cirrus detection as well as for better atmospheric moisture correction in relatively dry atmospheres. Atmospheric profiles of water vapor and temperature from a numerical weather prediction model, together with a radiative transfer model, are used to correct the multispectral algorithm for regional and seasonal biases due to changing atmospheric conditions. Each 10-minute observation interval is processed at full satellite resolution. The operational products are then produced by remapping over a 0.05-degree regular grid (60S-60N and 135W-15W) SST fields obtained by aggregating the available10-minute SST data into hourly files-hour time, with priority being given to the value closest in time to the product nominal hour. The product format is compliant with the GHRSST Data Specification (GDS) version 2.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.15770%2FEUM_SAF_OSI_NRT_2015",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.15770%2FEUM_SAF_OSI_NRT_2015",
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrsst.jpl.nasa.gov",
-                    "description": "GHRSST Global Data Assembly Center",
                     "@type": "dcat:Distribution",
+                    "description": "GHRSST Global Data Assembly Center",
+                    "downloadURL": "https://ghrsst.jpl.nasa.gov",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GOES16-OSISAF-L3C-v1.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GOES16-OSISAF-L3C-v1.0.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ghrsst.org",
-                    "description": "GHRSST Project Homepage",
                     "@type": "dcat:Distribution",
+                    "description": "GHRSST Project Homepage",
+                    "downloadURL": "https://www.ghrsst.org",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://osi-saf.eumetsat.int/lml/doc/osisaf_cdop3_ss1_pum_geo_sst.pdf",
-                    "description": "Product User Manual",
                     "@type": "dcat:Distribution",
+                    "description": "Product User Manual",
+                    "downloadURL": "https://osi-saf.eumetsat.int/lml/doc/osisaf_cdop3_ss1_pum_geo_sst.pdf",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2036877806-POCLOUD",
-                    "description": "Browse and download granules over HTTPS using the virtual directories",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2036877806-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2036877806-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2036877806-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://osi-saf.eumetsat.int/lml/doc/osisaf_cdop2_ss1_geo_sst_val_rep.pdf",
-                    "description": "Geostationary Satellite Sea Surface Temperature Scientific Validation Report",
                     "@type": "dcat:Distribution",
+                    "description": "Geostationary Satellite Sea Surface Temperature Scientific Validation Report",
+                    "downloadURL": "https://osi-saf.eumetsat.int/lml/doc/osisaf_cdop2_ss1_geo_sst_val_rep.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/OPeNDAP-in-the-Cloud",
-                    "description": "OPeNDAP Access for Data in the Cloud",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP Access for Data in the Cloud",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/OPeNDAP-in-the-Cloud",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GOES16-OSISAF-L3C-v1.0.jpg",
+            "identifier": "C2036877806-POCLOUD",
+            "issued": "2018-02-21",
+            "keyword": [
+                "ocean temperature",
+                "oceans",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.15770/EUM_SAF_OSI_NRT_2015",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-02-21",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "EUMETSAT Ocean and Sea Ice Satellite Application Facility, Lannion, France",
+            "series-name": "GHRSST L3C OSISAF sub-skin SST v1.0 from GOES16 ABI in East position",
             "spatial": "-135.0 -60.0 -15.0 60.0",
+            "temporal": "2017-12-14T14:30:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "GHRSST",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GHRSST L3C hourly America Region sub-skin Sea Surface Temperature v1.0 from ABI on GOES16 produced by OSISAF"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-LECP-4-SUMM-SECTOR-15MIN-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-lecp-4-summ-sector-15min-v1.0_48mz-3kci",
+            "issued": "2018-06-26",
+            "keyword": [
+                "voyager",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-LECP-4-SUMM-SECTOR-15MIN-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-lecp-4-summ-sector-15min-v1.0_48mz-3kci",
-            "description": "not applicable",
-            "title": "VG1 SAT LECP CALIBRATED RESAMPLED SECTORED 15MIN V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG1 SAT LECP CALIBRATED RESAMPLED SECTORED 15MIN V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IRAS-D-FPA-3-RDR-ZOHF-LOW-RES-V1.0",
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
-                "infrared astronomical satellite",
-                "dust"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The IRAS Low-Resolution (0.5 degree in-scan) Zodiacal Observational History File (ZOHF) consists of the time-ordered IRAS survey data averaged into 1/2 X 1/2 degree rectangular pixels along with pointing and timing information, covering the entire mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.iras-d-fpa-3-rdr-zohf-low-res-v1.0_48pc-e6vk",
+            "issued": "2018-06-26",
+            "keyword": [
+                "infrared astronomical satellite",
+                "dust"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IRAS-D-FPA-3-RDR-ZOHF-LOW-RES-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.iras-d-fpa-3-rdr-zohf-low-res-v1.0_48pc-e6vk",
-            "description": "The IRAS Low-Resolution (0.5 degree in-scan) Zodiacal Observational History File (ZOHF) consists of the time-ordered IRAS survey data averaged into 1/2 X 1/2 degree rectangular pixels along with pointing and timing information, covering the entire mission.",
-            "title": "IRAS LOW RESOLUTION ZODIACAL HISTORY FILE V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "IRAS LOW RESOLUTION ZODIACAL HISTORY FILE V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQUA/CERES/CRS_AQUA-FM4_L2.002B",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2008-03-18. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AQUA/CERES/CRS_AQUA-FM4_L2.002B.",
-            "issued": "2014-01-09",
-            "temporal": "2002-07-02T00:00:00Z/2005-03-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-09-29",
-            "keyword": [
-                "earth science",
-                "clouds",
-                "atmosphere",
-                "atmospheric radiation"
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
-            "identifier": "C4331632-LARC_ASDC",
             "description": "CER_CRS_Aqua-FM4-MODIS_Edition2B is the Clouds and the Earth's Radiant Energy System (CERES) Clouds and Radiative Swath (CRS) Aqua-Flight Model 4 (FM4) Moderate-Resolution Imaging Spectroradiometer (MODIS) Edition2B data product, which was collected using the CERES-FM4 instrument on the Aqua platform. Data collection for this product is complete. \r\n\r\nThe CRS product contains one hour of instantaneous Clouds and the Earth's Radiant Energy System (CERES) data for a single scanner instrument. The CRS contains all of the CERES SSF product data. For each CERES footprint on the SSF, the CRS also contains vertical flux profiles evaluated at four levels in the atmosphere: the surface, 500-, 70-, and 1-hPa. The CRS fluxes and cloud parameters are adjusted for consistency with a radiative transfer model and adjusted fluxes are evaluated at the four atmospheric levels for both clear-sky and total-sky.\r\n\r\nCERES is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions are a follow-on to the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument, protoflight model (PFM), was launched on November 27, 1997 as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the Earth Observing System (EOS) flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board Earth Observing System (EOS) Aqua on May 4, 2002. The CERES FM5 instrument was launched on board the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The newest CERES instrument (FM6) was launched on board the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite, now called NOAA-20, on November 18, 2017.",
-            "title": "CERES Clouds and Radiative Swath Aqua FM4 MODIS Edition2B",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQUA%2FCERES%2FCRS_AQUA-FM4_L2.002B",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQUA%2FCERES%2FCRS_AQUA-FM4_L2.002B",
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
-                    "downloadURL": "https://doi.org/10.5067/AQUA/CERES/CRS_AQUA-FM4_L2.002B",
-                    "description": "DOI data set landing page for CER_CRS_Aqua-FM4-MODIS_Edition2B",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CER_CRS_Aqua-FM4-MODIS_Edition2B",
+                    "downloadURL": "https://doi.org/10.5067/AQUA/CERES/CRS_AQUA-FM4_L2.002B",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C4331632-LARC_ASDC",
-                    "description": "Earthdata Search for CER_CRS_Aqua-FM4-MODIS_Edition2B (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CER_CRS_Aqua-FM4-MODIS_Edition2B (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C4331632-LARC_ASDC",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/quality_summaries/CER_CRS_Aqua_Edition2B.pdf",
-                    "description": "Quality Summary: CERES Aqua Edition 2B CRS",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Summary: CERES Aqua Edition 2B CRS",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/quality_summaries/CER_CRS_Aqua_Edition2B.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product quality assessment"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/CRS/Aqua-FM4-MODIS_Edition2B/",
-                    "description": "ASDC Direct Data Download for CER_CRS_Aqua-FM4-MODIS_Edition2B",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CER_CRS_Aqua-FM4-MODIS_Edition2B",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/CRS/Aqua-FM4-MODIS_Edition2B/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/CRS/Aqua-FM4-MODIS_Edition2B/contents.html",
-                    "description": "OPeNDAP data access for CER_CRS_Aqua-FM4-MODIS_Edition2B",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CER_CRS_Aqua-FM4-MODIS_Edition2B",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/CRS/Aqua-FM4-MODIS_Edition2B/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C4331632-LARC_ASDC",
+            "issued": "2014-01-09",
+            "keyword": [
+                "earth science",
+                "clouds",
+                "atmosphere",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQUA/CERES/CRS_AQUA-FM4_L2.002B",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-09-29",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2002-07-02T00:00:00Z/2005-03-30T23:59:59.999Z",
             "theme": [
                 "CERES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CERES Clouds and Radiative Swath Aqua FM4 MODIS Edition2B"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT5-3815-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2015-01-01 to 2016-12-31. It is a Occultation measurement and covers the time 2015-09-08T21:53:49 to 2015-09-09T06:35:22.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext5-3815-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars express"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT5-3815-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext5-3815-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2015-01-01 to 2016-12-31. It is a Occultation measurement and covers the time 2015-09-08T21:53:49 to 2015-09-09T06:35:22.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 5 3815 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 5 3815 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NSGDR-L2X02",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA/JPL/PO.DAAC. 1998-07-26. NSCAT Level 2 Ocean Wind Vectors. Version 2. NSCAT Level 2 Ocean Wind Vector Geophysical Data Record. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/JPL/PO.DAAC. https://doi.org/10.5067/NSGDR-L2X02. https://podaac-tools.jpl.nasa.gov/drive/files/allData/nscat/docs/nscat_manual.pdf. NASA/JPL/PO.DAAC, NASA/JPL/PO.DAAC, 1998-07-26, NSCAT Level 2 Ocean Wind Vector Geophysical Data Record, https://podaac-tools.jpl.nasa.gov/drive/files/allData/nscat/docs/nscat_manual.pdf.",
-            "issued": "2009-06-15",
-            "temporal": "1996-09-15T00:00:00Z/1997-06-29T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-04-28",
-            "keyword": [
-                "earth science",
-                "ocean winds",
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
-            "identifier": "C2617226657-POCLOUD",
-            "description": "The NASA Scatterometer (NSCAT) Level 2 ocean wind vectors in 50 km wind vector cell (WVC) swaths contain daily data from ascending and descending passes. Wind vectors are accurate to within 2 m/s (vector speed) and 20 degrees (vector direction). Wind vectors are not considered valid in rain contaminated regions; rain flags and precipitation information are not provided. Data is flagged where measurements are either missing, ambiguous, or contaminated by land/sea ice. Winds are calculated using the NSCAT-2 model function. This is the most up-to-date version, which designates the final phase of calibration, validation and science data processing, which was completed in November of 1998, on behalf of the JPL NSCAT Project; wind vectors are processed using the NSCAT-2 geophysical model function.",
-            "release-place": "PO.DAAC",
-            "series-name": "NSCAT Level 2 Ocean Wind Vectors",
-            "graphic-preview-description": "Thumbnail",
             "creator": "NASA/JPL/PO.DAAC",
-            "title": "NSCAT Level 2 Ocean Wind Vector Geophysical Data Record",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/NSCAT_LEVEL_2_V2.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The NASA Scatterometer (NSCAT) Level 2 ocean wind vectors in 50 km wind vector cell (WVC) swaths contain daily data from ascending and descending passes. Wind vectors are accurate to within 2 m/s (vector speed) and 20 degrees (vector direction). Wind vectors are not considered valid in rain contaminated regions; rain flags and precipitation information are not provided. Data is flagged where measurements are either missing, ambiguous, or contaminated by land/sea ice. Winds are calculated using the NSCAT-2 model function. This is the most up-to-date version, which designates the final phase of calibration, validation and science data processing, which was completed in November of 1998, on behalf of the JPL NSCAT Project; wind vectors are processed using the NSCAT-2 geophysical model function.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNSGDR-L2X02",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNSGDR-L2X02",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/nscat/open/docs/nscat_manual.pdf",
-                    "description": "Dataset User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Dataset User Guide",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/nscat/open/docs/nscat_manual.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/NSCAT_LEVEL_2_V2.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/NSCAT_LEVEL_2_V2.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L2/v2.1/README.txt",
-                    "description": "PO.DAAC Drive",
                     "@type": "dcat:Distribution",
+                    "description": "PO.DAAC Drive",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L2/v2.1/README.txt",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2617226657-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2617226657-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2617226657-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2617226657-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/NSCAT_LEVEL_2_V2.jpg",
+            "identifier": "C2617226657-POCLOUD",
+            "issued": "2009-06-15",
+            "keyword": [
+                "earth science",
+                "ocean winds",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/NSGDR-L2X02",
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
+            "series-name": "NSCAT Level 2 Ocean Wind Vectors",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1996-09-15T00:00:00Z/1997-06-29T23:59:59.999Z",
             "theme": [
                 "NSCAT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NSCAT Level 2 Ocean Wind Vector Geophysical Data Record"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-CAL-CONSERT-2-PDCS-V1.0",
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
+            "description": "This archive contains edited data (CODMAC level 2) from the CONSERT instrument onboard ROSETTA Orbiter and Lander, acquired  during PDCS mission phase (Pre Delivery Calib Science) during its journey to comet 67P/C-G. It also contains documentation which describes the CONSERT experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-cal-consert-2-pdcs-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "calibration",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-CAL-CONSERT-2-PDCS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-cal-consert-2-pdcs-v1.0",
-            "description": "This archive contains edited data (CODMAC level 2) from the CONSERT instrument onboard ROSETTA Orbiter and Lander, acquired  during PDCS mission phase (Pre Delivery Calib Science) during its journey to comet 67P/C-G. It also contains documentation which describes the CONSERT experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-ORBITER/ROSETTA-LANDER CAL CONSERT\n                           2 PDCS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER/ROSETTA-LANDER CAL CONSERT\n                           2 PDCS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Suborbital/LMOS/TraceGas_SurfaceMobile_EPA-GMAP_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2020-11-05. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/Suborbital/LMOS/TraceGas_SurfaceMobile_EPA-GMAP_Data_1.",
-            "issued": "2020-09-08",
-            "temporal": "2017-06-06T00:00:00Z/2017-06-13T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-19",
-            "keyword": [
-                "atmosphere",
-                "atmospheric chemistry",
-                "atmospheric winds",
-                "air quality",
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
-            "identifier": "C1966379610-LARC_ASDC",
             "description": "LMOS_TraceGas_SurfaceMobile_EPA-GMAP_Data_1 is the Lake Michigan Ozone Study (LMOS) trace gas surface mobile data collected via the Environmental Protection Agency (EPA) GMAP mobile platform during the LMOS field campaign. This product is a result of a joint effort across multiple agencies, including NASA, NOAA, the EPA, Electric Power Research Institute (EPRI), National Science Foundation (NSF), Lake Michigan Air Directors Consortium (LADCO) and its member states, and several research groups at universities. Data collection is complete.\r\n\r\nElevated spring and summertime ozone levels remain a challenge along the coast of Lake Michigan, with a number of monitors recording levels/amounts exceeding the 2015 National Ambient Air Quality Standards (NAAQS) for ozone. The production of ozone over Lake Michigan, combined with onshore daytime \u201clake breeze\u201d airflow is believed to increase ozone concentrations at locations within a few kilometers off shore. This observed lake-shore gradient motivated the Lake Michigan Ozone Study (LMOS). Conducted from May through June 2017, the goal of LMOS was to better understand ozone formation and transport around Lake Michigan; in particular, why ozone concentrations are generally highest along the lakeshore and drop off sharply inland and why ozone concentrations peak in rural areas far from major emission sources. LMOS was a collaborative, multi-agency field study that provided extensive observational air quality and meteorology datasets through a combination of airborne, ship, mobile laboratories, and fixed ground-based observational platforms. Chemical transport models (CTMs) and meteorological forecast tools assisted in planning for day-to-day measurement strategies. The long term goals of the LMOS field study were to improve modeled ozone forecasts for this region, better understand ozone formation and transport around Lake Michigan, provide a better understanding of the lakeshore gradient in ozone concentrations (which could influence how the Environmental Protection Agency (EPA) addresses future regional ozone issues), and provide improved knowledge of how emissions influence ozone formation in the region.",
-            "title": "LMOS Surface Mobile EPA-GMAP Ozone Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSuborbital%2FLMOS%2FTraceGas_SurfaceMobile_EPA-GMAP_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSuborbital%2FLMOS%2FTraceGas_SurfaceMobile_EPA-GMAP_Data_1",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/lmos/docs/LMOS_FAQ_rev_jun5.pdf",
-                    "description": "Lake Michigan Ozone Study (LMOS 2017) FAQ",
                     "@type": "dcat:Distribution",
+                    "description": "Lake Michigan Ozone Study (LMOS 2017) FAQ",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/lmos/docs/LMOS_FAQ_rev_jun5.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/lmos/docs/Great_Lakes_Ozone_Study_White_Paper_Draft_v6.pdf",
-                    "description": "White Paper: Lake Michigan Ozone Study 2017 (LMOS 2017)",
                     "@type": "dcat:Distribution",
+                    "description": "White Paper: Lake Michigan Ozone Study 2017 (LMOS 2017)",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/lmos/docs/Great_Lakes_Ozone_Study_White_Paper_Draft_v6.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/lmos/",
-                    "description": "LMOS Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "LMOS Project Home Page",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/lmos/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/Suborbital/LMOS/TraceGas_SurfaceMobile_EPA-GMAP_Data_1",
-                    "description": "DOI data set landing page for LMOS_TraceGas_SurfaceMobile_EPA-GMAP_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for LMOS_TraceGas_SurfaceMobile_EPA-GMAP_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/Suborbital/LMOS/TraceGas_SurfaceMobile_EPA-GMAP_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1966379610-LARC_ASDC",
-                    "description": "Earthdata Search for LMOS_TraceGas_SurfaceMobile_EPA-GMAP_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for LMOS_TraceGas_SurfaceMobile_EPA-GMAP_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1966379610-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www.ladco.org/wp-content/uploads/Research/LMOS2017/LMOS_LADCO_report_revision_apr2019_final.pdf",
-                    "description": "LMOS Lake Michigan Air Directors Consortium Mission Overview",
                     "@type": "dcat:Distribution",
+                    "description": "LMOS Lake Michigan Air Directors Consortium Mission Overview",
+                    "downloadURL": "https://www.ladco.org/wp-content/uploads/Research/LMOS2017/LMOS_LADCO_report_revision_apr2019_final.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/feature/langley/nasa-aids-study-of-lake-michigan-high-ozone-events",
-                    "description": "LMOS Nasa.gov \u201cNASA Aids Study of Lake Michigan High-Ozone Events\u201d Article",
                     "@type": "dcat:Distribution",
+                    "description": "LMOS Nasa.gov \u201cNASA Aids Study of Lake Michigan High-Ozone Events\u201d Article",
+                    "downloadURL": "https://www.nasa.gov/feature/langley/nasa-aids-study-of-lake-michigan-high-ozone-events",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/LMOS/2017",
-                    "description": "LMOS Data on the Sub-Orbital Order Tool (SOOT) Power User Interface (UI)",
                     "@type": "dcat:Distribution",
+                    "description": "LMOS Data on the Sub-Orbital Order Tool (SOOT) Power User Interface (UI)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/LMOS/2017",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/LMOS/pdocuments",
-                    "description": "LMOS Support Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "LMOS Support Documentation",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/LMOS/pdocuments",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/LMOS/TraceGas_SurfaceMobile_EPA-GMAP_Data_1/",
-                    "description": "ASDC Direct Data Download for LMOS_TraceGas_SurfaceMobile_EPA-GMAP_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for LMOS_TraceGas_SurfaceMobile_EPA-GMAP_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/LMOS/TraceGas_SurfaceMobile_EPA-GMAP_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1966379610-LARC_ASDC",
+            "issued": "2020-09-08",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "atmospheric winds",
+                "air quality",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Suborbital/LMOS/TraceGas_SurfaceMobile_EPA-GMAP_Data_1",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>40.0 -90.0 40.0 -85.0 45.0 -85.0 45.0 -90.0 40.0 -90.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2017-06-06T00:00:00Z/2017-06-13T23:59:59.999Z",
             "theme": [
                 "LMOS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LMOS Surface Mobile EPA-GMAP Ozone Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GOES-17/CERES/GEO_Ed4_SH_V01.2",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2018-08-08. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/GOES-17/CERES/GEO_Ed4_SH_V01.2. https://doi.org/10.5067/GOES-17/CERES/GEO_Ed4_SH_V01.2.",
-            "issued": "2018-05-24",
-            "temporal": "2020-02-29T00:00:00Z/2024-03-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-08-03",
-            "keyword": [
-                "clouds",
-                "earth science",
-                "atmosphere"
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
-            "identifier": "C1990752718-LARC_ASDC",
             "description": "CER_GEO_Ed4_GOE17_SH_V01.2 is the Satellite Cloud and Radiation Property retrieval System (SatCORPS) Clouds and the Earth's Radiant Energy System (CERES) Geostationary Satellite (GEO) Edition 4 Geostationary Operational Environmental Satellite 17 (GOES-17) over the Southern Hemisphere (SH) Version 1.2 data product. Data was collected using the Advanced Baseline Imager on the GOES-17 Platform. Data collection for this product is in progress. \r\n\r\nThis data set comprises cloud micro-physical and radiation properties derived hourly from GOES-17 geostationary satellite imager data using the Langley Research Center (LaRC) SATCORPS algorithms supporting the CERES project. Each active geostationary satellite's cloud microphysical and radiation properties are merged to create hourly global cloud properties that estimate fluxes between CERES instrument measurements to account for the changing diurnal cycle. The data set is arranged as files for each hour and in netCDF-4 format. The observations are at 4 km resolution (at nadir) and are sub-sampled to 8 km.\r\n\r\nCERES is a key Earth Observing System (EOS) program component. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions follow the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument, the proto flight model (PFM), was launched on November 27, 1997, as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit onboard the Earth Observing System (EOS) flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched onboard Earth Observing System (EOS) Aqua on May 4, 2002. The CERES FM5 instrument was launched onboard the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The newest CERES instrument (FM6) was launched onboard the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite, now called NOAA-20, on November 18, 2017.",
-            "graphic-preview-description": "Mission Logo",
-            "title": "SatCORPS CERES GEO Edition 4 GOES-17 Southern Hemisphere Version 1.2",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/ceres.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGOES-17%2FCERES%2FGEO_Ed4_SH_V01.2",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGOES-17%2FCERES%2FGEO_Ed4_SH_V01.2",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1990752718-LARC_ASDC",
-                    "description": "Earthdata Search for CER_GEO_Ed4_GOE17_SH_V01.2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CER_GEO_Ed4_GOE17_SH_V01.2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1990752718-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/GOES-17/CERES/GEO_Ed4_SH_V01.2",
-                    "description": "DOI data set landing page for CER_GEO_Ed4_GOE17_SH_V01.2",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CER_GEO_Ed4_GOE17_SH_V01.2",
+                    "downloadURL": "https://doi.org/10.5067/GOES-17/CERES/GEO_Ed4_SH_V01.2",
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
-                    "description": "CERES ATB",
                     "@type": "dcat:Distribution",
+                    "description": "CERES ATB",
+                    "downloadURL": "https://eospso.gsfc.nasa.gov/atbd-category/40",
+                    "mediaType": "text/html",
                     "title": "View this dataset's algorithm theoretical basis document"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/GEO/Edition4/GOE17_SH_V01.2/",
-                    "description": "ASDC Direct Data Download for CER_GEO_Ed4_GOE17_SH_V01.2",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CER_GEO_Ed4_GOE17_SH_V01.2",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/GEO/Edition4/GOE17_SH_V01.2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/GEO/Edition4/GOE17_SH_V01.2/contents.html",
-                    "description": "OPeNDAP data access for CER_GEO_Ed4_GOE17_SH_V01.2",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CER_GEO_Ed4_GOE17_SH_V01.2",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/GEO/Edition4/GOE17_SH_V01.2/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Mission Logo",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/ceres.png",
+            "identifier": "C1990752718-LARC_ASDC",
+            "issued": "2018-05-24",
+            "keyword": [
+                "clouds",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/GOES-17/CERES/GEO_Ed4_SH_V01.2",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-08-03",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-60.0 -180.0 -60.0 -90.0 0.0 -90.0 0.0 -180.0 -60.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2020-02-29T00:00:00Z/2024-03-27T00:00:00Z",
             "theme": [
                 "CERES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SatCORPS CERES GEO Edition 4 GOES-17 Southern Hemisphere Version 1.2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567832-USGS_LTA.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, DOI/USGS/EROS.",
-            "issued": "2019-09-20",
-            "temporal": "1970-01-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-03-25",
-            "keyword": [
-                "earth science",
-                "topography",
-                "land surface",
-                "surface radiative properties"
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
-            "identifier": "C1220567832-USGS_LTA",
             "description": "Mosaic data products, which are also available for Tri-Decadal Global Landsat Orthorectified TM and ETM+ Pan-sharpened data, and may be searched and downloaded through EarthExplorer.\n\nGround control points are fixed, and images have been registered to the Universal Transverse Mercator (UTM) map projection and coordinate system and the World Geodetic System 1984 (WGS84) datum. All image bands have been individually resampled, using a nearest neighbor algorithm. Positional accuracy on the final image product has a Root Mean Square Error of better than 100 meters (MSS) and 50 meters (TM and ETM+). The Landsat data were acquired and processed through a National Aeronautics and Space Administration (NASA) contract with Earth Satellite Corporation, Rockville, Maryland, and are part of NASA's Scientific Data Purchase program.\n\nWhen possible, data were collected when vegetation was at peak greenness. Peak greenness was determined from global 1-kilometer Advanced Very High Resolution Radiometer (AVHRR) Normalized Difference Vegetation Index (NDVI) data. When peak greenness data were not available, images from other times of the year were substituted.",
-            "title": "Thematic Mapper (TM) Mosaics (1984-1997)",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1220567832-USGS_LTA.html",
-                    "description": "View this dataset on the CMR (Common Metadata Repository)",
                     "@type": "dcat:Distribution",
+                    "description": "View this dataset on the CMR (Common Metadata Repository)",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1220567832-USGS_LTA.html",
+                    "mediaType": "text/html",
                     "title": "CMR"
                 }
             ],
+            "identifier": "C1220567832-USGS_LTA",
+            "issued": "2019-09-20",
+            "keyword": [
+                "earth science",
+                "topography",
+                "land surface",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567832-USGS_LTA.html",
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
+            "title": "Thematic Mapper (TM) Mosaics (1984-1997)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-RPCIES-2-AST1-V1.0",
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
-                "2867 steins"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains EDITED RAW DATA of the RPCIES instrument taken during the asteroid Steins encounter (AST1). Included are the data taken between 11 Jul 2008 and 06 Sep 2008.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-rpcies-2-ast1-v1.0_49au-74cs",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "2867 steins"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-RPCIES-2-AST1-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-rpcies-2-ast1-v1.0_49au-74cs",
-            "description": "This dataset contains EDITED RAW DATA of the RPCIES instrument taken during the asteroid Steins encounter (AST1). Included are the data taken between 11 Jul 2008 and 06 Sep 2008.",
-            "title": "ROSETTA-ORBITER STEINS RPCIES 2 AST1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER STEINS RPCIES 2 AST1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-UVIS-2-SPEC-V1.2",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-uvis-2-spec-v1.2_49bh-y3wg",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "janus",
                 "albiorix",
@@ -127296,543 +127298,517 @@
                 "titan",
                 "ymir"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-UVIS-2-SPEC-V1.2",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-uvis-2-spec-v1.2_49bh-y3wg",
-            "description": "Spectroscopy of Jupiter, Saturnian rings, atmospheres and satellites for determining chemical abundance, compositional albedo, aerosol profiling, ring reflected spectra and diffraction patterns.",
-            "title": "CASSINI ORBITER SATURN UVIS EDITED SPECTRA 1.2",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI ORBITER SATURN UVIS EDITED SPECTRA 1.2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/RSX12-L2B11",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "RapidScat Project. 2015-05-04. RapidScat Level 2B Ocean Wind Vectors in 12.5km Slice Composites. Version 1.1. RapidScat Level 2B Ocean Wind Vectors in 12.5km Slice Composites. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/RSX12-L2B11. http://www.jpl.nasa.gov/news/fact_sheets/issrapidscat_factsheet.pdf. RapidScat Project, PO.DAAC, 2015-05-04, RapidScat Level 2B Ocean Wind Vectors in 12.5km Slice Composites Version 1.1, http://www.jpl.nasa.gov/news/fact_sheets/issrapidscat_factsheet.pdf.",
-            "issued": "2015-04-15",
-            "temporal": "2014-10-03T19:28:21Z/2016-03-10T15:10:44Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-04-28",
-            "keyword": [
-                "ocean winds",
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
-            "identifier": "C2526576283-POCLOUD",
-            "description": "This dataset contains the RapidScat Level 2B 12.5km Version 1.1 science-quality ocean surface wind vectors. The Level 2B wind vectors are binned on a 12.5 km Wind Vector Cell (WVC) grid and processed using the Level 2A Sigma-0 dataset. RapidScat is a Ku-band dual beam circular rotating scatterometer retaining much of the same hardware and functionality of QuikSCAT, with exception of the antenna sub-system and digital interface to the International Space Station (ISS) Columbus module, which is where RapidScat is mounted. The NASA mission is officially referred to as ISS-RapidScat. Unlike QuikSCAT, ISS-RapidScat is not in sun-synchronous orbit, and flies at roughly half the altitude with a low inclination angle that restricts data coverage to the tropics and mid-latitude regions; the extent of latitudinal coverage stretches from approximately 61 degrees North to 61 degrees South. Furthermore, there is no consistent local time of day retrieval. This dataset is provided in a netCDF-3 file format that follows the netCDF-4 classic model (i.e., generated by the netCDF-4 API) and made available via FTP and OPeNDAP. For data access, please click on the \"Data Access\" tab above. This Version 1.1 dataset differs from the previous Version 1 dataset as follows: 1) A new neural network approach for high wind speeds provided rain corrections for the \"retrieve_wind_speed\" variable for wind speeds in excess of 15 m/s. 2) The data variables containing the number of measurements of each type for each wind vector cell have been corrected; these variables include \"number_in_aft\", \"number_in_fore\", \"number_out_aft\", and \"number_out_fore\". 3) The \"wind_obj\" data variable has been corrected to include the proper data for the conditional probability for the objective DIRTH function values. It is advised for users to avoid using the \"wind_obj\" variable in this dataset since it is minimally applicable and meant primarily for quality assurance; for users who wish to access the objective function values for each ambiguity, it is suggested to use only the \"ambiguity_obj\" variable. The \"wind_obj\" variable contains DIRTH probabilities (which are derived form the \"ambiguity_obj\" objective function values) in the range of 0 to 1 indicating the conditional probability that the true direction is within + or - 2.5 degrees of the retrieved wind direction given the observed backscatter measurements in the cell. If you have any questions, please contact podaac@podaac.jpl.nasa.gov",
-            "release-place": "PO.DAAC",
-            "series-name": "RapidScat Level 2B Ocean Wind Vectors in 12.5km Slice Composites",
-            "graphic-preview-description": "Thumbnail",
             "creator": "RapidScat Project",
-            "title": "RapidScat Level 2B Ocean Wind Vectors in 12.5km Slice Composites Version 1.1",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/RSCAT_LEVEL_2B_OWV_COMP_12_V1.1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset contains the RapidScat Level 2B 12.5km Version 1.1 science-quality ocean surface wind vectors. The Level 2B wind vectors are binned on a 12.5 km Wind Vector Cell (WVC) grid and processed using the Level 2A Sigma-0 dataset. RapidScat is a Ku-band dual beam circular rotating scatterometer retaining much of the same hardware and functionality of QuikSCAT, with exception of the antenna sub-system and digital interface to the International Space Station (ISS) Columbus module, which is where RapidScat is mounted. The NASA mission is officially referred to as ISS-RapidScat. Unlike QuikSCAT, ISS-RapidScat is not in sun-synchronous orbit, and flies at roughly half the altitude with a low inclination angle that restricts data coverage to the tropics and mid-latitude regions; the extent of latitudinal coverage stretches from approximately 61 degrees North to 61 degrees South. Furthermore, there is no consistent local time of day retrieval. This dataset is provided in a netCDF-3 file format that follows the netCDF-4 classic model (i.e., generated by the netCDF-4 API) and made available via FTP and OPeNDAP. For data access, please click on the \"Data Access\" tab above. This Version 1.1 dataset differs from the previous Version 1 dataset as follows: 1) A new neural network approach for high wind speeds provided rain corrections for the \"retrieve_wind_speed\" variable for wind speeds in excess of 15 m/s. 2) The data variables containing the number of measurements of each type for each wind vector cell have been corrected; these variables include \"number_in_aft\", \"number_in_fore\", \"number_out_aft\", and \"number_out_fore\". 3) The \"wind_obj\" data variable has been corrected to include the proper data for the conditional probability for the objective DIRTH function values. It is advised for users to avoid using the \"wind_obj\" variable in this dataset since it is minimally applicable and meant primarily for quality assurance; for users who wish to access the objective function values for each ambiguity, it is suggested to use only the \"ambiguity_obj\" variable. The \"wind_obj\" variable contains DIRTH probabilities (which are derived form the \"ambiguity_obj\" objective function values) in the range of 0 to 1 indicating the conditional probability that the true direction is within + or - 2.5 degrees of the retrieved wind direction given the observed backscatter measurements in the cell. If you have any questions, please contact podaac@podaac.jpl.nasa.gov",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FRSX12-L2B11",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FRSX12-L2B11",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://podaac.jpl.nasa.gov/dataset/RSCAT_LEVEL_2B_OWV_CLIM_12_V1",
-                    "description": "Access to Climate quality L2B data record.",
                     "@type": "dcat:Distribution",
+                    "description": "Access to Climate quality L2B data record.",
+                    "downloadURL": "http://podaac.jpl.nasa.gov/dataset/RSCAT_LEVEL_2B_OWV_CLIM_12_V1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/allData/rapidscat/ancillary/revtime.csv",
-                    "description": "ASCII CSV orbital revolution time tables with quality assurance information.",
                     "@type": "dcat:Distribution",
+                    "description": "ASCII CSV orbital revolution time tables with quality assurance information.",
+                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/allData/rapidscat/ancillary/revtime.csv",
+                    "mediaType": "text/csv",
                     "title": "View this dataset's documented anomalies"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/rapidscat/open/L2B12/docs/rscat_l2b_user_guide_v1.pdf",
-                    "description": "User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "User Guide",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/rapidscat/open/L2B12/docs/rscat_l2b_user_guide_v1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://winds.jpl.nasa.gov/missions/RapidScat/",
-                    "description": "Website providing more detailed information about the ISS-RapidScat Mission.",
                     "@type": "dcat:Distribution",
+                    "description": "Website providing more detailed information about the ISS-RapidScat Mission.",
+                    "downloadURL": "https://winds.jpl.nasa.gov/missions/RapidScat/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/RSCAT_LEVEL_2B_OWV_COMP_12_V1.1.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/RSCAT_LEVEL_2B_OWV_COMP_12_V1.1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
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
-                    "downloadURL": "http://www.jpl.nasa.gov/news/fact_sheets/issrapidscat_factsheet.pdf",
-                    "description": "Summary of Facts on the ISS-RapidScat Mission",
                     "@type": "dcat:Distribution",
+                    "description": "Summary of Facts on the ISS-RapidScat Mission",
+                    "downloadURL": "http://www.jpl.nasa.gov/news/fact_sheets/issrapidscat_factsheet.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/rapidscat/open/L2B12/v1.1/README.txt",
-                    "description": "README file",
                     "@type": "dcat:Distribution",
+                    "description": "README file",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/rapidscat/open/L2B12/v1.1/README.txt",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2526576283-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2526576283-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2526576283-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2526576283-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/RSCAT_LEVEL_2B_OWV_COMP_12_V1.1.jpg",
+            "identifier": "C2526576283-POCLOUD",
+            "issued": "2015-04-15",
+            "keyword": [
+                "ocean winds",
+                "oceans",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/RSX12-L2B11",
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
+            "series-name": "RapidScat Level 2B Ocean Wind Vectors in 12.5km Slice Composites",
             "spatial": "-180.0 -61.0 180.0 61.0",
+            "temporal": "2014-10-03T19:28:21Z/2016-03-10T15:10:44Z",
             "theme": [
                 "ISS_RapidScat",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "RapidScat Level 2B Ocean Wind Vectors in 12.5km Slice Composites Version 1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2OCSNS.008",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2004-07-15. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AURA/TES/TL2OCSNS.008. https://asdc.larc.nasa.gov/project/TES.",
-            "issued": "2019-02-27",
-            "temporal": "2004-09-13T00:00:00Z/2018-01-22T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "air quality",
-                "atmosphere",
-                "earth science",
-                "atmospheric chemistry"
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
-            "identifier": "C1618264471-LARC",
             "description": "TL2OCSNS_8 is the Tropospheric Emission Spectrometer (TES)/Aura Level 2 Atmospheric Temperatures Limb Version 8 data product. TES was an instrument aboard NASA's Aura satellite and was launched from California on July 15, 2004. Data collection for TES is complete. It consisted of information for one molecular species for an entire Global Survey or Special Observation. TES Level 2 data contained retrieved species (or temperature) profiles at the observation targets and the estimated errors. The geolocation, quality and other data (e.g., surface characteristics for nadir observations) were also provided. L2 modeled spectra were evaluated using radiative transfer modeling algorithms. The process, referred to as retrieval, compared observed spectra to the modeled spectra and iteratively updated the atmospheric parameters. L2 standard product files included information for one molecular species (or temperature) for an entire global survey or special observation run. A global survey consisted of a maximum of 16 consecutive orbits. Nadir and limb observations were in separate L2 files, and a single ancillary file was composed of data that are common to both nadir and limb files. \r\rA nadir sequence within the TES Global Survey was a fixed number of observations within an orbit for a Global Survey. Prior to April 24, 2005, it consisted of two low resolution scans over the same ground locations. After April 24, 2005, Global Survey data consisted of three low resolution scans. The Nadir standard product consists of four files, where each file is composed of the Global Survey Nadir observations from one of four focal planes for a single orbit, i.e. 72 orbit sequences. The Global Survey Nadir observations only used a single set of filter mix. A Global Survey consists of observations along 16 consecutive orbits at the start of a two day cycle, over which 3,200 retrievals were performed. Each observation was the input for retrievals of species volume mixing ratios (VMRs), temperature profiles, surface temperature and other data parameters with associated pressure levels, precision, total error, vertical resolution, total column density and other diagnostic quantities. Each TES Level 2 standard product reported information in a swath format conforming to the HDF-EOS Aura File Format Guidelines. Each Swath object wa bounded by the number of observations in a global survey and a predefined set of pressure levels representing slices through the atmosphere. Each standard product could have had a variable number of observations depending upon the Global Survey configuration and whether averaging is employed. Also, missing or bad retrievals were not reported. \r\rThe organization of data within the Swath object was based on a superset of the Upper Atmosphere Research Satellite (UARS) pressure levels that was used to report concentrations of trace atmospheric gases. The reporting grid was the same pressure grid used for modeling. There were 67 reporting levels from 1211.53 hPa, which allowed for very high surface pressure conditions, to 0.1 hPa, about 65 km. In addition, the products reported values directly at the surface when possible or at the observed cloud top level. Thus in the Standard Product files each observation could potentially contain estimates for the concentration of a particular molecule at 67 different pressure levels within the atmosphere. However, for most retrieved profiles, the highest pressure levels were not observed due to a surface at lower pressure or cloud obscuration. For pressure levels corresponding to altitudes below the cloud top or surface, where measurements were not possible, a fill value was applied.\r\rTo minimize the duplication of information between the individual species standard products, data fields common to each species (such as spacecraft coordinates, emissivity, and other data fields) have been collected into a separate standard product, termed the TES L2 Ancillary Data product (ESDT short name: TL2ANC). U",
-            "title": "TES/Aura L2 Carbonyl Sulfide Nadir Special Observation V008",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2OCSNS.008",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2OCSNS.008",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/cgi-bin/DUE/tes_L2GlbSrvy.cgi",
-                    "description": "Report of TES Level 2 Global Survey Products Available from the ASDC",
                     "@type": "dcat:Distribution",
+                    "description": "Report of TES Level 2 Global Survey Products Available from the ASDC",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/cgi-bin/DUE/tes_L2GlbSrvy.cgi",
+                    "mediaType": "text/html",
                     "title": "View this dataset's production history"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/README_L2_ReadSoftware.txt",
-                    "description": "Basic IDL Tools for extraction information from TES L2 HDF Product files",
                     "@type": "dcat:Distribution",
+                    "description": "Basic IDL Tools for extraction information from TES L2 HDF Product files",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/README_L2_ReadSoftware.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
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
-                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2OCSNS.008",
-                    "description": "DOI data set landing page for TL2OCSNS_8",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TL2OCSNS_8",
+                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2OCSNS.008",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2OCSNS.008/contents.html",
-                    "description": "OPeNDAP data access for TL2OCSNS_8",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for TL2OCSNS_8",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2OCSNS.008/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1618264471-LARC",
-                    "description": "Earthdata Search for TL2OCSNS_8 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TL2OCSNS_8 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1618264471-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2OCSNS.008/",
-                    "description": "ASDC Direct Data Download for TL2OCSNS_8",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for TL2OCSNS_8",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2OCSNS.008/",
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/archive_reports.html",
-                    "description": "ASDC List of TES Archive Reports",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC List of TES Archive Reports",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/archive_reports.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/tes_quality_statements.html",
-                    "description": "ASDC List of TES Quality Statements",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC List of TES Quality Statements",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/tes_quality_statements.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data quality document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/DPS.html",
-                    "description": "ASDC List of TES Data Products Specifications",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC List of TES Data Products Specifications",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/DPS.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product usage"
                 }
             ],
+            "identifier": "C1618264471-LARC",
+            "issued": "2019-02-27",
+            "keyword": [
+                "air quality",
+                "atmosphere",
+                "earth science",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2OCSNS.008",
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
+            "title": "TES/Aura L2 Carbonyl Sulfide Nadir Special Observation V008"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2292",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Joiner, J., Y. Yoshida, P. Koehler, C. Frankenberg, and N.C. Parazoo. 2023. L2 Daily Solar-Induced Fluorescence (SIF) from MetOp-A GOME-2, 2007-2018, V2. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2292",
-            "issued": "2024-01-25",
-            "temporal": "2007-02-01T00:29:17Z/2018-02-01T00:32:43Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-01-30",
-            "keyword": [
-                "surface radiative properties",
-                "vegetation",
-                "biosphere",
-                "earth science",
-                "ecological dynamics",
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
-            "identifier": "C2847115945-ORNL_CLOUD",
             "description": "This dataset provides Level 2 (L2) Solar-Induced Fluorescence (SIF) of chlorophyll estimates derived from the Global Ozone Monitoring Experiment 2 (GOME-2) instrument on the European Meteorological Satellite (EUMETSAT) MetOp-A with ~0.5 nm spectral resolution and wavelengths between 734 and 758 nm. GOME-2 covers global land on an orbital basis at a resolution of approximately 40 km x 80 km (before 15 July 2013) or 40 km x 40 km (since 15 July 2013). Data are provided for the period from 2007-02-01 to 2018-02-01. Each file contains daily raw and bias-adjusted solar-induced fluorescence, quality control information, and ancillary data. SIF measurements can provide information on vegetation's functional status, including light-use efficiency and global primary productivity, which can be used for global carbon cycle modeling and agricultural applications. The GOME-2 SIF product is inherently noisy due to low signal levels and has undergone only a limited amount of validation. The data are provided in netCDF format.",
-            "graphic-preview-description": "Monthly mean solar-induced fluorescence (SIF) values (mW m-2 nm-1 sr-1) at 740 nm and gridded at 0.5-degree spatial resolution, derived from this L2 dataset.",
-            "title": "L2 Daily Solar-Induced Fluorescence (SIF) from MetOp-A GOME-2, 2007-2018, V2",
-            "graphic-preview-file": "https://daac.ornl.gov/SIF-ESDR/guides/MetOpA_GOME2_SIF_V2_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2292",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2292",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/sif-esdr/17-MEASURES-0032/MetOpA_GOME2_SIF_V2/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/sif-esdr/17-MEASURES-0032/MetOpA_GOME2_SIF_V2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/SIF-ESDR/guides/MetOpA_GOME2_SIF_V2.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/SIF-ESDR/guides/MetOpA_GOME2_SIF_V2.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2292",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2292",
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
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/sif-esdr/17-MEASURES-0032/MetOpA_GOME2_SIF_V2/comp/MetOpA_GOME2_SIF_V2.pdf",
-                    "description": "L2 Daily Solar-Induced Fluorescence (SIF) from MetOp-A GOME-2, 2007-2018, V2: MetOpA_GOME2_SIF_V2.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "L2 Daily Solar-Induced Fluorescence (SIF) from MetOp-A GOME-2, 2007-2018, V2: MetOpA_GOME2_SIF_V2.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/sif-esdr/17-MEASURES-0032/MetOpA_GOME2_SIF_V2/comp/MetOpA_GOME2_SIF_V2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/SIF-ESDR/guides/MetOpA_GOME2_SIF_V2_Fig1.png",
-                    "description": "Monthly mean solar-induced fluorescence (SIF) values (mW m-2 nm-1 sr-1) at 740 nm and gridded at 0.5-degree spatial resolution, derived from this L2 dataset.",
                     "@type": "dcat:Distribution",
+                    "description": "Monthly mean solar-induced fluorescence (SIF) values (mW m-2 nm-1 sr-1) at 740 nm and gridded at 0.5-degree spatial resolution, derived from this L2 dataset.",
+                    "downloadURL": "https://daac.ornl.gov/SIF-ESDR/guides/MetOpA_GOME2_SIF_V2_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://science.jpl.nasa.gov/projects/measures/",
-                    "description": "Project site",
                     "@type": "dcat:Distribution",
+                    "description": "Project site",
+                    "downloadURL": "https://science.jpl.nasa.gov/projects/measures/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "graphic-preview-description": "Monthly mean solar-induced fluorescence (SIF) values (mW m-2 nm-1 sr-1) at 740 nm and gridded at 0.5-degree spatial resolution, derived from this L2 dataset.",
+            "graphic-preview-file": "https://daac.ornl.gov/SIF-ESDR/guides/MetOpA_GOME2_SIF_V2_Fig1.png",
+            "identifier": "C2847115945-ORNL_CLOUD",
+            "issued": "2024-01-25",
+            "keyword": [
+                "surface radiative properties",
+                "vegetation",
+                "biosphere",
+                "earth science",
+                "ecological dynamics",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2292",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-01-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-180.0 -89.78 180.0 89.6",
+            "temporal": "2007-02-01T00:29:17Z/2018-02-01T00:32:43Z",
             "theme": [
                 "SIF-ESDR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "L2 Daily Solar-Induced Fluorescence (SIF) from MetOp-A GOME-2, 2007-2018, V2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GPM/GMI/GPM/1B/07",
             "citation": "GPM Science Team. 2022-05-09. GPM_1BGMI. GPM GMI Brightness Temperatures L1B 1.5 hours 13 km V07. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/GMI/GPM/1B/07. https://disc.gsfc.nasa.gov/datacollection/GPM_1BGMI_07.html. Digital Science Data.",
-            "issued": "2022-05-09",
-            "temporal": "2014-03-04T00:00:00Z/2023-02-28T00:00:00Z",
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
                 "fn": "CHRISTOPHER COHOON",
                 "hasEmail": "mailto:helpdesk@pps-mail.nascom.nasa.gov"
             },
+            "creator": "GPM Science Team",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2259345403-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Version 07 is the current version of the data set. Older versions will no longer be available and have been superseded by Version 07.\n\nThe 1BGMI algorithm uses a non-linear three-point in-flight calibration to derive antenna temperature (Ta) and convert Ta to Tb using GMI antenna pattern corrections. The four-point calibration, which utilizes noise diode measurements, is used to monitor the sensor non-linearty. The noise diode measurements also provide a hot load back-up calibration in case hot load measurements are lost. Details are in the GMI ATBD. The 1BGMI algorithm and software transform Level 0 counts into geolocated and calibrated brightness temperatures (Tb) for 13 GMI channels.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "GPM_1BGMI",
-            "creator": "GPM Science Team",
-            "title": "GPM GMI Brightness Temperatures L1B 1.5 hours 13 km V07 (GPM_1BGMI) at GES DISC",
-            "graphic-preview-description": "Brightness Temperature from GPM GMI for 06/15/2016 (GPM_1BGMI)",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GPM_1BGMI_05.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FGMI%2FGPM%2F1B%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FGMI%2FGPM%2F1B%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GPM_1BGMI_05.png",
-                    "description": "Brightness Temperature from GPM GMI for 06/15/2016 (GPM_1BGMI)",
                     "@type": "dcat:Distribution",
+                    "description": "Brightness Temperature from GPM GMI for 06/15/2016 (GPM_1BGMI)",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GPM_1BGMI_05.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_1BGMI_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_1BGMI_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L1B/GPM_1BGMI.07/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L1B/GPM_1BGMI.07/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_1BGMI_07",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_1BGMI_07",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L1B/GPM_1BGMI.07/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L1B/GPM_1BGMI.07/contents.html",
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
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L1B/doc/README.GPM.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L1B/doc/README.GPM.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
@@ -127842,413 +127818,409 @@
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://gpmweb2https.pps.eosdis.nasa.gov/pub/GPMfilespec/filespec.GPM.pdf",
-                    "description": "FILE SPECIFICATION DOCUMENT",
                     "@type": "dcat:Distribution",
+                    "description": "FILE SPECIFICATION DOCUMENT",
+                    "downloadURL": "https://gpmweb2https.pps.eosdis.nasa.gov/pub/GPMfilespec/filespec.GPM.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://arthurhou.pps.eosdis.nasa.gov/Documents/ReleaseNotesofGPM_Version07_GMI_TMI_BASE_1B_2.pdf",
-                    "description": "Release Notes",
                     "@type": "dcat:Distribution",
+                    "description": "Release Notes",
+                    "downloadURL": "https://arthurhou.pps.eosdis.nasa.gov/Documents/ReleaseNotesofGPM_Version07_GMI_TMI_BASE_1B_2.pdf",
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
-                    "downloadURL": "https://pps.gsfc.nasa.gov/gpminstruments.html",
-                    "description": "Instrument Description",
                     "@type": "dcat:Distribution",
+                    "description": "Instrument Description",
+                    "downloadURL": "https://pps.gsfc.nasa.gov/gpminstruments.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Brightness Temperature from GPM GMI for 06/15/2016 (GPM_1BGMI)",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GPM_1BGMI_05.png",
+            "identifier": "C2259345403-GES_DISC",
+            "issued": "2022-05-09",
+            "keyword": [
+                "atmospheric water vapor",
+                "atmosphere",
+                "precipitation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/GMI/GPM/1B/07",
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
+            "series-name": "GPM_1BGMI",
             "spatial": "-180.0 -70.0 180.0 70.0",
+            "temporal": "2014-03-04T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "GPM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM GMI Brightness Temperatures L1B 1.5 hours 13 km V07 (GPM_1BGMI) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FCAL-ALICE-4-EXT1-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains CODMAC Level 4 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the comet 67P/Churyumov-Gerasimenko Rosetta Extension 1 mission phase, which took place between 2016-01-01 and 2016-04-05.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cal-alice-4-ext1-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "calibration",
                 "67p/churyumov-gerasimenko 1 (1969 r1)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FCAL-ALICE-4-EXT1-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cal-alice-4-ext1-v1.0",
-            "description": "This data set contains CODMAC Level 4 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the comet 67P/Churyumov-Gerasimenko Rosetta Extension 1 mission phase, which took place between 2016-01-01 and 2016-04-05.",
-            "title": "ROSETTA-ORBITER 67P/CAL ALICE 4 EXT1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P/CAL ALICE 4 EXT1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/888",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Asner, G.P., M.M. Keller, R.J.R. Pereira, J.C. Zweede, and J.N.M. Silva. 2008. LBA-ECO LC-13 GIS Coverages of Logged Areas, Juruena, Mato Grosso, Brazil: 2002. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/888",
-            "issued": "2023-10-03",
-            "temporal": "2002-11-12T00:00:00Z/2002-11-15T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-04",
-            "keyword": [
-                "landscape",
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
-            "identifier": "C2777369863-ORNL_CLOUD",
             "description": "This data set contains GIS coverages constructed from measurements taken of  logged areas in Juruena, Mato Grosso. Classes include roads, skids trails, tree crowns, tree-fall locations, and block boundary (Asner et al., 2004). Coverages are in ArcInfo SHAPE format (*.shp), UTM projection, using the WGS84 datum.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO LC-13 GIS Coverages of Logged Areas, Juruena, Mato Grosso, Brazil: 2002",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F888",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F888",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC13_GIS_Juruena/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC13_GIS_Juruena/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC13_GIS_Juruena.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC13_GIS_Juruena.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/888",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/888",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC13_GIS_Juruena/comp/LC13_GIS_Juruena.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC13_GIS_Juruena/comp/LC13_GIS_Juruena.pdf",
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
+            "identifier": "C2777369863-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "landscape",
+                "land surface",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/888",
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
+            "temporal": "2002-11-12T00:00:00Z/2002-11-15T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO LC-13 GIS Coverages of Logged Areas, Juruena, Mato Grosso, Brazil: 2002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-GWE-8-NULL-RESULTS-V1.0",
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
-                "ulysses",
-                "jupiter"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The GWE instrument did not gather any meaningful data during the Ulysses Jupiter Encounter.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-gwe-8-null-results-v1.0_49ii-rmfj",
+            "issued": "2021-05-21",
+            "keyword": [
+                "ulysses",
+                "jupiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-GWE-8-NULL-RESULTS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-gwe-8-null-results-v1.0_49ii-rmfj",
-            "description": "The GWE instrument did not gather any meaningful data during the Ulysses Jupiter Encounter.",
-            "title": "ULY JUPITER GRAVITATIONAL WAVE\n                                        EXPERIMENT NULL RESULTS",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ULY JUPITER GRAVITATIONAL WAVE\n                                        EXPERIMENT NULL RESULTS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0362-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-10-15T15:26:50.000 to 2014-10-15T22:52:33.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0362-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0362-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0362-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-10-15T15:26:50.000 to 2014-10-15T22:52:33.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0362 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0362 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/B28FM2QVVYWY",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MEaSUREs Greenland Ice Velocity: Selected Glacier Site Single-Pair Velocity Maps from Optical Images V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/B28FM2QVVYWY.",
-            "issued": "2016-01-01",
-            "temporal": "2016-01-01T00:00:00Z/2023-12-29T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-12-29",
-            "keyword": [
-                "earth science",
-                "snow/ice",
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
-            "identifier": "C2363258255-NSIDC_ECS",
             "description": "This data set, part of the NASA Making Earth System Data Records for Use in Research Environments (MEaSUREs) program, consists of surface velocity estimates for selected Greenland Ice Sheet outlet glaciers. Velocity fields were generated by tracking visible features in optical images acquired by the U.S. Geological Survey (USGS) Landsat 8 Operational Land Imager (OLI) and the European Space Agency (ESA) Copernicus Sentinel-2A and Sentinel-2B satellites.",
-            "title": "MEaSUREs Greenland Ice Velocity: Selected Glacier Site Single-Pair Velocity Maps from Optical Images V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FB28FM2QVVYWY",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FB28FM2QVVYWY",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MEASURES/NSIDC-0777.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MEASURES/NSIDC-0777.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=NSIDC-0777+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=NSIDC-0777+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0777/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0777/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MEASURES/NSIDC-0777.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MEASURES/NSIDC-0777.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=NSIDC-0777+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=NSIDC-0777+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0777/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0777/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MEASURES/NSIDC-0777.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MEASURES/NSIDC-0777.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=NSIDC-0777+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=NSIDC-0777+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0777/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0777/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/B28FM2QVVYWY",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/B28FM2QVVYWY",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/B28FM2QVVYWY",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/B28FM2QVVYWY",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2363258255-NSIDC_ECS",
+            "issued": "2016-01-01",
+            "keyword": [
+                "earth science",
+                "snow/ice",
+                "cryosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/B28FM2QVVYWY",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-12-29",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-70.0 62.0 -20.0 82.0",
+            "temporal": "2016-01-01T00:00:00Z/2023-12-29T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MEaSUREs Greenland Ice Velocity: Selected Glacier Site Single-Pair Velocity Maps from Optical Images V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CAR/DATA115",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Charles Gatebe; Michael King; Rajesh Poudyal. 2018-01-10. CAR_KUWAITOILFIRE_L1C. Version 1. CAR Kuwait Oil Fire Spectral Reflectance L1 V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/CAR/DATA115. https://disc.gsfc.nasa.gov/datacollection/CAR_KUWAITOILFIRE_L1C_1.html.",
-            "issued": "2017-11-29",
-            "temporal": "1991-05-18T00:00:00Z/1991-06-02T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-11-29",
-            "keyword": [
-                "oceans",
-                "land surface",
-                "earth science",
-                "clouds",
-                "atmospheric radiation",
-                "atmosphere",
-                "aerosols",
-                "surface radiative properties",
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
-            "identifier": "C1442068298-GES_DISC",
-            "description": "CAR Kuwait Oil Fire mission measured bidirectional reflectance function of smoke from Kuwait oil fires during the Kuwait Oil Fire Smoke Experiment. Measurements were also taken over the Saudi Arabian desert with overlying desert dust, and Persian Gulf waters with some overlying aerosols.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "CAR_KUWAITOILFIRE_L1C",
             "creator": "Charles Gatebe; Michael King; Rajesh Poudyal",
-            "title": "CAR Kuwait Oil Fire Spectral Reflectance L1 V1 (CAR_KUWAITOILFIRE_L1C) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/CAR_KUWAITOILFIRE_L1C_1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "CAR Kuwait Oil Fire mission measured bidirectional reflectance function of smoke from Kuwait oil fires during the Kuwait Oil Fire Smoke Experiment. Measurements were also taken over the Saudi Arabian desert with overlying desert dust, and Persian Gulf waters with some overlying aerosols.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAR%2FDATA115",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAR%2FDATA115",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -128258,1021 +128230,1031 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CAR_KUWAITOILFIRE_L1C_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CAR_KUWAITOILFIRE_L1C_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/CAR/CAR_KUWAITOILFIRE_L1C.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/CAR/CAR_KUWAITOILFIRE_L1C.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/opendap/CAR/CAR_KUWAITOILFIRE_L1C.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/opendap/CAR/CAR_KUWAITOILFIRE_L1C.1/contents.html",
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
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/CAR/CAR_KUWAITOILFIRE_L1C.1/doc/CAR_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/CAR/CAR_KUWAITOILFIRE_L1C.1/doc/CAR_README.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/CAR_KUWAITOILFIRE_L1C_1.jpg",
+            "identifier": "C1442068298-GES_DISC",
+            "issued": "2017-11-29",
+            "keyword": [
+                "oceans",
+                "land surface",
+                "earth science",
+                "clouds",
+                "atmospheric radiation",
+                "atmosphere",
+                "aerosols",
+                "surface radiative properties",
+                "ocean optics"
+            ],
+            "landingPage": "https://doi.org/10.5067/CAR/DATA115",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-11-29",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "CAR_KUWAITOILFIRE_L1C",
             "spatial": "46.9617 26.2602 50.7998 28.7545",
+            "temporal": "1991-05-18T00:00:00Z/1991-06-02T23:59:59.999Z",
             "theme": [
                 "CAR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CAR Kuwait Oil Fire Spectral Reflectance L1 V1 (CAR_KUWAITOILFIRE_L1C) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TCSP/LIP/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Blakeslee, Richard J., Monte  Bateman and Douglas M. Mach.2006. TCSP ER-2 LIGHTNING INSTRUMENT PACKAGE (LIP) [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/TCSP/LIP/DATA101",
-            "issued": "2006-04-07",
-            "temporal": "2005-07-02T12:50:35Z/2005-07-27T11:30:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
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
-            "identifier": "C1979951465-GHRC_DAAC",
             "description": "The TCSP ER-2 Lightning Instrument Package (LIP) dataset consists of electrical field measurements of lightning from seven field mills, air conductivity data from a two channel conductivity probe, and navigation data, for the period of July 2 to July 27, 2005. These data were collected by the Lightning Instrument Package (LIP) flown aboard the NASA ER-2 high-altitude aircraft during the Tropical Cloud Systems and Processes (TCSP) field campaign in July 2005. The main goal of the campaign was to gain further insight into the structure and lifecycle of tropical weather systems. The TCSP ER-2 LIP data are provided in ASCII text files with PNG browse image files.",
-            "graphic-preview-description": "N/A",
-            "title": "TCSP ER-2 LIGHTNING INSTRUMENT PACKAGE (LIP) V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/lip/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTCSP%2FLIP%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTCSP%2FLIP%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=tcsplip",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=tcsplip",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/lip/browse/TCSP_LIP_cond_2005.187_050706_1948_log.png",
-                    "description": "Sample Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample Browse Image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/lip/browse/TCSP_LIP_cond_2005.187_050706_1948_log.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://airbornescience.nasa.gov/instrument/LIP",
-                    "description": "Lightning Instrument Package (LIP)",
                     "@type": "dcat:Distribution",
+                    "description": "Lightning Instrument Package (LIP)",
+                    "downloadURL": "https://airbornescience.nasa.gov/instrument/LIP",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/lip/doc/tcsplip_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/lip/doc/tcsplip_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/tcsp/tcsplip/TCSP_LIP_conductivity_data.pdf",
-                    "description": "TCSP LIP Conductivity Data",
                     "@type": "dcat:Distribution",
+                    "description": "TCSP LIP Conductivity Data",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/tcsp/tcsplip/TCSP_LIP_conductivity_data.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
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
-                    "downloadURL": "https://doi.org/10.1175/JTECH1918.1",
-                    "description": "Retrieving storm electric fields from aircraft field mill data. Part II: Applications",
                     "@type": "dcat:Distribution",
+                    "description": "Retrieving storm electric fields from aircraft field mill data. Part II: Applications",
+                    "downloadURL": "https://doi.org/10.1175/JTECH1918.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/JTECH2080.1",
-                    "description": "General matrix inversion technique for the calibration of electric field sensor arrays on aircraft platforms",
                     "@type": "dcat:Distribution",
+                    "description": "General matrix inversion technique for the calibration of electric field sensor arrays on aircraft platforms",
+                    "downloadURL": "https://doi.org/10.1175/JTECH2080.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/2004GL021802",
-                    "description": "Observed electric fields associated with lightning initiation",
                     "@type": "dcat:Distribution",
+                    "description": "Observed electric fields associated with lightning initiation",
+                    "downloadURL": "https://doi.org/10.1029/2004GL021802",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/tcsp/tcsplip/plot_TCSP_archive_data.pro",
-                    "description": "TCSP Archive Data Plot Program",
                     "@type": "dcat:Distribution",
+                    "description": "TCSP Archive Data Plot Program",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/tcsp/tcsplip/plot_TCSP_archive_data.pro",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/TCSP",
-                    "description": "TCSP Field Campaign Project Homepage",
                     "@type": "dcat:Distribution",
+                    "description": "TCSP Field Campaign Project Homepage",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/TCSP",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/lip/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/lip/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/lip/browse/",
+            "identifier": "C1979951465-GHRC_DAAC",
+            "issued": "2006-04-07",
+            "keyword": [
+                "earth science",
+                "atmospheric electricity",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/TCSP/LIP/DATA101",
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
             "spatial": "-99.7368 4.68322 -53.0668 24.7845",
+            "temporal": "2005-07-02T12:50:35Z/2005-07-27T11:30:00Z",
             "theme": [
                 "TCSP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TCSP ER-2 LIGHTNING INSTRUMENT PACKAGE (LIP) V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-GIA-3-EXT1-EXTENSION-1-V1.0",
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
+            "description": "Rosetta Extension 1 Phase covers the period of time from 13 January 2016  until 5 April 2016. It started after Rosetta successfully completed the  Comet Escort 4 Phase. The present DataSet collects the GIADA data of EXT1 phase. The GIADA Scientific phase started on 7 May 2014 and was devoted to the characterization of the 67P environment.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-gia-3-ext1-extension-1-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-GIA-3-EXT1-EXTENSION-1-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-gia-3-ext1-extension-1-v1.0",
-            "description": "Rosetta Extension 1 Phase covers the period of time from 13 January 2016  until 5 April 2016. It started after Rosetta successfully completed the  Comet Escort 4 Phase. The present DataSet collects the GIADA data of EXT1 phase. The GIADA Scientific phase started on 7 May 2014 and was devoted to the characterization of the 67P environment.",
-            "title": "ROSETTA-ORBITER 67P GIADA 3 EXT1 EXTENSION 1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P GIADA 3 EXT1 EXTENSION 1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Suborbital/LISTOS/Ground_YaleCoastal_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2020-12-16. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/Suborbital/LISTOS/Ground_YaleCoastal_Data_1.",
-            "issued": "2020-09-08",
-            "temporal": "2018-07-01T00:00:00Z/2019-08-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-18",
-            "keyword": [
-                "atmosphere",
-                "atmospheric winds",
-                "atmospheric temperature",
-                "atmospheric chemistry",
-                "earth science",
-                "air quality"
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
-            "identifier": "C1981395972-LARC_ASDC",
             "description": "LISTOS_Ground_YaleCoastal_Data is the Long Island Sound Tropospheric Ozone Study (LISTOS) ground site data collected at the Yale Coastal ground site during the LISTOS field campaign. This product is a result of a joint effort across multiple agencies, including NASA, NOAA, the EPA Northeast States for Coordinated Air Use Management (NESCAUM), Maine Department of Environmental Protection, New Jersey Department of Environmental Protection, New York State Department of Environmental Conservation and several research groups at universities. Data collection is complete.\r\n\r\nThe New York City (NYC) metropolitan area (comprised of portions of New Jersey, New York, and Connecticut in and around NYC) is home to over 20 million people, but also millions of people living downwind in neighboring states. This area continues to persistently have challenges meeting past and recently revised federal health-based air quality standards for ground-level ozone, which impacts the health and well-being of residents living in the area. A unique feature of this chronic ozone problem is the pollution transported in a northeast direction out of NYC over Long Island Sound. The relatively cool waters of Long Island Sound confine the pollutants in a shallow and stable marine boundary layer. Afternoon heating over coastal land creates a sea breeze that carries the air pollution inland from the confined marine layer, resulting in high ozone concentrations in Connecticut and, at times, farther east into Rhode Island and Massachusetts. To investigate the evolving nature of ozone formation and transport in the NYC region and downwind, Northeast States for Coordinated Air Use Management (NESCAUM) launched the Long Island Sound Tropospheric Ozone Study (LISTOS). LISTOS was a multi-agency collaborative study focusing on Long Island Sound and the surrounding coastlines that continually suffer from poor air quality exacerbated by land/water circulation. The primary measurement observations took place between June-September 2018 and include in-situ and remote sensing instrumentation that were integrated aboard three aircraft, a network of ground sites, mobile vehicles, boat measurements, and ozonesondes. The goal of LISTOS was to improve the understanding of ozone chemistry and sea breeze transported pollution over Long Island Sound and its coastlines. LISTOS also provided NASA the opportunity to test air quality remote sensing retrievals with the use of its airborne simulators (GEOstationary Coastal and Air Pollution Events (GEO-CAPE) Airborne Simulator (GCAS), and Geostationary Trace gas and Aerosol Sensory Optimization (GeoTASO)) for the preparation of the Tropospheric Emissions; Monitoring of Pollution (TEMPO) observations for monitoring air quality from space. LISTOS also helped collaborators in the validation of Tropospheric Monitoring Instrument (TROPOMI) science products, with use of airborne- and ground-based measurements of ozone, NO2, and HCHO.",
-            "title": "LISTOS Yale Coastal Ground Site Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSuborbital%2FLISTOS%2FGround_YaleCoastal_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSuborbital%2FLISTOS%2FGround_YaleCoastal_Data_1",
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
-                    "downloadURL": "https://www.nescaum.org/documents/listos",
-                    "description": "NESCAUM Project Page for Long Island Sound Tropospheric Ozone Study (LISTOS)",
                     "@type": "dcat:Distribution",
+                    "description": "NESCAUM Project Page for Long Island Sound Tropospheric Ozone Study (LISTOS)",
+                    "downloadURL": "https://www.nescaum.org/documents/listos",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1981395972-LARC_ASDC",
-                    "description": "Earthdata Search for LISTOS_Ground_YaleCoastal_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for LISTOS_Ground_YaleCoastal_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1981395972-LARC_ASDC",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/LISTOS/2017",
-                    "description": "LISTOS Data on the Sub-Orbital Order Tool (SOOT) Power User Interface (UI)",
                     "@type": "dcat:Distribution",
+                    "description": "LISTOS Data on the Sub-Orbital Order Tool (SOOT) Power User Interface (UI)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/LISTOS/2017",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/LISTOS/pdocuments",
-                    "description": "LISTOS Support Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "LISTOS Support Documentation",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/LISTOS/pdocuments",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/LISTOS/2018",
-                    "description": "LISTOS 2018 Data on the Sub-Orbital Order Tool (SOOT) Power User Interface (UI)",
                     "@type": "dcat:Distribution",
+                    "description": "LISTOS 2018 Data on the Sub-Orbital Order Tool (SOOT) Power User Interface (UI)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/LISTOS/2018",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through the Sub-Orbital Order Tool"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/LISTOS/Ground_YaleCoastal_Data_1/",
-                    "description": "ASDC Direct Data Download for LISTOS_Ground_YaleCoastal_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for LISTOS_Ground_YaleCoastal_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/LISTOS/Ground_YaleCoastal_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1981395972-LARC_ASDC",
+            "issued": "2020-09-08",
+            "keyword": [
+                "atmosphere",
+                "atmospheric winds",
+                "atmospheric temperature",
+                "atmospheric chemistry",
+                "earth science",
+                "air quality"
+            ],
+            "landingPage": "https://doi.org/10.5067/Suborbital/LISTOS/Ground_YaleCoastal_Data_1",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>35.0 -80.0 35.0 75.0 45.0 75.0 45.0 -80.0 35.0 -80.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2018-07-01T00:00:00Z/2019-08-01T23:59:59.999Z",
             "theme": [
                 "LISTOS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LISTOS Yale Coastal Ground Site Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/855/",
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
-            "identifier": "DASHLINK_855",
             "description": "This paper presents a model-driven methodology for predict- ing the remaining useful life of electrolytic capacitors. This methodology adopts a Kalman filter approach in conjunction with an empirical state-based degradation model to predict the degradation of capacitor parameters through the life of the capacitor. Electrolytic capacitors are important components of systems that range from power supplies on critical avion- ics equipment to power drivers for electro-mechanical actuators. These devices are known for their comparatively low reliability and given their critical role in the system, they are good candidates for component level prognostics and health management. Prognostics provides a way to assess remain- ing useful life of a capacitor based on its current state of health and its anticipated future usage and operational conditions. This paper proposes and empirical degradation model and discusses experimental results for an accelerated aging test performed on a set of identical capacitors subjected to electrical stress. The data forms the basis for developing the Kalman-filter based remaining life prediction algorithm.",
-            "title": "Towards A Model-Based Prognostics Methodology For Electrolytic Capacitors: A Case Study Based On Electrical Overstress Accelerated Aging",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/ijphm_12_004.pdf",
-                    "description": "Full Paper PDF",
                     "@type": "dcat:Distribution",
+                    "description": "Full Paper PDF",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/ijphm_12_004.pdf",
+                    "mediaType": "application/pdf",
                     "title": "ijphm_12_004.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_855",
+            "issued": "2013-12-12",
+            "keyword": [
+                "dashlink",
+                "ames",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/855/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Towards A Model-Based Prognostics Methodology For Electrolytic Capacitors: A Case Study Based On Electrical Overstress Accelerated Aging"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LRO-L-SPICE-6-V1.0",
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
+            "description": "This data set includes the complete set of Lunar Reconnaissance Orbiter SPICE data files (``kernel files''), which can be accessed using SPICE software. The SPICE data contains geometric and other ancillary information needed to recover the full value of science instrument data. In particular SPICE kernels provide spacecraft and planetary ephemerides, instrument mounting alignments, spacecraft orientation, and data needed for relevant time conversions.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lro-l-spice-6-v1.0_49qr-j7bv",
+            "issued": "2021-05-21",
+            "keyword": [
+                "moon",
+                "lunar reconnaissance orbiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LRO-L-SPICE-6-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lro-l-spice-6-v1.0_49qr-j7bv",
-            "description": "This data set includes the complete set of Lunar Reconnaissance Orbiter SPICE data files (``kernel files''), which can be accessed using SPICE software. The SPICE data contains geometric and other ancillary information needed to recover the full value of science instrument data. In particular SPICE kernels provide spacecraft and planetary ephemerides, instrument mounting alignments, spacecraft orientation, and data needed for relevant time conversions.",
-            "title": "LRO LUNAR SPICE KERNELS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "LRO LUNAR SPICE KERNELS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-FC1-2-EDR-CERES-IMAGES-V1.0",
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
+            "description": "Abstract                                                                   ========                                                                   This dataset contains raw Framing Camera 1 (FC1) images sometimes        called level-1a or EDR data. It includes images from the Dawn Ceres      eXtended Mission 1 Orbit 3 (XMO3, aka Ceres Extended GRaND - CXG) phase  on 2017-02-19 and the Ceres eXtended Mission Orbit 4 (XMO4, aka Ceres    Extended Opposition - CXO) phase on 2017-04-29. In addition, there are   images from eXtended Mission 2 (XM2), orbits XMO6 (C2I - intermediate),  and XMO7 (C2E - elliptical) as well as some checkout and end-of-mission  star calibration images.FC1 is one of two identical units flying         on the Dawn spacecraft. It was designated as the backup system to be     used only in the event of a failure of the primary system, FC2. Prior to the Ceres extended mission, FC1 had only been used for in-flight         calibration and to periodically exercise its various mechanisms (door,   filter wheel, etc.). This is the only science dataset generated by FC1.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-fc1-2-edr-ceres-images-v1.0_49sk-f734",
+            "issued": "2021-05-21",
+            "keyword": [
+                "1 ceres",
+                "dawn mission to vesta and ceres"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-FC1-2-EDR-CERES-IMAGES-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-fc1-2-edr-ceres-images-v1.0_49sk-f734",
-            "description": "Abstract                                                                   ========                                                                   This dataset contains raw Framing Camera 1 (FC1) images sometimes        called level-1a or EDR data. It includes images from the Dawn Ceres      eXtended Mission 1 Orbit 3 (XMO3, aka Ceres Extended GRaND - CXG) phase  on 2017-02-19 and the Ceres eXtended Mission Orbit 4 (XMO4, aka Ceres    Extended Opposition - CXO) phase on 2017-04-29. In addition, there are   images from eXtended Mission 2 (XM2), orbits XMO6 (C2I - intermediate),  and XMO7 (C2E - elliptical) as well as some checkout and end-of-mission  star calibration images.FC1 is one of two identical units flying         on the Dawn spacecraft. It was designated as the backup system to be     used only in the event of a failure of the primary system, FC2. Prior to the Ceres extended mission, FC1 had only been used for in-flight         calibration and to periodically exercise its various mechanisms (door,   filter wheel, etc.). This is the only science dataset generated by FC1.",
-            "title": "DAWN FC1 RAW (EDR) CERES IMAGES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "DAWN FC1 RAW (EDR) CERES IMAGES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1274625639-GES_DISC.html",
             "citation": "Goddard Laboratory for Atmospheres at NASA GSFC. 1995-01-01. TOVSADNF. Version 01. TOVS GLA DAILY GRIDS from NOAA-9 V01. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/TOVSADNF_01.html. Digital Science Data.",
-            "issued": "1984-12-27",
-            "temporal": "1984-12-27T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "1987-01-01",
-            "keyword": [
-                "clouds",
-                "atmospheric radiation",
-                "ocean temperature",
-                "atmospheric pressure",
-                "atmospheric temperature",
-                "oceans",
-                "atmospheric water vapor",
-                "precipitation",
-                "atmospheric chemistry",
-                "earth science",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JOEL SUSSKIND",
                 "hasEmail": "mailto:joel.susskind-1@nasa.gov"
             },
+            "creator": "Goddard Laboratory for Atmospheres at NASA GSFC",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1274625639-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "This dataset (TOVSADNF) contains the TIROS Operational Vertical Sounder (TOVS) level 3 geophysical parameters derived using data from NOAA-9 and the physical retrieval method of Susskind et al. (1984) and processed by the Satellite Data Utilization Office of the Goddard Laboratory for Atmospheres at NASA/GSFC. This method, which is hydrodynamic model- and a priori data-dependent, is designated as the so-called Path A scheme by the TOVS Pathfinder Science Working Group. The 20 channel High resolution Infrared Radiation Sounder 2 (HIRS2) and the 4 channel Microwave Sounding Unit (MSU) aboard the NOAA-xx series of Polar Orbiting Satellites are used to produce global fields of the 3-dimensional temperature-moisture structure of the atmosphere. In addition to profiles of temperature and moisture, the HIRS2/MSU data are used to derive important quantities such as land and sea surface temperature, outgoing longwave radiation, cloud fraction, cloudtop height, total ozone overburden and precipitation estimates.\n\nThe Path A system steps through an interactive forecast-retrieval-analysis cycle. In each 6 hour synoptic period, a 2nd order General Circulation Model (Takacs et al., 1994) is used to generate the 6 hour forecast fields of temperature and humidity. These global fields are used as the first guess for all soundings occuring within a 6 hour time window centered upon the forecast time. These retrievals are then assimilated with all available insitu measurements (such as radiosonde and ship reports) in the 6 hour interval using an Optimal Interpolation (OI) analysis scheme developed by the Data Assimilation Office of the Goddard Laboratory for Atmospheres. This analysis is then used to specify the initial conditions for the next 6 hour forecast, thus completing the cycle.\n\nThe retrieval algorithm itself is a physical method based on the iterative relaxation technique originally proposed by Chahine (1968). The basic approach consists of modifying the temperature profile from the previous iteration by an amount proportional to the difference between the observed brightness temperatures and the brightness temperatures computed from the trial parameters using the full radiative transfer equation applied at the observed satellite zenith angle. For the case of the temperature profile, the updated layer mean temperatures are given as a linear combination of multichannel brightness temperature differences with the coefficients given by the channel weighting functions. Constraints are imposed upon the solution in order to ensure stability and convergence of the iterative process. For more details see Susskind et al (1984).\n\nThere are level 3 data product files for five TOVS satellites, each of which is in the HDF format and each representative of a different averaging time period. All files contain the same number of geophysical parameter arrays stored as HDF Scientific Data Sets (SDSs). The time periods include daily, 5 day (pentad) and monthly, with the AM and PM portions of the orbits treated separately.  All data are mapped to a 1 degree longitude by 1 degree latitude global grid.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TOVSADNF",
-            "creator": "Goddard Laboratory for Atmospheres at NASA GSFC",
-            "title": "TOVS GLA DAILY GRIDS from NOAA-9 V01 (TOVSADNF) at GES DISC",
-            "graphic-preview-description": "TOVSADNF image",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOVSADNF_01.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOVSADNF_01.png",
-                    "description": "TOVSADNF image",
                     "@type": "dcat:Distribution",
+                    "description": "TOVSADNF image",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOVSADNF_01.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TOVSADNF_01.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TOVSADNF_01.html",
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
-                    "downloadURL": "https://disc1.gesdisc.eosdis.nasa.gov/data/tovs/TOVSADNF",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://disc1.gesdisc.eosdis.nasa.gov/data/tovs/TOVSADNF",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TOVSADNF+001",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TOVSADNF+001",
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
+            "graphic-preview-description": "TOVSADNF image",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOVSADNF_01.png",
+            "identifier": "C1274625639-GES_DISC",
+            "issued": "1984-12-27",
+            "keyword": [
+                "clouds",
+                "atmospheric radiation",
+                "ocean temperature",
+                "atmospheric pressure",
+                "atmospheric temperature",
+                "oceans",
+                "atmospheric water vapor",
+                "precipitation",
+                "atmospheric chemistry",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1274625639-GES_DISC.html",
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
+            "series-name": "TOVSADNF",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1984-12-27T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "TOVS Pathfinder",
                 "CWIC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TOVS GLA DAILY GRIDS from NOAA-9 V01 (TOVSADNF) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MFAOHTY3YK34",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA SCP Arctic and Antarctic Ice Extent from QuikSCAT, 1999-2009, Version 2. Version 2. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/MFAOHTY3YK34.",
-            "issued": "1999-07-19",
-            "temporal": "1999-07-19T00:00:00Z/2009-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2009-12-31",
-            "keyword": [
-                "cryosphere",
-                "earth science",
-                "oceans",
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
-            "identifier": "C1386250250-NSIDCV0",
             "description": "This data set provides sea ice extent for the Arctic (60-90 degrees North) and Antarctic (52-90 degrees South) in Scatterometer Image Reconstruction (SIR) binary image format, along with ASCII text files containing latitude and longitude coordinates along the sea ice edge, and browse images of SIR files in Graphics Interchange Format (GIF) format. Ancillary products include daily-averaged total sea ice extent in ASCII format. Estimates of sea ice extent were produced from daily-averaged QuikSCAT sigma-0 measurements and extend from 19 July 1999 to 31 December 2009.\n\nQuikSCAT obtains 12 individual radar normalized backscatter (sigma-0) measurements, called slices, for each footprint as it scans over a 1800 km wide swath. Slices are typically 4 to 6 km long by 20 km wide. The summed measurements of the slices are called egg measurements. The effective resolution and shape of each egg measurement is approximately 20 by 30 km, depending on the antenna beam and instrument mode. This data set contains both slice and egg images for each day.\n\nThe Microwave Earth Remote Sensing (MERS) group at Brigham Young University (BYU) developed a SIR-with-filtering (SIRF) algorithm that combines forward- and aft-looking sigma-0 measurements to produce enhanced-resolution backscatter images over various azimuth angles. The polarization ratio, incidence angle dependence, and the sigma-0 estimate error standard deviation were used to discriminate between sea ice and ocean. Sea ice extent was estimated for both slice and egg images. The nominal pixel resolution of the slice images is 2.225 km with an estimated effective resolution of approximately 4 km. Egg images have a nominal pixel resolution of 4.45 km with an estimated effective resolution of approximately 8 to 10 km.\n\nData and browse images are available via FTP, along with C, Fortran, and Interactive Data Language (IDL) tools to read and display the SIR images.",
-            "title": "NASA SCP Arctic and Antarctic Ice Extent from QuikSCAT, 1999-2009, Version 2",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMFAOHTY3YK34",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMFAOHTY3YK34",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0265_QuikSCAT_ice_extent/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0265_QuikSCAT_ice_extent/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0265_QuikSCAT_ice_extent/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0265_QuikSCAT_ice_extent/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0265_QuikSCAT_ice_extent/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0265_QuikSCAT_ice_extent/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MFAOHTY3YK34",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/MFAOHTY3YK34",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MFAOHTY3YK34",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MFAOHTY3YK34",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386250250-NSIDCV0",
+            "issued": "1999-07-19",
+            "keyword": [
+                "cryosphere",
+                "earth science",
+                "oceans",
+                "sea ice"
+            ],
+            "landingPage": "https://doi.org/10.5067/MFAOHTY3YK34",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2009-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 60.0 180.0 90.0",
+            "temporal": "1999-07-19T00:00:00Z/2009-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NASA SCP Arctic and Antarctic Ice Extent from QuikSCAT, 1999-2009, Version 2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/CATLIN_ARCTIC_SURVEY/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/CATLIN_ARCTIC_SURVEY/DATA001.",
-            "issued": "2011-03-17",
-            "temporal": "2011-03-17T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean optics",
-                "earth science",
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
-            "identifier": "C1633360181-OB_DAAC",
             "description": "Measurements made in the Arctic Ocean by the RV Catlin in 2011.",
-            "title": "2011 R/V Catlin cruise in the Arctic Ocean",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FCATLIN_ARCTIC_SURVEY%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FCATLIN_ARCTIC_SURVEY%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Catlin_Arctic_Survey/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Catlin_Arctic_Survey/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360181-OB_DAAC",
+            "issued": "2011-03-17",
+            "keyword": [
+                "ocean optics",
+                "earth science",
+                "salinity/density",
+                "oceans",
+                "ocean chemistry",
+                "ocean temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/CATLIN_ARCTIC_SURVEY/DATA001",
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
+            "temporal": "2011-03-17T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "2011 R/V Catlin cruise in the Arctic Ocean"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-FAMILY-V3.0",
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
+            "description": "This dataset contains the asteroid dynamical family classifications contained in Zappala, et al. (1995) [ZAPPALAETAL1995]. These are based on the heirarchical clustering method applied to the proper elements of Milani and Knezevic (1994) [MILANI&KNEZEVIC1994]. 12,487 asteroids, numbered and unnumbered, are included.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-family-v3.0_49yh-gzd3",
+            "issued": "2021-05-21",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-FAMILY-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-family-v3.0_49yh-gzd3",
-            "description": "This dataset contains the asteroid dynamical family classifications contained in Zappala, et al. (1995) [ZAPPALAETAL1995]. These are based on the heirarchical clustering method applied to the proper elements of Milani and Knezevic (1994) [MILANI&KNEZEVIC1994]. 12,487 asteroids, numbered and unnumbered, are included.",
-            "title": "ASTEROID DYNAMICAL FAMILIES V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ASTEROID DYNAMICAL FAMILIES V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MET08/CERES/GEO_ED4_SH_V01.2",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2015-08-29. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/MET08/CERES/GEO_ED4_SH_V01.2. https://doi.org/10.5067/MET08/CERES/GEO_ED4_SH_V01.2.",
-            "issued": "2015-08-29",
-            "temporal": "2015-11-15T00:00:00Z/2024-03-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-08-29",
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
-            "identifier": "C1584979294-LARC_ASDC",
             "description": "CER_GEO_Ed4_MET08_SH_V01.2 is the Satellite Cloud and Radiation Property retrieval System (SatCORPS) Clouds and the Earth's Radiant Energy System (CERES) Geostationary Satellite (GEO) Edition 4 Meteosat-8 over the Southern Hemisphere (SH) Version 1.2 data product. Data was collected using the Spinning Enhanced Visible and Infrared Imager (SEVIRI) Instrument on the Meteosat-8 platform. Data collection for this product is in progress.\r\n\r\nNote: Version 1.2 covers when the satellite moves to 41\u00b0 E.\r\n\r\nThis data set comprises cloud micro-physical and radiation properties derived hourly from Meteosat-8 geostationary satellite imager data using the Langley Research Center (LARC) SATCORPS algorithms supporting the CERES project. Each active geostationary satellite's cloud microphysical and radiation properties are merged to create hourly global cloud properties that estimate fluxes between CERES instrument measurements to account for the changing diurnal cycle. The data set is arranged as files for each hour and in netCDF-4 format. The observations are at 3 km resolution (at nadir) and are sub-sampled to 6 km.\r\n\r\nCERES is a key Earth Observing System (EOS) program component. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions follow the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument, the proto flight model (PFM), was launched on November 27, 1997, as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit onboard the Earth Observing System (EOS) flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched onboard Earth Observing System (EOS) Aqua on May 4, 2002. The CERES FM5 instrument was launched onboard the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The newest CERES instrument (FM6) was launched onboard the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite, now called NOAA-20, on November 18, 2017.",
-            "graphic-preview-description": "Mission Logo",
-            "title": "SatCORPS CERES GEO Edition 4 Meteosat-8 Southern Hemisphere Version 1.2",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/ceres.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMET08%2FCERES%2FGEO_ED4_SH_V01.2",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMET08%2FCERES%2FGEO_ED4_SH_V01.2",
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
-                    "downloadURL": "https://doi.org/10.5067/MET08/CERES/GEO_ED4_SH_V01.2",
-                    "description": "DOI data set landing page for CER_GEO_Ed4_MET08_SH_V01.2",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CER_GEO_Ed4_MET08_SH_V01.2",
+                    "downloadURL": "https://doi.org/10.5067/MET08/CERES/GEO_ED4_SH_V01.2",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1584979294-LARC_ASDC",
-                    "description": "Earthdata Search for CER_GEO_Ed4_MET08_SH_V01.2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CER_GEO_Ed4_MET08_SH_V01.2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1584979294-LARC_ASDC",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/GEO/Edition4/MET08_SH_V01.2/",
-                    "description": "ASDC Direct Data Download for CER_GEO_Ed4_MET08_SH_V01.2",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CER_GEO_Ed4_MET08_SH_V01.2",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/GEO/Edition4/MET08_SH_V01.2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/GEO/Edition4/MET08_SH_V01.2/contents.html",
-                    "description": "OPeNDAP data access for CER_GEO_Ed4_MET08_SH_V01.2",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CER_GEO_Ed4_MET08_SH_V01.2",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/GEO/Edition4/MET08_SH_V01.2/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Mission Logo",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/ceres.png",
+            "identifier": "C1584979294-LARC_ASDC",
+            "issued": "2015-08-29",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "clouds"
+            ],
+            "landingPage": "https://doi.org/10.5067/MET08/CERES/GEO_ED4_SH_V01.2",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-08-29",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-60.0 -50.0 -60.0 -10.0 -60.0 100.0 0.0 100.0 0.0 -10.0 0.0 -50.0 -60.0 -50.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2015-11-15T00:00:00Z/2024-03-27T00:00:00Z",
             "theme": [
                 "CERES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SatCORPS CERES GEO Edition 4 Meteosat-8 Southern Hemisphere Version 1.2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/4a4j-76qh",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "temporal": "1977-01-01/2014-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "space science",
-                "nen",
-                "geography",
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
-            "identifier": "NASA-0000038__36",
+            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
             "description": "Planetary nomenclature, like terrestrial nomenclature, is used to uniquely identify a feature on the surface of a planet or satellite so that the feature can be easily located, described, and discussed. This gazetteer contains detailed information about all names of topographic and albedo features on planets and satellites (and some planetary ring and ring-gap systems) that the International Astronomical Union (IAU) has named and approved from its founding in 1919 through the present time.",
-            "title": "Gazetteer of Planetary Nomenclature",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -129280,21 +129262,41 @@
                     "mediaType": "application/vnd.google-earth.kmz"
                 }
             ],
-            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
-            "accrualPeriodicity": "irregular"
+            "identifier": "NASA-0000038__36",
+            "issued": "2018-06-25",
+            "keyword": [
+                "space science",
+                "nen",
+                "geography",
+                "wise"
+            ],
+            "landingPage": "https://data.nasa.gov/d/4a4j-76qh",
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-EXT1-67PCHURYUMOV-M26-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 1 mission phase, covering the period from 2016-02-09T23:25:00.000 to 2016-03-08T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Replaced FITs file extension .FTS with .FIT. Browse products changed to the same size as the original image. Corrected START_TIME and STOP_TIME for BALLISTIC_STACKED images.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-ext1-67pchuryumov-m26-v3.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "dark",
                 "international rosetta mission",
@@ -129303,290 +129305,266 @@
                 "zeta cas",
                 "vega"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-EXT1-67PCHURYUMOV-M26-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-ext1-67pchuryumov-m26-v3.0",
-            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 1 mission phase, covering the period from 2016-02-09T23:25:00.000 to 2016-03-08T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Replaced FITs file extension .FTS with .FIT. Browse products changed to the same size as the original image. Corrected START_TIME and STOP_TIME for BALLISTIC_STACKED images.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 2 EXT1-MTP026 EDR V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 2 EXT1-MTP026 EDR V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-SDC-3-PLUTOCRUISE-V1.0",
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
+            "description": "This data set contains Calibrated data taken by the New Horizons         Student Dust Counter                                                   instrument during the                                                    pluto cruise                                                           mission phase.  This is VERSION 1.0 of this data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-sdc-3-plutocruise-v1.0_4a7u-qcue",
+            "issued": "2018-09-05",
+            "keyword": [
+                "new horizons",
+                "dust"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-SDC-3-PLUTOCRUISE-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-sdc-3-plutocruise-v1.0_4a7u-qcue",
-            "description": "This data set contains Calibrated data taken by the New Horizons         Student Dust Counter                                                   instrument during the                                                    pluto cruise                                                           mission phase.  This is VERSION 1.0 of this data set.",
-            "title": "NEW HORIZONS                            \n      SDC PLUTO CRUISE                                                        \n      CALIBRATED V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS                            \n      SDC PLUTO CRUISE                                                        \n      CALIBRATED V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMAG-3-EXT3-CALIBRATED-V6.0",
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
+            "description": "This dataset contains CALIBRATED (CODMAC LEVEL 3) DATA of the\nEXTENDED MISSION PHASE 3 (EXT3) from June 29 until September 30, 2016\nof the ROSETTA orbiter magnetometer RPCMAG. Observations are done in\nthe vicinity of comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1).\nThe current version of the dataset is V6.0, the first one\nbeing archived.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmag-3-ext3-calibrated-v6.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMAG-3-EXT3-CALIBRATED-V6.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmag-3-ext3-calibrated-v6.0",
-            "description": "This dataset contains CALIBRATED (CODMAC LEVEL 3) DATA of the\nEXTENDED MISSION PHASE 3 (EXT3) from June 29 until September 30, 2016\nof the ROSETTA orbiter magnetometer RPCMAG. Observations are done in\nthe vicinity of comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1).\nThe current version of the dataset is V6.0, the first one\nbeing archived.",
-            "title": "ROSETTA-ORBITER 67P RPCMAG 3 EXT3 CALIBRATED V6.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCMAG 3 EXT3 CALIBRATED V6.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMAG-2-ESC1-RAW-V6.0",
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
+            "description": "This dataset contains EDITED RAW DATA (CODMAC LEVEL 2) of the COMET\nESCORT1 Phase (ESC1) from November 22, 2014 until March 10,2015 of the\nROSETTA orbiter magnetometer RPCMAG. Observations are done in the\nvicinity of comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). The\ncurrent version of the dataset is V6.0",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmag-2-esc1-raw-v6.0_4ae3-diiz",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMAG-2-ESC1-RAW-V6.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmag-2-esc1-raw-v6.0_4ae3-diiz",
-            "description": "This dataset contains EDITED RAW DATA (CODMAC LEVEL 2) of the COMET\nESCORT1 Phase (ESC1) from November 22, 2014 until March 10,2015 of the\nROSETTA orbiter magnetometer RPCMAG. Observations are done in the\nvicinity of comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). The\ncurrent version of the dataset is V6.0",
-            "title": "ROSETTA-ORBITER 67P RPCMAG 2 ESC1 RAW V6.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCMAG 2 ESC1 RAW V6.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-DERIVED-LIGHTCURVE-V5.0",
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
+            "description": "A compilation of published lightcurve-derived parameters for asteroids.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-derived-lightcurve-v5.0_4aj8-8d7a",
+            "issued": "2021-05-21",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-DERIVED-LIGHTCURVE-V5.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-derived-lightcurve-v5.0_4aj8-8d7a",
-            "description": "A compilation of published lightcurve-derived parameters for asteroids.",
-            "title": "ASTEROID LIGHTCURVE DERIVED DATA V5.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ASTEROID LIGHTCURVE DERIVED DATA V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-EXT3-67PCHURYUMOV-M34-V2.0",
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
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 3 mission phase, covering the period from 2016-09-02T06:40:00.000 to 2016-09-26T06:39:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-ext3-67pchuryumov-m34-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-EXT3-67PCHURYUMOV-M34-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-ext3-67pchuryumov-m34-v2.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 3 mission phase, covering the period from 2016-09-02T06:40:00.000 to 2016-09-26T06:39:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 EXT3-MTP034 RDR V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 EXT3-MTP034 RDR V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-C-COMPIL-5-DB-COMET-POLARIMETRY-V1.0",
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
+            "description": "This dataset presents a collection of 2334 published and 319 unpublished results in cometary polarimetry. The database contains 2653 measurements of linear and circular polarization for 65 comets since 1940. The narrow-band and broad-band measurements within the spectral region 0.3-3.5 micron are presented. The ranges of phase angles, helio- and geocentric distances of comets are 0.4-122 deg, 0.6-4.8 AU and 0.03-4.9 AU, respectively. We have compiled 64 references to the published papers and some unpublished sources. The data are presented in a tabular format (ASCII code). The database can be used as the observational basis for detailed theoretical modeling, interpretation of the phase-angle and spectral dependence of polarization, classification of comets, and for selecting future space-mission targets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-c-compil-5-db-comet-polarimetry-v1.0_4aq3-vzyi",
+            "issued": "2021-05-21",
+            "keyword": [
+                "comet",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-C-COMPIL-5-DB-COMET-POLARIMETRY-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-c-compil-5-db-comet-polarimetry-v1.0_4aq3-vzyi",
-            "description": "This dataset presents a collection of 2334 published and 319 unpublished results in cometary polarimetry. The database contains 2653 measurements of linear and circular polarization for 65 comets since 1940. The narrow-band and broad-band measurements within the spectral region 0.3-3.5 micron are presented. The ranges of phase angles, helio- and geocentric distances of comets are 0.4-122 deg, 0.6-4.8 AU and 0.03-4.9 AU, respectively. We have compiled 64 references to the published papers and some unpublished sources. The data are presented in a tabular format (ASCII code). The database can be used as the observational basis for detailed theoretical modeling, interpretation of the phase-angle and spectral dependence of polarization, classification of comets, and for selecting future space-mission targets.",
-            "title": "DATABASE OF COMET POLARIMETRY, V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "DATABASE OF COMET POLARIMETRY, V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/V8TCJ7HQD15A",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "OCO-2 Science Team/Michael Gunson, AnnmarieEldering. 2020-08-10. OCO2_L2_ABand. Version 10r. OCO-2 Level 2 spatially ordered geolocated retrievals screened using the A-band Preprocessor, Retrospective Processing V10r. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/V8TCJ7HQD15A. https://disc.gsfc.nasa.gov/datacollection/OCO2_L2_ABand_10r.html. Digital Science Data.",
-            "issued": "2020-08-01",
-            "temporal": "2014-09-06T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-08-10",
-            "keyword": [
-                "atmosphere",
-                "atmospheric chemistry",
-                "earth science"
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
-            "identifier": "C1685783936-GES_DISC",
-            "description": "Version 10r is the current version of the data set. Older versions will no longer be available and are superseded by Version 10r.\n\nIn early 2021, the OCO Team identified an issue with OCO-2 level 2 products processed since January 28, 2020. The Ancillary Geometric Product (AGAP) file, a static file used in OCO-2 Geolocation processing, was inadvertently replaced with an obsolete version. This AGAP file included a ~300 m pointing error. As a result, all OCO-2 Level 2, version 10r, data files for the period January 28 - December 31, 2020, were corrected and replaced. The replacement process was completed by the end of June, 2021. The significance of this error has been described in Kiel et al. (2019; doi:10.5194/amt-12-2241-2019).\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OCO2_L2_ABand",
             "creator": "OCO-2 Science Team/Michael Gunson, AnnmarieEldering",
-            "title": "OCO-2 Level 2 spatially ordered geolocated retrievals screened using the A-band Preprocessor, Retrospective Processing V10r (OCO2_L2_ABand) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OCO2_L2_ABand_8r.jpeg",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Version 10r is the current version of the data set. Older versions will no longer be available and are superseded by Version 10r.\n\nIn early 2021, the OCO Team identified an issue with OCO-2 level 2 products processed since January 28, 2020. The Ancillary Geometric Product (AGAP) file, a static file used in OCO-2 Geolocation processing, was inadvertently replaced with an obsolete version. This AGAP file included a ~300 m pointing error. As a result, all OCO-2 Level 2, version 10r, data files for the period January 28 - December 31, 2020, were corrected and replaced. The replacement process was completed by the end of June, 2021. The significance of this error has been described in Kiel et al. (2019; doi:10.5194/amt-12-2241-2019).\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FV8TCJ7HQD15A",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FV8TCJ7HQD15A",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -129596,59 +129574,59 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_L2_ABand_10r.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_L2_ABand_10r.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L2_ABand.10r/",
-                    "description": "Access the data via HTTP",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L2_ABand.10r/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO2_L2_ABand",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO2_L2_ABand",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L2_ABand.10r/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L2_ABand.10r/contents.html",
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
@@ -129658,213 +129636,206 @@
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OCO2_L2_ABand_8r.jpeg",
+            "identifier": "C1685783936-GES_DISC",
+            "issued": "2020-08-01",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/V8TCJ7HQD15A",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-08-10",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "OCO2_L2_ABand",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2014-09-06T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "OCO-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OCO-2 Level 2 spatially ordered geolocated retrievals screened using the A-band Preprocessor, Retrospective Processing V10r (OCO2_L2_ABand) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TERRA/MODIS/L3M/PAR/2022",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/TERRA/MODIS/L3M/PAR/2022.",
-            "issued": "2019-06-23",
-            "temporal": "2000-02-24T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-08-08",
-            "keyword": [
-                "national geospatial data asset",
-                "ngda",
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
-            "identifier": "C2331487884-OB_DAAC",
             "description": "MODIS (or Moderate-Resolution Imaging Spectroradiometer) is a key instrument aboard the Terra (EOS AM) and Aqua (EOS PM) satellites. Terra's orbit around the Earth is timed so that it passes from north to south across the equator in the morning, while Aqua passes south to north over the equator in the afternoon. Terra MODIS and Aqua MODIS are viewing the entire Earth's surface every 1 to 2 days, acquiring data in 36 spectral bands, or groups of wavelengths (see MODIS Technical Specifications). These data will improve our understanding of global dynamics and processes occurring on the land, in the oceans, and in the lower atmosphere. MODIS is playing a vital role in the development of validated, global, interactive Earth system models able to predict global change accurately enough to assist policy makers in making sound decisions concerning the protection of our environment.",
-            "title": "Terra MODIS Global Mapped Photosynthetically Active Radiation (PAR) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMODIS%2FL3M%2FPAR%2F2022",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMODIS%2FL3M%2FPAR%2F2022",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/TERRA/MODIS/L3M/PAR/2022",
-                    "description": "MODIS-Terra L3M Photosynthetically Active Radiation (PAR) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS-Terra L3M Photosynthetically Active Radiation (PAR) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/TERRA/MODIS/L3M/PAR/2022",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/MODIST/L3SMI/",
-                    "description": "OB.DAAC OPeNDAP Site for Terra MODIS Standard Mapped Image (SMI) Product",
                     "@type": "dcat:Distribution",
+                    "description": "OB.DAAC OPeNDAP Site for Terra MODIS Standard Mapped Image (SMI) Product",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/MODIST/L3SMI/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2331487884-OB_DAAC",
+            "issued": "2019-06-23",
+            "keyword": [
+                "national geospatial data asset",
+                "ngda",
+                "oceans",
+                "ocean optics",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/TERRA/MODIS/L3M/PAR/2022",
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
+            "title": "Terra MODIS Global Mapped Photosynthetically Active Radiation (PAR) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMAG-2-ESC1-RAW-V5.0",
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
+            "description": "This dataset contains EDITED RAW DATA (CODMAC LEVEL 2) of the COMET\nESCORT1 Phase from November 22, 2014 until March 10, 2015 of the\nROSETTA orbiter magnetometer RPCMAG. Observations are done in the\nvicinity of comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1).\nVersion V5.0 is the first version being released.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmag-2-esc1-raw-v5.0_4atv-pxds",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMAG-2-ESC1-RAW-V5.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmag-2-esc1-raw-v5.0_4atv-pxds",
-            "description": "This dataset contains EDITED RAW DATA (CODMAC LEVEL 2) of the COMET\nESCORT1 Phase from November 22, 2014 until March 10, 2015 of the\nROSETTA orbiter magnetometer RPCMAG. Observations are done in the\nvicinity of comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1).\nVersion V5.0 is the first version being released.",
-            "title": "ROSETTA-ORBITER 67P RPCMAG 2 ESC1 RAW V5.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCMAG 2 ESC1 RAW V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NCJELM4CS8H8",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Gary L. Fahnenstiel, Michael J. Sayers, Robert A. Shuchman, Foad Yousef, & Steven A. Pothoven. 2019-10-31. CMSLakeMichiganPPY. Version 1. Carbon Monitoring System Lake Michigan Primary Production Yearly. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/NCJELM4CS8H8. https://disc.gsfc.nasa.gov/datacollection/CMSLakeMichiganPPY_1.html.",
-            "issued": "2019-10-21",
-            "temporal": "2010-01-01T00:00:00Z/2013-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-10-21",
-            "references": [
-                "https://doi.org/10.1016/j.jglr.2016.02.004",
-                "https://doi.org/10.1016/j.jglr.2013.06.017",
-                "https://doi.org/10.1029/2004JC002780"
-            ],
-            "keyword": [
-                "ecological dynamics",
-                "national geospatial data asset",
-                "earth science",
-                "biosphere",
-                "ngda"
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
-            "identifier": "C1652491716-GES_DISC",
-            "description": "Yearly Average primary production/carbon fixation data for Lake Michigan.  The primary production data is derived using MODIS imagery with model data.\n\nThe NASA Carbon Monitoring System (CMS) is designed to make significant contributions in characterizing, quantifying, understanding, and predicting the evolution of global carbon sources and sinks through improved monitoring of carbon stocks and fluxes. The System will use the full range of NASA satellite observations and modeling/analysis capabilities to establish the accuracy, quantitative uncertainties, and utility of products for supporting national and international policy, regulatory, and management activities. CMS will maintain a global emphasis while providing finer scale regional information, utilizing space-based and surface-based data and will rapidly initiate generation and distribution of products both for user evaluation and to inform near-term policy development and planning.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "CMSLakeMichiganPPY",
             "creator": "Gary L. Fahnenstiel, Michael J. Sayers, Robert A. Shuchman, Foad Yousef, & Steven A. Pothoven",
-            "title": "Carbon Monitoring System Lake Michigan Primary Production Yearly V1 (CMSLakeMichiganPPY) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/CMS/CMSLakeMichiganPPY_1.png",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Yearly Average primary production/carbon fixation data for Lake Michigan.  The primary production data is derived using MODIS imagery with model data.\n\nThe NASA Carbon Monitoring System (CMS) is designed to make significant contributions in characterizing, quantifying, understanding, and predicting the evolution of global carbon sources and sinks through improved monitoring of carbon stocks and fluxes. The System will use the full range of NASA satellite observations and modeling/analysis capabilities to establish the accuracy, quantitative uncertainties, and utility of products for supporting national and international policy, regulatory, and management activities. CMS will maintain a global emphasis while providing finer scale regional information, utilizing space-based and surface-based data and will rapidly initiate generation and distribution of products both for user evaluation and to inform near-term policy development and planning.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNCJELM4CS8H8",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNCJELM4CS8H8",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -129874,45 +129845,45 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CMSLakeMichiganPPY_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CMSLakeMichiganPPY_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/CMSLakeMichiganPPY.1",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/CMSLakeMichiganPPY.1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/CMSLakeMichiganPPY.1/doc/README.CMSGreatLakesPrimaryProductivity.V1.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/CMSLakeMichiganPPY.1/doc/README.CMSGreatLakesPrimaryProductivity.V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/opendap/CMS/CMSLakeMichiganPPY.1",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/opendap/CMS/CMSLakeMichiganPPY.1",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=CMSLakeMichiganPPY",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=CMSLakeMichiganPPY",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
@@ -129922,61 +129893,101 @@
                     "title": "This dataset's landing page"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/CMS/CMSLakeMichiganPPY_1.png",
+            "identifier": "C1652491716-GES_DISC",
+            "issued": "2019-10-21",
+            "keyword": [
+                "ecological dynamics",
+                "national geospatial data asset",
+                "earth science",
+                "biosphere",
+                "ngda"
+            ],
+            "landingPage": "https://doi.org/10.5067/NCJELM4CS8H8",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-10-21",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jglr.2016.02.004",
+                "https://doi.org/10.1016/j.jglr.2013.06.017",
+                "https://doi.org/10.1029/2004JC002780"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "CMSLakeMichiganPPY",
             "spatial": "-84.762 43.001 -79.652 46.591",
+            "temporal": "2010-01-01T00:00:00Z/2013-12-31T23:59:59.999Z",
             "theme": [
                 "CMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Carbon Monitoring System Lake Michigan Primary Production Yearly V1 (CMSLakeMichiganPPY) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-URAP-4-SUMM-WFA-PEAK-E-10MIN-V1.0",
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
-                "ulysses"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "A. UDS data files -------------------- Eight files are provided that conform to the UDS conventions regarding the naming of files and the format of the data. The eight files are divided into 4 pairs of files with each pair consisting of a file containing data averaged over a 10 minute period and a file containing the maximum data value during the same 10 minute period. The 4 pairs of file contain data for the RAR, the PFR, WFA - magnetic field, and WFA - magnetic field.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-urap-4-summ-wfa-peak-e-10min-v1.0_4axk-ynaw",
+            "issued": "2018-06-26",
+            "keyword": [
+                "jupiter",
+                "ulysses"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-URAP-4-SUMM-WFA-PEAK-E-10MIN-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-urap-4-summ-wfa-peak-e-10min-v1.0_4axk-ynaw",
-            "description": "A. UDS data files -------------------- Eight files are provided that conform to the UDS conventions regarding the naming of files and the format of the data. The eight files are divided into 4 pairs of files with each pair consisting of a file containing data averaged over a 10 minute period and a file containing the maximum data value during the same 10 minute period. The 4 pairs of file contain data for the RAR, the PFR, WFA - magnetic field, and WFA - magnetic field.",
-            "title": "ULY JUP URAP WAVEFORM ANALYZER PEAK E-FIELD 10 MIN",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ULY JUP URAP WAVEFORM ANALYZER PEAK E-FIELD 10 MIN"
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
+                    "downloadURL": "http://fermi.gsfc.nasa.gov/ssc/data/access/lat/2yr_catalog/gll_psc_v07.xml",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "NASA-0000217__6",
             "issued": "2018-06-25",
-            "temporal": "2008-08-04/2010-07-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "acd",
                 "glast ssc",
@@ -129994,683 +130005,650 @@
                 "gamma",
                 "compton"
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
-            "identifier": "NASA-0000217__6",
-            "description": "The Fermi Gamma-ray Space Telescope (Fermi) Large Area Telescope (LAT) is a successor to EGRET, with greatly improved sensitivity, resolution, and energy range. This web page presents the second full catalog of LAT sources, based on the first 24 months of survey data. For a full explanation about the catalog and its construction see the LAT 2-year Catalog Paper (also available on arxiv).",
-            "title": "LAT 2-year Point Source Catalog",
-            "programCode": [
-                "026:014"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://fermi.gsfc.nasa.gov/ssc/data/access/lat/2yr_catalog/gll_psc_v07.xml",
-                    "mediaType": "application/xml"
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0773-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-05-14T04:54:20.000 to 2015-05-14T06:45:13.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0773-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0773-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0773-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-05-14T04:54:20.000 to 2015-05-14T06:45:13.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0773 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0773 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/KARIN-2PIX1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SWOT. 2022-06-16. SWOT Simulated Level 2 North America Continent KaRIn High Rate Water Mask Pixel Cloud Product Version 1.0. Version 1.0. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/KARIN-2PIX1.",
-            "issued": "2022-04-27",
-            "temporal": "2022-08-01T00:00:00Z/2022-08-22T23:59:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-08-22",
-            "references": [
-                "https://doi.org/10.1007/s10712-015-9346-y"
-            ],
-            "keyword": [
-                "earth science",
-                "terrestrial hydrosphere",
-                "surface water"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Damien Desroches",
                 "hasEmail": "mailto:damien.desroches@cnes.fr"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "identifier": "C2263383386-POCLOUD",
-            "description": "This dataset includes simulated water surface elevations that resemble the Ka-band Interferometer (KaRIn) measurements by the Surface Water and Ocean Topography (SWOT) mission. SWOT will provide a global coverage but this simulated subset focuses on the North America continent. The simulated SWOT KaRIN swaths span 128 km in the cross-swath direction with a 20-km nadir gap. The primary product contains the following: 1. Geolocated elevations (latitude, longitude, and height) 2. Classification mask (water/land flags, and water fraction) 3. Surface areas (projected pixel area on the ground) 4. Relevant data needed to compute and aggregate height and area uncertainties. Additional information includes: 1. Meta data (global instrument parameters) 2. Time varying parameters (TVP), which include sensor position, velocity, altitude, and time 3. Noise power estimates 4. Quality flags 5. Interferogram measurements (power and phase) and range and azimuth indices 6. Geophysical and crossover-calibration correction values. These additional fields are provided to improve the utility of the product and to facilitate generation of downstream products. Note that this is a simulated SWOT product and not suited for any scientific exploration.",
-            "release-place": "PO.DAAC",
-            "graphic-preview-description": "Thumbnail",
             "creator": "SWOT",
-            "title": "SWOT Simulated Level 2  North America Continent KaRIn High Rate Water Mask Pixel Cloud Product Version 1.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_SIMULATED_NA_CONTINENT_L2_HR_PIXC_V1.PNG",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset includes simulated water surface elevations that resemble the Ka-band Interferometer (KaRIn) measurements by the Surface Water and Ocean Topography (SWOT) mission. SWOT will provide a global coverage but this simulated subset focuses on the North America continent. The simulated SWOT KaRIN swaths span 128 km in the cross-swath direction with a 20-km nadir gap. The primary product contains the following: 1. Geolocated elevations (latitude, longitude, and height) 2. Classification mask (water/land flags, and water fraction) 3. Surface areas (projected pixel area on the ground) 4. Relevant data needed to compute and aggregate height and area uncertainties. Additional information includes: 1. Meta data (global instrument parameters) 2. Time varying parameters (TVP), which include sensor position, velocity, altitude, and time 3. Noise power estimates 4. Quality flags 5. Interferogram measurements (power and phase) and range and azimuth indices 6. Geophysical and crossover-calibration correction values. These additional fields are provided to improve the utility of the product and to facilitate generation of downstream products. Note that this is a simulated SWOT product and not suited for any scientific exploration.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FKARIN-2PIX1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FKARIN-2PIX1",
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
-                    "downloadURL": "https://swot.jpl.nasa.gov/",
-                    "description": "SWOT Mission Information Page",
                     "@type": "dcat:Distribution",
+                    "description": "SWOT Mission Information Page",
+                    "downloadURL": "https://swot.jpl.nasa.gov/",
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
-                    "mediaType": "image/png",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_SIMULATED_NA_CONTINENT_L2_HR_PIXC_V1.PNG",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_SIMULATED_NA_CONTINENT_L2_HR_PIXC_V1.PNG",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2263383386-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2263383386-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2263383386-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2263383386-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/swot_mission_docs/pdd/D-56411_SWOT_Product_Description_L2_HR_PIXC_20200810.pdf",
-                    "description": "SWOT Product Description L2_HR_PIXC",
                     "@type": "dcat:Distribution",
+                    "description": "SWOT Product Description L2_HR_PIXC",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/swot_mission_docs/pdd/D-56411_SWOT_Product_Description_L2_HR_PIXC_20200810.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://github.com/CNES/swot-hydrology-toolbox",
-                    "description": "SWOT Hydrology Toolbox",
                     "@type": "dcat:Distribution",
+                    "description": "SWOT Hydrology Toolbox",
+                    "downloadURL": "https://github.com/CNES/swot-hydrology-toolbox",
+                    "mediaType": "text/html",
                     "title": "View the documentation for this dataset's algorithms"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_SIMULATED_NA_CONTINENT_L2_HR_PIXC_V1.PNG",
+            "identifier": "C2263383386-POCLOUD",
+            "issued": "2022-04-27",
+            "keyword": [
+                "earth science",
+                "terrestrial hydrosphere",
+                "surface water"
+            ],
+            "landingPage": "https://doi.org/10.5067/KARIN-2PIX1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-08-22",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.1007/s10712-015-9346-y"
+            ],
+            "release-place": "PO.DAAC",
             "spatial": "-113.0 24.0 -82.0 52.0",
+            "temporal": "2022-08-01T00:00:00Z/2022-08-22T23:59:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SWOT Simulated Level 2  North America Continent KaRIn High Rate Water Mask Pixel Cloud Product Version 1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2CH4LN.007",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2004-07-15. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AURA/TES/TL2CH4LN.007. https://asdc.larc.nasa.gov/project/TES.",
-            "issued": "2015-08-27",
-            "temporal": "2004-08-01T00:00:00Z/2015-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "air quality",
-                "atmospheric chemistry",
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
-            "identifier": "C1607585807-LARC",
             "description": "TL2CH4LN_7 is the Tropospheric Emission Spectrometer (TES)/Aura Level 2 Methane Lite Nadir Version 7 data product. TES was an instrument aboard NASA's Aura satellite and was launched from California on July 15, 2004. Data collection for TES is complete. TES Level 2 data contain retrieved species (or temperature) profiles at the observation targets and the estimated errors. The geolocation, quality, and other data (e.g., surface characteristics for nadir observations) were also provided. L2 modeled spectra were evaluated using radiative transfer modeling algorithms. The process, referred to as retrieval, compared observed spectra to the modeled spectra and iteratively updated the atmospheric parameters. L2 standard product files included information for one molecular species (or temperature) for an entire global survey or special observation run. A global survey consisted of a maximum of 16 consecutive orbits. Nadir and limb observations were in separate L2 files, and a single ancillary file was composed of data that was common to both nadir and limb files.\r\rNadir observations, which point directly to the surface of the Earth, are different from limb observations, which are pointed at various off-nadir angles into the atmosphere. Nadir and limb observations were added to separate L2 files, and a single ancillary file was composed of data that are common to both nadir and limb files. A Nadir sequence within the TES Global Survey was a fixed number of observations within an orbit for a Global Survey. Prior to April 24, 2005, it consisted of two low resolution scans over the same ground locations. After April 24, 2005, Global Survey data consisted of three low resolution scans. The Nadir standard product consists of four files, where each file is composed of the Global Survey Nadir observations from one of four focal planes for a single orbit, i.e. 72 orbit sequences. The Global Survey Nadir observations only used a single set of filter mix. \r\rA Global Survey consisted of observations along 16 consecutive orbits at the start of a two day cycle, over which 4,608 retrievals were performed. Each observation was the input for retrievals of species Volume Mixing Ratios (VMRs), temperature profiles, surface temperature, and other data parameters with associated pressure levels, precision, total error, vertical resolution, total column density, and other diagnostic quantities. Each TES Level 2 standard product reported information in a swath format conforming to the HDF-EOS Aura File Format Guidelines. Each Swath object was bounded by the number of observations in a global survey and a predefined set of pressure levels, representing slices through the atmosphere. Each standard product could have had a variable number of observations depending upon the Global Survey configuration and whether averaging was employed. Also, missing or bad retrievals were not reported. Further, observations were occasionally scheduled on non-global survey days. In general they were measurements made for validation purposes or with highly focused science objectives. Those non-global survey measurements were referred to as \u201cspecial observations.\u201d\r\rA Limb sequence within the TES Global Survey was three high-resolution scans over the same limb locations. The Limb standard product consists of four files, where each file is composed of the Global Survey Limb observations from one of four focal planes for a single orbit, i.e. 72 orbit sequences. The Global Survey Limb observations used a repeating sequence of filter wheel positions. Special Observations could only be scheduled during the 9 or 10 orbit gaps in the Global Surveys, and were conducted in any of three basic modes: stare, transect, step-and-stare. The mode used depended on the science requirement. Each limb observation Limb 1, Limb 2 and Limb 3, were processed independently. Thus, each limb standard product consisted of three sets where each set consisted of 1,152 observations. For TES, the swath object r",
-            "title": "TES/Aura L2 Methane Lite Nadir V007",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2CH4LN.007",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2CH4LN.007",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/cgi-bin/DUE/tes_L2GlbSrvy.cgi",
-                    "description": "Report of TES Level 2 Global Survey Products Available from the ASDC",
                     "@type": "dcat:Distribution",
+                    "description": "Report of TES Level 2 Global Survey Products Available from the ASDC",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/cgi-bin/DUE/tes_L2GlbSrvy.cgi",
+                    "mediaType": "text/html",
                     "title": "View this dataset's production history"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/TES_Lite_Products_Users_Guide.pdf",
-                    "description": "AVDC TES Lite products user\u2019s guide",
                     "@type": "dcat:Distribution",
+                    "description": "AVDC TES Lite products user\u2019s guide",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/TES_Lite_Products_Users_Guide.pdf",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/README_L2_ReadSoftware.txt",
-                    "description": "Basic IDL Tools for extraction information from TES L2 HDF Product files",
                     "@type": "dcat:Distribution",
+                    "description": "Basic IDL Tools for extraction information from TES L2 HDF Product files",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/README_L2_ReadSoftware.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
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
-                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2CH4LN.007",
-                    "description": "DOI data set landing page for TL2CH4LN_7",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TL2CH4LN_7",
+                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2CH4LN.007",
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
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2CH4LN.007/contents.html",
-                    "description": "OPeNDAP data access for TL2CH4LN_7",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for TL2CH4LN_7",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2CH4LN.007/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1607585807-LARC",
-                    "description": "Earthdata Search for TL2CH4LN_7 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TL2CH4LN_7 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1607585807-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2CH4LN.007/",
-                    "description": "ASDC Direct Data Download for TL2CH4LN_7",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for TL2CH4LN_7",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2CH4LN.007/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
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
                 }
             ],
+            "identifier": "C1607585807-LARC",
+            "issued": "2015-08-27",
+            "keyword": [
+                "air quality",
+                "atmospheric chemistry",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2CH4LN.007",
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
+            "temporal": "2004-08-01T00:00:00Z/2015-12-31T23:59:59.999Z",
             "theme": [
                 "TES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TES/Aura L2 Methane Lite Nadir V007"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGN-V-RDRS-5-MIDR-FULL-RES-V1.0",
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
+            "description": "This data set contains the Magellan Full-resolution Mosaic Image Data Records (F-MIDR) which consists of SAR mosaics generated from F-BIDRs (i.e., with 75 meters / pixel). Each F-MIDR is in a sinusoidal equal area projection and has an origin at 0 degrees latitude, with the central meridian defined as the longitude bisecting the mosaic. Each F-MIDR has 7168 lines (aligned with latitude) by 8192 samples, arranged on the CD-ROM as 56 1024 x 1024 files. F-MIDRs have been generated for key terrains on the planet, regions where highest spatial resolution is required for analysis.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgn-v-rdrs-5-midr-full-res-v1.0_4b9r-aj4b",
+            "issued": "2021-05-21",
+            "keyword": [
+                "venus",
+                "magellan"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGN-V-RDRS-5-MIDR-FULL-RES-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgn-v-rdrs-5-midr-full-res-v1.0_4b9r-aj4b",
-            "description": "This data set contains the Magellan Full-resolution Mosaic Image Data Records (F-MIDR) which consists of SAR mosaics generated from F-BIDRs (i.e., with 75 meters / pixel). Each F-MIDR is in a sinusoidal equal area projection and has an origin at 0 degrees latitude, with the central meridian defined as the longitude bisecting the mosaic. Each F-MIDR has 7168 lines (aligned with latitude) by 8192 samples, arranged on the CD-ROM as 56 1024 x 1024 files. F-MIDRs have been generated for key terrains on the planet, regions where highest spatial resolution is required for analysis.",
-            "title": "MGN V RDRS DERIVED MOSAIC IMAGE DATA RECORD FULL RES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MGN V RDRS DERIVED MOSAIC IMAGE DATA RECORD FULL RES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/G2FKY92PRSF5",
             "citation": "Kevin W. Bowman. 2023-10-05. TRPSYL2ALLCRSMGLAG. Version 1. TROPESS CrIS-SNPP L2 for Lagos Megacity, Summary Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/G2FKY92PRSF5. https://disc.gsfc.nasa.gov/datacollection/TRPSYL2ALLCRSMGLAG_1.html. Digital Science Data.",
-            "issued": "2023-08-29",
-            "temporal": "2016-01-02T00:00:00Z/2023-10-09T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-29",
-            "references": [
-                "https://doi.org/10.1126/sciadv.abf7460"
-            ],
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "atmospheric chemistry"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "KEVIN BOWMAN",
                 "hasEmail": "mailto:kevin.w.bowman@jpl.nasa.gov"
             },
+            "creator": "Kevin W. Bowman",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2569846528-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS CrIS-SNPP L2 for Lagos Megacity, Summary Product contains the vertical distribution of six retrieved atmospheric gases (CH4, CO, HDO, NH3, O3 and PAN), along with formal uncertainties measured by the CrIS instrument on the Suomi-NPP satellite. The forward stream summary product is centered on a 3x3 degree region over Lagos for the time period from 2021-02-01 to present. The NASA TRopospheric Ozone and Precursors from Earth System Sounding (TROPESS) project, uses an optimal estimation algorithm, known as the MUlti-SpEctra, MUlti-SpEcies, Multi-SEnsors (MUSES).\n\nThe data files are written in the netCDF version 4 file format, and each file contains one day of data. The data have a spatial resolution of 14 km (CrIS nadir FOV), and are reported at 17 vertical levels from the surface to 0.1 hPa. The principal investigator for the TROPESS project is Kevin W. Bowman.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSYL2ALLCRSMGLAG",
-            "creator": "Kevin W. Bowman",
-            "graphic-preview-description": "TROPESS CrIS-SNPP Lagos Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
-            "title": "TROPESS CrIS-SNPP L2 for Lagos Megacity, Summary Product V1 (TRPSYL2ALLCRSMGLAG) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSYL2ALLCRSMGLAG_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FG2FKY92PRSF5",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FG2FKY92PRSF5",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSYL2ALLCRSMGLAG_Sample.png",
-                    "description": "TROPESS CrIS-SNPP Lagos Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS CrIS-SNPP Lagos Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSYL2ALLCRSMGLAG_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSYL2ALLCRSMGLAG_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSYL2ALLCRSMGLAG_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_MegaCities_Summary/TRPSYL2ALLCRSMGLAG.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_MegaCities_Summary/TRPSYL2ALLCRSMGLAG.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSYL2ALLCRSMGLAG_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSYL2ALLCRSMGLAG_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_MegaCities_Summary/TRPSYL2ALLCRSMGLAG.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_MegaCities_Summary/TRPSYL2ALLCRSMGLAG.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_MegaCities_Summary/TRPSYL2ALLCRSMGLAG.1/doc/TROPESS_Forward_Stream_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_MegaCities_Summary/TRPSYL2ALLCRSMGLAG.1/doc/TROPESS_Forward_Stream_README.pdf",
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
+            "graphic-preview-description": "TROPESS CrIS-SNPP Lagos Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSYL2ALLCRSMGLAG_Sample.png",
+            "identifier": "C2569846528-GES_DISC",
+            "issued": "2023-08-29",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/G2FKY92PRSF5",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-08-29",
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
+            "series-name": "TRPSYL2ALLCRSMGLAG",
             "spatial": "2.0 5.0 5.0 8.0",
+            "temporal": "2016-01-02T00:00:00Z/2023-10-09T00:00:00Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS CrIS-SNPP L2 for Lagos Megacity, Summary Product V1 (TRPSYL2ALLCRSMGLAG) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GGAOD-3MJ63",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Felix Landerer. 2020-03-31. JPL GRACE/GRACE-FO Gridded-AOD1B Water-Equivalent-Thickness Surface-Mass Anomaly dataset for Tellus Level-3 mascon 0.5-degree grid. Version RL06.3. JPL GRACE/GRACE-FO Gridded-AOD1B Water-Equivalent-Thickness Surface-Mass Anomaly RL06.3 dataset for Tellus Level-3 mascon 0.5-degree grid. JPL. Archived by National Aeronautics and Space Administration, U.S. Government, TELLUS. https://doi.org/10.5067/GGAOD-3MJ63. https://doi.org/10.1029/2011WR011453. Felix Landerer, TELLUS, 2020-03-31, JPL GRACE/GRACE-FO Gridded-AOD1B Water-Equivalent-Thickness Surface-Mass Anomaly RL06 dataset for Tellus Level-3 mascon 0.5-degree grid, Landerer F. W. and S. C. Swenson, 2012, Accuracy of scaled GRACE terrestrial water storage estimates. Water Resources Research, Vol 48, W04531, 11 PP, doi:https://doi.org/10.1029/2011WR011453.",
-            "issued": "2020-03-11",
-            "temporal": "2002-04-04T00:00:00Z/2024-11-11T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-03-11",
-            "keyword": [
-                "ocean pressure",
-                "oceans",
-                "earth science",
-                "atmosphere",
-                "atmospheric pressure"
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
-            "identifier": "C3215162709-POCLOUD",
-            "description": "GRACE non-tidal high-frequency atmospheric and oceanic mass variation models are routinely generated at GFZ as so-called Atmosphere and Ocean De-aliasing Level-1B (AOD1B) products (in terms of corresponding spherical harmonic geopotential coefficients) to be added to the background static gravity model during GRACE monthly gravity field determination. AOD1B products are 3-hourly series of spherical harmonic coefficients up to degree and order 180 which are routinely provided to the GRACE Science Data System and the user community with only a few days time delay. These products reflect spatio-temporal mass variations in the atmosphere and oceans deduced from an operational atmospheric model and corresponding ocean dynamics provided by an ocean model. The variability is derived by subtraction of a long-term mean of vertical integrated atmospheric mass distributions and a corresponding mean of ocean bottom pressure as simulated with the ocean model. For further details, please refer to https://www.gfz-potsdam.de/en/aod1b/.\r\n\r\nThe Gridded AOD1B data sets provided here contain the monthly mean AOD1B data in geolocated gridded form, smoothed or spatially aggregated to be consistent with the GRACE and GRACE-FO Tellus Level-3 data products of land and/or ocean mass anomalies. With these gridded AOD1B Level-3 products, users can remove or add the effects of the modeled mean monthly atmospheric and ocean bottom pressure change (e.g., to compare different models).",
-            "release-place": "JPL",
-            "series-name": "JPL GRACE/GRACE-FO Gridded-AOD1B Water-Equivalent-Thickness Surface-Mass Anomaly dataset for Tellus Level-3 mascon 0.5-degree grid",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Felix Landerer",
-            "title": "JPL GRACE/GRACE-FO Gridded-AOD1B Water-Equivalent-Thickness Surface-Mass Anomaly RL06.3 dataset for Tellus Level-3 mascon 0.5-degree grid",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GRC-GFO_GRIDDED_AOD1B_JPL_MASCON_RL06.3.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "GRACE non-tidal high-frequency atmospheric and oceanic mass variation models are routinely generated at GFZ as so-called Atmosphere and Ocean De-aliasing Level-1B (AOD1B) products (in terms of corresponding spherical harmonic geopotential coefficients) to be added to the background static gravity model during GRACE monthly gravity field determination. AOD1B products are 3-hourly series of spherical harmonic coefficients up to degree and order 180 which are routinely provided to the GRACE Science Data System and the user community with only a few days time delay. These products reflect spatio-temporal mass variations in the atmosphere and oceans deduced from an operational atmospheric model and corresponding ocean dynamics provided by an ocean model. The variability is derived by subtraction of a long-term mean of vertical integrated atmospheric mass distributions and a corresponding mean of ocean bottom pressure as simulated with the ocean model. For further details, please refer to https://www.gfz-potsdam.de/en/aod1b/.\r\n\r\nThe Gridded AOD1B data sets provided here contain the monthly mean AOD1B data in geolocated gridded form, smoothed or spatially aggregated to be consistent with the GRACE and GRACE-FO Tellus Level-3 data products of land and/or ocean mass anomalies. With these gridded AOD1B Level-3 products, users can remove or add the effects of the modeled mean monthly atmospheric and ocean bottom pressure change (e.g., to compare different models).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGGAOD-3MJ63",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGGAOD-3MJ63",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gracefo.jpl.nasa.gov/",
-                    "description": "Additional resource and information site for GRACE-FO. This includes update announcements, user feedback page, and FAQ's.",
                     "@type": "dcat:Distribution",
+                    "description": "Additional resource and information site for GRACE-FO. This includes update announcements, user feedback page, and FAQ's.",
+                    "downloadURL": "https://gracefo.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/GRACE-FO",
-                    "description": "PODAAC's GRACE-FO Mission-Page",
                     "@type": "dcat:Distribution",
+                    "description": "PODAAC's GRACE-FO Mission-Page",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/GRACE-FO",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GRC-GFO_GRIDDED_AOD1B_JPL_MASCON_RL06.3.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GRC-GFO_GRIDDED_AOD1B_JPL_MASCON_RL06.3.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/grace/open/docs/AOD1B_PDD_RL06_v6.1.pdf",
-                    "description": "AOD1B Product Description Document for Product Release 6.1 (applicable for the 6.3 release)",
                     "@type": "dcat:Distribution",
+                    "description": "AOD1B Product Description Document for Product Release 6.1 (applicable for the 6.3 release)",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/grace/open/docs/AOD1B_PDD_RL06_v6.1.pdf",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C3215162709-POCLOUD",
-                    "description": "Browse and download granules over HTTPS using the virtual directories",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C3215162709-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C3215162709-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C3215162709-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GRC-GFO_GRIDDED_AOD1B_JPL_MASCON_RL06.3.jpg",
+            "identifier": "C3215162709-POCLOUD",
+            "issued": "2020-03-11",
+            "keyword": [
+                "ocean pressure",
+                "oceans",
+                "earth science",
+                "atmosphere",
+                "atmospheric pressure"
+            ],
+            "landingPage": "https://doi.org/10.5067/GGAOD-3MJ63",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-03-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "JPL",
+            "series-name": "JPL GRACE/GRACE-FO Gridded-AOD1B Water-Equivalent-Thickness Surface-Mass Anomaly dataset for Tellus Level-3 mascon 0.5-degree grid",
             "spatial": "-180.0 -89.5 180.0 89.5",
+            "temporal": "2002-04-04T00:00:00Z/2024-11-11T00:00:00Z",
             "theme": [
                 "GRACE",
                 "GRACE-FO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "JPL GRACE/GRACE-FO Gridded-AOD1B Water-Equivalent-Thickness Surface-Mass Anomaly RL06.3 dataset for Tellus Level-3 mascon 0.5-degree grid"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/8E8EG9HHVDZS",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "J. Harder. 2021-06-17. SOR3SIMD_TAV. Version 002. SORCE SIM Level 3 TSIS-Adjusted Values Solar Spectral Irradiance 24-Hour Means V002. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/8E8EG9HHVDZS. https://disc.gsfc.nasa.gov/datacollection/SOR3SIMD_TAV_002.html. Digital Science Data.",
-            "issued": "2021-06-15",
-            "temporal": "2003-04-14T00:00:00Z/2020-02-25T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-06-15",
-            "keyword": [
-                "solar activity",
-                "sun-earth interactions",
-                "earth science"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JERRY HARDER",
                 "hasEmail": "mailto:Jerry.Harder@lasp.colorado.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C2069458519-GES_DISC",
-            "description": "Version 002 is the most recent version of this data product, and supersedes all previous versions.\n\nThe SORCE SIM Level 3 TSIS-Adjusted Values Solar Spectral Irradiance 24-Hour Means data product (SOR3SIMD_TAV) uses the temporal overlap of the Solar Radiation and Climate Experiment (SORCE) and the Total and Spectral Solar Irradiance Sensor (TSIS-1) Spectral Irradiance Monitor (SIM) instruments to create an alternate SORCE-SIM irradiance calibration, known as the TSIS1 Adjusted Values (TAV). The SORCE-SIM Solar Spectral Irradiance (SSI) data products are provided on a fixed wavelength scale which varies in spectral resolution from 1-34 nm over the spectral range from 240 to 2401 nm. Irradiances are reported at a mean solar distance of 1 AU and zero relative line-of-sight velocity with respect to the Sun. The TAV data is on the SORCE-SIM wavelength scale, with the exception that the longest TAV wavelength is 2401.4 nm.\n\nAll of the SOR3SIMD_TAV data are arranged in a single file in a tabular ASCII text file which can be easily read into a spreadsheet application. The columns contain the date, Julian day, minimum wavelength, maximum wavelength, instrument mode, data version number, irradiance value, irradiance uncertainty, and data quality. The rows are arranged with data at each wavelength over the full SIM wavelength range, repeating for each day for the length of the measurement period.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "SOR3SIMD_TAV",
             "creator": "J. Harder",
-            "title": "SORCE SIM Level 3 TSIS-Adjusted Values Solar Spectral Irradiance 24-Hour Means V002 (SOR3SIMD_TAV) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SORCE_Logo.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Version 002 is the most recent version of this data product, and supersedes all previous versions.\n\nThe SORCE SIM Level 3 TSIS-Adjusted Values Solar Spectral Irradiance 24-Hour Means data product (SOR3SIMD_TAV) uses the temporal overlap of the Solar Radiation and Climate Experiment (SORCE) and the Total and Spectral Solar Irradiance Sensor (TSIS-1) Spectral Irradiance Monitor (SIM) instruments to create an alternate SORCE-SIM irradiance calibration, known as the TSIS1 Adjusted Values (TAV). The SORCE-SIM Solar Spectral Irradiance (SSI) data products are provided on a fixed wavelength scale which varies in spectral resolution from 1-34 nm over the spectral range from 240 to 2401 nm. Irradiances are reported at a mean solar distance of 1 AU and zero relative line-of-sight velocity with respect to the Sun. The TAV data is on the SORCE-SIM wavelength scale, with the exception that the longest TAV wavelength is 2401.4 nm.\n\nAll of the SOR3SIMD_TAV data are arranged in a single file in a tabular ASCII text file which can be easily read into a spreadsheet application. The columns contain the date, Julian day, minimum wavelength, maximum wavelength, instrument mode, data version number, irradiance value, irradiance uncertainty, and data quality. The rows are arranged with data at each wavelength over the full SIM wavelength range, repeating for each day for the length of the measurement period.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F8E8EG9HHVDZS",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F8E8EG9HHVDZS",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -130680,216 +130658,240 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/SORCE_Level3/SOR3SIMD_TAV.002/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/SORCE_Level3/SOR3SIMD_TAV.002/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SOR3SIMD_TAV_002",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SOR3SIMD_TAV_002",
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
-                    "downloadURL": "http://lasp.colorado.edu/home/sorce/instruments/sim/sorce-sim-data-products-release-notes/",
-                    "description": "SIM Release Notes",
                     "@type": "dcat:Distribution",
+                    "description": "SIM Release Notes",
+                    "downloadURL": "http://lasp.colorado.edu/home/sorce/instruments/sim/sorce-sim-data-products-release-notes/",
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
+            "identifier": "C2069458519-GES_DISC",
+            "issued": "2021-06-15",
+            "keyword": [
+                "solar activity",
+                "sun-earth interactions",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/8E8EG9HHVDZS",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-06-15",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "SOR3SIMD_TAV",
+            "temporal": "2003-04-14T00:00:00Z/2020-02-25T23:59:59.999Z",
             "theme": [
                 "SORCE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SORCE SIM Level 3 TSIS-Adjusted Values Solar Spectral Irradiance 24-Hour Means V002 (SOR3SIMD_TAV) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Suborbital/LISTOS/Ground_QueensCollege_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2020-12-16. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/Suborbital/LISTOS/Ground_QueensCollege_Data_1.",
-            "issued": "2020-09-08",
-            "temporal": "2018-04-30T00:00:00Z/2019-06-14T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-18",
-            "keyword": [
-                "atmosphere",
-                "atmospheric chemistry",
-                "air quality",
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
-            "identifier": "C1981394321-LARC_ASDC",
             "description": "LISTOS_Ground_QueensCollege_Data is the Long Island Sound Tropospheric Ozone Study (LISTOS) ground site data collected at the Queens College ground site during the LISTOS field campaign. This product is a result of a joint effort across multiple agencies, including NASA, NOAA, the EPA Northeast States for Coordinated Air Use Management (NESCAUM), Maine Department of Environmental Protection, New Jersey Department of Environmental Protection, New York State Department of Environmental Conservation and several research groups at universities. Data collection is complete.\r\n\r\nThe New York City (NYC) metropolitan area (comprised of portions of New Jersey, New York, and Connecticut in and around NYC) is home to over 20 million people, but also millions of people living downwind in neighboring states. This area continues to persistently have challenges meeting past and recently revised federal health-based air quality standards for ground-level ozone, which impacts the health and well-being of residents living in the area. A unique feature of this chronic ozone problem is the pollution transported in a northeast direction out of NYC over Long Island Sound. The relatively cool waters of Long Island Sound confine the pollutants in a shallow and stable marine boundary layer. Afternoon heating over coastal land creates a sea breeze that carries the air pollution inland from the confined marine layer, resulting in high ozone concentrations in Connecticut and, at times, farther east into Rhode Island and Massachusetts. To investigate the evolving nature of ozone formation and transport in the NYC region and downwind, Northeast States for Coordinated Air Use Management (NESCAUM) launched the Long Island Sound Tropospheric Ozone Study (LISTOS). LISTOS was a multi-agency collaborative study focusing on Long Island Sound and the surrounding coastlines that continually suffer from poor air quality exacerbated by land/water circulation. The primary measurement observations took place between June-September 2018 and include in-situ and remote sensing instrumentation that were integrated aboard three aircraft, a network of ground sites, mobile vehicles, boat measurements, and ozonesondes. The goal of LISTOS was to improve the understanding of ozone chemistry and sea breeze transported pollution over Long Island Sound and its coastlines. LISTOS also provided NASA the opportunity to test air quality remote sensing retrievals with the use of its airborne simulators (GEOstationary Coastal and Air Pollution Events (GEO-CAPE) Airborne Simulator (GCAS), and Geostationary Trace gas and Aerosol Sensory Optimization (GeoTASO)) for the preparation of the Tropospheric Emissions; Monitoring of Pollution (TEMPO) observations for monitoring air quality from space. LISTOS also helped collaborators in the validation of Tropospheric Monitoring Instrument (TROPOMI) science products, with use of airborne- and ground-based measurements of ozone, NO2, and HCHO.",
-            "title": "LISTOS Queens College Ground Site Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSuborbital%2FLISTOS%2FGround_QueensCollege_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSuborbital%2FLISTOS%2FGround_QueensCollege_Data_1",
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
-                    "downloadURL": "https://www.nescaum.org/documents/listos",
-                    "description": "NESCAUM Project Page for Long Island Sound Tropospheric Ozone Study (LISTOS)",
                     "@type": "dcat:Distribution",
+                    "description": "NESCAUM Project Page for Long Island Sound Tropospheric Ozone Study (LISTOS)",
+                    "downloadURL": "https://www.nescaum.org/documents/listos",
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
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/Suborbital/LISTOS/Ground_QueensCollege_Data_1",
-                    "description": "DOI data set landing page for LISTOS_Ground_QueensCollege_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for LISTOS_Ground_QueensCollege_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/Suborbital/LISTOS/Ground_QueensCollege_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/LISTOS/2017",
-                    "description": "LISTOS Data on the Sub-Orbital Order Tool (SOOT) Power User Interface (UI)",
                     "@type": "dcat:Distribution",
+                    "description": "LISTOS Data on the Sub-Orbital Order Tool (SOOT) Power User Interface (UI)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/LISTOS/2017",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1981394321-LARC_ASDC",
-                    "description": "Earthdata Search for LISTOS_Ground_QueensCollege_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for LISTOS_Ground_QueensCollege_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1981394321-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/LISTOS/pdocuments",
-                    "description": "LISTOS Support Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "LISTOS Support Documentation",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/LISTOS/pdocuments",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/LISTOS/2018",
-                    "description": "LISTOS 2018 Data on the Sub-Orbital Order Tool (SOOT) Power User Interface (UI)",
                     "@type": "dcat:Distribution",
+                    "description": "LISTOS 2018 Data on the Sub-Orbital Order Tool (SOOT) Power User Interface (UI)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/LISTOS/2018",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through the Sub-Orbital Order Tool"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/LISTOS/Ground_QueensCollege_Data_1/",
-                    "description": "ASDC Direct Data Download for LISTOS_Ground_QueensCollege_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for LISTOS_Ground_QueensCollege_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/LISTOS/Ground_QueensCollege_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1981394321-LARC_ASDC",
+            "issued": "2020-09-08",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "air quality",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Suborbital/LISTOS/Ground_QueensCollege_Data_1",
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
+            "temporal": "2018-04-30T00:00:00Z/2019-06-14T23:59:59.999Z",
             "theme": [
                 "LISTOS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LISTOS Queens College Ground Site Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-PLS-5-RTS-MOMENTS-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "TBD",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-pls-5-rts-moments-v1.0_4bet-dtp9",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "io",
                 "callisto",
@@ -130898,852 +130900,852 @@
                 "ganymede",
                 "europa"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-PLS-5-RTS-MOMENTS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-pls-5-rts-moments-v1.0_4bet-dtp9",
-            "description": "TBD",
-            "title": "GALILEO JUPITER RTS MOMENT DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GALILEO JUPITER RTS MOMENT DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASTER/AST_L1BE.003",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA/METI/AIST/Japan Spacesystems and U.S./Japan ASTER Science Team. 2001-04-30. AST_L1BE.003. Expedited ASTER Level 1B Data Set Registered Radiance at the Sensor. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes DAAC. https://doi.org/10.5067/ASTER/AST_L1BE.003. https://doi.org/10.5067/ASTER/AST_L1BE.003. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2002-03-14",
-            "temporal": "2000-03-04T20:34:04Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-09-14",
-            "keyword": [
-                "national geospatial data asset",
-                "spectral/engineering",
-                "infrared wavelengths",
-                "ngda",
-                "earth science",
-                "visible wavelengths"
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
-            "identifier": "C179460406-LPDAAC_ECS",
-            "description": "The Advanced Spaceborne Thermal Emission and Reflection Radiometer (ASTER) Expedited Level 1B Registered Radiance at the Sensor data product is radiometrically calibrated and geometrically co-registered. Application of intra-telescope and inter-telescope registration corrections for all bands are relative to the reference band for each telescope: Visible  and Near Infrared (VNIR) Band 2, Shortwave Infrared (SWIR) Band 6, and Thermal Infrared (TIR) Band 11. The Expedited Level 1B data product is similar to the (AST_L1B) (https://doi.org/10.5067/ASTER/AST_L1B.003) with a few notable exceptions. These include:\r\n* The AST_L1BE is available for download within 48 hours of acquisition in support of field calibration and validation efforts, in addition to emergency response for natural disasters where the quick turn-around time from acquisition to availability would prove beneficial in initial damage or impact assessments.\r\n* The registration quality of the AST_L1BE is likely to be lower than the AST_L1B, and may vary from scene to scene.\r\n* The AST_L1BE dataset does not contain the VNIR 3B (aft-viewing) Band.\r\n* This dataset does not have short-term calibration for the Thermal Infrared (TIR) sensor.",
-            "series-name": "AST_L1BE.003",
             "creator": "NASA/METI/AIST/Japan Spacesystems and U.S./Japan ASTER Science Team",
-            "title": "ASTER Expedited L1B Registered Radiance at the Sensor V003",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Advanced Spaceborne Thermal Emission and Reflection Radiometer (ASTER) Expedited Level 1B Registered Radiance at the Sensor data product is radiometrically calibrated and geometrically co-registered. Application of intra-telescope and inter-telescope registration corrections for all bands are relative to the reference band for each telescope: Visible  and Near Infrared (VNIR) Band 2, Shortwave Infrared (SWIR) Band 6, and Thermal Infrared (TIR) Band 11. The Expedited Level 1B data product is similar to the (AST_L1B) (https://doi.org/10.5067/ASTER/AST_L1B.003) with a few notable exceptions. These include:\r\n* The AST_L1BE is available for download within 48 hours of acquisition in support of field calibration and validation efforts, in addition to emergency response for natural disasters where the quick turn-around time from acquisition to availability would prove beneficial in initial damage or impact assessments.\r\n* The registration quality of the AST_L1BE is likely to be lower than the AST_L1B, and may vary from scene to scene.\r\n* The AST_L1BE dataset does not contain the VNIR 3B (aft-viewing) Band.\r\n* This dataset does not have short-term calibration for the Thermal Infrared (TIR) sensor.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASTER%2FAST_L1BE.003",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASTER%2FAST_L1BE.003",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASTER/AST_L1BE.003",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ASTER/AST_L1BE.003",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/ASTT/AST_L1BE.003/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/ASTT/AST_L1BE.003/",
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
-                    "downloadURL": "http://asterweb.jpl.nasa.gov/",
-                    "description": "The ASTER home page is maintained through NASA's Jet Propulsion Laboratory and documents various aspects of the ASTER mission.      ",
                     "@type": "dcat:Distribution",
+                    "description": "The ASTER home page is maintained through NASA's Jet Propulsion Laboratory and documents various aspects of the ASTER mission.      ",
+                    "downloadURL": "http://asterweb.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C179460406-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C179460406-LPDAAC_ECS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
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
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/69/AST_L1_User_Guide_V3.pdf",
-                    "description": "ASTER Level-1 User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "ASTER Level-1 User Guide",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/69/AST_L1_User_Guide_V3.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asterweb.jpl.nasa.gov/content/03_data/04_Documents/ASTERHigherLevelUserGuideVer2May01.pdf",
-                    "description": "ASTER Higher-Level Product User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "ASTER Higher-Level Product User Guide",
+                    "downloadURL": "https://asterweb.jpl.nasa.gov/content/03_data/04_Documents/ASTERHigherLevelUserGuideVer2May01.pdf",
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
+            "identifier": "C179460406-LPDAAC_ECS",
+            "issued": "2002-03-14",
+            "keyword": [
+                "national geospatial data asset",
+                "spectral/engineering",
+                "infrared wavelengths",
+                "ngda",
+                "earth science",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASTER/AST_L1BE.003",
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
+            "series-name": "AST_L1BE.003",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-03-04T20:34:04Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Terra",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ASTER Expedited L1B Registered Radiance at the Sensor V003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-CHEMCAM-SOH-2-EDR-V1.0",
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
+            "description": "The MSL ChemCam SOH EDR data set consists of all raw state of health data collected by the ChemCam instrument on the Mars Science Laboratory rover.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-chemcam-soh-2-edr-v1.0_4bga-9skc",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars science laboratory",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-CHEMCAM-SOH-2-EDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-chemcam-soh-2-edr-v1.0_4bga-9skc",
-            "description": "The MSL ChemCam SOH EDR data set consists of all raw state of health data collected by the ChemCam instrument on the Mars Science Laboratory rover.",
-            "title": "MSL CHEMCAM STATE OF HEALTH EDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MSL CHEMCAM STATE OF HEALTH EDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/GCPEX/METTOWER/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hudak, David .2013. GPM GROUND VALIDATION METEOROLOGICAL TOWER ENVIRONMENT CANADA GCPEX [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/GCPEX/METTOWER/DATA101",
-            "issued": "2013-04-30",
-            "temporal": "2012-01-15T00:00:00Z/2012-03-01T23:59:58Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-24",
-            "keyword": [
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "earth science",
-                "atmospheric winds",
-                "atmosphere",
-                "atmospheric pressure",
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
-            "identifier": "C1979620588-GHRC_DAAC",
             "description": "The GPM Ground Validation Meteorological Tower Environment Canada GCPEx dataset provides temperature, relative humidity, 10 m winds, pressure and solar radiation data collected by a suite of standard meteorological instruments attached to a 10 m met tower. The GPM Cold-season Precipitation Experiment (GCPEx) addressed shortcomings in the GPM snowfall retrieval algorithm by collecting microphysical properties, associated remote sensing observations, and coordinated model simulations of precipitating snow. Data was gathered over the Ontario region of Canada in 2012 from January 15th through March 1st. Browse images are available online. The observation station was assembled by Automated Transportable Meteorological Observation Station (ATMOS).",
-            "graphic-preview-description": "N/A",
-            "title": "GPM GROUND VALIDATION METEOROLOGICAL TOWER ENVIRONMENT CANADA GCPEX V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/met_tower_EC/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FGCPEX%2FMETTOWER%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FGCPEX%2FMETTOWER%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmmettecgcpex",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmmettecgcpex",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/met_tower_EC/browse/STEAMSHOW/gcpex_met_20120124_EC_STEAMSHOW.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/met_tower_EC/browse/STEAMSHOW/gcpex_met_20120124_EC_STEAMSHOW.png",
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
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/gpmgv/gcpex/gpmmettecgcpex/gpmmettecgcpex_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/gpmgv/gcpex/gpmmettecgcpex/gpmmettecgcpex_dataset.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/gpmgv/gcpex/gpmmettecgcpex/GCPEX_Met_Tower_instruments.html",
-                    "description": "GCPEX Met Tower Instruments",
                     "@type": "dcat:Distribution",
+                    "description": "GCPEX Met Tower Instruments",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/gpmgv/gcpex/gpmmettecgcpex/GCPEX_Met_Tower_instruments.html",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/gpmgv/gcpex/gpmmettecgcpex/GCPEX_MET_decipher.txt",
-                    "description": "Data Deciphering(format) information",
                     "@type": "dcat:Distribution",
+                    "description": "Data Deciphering(format) information",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/gpmgv/gcpex/gpmmettecgcpex/GCPEX_MET_decipher.txt",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/met_tower_EC/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/met_tower_EC/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/met_tower_EC/browse/",
+            "identifier": "C1979620588-GHRC_DAAC",
+            "issued": "2013-04-30",
+            "keyword": [
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "earth science",
+                "atmospheric winds",
+                "atmosphere",
+                "atmospheric pressure",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/GCPEX/METTOWER/DATA101",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-05-24",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/MSFC/GHRC"
+            },
             "spatial": "-79.93 44.18 -79.64 44.69",
+            "temporal": "2012-01-15T00:00:00Z/2012-03-01T23:59:58Z",
             "theme": [
                 "GCPEx",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM GROUND VALIDATION METEOROLOGICAL TOWER ENVIRONMENT CANADA GCPEX V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0325-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-09-29T16:18:55.000 to 2014-09-29T22:55:43.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0325-v1.0_4bii-mgnw",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0325-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0325-v1.0_4bii-mgnw",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-09-29T16:18:55.000 to 2014-09-29T22:55:43.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0325 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0325 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/596",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Rapalee, G., and J.E. Nickeson. 2001. BOREAS Follow-On DSP-09 Saskatchewan Raster Forest Fire Chronology, 1945-1996. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/596",
-            "issued": "2024-04-27",
-            "temporal": "1945-01-01T00:00:00Z/1997-01-01T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-28",
-            "keyword": [
-                "earth science",
-                "biosphere",
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
-            "identifier": "C2956514059-ORNL_CLOUD",
             "description": "This data set contains a pair of raster images and a spreadsheet chronicling the most recent fire history of Saskatchewan from 1945 to 1996.  This data set was developed from a series of ARC/INFO export files of annual fire data  compiled and provided by the Saskatchewan Environment and Resource Management (SERM) Wildlife Branch.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS Follow-On DSP-09 Saskatchewan Raster Forest Fire Chronology, 1945-1996",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F596",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F596",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/DSP/BFO_dsp09_sask_fire_map/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/DSP/BFO_dsp09_sask_fire_map/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/FollowOn/guides/dsp09_sask_fires_raster_doc.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/FollowOn/guides/dsp09_sask_fires_raster_doc.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/596",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/596",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/DSP/BFO_dsp09_sask_fire_map/comp/0_readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/DSP/BFO_dsp09_sask_fire_map/comp/0_readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/DSP/BFO_dsp09_sask_fire_map/comp/dsp09_sask_fires_raster_doc.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/DSP/BFO_dsp09_sask_fire_map/comp/dsp09_sask_fires_raster_doc.pdf",
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
-            "spatial": "-111.0 48.0 -90.0 60.0",
-            "theme": [
-                "BOREAS",
-                "geospatial"
-            ],
-            "language": [
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
+            "identifier": "C2956514059-ORNL_CLOUD",
+            "issued": "2024-04-27",
+            "keyword": [
+                "earth science",
+                "biosphere",
+                "ecological dynamics"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/596",
+            "language": [
                 "en-US"
-            ]
+            ],
+            "modified": "2024-04-28",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
+            "spatial": "-111.0 48.0 -90.0 60.0",
+            "temporal": "1945-01-01T00:00:00Z/1997-01-01T23:59:59Z",
+            "theme": [
+                "BOREAS",
+                "geospatial"
+            ],
+            "title": "BOREAS Follow-On DSP-09 Saskatchewan Raster Forest Fire Chronology, 1945-1996"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-GRAND-5-VESTA-GAMMA-IRON-UNC-V1.0",
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
-                "4 vesta",
-                "dawn mission to vesta and ceres"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set provides tables of         net counting rates of Fe gamma rays at 7.6 MeV measured by the BGO      detector of Dawn's Gamma Ray and Neutron Detector acquired at the       low altitude mapping orbit. The counting rates are accompanied by       their 1-sigma standard errors of the mean and average numbers of        5-deg pixels used to derive the 30-deg counting rates and errors.       The counting rates were normalized for variations of live time,         solid angle of Vesta, and galactic cosmic ray intensity, but were       not corrected for variations of neutron number density. The table       contains the original Fe counting rates and errors reported by          YAMASHITAETAL2013.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-grand-5-vesta-gamma-iron-unc-v1.0_4bnu-cddv",
+            "issued": "2018-06-26",
+            "keyword": [
+                "4 vesta",
+                "dawn mission to vesta and ceres"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-GRAND-5-VESTA-GAMMA-IRON-UNC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-grand-5-vesta-gamma-iron-unc-v1.0_4bnu-cddv",
-            "description": "This data set provides tables of         net counting rates of Fe gamma rays at 7.6 MeV measured by the BGO      detector of Dawn's Gamma Ray and Neutron Detector acquired at the       low altitude mapping orbit. The counting rates are accompanied by       their 1-sigma standard errors of the mean and average numbers of        5-deg pixels used to derive the 30-deg counting rates and errors.       The counting rates were normalized for variations of live time,         solid angle of Vesta, and galactic cosmic ray intensity, but were       not corrected for variations of neutron number density. The table       contains the original Fe counting rates and errors reported by          YAMASHITAETAL2013.",
-            "title": "DAWN GRAND MAP VESTA GAMMA FE           \n                                     UNCORRECTED COUNTS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "DAWN GRAND MAP VESTA GAMMA FE           \n                                     UNCORRECTED COUNTS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/HNAUGJQXSCVU",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "High Mountain Asia UCLA Daily Snow Reanalysis V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/HNAUGJQXSCVU.",
-            "issued": "1999-10-01",
-            "temporal": "1999-10-01T00:00:00Z/2017-09-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-09-30",
-            "keyword": [
-                "national geospatial data asset",
-                "ngda",
-                "snow/ice",
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
-            "identifier": "C2037494637-NSIDC_ECS",
             "description": "Snowpack plays a significant role in the hydrologic cycle over High Mountain Asia (HMA). As a vital water resource, the distribution of snowpack volume also impacts the water availability for downstream populations. To assess the regional water balance, it is important to characterize the spatio-temporal distribution of water storage in the HMA snowpack.\nThis HMA snow reanalysis data set contains daily estimates of posterior snow water equivalent (SWE), fractional snow covered area (fSCA), snow depth (SD), etc.",
-            "title": "High Mountain Asia UCLA Daily Snow Reanalysis V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FHNAUGJQXSCVU",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FHNAUGJQXSCVU",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/HMA/HMA_SR_D.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/HMA/HMA_SR_D.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2037494637-NSIDC_ECS&tl=1603306463%214%21%21&m=13.871524500788853%2128.354494094848633%212%211%210%210%2C2",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2037494637-NSIDC_ECS&tl=1603306463%214%21%21&m=13.871524500788853%2128.354494094848633%212%211%210%210%2C2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/HMA_SR_D/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/HMA_SR_D/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/HNAUGJQXSCVU",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/HNAUGJQXSCVU",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/HNAUGJQXSCVU",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/HNAUGJQXSCVU",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2037494637-NSIDC_ECS",
+            "issued": "1999-10-01",
+            "keyword": [
+                "national geospatial data asset",
+                "ngda",
+                "snow/ice",
+                "cryosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/HNAUGJQXSCVU",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-09-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "60.0 27.0 105.0 45.0",
+            "temporal": "1999-10-01T00:00:00Z/2017-09-30T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "High Mountain Asia UCLA Daily Snow Reanalysis V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Ainsight-ifg-cruise&version=1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This bundle contains InSight IFG Cruise data and associated products",
+            "identifier": "urn:nasa:pds:insight-ifg-cruise",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "insight mars lander mission",
                 "solar wind",
                 "mag"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Ainsight-ifg-cruise&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:insight-ifg-cruise",
-            "description": "This bundle contains InSight IFG Cruise data and associated products",
-            "title": "InSight IFG Cruise Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "InSight IFG Cruise Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/199",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Vorosmarty, C. J., B. M. Fekete, and B. A. Tucker. 1998. Global River Discharge, 1807-1991, V. 1.1 (RivDIS). ORNL DAAC, Oak Ridge Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/199",
-            "issued": "2023-08-23",
-            "temporal": "1807-01-01T00:00:00Z/1991-09-30T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-24",
-            "keyword": [
-                "terrestrial hydrosphere",
-                "earth science",
-                "surface water"
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
-            "identifier": "C2756230785-ORNL_CLOUD",
             "description": "The Global Monthly River Discharge Data Set (RivDIS) contains monthly averaged discharge measurements for 1,018 stations located throughout the world from 1807-1991. The period of record varies widely from station to station with a mean of 21.5 years. The data are derived from the published UNESCO archives for river discharge, and checked against information obtained from the Global Runoff Center in Koblenz, Germany through the U.S. National Geophysical Data Center in Boulder, Colorado.",
-            "graphic-preview-description": "Browse Image",
-            "title": "Global River Discharge, 1807-1991, V[ersion]. 1.1 (RivDIS)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/hydroclimatology_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F199",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F199",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/global_hydroclimatology/rivdis/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/global_hydroclimatology/rivdis/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/RIVDIS/guides/rivdis_guide.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/RIVDIS/guides/rivdis_guide.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/199",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/199",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_hydroclimatology/rivdis/comp/README",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_hydroclimatology/rivdis/comp/README",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_hydroclimatology/rivdis/comp/rivdis_guide.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_hydroclimatology/rivdis/comp/rivdis_guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_hydroclimatology/rivdis/comp/STATION.DAT",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_hydroclimatology/rivdis/comp/STATION.DAT",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/hydroclimatology_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/hydroclimatology_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/hydroclimatology_logo_square.png",
+            "identifier": "C2756230785-ORNL_CLOUD",
+            "issued": "2023-08-23",
+            "keyword": [
+                "terrestrial hydrosphere",
+                "earth science",
+                "surface water"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/199",
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
             "spatial": "-178.5 -47.35 176.73 72.12",
+            "temporal": "1807-01-01T00:00:00Z/1991-09-30T23:59:59Z",
             "theme": [
                 "Hydroclimatology",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global River Discharge, 1807-1991, V[ersion]. 1.1 (RivDIS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-C-CONSERT-2-LTS-V1.0",
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
+            "description": "This archive contains edited (CODMAC level 2) data that refers to target 67P  from the CONSERT instrument onboard ROSETTA Orbiter, acquired  during LTS (Long Term Science) mission phase. It also contains documentation which describes the CONSERT experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-c-consert-2-lts-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-C-CONSERT-2-LTS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-c-consert-2-lts-v1.0",
-            "description": "This archive contains edited (CODMAC level 2) data that refers to target 67P  from the CONSERT instrument onboard ROSETTA Orbiter, acquired  during LTS (Long Term Science) mission phase. It also contains documentation which describes the CONSERT experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-ORBITER/ROSETTA-LANDER 67P CONSERT\n                           2 LTS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER/ROSETTA-LANDER 67P CONSERT\n                           2 LTS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/350",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Saugier, B. 1999. BOREAS TE-11 Surface Meteorological Data. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/350",
-            "issued": "2023-11-22",
-            "temporal": "1994-01-01T00:00:00Z/1994-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-28",
-            "keyword": [
-                "soils",
-                "biosphere",
-                "atmospheric water vapor",
-                "atmospheric winds",
-                "atmospheric temperature",
-                "atmospheric radiation",
-                "earth science",
-                "land surface",
-                "precipitation",
-                "surface thermal properties",
-                "vegetation",
-                "atmospheric pressure",
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
-            "identifier": "C2808129935-ORNL_CLOUD",
             "description": "Data collected in support of efforts to characterize and interpret information on the sapflow, gas exchange, and lichen photosynthesis.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS TE-11 Surface Meteorological Data",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F350",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F350",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TE/te11smet/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TE/te11smet/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TE11_Surf_Met.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TE11_Surf_Met.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/350",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/350",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te11smet/comp/te11smet.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te11smet/comp/te11smet.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te11smet/comp/TE11_Surf_Met.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te11smet/comp/TE11_Surf_Met.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te11smet/comp/TE11_Surf_Met.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te11smet/comp/TE11_Surf_Met.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te11smet/comp/TE11_Surf_Met.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te11smet/comp/TE11_Surf_Met.txt",
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
+            "identifier": "C2808129935-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "soils",
+                "biosphere",
+                "atmospheric water vapor",
+                "atmospheric winds",
+                "atmospheric temperature",
+                "atmospheric radiation",
+                "earth science",
+                "land surface",
+                "precipitation",
+                "surface thermal properties",
+                "vegetation",
+                "atmospheric pressure",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/350",
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
+            "temporal": "1994-01-01T00:00:00Z/1994-12-31T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS TE-11 Surface Meteorological Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSIWAC-3-CVP2-CHECKOUT-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the COMMISSIONING 2 mission phase, covering the period  from 2004-09-06T00:00:00.000 to 2004-10-16T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. After the October 2018 PSA/PDS external peer review, the COMMISSIONING  data set was reprocessed and split into multiple data sets.  This  version V1.0 is one part and supersedes the previous delivery.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osiwac-3-cvp2-checkout-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "m42",
                 "vega",
@@ -131754,785 +131756,785 @@
                 "16 cyg b",
                 "earth"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSIWAC-3-CVP2-CHECKOUT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osiwac-3-cvp2-checkout-v1.0",
-            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the COMMISSIONING 2 mission phase, covering the period  from 2004-09-06T00:00:00.000 to 2004-10-16T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. After the October 2018 PSA/PDS external peer review, the COMMISSIONING  data set was reprocessed and split into multiple data sets.  This  version V1.0 is one part and supersedes the previous delivery.",
-            "title": "ROSETTA-ORBITER CHECKOUT OSIWAC 3 CVP2 RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECKOUT OSIWAC 3 CVP2 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1813",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wang, C., K. Guan, B. Peng, C. Jiang, J. Peng, G. Wu, C. Frankenberg, P. Koehler, X. Yang, Y. Cai, and Y. Huang. 2021. High Resolution Land Cover-Specific Solar-Induced Fluorescence, Midwestern USA, 2018. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1813",
-            "issued": "2021-03-15",
-            "temporal": "2018-05-02T00:00:00Z/2018-09-23T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-17",
-            "keyword": [
-                "biosphere",
-                "vegetation",
-                "ngda",
-                "national geospatial data asset",
-                "land use/land cover",
-                "land surface",
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
-            "identifier": "C2345900038-ORNL_CLOUD",
             "description": "This dataset provides estimated solar-induced chlorophyll fluorescence (SIF) of specific vegetation types and total SIF under clear-sky and real/cloudy conditions at a resolution of 4 km for the Midwest USA. The estimates are 8-day averaged daily means over the 2018 crop growing season for the time period 2018-05-01 to 2018-09-29. SIF of a specific vegetation type (i.e., corn, soybean, grass/pasture, forest) was expressed as the product of photosynthetically active radiation (PAR), the fraction of photosynthetically active radiation absorbed by the canopy (fPAR), and canopy SIF yield (SIFyield) for each vegetation type. Uncertainty of each variable was also calculated and is provided. These components of the SIF model were derived using a TROPOspheric Monitoring Instrument (TROPOMI) dataset, the USDA National Agricultural Statistics Service Cropland Data Layer, and the MODIS MCD15A2H 8-day 500 m fPAR product. These data could be used to improve estimates of vegetation productivity and vegetation stress.",
-            "graphic-preview-description": "Examples of spatial patterns of reconstructed SIF at 4 km resolution. Only pixels with a fraction of the specific vegetation type larger than 0.1 are shown. For Total SIF, only pixels with a fraction of corn, soybean, grass/pasture, and forest larger than 0.8 are displayed. Source: Wang et al., 2020.",
-            "title": "High Resolution Land Cover-Specific Solar-Induced Fluorescence, Midwestern USA, 2018",
-            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/SIF_PAR_fPAR_US_Midwest_2018_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1813",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1813",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/cms/SIF_PAR_fPAR_US_Midwest_2018/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/cms/SIF_PAR_fPAR_US_Midwest_2018/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/SIF_PAR_fPAR_US_Midwest_2018.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/SIF_PAR_fPAR_US_Midwest_2018.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1813",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1813",
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
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/SIF_PAR_fPAR_US_Midwest_2018/comp/SIF_PAR_fPAR_US_Midwest_2018.pdf",
-                    "description": "High Resolution Land Cover-Specific Solar-Induced Fluorescence, Midwestern USA, 2018: SIF_PAR_fPAR_US_Midwest_2018.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "High Resolution Land Cover-Specific Solar-Induced Fluorescence, Midwestern USA, 2018: SIF_PAR_fPAR_US_Midwest_2018.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/SIF_PAR_fPAR_US_Midwest_2018/comp/SIF_PAR_fPAR_US_Midwest_2018.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/SIF_PAR_fPAR_US_Midwest_2018_Fig1.png",
-                    "description": "Examples of spatial patterns of reconstructed SIF at 4 km resolution. Only pixels with a fraction of the specific vegetation type larger than 0.1 are shown. For Total SIF, only pixels with a fraction of corn, soybean, grass/pasture, and forest larger than 0.8 are displayed. Source: Wang et al., 2020.",
                     "@type": "dcat:Distribution",
+                    "description": "Examples of spatial patterns of reconstructed SIF at 4 km resolution. Only pixels with a fraction of the specific vegetation type larger than 0.1 are shown. For Total SIF, only pixels with a fraction of corn, soybean, grass/pasture, and forest larger than 0.8 are displayed. Source: Wang et al., 2020.",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/SIF_PAR_fPAR_US_Midwest_2018_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1813/catalog.html",
-                    "description": "The THREDDS location for this Collection.",
                     "@type": "dcat:Distribution",
+                    "description": "The THREDDS location for this Collection.",
+                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1813/catalog.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Examples of spatial patterns of reconstructed SIF at 4 km resolution. Only pixels with a fraction of the specific vegetation type larger than 0.1 are shown. For Total SIF, only pixels with a fraction of corn, soybean, grass/pasture, and forest larger than 0.8 are displayed. Source: Wang et al., 2020.",
+            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/SIF_PAR_fPAR_US_Midwest_2018_Fig1.png",
+            "identifier": "C2345900038-ORNL_CLOUD",
+            "issued": "2021-03-15",
+            "keyword": [
+                "biosphere",
+                "vegetation",
+                "ngda",
+                "national geospatial data asset",
+                "land use/land cover",
+                "land surface",
+                "ecological dynamics",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1813",
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
             "spatial": "-110.02 34.98 -77.98 49.94",
+            "temporal": "2018-05-02T00:00:00Z/2018-09-23T23:59:59Z",
             "theme": [
                 "CMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "High Resolution Land Cover-Specific Solar-Induced Fluorescence, Midwestern USA, 2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/ATCS/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/ATCS/DATA001.",
-            "issued": "2007-11-27",
-            "temporal": "2007-11-27T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "oceans",
-                "ocean temperature",
-                "earth science",
-                "ocean chemistry",
-                "ocean optics",
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
-            "identifier": "C2172083412-OB_DAAC",
             "description": "ATCS is a dataset designed to train deep learning models to volumetrically segment clouds from multi-angle satellite imagery. The dataset consists of spatiotemporally aligned patches of multi-angle polarimetry from the POLDER sensor aboard the PARASOL mission and vertical cloud profiles from the 2B-CLDCLASS product using the cloud profiling radar (CPR) aboard CloudSat.",
-            "title": "The A-Train Cloud Segmentation Dataset",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FATCS%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FATCS%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/ATCS/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/ATCS/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2172083412-OB_DAAC",
+            "issued": "2007-11-27",
+            "keyword": [
+                "oceans",
+                "ocean temperature",
+                "earth science",
+                "ocean chemistry",
+                "ocean optics",
+                "salinity/density"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/ATCS/DATA001",
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
+            "temporal": "2007-11-27T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "The A-Train Cloud Segmentation Dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-RPCMAG-3-AST1-CALIBRATED-V3.0",
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
-                "2867 steins"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains CALIBRATED DATA of the STEINS flyby Phase from September 1 until September 10, 2008. The closest approach (CA) took place on September 5, 2008 at 18:38",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-rpcmag-3-ast1-calibrated-v3.0_4c3u-qnyr",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international rosetta mission",
+                "2867 steins"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-RPCMAG-3-AST1-CALIBRATED-V3.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-rpcmag-3-ast1-calibrated-v3.0_4c3u-qnyr",
-            "description": "This dataset contains CALIBRATED DATA of the STEINS flyby Phase from September 1 until September 10, 2008. The closest approach (CA) took place on September 5, 2008 at 18:38",
-            "title": "ROSETTA-ORBITER STEINS RPCMAG 3 AST1 CALIBRATED V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER STEINS RPCMAG 3 AST1 CALIBRATED V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2OCSN_L2.007",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2017-04-06. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AURA/TES/TL2OCSN_L2.007. https://asdc.larc.nasa.gov/project/TES.",
-            "issued": "2015-04-08",
-            "temporal": "2004-08-22T00:00:00Z/2018-01-22T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric chemistry",
-                "air quality"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Scott Gluck",
                 "hasEmail": "mailto:scott.gluck@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1331888267-LARC",
             "description": "TL2OCSN_7 is the Tropospheric Emission Spectrometer (TES)/Aura Level 2 Atmospheric Temperatures Limb Version 7 data product. TES was an instrument aboard NASA's Aura satellite and was launched from California on July 15, 2004. Data collection for TES is complete. It contains atmospheric vertical profile estimates and associated errors (diagonals and covariance matrices), along with retrieved surface temperature, cloud effective optical depth, column estimates, quality flags, averaging kernels and a priori constraint vectors. \r\rTES Level 2 data contain retrieved species (or temperature) profiles at the observation targets and the estimated errors. The geolocation, quality, and other data (e.g., surface characteristics for nadir observations) were also provided. L2 modeled spectra were evaluated using radiative transfer modeling algorithms. The process, referred to as retrieval, compared observed spectra to the modeled spectra and iteratively updated the atmospheric parameters. L2 standard product files included information for one molecular species (or temperature) for an entire global survey or special observation run. A global survey consisted of a maximum of 16 consecutive orbits. \r\rNadir observations, which point directly to the surface of the Earth are different from limb observations, which are pointed at various off-nadir angles into the atmosphere. Nadir and limb observations were added to separate L2 files, and a single ancillary file was composed of data that are common to both nadir and limb files. A Nadir sequence within the TES Global Survey was a fixed number of observations within an orbit for a Global Survey. Prior to April 24, 2005, it consisted of two low resolution scans over the same ground locations. After April 24, 2005, Global Survey data consisted of three low resolution scans. The Nadir standard product consists of four files, where each file is composed of the Global Survey Nadir observations from one of four focal planes for a single orbit, i.e. 72 orbit sequences. The Global Survey Nadir observations only used a single set of filter mix. \r\rA Global Survey consisted of observations along 16 consecutive orbits at the start of a two day cycle, over which 3,200 retrievals were performed. Each observation was the input for retrievals of species Volume Mixing Ratios (VMRs), temperature profiles, surface temperature, and other data parameters with associated pressure levels, precision, total error, vertical resolution, total column density, and other diagnostic quantities. Each TES Level 2 standard product reported information in a swath format conforming to the HDF-EOS Aura File Format Guidelines. Each Swath object was bounded by the number of observations in a global survey and a predefined set of pressure levels representing slices through the atmosphere. Each standard product could have had a variable number of observations depending upon the Global Survey configuration and whether averaging was employed. Also, missing or bad retrievals were not reported. Further, observations were occasionally scheduled on non-global survey days. In general they were measurements made for validation purposes or with highly focused science objectives. Those non-global survey measurements were referred to as \u201cspecial observations\u201d\r\rThe organization of data within the Swath object was based on a superset of the Upper Atmosphere Research Satellite (UARS) pressure levels used to report concentrations of trace atmospheric gases. The reporting grid was the same pressure grid used for modeling. There were 67 reporting levels from 1211.53 hPa, which allowed for very high surface pressure conditions, to 0.1 hPa, about 65 km. In addition, the products reported values directly at the surface when possible or at the observed cloud top level. Thus in the Standard Product files, each observation could potentially contain estimates for the concentration of a particular molecule at 67 different pressure levels within the atmosphere. Ho",
-            "title": "TES/Aura L2 Carbonyl Sulfide Nadir V007",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2OCSN_L2.007",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2OCSN_L2.007",
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
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/cgi-bin/DUE/tes_L2GlbSrvy.cgi",
-                    "description": "Report of TES Level 2 Global Survey Products Available from the ASDC",
                     "@type": "dcat:Distribution",
+                    "description": "Report of TES Level 2 Global Survey Products Available from the ASDC",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/cgi-bin/DUE/tes_L2GlbSrvy.cgi",
+                    "mediaType": "text/html",
                     "title": "View this dataset's production history"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/README_L2_ReadSoftware.txt",
-                    "description": "Basic IDL Tools for extraction information from TES L2 HDF Product files",
                     "@type": "dcat:Distribution",
+                    "description": "Basic IDL Tools for extraction information from TES L2 HDF Product files",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/README_L2_ReadSoftware.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/TES_Lite_Products_Users_Guide.pdf",
-                    "description": "AVDC TES Lite products user\u2019s guide",
                     "@type": "dcat:Distribution",
+                    "description": "AVDC TES Lite products user\u2019s guide",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/TES_Lite_Products_Users_Guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1331888267-LARC",
-                    "description": "Earthdata Search for TL2OCSN_7 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TL2OCSN_7 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1331888267-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2OCSN_L2.007",
-                    "description": "DOI data set landing page for TL2OCSN_7",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TL2OCSN_7",
+                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2OCSN_L2.007",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2OCSN.007/contents.html",
-                    "description": "OPeNDAP data access for TL2OCSN_7",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for TL2OCSN_7",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2OCSN.007/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2OCSN.007/",
-                    "description": "ASDC Direct Data Download for TL2OCSN_7",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for TL2OCSN_7",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2OCSN.007/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
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
                 }
             ],
+            "identifier": "C1331888267-LARC",
+            "issued": "2015-04-08",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry",
+                "air quality"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2OCSN_L2.007",
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
+            "title": "TES/Aura L2 Carbonyl Sulfide Nadir V007"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0331-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-10-02T16:08:45.000 to 2014-10-02T22:55:08.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0331-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0331-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0331-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-10-02T16:08:45.000 to 2014-10-02T22:55:08.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0331 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0331 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/990",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Menton, M.C., A.M.S. Figueira, C.A.D. de Sousa, S.D. Miller, H.R. da Rocha, and M.L. Goulden. 2011. LBA-ECO CD-04 Biomass Survey, km 83 Tower Site, Tapajos National Forest, Brazil. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/990",
-            "issued": "2023-10-03",
-            "temporal": "2000-03-01T00:00:00Z/2009-03-28T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-05",
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
-            "identifier": "C2777825408-ORNL_CLOUD",
             "description": "This data set contains the results of a biometric tree survey of a 19.25 ha area adjacent to the eddy flux tower at the km 83 logged forest tower site in Tapajos National Forest, Para, Brazil. The survey was done in March 2000. All measurements reported here were taken before the logging began. Diameters of all trees > 35 cm DBH within the 19.25 ha survey area were recorded and trees with DBH between 10 and 35 cm DBH were recorded along three transects with a total area of 2.3 ha (Miller et al., 2004). These data were used to calculate net ecosystem productivity (NEP) and the role of this forest as a carbon source or sink. Biometric data are reported in one comma-delimited ASCII file.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO CD-04 Biomass Survey, km 83 Tower Site, Tapajos National Forest, Brazil",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F990",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F990",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/carbon_dynamics/CD04_Biomass/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/carbon_dynamics/CD04_Biomass/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/CD04_Biomass_km83.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/CD04_Biomass_km83.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/990",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/990",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD04_Biomass/comp/CD04_Biomass_km83.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD04_Biomass/comp/CD04_Biomass_km83.pdf",
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
+            "identifier": "C2777825408-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "vegetation",
+                "biosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/990",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-10-05",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-3.02 -54.97",
+            "temporal": "2000-03-01T00:00:00Z/2009-03-28T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO CD-04 Biomass Survey, km 83 Tower Site, Tapajos National Forest, Brazil"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-RADAR-V15.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-radar-v15.0_4c9k-pswz",
+            "issued": "2021-05-21",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-RADAR-V15.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-radar-v15.0_4c9k-pswz",
-            "description": "This data set is intended to include all published groundbased asteroid radar detections. The file is based on the collection of asteroid radar detections established by Steven J. Ostro and currently maintained by Lance A.M. Benner. The file includes disc-integrated radar properties extracted from the published papers.",
-            "title": "ASTEROID RADAR V15.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ASTEROID RADAR V15.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-MAG-3-RDR-EROS%2FFLY%2FBY-V1.0",
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
+            "description": "NEAR MAG RDR volume sets contain a single data set, from one instrument and one mission phase (defined in the phase table in /AAREADME.TXT).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-mag-3-rdr-eros-fly-by-v1.0_4ca8-9uxf",
+            "issued": "2021-05-21",
+            "keyword": [
+                "eros",
+                "near earth asteroid rendezvous"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-MAG-3-RDR-EROS%2FFLY%2FBY-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-mag-3-rdr-eros-fly-by-v1.0_4ca8-9uxf",
-            "description": "NEAR MAG RDR volume sets contain a single data set, from one instrument and one mission phase (defined in the phase table in /AAREADME.TXT).",
-            "title": "NEAR MAG DATA FOR EROS/FLY/BY",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEAR MAG DATA FOR EROS/FLY/BY"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D12.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler\r\n. 2019-11-07. VNP43D12. Version 001. VIIRS/NPP BRDF/Albedo Parameter 3 Band M4 Daily L3 Global 30 ArcSec CMG V001\r\n. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VNP43D12.001. https://doi.org/10.5067/VIIRS/VNP43D12.001. Digital Science Data. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
-            "issued": "2019-11-07",
-            "temporal": "2012-01-19T00:00:00Z/2024-05-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-11-07",
-            "keyword": [
-                "land surface",
-                "surface radiative properties",
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
-            "identifier": "C1607316266-LPDAAC_ECS",
-            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Model Parameter 3 Band M4 product (VNP43D12) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. Each of the three model parameters (isotropic, volumetric, and geometric) for each of the nine VIIRS moderate resolution bands along with the visible, near-infrared (NIR), and shortwave bands included in the VNP43MA1 (https://doi.org/10.5067/VIIRS/VNP43MA1.001) product is stored in a separate file as VNP43D01 through VNP43D36. In addition to the bands included in VNP43MA1, this product suite includes model parameters for the VIIRS Day/Night Band (DNB) as VNP43D37 through VNP43D39. Details regarding methodology are available on the VNP43MA1 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D12 is the BRDF geometric parameter for VIIRS band M4 (0.555 \u03bcm). The geometric parameter, in conjunction with the isotropic and volumetric parameters, is used to derive the BRDF/Albedo values for VIIRS band M4.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "VNP43D12",
             "creator": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler",
-            "title": "VIIRS/NPP BRDF/Albedo Parameter 3 Band M4 Daily L3 Global 30 ArcSec CMG V001",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Model Parameter 3 Band M4 product (VNP43D12) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. Each of the three model parameters (isotropic, volumetric, and geometric) for each of the nine VIIRS moderate resolution bands along with the visible, near-infrared (NIR), and shortwave bands included in the VNP43MA1 (https://doi.org/10.5067/VIIRS/VNP43MA1.001) product is stored in a separate file as VNP43D01 through VNP43D36. In addition to the bands included in VNP43MA1, this product suite includes model parameters for the VIIRS Day/Night Band (DNB) as VNP43D37 through VNP43D39. Details regarding methodology are available on the VNP43MA1 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D12 is the BRDF geometric parameter for VIIRS band M4 (0.555 \u03bcm). The geometric parameter, in conjunction with the isotropic and volumetric parameters, is used to derive the BRDF/Albedo values for VIIRS band M4.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D12.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D12.001",
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
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D12.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D12.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/xhdf5",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D12.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D12.001/",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607316266-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607316266-LPDAAC_ECS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D12.001/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D12.001/contents.html",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D12",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D12",
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
+            "identifier": "C1607316266-LPDAAC_ECS",
+            "issued": "2019-11-07",
+            "keyword": [
+                "land surface",
+                "surface radiative properties",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D12.001",
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
+            "series-name": "VNP43D12",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-19T00:00:00Z/2024-05-20T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP BRDF/Albedo Parameter 3 Band M4 Daily L3 Global 30 ArcSec CMG V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/B04/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/B04/DATA001.",
-            "issued": "2005-03-30",
-            "temporal": "2005-03-30T00:00:00Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "oceans",
-                "ocean optics",
-                "salinity/density",
-                "ocean chemistry",
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
-            "identifier": "C1633360128-OB_DAAC",
             "description": "Measurements made near the mid-Atlantic coastal region of the continental shelf in 2005 and 2006.",
-            "title": "Mid-Atlantic coastal region measurements",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FB04%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FB04%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/B04/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/B04/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360128-OB_DAAC",
+            "issued": "2005-03-30",
+            "keyword": [
+                "oceans",
+                "ocean optics",
+                "salinity/density",
+                "ocean chemistry",
+                "earth science",
+                "ocean temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/B04/DATA001",
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
+            "temporal": "2005-03-30T00:00:00Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Mid-Atlantic coastal region measurements"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0387-3-SUBMMLC-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Submillimeter lightcurves of large asteroids Ceres, Davida, Io, Juno, Pallas, Vesta, and Victoria, observed at the Heinrich-Hertz Submillimeter Telescope from January 2003 through May 2004.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0387-3-submmlc-v1.0_4cfy-xmw9",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "2 pallas",
                 "3 juno",
@@ -132544,110 +132546,122 @@
                 "support archives",
                 "85 io"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0387-3-SUBMMLC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0387-3-submmlc-v1.0_4cfy-xmw9",
-            "description": "Submillimeter lightcurves of large asteroids Ceres, Davida, Io, Juno, Pallas, Vesta, and Victoria, observed at the Heinrich-Hertz Submillimeter Telescope from January 2003 through May 2004.",
-            "title": "SUBMILLIMETER LIGHTCURVES OF ASTEROIDS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "SUBMILLIMETER LIGHTCURVES OF ASTEROIDS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1249-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-10T18:17:45.000 to 2015-12-10T22:57:07.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1249-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1249-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1249-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-10T18:17:45.000 to 2015-12-10T22:57:07.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1249 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1249 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VL1%2FVL2-M-FTS-4-SOL-AVG-FTPD-TEMP-V1.0",
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
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vl1-vl2-m-fts-4-sol-avg-ftpd-temp-v1.0_4ckb-xnek",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "viking"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VL1%2FVL2-M-FTS-4-SOL-AVG-FTPD-TEMP-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vl1-vl2-m-fts-4-sol-avg-ftpd-temp-v1.0_4ckb-xnek",
-            "description": "not applicable",
-            "title": "VL1/VL2 MARS METEOROLOGY RESAMPLED SOL AVG FOOTPAD TEMP V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VL1/VL2 MARS METEOROLOGY RESAMPLED SOL AVG FOOTPAD TEMP V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.nasa.gov/mission_pages/station/expeditions/expedition15/index.html",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brian Dunbar",
+                "hasEmail": "mailto:brian.dunbar@nasa.gov"
+            },
+            "description": "Press kit for ISS mission Expedition 15 from 04/2007-10/2007. Press kits contain information about each mission overview, crew, mission timeline, benefits, and media contact information.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Press Kit PDF",
+                    "downloadURL": "http://www.nasa.gov/pdf/172356main_expedition15_presskit.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "ISS 15 Press Kit"
+                }
+            ],
+            "identifier": "OCIO-Fitara-27",
             "issued": "2007-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "2007",
                 "schedule",
@@ -132659,369 +132673,330 @@
                 "15",
                 "crew"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brian Dunbar",
-                "hasEmail": "mailto:brian.dunbar@nasa.gov"
-            },
+            "landingPage": "http://www.nasa.gov/mission_pages/station/expeditions/expedition15/index.html",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:037"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "JSC"
             },
-            "identifier": "OCIO-Fitara-27",
-            "description": "Press kit for ISS mission Expedition 15 from 04/2007-10/2007. Press kits contain information about each mission overview, crew, mission timeline, benefits, and media contact information.",
-            "title": "ISS Expedition 15 Press Kit",
-            "programCode": [
-                "026:037"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.nasa.gov/pdf/172356main_expedition15_presskit.pdf",
-                    "description": "Press Kit PDF",
-                    "@type": "dcat:Distribution",
-                    "title": "ISS 15 Press Kit"
-                }
-            ],
-            "accrualPeriodicity": "irregular"
+            "title": "ISS Expedition 15 Press Kit"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1988",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Thompson, D.R., D.J. Jensen, J.W. Chapman, E. Greenberg, and M. Simard. 2022. Delta-X: AVIRIS-NG L2 Surface Reflectance, MRD Louisiana, 2021. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1988",
-            "issued": "2022-08-29",
-            "temporal": "2021-03-27T00:00:00Z/2021-09-25T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "geomorphic landforms/processes",
-                "earth science",
-                "surface water",
-                "visible wavelengths",
-                "land surface",
-                "spectral/engineering",
-                "surface radiative properties",
-                "infrared wavelengths",
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
-            "identifier": "C2430019879-ORNL_CLOUD",
             "description": "This dataset provides Level 2 (L2) atmospherically corrected surface reflectance data acquired from NASA's Airborne Visible-Infrared Imaging Spectrometer-Next Generation (AVIRIS-NG) over regions of interest in the Atchafalaya and Terrebonne basins on the southern coast of Louisiana, United States. Data were collected as part of the Delta-X Spring and Fall 2021 deployments that occurred from 2021-03-27 to 2021-04-06 and from 2021-08-18 to 2021-08-25. Additionally, L2 data from flights flown specifically to capture the Significant Event of Hurricane Ida are provided.  This includes 56 files from flights conducted following Hurricane Ida from 2021-09-23 to 2021-09-25. Hurricane Ida made landfall over this region on 2021-08-29. AVIRIS-NG is a pushbroom spectral mapping system with a high signal-to-noise ratio (SNR) designed for high performance imaging spectroscopy. AVIRIS-NG measures the wavelength range from 380 nm to 2510 nm with 5-nm sampling resolution. For this dataset, spatial resolution varies from 3.8-5.4 meters. For this campaign, the AVIRIS-NG instrument was deployed on the Dynamic Aviation King Air B200 platform. This dataset represents one part of a multisensor airborne sampling campaign conducted by different aircraft teams for the Delta-X Campaign. Data are provided in ENVI file format.",
-            "graphic-preview-description": "The Delta-X study region on the coast of Louisiana, U.S.  Polygons show AVIRIS-NG Flight Lines.",
-            "title": "Delta-X: AVIRIS-NG L2 Surface Reflectance, MRD Louisiana, 2021",
-            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L2_AVIRIS_Reflectance_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1988",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1988",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/deltax/DeltaX_L2_AVIRIS_Reflectance/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/deltax/DeltaX_L2_AVIRIS_Reflectance/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L2_AVIRIS_Reflectance.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L2_AVIRIS_Reflectance.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1988",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1988",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/DeltaX_L2_AVIRIS_Reflectance/comp/DeltaX_L2_AVIRIS_Reflectance.pdf",
-                    "description": "Delta-X: AVIRIS-NG L2 Surface Reflectance, MRD Louisiana, 2021: DeltaX_L2_AVIRIS_Reflectance.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Delta-X: AVIRIS-NG L2 Surface Reflectance, MRD Louisiana, 2021: DeltaX_L2_AVIRIS_Reflectance.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/DeltaX_L2_AVIRIS_Reflectance/comp/DeltaX_L2_AVIRIS_Reflectance.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/DeltaX_L2_AVIRIS_Reflectance/comp/Hurricane_Ida_file_list.txt",
-                    "description": "Delta-X: AVIRIS-NG L2 Surface Reflectance, MRD Louisiana, 2021: Hurricane_Ida_file_list.txt",
                     "@type": "dcat:Distribution",
+                    "description": "Delta-X: AVIRIS-NG L2 Surface Reflectance, MRD Louisiana, 2021: Hurricane_Ida_file_list.txt",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/DeltaX_L2_AVIRIS_Reflectance/comp/Hurricane_Ida_file_list.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L2_AVIRIS_Reflectance_Fig1.jpg",
-                    "description": "The Delta-X study region on the coast of Louisiana, U.S.  Polygons show AVIRIS-NG Flight Lines.",
                     "@type": "dcat:Distribution",
+                    "description": "The Delta-X study region on the coast of Louisiana, U.S.  Polygons show AVIRIS-NG Flight Lines.",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L2_AVIRIS_Reflectance_Fig1.jpg",
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
+            "graphic-preview-description": "The Delta-X study region on the coast of Louisiana, U.S.  Polygons show AVIRIS-NG Flight Lines.",
+            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L2_AVIRIS_Reflectance_Fig1.jpg",
+            "identifier": "C2430019879-ORNL_CLOUD",
+            "issued": "2022-08-29",
+            "keyword": [
+                "geomorphic landforms/processes",
+                "earth science",
+                "surface water",
+                "visible wavelengths",
+                "land surface",
+                "spectral/engineering",
+                "surface radiative properties",
+                "infrared wavelengths",
+                "terrestrial hydrosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1988",
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
             "spatial": "-91.64 29.02 -89.59 29.85",
+            "temporal": "2021-03-27T00:00:00Z/2021-09-25T23:59:59Z",
             "theme": [
                 "Delta-X",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Delta-X: AVIRIS-NG L2 Surface Reflectance, MRD Louisiana, 2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-TES-3-SAMPLER-V1.0",
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
+            "description": "MGS TES calibrated radiance single-scan data for MGS assessment orbits",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-tes-3-sampler-v1.0_4cpk-cer9",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars global surveyor",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-TES-3-SAMPLER-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-tes-3-sampler-v1.0_4cpk-cer9",
-            "description": "MGS TES calibrated radiance single-scan data for MGS assessment orbits",
-            "title": "MGS SAMPLER THERMAL EMISSION SPECTROMETER CALIBRATED RADIANC",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MGS SAMPLER THERMAL EMISSION SPECTROMETER CALIBRATED RADIANC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/MEASURES/GPCP/DATA304",
             "citation": "Huffman, G.J., A. Behrangi, D.T. Bolvin, E.J. Nelkin. Huffman, G.J., A. Behrangi, D.T. Bolvin, E.J. Nelkin. 2022-02-02. GPCPMON. Version 3.2. GPCP Version 3.2 Satellite-Gauge (SG) Combined Precipitation Data Set. Greenbelt, Maryland, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/MEASURES/GPCP/DATA304. https://disc.gsfc.nasa.gov/datacollection/GPCPMON_3.2.html. Digital Science Data.",
-            "issued": "2021-02-02",
-            "temporal": "1983-01-01T00:00:00Z/2022-09-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-02",
-            "keyword": [
-                "earth science",
-                "precipitation",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "GEORGE HUFFMAN",
                 "hasEmail": "mailto:George.J.Huffman@nasa.gov"
             },
+            "creator": "Huffman, G.J., A. Behrangi, D.T. Bolvin, E.J. Nelkin",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2211412414-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Version 3.2 is the current version. Older versions have been superseded by Version 3.2.\n\nThe Global Precipitation Climatology Project (GPCP) is the precipitation component of an internationally coordinated set of (mainly) satellite-based global products dealing with the Earth's water and energy cycles, under the auspices of the Global Water and Energy Experiment (GEWEX) Data and Assessment Panel (GDAP) of the World Climate Research Program.  As the follow on to the GPCP Version 2.X products, GPCP Version 3 (GPCP V3.2) seeks to continue the long, homogeneous precipitation record using modern merging techniques and input data sets.  The GPCPV3 suite currently consists the 0.5-degree monthly and daily products.  A follow-on 0.1-degree 3-hourly is expected.  All GPCPV3 products will be internally consistent. The monthly product spans 1983 - 2020. Inputs consist of the GPROF SSMI/SSMIS orbit files that are used to calibrate the PERSIANN-CDR IR-based precipitation in the span 60\u00b0N-S, which are in turn calibrated to the monthly 2.5-degree METH product.  The METH-GPROF-adjusted PERSIANN-CDR IR estimates are then climatologically adjusted to the blended TCC/MCTG.  Outside of 58\u00b0N-S, TOVS/AIRS estimates, adjusted climatologically to the MCTG, are used.  The PERSIANN-CDR / TOVS/AIRS estimates are then merged in the region 35\u00b0N-S-58\u00b0N-S, which are then merged with GPCC gauge analyses over land to obtain the final product. In addition to the final precipitation field, ancillary precipitation and error estimates are provided.",
-            "editor": "Huffman, G.J., A. Behrangi, D.T. Bolvin, E.J. Nelkin",
-            "release-place": "Greenbelt, Maryland, USA",
-            "series-name": "GPCPMON",
-            "creator": "Huffman, G.J., A. Behrangi, D.T. Bolvin, E.J. Nelkin",
-            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
-            "title": "GPCP Precipitation Level 3 Monthly 0.5-Degree V3.2 (GPCPMON) at GES DISC",
-            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=GPCP%20monthly%20V3.2",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FGPCP%2FDATA304",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FGPCP%2FDATA304",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GPCPMON_V32.png",
-                    "description": "A sample map for sat_gauge_precip",
                     "@type": "dcat:Distribution",
+                    "description": "A sample map for sat_gauge_precip",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GPCPMON_V32.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPCPMON_3.2.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPCPMON_3.2.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/GPCP/GPCPMON.3.2/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/GPCP/GPCPMON.3.2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPCPMON_3.2",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPCPMON_3.2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=GPCP%20monthly%20V3.2",
-                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
                     "@type": "dcat:Distribution",
+                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=GPCP%20monthly%20V3.2",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through GIOVANNI"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/GPCP/GPCPMON.3.2/",
-                    "description": "Access to the data via OPeNDAP protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access to the data via OPeNDAP protocol",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/GPCP/GPCPMON.3.2/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/GPCP/GPCPMON.3.2/doc/README.GPCPV3.2_Monthly.pdf",
-                    "description": "README document",
                     "@type": "dcat:Distribution",
+                    "description": "README document",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/GPCP/GPCPMON.3.2/doc/README.GPCPV3.2_Monthly.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/GPCP_ATBD_V3.2_Monthly.pdf",
-                    "description": "GPCP_ATBD_V3.2_Monthly.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "GPCP_ATBD_V3.2_Monthly.pdf",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/GPCP_ATBD_V3.2_Monthly.pdf",
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
+            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=GPCP%20monthly%20V3.2",
+            "identifier": "C2211412414-GES_DISC",
+            "issued": "2021-02-02",
+            "keyword": [
+                "earth science",
+                "precipitation",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/GPCP/DATA304",
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
+            "series-name": "GPCPMON",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1983-01-01T00:00:00Z/2022-09-30T23:59:59.999Z",
             "theme": [
                 "MEaSUREs",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPCP Precipitation Level 3 Monthly 0.5-Degree V3.2 (GPCPMON) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0257-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-30T13:02:05.000 to 2014-08-30T15:17:37.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0257-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0257-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0257-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-30T13:02:05.000 to 2014-08-30T15:17:37.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0257 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0257 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "issue-identification": "MAM05S0",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1236350973-GES_DISC.html",
             "citation": "MODIS Science Team. 2006-10-01. MAM05S0. Version 002. MODIS/Aqua Total Precip Water Vapor 1km and 5km 5-Min L2 Swath Subset along MLS. Greenbelt, MD, USA. MAM05S0. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/MAM05S0_002.html. Digital Science Data.",
-            "issued": "2004-08-08",
-            "temporal": "2004-08-08T00:00:00Z/2008-01-11T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2008-01-11",
-            "keyword": [
-                "atmosphere",
-                "national geospatial data asset",
-                "earth science",
-                "ngda",
-                "atmospheric water vapor"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANDREY SAVTCHENKO",
                 "hasEmail": "mailto:Andrey.Savtchenko@nasa.gov"
             },
+            "creator": "MODIS Science Team",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1236350973-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "This is the MODIS/Aqua subset along MLS field of view track. The goal of the subset is to select and return MODIS data that are within +-100 km across the MLS track. I.e. the resultant MODIS subset swath is sought to be about 200 km cross-track. However, the original MYD05_L2 has data of 5- and 1-km pixels. Thus, MAM05S0 cross-track width is 41- and 201-pixels, depending on the parameter.  Along-track, all MODIS pixels from the original product are preserved.\n      \nIn the standard product, the MODIS level-2 atmospheric precipitable water product consists of total atmospheric column water vapor amounts (and ancillary parameters) over clear land areas of the globe, over extended clear oceanic areas with the Sun glint, and above clouds over both land and ocean. These estimates are based on a near-infrared algorithm using only daytime measurements with solar zenith angle less than 72 degrees. The retrieval algorithm relies on observations of water vapor attenuation of near-infrared solar radiation reflected by surfaces and clouds. The product is produced only over areas that have reflective surfaces in the near-infrared. The infrared-derived precipitable water vapor generated for both daytime & nighttime conditions as one component of another MODIS product (MYD07) is also provided as a part of this product. \n      \n      \n(The shortname for this product is MAM05S0).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "MAM05S0",
-            "creator": "MODIS Science Team",
-            "title": "MODIS/Aqua Total Precip Water Vapor 1km and 5km 5-Min L2 Swath Subset along MLS V002 (MAM05S0) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/MAM05S0_002.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -133030,76 +133005,103 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/MAM05S0_002.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/MAM05S0_002.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://atrain.gesdisc.eosdis.nasa.gov/data/MAM/MAM05S0.002/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://atrain.gesdisc.eosdis.nasa.gov/data/MAM/MAM05S0.002/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.nascom.nasa.gov",
-                    "description": "View standard full-sized MODIS data availability.",
                     "@type": "dcat:Distribution",
+                    "description": "View standard full-sized MODIS data availability.",
+                    "downloadURL": "https://ladsweb.nascom.nasa.gov",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis.gsfc.nasa.gov/",
-                    "description": "MODIS Science Team",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS Science Team",
+                    "downloadURL": "https://modis.gsfc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://mcst.gsfc.nasa.gov/",
-                    "description": "MODIS Characterization Support Team (MCST)",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS Characterization Support Team (MCST)",
+                    "downloadURL": "https://mcst.gsfc.nasa.gov/",
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
-                    "downloadURL": "https://modis-atmos.gsfc.nasa.gov/data-issues/water-vapor",
-                    "description": "Quality Assurance for the original product.",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Assurance for the original product.",
+                    "downloadURL": "https://modis-atmos.gsfc.nasa.gov/data-issues/water-vapor",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/MAM05S0_002.png",
+            "identifier": "C1236350973-GES_DISC",
+            "issue-identification": "MAM05S0",
+            "issued": "2004-08-08",
+            "keyword": [
+                "atmosphere",
+                "national geospatial data asset",
+                "earth science",
+                "ngda",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1236350973-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2008-01-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "MAM05S0",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2004-08-08T00:00:00Z/2008-01-11T23:59:59.999Z",
             "theme": [
                 "ATDD",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Aqua Total Precip Water Vapor 1km and 5km 5-Min L2 Swath Subset along MLS V002 (MAM05S0) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Agbo.ast-m-type.fornasier.spectra&version=1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains reduced composite visual and near-infrared spectra of thirty M-type asteroids, observed  over the years 2004-2008 and presented in Fornasier et al. (2010).     The spectra were taken with the Dolores and NICS instruments at the    Telescopio Nationale Galileo (TNG) in La Palma, with the EMMI and SOFI instruments at the ESO New Technology Telescope (NTT) in Chile, and    with the SPeX instrument at the Infrared Telescope Facility (IRTF) in  Hawaii.  The individual spectra from the various instruments used to   produce the composite spectra are also included.",
+            "identifier": "urn:nasa:pds:gbo.ast-m-type.fornasier.spectra",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "(872) holda",
                 "multiple asteroids",
@@ -133134,463 +133136,473 @@
                 "(22) kalliope",
                 "none"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Agbo.ast-m-type.fornasier.spectra&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:gbo.ast-m-type.fornasier.spectra",
-            "description": "This data set contains reduced composite visual and near-infrared spectra of thirty M-type asteroids, observed  over the years 2004-2008 and presented in Fornasier et al. (2010).     The spectra were taken with the Dolores and NICS instruments at the    Telescopio Nationale Galileo (TNG) in La Palma, with the EMMI and SOFI instruments at the ESO New Technology Telescope (NTT) in Chile, and    with the SPeX instrument at the Infrared Telescope Facility (IRTF) in  Hawaii.  The individual spectra from the various instruments used to   produce the composite spectra are also included.",
-            "title": "FORNASIER SPECTRA OF M ASTEROIDS",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "FORNASIER SPECTRA OF M ASTEROIDS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0587-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-02-18T03:36:25.000 to 2015-02-18T10:15:30.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0587-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0587-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0587-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-02-18T03:36:25.000 to 2015-02-18T10:15:30.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0587 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0587 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/W569D47GCOUX",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "LVIS Classic L2 Geolocated Surface Elevation and Canopy Height Product V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/W569D47GCOUX.",
-            "issued": "2019-05-21",
-            "temporal": "2019-05-21T00:00:00Z/2023-11-06T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-05-31",
-            "keyword": [
-                "earth science",
-                "glaciers/ice sheets",
-                "topography",
-                "vegetation",
-                "biosphere",
-                "cryosphere",
-                "sea ice",
-                "land surface"
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
-            "identifier": "C1703031106-NSIDC_ECS",
             "description": "This data set contains Level-2 geolocated surface elevation and canopy height measurements collected by the NASA Land, Vegetation, and Ice Sensor (LVIS) Facility, an imaging lidar and camera sensor suite.",
-            "title": "LVIS Classic L2 Geolocated Surface Elevation and Canopy Height Product V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FW569D47GCOUX",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FW569D47GCOUX",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/LVISC2.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/LVISC2.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=LVISC2+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=LVISC2+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/LVISC2/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/LVISC2/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/W569D47GCOUX",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/W569D47GCOUX",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/W569D47GCOUX",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/W569D47GCOUX",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1703031106-NSIDC_ECS",
+            "issued": "2019-05-21",
+            "keyword": [
+                "earth science",
+                "glaciers/ice sheets",
+                "topography",
+                "vegetation",
+                "biosphere",
+                "cryosphere",
+                "sea ice",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/W569D47GCOUX",
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
+            "temporal": "2019-05-21T00:00:00Z/2023-11-06T00:00:00Z",
             "theme": [
                 "ABoVE",
                 "GEDI",
                 "MULTI_NASA",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LVIS Classic L2 Geolocated Surface Elevation and Canopy Height Product V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Agbo-mcdonald&version=1.0",
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
-                "multiple comets",
-                "none"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This bundle collects data taken at McDonald Observatory.",
+            "identifier": "urn:nasa:pds:gbo-mcdonald",
+            "issued": "2021-05-21",
+            "keyword": [
+                "multiple comets",
+                "none"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Agbo-mcdonald&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:gbo-mcdonald",
-            "description": "This bundle collects data taken at McDonald Observatory.",
-            "title": "Groundbased Observations at McDonald Observatory",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Groundbased Observations at McDonald Observatory"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/450",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hall, F.G. 1999. BOREAS TE-18 Biomass Density Image of the SSA. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/450",
-            "issued": "2023-11-22",
-            "temporal": "1994-09-02T00:00:00Z/1994-09-02T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-11",
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
-            "identifier": "C2929130809-ORNL_CLOUD",
             "description": "This biomass density image covers almost the entire BOREAS SSA.  The pixels for which biomass density is computed include areas that are in conifer land cover classes only.  The biomass density values represent the amount of overstory biomass (i.e., tree biomass only) per unit area.  It is derived from a Landsat-5 TM image collected on 02-Sep-1994.  The technique that was used to create this image is very similar to the technique that was used to create the physical classification of the SSA.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS TE-18 Biomass Density Image of the SSA",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F450",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F450",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TE/biomdens/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TE/biomdens/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TE18_SSA_Biomass_Dens.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TE18_SSA_Biomass_Dens.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/450",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/450",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/biomdens/comp/README",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/biomdens/comp/README",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/biomdens/comp/TE18_SSA_Biomass_Dens.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/biomdens/comp/TE18_SSA_Biomass_Dens.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/biomdens/comp/TE18_SSA_Biomass_Dens.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/biomdens/comp/TE18_SSA_Biomass_Dens.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/biomdens/comp/TE18_SSA_Biomass_Dens.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/biomdens/comp/TE18_SSA_Biomass_Dens.txt",
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
+            "identifier": "C2929130809-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "biosphere",
+                "vegetation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/450",
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
             "spatial": "-106.52 53.31 -104.19 54.44",
+            "temporal": "1994-09-02T00:00:00Z/1994-09-02T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS TE-18 Biomass Density Image of the SSA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/DORIS/DORIS_IDSDPOD_001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GGL/CDDIS. https://doi.org/10.5067/DORIS/DORIS_IDSDPOD_001.",
-            "issued": "1993-01-01",
-            "temporal": "1992-01-01T00:00:00Z/2023-06-19T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-31",
-            "keyword": [
-                "tectonics",
-                "gravity/gravitational field",
-                "earth science",
-                "geodetics",
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
-            "identifier": "C1602788193-CDDIS",
             "description": "Doppler Orbitography and Radiopositioning Integrated by Satellite (DORIS) Station Position Product for Precise Orbit Determination from the NASA Crustal Dynamics Data Information System (CDDIS). DORIS is a dual-frequency Doppler system consisting of a receiver flying aboard a satellite and a globally distributed network of ground beacons. The DORIS receiver on-board the orbiting satellite tracks the dual-frequency radio signals transmitted by the network of ground beacons and generates the DORIS data. A measurement is made of either the Doppler shift or absolute phase as the satellite\u2019s orbit moves over the ground-based beacon. DORIS data records contain a time-tagged range-rate measurement with associated ancillary information. DORIS observations from a global network can be utilized for a variety of products. Analysis Centers (ACs) of the International DORIS Service (IDS) retrieve DORIS data on a regular basis to compute station position solutions for the DORIS beacons supporting the IDS network. The IDS Analysis Center Coordinator combines these solutions to produce an official IDS product. This DPOD (DORIS extension of the ITRF for Precise Orbit Determination) solution is a set of coordinates and velocities of all the DORIS tracking stations for Precise Orbit Determination (POD) applications. The combined solution is generated in conjunction with official determination of the International Terrestrial Reference Frame. DPOD solutions are available in SINEX format.",
-            "title": "Ground-Based Doppler Orbitography and Radiopositioning Integrated by Satellite (DORIS) Station Position Product for Precise Orbit Determination from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FDORIS%2FDORIS_IDSDPOD_001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FDORIS%2FDORIS_IDSDPOD_001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/archive/doris/products/dpod/",
-                    "description": "URL for retrieval of DORIS products through https",
                     "@type": "dcat:Distribution",
+                    "description": "URL for retrieval of DORIS products through https",
+                    "downloadURL": "https://cddis.nasa.gov/archive/doris/products/dpod/",
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
-                    "downloadURL": "http://dx.doi.org/10.5067/DORIS/DORIS_IDSDPOD_001",
-                    "description": "URL for more information about DORIS products",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about DORIS products",
+                    "downloadURL": "http://dx.doi.org/10.5067/DORIS/DORIS_IDSDPOD_001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1602788193-CDDIS",
+            "issued": "1993-01-01",
+            "keyword": [
+                "tectonics",
+                "gravity/gravitational field",
+                "earth science",
+                "geodetics",
+                "solid earth"
+            ],
+            "landingPage": "https://doi.org/10.5067/DORIS/DORIS_IDSDPOD_001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GGL/CDDIS"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1992-01-01T00:00:00Z/2023-06-19T00:00:00Z",
             "theme": [
                 "IDS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Ground-Based Doppler Orbitography and Radiopositioning Integrated by Satellite (DORIS) Station Position Product for Precise Orbit Determination from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AVHRR/N19_AVH13C1.006",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The Long-Term Data Record (LTDR) project. 2023-07-25. NOAA-19 AVHRR Atmospherically Corrected Normalized Difference Vegetation Index Daily L3 Global 0.05 Deg. CMG. Version 6. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/AVHRR/N19_AVH13C1.006.",
-            "issued": "2022-10-23",
-            "temporal": "2009-05-31T00:00:00Z/2018-01-31T23:59:59.900Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-01-01",
-            "keyword": [
-                "land use/land cover",
-                "vegetation",
-                "land surface",
-                "earth science",
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
-            "identifier": "C2736308262-LAADS",
-            "description": "The Long-Term Data Record (LTDR) produces, validates, and distributes a global land surface climate data record (CDR) that uses both mature and well-tested algorithms in concert with the best-available polar-orbiting satellite data from past to the present.   The CDR is critically important to studying global climate change.  The LTDR project is unique in that it serves as a bridge that connects data derived from the NOAA Advanced Very High Resolution Radiometer (AVHRR), the EOS Moderate resolution Imaging Spectroradiometer (MODIS), the Suomi National Polar-orbiting Partnership (SNPP) Visible Infrared Imaging Radiometer Suite (VIIRS), and Joint Polar Satellite System (JPSS) VIIRS missions.  The LTDR draws from the following eight AVHRR missions: \r\nNOAA-7, NOAA-9, NOAA-11, NOAA-14, NOAA-16, NOAA-18, NOAA-19, and MetOp-B.\r\nCurrently, the project generates a daily surface reflectance product as the fundamental climate data record (FCDR) and derives daily Normalized Differential Vegetation Index (NDVI) and Leaf-Area Index/fraction of absorbed Photosynthetically Active Radiation (LAI/fPAR) as two thematic CDRs (TCDR).  LAI/fPAR was developed as an experimental product.\r\n\r\nThe NOAA-19 AVHRR Atmospherically Corrected Normalized Difference Vegetation Index (NDVI) Daily L3 Global 0.05 Deg CMG, short-name N19_AVH13C1 is generated from GIMMS Advanced Processing System (GAPS) BRDF-corrected Surface Reflectance product (N19_AVH01C1). The N19_AVH13C1 product is available in HDF4 file format.",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "The Long-Term Data Record (LTDR) project",
-            "title": "NOAA19 AVHRR Atmospherically Corrected Normalized Difference Vegetation Index Daily L3 Global 0.05 Deg. CMG",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Long-Term Data Record (LTDR) produces, validates, and distributes a global land surface climate data record (CDR) that uses both mature and well-tested algorithms in concert with the best-available polar-orbiting satellite data from past to the present.   The CDR is critically important to studying global climate change.  The LTDR project is unique in that it serves as a bridge that connects data derived from the NOAA Advanced Very High Resolution Radiometer (AVHRR), the EOS Moderate resolution Imaging Spectroradiometer (MODIS), the Suomi National Polar-orbiting Partnership (SNPP) Visible Infrared Imaging Radiometer Suite (VIIRS), and Joint Polar Satellite System (JPSS) VIIRS missions.  The LTDR draws from the following eight AVHRR missions: \r\nNOAA-7, NOAA-9, NOAA-11, NOAA-14, NOAA-16, NOAA-18, NOAA-19, and MetOp-B.\r\nCurrently, the project generates a daily surface reflectance product as the fundamental climate data record (FCDR) and derives daily Normalized Differential Vegetation Index (NDVI) and Leaf-Area Index/fraction of absorbed Photosynthetically Active Radiation (LAI/fPAR) as two thematic CDRs (TCDR).  LAI/fPAR was developed as an experimental product.\r\n\r\nThe NOAA-19 AVHRR Atmospherically Corrected Normalized Difference Vegetation Index (NDVI) Daily L3 Global 0.05 Deg CMG, short-name N19_AVH13C1 is generated from GIMMS Advanced Processing System (GAPS) BRDF-corrected Surface Reflectance product (N19_AVH01C1). The N19_AVH13C1 product is available in HDF4 file format.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAVHRR%2FN19_AVH13C1.006",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAVHRR%2FN19_AVH13C1.006",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/1/N19_AVH13C1--466",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/1/N19_AVH13C1--466",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/466/N19_AVH13C1/",
-                    "description": "Direct access to C6 N19_AVH13C1 data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to C6 N19_AVH13C1 data set.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/466/N19_AVH13C1/",
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
+            "identifier": "C2736308262-LAADS",
+            "issued": "2022-10-23",
+            "keyword": [
+                "land use/land cover",
+                "vegetation",
+                "land surface",
+                "earth science",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/AVHRR/N19_AVH13C1.006",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-01-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2009-05-31T00:00:00Z/2018-01-31T23:59:59.900Z",
             "theme": [
                 "NOAA - SPACE WEATHER PROGRAM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NOAA19 AVHRR Atmospherically Corrected Normalized Difference Vegetation Index Daily L3 Global 0.05 Deg. CMG"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1214470682-ASF.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, ASF.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "undefined",
+                "hasEmail": "mailto:uso@asf.alaska.edu"
+            },
+            "description": "Sentinel-1A Single-pol ground projected high and full resolution images",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Vertex, the ASF search and download interface",
+                    "downloadURL": "https://vertex.daac.asf.alaska.edu/",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                }
+            ],
+            "identifier": "C1214470682-ASF",
             "issued": "2014-06-15",
-            "temporal": "2014-04-03T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-11-17",
             "keyword": [
                 "cryosphere",
                 "geomorphic landforms/processes",
@@ -133617,124 +133629,114 @@
                 "landscape",
                 "glaciers/ice sheets"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:uso@asf.alaska.edu"
-            },
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1214470682-ASF.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-11-17",
+            "programCode": [
+                "026:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "ASF"
             },
-            "identifier": "C1214470682-ASF",
-            "description": "Sentinel-1A Single-pol ground projected high and full resolution images",
-            "title": "SENTINEL-1A_SINGLE_POL_GRD_HIGH_RES",
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
+            "temporal": "2014-04-03T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SENTINEL-1A_SINGLE_POL_GRD_HIGH_RES"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-VIRTIS-3-PRL-MTP009-V2.0",
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
+            "description": "This release contains the calibrated data of the VIRTIS instrument on board of the spacecraft Rosetta. This volume contains data from the PRELANDING MTP009 phase, which occurred from 2014-10-24 to 2014-11-22 when at the vicinity of comet 67P. This data set V2.0 supersedes V1.0. It includes major updates on the data and documentation.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-virtis-3-prl-mtp009-v2.0_4d7w-q8vw",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-VIRTIS-3-PRL-MTP009-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-virtis-3-prl-mtp009-v2.0_4d7w-q8vw",
-            "description": "This release contains the calibrated data of the VIRTIS instrument on board of the spacecraft Rosetta. This volume contains data from the PRELANDING MTP009 phase, which occurred from 2014-10-24 to 2014-11-22 when at the vicinity of comet 67P. This data set V2.0 supersedes V1.0. It includes major updates on the data and documentation.",
-            "title": "ROSETTA-ORBITER 67P VIRTIS 3 PRELANDING MTP009 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P VIRTIS 3 PRELANDING MTP009 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0386-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-10-25T14:56:55.000 to 2014-10-25T21:33:28.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0386-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0386-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0386-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-10-25T14:56:55.000 to 2014-10-25T21:33:28.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0386 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0386 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-M-OSINAC-4-MARS-MARS-STRLIGHT-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the MARS SWING-BY mission phase, covering the period  from 2006-07-29T00:00:00.000 to 2007-05-28T23:59:59.000. The prime target is planet Mars. This version V1.0 is the first version of this dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-m-osinac-4-mars-mars-strlight-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "phobos",
                 "21 lutetia",
@@ -133746,499 +133748,511 @@
                 "jupiter",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-M-OSINAC-4-MARS-MARS-STRLIGHT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-m-osinac-4-mars-mars-strlight-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the MARS SWING-BY mission phase, covering the period  from 2006-07-29T00:00:00.000 to 2007-05-28T23:59:59.000. The prime target is planet Mars. This version V1.0 is the first version of this dataset.",
-            "title": "ROSETTA-ORBITER MARS OSINAC 4 MARS RDR-STRLIGHT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER MARS OSINAC 4 MARS RDR-STRLIGHT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1093",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Dobson, M.C., and L.E. Pierce. 2012. LBA-ECO LC-03 SAR Images, Land Cover, and Biomass, Four Areas across Brazilian Amazon. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1093",
-            "issued": "2023-10-03",
-            "temporal": "1974-01-01T00:00:00Z/1998-06-18T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-10",
-            "keyword": [
-                "earth science",
-                "land surface",
-                "biosphere",
-                "vegetation",
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
-            "identifier": "C2780128555-ORNL_CLOUD",
             "description": "This data set provides three related land cover products for four study areas across the Brazilian Amazon: Manaus, Amazonas; Tapajos National Forest, Para Western (Santarem); Rio Branco, Acre; and Rondonia, Rondonia. Products include (1) orthorectified JERS-1 and RadarSat images, (2) land cover classifications derived from the SAR data, and (3) biomass estimates in tons per hectare based on the land cover classification. There are 12 image files (.tif) with this data set.Orthorectified JERS-1 and RadarSat images are provided as GeoTIFF images - one file for each study area.For the Manaus and Tapajos sites: The images are orthorectified at 12.5-meter resolution and then re-sampled at 25-meter resolution.For the Rondonia and Rio Branco sites: The images from 1978 are orthorectified at 25-meter resolution and then re-sampled at 90-meter resolution. Each GeoTIFF file contains 3 image channels: - 2 L-band JERS-1 data in Fall and Spring seasons and - 1 C-band RadarSat data.Land cover classifications are based on two JERS-1 images and one RadarSat image and provided as GeoTIFFs - one file for each study area. Four major land cover classes are distinguished: (1) Flat surface; (2) Regrowth area; (3) Short vegetation; and (4) Tall vegetation. The biomass estimates in tons per hectare are based on the land cover classification results and are reported in one GeoTIFF file for each study area.DATA QUALITY STATEMENT: The Data Center has determined that there are questions about the quality of the data reported in this data set. The data set has missing or incomplete data, metadata, or other documentation that diminishes the usability of the products.KNOWN PROBLEMS: The data providers note that due to limited resources, these data have been neither validated nor quality-assured for general use. For that reason, extreme caution is advised when considering the use of these data.Any use of the derived data is not recommended because the results have not been validated. However, the DEM and vectors (related data set), and orthorectified SAR data can be used if the user understands how these were produced and accepts the limitations.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO LC-03 SAR Images, Land Cover, and Biomass, Four Areas across Brazilian Amazon",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1093_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1093",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1093",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/grab_bag/LC03_SAR_LC_Biomass/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/grab_bag/LC03_SAR_LC_Biomass/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC03_SAR_LC_Biomass.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC03_SAR_LC_Biomass.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1093",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1093",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/grab_bag/LC03_SAR_LC_Biomass/comp/LC03_SAR_LC_Biomass.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/grab_bag/LC03_SAR_LC_Biomass/comp/LC03_SAR_LC_Biomass.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1093_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1093_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1093",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1093",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1093_1_fit.png",
+            "identifier": "C2780128555-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "earth science",
+                "land surface",
+                "biosphere",
+                "vegetation",
+                "land use/land cover"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1093",
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
             "spatial": "-68.5 -10.5 -54.5 -2.0",
+            "temporal": "1974-01-01T00:00:00Z/1998-06-18T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO LC-03 SAR Images, Land Cover, and Biomass, Four Areas across Brazilian Amazon"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7265/N5FT8HZS",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "International Polar Year Historical Data and Literature, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center. https://doi.org/10.7265/N5FT8HZS.",
-            "issued": "1882-01-01",
-            "temporal": "1882-01-01T00:00:00Z/2007-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2007-12-31",
-            "keyword": [
-                "salinity/density",
-                "paleoclimate",
-                "land records",
-                "ionosphere/magnetosphere dynamics",
-                "ice core records",
-                "glaciers/ice sheets",
-                "atmosphere",
-                "snow/ice",
-                "terrestrial hydrosphere",
-                "atmospheric temperature",
-                "cryosphere",
-                "oceans",
-                "solar activity",
-                "seismology",
-                "solid earth",
-                "sea ice",
-                "earth science",
-                "geomorphology",
-                "frozen ground",
-                "ocean temperature",
-                "aerosols",
-                "atmospheric electricity",
-                "atmospheric pressure",
-                "sun-earth interactions",
-                "land surface"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ruth Duerr",
                 "hasEmail": "mailto:rduerr@nsidc.org"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NSIDC"
-            },
-            "identifier": "C1386206531-NSIDCV0",
             "description": "The International Polar Year Historical Data and Literature collection (formerly known as the Discovery and Access of Historic Literature from the IPYs (DAHLI) project) is an online data collection consisting primarily of photographs, publications, and observational data records from, and relating to, the first two International Polar Years (IPY) 1882-83 and 1932-33 and the International Geophysical Year (IGY)1957-58. Examples of data contained in observational records include, but are not limited to: air magnetic vertical intensity, air conductivity, atmospheric-electric observations, auroral log data, potential-gradient electrographic data, dust counts, and meteorological observations.  Photographs within the collection include those from the Wilkes Station in Antarctica, the USGS survey of Fletcher's Ice Island, and the DTM Geophysical Laboratory Library.  Publications within this collection primarily consist of government (national and international) bulletins and reports on activities during the International Polar and International Geophysical years.  Other data include audio files of interviews recorded during NCAR's Oral Histories Project, and a video on Drifting Station Alpha during the IGY, published by NSIDC.",
-            "title": "International Polar Year Historical Data and Literature, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN5FT8HZS",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN5FT8HZS",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/G02201_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/G02201_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/G02201_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/G02201_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/G02201_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/G02201_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/G02201_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/G02201_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/G02201_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/G02201_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/G02201_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/G02201_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5FT8HZS",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/N5FT8HZS",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5FT8HZS",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/N5FT8HZS",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386206531-NSIDCV0",
+            "issued": "1882-01-01",
+            "keyword": [
+                "salinity/density",
+                "paleoclimate",
+                "land records",
+                "ionosphere/magnetosphere dynamics",
+                "ice core records",
+                "glaciers/ice sheets",
+                "atmosphere",
+                "snow/ice",
+                "terrestrial hydrosphere",
+                "atmospheric temperature",
+                "cryosphere",
+                "oceans",
+                "solar activity",
+                "seismology",
+                "solid earth",
+                "sea ice",
+                "earth science",
+                "geomorphology",
+                "frozen ground",
+                "ocean temperature",
+                "aerosols",
+                "atmospheric electricity",
+                "atmospheric pressure",
+                "sun-earth interactions",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.7265/N5FT8HZS",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2007-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1882-01-01T00:00:00Z/2007-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "International Polar Year Historical Data and Literature, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MRO-M-CRISM-3-RDR-TARGETED-V1.0",
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
+            "description": "This dataset is intended to include IR and VNIR data from the CRISM instrument on MRO, processed to several different levels. The core structure parallels that of an EDR with a multiband image and a text file containing frame-specific housekeeping information for each of the concatenated image frames in the multiband image. However the image data has been converted to units of radiance using level-4 and level-6 CDRs, and analog housekeeping items in the text file (voltages, currents, and temperatures) have been converted into physical units using a level-6 CDR. Both files share a common label. A TRDR may also contain separately labeled multiband images in which radiance has been processed to I/F (radiance divided by (pi * solar flux at 1 AU * heliocentric distance^2)), Lambert albedo, or a set of derived spectral parameters (summary products) that provide an overview of the data set. The summary products include Lambert albedo at key wavelengths, or key band depths or spectral reflectance ratios. To create Lambert albedo or most summary products, estimated corrections for atmospheric and photometric effects are applied to the I/F data.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mro-m-crism-3-rdr-targeted-v1.0_4dc2-g7ub",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "mars reconnaissance orbiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MRO-M-CRISM-3-RDR-TARGETED-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mro-m-crism-3-rdr-targeted-v1.0_4dc2-g7ub",
-            "description": "This dataset is intended to include IR and VNIR data from the CRISM instrument on MRO, processed to several different levels. The core structure parallels that of an EDR with a multiband image and a text file containing frame-specific housekeeping information for each of the concatenated image frames in the multiband image. However the image data has been converted to units of radiance using level-4 and level-6 CDRs, and analog housekeeping items in the text file (voltages, currents, and temperatures) have been converted into physical units using a level-6 CDR. Both files share a common label. A TRDR may also contain separately labeled multiband images in which radiance has been processed to I/F (radiance divided by (pi * solar flux at 1 AU * heliocentric distance^2)), Lambert albedo, or a set of derived spectral parameters (summary products) that provide an overview of the data set. The summary products include Lambert albedo at key wavelengths, or key band depths or spectral reflectance ratios. To create Lambert albedo or most summary products, estimated corrections for atmospheric and photometric effects are applied to the I/F data.",
-            "title": "MRO CRISM TARGETED REDUCED DATA RECORD V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MRO CRISM TARGETED REDUCED DATA RECORD V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-MOLA-5-IEGDR-L3-V1.0",
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
-                "mars global surveyor"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The IEGDR product is a global map of planetary radius, areiod,topography, and number of observations, derived from MOLA PEDR products and aggregated into latitude-longitude bins. The IEGDR is released in two formats, an ASCII table and an image. The table (this data set) has one row for each latitude-longitude bin, from 90 to -90 degrees latitude and from 0 to 360 degrees longitude. Values for planetary radius, areoid, topography, and number of observations per bin are stored as columns in the table.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-mola-5-iegdr-l3-v1.0_4dfr-yi42",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars global surveyor"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-MOLA-5-IEGDR-L3-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-mola-5-iegdr-l3-v1.0_4dfr-yi42",
-            "description": "The IEGDR product is a global map of planetary radius, areiod,topography, and number of observations, derived from MOLA PEDR products and aggregated into latitude-longitude bins. The IEGDR is released in two formats, an ASCII table and an image. The table (this data set) has one row for each latitude-longitude bin, from 90 to -90 degrees latitude and from 0 to 360 degrees longitude. Values for planetary radius, areoid, topography, and number of observations per bin are stored as columns in the table.",
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
-            "landingPage": "https://doi.org/10.5067/ADEOS-I/OCTS/L3M/IOP/2014",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/ADEOS-I/OCTS/L3M/IOP/2014.",
-            "issued": "2017-01-11",
-            "temporal": "1996-11-01T00:00:00Z/1997-06-30T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-10-10",
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
-            "identifier": "C1200034365-OB_DAAC",
             "description": "On August 17, 1996, the Japanese Space Agency (NASDA - National Space Development Agency)\nlaunched the Advanced Earth Observing Satellite (ADEOS). ADEOS was in a descending, Sun\nsynchronous orbit with a nominal equatorial crossing time of 10:30 a.m. Amoung the\ninstruments carried aboard the ADEOS spacecraft was the Ocean Color and Temperature\nScanner (OCTS). OCTS is an optical radiometer with 12 bands covering the visible, near\ninfrared and thermal infrared regions. (Eight of the bands are in the VIS/NIR. These are\nthe only bands calibrated and processed by the OBPG) OCTS has a swath width of\napproximately 1400 km, and a nominal nadir resolution of 700 m. The instrument operated\nat three tilt states (20 degrees aft, nadir and 20 degrees fore), similar to SeaWiFS.",
-            "title": "ADEOS-I Ocean Color and Temperature Scanner (OCTS) Inherent Optical Properties (IOP) Global Mapped Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FADEOS-I%2FOCTS%2FL3M%2FIOP%2F2014",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FADEOS-I%2FOCTS%2FL3M%2FIOP%2F2014",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/OCTS/L3SMI/",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/OCTS/L3SMI/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/OCTS/L3SMI/",
-                    "description": "OPeNDAP Site for OCTS Small Mapped Image (SMI) Product Suite",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP Site for OCTS Small Mapped Image (SMI) Product Suite",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/OCTS/L3SMI/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/octs",
-                    "description": "NASA Ocean Color Web - Instrument Description Page",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Instrument Description Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/octs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/atbd/giop",
-                    "description": "NASA Ocean Color Web - Algorithm Descriptions",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Algorithm Descriptions",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/atbd/giop",
+                    "mediaType": "text/html",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/reprocessing",
-                    "description": "NASA Ocean Color Web - Data Processing History",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Processing History",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/reprocessing",
+                    "mediaType": "text/html",
                     "title": "View this dataset's processing history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/ADEOS-I/OCTS/L3M/IOP/2014",
-                    "description": "OB.DAAC OCTS ADEOS-I L3M Inherent Optical Properties (IOP) Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "OB.DAAC OCTS ADEOS-I L3M Inherent Optical Properties (IOP) Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/ADEOS-I/OCTS/L3M/IOP/2014",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/forum/oceancolor/forum_show.pl",
-                    "description": "Ocean Color Forum",
                     "@type": "dcat:Distribution",
+                    "description": "Ocean Color Forum",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/forum/oceancolor/forum_show.pl",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1200034365-OB_DAAC",
+            "issued": "2017-01-11",
+            "keyword": [
+                "ocean optics",
+                "oceans",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ADEOS-I/OCTS/L3M/IOP/2014",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-10-10",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1996-11-01T00:00:00Z/1997-06-30T23:59:59Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ADEOS-I Ocean Color and Temperature Scanner (OCTS) Inherent Optical Properties (IOP) Global Mapped Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-GRAND-5-CERES-HYDROGEN-MAP_V1.0",
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
-                "1 ceres"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "A global map of the                     concentration of hydrogen within the regolith of asteroid 1 Ceres       on twenty-degree quasi-equal-area pixels is provided. Hydrogen          concentrations were determined from thermal+epithermal neutron          counting data acquired by the NASA Dawn mission's Gamma Ray and Neutron Detector (GRaND) while in low altitude mapping orbit, about 385 km from Ceres' surface (about 0.8 body radii altitude).  The concentrations are representative of Ceres's bulk  regolith to depths up to a few          decimeters with a spatial resolution of about 600-km                    full-width-at-half-maximum of arc length on the surface. The methods    used to determine hydrogen concentration are described by               PRETTYMANETAL2017.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-grand-5-ceres-hydrogen-map_v1.0_4dj4-77ah",
+            "issued": "2021-05-21",
+            "keyword": [
+                "dawn mission to vesta and ceres",
+                "1 ceres"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-GRAND-5-CERES-HYDROGEN-MAP_V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-grand-5-ceres-hydrogen-map_v1.0_4dj4-77ah",
-            "description": "A global map of the                     concentration of hydrogen within the regolith of asteroid 1 Ceres       on twenty-degree quasi-equal-area pixels is provided. Hydrogen          concentrations were determined from thermal+epithermal neutron          counting data acquired by the NASA Dawn mission's Gamma Ray and Neutron Detector (GRaND) while in low altitude mapping orbit, about 385 km from Ceres' surface (about 0.8 body radii altitude).  The concentrations are representative of Ceres's bulk  regolith to depths up to a few          decimeters with a spatial resolution of about 600-km                    full-width-at-half-maximum of arc length on the surface. The methods    used to determine hydrogen concentration are described by               PRETTYMANETAL2017.",
-            "title": "DAWN GRAND MAP CERES                    \n                                      HYDROGEN MAP V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "DAWN GRAND MAP CERES                    \n                                      HYDROGEN MAP V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-C-PTOLEMY-3-FSS-V1.0",
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
+            "description": "This archive contains calibrated data from the PTOLEMY instrument onboard ROSETTA Lander, acquired during the FSS mission phase. The primary target is the comet 67P/CHURYUMOV-GERASIMENKO. It also contains documentation which describes the PTOLEMY experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-c-ptolemy-3-fss-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-C-PTOLEMY-3-FSS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-c-ptolemy-3-fss-v1.0",
-            "description": "This archive contains calibrated data from the PTOLEMY instrument onboard ROSETTA Lander, acquired during the FSS mission phase. The primary target is the comet 67P/CHURYUMOV-GERASIMENKO. It also contains documentation which describes the PTOLEMY experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER 67P PTOLEMY 3 FSS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-LANDER 67P PTOLEMY 3 FSS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/4dmg-hyyh",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "To further development of our gene expression approach to biodosimetry we have employed whole genome microarray expression profiling as a discovery platform to identify genes with the potential to distinguish radiation dose across an exposure range relevant for medical decision-making in a radiological emergency. Human peripheral blood from healthy donors was irradiated ex vivo and a 74-gene consensus signature was identified that distinguished between four radiation doses (0.5 2 5 and 8 Gy) and control samples. The same set of genes separated samples by exposure level at both six and 24 hours after treatment with overlap evident only at the highest two doses (5 and 8 Gy). Expression of five genes (CDKN1A FDXR SESN1 BBC3 and PHPT1) from this signature was quantified in the same RNA samples by real-time PCR confirming low variability between donors as well as the predicted radiation response pattern. Experiment Overall Design: Radiation induced gene expression in human blood was measured at 6 and 24 hours after exposure to doses of 0 0.5 2 5 and 8 Gy g-rays. Five independent experiments were performed at each time (6 or 24 hours) using different donors for each experiment",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-152",
+                    "mediaType": "text/html",
+                    "title": "Transcription profiling of human peripheral blood to development gene expression signatures for practical radiation biodosimetry"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-152_4dmg-hyyh",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "p-g8917-5",
                 "p-g8917-3",
@@ -134258,82 +134272,41 @@
                 "p-g8917-6",
                 "p-g8917-4"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/4dmg-hyyh",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-152_4dmg-hyyh",
-            "description": "To further development of our gene expression approach to biodosimetry we have employed whole genome microarray expression profiling as a discovery platform to identify genes with the potential to distinguish radiation dose across an exposure range relevant for medical decision-making in a radiological emergency. Human peripheral blood from healthy donors was irradiated ex vivo and a 74-gene consensus signature was identified that distinguished between four radiation doses (0.5 2 5 and 8 Gy) and control samples. The same set of genes separated samples by exposure level at both six and 24 hours after treatment with overlap evident only at the highest two doses (5 and 8 Gy). Expression of five genes (CDKN1A FDXR SESN1 BBC3 and PHPT1) from this signature was quantified in the same RNA samples by real-time PCR confirming low variability between donors as well as the predicted radiation response pattern. Experiment Overall Design: Radiation induced gene expression in human blood was measured at 6 and 24 hours after exposure to doses of 0 0.5 2 5 and 8 Gy g-rays. Five independent experiments were performed at each time (6 or 24 hours) using different donors for each experiment",
-            "title": "Transcription profiling of human peripheral blood to development gene expression signatures for practical radiation biodosimetry",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-152",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Transcription profiling of human peripheral blood to development gene expression signatures for practical radiation biodosimetry"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Transcription profiling of human peripheral blood to development gene expression signatures for practical radiation biodosimetry"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/MEASURES/OZONE/DATA209",
             "citation": "P.K. Bhartia, et al.. 2012-09-10. SBUV2N19L2. Version 1. SBUV2/NOAA-19 Ozone (O3) Nadir Profile and Total Column 1 Day L2 V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/MEASURES/OZONE/DATA209. https://disc.gsfc.nasa.gov/datacollection/SBUV2N19L2_1.html. Digital Science Data.",
-            "issued": "2013-08-29",
-            "temporal": "2009-02-23T00:00:00Z/2013-08-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2013-08-29",
-            "references": [
-                "https://doi.org/doi:10.5194/amt-5-2951-2012",
-                "https://doi.org/doi:10.5194/amt-6-2533-2013",
-                "https://doi.org/doi:10.1002/jgrd.50597"
-            ],
-            "keyword": [
-                "atmosphere",
-                "atmospheric chemistry",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "RICHARD MCPETERS, PH. D",
                 "hasEmail": "mailto:richard.d.mcpeters@nasa.gov"
             },
+            "creator": "P.K. Bhartia, et al.",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1251051657-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The Solar Backscattered Ultraviolet (SBUV) from NOAA-19 Level-2 daily product (SBUV2N19L2) contains ozone nadir profile and total column data from retrievals generated from the v8.6 SBUV algorithm. The v8.6 SBUV algorithm estimates the ozone nadir profile and total column from SBUV measurements using 1) the Brion-Daumont-Malicet ozone cross sections, 2) an OMI-derived cloud-height climatology, 3) a revised a priori ozone climatology, and 4) inter-instrument calibration based on comparisons with no local time difference.\n\nThe SBUV2N19L2 product is written as daily files using the HDF5 format, with file sizes ranging from about 1 to 5 Mbytes. Data are available from February 2009 through July 2013. The SBUV2N19L2 data product was used as input in creating the SBUV2N19L3zm monthly zonal mean data product.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "SBUV2N19L2",
-            "creator": "P.K. Bhartia, et al.",
-            "title": "SBUV2/NOAA-19 Ozone (O3) Nadir Profile and Total Column 1 Day L2 V1 (SBUV2N19L2) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SBUV2N19L2_1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FOZONE%2FDATA209",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FOZONE%2FDATA209",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -134343,206 +134316,245 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SBUV2N19L2_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SBUV2N19L2_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/Ozone/SBUV2N19L2.1/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/Ozone/SBUV2N19L2.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/Ozone/SBUV2N19L2.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/Ozone/SBUV2N19L2.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/Ozone/SBUV2N19L2.1/catalog.xml",
-                    "description": "Access the data using the THREDDS Catalog.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data using the THREDDS Catalog.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/Ozone/SBUV2N19L2.1/catalog.xml",
+                    "mediaType": "text/html",
                     "title": "Use THREDDS DATA to download the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/Ozone/SBUV2N19L2.1/doc/README.SBUVL2.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/Ozone/SBUV2N19L2.1/doc/README.SBUVL2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SBUV2N19L2_1.png",
+            "identifier": "C1251051657-GES_DISC",
+            "issued": "2013-08-29",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/OZONE/DATA209",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2013-08-29",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/doi:10.5194/amt-5-2951-2012",
+                "https://doi.org/doi:10.5194/amt-6-2533-2013",
+                "https://doi.org/doi:10.1002/jgrd.50597"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "SBUV2N19L2",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2009-02-23T00:00:00Z/2013-08-01T23:59:59.999Z",
             "theme": [
                 "MEaSUREs",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SBUV2/NOAA-19 Ozone (O3) Nadir Profile and Total Column 1 Day L2 V1 (SBUV2N19L2) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DC3_jValue_AircraftInSitu_NSF-GV-HIAPER_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2021-04-29. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/DC3_jValue_AircraftInSitu_NSF-GV-HIAPER_Data_1.",
-            "issued": "2021-03-12",
-            "temporal": "2012-05-01T00:00:00Z/2012-06-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-04-29",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric chemistry"
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
-            "identifier": "C2047155076-LARC_ASDC",
             "description": "DC3_jValue_AircraftInSitu_NSF-GV-HIAPER_Data are in-situ photolysis rate data collected onboard the NSF/NCAR GV-HIAPER aircraft during the Deep Convective Clouds and Chemistry (DC3) field campaign. Data collection for this product is complete.\r\n\r\nThe Deep Convective Clouds and Chemistry (DC3) field campaign sought to understand the dynamical, physical, and lightning processes of deep, mid-latitude continental convective clouds and to define the impact of these clouds on upper tropospheric composition and chemistry. DC3 was conducted from May to June 2012 with a base location of Salina, Kansas. Observations were conducted in northeastern Colorado, west Texas to central Oklahoma, and northern Alabama in order to provide a wide geographic sample of storm types and boundary layer compositions, as well as to sample convection.\r\nDC3 had two primary science objectives. The first was to investigate storm dynamics and physics, lightning and its production of nitrogen oxides, cloud hydrometeor effects on wet deposition of species, surface emission variability, and chemistry in anvil clouds. Observations related to this objective focused on the early stages of active convection. The second objective was to investigate changes in upper tropospheric chemistry and composition after active convection. Observations related to this objective focused on the 12-48 hours following convection. This objective also served to explore seasonal change of upper tropospheric chemistry.\r\nIn addition to using the NSF/NCAR Gulfstream-V (GV) aircraft, the NASA DC-8 was used during DC3 to provide in-situ measurements of the convective storm inflow and remotely-sensed measurements used for flight planning and column characterization. DC3 utilized ground-based radar networks spread across its observation area to measure the physical and kinematic characteristics of storms. Additional sampling strategies relied on lightning mapping arrays, radiosondes, and precipitation collection. Lastly, DC3 used data collected from various satellite instruments to achieve its goals, focusing on measurements from CALIOP onboard CALIPSO and CPL onboard CloudSat. In addition to providing an extensive set of data related to deep, mid-latitude continental convective clouds and analyzing their impacts on upper tropospheric composition and chemistry, DC3 improved models used to predict convective transport. DC3 improved knowledge of convection and chemistry, and provided information necessary to understanding the processes relating to ozone in the upper troposphere.",
-            "title": "DC3 In-Situ NSF/NCAR GV-HIAPER Photolysis Rate Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDC3_jValue_AircraftInSitu_NSF-GV-HIAPER_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDC3_jValue_AircraftInSitu_NSF-GV-HIAPER_Data_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "description": "DC3 Experimental Design Overview",
                     "@type": "dcat:Distribution",
+                    "description": "DC3 Experimental Design Overview",
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
                     "title": "The dataset's project home page"
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2047155076-LARC_ASDC",
-                    "description": "Earthdata Search for DC3_jValue_AircraftInSitu_NSF-GV-HIAPER_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for DC3_jValue_AircraftInSitu_NSF-GV-HIAPER_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2047155076-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/DC3/jValue_AircraftInSitu_NSF-GV-HIAPER_Data_1/",
-                    "description": "ASDC Direct Data Download for DC3_jValue_AircraftInSitu_NSF-GV-HIAPER_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for DC3_jValue_AircraftInSitu_NSF-GV-HIAPER_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/DC3/jValue_AircraftInSitu_NSF-GV-HIAPER_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2047155076-LARC_ASDC",
+            "issued": "2021-03-12",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DC3_jValue_AircraftInSitu_NSF-GV-HIAPER_Data_1",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>20.0 -125.0 20.0 -75.0 45.0 -75.0 45.0 -125.0 20.0 -125.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2012-05-01T00:00:00Z/2012-06-30T23:59:59.999Z",
             "theme": [
                 "DC3",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "DC3 In-Situ NSF/NCAR GV-HIAPER Photolysis Rate Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://svs.gsfc.nasa.gov/Gallery/index.html",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Jocelyn Thomas Jones",
+                "hasEmail": "mailto:jocelyn.t.jones@nasa.gov"
+            },
+            "description": "The Scientific Visualization Studio hosts a collection of media galleries on Earth, air, and space themes.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://svs.gsfc.nasa.gov/Gallery/index.html",
+                    "mediaType": "application/html"
+                }
+            ],
+            "identifier": "NASA-907",
             "issued": "1997-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "ozone",
                 "mars",
@@ -134560,649 +134572,619 @@
                 "solar sun",
                 "fire"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Jocelyn Thomas Jones",
-                "hasEmail": "mailto:jocelyn.t.jones@nasa.gov"
-            },
+            "landingPage": "https://svs.gsfc.nasa.gov/Gallery/index.html",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-907",
-            "description": "The Scientific Visualization Studio hosts a collection of media galleries on Earth, air, and space themes.",
-            "title": "NASA Scientific Visualization Studio Galleries",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://svs.gsfc.nasa.gov/Gallery/index.html",
-                    "mediaType": "application/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NASA Scientific Visualization Studio Galleries"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1735",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Gately, C., L.R. Hutyra, and I.S. Wing. 2019. DARTE Annual On-road CO2 Emissions on a 1-km Grid, Conterminous USA, V2, 1980-2017. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1735",
-            "issued": "2019-09-27",
-            "temporal": "1980-01-01T00:00:00Z/2017-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "human dimensions",
-                "atmosphere",
-                "atmospheric chemistry",
-                "earth science",
-                "environmental impacts"
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
-            "identifier": "C2389100132-ORNL_CLOUD",
             "description": "This data set provides a 38-year, 1-km resolution inventory of annual on-road CO2 emissions for the conterminous United States based on roadway-level vehicle traffic data and state-specific emissions factors for multiple vehicle types on urban and rural roads as compiled in the Database of Road Transportation Emissions (DARTE). CO2 emissions from the on-road transportation sector are provided annually for 1980-2017 as a continuous surface at a spatial resolution of 1 km.",
-            "graphic-preview-description": "Map of DARTE 2017 on-road CO2 emissions for the conterminous United States.",
-            "title": "DARTE Annual On-road CO2 Emissions on a 1-km Grid, Conterminous USA, V2, 1980-2017",
-            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/CMS_DARTE_V2_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1735",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1735",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/cms/CMS_DARTE_V2/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/cms/CMS_DARTE_V2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_DARTE_V2.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_DARTE_V2.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1735",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1735",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/CMS_DARTE_V2/comp/CMS_DARTE_V2.pdf",
-                    "description": "DARTE Annual On-road CO2 Emissions on a 1-km Grid, Conterminous USA V2, 1980-2017: CMS_DARTE_V2.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "DARTE Annual On-road CO2 Emissions on a 1-km Grid, Conterminous USA V2, 1980-2017: CMS_DARTE_V2.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/CMS_DARTE_V2/comp/CMS_DARTE_V2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_DARTE_V2_Fig1.png",
-                    "description": "Map of DARTE 2017 on-road CO2 emissions for the conterminous United States.",
                     "@type": "dcat:Distribution",
+                    "description": "Map of DARTE 2017 on-road CO2 emissions for the conterminous United States.",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_DARTE_V2_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1735",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1735",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Map of DARTE 2017 on-road CO2 emissions for the conterminous United States.",
+            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/CMS_DARTE_V2_Fig1.png",
+            "identifier": "C2389100132-ORNL_CLOUD",
+            "issued": "2019-09-27",
+            "keyword": [
+                "human dimensions",
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science",
+                "environmental impacts"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1735",
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
             "spatial": "-137.26 22.09 -62.04 53.39",
+            "temporal": "1980-01-01T00:00:00Z/2017-12-31T23:59:59Z",
             "theme": [
                 "CMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "DARTE Annual On-road CO2 Emissions on a 1-km Grid, Conterminous USA, V2, 1980-2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Colorado_AircraftRemoteSensing_Falcon_GeoTASO_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2022-04-18. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Colorado_AircraftRemoteSensing_Falcon_GeoTASO_Data_1.",
-            "issued": "2021-08-20",
-            "temporal": "2014-07-22T00:00:00Z/2014-08-15T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-18",
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
-            "identifier": "C2254457470-LARC_ASDC",
             "description": "DISCOVERAQ_Colorado_AircraftRemoteSensing_Falcon_GeoTASO_Data contains remotely sensed data collected by the Geostationary Trace gas and Aerosol Optimization (GeoTASO) onboard NASA's B-200 aircraft during the Colorado (Denver) deployment of NASA's DISCOVER-AQ field study. This data product contains data for only the Colorado deployment, and data collection is complete.\r\n\r\nUnderstanding the factors that contribute to near surface pollution is difficult using only satellite-based observations. The incorporation of surface-level measurements from aircraft and ground-based platforms provides the crucial information necessary to validate and expand upon the use of satellites in understanding near surface pollution. Deriving Information on Surface conditions from Column and Vertically Resolved Observations Relevant to Air Quality (DISCOVER-AQ) was a four-year campaign conducted in collaboration between NASA Langley Research Center, NASA Goddard Space Flight Center, NASA Ames Research Center, and multiple universities to improve the use of satellites to monitor air quality for public health and environmental benefit. Through targeted airborne and ground-based observations, DISCOVER-AQ enabled more effective use of current and future satellites to diagnose ground level conditions influencing air quality.\r\n\r\nDISCOVER-AQ employed two NASA aircraft, the P-3B and King Air, with the P-3B completing in-situ spiral profiling of the atmosphere (aerosol properties, meteorological variables, and trace gas species). The King Air conducted both passive and active remote sensing of the atmospheric column extending below the aircraft to the surface. Data from an existing network of surface air quality monitors, AERONET sun photometers, Pandora UV/vis spectrometers and model simulations were also collected. Further, DISCOVER-AQ employed many surface monitoring sites, with measurements being made on the ground, in conjunction with the aircraft. The B200 and P-3B conducted flights in Baltimore-Washington, D.C. in 2011, Houston, TX in 2013, San Joaquin Valley, CA in 2013, and Denver, CO in 2014. These regions were targeted due to being in violation of the National Ambient Air Quality Standards (NAAQS).\r\n\r\nThe first objective of DISCOVER-AQ was to determine and investigate correlations between surface measurements and satellite column observations for the trace gases ozone (O3), nitrogen dioxide (NO2), and formaldehyde (CH2O) to understand how satellite column observations can diagnose surface conditions. DISCOVER-AQ also had the objective of using surface-level measurements to understand how satellites measure diurnal variability and to understand what factors control diurnal variability. Lastly, DISCOVER-AQ aimed to explore horizontal scales of variability, such as regions with steep gradients and urban plumes.",
-            "title": "DISCOVER-AQ Colorado Deployment Falcon Aircraft Remotely Sensed Geostationary Trace gas and Aerosol Optimization (GeoTASO) Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDISCOVERAQ_Colorado_AircraftRemoteSensing_Falcon_GeoTASO_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDISCOVERAQ_Colorado_AircraftRemoteSensing_Falcon_GeoTASO_Data_1",
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
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Texas_AircraftRemoteSensing_Falcon_GeoTASO_Data_1",
-                    "description": "DOI link for DISCOVERAQ_COLORADO_AIRCRAFTREMOTESENSING_FALCON_GEOTASO_DATA_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI link for DISCOVERAQ_COLORADO_AIRCRAFTREMOTESENSING_FALCON_GEOTASO_DATA_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Texas_AircraftRemoteSensing_Falcon_GeoTASO_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2254457470-LARC_ASDC",
-                    "description": "Earthdata Search Client for DISCOVERAQ_COLORADO_AIRCRAFTREMOTESENSING_FALCON_GEOTASO_DATA_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search Client for DISCOVERAQ_COLORADO_AIRCRAFTREMOTESENSING_FALCON_GEOTASO_DATA_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2254457470-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/DISCOVER-AQ/Colorado_AircraftRemoteSensing_Falcon_GeoTASO_Data_1/",
-                    "description": "ASDC Direct Data Download for DISCOVERAQ_Colorado_AircraftRemoteSensing_Falcon_GeoTASO_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for DISCOVERAQ_Colorado_AircraftRemoteSensing_Falcon_GeoTASO_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/DISCOVER-AQ/Colorado_AircraftRemoteSensing_Falcon_GeoTASO_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/DISCOVER-AQ/Colorado_AircraftRemoteSensing_Falcon_GeoTASO_Data_1/contents.html",
-                    "description": "OPeNDAP data access for DISCOVERAQ_Colorado_AircraftRemoteSensing_Falcon_GeoTASO_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for DISCOVERAQ_Colorado_AircraftRemoteSensing_Falcon_GeoTASO_Data_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/DISCOVER-AQ/Colorado_AircraftRemoteSensing_Falcon_GeoTASO_Data_1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2254457470-LARC_ASDC",
+            "issued": "2021-08-20",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Colorado_AircraftRemoteSensing_Falcon_GeoTASO_Data_1",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>28.0 -111.0 28.0 -65.0 48.0 -65.0 48.0 -111.0 28.0 -111.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2014-07-22T00:00:00Z/2014-08-15T23:59:59.999Z",
             "theme": [
                 "DISCOVER-AQ",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "DISCOVER-AQ Colorado Deployment Falcon Aircraft Remotely Sensed Geostationary Trace gas and Aerosol Optimization (GeoTASO) Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-TEGA-4-SCRDR-V1.0",
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
+            "description": "Calibrated or converted engineering, housekeeping and scientific data collected from the Thermal Evolved Gas Analyzer (TEGA) aboard the 2007 Mars Phoenix Lander.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-tega-4-scrdr-v1.0_4dyr-24ep",
+            "issued": "2018-06-26",
+            "keyword": [
+                "phoenix",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-TEGA-4-SCRDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-tega-4-scrdr-v1.0_4dyr-24ep",
-            "description": "Calibrated or converted engineering, housekeeping and scientific data collected from the Thermal Evolved Gas Analyzer (TEGA) aboard the 2007 Mars Phoenix Lander.",
-            "title": "PHX MARS THERMAL EVOLVED GAS ANALYZER 4 SCRDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "PHX MARS THERMAL EVOLVED GAS ANALYZER 4 SCRDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/IPHEX/MWR/DATA301",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Barros, Ana P and Maria P Cadeddu.2017. GPM Ground Validation Duke Microwave Radiometer (MWR) IPHEx [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/IPHEX/MWR/DATA301",
-            "issued": "2017-07-31",
-            "temporal": "2014-05-01T00:04:50Z/2014-06-15T23:59:57Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-09",
-            "keyword": [
-                "precipitation",
-                "atmosphere",
-                "earth science",
-                "spectral/engineering",
-                "atmospheric water vapor",
-                "atmospheric winds",
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
-            "identifier": "C1979634924-GHRC_DAAC",
             "description": "The GPM Ground Validation Duke Microwave Radiometer (MWR) IPHEx dataset consists of data collected by the MWR, which is a sensitive microwave radiometer that detects the microwave radiances  at two frequencies: 23.8 and 31.4 GHz.  The measurements are are used to determine the presence of vapor and liquid water molecules in the atmosphere along with other derived parameters.  These data were obtained during the Integrated Precipitation and Hydrology Experiment (IPHEx) field experiment, which was held in North Carolina with the goal to characterize warm season orographic precipitation regimes and the relationship between precipitation regimes and hydrologic processes in regions of complex terrain. These data are available for May 1, 2014 through June 15, 2014 and are in netCDF-3 format.",
-            "title": "GPM Ground Validation Duke Microwave Radiometer (MWR) IPHEx V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FIPHEX%2FMWR%2FDATA301",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FIPHEX%2FMWR%2FDATA301",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmmwrdukeiphx",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmmwrdukeiphx",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.osti.gov/scitech/servlets/purl/1253898",
-                    "description": "ARM Data File Standards Version 1.2",
                     "@type": "dcat:Distribution",
+                    "description": "ARM Data File Standards Version 1.2",
+                    "downloadURL": "https://www.osti.gov/scitech/servlets/purl/1253898",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www.arm.gov/publications/programdocs/doe-sc-arm-16-008.pdf",
-                    "description": "Integrated Precipitation and Hydrology Experiment (IPHEx)/Orographic Precipitation Processes Study Field Campaign Report",
                     "@type": "dcat:Distribution",
+                    "description": "Integrated Precipitation and Hydrology Experiment (IPHEx)/Orographic Precipitation Processes Study Field Campaign Report",
+                    "downloadURL": "https://www.arm.gov/publications/programdocs/doe-sc-arm-16-008.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www.arm.gov/publications/tech_reports/handbooks/mwr3c_handbook.pdf",
-                    "description": "Microwave Radiometer - 3 Channel (MWR3C) Handbook",
                     "@type": "dcat:Distribution",
+                    "description": "Microwave Radiometer - 3 Channel (MWR3C) Handbook",
+                    "downloadURL": "https://www.arm.gov/publications/tech_reports/handbooks/mwr3c_handbook.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.researchgate.net/publication/268202099_Automatic_Self-Calibration_of_ARM_Microwave_Radiometers",
-                    "description": "Automatic Self-Calibration of ARM Microwave Radiometers",
                     "@type": "dcat:Distribution",
+                    "description": "Automatic Self-Calibration of ARM Microwave Radiometers",
+                    "downloadURL": "https://www.researchgate.net/publication/268202099_Automatic_Self-Calibration_of_ARM_Microwave_Radiometers",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www.arm.gov/publications/tech_reports/handbooks/mwr_handbook.pdf",
-                    "description": "Microwave Radiometer (MWR) Handbook",
                     "@type": "dcat:Distribution",
+                    "description": "Microwave Radiometer (MWR) Handbook",
+                    "downloadURL": "https://www.arm.gov/publications/tech_reports/handbooks/mwr_handbook.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.5067/GPMGV/IPHEX/DATA101",
-                    "description": "IPHEx Field Campaign Collection DOI",
                     "@type": "dcat:Distribution",
+                    "description": "IPHEx Field Campaign Collection DOI",
+                    "downloadURL": "http://dx.doi.org/10.5067/GPMGV/IPHEX/DATA101",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/iphex/mwr_Duke/doc/gpmmwrdukeiphx_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/iphex/mwr_Duke/doc/gpmmwrdukeiphx_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1109/36.843018",
-                    "description": "Analysis and improvement of tipping calibration for ground-based microwave radiometers",
                     "@type": "dcat:Distribution",
+                    "description": "Analysis and improvement of tipping calibration for ground-based microwave radiometers",
+                    "downloadURL": "https://doi.org/10.1109/36.843018",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/2000JD900817",
-                    "description": "A new retrieval for cloud liquid water path using a ground-based microwave radiometer and measurements of cloud temperature",
                     "@type": "dcat:Distribution",
+                    "description": "A new retrieval for cloud liquid water path using a ground-based microwave radiometer and measurements of cloud temperature",
+                    "downloadURL": "https://doi.org/10.1029/2000JD900817",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/2000JD000055",
-                    "description": "Analysis of integrated cloud liquid and precipitable water vapor retrievals from microwave radiometers during the Surface Heat Budget of the Arctic Ocean project",
                     "@type": "dcat:Distribution",
+                    "description": "Analysis of integrated cloud liquid and precipitable water vapor retrievals from microwave radiometers during the Surface Heat Budget of the Arctic Ocean project",
+                    "downloadURL": "https://doi.org/10.1029/2000JD000055",
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
+            "identifier": "C1979634924-GHRC_DAAC",
+            "issued": "2017-07-31",
+            "keyword": [
+                "precipitation",
+                "atmosphere",
+                "earth science",
+                "spectral/engineering",
+                "atmospheric water vapor",
+                "atmospheric winds",
+                "infrared wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/IPHEX/MWR/DATA301",
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
             "spatial": "-83.0948 35.5199 -82.6604 35.8046",
+            "temporal": "2014-05-01T00:04:50Z/2014-06-15T23:59:57Z",
             "theme": [
                 "IPHEx",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM Ground Validation Duke Microwave Radiometer (MWR) IPHEx V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4416V05",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Yale Center for Environmental Law and Policy - YCELP - Yale University, Center for International Earth Science Information Network - CIESIN - Columbia University, and World Economic Forum - WEF. 2014-04-17. 2014 Environmental Performance Index (EPI). Version 2014.00. New Haven, CT. Archived by National Aeronautics and Space Administration, U.S. Government, Yale Center for Environmental Law and Policy (YCELP)/Yale University. https://doi.org/10.7927/H4416V05. https://doi.org/10.7927/H4416V05.",
-            "issued": "2014-04-17",
-            "temporal": "2002-01-01T00:00:00Z/2014-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2014-04-17",
-            "references": [
-                "https://doi.org/10.7927/H44M92GX",
-                "https://doi.org/10.7927/H4HT2M77",
-                "https://doi.org/10.7927/H4D21VHT",
-                "https://doi.org/10.7927/H48913SG",
-                "https://doi.org/10.7927/H4FX77CS",
-                "https://doi.org/10.7927/H4X928CF",
-                "https://doi.org/10.7927/f54c-0r44"
-            ],
-            "keyword": [
-                "human dimensions",
-                "earth science",
-                "sustainability"
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
-            "identifier": "C1000000541-SEDAC",
-            "description": "The 2014 Environmental Performance Index (EPI) ranks 178 countries on 20 performance indicators in the following 9 policy categories: health impacts, air quality, water and sanitation, water resources, agriculture, forests, fisheries, biodiversity and habitat, and climate and energy. These categories track performance and progress on two broad policy objectives, environmental health and ecosystem vitality. The EPI's proximity-to-target methodology facilitates cross-country comparisons among economic and regional peer groups. The data set includes the 2014 EPI and component scores, backcast EPI scores for 2002-2012, and time-series source data. The 2014 EPI was formally released in Davos, Switzerland, at the annual meeting of the World Economic Forum on January 25, 2014. These are the result of collaboration between the Yale Center for Environmental Law and Policy (YCELP) and the Columbia University Center for International Earth Science Information Network (CIESIN). The Interactive Website for the 2014 EPI is at http://epi.yale.edu/.",
-            "release-place": "New Haven, CT",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Yale Center for Environmental Law and Policy - YCELP - Yale University, Center for International Earth Science Information Network - CIESIN - Columbia University, and World Economic Forum - WEF",
-            "title": "2014 Environmental Performance Index (EPI)",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/epi-environmental-performance-index-2014/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The 2014 Environmental Performance Index (EPI) ranks 178 countries on 20 performance indicators in the following 9 policy categories: health impacts, air quality, water and sanitation, water resources, agriculture, forests, fisheries, biodiversity and habitat, and climate and energy. These categories track performance and progress on two broad policy objectives, environmental health and ecosystem vitality. The EPI's proximity-to-target methodology facilitates cross-country comparisons among economic and regional peer groups. The data set includes the 2014 EPI and component scores, backcast EPI scores for 2002-2012, and time-series source data. The 2014 EPI was formally released in Davos, Switzerland, at the annual meeting of the World Economic Forum on January 25, 2014. These are the result of collaboration between the Yale Center for Environmental Law and Policy (YCELP) and the Columbia University Center for International Earth Science Information Network (CIESIN). The Interactive Website for the 2014 EPI is at http://epi.yale.edu/.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4416V05",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4416V05",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/epi/epi-environmental-performance-index-2014/epi2014-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/epi/epi-environmental-performance-index-2014/epi2014-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/epi-environmental-performance-index-2014/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/epi-environmental-performance-index-2014/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/epi-environmental-performance-index-2014/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/epi-environmental-performance-index-2014/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/epi-environmental-performance-index-2014/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/epi-environmental-performance-index-2014/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/epi-environmental-performance-index-2014/maps/services",
-                    "description": "Web Map Service Page",
                     "@type": "dcat:Distribution",
+                    "description": "Web Map Service Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/epi-environmental-performance-index-2014/maps/services",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/epi-environmental-performance-index-2014",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/epi-environmental-performance-index-2014",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/epi-environmental-performance-index-2014/maps",
+            "identifier": "C1000000541-SEDAC",
+            "issued": "2014-04-17",
+            "keyword": [
+                "human dimensions",
+                "earth science",
+                "sustainability"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4416V05",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2014-04-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H44M92GX",
+                "https://doi.org/10.7927/H4HT2M77",
+                "https://doi.org/10.7927/H4D21VHT",
+                "https://doi.org/10.7927/H48913SG",
+                "https://doi.org/10.7927/H4FX77CS",
+                "https://doi.org/10.7927/H4X928CF",
+                "https://doi.org/10.7927/f54c-0r44"
+            ],
+            "release-place": "New Haven, CT",
             "spatial": "-180.0 -55.0 180.0 90.0",
+            "temporal": "2002-01-01T00:00:00Z/2014-12-31T00:00:00Z",
             "theme": [
                 "EPI",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "2014 Environmental Performance Index (EPI)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MIDAS-3-ESC1-SAMPLES-V1.0",
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
+            "description": "The Micro-Imaging Dust Analysis System (MIDAS) is an instrument on the\nROSETTA Orbiter that will provide 3D images and statistical parameters\nof pristine cometary particles hitting the detector. This data set\nincludes all data from the COMET ESCORT 1 mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-midas-3-esc1-samples-v1.0_4e2e-j52e",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MIDAS-3-ESC1-SAMPLES-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-midas-3-esc1-samples-v1.0_4e2e-j52e",
-            "description": "The Micro-Imaging Dust Analysis System (MIDAS) is an instrument on the\nROSETTA Orbiter that will provide 3D images and statistical parameters\nof pristine cometary particles hitting the detector. This data set\nincludes all data from the COMET ESCORT 1 mission phase.",
-            "title": "ROSETTA-ORBITER 67P MIDAS 3 ESC1 SAMPLES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER 67P MIDAS 3 ESC1 SAMPLES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-C-MRI-2-9P-ENCOUNTER-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains raw 9P/Tempel 1 and science calibration images acquired by the Deep Impact Deep Impact Medium Resolution Instrument Visible CCD during the 9P encounter phase of the mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-c-mri-2-9p-encounter-v1.0_4e2i-29ax",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "9p/tempel 1 (1867 g1)",
                 "deep impact",
                 "calibration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-C-MRI-2-9P-ENCOUNTER-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-c-mri-2-9p-encounter-v1.0_4e2i-29ax",
-            "description": "This data set contains raw 9P/Tempel 1 and science calibration images acquired by the Deep Impact Deep Impact Medium Resolution Instrument Visible CCD during the 9P encounter phase of the mission.",
-            "title": "DEEP IMPACT 9P/TEMPEL ENCOUNTER - RAW MRI DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "DEEP IMPACT 9P/TEMPEL ENCOUNTER - RAW MRI DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/4e3u-5sk9",
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
-                "nen",
-                "space science"
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
-            "identifier": "NASA-0000037__11",
+            "describedBy": "http://www.lpi.usra.edu/resources/gc/gcreadme.html",
             "description": "Planetary nomenclature, like terrestrial nomenclature, is used to uniquely identify a feature on the surface of a planet or satellite so that the feature can be easily located, described, and discussed. This gazetteer contains detailed information about all names of topographic and albedo features on planets and satellites (and some planetary ring and ring-gap systems) that the International Astronomical Union (IAU) has named and approved from its founding in 1919 through the present time.",
-            "title": "Gateway to Astronaut Photography of Earth",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -135210,21 +135192,48 @@
                     "mediaType": "text/html"
                 }
             ],
-            "describedBy": "http://www.lpi.usra.edu/resources/gc/gcreadme.html",
-            "accrualPeriodicity": "irregular"
+            "identifier": "NASA-0000037__11",
+            "issued": "2018-06-25",
+            "keyword": [
+                "wise",
+                "geography",
+                "nen",
+                "space science"
+            ],
+            "landingPage": "https://data.nasa.gov/d/4e3u-5sk9",
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
+            "description": "CDA, CIRS, ISS, RADAR, RSS, UVIS, VIMS, SPICE",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/PDS-Subscription-Service-06-Feb-07.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-708",
+            "issued": "2018-06-25",
             "keyword": [
                 "iss",
                 "vims",
@@ -135236,45 +135245,38 @@
                 "rss",
                 "pds"
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
-            "identifier": "NASA-708",
-            "description": "CDA, CIRS, ISS, RADAR, RSS, UVIS, VIMS, SPICE",
-            "title": "PDS Cassini Data Release 6 & 7",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/PDS-Subscription-Service-06-Feb-07.shtml",
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
+            "title": "PDS Cassini Data Release 6 & 7"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-E%2FV%2FH-MLA-3%2F4-CDR%2FRDR-DATA-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Abstract ======== This data set consists of the MESSENGER Mercury Laser Altimeter (MLA) Calibrated Data Record (CDR) and Reduced Data Record (RDR) products. The MLA is a solid-state pulsed laser that measures the distance between the spacecraft and the surface of Mercury. The CDR products contain the science and auxiliary data products calibrated to physical units. The RDR products contain the calibrated, geolocated range data as profile measurements of the planetary radius.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-e-v-h-mla-3-4-cdr-rdr-data-v1.0_4e5y-ytdn",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "earth",
                 "mercury",
@@ -135282,233 +135284,211 @@
                 "venus",
                 "calibration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-E%2FV%2FH-MLA-3%2F4-CDR%2FRDR-DATA-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-e-v-h-mla-3-4-cdr-rdr-data-v1.0_4e5y-ytdn",
-            "description": "Abstract ======== This data set consists of the MESSENGER Mercury Laser Altimeter (MLA) Calibrated Data Record (CDR) and Reduced Data Record (RDR) products. The MLA is a solid-state pulsed laser that measures the distance between the spacecraft and the surface of Mercury. The CDR products contain the science and auxiliary data products calibrated to physical units. The RDR products contain the calibrated, geolocated range data as profile measurements of the planetary radius.",
-            "title": "MESSENGER E/V/H MLA 3/4 CDR/RDR DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MESSENGER E/V/H MLA 3/4 CDR/RDR DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1523",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Dubayah, R.O., A. Swatantran, W. Huang, L. Duncanson, H. Tang, K. Johnson, J.O. Dunne, and G.C. Hurtt. 2017. CMS: LiDAR-derived Biomass, Canopy Height and Cover, Sonoma County, California, 2013. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1523",
-            "issued": "2022-05-10",
-            "temporal": "2013-09-01T00:00:00Z/2013-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
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
-            "identifier": "C2389082431-ORNL_CLOUD",
             "description": "This data set provides estimates of above-ground biomass (AGB), canopy height, and percent tree cover at 30-m spatial resolution for Sonoma County, California, USA, for the nominal year 2013. Biomass estimates, megagrams of biomass per hectare (Mg/ha) were generated using a combination of LiDAR data, field plot measurements, and random forest modeling approaches. Estimates of AGB uncertainty are also provided. Maximum canopy height and tree cover were derived from LiDAR data and high-resolution National Agriculture Imagery Program (NAIP) images.",
-            "graphic-preview-description": "Browse Image",
-            "title": "CMS: LiDAR-derived Biomass, Canopy Height and Cover, Sonoma County, California, 2013",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1523_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1523",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1523",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/cms/CMS_LiDAR_Biomass_CanHt_Sonoma/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/cms/CMS_LiDAR_Biomass_CanHt_Sonoma/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_LiDAR_Biomass_CanHt_Sonoma.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_LiDAR_Biomass_CanHt_Sonoma.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1523",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1523",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/CMS_LiDAR_Biomass_CanHt_Sonoma/comp/CMS_LiDAR_Biomass_CanHt_Sonoma.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/CMS_LiDAR_Biomass_CanHt_Sonoma/comp/CMS_LiDAR_Biomass_CanHt_Sonoma.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/CMS_LiDAR_Biomass_CanHt_Sonoma/comp/CMS_LiDAR_Biomass_CanHt_Sonoma_Fig1.png",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/CMS_LiDAR_Biomass_CanHt_Sonoma/comp/CMS_LiDAR_Biomass_CanHt_Sonoma_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1523_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1523_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1523",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1523",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1523_1_fit.png",
+            "identifier": "C2389082431-ORNL_CLOUD",
+            "issued": "2022-05-10",
+            "keyword": [
+                "biosphere",
+                "vegetation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1523",
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
             "spatial": "-123.54 38.1 -122.34 38.86",
+            "temporal": "2013-09-01T00:00:00Z/2013-12-31T23:59:59Z",
             "theme": [
                 "CMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CMS: LiDAR-derived Biomass, Canopy Height and Cover, Sonoma County, California, 2013"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0749-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-05-04T05:17:45.000 to 2015-05-04T09:17:04.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0749-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0749-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0749-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-05-04T05:17:45.000 to 2015-05-04T09:17:04.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0749 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0749 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MRO-M-HIRISE-3-RDR-V1.0",
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
+            "description": "This dataset includes reduced data records from the HiRISE instrument on MRO.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mro-m-hirise-3-rdr-v1.0_4e72-hpwr",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars reconnaissance orbiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MRO-M-HIRISE-3-RDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mro-m-hirise-3-rdr-v1.0_4e72-hpwr",
-            "description": "This dataset includes reduced data records from the HiRISE instrument on MRO.",
-            "title": "MRO MARS HIGH RESOLUTION IMAGE SCIENCE EXPERIMENT RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MRO MARS HIGH RESOLUTION IMAGE SCIENCE EXPERIMENT RDR V1.0"
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
-                "pds",
-                "data"
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
-            "identifier": "NASA-541",
             "description": "PDS Software Release Tools Package (4.9)",
-            "title": "PDS Software Release Tools Package (4.9)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -135516,210 +135496,244 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-541",
+            "issued": "2018-06-25",
+            "keyword": [
+                "tool",
+                "pds",
+                "data"
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
+            "title": "PDS Software Release Tools Package (4.9)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/SECRET/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/SECRET/DATA001.",
-            "issued": "1998-08-02",
-            "temporal": "1998-08-02T16:29:00Z/2023-04-17T00:00:00Z",
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
-            "identifier": "C1633360657-OB_DAAC",
             "description": "Measurements spanning from the California coast to Hawaii in the mid-Pacific Ocean from 1998 to 2006.",
-            "title": "Studies of Ecological and Chemical Responses to Environmental Trends (SECRET)",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FSECRET%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FSECRET%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Secret/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Secret/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360657-OB_DAAC",
+            "issued": "1998-08-02",
+            "keyword": [
+                "ocean optics",
+                "oceans",
+                "ocean temperature",
+                "salinity/density",
+                "earth science",
+                "ocean chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/SECRET/DATA001",
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
+            "temporal": "1998-08-02T16:29:00Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Studies of Ecological and Chemical Responses to Environmental Trends (SECRET)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2049",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Melebari, A., R. Akbar, E. Hodges, D. Mckague, C.S. Ruf, A.R. Silva, M. Moghaddam, R. Shrestha, C.J. Lindsley, T.R. Walker, and B.E. Wilson. 2023. Soil Moisture Profiles and Temperature Data from SoilSCAPE Sites, Version 2. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2049",
-            "issued": "2024-02-13",
-            "temporal": "2021-12-03T20:43:45Z/2023-02-03T17:51:45Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-02-14",
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
-            "identifier": "C2736725173-ORNL_CLOUD",
             "description": "This dataset contains in-situ soil moisture profile and soil temperature data collected at 30-minute intervals at SoilSCAPE (Soil moisture Sensing Controller and oPtimal Estimator) project sites since 2021 in the United States and New Zealand. The SoilSCAPE network has used wireless sensor technology to acquire high temporal resolution soil moisture and temperature data over varying durations since 2011. Since 2021, the SoilSCAPE has upgraded the two previously active sites in Arizona and added several new sites in the United States and New Zealand. These new sites typically use the METER Teros-12 soil moisture sensor. At its maximum, the new network consisted of 57 wireless sensor installations (nodes), with a range of 6 to 8 nodes per site. Each SoilSCAPE site contains multiple wireless end-devices (EDs). Each ED supports up to five soil moisture probes typically installed at 5, 10, 20, and 30 cm below the surface. Sites in Arizona have soil moisture probes installed at up to 75 cm below the surface. Soil conditions (e.g., hard soil or rocks) may have limited sensor placement. The data enables estimation of local-scale soil moisture at high temporal resolution and validation of remote sensing estimates of soil moisture at regional and national (e.g. NASA's Cyclone Global Navigation Satellite System - CYGNSS and Soil Moisture Active Passive - SMAP) scales. The data are provided in NetCDF format.",
-            "graphic-preview-description": "Root zone soil moisture at 5, 15, and 30 cm depth for a node in Lucky Hills, AZ.",
-            "title": "Soil Moisture Profiles and Temperature Data from SoilSCAPE Sites, Version 2",
-            "graphic-preview-file": "https://daac.ornl.gov/LAND_VAL/guides/SoilSCAPE_V2_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2049",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2049",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/eos_land_val/SoilSCAPE_V2/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/eos_land_val/SoilSCAPE_V2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LAND_VAL/guides/SoilSCAPE_V2.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LAND_VAL/guides/SoilSCAPE_V2.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2049",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2049",
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
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/eos_land_val/SoilSCAPE_V2/comp/SoilSCAPE_V2.pdf",
-                    "description": "Soil Moisture Profiles and Temperature Data from SoilSCAPE Sites, Version 2: SoilSCAPE_V2.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Soil Moisture Profiles and Temperature Data from SoilSCAPE Sites, Version 2: SoilSCAPE_V2.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/eos_land_val/SoilSCAPE_V2/comp/SoilSCAPE_V2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/LAND_VAL/guides/SoilSCAPE_V2_Fig1.png",
-                    "description": "Root zone soil moisture at 5, 15, and 30 cm depth for a node in Lucky Hills, AZ.",
                     "@type": "dcat:Distribution",
+                    "description": "Root zone soil moisture at 5, 15, and 30 cm depth for a node in Lucky Hills, AZ.",
+                    "downloadURL": "https://daac.ornl.gov/LAND_VAL/guides/SoilSCAPE_V2_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Root zone soil moisture at 5, 15, and 30 cm depth for a node in Lucky Hills, AZ.",
+            "graphic-preview-file": "https://daac.ornl.gov/LAND_VAL/guides/SoilSCAPE_V2_Fig1.png",
+            "identifier": "C2736725173-ORNL_CLOUD",
+            "issued": "2024-02-13",
+            "keyword": [
+                "soils",
+                "land surface",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2049",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-02-14",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-110.05 -36.72 174.62 37.2",
+            "temporal": "2021-12-03T20:43:45Z/2023-02-03T17:51:45Z",
             "theme": [
                 "EOS LAND VAL",
                 "AirMOSS",
                 "Soil",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Soil Moisture Profiles and Temperature Data from SoilSCAPE Sites, Version 2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-RPCMAG-4-EAR1-RESAMPLED-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "2010-07-30 SBN:T.Barnes Updated and DATA_SET_DESCThis dataset contains RESAMPLED DATA of the first Earth Flyby (EAR1). Included are the data of the very Flyby from March 1 until March 7 and the data of the Passive Checkout (PC0) at March 29. (Version 3.0 is the first version archived.)",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-rpcmag-4-ear1-resampled-v3.0_4efu-9rtg",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "unknown",
                 "international rosetta mission",
                 "earth"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-RPCMAG-4-EAR1-RESAMPLED-V3.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-rpcmag-4-ear1-resampled-v3.0_4efu-9rtg",
-            "description": "2010-07-30 SBN:T.Barnes Updated and DATA_SET_DESCThis dataset contains RESAMPLED DATA of the first Earth Flyby (EAR1). Included are the data of the very Flyby from March 1 until March 7 and the data of the Passive Checkout (PC0) at March 29. (Version 3.0 is the first version archived.)",
-            "title": "ROSETTA-ORBITER EARTH RPCMAG 4 EAR1 RESAMPLED V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER EARTH RPCMAG 4 EAR1 RESAMPLED V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/4eg2-qrs7",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Changes in gravitational force such as that experienced by astronauts during space flight induce a redistribution of fluids from the caudad to the cephalad portion of the body together with an elimination of normal head-to-foot hydrostatic pressure gradients. To assess brain gene profile changes associated with microgravity and fluid shift a large-scale analysis of mRNA expression levels was performed in the brains of 2 weeks control and hindlimb-unloaded (HU) mice using cDNA microarrays. Although to different extent all functional categories displayed significantly regulated genes indicating that considerable transcriptomic alterations are induced by HU. Interestingly the TIC class (transport of small molecules and ions into the cells) had the highest percentage of up-regulated genes while the most down-regulated genes were those of the JAE class (Cell junction Adhesion Extracellular Matrix). TIC genes comprised 16% of those whose expression was altered including sodium channel nonvoltage-gated 1 beta (Scnn1b) glutamate receptor (Grin1) voltage-dependent anion channel 1 (Vdac1) calcium channel beta 3 subunit (Cacnb3) and others. The analysis performed by GeneMAPP revealed several altered protein classes and functional pathways such as blood coagulation and immune response learning and memory ion channels and cell junction. In particular data indicate that HU causes an alteration in hemostasis which resolves in a shift toward a more hyper-coagulative state with an increased risk of venous thrombosis. Furthermore HU treatment seems to impact on key steps of synaptic plasticity and learning processes. We used brains of four control (C1 C2 C3 C4) and four tail-suspended hindlimb-unloaded (E1 E2 E3 E4) mice to ensure statistical relevance of the study. 60 ug of total RNA extracted in TRIzol from each brain was reversed transcribed into labeled cDNAs using fluorescent Cy5 or Cy3-dUTP (Amersham Biosciences NJ). Differently labeled cDNAs obtained from a pair of biological replicas were co-hybridized overnight at 50C with a microscope slide spotted with ~ 27,000 mouse cDNA sequences produced by the Microarray Core Facility of the Albert Einstein College of Medicine in the  xef xbf xbdmultiple yellow xef xbf xbd design (i.e.: C1C2 C3C4 E1E2 E3E4) described in Iacobas DA Fan C Iacobas S et al. Transcriptomic changes in developing kidney exposed to chronic hypoxia. Biochem Biophys Res Commun. 2006 349(1):329-38).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-32",
+                    "mediaType": "text/html",
+                    "title": "Effect of microgravity on brain gene expression in mice"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-32_4eg2-qrs7",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "image_aquisition",
                 "nucleic_acid_extraction",
@@ -135742,78 +135756,42 @@
                 "labeling",
                 "p-gse12312-1"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/4eg2-qrs7",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-32_4eg2-qrs7",
-            "description": "Changes in gravitational force such as that experienced by astronauts during space flight induce a redistribution of fluids from the caudad to the cephalad portion of the body together with an elimination of normal head-to-foot hydrostatic pressure gradients. To assess brain gene profile changes associated with microgravity and fluid shift a large-scale analysis of mRNA expression levels was performed in the brains of 2 weeks control and hindlimb-unloaded (HU) mice using cDNA microarrays. Although to different extent all functional categories displayed significantly regulated genes indicating that considerable transcriptomic alterations are induced by HU. Interestingly the TIC class (transport of small molecules and ions into the cells) had the highest percentage of up-regulated genes while the most down-regulated genes were those of the JAE class (Cell junction Adhesion Extracellular Matrix). TIC genes comprised 16% of those whose expression was altered including sodium channel nonvoltage-gated 1 beta (Scnn1b) glutamate receptor (Grin1) voltage-dependent anion channel 1 (Vdac1) calcium channel beta 3 subunit (Cacnb3) and others. The analysis performed by GeneMAPP revealed several altered protein classes and functional pathways such as blood coagulation and immune response learning and memory ion channels and cell junction. In particular data indicate that HU causes an alteration in hemostasis which resolves in a shift toward a more hyper-coagulative state with an increased risk of venous thrombosis. Furthermore HU treatment seems to impact on key steps of synaptic plasticity and learning processes. We used brains of four control (C1 C2 C3 C4) and four tail-suspended hindlimb-unloaded (E1 E2 E3 E4) mice to ensure statistical relevance of the study. 60 ug of total RNA extracted in TRIzol from each brain was reversed transcribed into labeled cDNAs using fluorescent Cy5 or Cy3-dUTP (Amersham Biosciences NJ). Differently labeled cDNAs obtained from a pair of biological replicas were co-hybridized overnight at 50C with a microscope slide spotted with ~ 27,000 mouse cDNA sequences produced by the Microarray Core Facility of the Albert Einstein College of Medicine in the  xef xbf xbdmultiple yellow xef xbf xbd design (i.e.: C1C2 C3C4 E1E2 E3E4) described in Iacobas DA Fan C Iacobas S et al. Transcriptomic changes in developing kidney exposed to chronic hypoxia. Biochem Biophys Res Commun. 2006 349(1):329-38).",
-            "title": "Effect of microgravity on brain gene expression in mice",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-32",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Effect of microgravity on brain gene expression in mice"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Effect of microgravity on brain gene expression in mice"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA/3302",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Santee, M., Livesey, N., Read, W., and Fuller, R.. 2020-04-20. ML3DZCH3CL. Version 004. MLS/Aura Level 3 Daily Binned Methyl Chloride (CH3Cl) Mixing Ratio on Zonal and Similar Grids V004. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA/3302. https://disc.gsfc.nasa.gov/datacollection/ML3DZCH3CL_004.html. Digital Science Data.",
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
-            "identifier": "C1725334314-GES_DISC",
-            "description": "ML3DZCH3CL is the EOS Aura Microwave Limb Sounder (MLS) daily binned on zonal and assorted vertical grids product for methyl chloride (CH3Cl) derived from radiances measured by the 640 GHz radiometer. The data version is 4.2. Data coverage is from August 2, 2004 to current. Spatial coverage is near-global (-82 to +82 degrees latitude) at 4 degree latitude zonal increments. The recommended useful vertical range is between 147 and 4.64 hPa, and the vertical resolution ranges between 4-6 km in the lower stratosphere and 8-10 km above 14 hPa. Users of the ML3DZCH3CL data product should read chapter 4 and section 3.3 of the EOS MLS Level 2 Version 4 Quality Document for more information.\n\nThe data files contain one year of data and are archived in the netCDF4 format, which is also compatible with HDF5 readers and tools. Each file contains four group objects: lat vs pressure zonal mean, lat vs \"potential temperature\" zonal mean, \"equivalent latitude\" vs \"potential temperature\" zonal mean, and vortex average vs \"potential temperature\". Each group has a set of data (average, min, max, std dev, rms) and geolocation fields, grid attributes, and metadata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML3DZCH3CL",
             "creator": "Santee, M., Livesey, N., Read, W., and Fuller, R.",
-            "title": "MLS/Aura Level 3 Daily Binned Methyl Chloride (CH3Cl) Mixing Ratio on Zonal and Similar Grids V004 (ML3DZCH3CL) at GES DISC",
```

